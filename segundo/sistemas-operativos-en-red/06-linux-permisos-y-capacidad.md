# 6. Linux en red: resolución de identidades, permisos y capacidad

[Índice del módulo](README.md) · [Guía inicial](02-guia-tecnica.md) · [Directorio e identidades](05-directorio-identidades-y-gpo.md)

## 6.1 Una cuenta puede existir en más de una fuente

En un servidor GNU/Linux, las aplicaciones solicitan información sobre usuarios y grupos a través de interfaces del sistema. NSS determina qué fuentes se consultan y en qué orden para determinadas bases: archivos locales, servicios de directorio u otros mecanismos configurados. PAM participa en operaciones de autenticación y gestión de sesión de las aplicaciones que lo utilizan. Son piezas relacionadas, pero editar una de ellas no produce automáticamente una integración de dominio completa.

La consulta `getent passwd ana` pide al sistema que resuelva la entrada mediante las fuentes activas; buscar `ana` directamente en `/etc/passwd` sólo examina el archivo local. Esta diferencia resulta esencial cuando hay LDAP, SSSD o winbind. Una aplicación puede ver un usuario mediante NSS y aun fallar la autenticación; otra puede autenticarlo, pero no resolver correctamente los grupos necesarios para un archivo.

Empieza con consultas en `srv01`, sin cambiar configuración:

```bash
getent passwd ana
getent group soporte
id ana
getent passwd bruno
sed -n '/^passwd:/p; /^group:/p; /^hosts:/p' /etc/nsswitch.conf
```

No publiques listados completos del servidor si no son necesarios. En un entorno con usuarios centralizados, un nombre corto puede colisionar con una cuenta local. Documenta el formato esperado y las reglas de resolución. Crear una cuenta local homónima para «arreglar» la consulta puede ocultar la integración defectuosa y asignar un UID diferente al previsto.

El identificador numérico importa para la propiedad de archivos UNIX. Si restauras datos en un servidor donde el UID antiguo se asignó a otra cuenta, el nombre mostrado puede cambiar sin que cambien los bits de propietario del archivo. Por tanto una migración incluye coherencia de UID/GID o un mapeo explícito y revisado; no basta con copiar nombres visibles. La opción `--numeric-owner` de herramientas de archivo conserva números, pero esa conservación sólo es correcta cuando el diseño de identidades la justifica.

## 6.2 PAM y acceso: entender antes de modificar

PAM organiza pilas de módulos para operaciones como autenticación, comprobación de cuenta, cambio de credenciales y apertura de sesión. Las reglas de control de cada módulo determinan cómo un éxito o fallo influye en el conjunto. Un archivo sintácticamente válido puede producir un bloqueo de acceso si el orden o los controles son incorrectos. Por eso este capítulo no propone reemplazar de forma genérica la configuración de PAM de Debian.

Para un diagnóstico, identifica qué servicio llama a PAM, qué archivo utiliza, qué operación falla y qué registro corresponde. Iniciar una sesión SSH interactiva no es el mismo caso que acceder a Samba con una cuenta cuyo shell es `nologin`. El shell puede impedir una sesión interactiva sin que todos los servicios lo interpreten de forma idéntica. La política se verifica en el servicio real, no mediante suposiciones sobre un campo de `/etc/passwd`.

Antes de probar una integración centralizada, mantén una cuenta administrativa local de emergencia, protegida y comprobada desde consola. Documenta su uso y no la emplees para las tareas ordinarias. Un fallo temporal del directorio puede necesitar mecanismos de continuidad, pero la decisión de permitir credenciales en caché debe valorar revocación, dispositivos perdidos y disponibilidad. «Funciona sin red» no demuestra que la baja de una cuenta se aplique inmediatamente.

En un laboratorio con acceso local, examina los archivos de configuración sin cambiarlos y relaciona las entradas con sus manuales instalados. Si una práctica posterior requiere modificar un módulo, haz una copia, conserva una sesión de consola ya autenticada, prueba una nueva sesión y revierte antes de cerrar el único acceso administrativo. No edites la pila de autenticación de tu equipo personal para seguir un ejemplo pensado para una VM.

## 6.3 Permisos de directorios y recorrido de una ruta

El permiso de ejecución de un directorio permite atravesarlo; el de lectura permite enumerar nombres; el de escritura, junto con condiciones pertinentes, permite alterar entradas. El archivo final puede permitir lectura y aun resultar inaccesible porque un directorio padre impide atravesar la ruta. Para diagnosticar `/srv/samba/manuales/prueba.txt`, examina toda la cadena:

```bash
namei -l /srv/samba/manuales/prueba.txt
getfacl -p /srv/samba/manuales
getfacl -p /srv/samba/manuales/prueba.txt
stat -c '%n %U %G %a %u %g' /srv/samba/manuales/prueba.txt
```

