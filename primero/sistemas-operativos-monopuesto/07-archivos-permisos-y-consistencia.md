# 07 · Archivos, permisos efectivos y consistencia

[Índice](README.md) · [Administración básica](02-guia-tecnica.md)

## 1. Una ruta es una búsqueda, no sólo un nombre

Cuando una aplicación abre `/srv/documentos/informe.txt`, el sistema resuelve cada componente de la ruta hasta localizar el objeto. Necesita atravesar los directorios y después solicitar derechos sobre el archivo. Tener lectura en el archivo final no ayuda si una carpeta padre impide la búsqueda. Una comprobación de permisos que sólo muestra la última línea deja fuera parte del problema.

En Linux, `namei -l /ruta/al/archivo` permite observar componentes y permisos de un trayecto, si el comando está disponible en `util-linux`. `stat` muestra metadatos del objeto y `getfacl` sus ACL cuando procede. Distingue también la identidad que intenta acceder: proceso interactivo, servicio, tarea programada o usuario elevado. Tu terminal puede tener derechos que el servicio no tiene.

Las rutas relativas dependen del directorio de trabajo. Un script que abre `datos.csv` puede funcionar desde su carpeta y fallar al ejecutarse mediante un programador. La solución consiste en definir el contrato de rutas y verificarlo, no en conceder permisos globales o ejecutar siempre como administrador. La localización correcta del objeto y la autorización son comprobaciones separadas.

## 2. Inodos y enlaces duros

En un sistema de archivos UNIX típico, una entrada de directorio relaciona un nombre con un inodo que conserva metadatos y referencias al contenido. Dos enlaces duros pueden nombrar el mismo objeto. Cambiar el contenido mediante uno se observa por el otro; borrar uno de los nombres no elimina inmediatamente el contenido si sigue existiendo otra referencia relevante.

Una práctica en una carpeta nueva de tu cuenta muestra la relación sin privilegios:

```bash
mkdir -p "$HOME/smr-enlaces"
cd "$HOME/smr-enlaces"
printf '%s\n' 'Texto sintético' > original.txt
ln -- original.txt segundo-nombre.txt
ls -li -- original.txt segundo-nombre.txt
stat -- original.txt segundo-nombre.txt
```

Antes de ejecutarla comprueba que no existen archivos con esos nombres que debas conservar. El mismo número de inodo, dentro del mismo sistema de archivos, y el contador de enlaces permiten explicar por qué no son dos copias independientes. No uses enlaces duros como copia de seguridad de un archivo que luego modificarás: ambos nombres siguen apuntando al mismo contenido.

Un enlace duro ordinario no cruza sistemas de archivos y no funciona como un acceso directo a cualquier ruta remota. La relación se interpreta dentro del dispositivo y espacio de nombres correspondiente; números de inodo iguales en sistemas distintos no demuestran que sea el mismo archivo.

## 3. Enlaces simbólicos y resolución

Un enlace simbólico contiene una referencia que se resuelve como ruta. Puede quedar colgante si desaparece el destino, y su existencia no garantiza que el usuario pueda acceder al objeto final. Una ruta relativa dentro del enlace se interpreta respecto al lugar donde está el enlace, no respecto al directorio desde el que invocas cualquier aplicación.

Continúa la práctica anterior:

```bash
ln -s -- original.txt referencia.txt
ls -l -- referencia.txt
readlink -- referencia.txt
```

Si renombras el original conservando sólo el otro enlace duro, el simbólico que contiene `original.txt` puede dejar de resolver mientras el enlace duro restante sigue funcionando. Haz el cambio sólo con esos archivos sintéticos y documenta la diferencia. No modifiques enlaces del sistema como experimento.

En automatización, decidir si seguir enlaces forma parte del contrato. Un inventario que pretende quedarse en un árbol no debe recorrer accidentalmente un enlace hacia datos externos. Incluso comprobar la ruta canónica antes de operar no elimina todas las carreras si otros actores pueden cambiar el árbol entre comprobación y uso; en una práctica limita el ámbito a una carpeta controlada por la misma cuenta y explica esa limitación.

## 4. Permisos de archivo y de directorio

La lectura de un archivo permite recuperar contenido; la escritura permite modificarlo según condiciones; la ejecución tiene significado para programas y para la búsqueda de directorios. En un directorio, lectura permite enumerar nombres, ejecución permite atravesar y acceder a objetos conocidos y escritura participa en creación o eliminación de entradas. No traslades directamente el significado de `rwx` de archivo a carpeta.

