# 1. Fundamentos de los sistemas operativos en red

## 1.1 De un equipo autónomo a un servicio compartido

Un sistema operativo monopuesto administra CPU, memoria, procesos y dispositivos de un equipo. Un sistema en red añade coordinación entre máquinas: identidades compartidas, nombres, recursos remotos, políticas y disponibilidad. Un directorio no elimina las cuentas locales; añade otro ámbito de identidad. `CLI01\ana` y `AULA\ana` pueden llamarse igual y representar principales de seguridad diferentes.

Un grupo de trabajo conserva bases de cuentas independientes. Sirve para pocos equipos, pero la baja de una persona debe repetirse en cada servidor. Un dominio centraliza identidad y políticas; reduce esa repetición a cambio de depender de controladores, DNS, hora y procedimientos de recuperación. Centralización no significa conceder administrador de dominio a todo el personal técnico.

Define primero las funciones del servidor: directorio, archivos, impresión, aplicaciones, actualización o copia. Una VM que concentra todas las funciones dificulta el diagnóstico y amplía el impacto de una avería. En el aula puede haber pocos recursos, pero los límites lógicos deben quedar escritos. El controlador del directorio tiene un nivel de confianza distinto al de un servidor de archivos usado por usuarios.

## 1.2 Identidad, autenticación y autorización

**Identificación** es declarar una identidad. **Autenticación** es aportar prueba suficiente para vincular una sesión a esa identidad. **Autorización** es decidir sus acciones sobre un recurso. **Auditoría** permite reconstruir quién intentó o realizó una operación. Un inicio de sesión correcto seguido de un «acceso denegado» suele indicar un problema de autorización, no una contraseña incorrecta.

En Linux las identidades de archivos se almacenan como UID y GID numéricos. `/etc/passwd` describe cuentas y su shell; las contraseñas locales se representan mediante verificadores protegidos, normalmente en `/etc/shadow`. Cambiar el nombre visible de una cuenta no cambia automáticamente todos los identificadores de archivos. Reutilizar un UID tras una baja puede otorgar acceso a archivos antiguos si no se revisa su propiedad.

Windows utiliza SID para identificar principales. Las ACL contienen referencias a SID y derechos, no sólo el texto del nombre de usuario. Borrar y recrear `ana` no genera la misma identidad. Por eso no se resuelven fallos de permisos borrando cuentas a ciegas. El token de acceso se crea al iniciar sesión; una pertenencia a grupo recién modificada puede requerir cerrar sesión y abrir una nueva para reflejarse.

En un Samba independiente existen cuentas Unix y una base de autenticación Samba. Crear la cuenta Unix no la habilita automáticamente para SMB. Las prácticas usan esta separación para explicar qué base valida la contraseña y qué identidad controla el acceso al archivo. No se escriben contraseñas en los comandos, porque acabarían en historiales, capturas o registros.

## 1.3 Directorios y Active Directory

AD DS es un servicio de directorio que almacena objetos y sus relaciones: usuarios, grupos, equipos, OU y políticas asociadas. LDAP es un protocolo para consultar o modificar directorios; no es sinónimo de Active Directory. Kerberos se utiliza para autenticación de dominio. DNS permite localizar servicios mediante registros específicos, incluidos SRV. SYSVOL distribuye contenido de directivas y scripts entre controladores.

Un **bosque** establece un ámbito de esquema, configuración y confianza del directorio. Un **dominio** organiza identidades y replicación en ese bosque. Una **OU** es un contenedor administrativo al que pueden vincularse GPO y delegarse tareas; no es un grupo de seguridad. Un grupo sirve para agrupar principales y asignar permisos. Crear una OU «Ventas» no concede acceso a una carpeta «Ventas».

Una topología con dos controladores puede tolerar la pérdida de uno si DNS y los clientes están bien configurados. Dos controladores en el mismo anfitrión, disco y suministro eléctrico comparten riesgos importantes. La replicación no equivale a copia: una eliminación o configuración incorrecta puede replicarse correctamente a todos.

El nombre DNS del laboratorio es `ad.aula.test`; `AULA` es el nombre corto NetBIOS. Un sufijo UPN define nombres de inicio como `ana@ad.aula.test`. No se debe escoger un dominio público ajeno ni inventar un sufijo que entre en conflicto con servicios reales. Para producción debe existir un diseño de nombres aprobado, revisado antes de promover el primer controlador.

## 1.4 DNS y hora como dependencias

Un cliente de dominio debe consultar un DNS que conozca el dominio y sus registros SRV. Poner como DNS alternativo un resolver público no añade redundancia del dominio: ese resolver no conoce el directorio privado. La salida a Internet se resuelve mediante reenviadores del DNS del dominio o mediante una arquitectura que mantenga su resolución interna.

DNS permite encontrar al controlador, pero Kerberos también exige coherencia temporal. La tolerancia real depende de la política del dominio; no se trata como un margen para mantener relojes desajustados. En un dominio se utiliza una jerarquía de tiempo coherente y se revisa la fuente del emulador PDC. Las VM pueden recibir hora tanto del hipervisor como del sistema invitado: hay que conocer el mecanismo y evitar saltos inesperados.

Un error «no se encuentra el dominio» no se diagnostica primero cambiando permisos. Se comprueba IP, máscara, rutas, DNS configurado, consulta de SRV y hora. Una entrada manual en `hosts` puede resolver el nombre de un servidor, pero no sustituye todos los registros de localización de AD.