La consulta de un archivo protegido puede necesitar `sudo`; añade elevación sólo para observar lo necesario, sin utilizar el éxito del administrador como prueba del acceso de una cuenta ordinaria. Comprueba el caso de Ana con `sudo -u ana` o una sesión de laboratorio de Ana, y el de Bruno en otro contexto. Una orden ejecutada como root puede saltarse restricciones que sí afectan al usuario.

El bit setgid de un directorio favorece que las entradas nuevas conserven su grupo. La ACL por defecto define reglas heredadas en objetos nuevos, y la máscara limita los permisos efectivos de la clase de grupo, incluidas entradas de usuarios o grupos nombrados. Por ello una ACL puede mostrar `rwx` en una entrada y un comentario de permisos efectivos más limitado. Modificar la máscara para arreglar un usuario puede ampliar también otros accesos y debe revisarse como cambio de política.

Una ACL por defecto no reescribe automáticamente todos los archivos preexistentes. Si unos documentos se crearon antes y otros después de la configuración, pueden presentar resultados diferentes. Una copia de un archivo que conserva metadatos también puede introducir permisos distintos a los esperados por la carpeta destino. La práctica avanzada debe incluir archivos creados, copiados y movidos, explicando qué mecanismo actúa en cada caso y sin asumir reglas idénticas en todos los sistemas de archivos.

## 6.4 Caso trabajado de autorización POSIX

Imagina un directorio de laboratorio para manuales. El grupo `soporte` debe crear y modificar documentos; el grupo `lectores` debe consultar; otras cuentas no deben entrar. El diseño se registra antes de editar:

| Principal | Directorio | Archivo ordinario nuevo | Motivo |
| --- | --- | --- | --- |
| Propietario administrativo | Administración completa | Administración completa | Operación del recurso |
| Grupo soporte | Leer, atravesar y crear | Leer y escribir | Mantener manuales |
| Grupo lectores | Leer y atravesar | Leer | Consulta |
| Resto | Sin acceso | Sin acceso | Mínimo privilegio |

No se aplica esta tabla recursivamente sobre datos ajenos. En una carpeta nueva de práctica, crea los grupos sintéticos si no existen y añade cuentas según la guía inicial. Guarda ACL con `getfacl -Rp`, conserva el inventario y modifica únicamente el árbol del ejercicio. Verifica después la máscara efectiva. Añadir lectores mediante una ACL nombrada evita convertirlos en miembros del grupo de edición.

La evidencia debe incluir una creación por un editor, lectura de ese archivo por un lector, intento de escritura por el lector e intento de entrada por una persona no autorizada. Introduce un segundo editor y comprueba colaboración sobre archivos nuevos. El resultado se recoge con texto y códigos de salida, no sólo con la lista de permisos. Si la lectura funciona pero el guardado de una aplicación falla, comprueba si la aplicación crea un archivo temporal y renombra después: esa operación necesita permisos sobre el directorio, además de los del archivo original.

## 6.5 Samba: conservar un modelo de permisos coherente

El servidor independiente inicial utiliza permisos POSIX y ACL compatibles con su diseño. Samba evalúa además parámetros del recurso, identidad autenticada, grupos y opciones relacionadas con creación y acceso. Un `read only = no` no concede escritura que el sistema de archivos deniega. `valid users` tampoco es una lista completa de permisos sobre cada archivo.

Si se decide usar un modelo de ACL de Windows almacenadas en atributos extendidos, entran en juego módulos VFS y opciones específicas. Ese modelo debe estudiarse en un recurso separado y con su documentación de versión. No añadas `acl_xattr` y opciones copiadas de otro servidor encima del recurso POSIX esperando que todos los mecanismos signifiquen lo mismo. La configuración de ignorar ACL del sistema cambia supuestos sobre accesos locales o por otros protocolos y exige un diseño que los contemple.

Elige y documenta cuál es la interfaz autorizada para administrar permisos. Si una persona cambia ACL desde Windows, otra ejecuta `chmod` recursivo y otra restaura archivos sin atributos extendidos, el resultado puede perder información o contradecir las expectativas de herencia. La copia debe conservar los metadatos que utiliza el modelo elegido y su restauración debe probarlos desde los clientes previstos.

Para aislar un problema, prueba primero el acceso local con el UID/GID efectivo; después autentica a Samba; por último realiza la operación SMB. Si falla ya el primer paso, inspecciona ruta y ACL. Si el acceso local funciona y Samba deniega, revisa configuración efectiva mediante `testparm -s`, pertenencias de la sesión y registros. Si sólo falla Windows, examina credenciales de conexiones existentes y nombre de destino antes de culpar al servidor.

## 6.6 Capacidad: espacio, inodos, cuotas y crecimiento

