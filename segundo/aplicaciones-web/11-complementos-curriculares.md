# Complementos de despliegue: LMS, archivos, ofimática y escritorio web

[Índice del módulo](README.md) · [Retos por RA](10-retos-por-ra.md) · [Matriz](09-alineacion-ra.md)

Este complemento prepara aplicaciones propias para los RA2–RA5. Aporta una ruta de instalación y verificación; sus pasos deben adaptarse a la versión soportada que se registre en el laboratorio. No afirma que se hayan desplegado estos productos durante la redacción. La documentación del producto de la versión elegida resuelve sus requisitos concretos.

## 1. Contrato de laboratorio y separación de funciones

Utiliza un clon aislado de `srv01`, `192.168.56.10/24`, con cliente `.20`, sin gateway en LAB y con NAT independiente si se necesitan descargas. Moodle y Nextcloud pueden ensayarse en clones alternativos con la misma dirección, nunca simultáneamente en la red. Si se mantienen en una VM, asigna virtual hosts, rutas, bases y usuarios diferentes, y dimensiona memoria y almacenamiento. No cambies el DNS del dominio AD para preparar estas aplicaciones.

| Aplicación | Nombre LAB propuesto | Código | Datos persistentes |
| --- | --- | --- | --- |
| Moodle | `lms.aula.test` | `/srv/www/moodle-lab` | Base `moodle_lab` y `/srv/moodledata-lab` |
| Nextcloud | `cloud.aula.test` | `/srv/www/nextcloud-lab` | Base `nextcloud_lab`, configuración y `/srv/nextcloud-data-lab` |
| Editor ofimático | Integración de la instancia o nombre dedicado documentado | Conector y backend separados | Documentos del gestor y configuración de integración |
| Correo | Frontend dentro de la aplicación elegida | Aplicación Mail o Roundcube | Buzones del servidor IMAP, además de preferencias del frontend |

Crea únicamente los nombres que hayas instalado. Cliente y servidor deben resolver sus propios nombres canónicos, y el certificado debe incluirlos. Reutiliza el procedimiento de CA de laboratorio del [capítulo técnico](02-guia-tecnica.md), generando certificados apropiados para esos nombres. Una CA confiada por el navegador puede necesitar configuración adicional para una petición HTTP interna de otra aplicación; no desactives globalmente la verificación TLS para resolverlo.

## 2. Inventario de compatibilidad antes de instalar

En Debian consulta el estado sin modificar:

```bash
cat /etc/os-release
php -v
php -m
apt-cache policy php8.4-fpm mariadb-server nginx
systemctl status php8.4-fpm nginx --no-pager
sudo ss -lntp
```

Anota versión y procedencia reales. Compara requisitos de PHP, SQL, extensiones, arquitectura y recursos con la versión de aplicación. No deduzcas compatibilidad sólo porque el paquete existe. El PHP usado por FPM puede cargar otro `php.ini` y otros módulos respecto al de consola; identifica ambos contextos mediante los procedimientos del distribuidor y las comprobaciones de entorno del producto.

Descarga únicamente desde el sitio oficial, registra versión exacta y verifica la firma o mecanismo de integridad publicado por una fuente confiable. Una suma calculada sobre tu propia descarga permite futuras comparaciones, pero no autentica por sí sola el origen. No extraigas un archivo desconocido directamente como administrador dentro del servidor activo: inspecciona primero su contenido en un espacio de trabajo y conserva el procedimiento de despliegue.

La instalación de dependencias se realiza después de esa comparación. Revisa la propuesta de APT y utiliza los módulos que realmente requiere la versión, por ejemplo drivers SQL, XML, internacionalización, cURL, ZIP o GD. No copies una lista histórica que incluya módulos retirados. No mantengas un archivo `phpinfo()` accesible cuando termine un diagnóstico.

## 3. Moodle: código, configuración y almacenamiento privado

