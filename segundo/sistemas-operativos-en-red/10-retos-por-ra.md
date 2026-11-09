# Retos prácticos por resultado de aprendizaje · 0224

[Mapa de RA y criterios](09-alineacion-ra.md) · [Índice](README.md) · [Trazabilidad JSON](alineacion-ra.json)

## Preparación del dossier

Estos seis retos desarrollan las actividades que identifica el JSON del módulo. Los enunciados oficiales y las letras de los 48 CE se encuentran en el [mapa de alineación](09-alineacion-ra.md); los procedimientos, casos y comprobaciones de esta guía son una propuesta didáctica. Prepara una ficha por RA con estado inicial, actuación, resultado real, criterio al que responde y recuperación. Una captura de un asistente no demuestra por sí sola el funcionamiento del servicio desde un cliente.

El escenario base utiliza Debian 13 en `srv01` (`192.168.56.10/24`), Windows Server 2025 en `dc01` (`.11`) y un cliente Windows 11 Pro en `cli01` (`.20`). La LAB es host-only o interna, sin gateway. El acceso de actualización mediante NAT se planifica por separado y se retira del controlador antes de promoverlo según la guía técnica. No hay SMB, RDP, LDAP o Kerberos publicados a Internet.

Dos extensiones requieren más recursos: `dc02` (`.12`) representa un bosque independiente `colab.test`; `fs01` (`.13`) es un servidor miembro de archivos y `cli02` (`.21`) un segundo cliente para comprobar perfiles. Registra estas direcciones antes de utilizarlas: no sustituyen a `.30`, reservada al DNS secundario de Servicios, ni a `.50`, reserva DHCP. Puedes encender los clientes por turnos, pero cada uno conserva identidad y configuración propias. Si no dispones del producto, recurso físico o participante necesario, conserva el diseño y marca la ejecución correspondiente como pendiente.

Las instalaciones usan licencias o evaluaciones legítimas y plataformas compatibles. Antes de modificar, identifica cuenta, máquina, disco, objeto y medio de retorno. No copies contraseñas, claves de recuperación o ficheros de respuesta con secretos al repositorio. Los resultados descritos son expectativas de laboratorio, no actuaciones ejecutadas al redactar esta guía.

<a id="ra1"></a>
## RA1 · 0224-RA1-A1: instalar un servidor mediante un plan repetible

### Requisitos y selección

Una oficina ficticia necesita archivos compartidos para seis personas y administración desde LAB. Entrega una matriz que relacione arquitectura, CPU, RAM, almacenamiento, firmware virtual, sistema de archivos y soporte con esos usos. Distingue requisitos mínimos del fabricante y dimensionamiento para la carga: cumplir un mínimo no garantiza la experiencia deseada.

Compara tres caminos: instalación interactiva, instalación con respuestas y actualización de una instalación existente. La primera ayuda a observar decisiones; la segunda facilita repetición; la tercera conserva estado y exige estudiar compatibilidad y retorno. Selecciona dos ensayos sobre VMs nuevas, sin discos físicos ni carpetas con datos montadas desde el anfitrión.

Diseña el disco antes del instalador: particiones de arranque, sistema, datos y espacio de crecimiento según el SO. Justifica ext4 o NTFS por los roles, permisos y recuperación previstos. Al seleccionar el destino comprueba tamaño y pertenencia a la VM; no añadas a una guía un comando genérico que formatee el primer disco encontrado. Documenta después el resultado con herramientas de consulta, como `lsblk -f`, `findmnt -T /srv` o `Get-Volume`.

### Ensayo de automatización

Para Debian, consulta el apéndice de instalación automatizada de la versión 13. Prepara un fichero de respuestas de alcance limitado: idioma, teclado, zona y selección de componentes. Mantén la decisión de almacenamiento bajo control explícito y las credenciales fuera de ese fichero. El ejemplo siguiente muestra opciones de selección; no pretende constituir un instalador completo:

```text
d-i debian-installer/locale string es_ES.UTF-8
d-i keyboard-configuration/xkb-keymap select es
d-i time/zone string Europe/Madrid
tasksel tasksel/first multiselect standard
d-i pkgsel/include string openssh-server
```

Sirve el fichero únicamente por un medio o red del laboratorio y aplica el mecanismo de carga indicado por el manual del instalador utilizado. Ejecuta primero sobre una VM nueva, sin unidades ajenas conectadas, con consola y posibilidad de abandonar. Registra qué preguntas se resolvieron automáticamente y cuáles permanecieron interactivas. Una automatización parcial debe identificarse como tal; no equivale a haber ensayado una instalación completamente desatendida. Si el centro exige esta última, completa el fichero y su prueba bajo sus condiciones de almacenamiento y custodia de credenciales.

Compara la selección mínima de paquetes con los roles realmente necesarios. SSH, Samba o un directorio tienen dependencias y superficies distintas. No instales BIND y un DNS de controlador intentando ocupar la misma IP y puerto. Tras instalar, inventaría versiones, cuentas administrativas y servicios; ajusta preferencias personales sin modificar controles del servidor para hacer más cómoda una captura.

### Actualización y aceptación

Prepara una actualización desde repositorios oficiales o un canal admitido por el fabricante, con estado previo, copia y pruebas posteriores. En Debian revisa lo que propone `apt`; en Windows registra actualización y reinicios requeridos. No uses únicamente la desaparición de un aviso como evidencia de mantenimiento.

Desde el cliente prueba dirección, nombre y operación de servicio. Un ping puede responder aunque SMB o SSH no funcionen; un proceso puede figurar activo aunque no escuche en LAB. Entrega plan, acta de instalación, respuestas saneadas, inventario de componentes, registro de cambios y matriz cliente/servidor. Acepta el reto cuando las decisiones sean reproducibles y las funciones previstas estén comprobadas. Si el ensayo automatizado falla, preserva el log, identifica la pregunta o dependencia y repite sobre otro destino limpio.

<a id="ra2"></a>
## RA2 · 0224-RA2-A1: ciclo de vida de identidades y perfiles

### Altas, cambios y baja

En una OU exclusiva crea tres cuentas sintéticas: personal de lectura, edición y soporte. Define propiedades, finalidad, fecha de revisión y grupo funcional. Usa herramientas gráficas y consultas PowerShell para mostrar que ambas administran los mismos objetos. No reutilices usuarios reales ni conviertas una cuenta de servicio en administradora para evitar un error de permisos.

Comprueba también la cuenta de `cli01` unido al dominio: nombre, OU, canal y DNS. Distingue objeto de equipo, cuenta de persona y sesión. Documenta grupos locales, globales, universales y locales de dominio, señalando su ámbito y función. Las OU sirven para organización, delegación y GPO; no se utilizan como sustituto de un grupo de autorización.

Aplica un cambio de pertenencia a una cuenta de prueba y ensaya acceso antes y después de renovar su sesión. La lista que muestra una consola no describe necesariamente el token de una conexión SMB antigua. Inspecciona la conexión pertinente y cierra sólo la sesión de laboratorio que necesite renovarse. Para la baja, deshabilita primero la cuenta del ejercicio, identifica recursos y tareas dependientes y conserva el registro; borrar el objeto inmediatamente puede perder trazabilidad o dejar datos sin responsable.

Incluye una ficha de cuentas y grupos integrados: función, privilegios y razón para no usarlos en tareas ordinarias. No los renombres o elimines para obtener una captura diferente. El criterio se evidencia mediante identificación y uso adecuado, no mediante una modificación innecesaria.

### Plan y prueba de perfil móvil

Un perfil reúne configuración de usuario; una carpeta personal y una carpeta redirigida resuelven necesidades distintas. Sincronizar documentos no demuestra itinerancia de perfil. Consulta la aplicabilidad de perfiles móviles a las versiones y compilaciones concretas de Windows del laboratorio; algunos componentes y versiones de perfil no se comparten entre todas las ediciones o actualizaciones.