Eliminar un nombre es una modificación del directorio. Un usuario puede no tener escritura sobre el contenido de un archivo y aun así poder borrar su entrada si el directorio y las reglas aplicables lo permiten. Por eso «archivo de sólo lectura» no equivale a protección universal contra borrado. Los controles de aplicación, propietario, directorio y políticas tienen que alinearse con el requisito.

El bit sticky añade restricciones a eliminación y renombrado en ciertos directorios compartidos, como el uso típico de `/tmp`; no concede confidencialidad de lectura. El bit setgid en una carpeta ayuda a mantener grupo en nuevas entradas, pero no obliga a que cada aplicación conceda siempre el mismo conjunto de permisos. La herencia debe estudiarse junto a ACL por defecto y modo solicitado al crear.

## 5. ACL POSIX y máscara efectiva

Las ACL amplían las entradas básicas con usuarios y grupos nombrados. La máscara limita el conjunto de derechos de la clase de grupo y de las entradas nombradas a las que corresponde; no limita de la misma forma al propietario ni a `other`. Para interpretar una entrada necesitas leer también la máscara y el algoritmo de selección de identidad.

No imagines que el sistema suma indiscriminadamente propietario, grupo y otros hasta encontrar la combinación más permisiva. Si coincide la entrada de propietario se aplica esa clase; existen después reglas para usuario nombrado y grupos. El manual de `acl(5)` describe el algoritmo completo. Esta distinción explica por qué un permiso aparentemente presente puede no formar parte del acceso efectivo.

Ejemplo de salida conceptual:

```text
user::rw-
user:nobody:rw-           #effective:r--
group::---
mask::r--
other::---
```

La cuenta nombrada no recibe escritura porque su `rw-` queda limitada por `r--`. El comentario `effective` ayuda a detectar el problema. Cambiar la máscara puede ampliar también otras entradas, así que no se hace a ciegas. Antes de modificar conserva la ACL con rutas absolutas y revisa el alcance.

## 6. Práctica controlada de máscara

Esta práctica modifica sólo una carpeta nueva de la VM, requiere `acl` y una cuenta `nobody` existente. Comprueba primero `getent passwd nobody`. Si `/srv/smr-som-acl` ya existe, detente y elige otra ruta acordada; no reutilices contenido anterior. No se utiliza para recursos reales del centro.

```bash
sudo install -d -o root -g root -m 0711 /srv/smr-som-acl
printf '%s\n' 'Dato sintético de ACL' | sudo tee /srv/smr-som-acl/dato.txt >/dev/null
sudo chmod 0600 /srv/smr-som-acl/dato.txt
sudo setfacl -m u:nobody:rw-,m::r-- /srv/smr-som-acl/dato.txt
getfacl /srv/smr-som-acl/dato.txt
sudo -u nobody cat /srv/smr-som-acl/dato.txt
sudo -u nobody sh -c 'printf "%s\n" "Cambio de prueba" >> "$1"' sh /srv/smr-som-acl/dato.txt
```

La lectura debe permitirse y la escritura debe denegarse con esta configuración. El directorio permite atravesar a la identidad de prueba, de forma que la denegación buscada está en el archivo. Confirma el resultado real: si cambiaste la ruta, ACL o usuario, debes volver a justificarlo. El fallo de escritura es el resultado esperado de la prueba negativa.

Exporta antes de una modificación adicional con `sudo getfacl -p /srv/smr-som-acl/dato.txt > acl-antes.txt`. Revisa la copia y utiliza `sudo setfacl --test --restore=acl-antes.txt` como simulación antes de una restauración autorizada. La copia ACL no conserva los datos del archivo. La retirada final elimina sólo los objetos sintéticos de la práctica mediante el procedimiento acordado, después de inspeccionar su contenido.

## 7. NTFS: identidad, token y herencia

En Windows, los permisos se aplican a identidades de seguridad y grupos presentes en el token utilizado para la operación. Pertenecer a un grupo administrativo no significa que toda aplicación esté ejecutándose con token elevado. Una tarea programada, un servicio y una ventana interactiva pueden usar identidades o contextos diferentes incluso en el mismo equipo.

La DACL contiene entradas que autorizan o deniegan derechos, con reglas de herencia y orden. No reduzcas el modelo a «denegar siempre gana»: para explicar un acceso concreto hay que considerar derechos solicitados, entradas aplicables, orden canónico y token. La interfaz de permisos avanzados y acceso efectivo ayuda, pero la prueba con la identidad real sigue siendo necesaria.

