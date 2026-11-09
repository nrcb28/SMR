# Retos completos por RA · Aplicaciones web

[Índice del módulo](README.md) · [Matriz de criterios](09-alineacion-ra.md) · [Preparación de aplicaciones](11-complementos-curriculares.md) · [Trazabilidad JSON](alineacion-ra.json)

Los cinco retos siguientes desarrollan las actividades `0228-RA1-A1` a `0228-RA5-A1`. Los resultados de aprendizaje y las letras de criterio proceden del anexo I del [RD 1691/2007](https://www.boe.es/eli/es/rd/2007/12/14/1691); el procedimiento y la aceptación son una propuesta didáctica. Cada reto exige artefactos y comprobaciones. Haber leído la guía o utilizado un servicio ajeno no equivale a haber instalado y verificado la aplicación.

## Preparación común y dossier

Trabaja en un clon identificado de `srv01`, con dirección LAB `192.168.56.10/24`, cliente `.20` y salida NAT separada si necesitas descargar paquetes. No hay gateway en LAB. Antes de activar servidores, revisa interfaces, resolutores, puertos, virtual hosts y espacio. Conserva el acceso por consola y una copia independiente cuando el objetivo sea recuperar datos. Las aplicaciones pueden ocupar el mismo nombre/IP en ensayos separados; no mantengas dos clones con la misma dirección conectados a la vez.

Registra versiones de SO, PHP, motor de datos, aplicación y extensiones. La matriz de compatibilidad del producto elegido determina dependencias. Moodle 5.1 introdujo un directorio público específico; no traslades sin revisar una plantilla de un CMS que publica otra estructura. PHP CLI y PHP-FPM pueden cargar módulos y límites diferentes. El [complemento](11-complementos-curriculares.md) explica cómo preparar instancias propias sin exponer bases de datos o directorios privados.

El dossier contiene inventario, requisitos, copia previa, configuración saneada, pruebas con fecha/contexto, interpretación y recuperación. Separa resultado esperado y observado. Utiliza únicamente cuentas y contenido sintéticos. Si falta un backend o recurso, deja esa operación pendiente y explica la dependencia; no declares demostrada una instalación porque una captura de otro equipo muestra una pantalla similar.

<a id="ra1"></a>
## RA1 · 0228-RA1-A1: CMS con foro y mantenimiento

**Encargo:** un aula ficticia necesita noticias, páginas de ayuda y un foro moderado. El visitante consulta contenido publicado; un editor modifica noticias; participantes del foro envían temas; el moderador decide su publicación. La cuenta administradora conserva instalación y configuración. Debes implantarlo y demostrar que el mantenimiento conserva esas funciones.

### Procedimiento

1. Completa una ficha de compatibilidad del CMS, PHP, SQL, memoria, almacenamiento y extensiones. Incluye la licencia del núcleo y de los componentes. Usa la instalación WordPress del [capítulo técnico](02-guia-tecnica.md), o una alternativa mantenida que permita demostrar todas las operaciones.
2. Prepara la base y una identidad SQL limitada a ella. Registra host, base, permisos y mecanismo de recuperación de la credencial, sin copiarla al dossier. Comprueba desde el cliente el nombre canónico y HTTPS con confianza de laboratorio.
3. Crea cuentas sintéticas para administración, edición, participación y moderación. Documenta la relación entre roles del CMS y del componente de foro. Un rol editorial del núcleo no implica necesariamente ser moderador del foro.
4. Personaliza portada, navegación, tema y dos páginas. Utiliza el mecanismo de menús del tema elegido; distingue datos de configuración y código. No edites el núcleo para cambiar un texto o un color.
5. Evalúa un componente de foro mantenido y compatible, por ejemplo bbPress si sus requisitos corresponden a la versión ensayada. Registra procedencia y versión antes de incorporarlo en la copia de pruebas. En el modelo del repositorio el código es propiedad de despliegue y `DISALLOW_FILE_MODS` impide instalar desde el panel: realiza el despliegue controlado del [capítulo de operación](07-operacion-migracion-y-recuperacion-cms.md), sin abrir escritura universal al servidor web.
6. Crea dos secciones de foro: una de lectura pública y otra restringida a participantes. Configura alta de usuarios, moderación, publicación y edición conforme al encargo. No uses una casilla de «ocultar a buscadores» como restricción de acceso.
7. Guarda una línea base, actualiza en la copia de pruebas el componente o núcleo previsto por el ejercicio y repite las operaciones. Si el cambio requiere migración de datos, documenta qué copia permite volver al conjunto anterior.

### Comprobaciones y solución razonada

Prueba lectura anónima, publicación editorial, envío de un tema y moderación. Una cuenta sin el rol correspondiente debe recibir denegación al intentar configurar el foro o editar una página. No basta con ocultar un enlace: usa la URL de una operación conocida con una sesión que no tenga permiso y comprueba la autorización del servidor.

Los criterios d) e i) de este RA exigen pruebas de funcionamiento en momentos distintos del trabajo. Conserva una tabla antes/después del cambio: portada, navegación, entrada, foro, moderación y acceso denegado. Si una extensión se desactiva durante la actualización y desaparece el foro, que la portada siga abriendo no demuestra ausencia de regresión.