Para el ensayo prepara `fs01.ad.aula.test`, miembro del dominio y con almacenamiento separado para perfiles, y dos clientes compatibles. Crea un recurso `Perfiles$` con acceso restringido a administradores y al grupo del ejercicio. El sufijo `$` oculta una enumeración habitual del recurso, pero no concede seguridad por sí mismo. Revisa conjuntamente permiso SMB y NTFS.

En NTFS, sigue el diseño del fabricante: SYSTEM y administradores con control previsto, CREATOR OWNER para subcarpetas y archivos, y grupo de usuarios con lectura/listado y creación de carpetas en la raíz según la tabla del procedimiento oficial. La herencia y el ámbito «sólo esta carpeta» son esenciales. Un permiso de compartir amplio para un grupo controlado no elimina las restricciones NTFS; valida que un usuario no pueda leer el perfil de otro.

Asigna a una cuenta de prueba una ruta individual del recurso, por ejemplo `\\fs01.ad.aula.test\Perfiles$\ra2ana`, desde las propiedades o la herramienta de administración del directorio. Evita cambiar a la vez perfil, redirección de carpetas y sincronización: se perdería capacidad para atribuir los resultados. Inicia sesión con `ra2ana` en `cli01`, cambia una preferencia compatible y crea un archivo sintético pequeño; cierra sesión normalmente para permitir actualización. Inicia después en `cli02` y observa qué estado se recupera.

Vuelve al primer cliente y comprueba que una sesión simultánea o un cierre abrupto puede introducir conflictos. No fuerces cortes para provocar pérdida: registra los mecanismos de sincronización, caché y eventos que documenta Windows. Si aparece un perfil temporal, investiga nombre, red, disponibilidad del recurso, permisos, versión y eventos del servicio de perfiles antes de borrar carpetas.

**Aceptación:** ciclo de cuentas y equipos registrado, ámbitos justificados, cambio de pertenencia probado en sesión nueva, diseño de perfiles con prueba de itinerancia y denegación entre usuarios. Si sólo se elaboró el diseño, el componente práctico de perfil permanece pendiente. La retirada restaura la propiedad de perfil de la cuenta del ejercicio antes de eliminar copias o recursos, preservando los datos que procedan.

<a id="ra3"></a>
## RA3 · 0224-RA3-A1: directorio, organización y confianza

### Directorio y administración

Promueve `dc01` en el escenario de la guía técnica y valida DNS, hora, descubrimiento y autenticación antes de crear políticas. Relaciona `ad.aula.test`, un DN como `OU=Laboratorio,DC=ad,DC=aula,DC=test`, un UPN y un grupo: son nombres y objetos de funciones diferentes. Dibuja dominio, bosque, OU, objetos y delegaciones.

Crea una OU para los usuarios de prueba y otra para equipos; delega sólo una tarea limitada a una cuenta de soporte, si el ejercicio la necesita. Comprueba una operación autorizada y otra fuera de alcance. Una GPO vinculada a una OU no debe extenderse por accidente al controlador o a cuentas no incluidas. Conserva consultas, cambio y evidencia desde cliente, no únicamente una captura del editor.

### 0224-RA3-A2: extensión para establecer una confianza real

La extensión utiliza dos bosques aislados: `ad.aula.test` en `.11` y `colab.test` en `dc02/.12`, ambos con sistemas y niveles funcionales compatibles. Antes de promover el segundo comprueba IP, DNS, hora y ausencia de conflictos. El DNS del primer bosque debe poder localizar el segundo y viceversa; configura resolución condicionada de las zonas correspondientes mediante las herramientas de DNS, sin sustituir el DNS del dominio por un servidor público.