La documentación de [Moodle 5.1](https://moodledev.io/general/releases/5.1) confirma soporte de PHP 8.4 y una nueva estructura pública. Es una referencia concreta para comprender el cambio, no una orden de instalar una revisión antigua: elige una revisión con soporte y parches vigentes y vuelve a comprobar su matriz. En versiones con esa estructura, el document root apunta a `/srv/www/moodle-lab/public`, mientras configuración y scripts administrativos permanecen en otras ubicaciones del árbol.

### Preparación

1. Guarda el paquete verificado en una carpeta de trabajo del usuario. Inspecciona su estructura y despliega una copia en la ruta nueva. Si ya existe la ruta o una base homónima, detente a identificar su uso; no sobrescribas una práctica anterior.
2. Crea `moodle_lab` con codificación y colación admitidas por la versión. Crea una cuenta SQL dedicada, por ejemplo `moodle_lab` restringida a `localhost`, con permisos sólo en esa base. Introduce su contraseña por el mecanismo administrativo privado del motor; no la incorpores a comandos publicados o capturas del informe.
3. Crea el directorio de datos fuera del código público. En la VM exclusiva y con la ruta nueva verificada, un ejemplo es `sudo install -d -o www-data -g www-data -m 0750 /srv/moodledata-lab`. El usuario efectivo de PHP-FPM debe poder escribir allí. El código se conserva bajo control de despliegue y legible por el servicio.
4. Prepara `config.php` desde el modelo de la misma versión, con base, cuenta, contraseña, URL canónica y `dataroot` reales. Puedes editarlo de forma administrativa fuera de la raíz pública; protege su lectura y no publiques el archivo con credenciales. No copies una configuración de otro sitio cambiando sólo la URL.
5. Prepara el virtual host y los límites de PHP requeridos. El [ejemplo oficial Nginx](https://docs.moodle.org/501/en/Nginx) contempla routing y `PATH_INFO`; una plantilla que sólo ejecuta archivos `.php` puede romper recursos o rutas. Adapta su configuración a LAB, socket FPM y certificado del ejercicio, manteniendo el directorio público correcto.

Inspecciona todos los `listen` activos. Deshabilita el sitio predeterminado sólo en el clon destinado a la actividad, conservando su configuración y siguiendo el procedimiento ya descrito para WordPress. Valida Nginx antes de recargar, observa listeners y realiza una petición normal al nombre canónico desde el cliente.

### Inicialización y tareas

Abre el instalador o página administrativa que corresponda a la versión con el sitio ya configurado. Revisa licencia, entorno y configuración SQL. Crea una cuenta administradora exclusiva del laboratorio y termina la inicialización. Si el asistente genera configuración para guardarla manualmente, colócala en la ruta que indique, fuera del directorio público cuando así lo requiere la estructura. No concedas permisos `777` al árbol para evitar comprender ese paso.

Comprueba los scripts disponibles antes de programarlos. En el árbol convencional, las consultas siguientes permiten localizar la ayuda y ejecutar la tarea de mantenimiento como usuario del servicio:

```bash
sudo -u www-data php /srv/www/moodle-lab/admin/cli/cron.php --help
sudo -u www-data php /srv/www/moodle-lab/admin/cli/cron.php
```

Si la versión cambia su CLI, sigue su manual y registra la ruta nueva. Programa después la periodicidad recomendada mediante el mecanismo del sistema, con el mismo usuario, PHP y contexto. Conserva la salida de una ejecución y comprueba el estado de tareas en la aplicación; una línea de crontab no demuestra que se ejecute sin errores.

Para RA2 crea el curso, perfiles y actividades descritos en el reto. La copia `.mbz` de un curso no equivale a backup de instancia. Para recuperar toda la instalación se necesitan base coherente, datos, configuración, código/versiones y el material de autenticación que corresponda. Ensaya la recuperación sin enviar avisos a cuentas reales ni reutilizar una URL que confunda al cliente.

## 4. Nextcloud como gestor de archivos instalado

Consulta los [requisitos](https://docs.nextcloud.com/server/stable/admin_manual/installation/system_requirements.html) de la versión soportada elegida. Registra PHP, motor y versión de SQL realmente admitidos. Si una dependencia del Debian base no está admitida por esa edición, prepara un escenario compatible documentado en otra VM; no suprimas controles de versión del instalador para aparentar un despliegue correcto.

### Instalación de una instancia de prueba

1. Despliega el código verificado en `/srv/www/nextcloud-lab`. Crea la base `nextcloud_lab` y una cuenta SQL independiente de Moodle y WordPress. Separa también directorio de datos y política de copia.
2. Crea `/srv/nextcloud-data-lab` fuera del document root, con escritura para el usuario HTTP y permisos acordes al manual. Establece un modelo de propiedad del código coherente con el modo de actualización. La instalación de aplicaciones puede necesitar escritura en un directorio de aplicaciones concreto; no amplíes por ello la escritura de todo `/srv`.
3. Adapta la configuración Nginx oficial de Nextcloud. Necesita reglas de acceso, WebDAV y tratamiento PHP que no se deducen de una plantilla estática. Mantén listeners LAB, TLS, socket de FPM correcto y protección de rutas privadas.
4. Configura `cloud.aula.test` en resolución de servidor y cliente. Completa el asistente con cuenta administradora sintética, directorio de datos y base. Introduce secretos en el diálogo o mecanismo protegido, sin publicarlos en una línea de comandos.
5. Revisa dominio de confianza, avisos de administración y tarea de fondo. La URL autorizada debe corresponder al nombre usado. Comprueba la herramienta `occ` de esa copia y su estado:

```bash
sudo -u www-data php /srv/www/nextcloud-lab/occ status
sudo -u www-data php /srv/www/nextcloud-lab/occ list
```

Configura las tareas periódicas conforme al manual y registra cómo se ejecutan. Distingue la versión del núcleo y las de aplicaciones. No consideres resuelto un aviso de configuración sólo porque permite cerrar la notificación.

Crea cuentas y grupos antes de probar datos. Sube archivos mediante la aplicación y utiliza su cliente o WebDAV compatible; copiar ficheros directamente al directorio privado puede dejar desajustada la información que mantiene el gestor. Si tu procedimiento requiere escaneo o reparación, utiliza la herramienta documentada y limita el alcance a la instancia de pruebas.

Comprueba descarga, hash, búsqueda y permisos según el reto. El buscador estándar por nombre no implica indexación de contenido completo. Documenta funciones instaladas y resultados, sin atribuir al producto una capacidad que depende de componentes adicionales.

## 5. Conectar un editor ofimático propio

Nextcloud Office utiliza un conector y un backend de edición. Instalar el conector no demuestra que exista un servidor Collabora operativo. Revisa [la administración de Office](https://docs.nextcloud.com/server/stable/admin_manual/office/) y los requisitos de arquitectura, recursos, licencia y versión.

En un laboratorio compatible se puede utilizar la edición CODE integrada si está disponible y admitida. Instala las aplicaciones necesarias desde su origen oficial mediante el procedimiento autorizado de mantenimiento; registra qué componente proporciona el backend. Si eliges un servidor separado, conserva su URL, TLS, routing y configuración de orígenes WOPI, con exposición únicamente a los clientes/servicios previstos.

Desde administración selecciona la modalidad instalada y ejecuta sus verificaciones. Abre un documento con una cuenta ordinaria y observa creación, edición y guardado. Examina los registros de ambos componentes cuando el editor no abra. Un error de confianza en una petición interna se resuelve instalando la CA mediante el mecanismo admitido, no desactivando verificación para todas las conexiones.

Ensaya la colaboración con dos identidades y un lector. Exporta el producto y revisa interoperabilidad. Registra los límites de CODE y de tu entorno; la edición de desarrollo no constituye una garantía de capacidad para una organización. El objetivo curricular es demostrar despliegue, cuentas, prestaciones y trabajo colaborativo bajo condiciones conocidas.

## 6. Webmail y agenda: frontend frente a backend

Para correo necesitas un servidor que ofrezca IMAP y SMTP apropiados al escenario y un cliente web. Una aplicación Mail no crea necesariamente buzones. Usa cuentas sintéticas del laboratorio, con servidor de correo sin retransmisión pública, y registra qué componente gestiona las identidades.

Si el backend sólo escucha en loopback, el frontend debe estar en el mismo host o se debe preparar una extensión de red expresamente documentada. No sustituyas `localhost` por una IP y des por hecho que el servicio estará escuchando allí. Comprueba listeners, TLS, autorización y puertos de cada protocolo.

Instala una edición compatible de Nextcloud Mail, o Roundcube en otro virtual host si esa es la variante elegida. Añade la cuenta con dirección, servidor IMAP, SMTP y método de autenticación reales. En el cliente web envía un mensaje a la otra cuenta de prueba y responde. Correlaciona cabeceras y logs sin conservar tokens de sesión. Recepción correcta y envío fallido son trayectos distintos y se investigan por separado.

Instala Calendar y, para tareas, una aplicación compatible cuando se requiera esa función. Crea un calendario privado, compártelo con lectura y escritura diferentes y utiliza el enlace CalDAV que publique la aplicación. Éste es también un backend de prueba posible para el reto de correo/agenda de [Ofimática](../../primero/aplicaciones-ofimaticas/10-retos-por-ra.md#ra8).

Conecta el cliente de escritorio y un cliente móvil autorizado con la misma cuenta de laboratorio. Comprueba creación desde equipo, recepción en móvil, modificación en móvil y actualización en equipo. Instala la CA según el dispositivo sin importar la clave privada. Si el móvil no llega a la red host-only, prepara una topología autorizada o marca pendiente esa prueba; no expongas el calendario a Internet para simplificar la conectividad del aula.

## 7. Copias, retorno y aceptación del conjunto

Define qué contiene cada copia. En Moodle diferencia curso e instancia; en Nextcloud, configuración, datos y base; en correo, frontend y buzones; en Office, documentos y backend/configuración. Una copia del código no conserva por sí sola los datos del usuario.

Utiliza el modo de mantenimiento y los mecanismos de coherencia del producto cuando corresponda. Identifica y verifica el destino antes de escribir. Restaura en otra base y ruta o en una VM separada, con URL y red que no interfieran con la instancia original. Comprueba una cuenta, permisos, un archivo, una actividad o mensaje y una operación de edición según la aplicación.

Para volver atrás conserva versión de código, esquema de datos y extensiones compatibles. Cambiar sólo el código después de una migración puede dejar una base incompatible. Registra el punto recuperable, tiempos reales y datos que retrocederían; no uses una instantánea como explicación universal para cualquier dependencia.

Una instalación se acepta cuando la aplicación responde desde el cliente, sus tareas funcionan, los permisos corresponden al encargo y existe una prueba de recuperación. Los defectos o recursos pendientes quedan identificados. La evidencia de un reto no se extiende automáticamente a todos los demás: crear un archivo no demuestra calendario, y abrir un documento no demuestra colaboración.

## Referencias primarias

- [Moodle 5.1: instalación](https://docs.moodle.org/501/en/Installing_Moodle), [Nginx](https://docs.moodle.org/501/en/Nginx) y [administración CLI](https://docs.moodle.org/501/en/Administration_via_command_line).
- [Nextcloud: instalación manual](https://docs.nextcloud.com/server/stable/admin_manual/installation/source_installation.html), [asistente](https://docs.nextcloud.com/server/stable/admin_manual/installation/installation_wizard.html) y [comandos](https://docs.nextcloud.com/server/stable/admin_manual/occ_command.html).
- [Nextcloud: copias](https://docs.nextcloud.com/server/stable/admin_manual/maintenance/backup.html), [Mail](https://docs.nextcloud.com/server/stable/user_manual/en/groupware/mail.html) y [Calendar](https://docs.nextcloud.com/server/stable/user_manual/en/groupware/calendar.html).
- [Roundcube](https://roundcube.net/) y [Radicale](https://radicale.org/v3.html): alternativas de cliente web y servidor CalDAV/CardDAV, con su documentación de versión.