Genera una copia que incluya datos SQL, contenido, configuración y versiones necesarias. Restaura en una base y una ruta separadas siguiendo el procedimiento de recuperación; comprueba una entrada, una cuenta, un tema y su estado de moderación. Un ZIP de temas sin la base no recupera esas relaciones. Un volcado SQL sin los archivos subidos tampoco conserva todo el servicio.

**Entregables:** ficha de requisitos, inventario de componentes/menús, matriz de roles, pruebas iniciales y posteriores, registro de cambio, copia y ensayo de restauración. La aceptación requiere datos recuperados y acciones permitidas/denegadas coherentes. Los criterios a)–j) se revisan por separado en la matriz: un foro instalado sin reglas de acceso deja incompleta una parte del RA.

<a id="ra2"></a>
## RA2 · 0228-RA2-A1: LMS instalado y curso restaurado

**Encargo:** desplegar un aula virtual propia para una unidad «Diagnóstico de conectividad». Debe disponer de un docente, dos estudiantes matriculados, un estudiante ajeno, recursos descargables, una consulta y un foro. Después se exportarán contenidos y se recuperará un curso separado.

### Preparación y secuencia

1. Instala una versión de Moodle con soporte vigente y compatible con el entorno, siguiendo el [complemento de instalación](11-complementos-curriculares.md). Dibuja código, directorio público, configuración, `moodledata` y base. El almacenamiento de datos no queda dentro del árbol que sirve Nginx.
2. Accede como administrador, registra versión y revisa los avisos de entorno. Configura idioma, zona horaria, cron y, para el ejercicio, un sistema de correo local o capturador que no envíe a personas reales. Una instalación sin tareas programadas puede mostrar pantallas, pero acumular procesos pendientes.
3. Cambia portada, encabezado y tema con opciones compatibles. Crea una categoría y el curso. Define qué verá alguien sin matrícula y qué información del perfil puede editar cada usuario.
4. Crea el docente y tres cuentas de estudiante. Matricula sólo a dos. Configura un dato de perfil de prueba que no contenga información personal, si el ejercicio requiere personalización, y decide su visibilidad. Evita utilizar una contraseña compartida como supuesto mecanismo de rol.
5. Añade una página, un archivo sintético, un foro y una actividad de consulta. El docente publica una pregunta; los estudiantes responden según las reglas; el docente revisa o comenta. Registra quién puede modificar el enunciado y quién sólo participar.
6. Importa un pequeño banco de preguntas en GIFT y exporta una copia en GIFT y Moodle XML cuando la versión lo admita. Estos formatos de preguntas no son una copia integral del curso; conserva esa diferencia en el inventario.

Ejemplo de pregunta sintética GIFT para preparar en UTF-8:

```text
::Resolucion::¿Qué servicio relaciona nombres con direcciones? {=DNS ~DHCP ~SMB}
```

Verifica en la vista previa cuál es la opción correcta y que el texto no ha perdido tildes. Si importas un formato de contenidos distinto, utiliza un paquete de prueba autorizado y compatible. Abrir el archivo ZIP en el explorador no demuestra que el LMS lo haya importado.

### Copia, recuperación y evidencia