Define primero la necesidad con una flecha inequívoca: «usuarios de `colab.test` acceden a un recurso de `ad.aula.test`». En ese caso el dominio que aloja recursos debe confiar en el que contiene esas identidades. La confianza permite una relación de autenticación, pero todavía no otorga permiso al archivo. Registra la dirección elegida y el significado de las opciones del asistente, en lugar de deducirlo sólo de la palabra entrante o saliente sin indicar desde qué lado se observa.

Desde Dominios y confianzas de Active Directory, abre las propiedades del dominio pertinente y crea una nueva confianza. Introduce el nombre DNS del otro bosque, elige el tipo compatible con el diseño y la dirección que permite el flujo requerido. Si el asistente configura ambos extremos, usa credenciales administrativas de laboratorio por el canal interactivo; no se guardan en scripts o capturas. Documenta si la autenticación es de ámbito completo o selectiva y qué autorizaciones adicionales requeriría la segunda.

Valida ambos extremos mediante el asistente y consulta el resultado:

```powershell
Get-ADTrust -Filter * | Select-Object Name, Direction, TrustType, ForestTransitive
```

Esa consulta prueba existencia y propiedades del objeto visible; la aceptación necesita además una operación con identidad del otro dominio. Prepara un archivo del ejercicio, un grupo de permiso del dominio de recursos y una pertenencia compatible que incluya al principal del dominio de cuentas. Otorga lectura al grupo y prueba desde una sesión con la identidad de `colab.test`. Prueba también una cuenta sin pertenencia y la dirección inversa si no fue autorizada: una confianza unidireccional no se convierte en acceso universal.

### Solución razonada y retorno

Si se encuentra el dominio pero falla autenticación, revisa DNS de servicios, hora, configuración de confianza y credencial. Si la identidad se autentica pero el archivo se deniega, investiga autorización y sesión. No recrees el bosque antes de distinguir esos casos. El acta contiene estructura, privilegios utilizados, dirección de confianza, validación y matriz de acceso.

Un diagrama o la definición de confianza no satisfacen por sí solos el establecimiento práctico de 3.c. Si no hay un segundo dominio disponible, marca esa ejecución como pendiente. Para retirar la extensión, elimina primero autorizaciones y pertenencias de prueba, registra las dependencias y retira la confianza en ambos extremos por el procedimiento del producto. No restaures indiscriminadamente instantáneas antiguas de controladores como sustituto del procedimiento de recuperación de AD.

<a id="ra4"></a>
## RA4 · 0224-RA4-A1 y 0224-RA4-A2: recursos e impresión con acceso efectivo

### Carpetas y responsabilidades

Diseña un recurso de lectura y edición con propietario funcional, alcance, usuarios, grupos y copia. Explica la diferencia entre permiso sobre un objeto y derecho o privilegio del sistema. Poder iniciar sesión no concede lectura de un recurso; poder leer un archivo no concede administración del servidor.

Configura el recurso por un asistente gráfico y revisa después la configuración efectiva con herramientas de consulta. En Windows considera SMB y NTFS; en Samba, reglas del recurso, identidad UNIX y ACL. Elige el procedimiento del [capítulo técnico](02-guia-tecnica.md) y conserva un único diseño por escenario, sin combinar valores incompatibles de varios tutoriales.

Prueba lectura, creación, modificación y denegación con archivos nuevos. Registra la cuenta realmente usada y la conexión. Crea una segunda cuenta de rol equivalente para comprobar que el comportamiento procede del grupo y no de un permiso directo residual. Un acceso invitado universal, SMB1 o `chmod 777` no es una solución para un requisito de separación por identidad.

### 0224-RA4-A2: impresora compartida

Inventaría impresora, conectividad, protocolo, controlador y soporte. Usa equipo y cola autorizados. En el escenario Windows instala la función de impresión pertinente y publica una cola limitada a LAB mediante el administrador de impresión. Selecciona un controlador soportado y revisa las restricciones de instalación de controladores; no debilites políticas de seguridad para evitar una solicitud de elevación.