Consulta sin cambiar:

```powershell
whoami /user
whoami /groups
Get-Acl -LiteralPath 'C:\SMR-LAB\documento.txt' | Format-List
```

La ruta es un ejemplo de objeto sintético que debes crear previamente. No publiques la lista completa de SID de un entorno real si no es necesaria. Al copiar o mover archivos, el resultado de permisos puede depender de herramienta, volumen, herencia y opciones. Antes de una migración, ensaya con un árbol pequeño y verifica propietario, ACL y funcionamiento desde una cuenta de lectura y otra de escritura.

## 8. Espacio, inodos y archivos todavía abiertos

`df` informa del uso del sistema de archivos; `du` suma contenido accesible según sus opciones y el árbol recorrido. Pueden diferir por archivos abiertos que ya no tienen nombre, instantáneas, reservas, metadatos, montajes y permisos. No elimines más archivos sólo porque ambas cifras no coinciden. Investiga qué medida ofrece cada herramienta.

En Linux, `df -hT` y `df -i` permiten distinguir capacidad en bytes e inodos en sistemas que los exponen así. Un gran número de archivos pequeños puede agotar entradas disponibles antes de llenar la capacidad de datos. NTFS y otros sistemas tienen modelos distintos; no se traslada literalmente el mismo contador a todos los formatos.

Un proceso puede mantener abierto un archivo cuyo nombre se eliminó. El espacio se libera cuando desaparecen las referencias que correspondan. `lsof +L1`, si se instala el paquete `lsof` en el laboratorio y se dispone de privilegios apropiados, ayuda a localizar ese caso. No mates el proceso sin analizar su función: puede ser un servicio importante que requiere rotación o cierre ordenado.

## 9. Marcas de tiempo, escritura y consistencia

`mtime` se relaciona con modificación del contenido; `ctime`, con cambios de estado de metadatos y no con una «fecha de creación» universal UNIX; `atime` registra accesos bajo la política de montaje. La disponibilidad de fecha de nacimiento depende del sistema y herramientas. Un informe forense o de auditoría no se construye suponiendo que todas esas marcas significan lo mismo.

El journaling favorece recuperación de consistencia bajo el diseño del sistema de archivos, pero no equivale a backup ni garantiza que la última edición de la aplicación sobreviva a cualquier corte. La aplicación, la caché del SO, las operaciones de sincronización y el dispositivo participan en la persistencia. Un mensaje «guardado» tiene que interpretarse con el comportamiento concreto de la aplicación y su almacenamiento.

Una escritura atómica de un informe mediante archivo temporal y renombrado puede evitar que otros lean un resultado parcial, siempre dentro de los supuestos del sistema de archivos y volumen. No crea por sí sola un snapshot consistente de los archivos que se estaban leyendo, ni garantiza durabilidad ante pérdida de energía sin mecanismos adicionales. Aprende a distinguir atomicidad, consistencia y persistencia.

## 10. Caso resuelto de permisos y aceptación

Una tarea lee el archivo desde una consola administradora, pero falla al ejecutarse programada. Hipótesis: identidad diferente, directorio de trabajo, ruta de red no disponible en esa sesión o permisos de recorrido. La prueba inicial registra identidad y rutas absolutas desde la tarea, sin imprimir secretos. Después se comprueba la misma operación con el token previsto sobre una carpeta sintética.

No se marca «ejecutar con privilegios más altos» como remedio automático. Si sólo necesita leer un directorio y escribir un informe, concede únicamente esos derechos. La aceptación incluye ejecución programada con el usuario correcto, caso negativo sobre un recurso fuera del alcance, informe válido y conservación de la configuración inicial para revertir.

## Fuentes primarias

- [Debian: ACL y algoritmo de acceso](https://manpages.debian.org/trixie/acl/acl.5.en.html).
- [Debian: setfacl](https://manpages.debian.org/trixie/acl/setfacl.1.en.html).
- [Debian: stat](https://manpages.debian.org/trixie/coreutils/stat.1.en.html).
- [Microsoft: control de acceso](https://learn.microsoft.com/windows/win32/secauthz/access-control).
- [Microsoft: orden de entradas en una DACL](https://learn.microsoft.com/windows/win32/secauthz/order-of-aces-in-a-dacl).
- [GNU Coreutils: enlaces](https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html).