Realiza una copia de curso mediante el mecanismo de Moodle, con una selección de datos acorde al ejercicio. Restaura como curso nuevo y comprueba secciones, recursos, preguntas y actividades. Si excluiste usuarios o entregas, anótalo; no interpretes su ausencia como corrupción ni declares que la copia los conserva. Una restauración de curso no sustituye una copia completa de instancia con base, código y `moodledata`.

Genera informes de acceso y utilización a partir de las acciones realmente efectuadas con cuentas sintéticas. Compara al menos un evento esperado con su contexto: usuario, actividad y momento. Un registro de visita no demuestra que la persona haya comprendido el recurso; la actividad y su revisión aportan otra evidencia. No inventes entradas para que el informe parezca más completo.

**Prueba negativa:** el estudiante ajeno no accede al curso restringido ni a un archivo privado copiando una URL de una sesión autorizada. Comprueba también que el docente del curso no adquiere administración global por su matrícula. Si usas un modo de invitado, distingue deliberadamente acceso público y matrícula.

**Entregables:** mapa de directorios, ficha de instalación, curso, perfiles/matrículas, intercambios del foro, importaciones/exportaciones, copia/restauración e informe saneado. Acepta cuando se han demostrado las ocho letras del RA, incluidas seguridad e interpretación del uso, no sólo el acceso del administrador a la portada.

<a id="ra3"></a>
## RA3 · 0228-RA3-A1: gestión web de archivos e integridad

**Encargo:** ofrecer documentos al grupo soporte y al grupo alumnado sin un listado público del servidor. Cada grupo tendrá una carpeta compartida; una cuenta ajena no verá su contenido. El servicio debe permitir búsqueda, información contextual y operaciones con integridad comprobable.

Compara al menos dos aplicaciones según cuentas, permisos, metadatos, búsqueda, recuperación, exportación y mantenimiento. Puedes instalar Nextcloud en la variante del complemento; registra su versión y los requisitos que has verificado. Acceder a una carpeta local mediante `file://` o publicar un índice de Nginx no demuestra instalar un gestor web con cuentas.

### Procedimiento observable

1. Prepara la instancia con datos privados fuera del área pública y acceso HTTPS. Registra URL, base, ubicación de archivos y tareas de fondo. Verifica que las rutas internas no sirven directamente los documentos saltándose la aplicación.
2. Crea los grupos y cuatro cuentas sintéticas: propietaria, editora, lectora y ajena. Define quién puede compartir y si se permiten enlaces públicos. Deshabilita la compartición pública cuando no sea necesaria.
3. Crea un árbol con `manuales`, `inventario` y `evidencias`. Añade un archivo de información que explique finalidad, formato y responsable funcional de cada conjunto. No incluyas contraseñas en un README para facilitar la entrega.
4. Sube tres archivos pequeños, descarga uno y compara su SHA-256 con el original. Renombra, mueve y crea una versión nueva de uno; registra qué funciones conserva el gestor y qué cambia en sus enlaces o historial.
5. Aplica una convención de nombres y etiquetas o descripciones si están disponibles. Comprueba la búsqueda por nombre con una cuenta autorizada. Distingue el índice de archivos de un motor de búsqueda de contenido completo: no atribuyas búsqueda en PDFs al sistema si no has instalado y probado ese componente.
6. Borra un archivo de prueba desde una cuenta habilitada y ensaya la recuperación prevista —papelera, versiones o backup—. Repite la descarga y su comparación. El archivo inicial permanece guardado para contrastar.

La cuenta lectora no debe modificar un archivo y la ajena no debe obtenerlo mediante búsqueda, enlace directo ni carpeta compartida que no le corresponda. Las pruebas usan rutas conocidas de tu propio laboratorio; no exploran instancias de terceros. Una denegación en la interfaz se complementa con el intento de abrir el recurso en otra sesión.

**Solución razonada:** integridad, autorización e indexación son condiciones diferentes. Un hash coincidente prueba el contenido de ese archivo; no demuestra permisos correctos. Una búsqueda sin resultados puede deberse al permiso, al nombre o a un índice pendiente. Para interpretarla necesitas una prueba con un archivo permitido y otra con uno no permitido, preservando el mismo término cuando sea posible.