Un servidor puede quedarse sin capacidad aun cuando el porcentaje de bytes ocupados parezca razonable. Los inodos o metadatos disponibles, el destino real de una ruta, reservas del sistema, cuotas y límites del proceso pueden restringir una operación. Utiliza consultas complementarias:

```bash
findmnt -T /srv/samba/manuales
lsblk -f
df -hT /srv/samba/manuales
df -i /srv/samba/manuales
sudo du -xhd1 /srv/samba 2>/dev/null
```

`findmnt -T` identifica el montaje que contiene la ruta, incluso cuando `/srv` no es un montaje independiente. `du -x` limita el recorrido al mismo sistema de archivos y evita sumar otros montajes de forma inadvertida. Su cálculo requiere tiempo y permisos; en un servidor real se planifica para no añadir una carga excesiva. La diferencia entre `df` y `du` puede tener explicaciones como archivos borrados que un proceso mantiene abiertos, metadatos y acceso parcial del usuario.

Una cuota establece límites para una identidad, grupo o proyecto según el sistema de archivos y las herramientas. No amplía el almacenamiento ni sustituye avisos de crecimiento. Antes de habilitarla identifica tipo de sistema de archivos, soporte, montaje y procedimiento de esa versión. Habilitar opciones de cuota o ejecutar verificaciones sobre un volumen en uso no se enseña como comando universal: el comportamiento depende de ext4, XFS u otra tecnología y de su estado.

Ejemplo de dimensionamiento didáctico: 18 personas generan 150 MiB semanales de documentos durante 30 semanas. El crecimiento estimado es `18 × 150 × 30 = 81.000 MiB`, aproximadamente `79,10 GiB`. Si ya existen 35 GiB, el conjunto llega a 114,10 GiB antes de versiones, temporales y copias. Añadir un margen del 25 % produce unos 142,63 GiB. El margen es una hipótesis de planificación, no una garantía; revisa la tasa real cada periodo y separa la capacidad del backup.

## 6.7 Recursos de servicios con systemd y cgroups

Los límites de recursos pueden impedir que una tarea de laboratorio monopolice la VM. `CPUQuota` expresa una cuota respecto a una CPU, no necesariamente un porcentaje del total de todos los núcleos. Un 50 % permite aproximadamente la mitad del tiempo de una CPU bajo las reglas del controlador, mientras que una VM con varias vCPU tiene una capacidad total distinta. `MemoryHigh` introduce presión de control y `MemoryMax` actúa como límite más estricto; alcanzar límites puede afectar rendimiento o terminar procesos.

Para estudiar controles sin modificar un servicio compartido, se utiliza una unidad transitoria de usuario y una tarea pequeña, de duración limitada. Comprueba antes que el gestor de usuario y el controlador pertinente estén disponibles. No emplees un generador de carga ilimitada ni un bucle que agote toda la memoria. La documentación de la versión instalada y los permisos del gestor determinan qué propiedades se aceptan.

En un servicio existente, empieza observando:

```bash
systemctl show smbd -p MainPID -p ControlGroup -p MemoryCurrent -p TasksCurrent
systemctl cat smbd
systemd-cgls
```

Un valor vacío o no disponible necesita interpretación según contabilidad y versión; no se convierte en cero consumo. Si decides aplicar un drop-in, guarda la configuración, limita el cambio al clon de prueba, valida la unidad, recarga configuración y reinicia sólo cuando proceda. `systemctl revert` puede eliminar todos los cambios locales de una unidad y no debe usarse a ciegas: retira el archivo concreto creado por la práctica y documenta el retorno.

## 6.8 Procedimiento de aceptación de capacidad y permisos

Una entrega avanzada relaciona ruta lógica, montaje físico o virtual, propietario numérico, grupos, ACL, recurso Samba y operación del cliente. Incluye una previsión de crecimiento con unidades y supuestos, un umbral de aviso y una prueba de restauración de metadatos. Si utilizas un límite de recursos, registra valor, alcance y síntoma esperado, y demuestra que la operación normal sigue cumpliéndose.

El criterio de cierre es que una segunda persona pueda responder por qué una operación se permite, qué recurso limita el rendimiento y cómo recuperar el estado anterior. No basta con que un comando aislado devuelva éxito: la autorización y la capacidad forman parte del comportamiento que recibe el usuario.

## Referencias primarias

- [Debian Reference: autenticación y control de acceso](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html).
- [Manuales Debian: nsswitch.conf](https://manpages.debian.org/trixie/manpages/nsswitch.conf.5.en.html).
- [Manuales Debian: getfacl](https://manpages.debian.org/trixie/acl/getfacl.1.en.html) y [setfacl](https://manpages.debian.org/trixie/acl/setfacl.1.en.html).
- [Samba: documentación y manuales por versión](https://www.samba.org/samba/docs/).
- [systemd: control de recursos](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html).
- [systemd: configuración de unidades](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html).