En el cliente añade la cola por el mecanismo admitido y verifica nombre y opciones. Envía una página sintética con identificador de prueba, fecha y origen. Registra trabajo en cola, estado, salida y diferencia entre permiso para imprimir y administración de impresora o documentos. Un PDF virtual permite observar una parte de la cola, pero no acredita la salida física ni los consumibles.

Realiza la comprobación entre dos participantes: una persona prepara el recurso, otra ejecuta las pruebas y ambas revisan desviaciones. Registra aportaciones, dudas y correcciones. Una actividad individual puede demostrar configuración, pero no acredita colaboración grupal por incluir dos nombres en la memoria.

**Aceptación:** matriz aplicada, operación útil desde cliente, identidad ajena denegada y salida de impresión observada cuando se dispone de equipo. La retirada cancela sólo trabajos sintéticos identificados y elimina la cola creada por la práctica si no se necesita; no se borra la cola de otra actividad.

<a id="ra5"></a>
## RA5 · 0224-RA5-A1: observar, mantener y automatizar

### Investigar una lentitud reproducible

Define una operación concreta: leer un conjunto sintético de archivos desde el cliente. Conserva tamaño, número de archivos, tiempo, caché, concurrencia y versión. Recoge métricas de almacenamiento, memoria, CPU y red en el mismo intervalo. La ocupación en porcentaje no equivale a latencia, y una cifra elevada de CPU no demuestra por sí sola que sea la causa de una lentitud.

En Debian consulta `df -hT`, `findmnt -T /srv`, `free -h`, `ip route` y los registros del servicio que interviene. Las herramientas de I/O opcionales se instalan por el canal previsto y se interpretan con su manual. En Windows usa Monitor de rendimiento y Visor de eventos, seleccionando contadores y registros relacionados con la pregunta. Describe qué aporta cada herramienta y qué no demuestra.

Correlaciona un evento de cliente con el servidor mediante hora y zona. Una coincidencia temporal orienta una hipótesis, pero no identifica automáticamente la causa. Propón una prueba que cambie una variable: otro tamaño, otra carga o el mismo acceso local frente a remoto. Evita generar carga elevada fuera de una VM preparada para el ensayo.

### Tarea operativa con fallo visible

Utiliza el [generador de plan](ejemplos/plan-altas-lab.ps1) para estudiar una automatización que no crea objetos, o una tarea de consulta que genere un informe en un directorio del ejercicio. Documenta intérprete, identidad, permisos, ruta de trabajo, salida, código de terminación y programación. Si el objetivo requiere una actuación real, diseña y autoriza esa parte por separado: obtener una propuesta no equivale a aplicar un alta.

Prueba al menos una condición negativa, como CSV mal formado o destino de informe no accesible, con datos ficticios. El error debe ser visible y no dejar un resultado aparentemente correcto. Registra cómo se conserva o sustituye el informe anterior y cómo se retira la programación al terminar.

Prepara también un mantenimiento del servidor: motivo, versión anterior/nueva, copia, dependencias y prueba después. Si necesita reinicio, coordínalo en LAB. Verifica configuración efectiva de NIC, rutas y DNS y su persistencia; un cambio temporal con una herramienta no demuestra configuración persistente en el gestor activo.

**Aceptación:** línea temporal con fuentes, hipótesis comprobable, mantenimiento con retorno y automatización ensayada con éxito y fallo. Un registro vacío no demuestra salud si dejó de producirse. La memoria distingue medidas, interpretación y acciones.

<a id="ra6"></a>
## RA6 · 0224-RA6-A1 y 0224-RA6-A2: integrar Linux y Windows

### Archivos, identidad y metadatos

Parte de un caso de uso que necesite compartir documentos entre ambos sistemas. Justifica protocolo, servidor, cliente, identidad y política de acceso. Un mismo nombre de cuenta no significa el mismo SID, UID o autenticación. Dibuja flujo SMB y relaciona proceso, puerto y permisos.