**Entregables:** comparación, instancia, usuarios/grupos, árbol con información adicional, operaciones y hashes, prueba de búsqueda y matriz de seguridad. Acepta cuando otra persona puede localizar el conjunto permitido, entender su contexto y repetir descarga/recuperación sin recibir acceso indebido.

<a id="ra4"></a>
## RA4 · 0228-RA4-A1: ofimática web instalada y colaborativa

**Encargo:** dos personas deben preparar un documento, una hoja y una presentación desde navegador, con una tercera cuenta de lectura. Se necesita una aplicación instalada en el laboratorio y su backend de edición. Una cuenta gratuita en un SaaS externo puede servir para comparar prestaciones, pero no demuestra este despliegue.

### Instalación e integración

Parte del gestor de archivos anterior o de una copia específica. Evalúa una integración compatible, como Nextcloud Office con un servidor Collabora mantenido. La edición CODE integrada, cuando esté disponible para la arquitectura y versión, es una alternativa para ensayos con los límites indicados por su proveedor. No la presentes como dimensionamiento o garantía de un servicio de producción.

Registra por separado aplicación de archivos, conector ofimático, backend y licencias. Sigue [el procedimiento complementario](11-complementos-curriculares.md), comprueba URL canónica, certificado y permiso de los orígenes WOPI según el producto. Si el editor muestra un marco vacío, examina sus registros y la integración; el hecho de que la aplicación de archivos abra no prueba que el backend esté accesible.

Crea un grupo de trabajo y asigna dos editores y un lector. Prepara un documento con encabezados, una hoja con cinco filas y una presentación de tres diapositivas. En la hoja calcula una suma y compara un resultado manual. Prueba importar y exportar un archivo compatible, revisando fórmulas, estilos y objetos; no prometas equivalencia perfecta con cualquier formato de escritorio.

Abre el mismo documento en dos navegadores con identidades distintas. Una persona añade un párrafo y otra un comentario o una corrección acordada. Observa propagación, autoría y guardado. Realiza una edición concurrente controlada en dos zonas diferentes y después en un punto común, conservando el comportamiento real del editor. No sustituyas esta prueba por mostrar dos pestañas de la misma cuenta.

Prueba al lector: debe ver el contenido, pero no editar ni ampliar sus permisos. Retira a un usuario del grupo o cambia su autorización y comprueba qué ocurre con una sesión ya abierta y con otra nueva. Documenta los límites de revocación y caché del producto; no supongas que una baja elimina copias descargadas previamente.

### Aceptación y recuperación

Conserva historial de cambios, matriz de cuentas, formatos y límites observados. Exporta los tres productos y restaura una copia de la instancia si el ejercicio lo exige. Los documentos y su historial pueden almacenarse de forma diferente; comprueba qué conserva el procedimiento elegido.

**Solución razonada:** una aplicación colaborativa es una cadena: identidad, permisos, almacenamiento, conector, backend y navegador. El error puede aparecer en cualquier enlace. La solución exige observar los dos usuarios y el producto guardado, no únicamente instalar un paquete que se llama «Office».

**Entregables:** estudio de alternativas, inventario de componentes, despliegue registrado, tres productos editables, sesión concurrente y pruebas negativas. Acepta cuando se han demostrado instalación propia, prestaciones, gestión de cuentas y colaboración de las siete letras del resultado.

<a id="ra5"></a>
## RA5 · 0228-RA5-A1: webmail y calendario web

**Encargo:** instalar un frontend web de correo y una agenda web para cuentas de laboratorio. El usuario debe enviar y recibir un mensaje sintético, gestionar una cita y una tarea cuando la aplicación elegida lo permita. Las cuentas no pertenecen a personas reales y el servidor no retransmite correo a Internet.

Dibuja la cadena navegador–frontend–IMAP/SMTP y la cadena navegador–calendario–CalDAV. Nextcloud Mail y Calendar/Tasks pueden resolver el frontend; Roundcube y una aplicación de calendario constituyen otra combinación. Un calendario ICS descargable no equivale a una aplicación instalada con edición y cuentas. El [complemento](11-complementos-curriculares.md) concreta dependencias y preparación.

### Secuencia de trabajo