## 1.5 Permisos POSIX, ACL y acceso remoto

Los permisos POSIX básicos separan propietario, grupo y otros. En un archivo, `r` permite leer datos, `w` modificarlos y `x` ejecutarlos. En un directorio, `r` permite enumerar nombres; `x`, atravesarlo; `w` junto con `x`, crear o eliminar entradas sujeto a otras restricciones. Tener lectura sobre un archivo no basta si falta travesía en un directorio padre.

El bit setgid en un directorio favorece que las nuevas entradas hereden su grupo. No concede por sí solo escritura ni asegura todos los permisos. Una ACL por defecto establece entradas heredadas por nuevas creaciones, mientras que la ACL de acceso rige el objeto actual. La máscara de una ACL limita los derechos efectivos de grupos y de usuarios nombrados; `getfacl` puede mostrar un permiso solicitado y otro efectivo.

Con Samba independiente se combinan controles de la sesión SMB, restricciones del recurso y permisos del sistema de archivos. Si Samba acepta el inicio de sesión pero el usuario Unix no puede escribir en la ruta, el cliente no obtiene escritura por añadir `read only = no`. `chmod 777` oculta el diseño defectuoso y permite modificaciones que no estaban autorizadas.

En Windows conviene separar permisos del recurso compartido y ACL NTFS. El acceso por SMB debe superar ambos controles; el acceso local no pasa por la ACL del recurso compartido. Las entradas de denegación, herencia, propietario y grupos complican el cálculo real. Usa «Acceso efectivo» y pruebas con cuentas de usuario, no la cuenta administradora que creó la carpeta.

## 1.6 Grupos y delegación: AGDLP

Un patrón útil en un dominio es **Accounts → Global groups → Domain Local groups → Permissions**. Las personas pertenecen a grupos globales que representan funciones; esos grupos entran en grupos locales de dominio que representan permisos sobre recursos. La ACL se asigna al grupo de recurso. El patrón evita añadir personas directamente a cada carpeta.

Ejemplo: `ana` pertenece a `GG_Soporte`; éste pertenece a `DL_Manuales_RW`; el grupo local de dominio recibe modificación sobre `D:\Datos\Manuales`. Para dar sólo lectura a auditoría se crea otro grupo de recurso. La organización puede necesitar patrones más complejos entre varios dominios, pero no hace falta introducirlos antes de entender el caso simple.

Delegar restablecimiento de contraseñas sobre una OU de pruebas no exige hacer miembro de Domain Admins al alumno. Una delegación debe especificar contenedor, tipos de objeto y acciones. Se prueba una acción permitida y otra que quede fuera de su ámbito. Separar cuenta cotidiana y cuenta de administración permite evitar que un navegador con una sesión normal tenga privilegios de dominio.

## 1.7 Disponibilidad, capacidad y cambios

La disponibilidad depende de energía, almacenamiento, red, identidades y aplicaciones. RAID puede mantener servicio tras algunos fallos de disco, pero no evita borrados, ransomware, errores lógicos o pérdida del equipo. Una instantánea facilita volver atrás en un laboratorio; no constituye por sí sola una copia independiente ni una estrategia de recuperación de AD.

Antes de un cambio registra objetivo, estado actual, copia, ventana, prueba de aceptación y mecanismo de reversión. Después registra lo observado y las diferencias. Repetir comandos sin saber si ya se ejecutaron puede crear objetos duplicados o cambiar permisos. Una guía reproducible distingue comprobación de modificación y explica los supuestos de cada bloque.

Para dimensionar observa RAM disponible, presión de memoria, latencia de disco, crecimiento, CPU y tráfico en horas de uso. Una CPU al 15 % no prueba que el servicio vaya bien si el almacenamiento está saturado. La medición debe relacionarse con una operación de usuario: abrir un archivo, iniciar sesión o aplicar una política.

## 1.8 Diseño mínimo de este módulo

| Equipo | Rol | Identidad y DNS | Dirección LAB |
| --- | --- | --- | --- |
| `srv01` | Debian 13, Samba independiente | Cuentas locales; ámbito `aula.test` | `192.168.56.10/24` |
| `dc01` | Windows Server 2025, AD DS y DNS | Dominio `ad.aula.test` | `192.168.56.11/24` |
| `cli01` | Windows 11 Pro | Primero local; después unido al dominio | `192.168.56.20/24` |

Las prácticas son escenarios distintos. El DNS que use `cli01` en el escenario AD será `192.168.56.11`. El BIND de `srv01` pertenece al escenario de Servicios en red; no se reemplaza silenciosamente. Para visitar servicios `aula.test` desde el dominio se necesitará resolución apropiada, por ejemplo un reenviador condicional bien diseñado. No es necesario añadirlo para las prácticas de este módulo.

## Referencias para ampliar

- [Debian Reference: autenticación y control de acceso](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html).
- [Manual oficial de smb.conf](https://www.samba.org/samba/docs/current/man-html/smb.conf.5.html).
- [Microsoft Learn: conceptos y despliegue de AD DS](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/active-directory-domain-services-overview).
- [Microsoft Learn: grupos de seguridad de Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups).
- [Microsoft Learn: directiva de grupo](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview).

Las referencias documentan los productos; los ejemplos y la organización pedagógica de esta guía son propios. Consulta la ayuda instalada para la versión exacta antes de automatizar un despliegue.