En `srv01` prepara Samba independiente según la guía técnica, enlazado a LAB y con autenticación. Comprueba sintaxis, servicio y listeners antes de pasar al cliente. Usa Linux y Windows para leer, escribir y verificar un conjunto pequeño; incluye nombres con espacios y caracteres españoles, manteniendo versiones y codificación documentadas. Si una aplicación bloquea un archivo o cambia sus metadatos, registra el comportamiento en lugar de atribuirlo a corrupción sin comprobar.

Comprueba acceso en las direcciones pertinentes para la arquitectura. Si el servidor es Linux y los clientes Linux/Windows, ambos deben usar su recurso; no es necesario abrir además una compartición insegura en cada cliente sólo para obtener una flecha simétrica. La conectividad se demuestra mediante operación de servicio, no sólo ICMP.

### 0224-RA6-A2: impresión heterogénea

Prepara una cola IPP admitida por el dispositivo o un servidor de impresión de laboratorio. En Linux utiliza la configuración de impresoras y, cuando CUPS esté instalado, consulta `lpstat -t`; en Windows añade la impresora mediante el procedimiento IPP o controlador compatible de esa versión. Documenta si la cola se sirve directamente desde el dispositivo, desde Windows o desde CUPS.

Envía el mismo documento sintético desde ambos clientes con un identificador diferente. Comprueba llegada, páginas, orientación, caracteres y permisos de cada trabajo. Si se emplea una cola virtual, describe qué parte se verificó y deja pendiente la impresión física. No equipares que un trabajo desaparezca de la cola con que exista una salida correcta.

### Colaboración, cierre y recuperación

Reparte roles: administración del servidor, prueba Linux, prueba Windows y revisión. Si hay menos participantes, realiza un relevo real y registra qué otra persona pudo repetir. Cada una aporta resultado y contexto; una memoria conjunta no debe ocultar qué pruebas no se realizaron.

La entrega final incluye configuración sanitizada, tabla de identidades, matriz de lectura/escritura/denegación, pruebas de impresión y acta de funcionamiento. Restaura un archivo en otra ruta y comprueba contenido y permisos desde ambos sistemas cuando sea pertinente. Registra además cómo retirar recursos y credenciales de sesión creados por el ejercicio sin afectar otras conexiones.

**Aceptación:** interoperabilidad útil con seguridad efectiva, recuperación razonada y colaboración evidenciada. Las limitaciones de dispositivos o licencias quedan identificadas por criterio. No se marca todo el RA como adquirido por haber copiado un archivo una vez.

## Revisión y recuperación del aprendizaje

Presenta cada evidencia junto al CE que pretende demostrar. Si una comprobación falla, conserva el resultado, delimita qué parte sí se observó y formula una segunda prueba. Una plantilla completa no sustituye la actuación ni una conclusión técnica. La programación del centro determina instrumentos y calificaciones; este dossier facilita una revisión por criterios y una recuperación planificada.

## Fuentes para preparar los ensayos

- [Debian 13, automatización de la instalación](https://www.debian.org/releases/trixie/amd64/apb.en.html).
- [Microsoft Learn: AD DS](https://learn.microsoft.com/windows-server/identity/ad-ds/).
- [Microsoft Learn: despliegue de perfiles móviles](https://learn.microsoft.com/windows-server/storage/folder-redirection/deploy-roaming-user-profiles).
- [Microsoft Learn: bosques y dominios de AD DS](https://learn.microsoft.com/training/modules/introduction-to-ad-ds/4-define-forests-domains) y [Microsoft Press: Active Directory y confianza entre bosques](https://www.microsoftpressstore.com/articles/article.aspx?p=3222421&seqNum=3).
- [Microsoft Learn: impresión](https://learn.microsoft.com/windows-server/administration/windows-commands/print).
- [Documentación de Samba](https://www.samba.org/samba/docs/) y [CUPS](https://www.cups.org/documentation.html).

Contrasta aplicabilidad, edición y versión antes de ejecutar cada procedimiento. Los enunciados y letras oficiales siguen el referente normativo enlazado en el mapa de RA, consultado el 09/11/2026.