1. Comprueba que existe un backend de correo de laboratorio con dos buzones, recepción IMAP y envío SMTP autorizado. La práctica de [Servicios en red](../servicios-en-red/README.md) documenta escenarios aislados. La variante sólo loopback de correo no es accesible desde otra VM por el mero hecho de instalar el frontend: ubica ambos en el mismo host o prepara expresamente una extensión LAB con TLS y autenticación.
2. Instala la aplicación de webmail compatible. Configura dirección, puertos, seguridad y método de autenticación con los valores de tu backend. No supongas que IMAP y SMTP usan el mismo puerto ni que la cuenta SQL del frontend es la cuenta de correo.
3. Asocia dos cuentas sintéticas y explica dónde se crean realmente los buzones. Añadir una cuenta al frontend configura un cliente; no siempre provisiona una identidad en el servidor. Comprueba cierre de sesión y acceso de cada usuario.
4. Envía un mensaje con identificador único, recíbelo en el otro buzón y responde. Añade una carpeta y un filtro si la aplicación lo admite. Conserva cabeceras mínimas saneadas para relacionar envío, recepción y mensaje, sin copiar tokens de sesión.
5. Instala y habilita Calendar y, si se necesita, Tasks compatibles. Crea un calendario de prueba, un evento con zona horaria y un recordatorio. Comparte lectura y escritura con cuentas distintas. Utiliza el enlace CalDAV publicado por la aplicación cuando conectes un cliente externo; no construyas una ruta de memoria.
6. Crea una tarea, cambia su estado y comprueba la vista disponible. Si la edición sólo proporciona citas, selecciona e instala el componente de tareas apropiado o deja explícitamente pendiente esa función; no la declares demostrada por existir un icono.

### Solución, pruebas y entrega

Realiza pruebas en sesiones independientes: lectura de mensajes propios, acceso denegado al buzón ajeno, envío permitido, calendario de sólo lectura y evento editable para la cuenta autorizada. Añade una cita de hora conocida y comprueba su representación después de cambiar la zona horaria de un cliente. Distingue instante almacenado, zona del evento y zona de visualización.

Un error de envío con recepción correcta apunta a otra dependencia: revisa SMTP, autorización, certificado y logs. No cambies la clave SQL si el error procede de autenticación IMAP. Si el calendario se lee pero no se actualiza desde un móvil, comprueba permisos, cuenta y compatibilidad antes de conceder escritura a todos.

**Entregables:** alternativas, versiones, diagrama de backends, configuración saneada, gestión de cuentas, intercambio de correo y agenda/tareas con pruebas positivas y negativas. La recuperación identifica por separado contenido del buzón, datos de agenda y configuración de frontend; una copia del cliente web no contiene necesariamente los mensajes almacenados en el servidor.

## Cierre de los cinco retos

Revisa cada letra de la [matriz](09-alineacion-ra.md). Registra `sin realizar`, `ensayado`, `evidencia disponible` o `revisión pendiente` como estados del portfolio, sin convertirlos en una calificación oficial. Si varios integrantes han trabajado juntos, identifica qué operación hizo cada uno y qué puede explicar o repetir individualmente.

Las pruebas del dossier son las que ejecutes en tu laboratorio. Esta guía no afirma haber instalado esos servicios durante su redacción. Una incompatibilidad o recurso no disponible se registra con su diagnóstico, alternativa y pendiente concreto.

## Fuentes primarias de contraste

- [WordPress: administración](https://developer.wordpress.org/advanced-administration/) y [bbPress](https://bbpress.org/): permisos, componentes y foro compatible.
- [Moodle: instalación](https://docs.moodle.org/501/en/Installing_Moodle), [copias](https://docs.moodle.org/501/en/Course_backup) y [restauración](https://docs.moodle.org/501/en/Course_restore): procedimientos según versión.
- [Nextcloud: instalación](https://docs.nextcloud.com/server/stable/admin_manual/installation/), [Files](https://docs.nextcloud.com/server/stable/user_manual/en/files/) y [Office](https://docs.nextcloud.com/server/stable/admin_manual/office/): almacenamiento, cuentas e integración.
- [Nextcloud Mail](https://docs.nextcloud.com/server/stable/user_manual/en/groupware/mail.html) y [Calendar](https://docs.nextcloud.com/server/stable/user_manual/en/groupware/calendar.html): clientes web, cuentas y agenda.
