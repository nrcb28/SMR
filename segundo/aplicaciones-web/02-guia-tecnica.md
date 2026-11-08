# Guía técnica de despliegue, mantenimiento y recuperación

## 1. Preparación y límites del laboratorio

Todos los comandos de modificación de este documento se ejecutan **dentro de la VM de prácticas**, después de crear una instantánea y comprobar que no hay servicios de otras prácticas que deban conservarse. Los comandos se muestran para su estudio y ejecución por el alumno; no se afirma que hayan sido ejecutados en tus máquinas.

Comprueba primero, sin cambiar configuración:

```bash
cat /etc/os-release
ip -br address
ip route
ss -lntup
apt-cache policy nginx php-fpm mariadb-server
```

Debes identificar la dirección `192.168.56.10` en la interfaz LAB real. El nombre `ens19` es orientativo: no lo copies sin comprobarlo. La ruta por defecto para descargas pertenece a la NIC NAT; no añadas una ruta por defecto ficticia en host-only. Si Apache u otro servicio ya ocupa 80/443, decide qué servicio pertenece a este clon antes de continuar. No detengas procesos al azar para liberar un puerto.

Tanto **srv01 como el cliente** deben resolver `wp.aula.test` hacia `192.168.56.10` mediante el DNS de laboratorio o una entrada local controlada. WordPress realiza peticiones HTTP a su propia URL para comprobaciones de salud y tareas: resolver el nombre sólo en el cliente no basta. En Windows se puede editar, como administrador, `C:\Windows\System32\drivers\etc\hosts`; en Linux, `/etc/hosts`. Guarda una copia, evita entradas contradictorias y registra esta línea en cada máquina que no utilice el DNS LAB:

```text
192.168.56.10 wp.aula.test
```

En srv01, `getent ahostsv4 wp.aula.test` debe mostrar `192.168.56.10`. Comprueba también la resolución desde el cliente. No añadas una dirección IPv6 ficticia para este nombre: el servidor virtual del ejemplo escucha únicamente en la IPv4 LAB. Usar un nombre distinto después de instalar el CMS puede provocar redirecciones o recursos que apuntan a la URL anterior.

## 2. Inspeccionar y servir el sitio estático

El [ejemplo HTML](ejemplos/sitio-estatico/index.html) y su [CSS](ejemplos/sitio-estatico/estilos.css) no necesitan compilación ni bibliotecas externas. Puedes abrir el archivo local para una inspección inicial, pero utilizar HTTP reproduce mejor la carga de recursos y las cabeceras.

Desde la carpeta del ejemplo, con Python 3 disponible:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Abre `http://127.0.0.1:8000/` en la misma VM. El proceso termina con `Ctrl+C`. El servidor de Python es una herramienta de desarrollo, no el servicio de producción del curso. Si necesitas acceso desde el cliente, enlázalo explícitamente a `192.168.56.10`, limita el acceso a LAB y vuelve a detenerlo al terminar. No lo ejecutes en una carpeta que contenga claves, copias o documentos privados: su función es publicar los archivos de esa carpeta.

En las herramientas del navegador revisa la pestaña Red: `index.html` y `estilos.css` deben cargarse sin peticiones a terceros. Prueba la navegación con Tab, el enlace de salto y una ventana de 320 píxeles de ancho. Un resultado visual aceptable no demuestra por sí solo accesibilidad completa.

## 3. Instalar las dependencias del CMS

En Debian 13 actualizado, revisa primero la propuesta del gestor. El siguiente comando modifica paquetes y arranca servicios; ejecútalo únicamente en el clon previsto:

```bash
sudo apt update
sudo apt install nginx mariadb-server php-fpm php-mysql php-curl \
  php-gd php-intl php-mbstring php-xml php-zip curl ca-certificates openssl
```

El paquete Nginx puede activar automáticamente su sitio predeterminado con listeners en todas las interfaces, incluida IPv6. Mantén el clon aislado durante la preparación; en la sección 7 se inspecciona y retira únicamente su enlace de activación antes de aceptar el despliegue. Instalar un servidor virtual limitado a LAB no elimina otros listeners ya activos.

Las extensiones de PHP aportan acceso a base de datos, peticiones HTTPS, imágenes, internacionalización, cadenas y formatos utilizados por el CMS. Comprueba las versiones reales:

```bash
nginx -v
php -v
mariadb --version
php -m
systemctl status nginx mariadb php8.4-fpm --no-pager
ls -l /run/php/
```

`php -v` describe la interfaz CLI. PHP-FPM puede utilizar otra versión o archivo de configuración; identifica el servicio y su socket. El ejemplo Nginx utiliza `/run/php/php8.4-fpm.sock`. Si el sistema no presenta ese socket, corrige el ejemplo para la versión instalada y compatible. No crees un enlace simbólico hacia un socket desconocido para ocultar la diferencia.

Consulta la [matriz oficial de WordPress y PHP](https://make.wordpress.org/core/handbook/references/php-compatibility-and-wordpress-versions/) y los requisitos de los temas/complementos. Selecciona una versión estable mantenida y anota la combinación exacta. No deduzcas compatibilidad de una extensión porque el núcleo acepte la versión de PHP.

## 4. Crear una base y una identidad limitada

MariaDB debe permanecer accesible por socket local o loopback; el cliente web no necesita acceso directo al puerto 3306. Compruébalo con `ss -lntp` y la configuración efectiva del servidor. No abras ese puerto en la interfaz LAB para resolver un problema de credenciales.

Entra en el cliente SQL administrativo de la VM, evitando que el historial del cliente conserve la contraseña que introducirás:

```bash
sudo env MYSQL_HISTFILE=/dev/null mariadb
```

Ejecuta las siguientes sentencias **sustituyendo el marcador de contraseña por una contraseña aleatoria propia**. El marcador no debe quedar como contraseña real ni guardarse en Git. Si tu contraseña contiene comillas, usa un procedimiento de aprovisionamiento que las trate correctamente; no la pegues sin escapar dentro de SQL.

```sql
CREATE DATABASE wp_aula CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'wp_aula'@'localhost' IDENTIFIED BY 'SUSTITUIR_POR_SECRETO_ALEATORIO';
GRANT ALL PRIVILEGES ON wp_aula.* TO 'wp_aula'@'localhost';
SHOW GRANTS FOR 'wp_aula'@'localhost';
EXIT;
```

El permiso se limita al esquema `wp_aula`: no incluye privilegios globales ni capacidad de conceder permisos. WordPress necesita crear y modificar tablas durante instalación y actualizaciones; un modelo más restrictivo requiere distinguir operación editorial y despliegue y probarlo con las extensiones elegidas.

Comprueba la identidad desde el mismo servidor:

```bash
mariadb --user=wp_aula --password --database=wp_aula \
  --execute='SELECT CURRENT_USER(), DATABASE();'
```

`--password` sin valor solicita el secreto sin ponerlo en la línea de procesos. Si falla, diferencia servicio, socket, usuario/host y contraseña. Crear otro usuario con permisos globales no corrige el diagnóstico.

## 5. Obtener y preparar WordPress

Descarga desde el proyecto oficial a una carpeta temporal de tu usuario. No ejecutes como root un script obtenido directamente de Internet. Ejemplo de descarga e inspección:

```bash
mkdir -p "$HOME/lab-web/descargas"
cd "$HOME/lab-web/descargas"
curl --fail --location --proto '=https' --tlsv1.2 \
  https://wordpress.org/latest.tar.gz --output wordpress.tar.gz
sha256sum wordpress.tar.gz
tar -tzf wordpress.tar.gz | head
```

`latest.tar.gz` cambia con el tiempo: conserva fecha, hash y versión de la descarga. El hash calculado sirve para identificar tu artefacto; no demuestra autenticidad por sí solo si no se compara con una referencia de confianza. Revisa las publicaciones oficiales y, si usas WP-CLI desde su fuente oficial, sus funciones de verificación de checksums. Para una práctica repetible conserva el artefacto y el inventario, sin redistribuirlo innecesariamente en el repositorio.

Extrae como usuario en esa carpeta y despliega sólo después de inspeccionar el contenido:

```bash
tar -xzf wordpress.tar.gz
sudo install -d -o root -g www-data -m 0750 /srv/www/wp-aula
sudo cp -a wordpress/. /srv/www/wp-aula/
sudo chown -R root:www-data /srv/www/wp-aula
sudo find /srv/www/wp-aula -type d -exec chmod 0750 {} \;
sudo find /srv/www/wp-aula -type f -exec chmod 0640 {} \;
sudo install -d -o www-data -g www-data -m 0750 \
  /srv/www/wp-aula/wp-content/uploads
sudo cp /srv/www/wp-aula/wp-config-sample.php /srv/www/wp-aula/wp-config.php
sudo chown root:www-data /srv/www/wp-aula/wp-config.php
sudo chmod 0640 /srv/www/wp-aula/wp-config.php
```

El trabajador de PHP, `www-data` en esta VM, necesita leer el código, pero no modificarlo. La carpeta de subidas sí admite escritura. No utilices permisos `777`: resolverían síntomas ampliando innecesariamente la capacidad de modificación. La configuración presupone un único servicio didáctico de confianza; para alojar sitios de usuarios distintos se deben separar usuarios y pools de FPM.

Edita `wp-config.php` con `sudoedit`. Configura `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` como `localhost` y `DB_CHARSET` como `utf8mb4`; conserva la colación vacía del ejemplo salvo necesidad documentada. Sustituye claves y sales de autenticación por valores aleatorios únicos siguiendo la documentación oficial. Añade antes del comentario final de configuración:

```php
define( 'DISALLOW_FILE_EDIT', true );
define( 'DISALLOW_FILE_MODS', true );
define( 'FORCE_SSL_ADMIN', true );
define( 'WP_ENVIRONMENT_TYPE', 'local' );
```

Este modelo deshabilita edición e instalación/actualización de archivos desde el panel: el mantenimiento se realiza mediante un despliegue controlado, después de ensayar en pruebas. Es una decisión deliberada y debe explicarse al usuario; no esperes que el botón de actualizar funcione con código propiedad de root y modificaciones deshabilitadas.

No publiques `wp-config.php`, contraseñas ni sales. El archivo de configuración de Nginx incluido contiene rutas y nombres de ejemplo, pero ningún secreto.

## 6. TLS interno con una autoridad de laboratorio

Utiliza preferentemente la CA del laboratorio si ya existe. El siguiente procedimiento crea una **CA exclusiva de prácticas**, cuya clave se conserva fuera del árbol web. No la instales en equipos ajenos ni en el sistema personal para otras finalidades.

En tu usuario de la VM:

```bash
umask 077
mkdir -p "$HOME/lab-web/pki"
cd "$HOME/lab-web/pki"
openssl req -x509 -newkey rsa:3072 -sha256 -days 365 -noenc \
  -keyout ca.key -out ca.crt -subj '/CN=CA laboratorio SMR' \
  -addext 'basicConstraints=critical,CA:TRUE' \
  -addext 'keyUsage=critical,keyCertSign,cRLSign'
openssl req -new -newkey rsa:2048 -noenc \
  -keyout wp-aula.key -out wp-aula.csr -subj '/CN=wp.aula.test'
```

Crea `servidor.ext` en esa carpeta:

```ini
basicConstraints=critical,CA:FALSE
keyUsage=critical,digitalSignature,keyEncipherment
extendedKeyUsage=serverAuth
subjectAltName=DNS:wp.aula.test,IP:192.168.56.10
```

Firma e instala únicamente los archivos necesarios para el servidor:

```bash
openssl x509 -req -in wp-aula.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out wp-aula.crt -days 90 -sha256 -extfile servidor.ext
openssl verify -CAfile ca.crt wp-aula.crt
sudo install -o root -g root -m 0644 wp-aula.crt /etc/ssl/certs/wp-aula.crt
sudo install -o root -g root -m 0600 wp-aula.key /etc/ssl/private/wp-aula.key
```

La clave CA sin contraseña es aceptable únicamente en este laboratorio efímero, con permisos restrictivos y sin uso externo. En una PKI real su custodia y operación requieren un diseño específico. Importa **el certificado público `ca.crt`, nunca `ca.key`**, en el almacén de confianza del cliente o navegador de prácticas mediante su procedimiento documentado. Registra cómo retirarlo al terminar. Verifica emisor, SAN y fechas; no soluciones una alerta pulsando continuar de forma permanente.

### 6.1 Confianza del servidor y HTTP API de WordPress

Srv01 también necesita confiar en esa CA para sus peticiones HTTPS locales. Desde la carpeta de la PKI, instala **sólo el certificado público** en el almacén Debian del clon. Si ya existe un archivo homónimo, inspecciónalo y conserva su configuración antes de continuar:

```bash
sudo install -o root -g root -m 0644 ca.crt \
  /usr/local/share/ca-certificates/smr-lab-ca.crt
sudo update-ca-certificates
```

Esto añade confianza a los programas que utilizan el almacén del sistema en esa VM. La HTTP API de WordPress define por defecto su propio archivo `wp-includes/certificates/ca-bundle.crt`; por ello el cambio del almacén del SO puede no bastar para las peticiones del CMS a `wp.aula.test`. La API permite seleccionar `sslcertificates` y conservar `sslverify` mediante el filtro `http_request_args`. Son opciones documentadas en [WP_Http::request](https://developer.wordpress.org/reference/classes/wp_http/request/) y [http_request_args](https://developer.wordpress.org/reference/hooks/http_request_args/).

Para este laboratorio se incluye [smr-lab-ca.php](ejemplos/smr-lab-ca.php), un pequeño **must-use plugin**. Sólo actúa si `WP_ENVIRONMENT_TYPE` es `local`, el esquema es HTTPS, el host coincide exactamente con `wp.aula.test` y el puerto es 443 o implícito. Para esas peticiones selecciona el almacén Debian y fuerza verificación de certificado y nombre. Desactiva el seguimiento automático de redirecciones en esas peticiones locales: la URL canónica debe responder directamente, lo que evita trasladar esta configuración a destinos redirigidos. Las demás peticiones conservan sus argumentos.

Instálalo desde la raíz de este repositorio, sin modificar núcleo ni bibliotecas de terceros:

```bash
php -l segundo/aplicaciones-web/ejemplos/smr-lab-ca.php
sudo install -d -o root -g www-data -m 0750 \
  /srv/www/wp-aula/wp-content/mu-plugins
sudo install -o root -g www-data -m 0640 \
  segundo/aplicaciones-web/ejemplos/smr-lab-ca.php \
  /srv/www/wp-aula/wp-content/mu-plugins/smr-lab-ca.php
```

WordPress carga los archivos PHP de primer nivel de `mu-plugins` automáticamente; no requieren activación en el panel. El archivo permanece propiedad de root según el modelo de despliegue. Si el almacén no existe o el certificado es inválido, la petición debe fallar; no se establece `sslverify=false` ni se edita el bundle del núcleo. Esta solución es específica del clon Debian y su CA interna: no la distribuyas como configuración general de un sitio público. [Documentación de must-use plugins](https://developer.wordpress.org/advanced-administration/plugins/mu-plugins/).

## 7. Configurar Nginx y completar el asistente

Copia [wp-aula.nginx.conf](ejemplos/wp-aula.nginx.conf) a `/etc/nginx/sites-available/wp-aula` y revísalo. El listener se limita a `192.168.56.10`; el acceso al puerto debe permitirse únicamente desde LAB en el firewall de la VM. Si ya existe un gestor de firewall, añade la regla allí, sin mezclar herramientas.

### 7.1 Inspeccionar y retirar el sitio predeterminado del clon

En este **clon dedicado**, conserva primero una copia completa e inspecciona enlaces y configuración efectiva:

```bash
respaldo_nginx="/root/nginx-antes-wp-aula-$(date +%Y%m%d-%H%M%S)"
sudo cp -a /etc/nginx "$respaldo_nginx"
sudo ls -l /etc/nginx/sites-enabled/
sudo nginx -T
```

Registra el valor de `respaldo_nginx` en tu memoria privada. Revisa todas las directivas `listen`, no sólo las del archivo nuevo. Si existe el enlace estándar `sites-enabled/default` hacia `sites-available/default`, retira **sólo ese enlace**; el archivo de configuración original permanece disponible y está respaldado:

```bash
if [ -L /etc/nginx/sites-enabled/default ] && \
   [ "$(readlink -f /etc/nginx/sites-enabled/default)" = /etc/nginx/sites-available/default ]; then
    sudo unlink /etc/nginx/sites-enabled/default
else
    printf '%s\n' 'No se ha retirado ningún enlace: revisar la configuración real.'
fi
```

Si `default` es un archivo regular, apunta a otro destino o hay más sitios activos, detente a interpretar esa configuración: no elimines contenidos ajenos. En un servidor compartido este paso requiere planificar la coexistencia en lugar de desactivar el sitio de otra asignatura. La aceptación del clon dedicado exige que ningún otro bloque conserve `0.0.0.0:80`, `*:80`, `[::]:80` o listeners 443 fuera de LAB.

### 7.2 Activar, validar y comprobar listeners

```bash
sudo ln -s /etc/nginx/sites-available/wp-aula /etc/nginx/sites-enabled/wp-aula
sudo nginx -t
sudo systemctl reload nginx
sudo ss -lntp '( sport = :80 or sport = :443 )'
```

Si el enlace ya existe, inspecciónalo en lugar de sobrescribirlo. Sólo recarga cuando `nginx -t` termine correctamente. Los listeners de Nginx de este clon deben quedar en `192.168.56.10:80` y `192.168.56.10:443`, sin listeners wildcard IPv4/IPv6. Si quedan otros, identifica el bloque activo y corrígelo conservando la copia. La validación sintáctica no comprueba credenciales SQL ni funcionalidad editorial.

Primero comprueba la resolución **real de srv01** y la confianza del SO, sin sobrescribir DNS en curl:

```bash
getent ahostsv4 wp.aula.test
curl --cacert /etc/ssl/certs/ca-certificates.crt --head https://wp.aula.test/
```

La resolución debe producir `.10` y TLS debe verificarse correctamente. Para aislar después una incidencia de DNS, desde la VM y la carpeta de la CA puedes comparar con:

```bash
curl --cacert ca.crt --resolve wp.aula.test:443:192.168.56.10 \
  --head https://wp.aula.test/
```

Se espera una respuesta del sitio o una redirección al instalador, no necesariamente un 200 antes de completar la instalación. `--resolve` conserva el nombre de host y SNI mientras fija la IP; acceder a la dirección IP puede seleccionar otro servidor virtual. Esta comparación diagnóstica no sustituye la prueba anterior sin `--resolve`: por sí sola no demuestra que WordPress pueda resolver su nombre.

Abre `https://wp.aula.test/` desde el cliente confiado y completa el asistente. Utiliza un usuario administrador de laboratorio con contraseña única, desactiva el registro público si no se necesita y evita correo real. No interpretes «disuadir motores de búsqueda» como control de acceso: el aislamiento depende de red, firewall y autenticación.

Crea una cuenta editorial de menor privilegio, una página de inicio y dos entradas. Prueba publicación, subida de una imagen, cierre de sesión y lectura anónima. Verifica desde el navegador que las URLs usan HTTPS y el nombre correcto.

### 7.3 Comprobar peticiones internas y retirar los cambios de laboratorio

Después de completar la instalación, ejecuta en srv01 una petición mediante **la propia HTTP API de WordPress**, como el usuario del servicio:

```bash
sudo -u www-data php <<'PHP'
<?php
require '/srv/www/wp-aula/wp-load.php';
$respuesta = wp_remote_get( 'https://wp.aula.test/', array( 'timeout' => 10 ) );
if ( is_wp_error( $respuesta ) ) {
    fwrite( STDERR, $respuesta->get_error_message() . PHP_EOL );
    exit( 1 );
}
echo wp_remote_retrieve_response_code( $respuesta ), PHP_EOL;
PHP
```

Con la portada publicada y URL canónica correcta, se espera 200. Una respuesta 3xx exige revisar la URL o redirección, porque el plugin local no las sigue. Un error TLS exige comprobar CA, SAN, fecha, lectura del bundle y carga del mu-plugin. La prueba CLI complementa, pero no sustituye, `Herramientas → Salud del sitio`: comprueba allí las peticiones de bucle invertido y la API REST, pues se ejecutan mediante el entorno web/FPM. Revisa también los avisos de tareas programadas; WP-Cron depende de visitas o de un disparador planificado y una prueba TLS aislada no demuestra que todas las tareas se ejecuten.

Para revertir el laboratorio, retira únicamente `wp-content/mu-plugins/smr-lab-ca.php`, la entrada `WP_ENVIRONMENT_TYPE` añadida y el certificado público `/usr/local/share/ca-certificates/smr-lab-ca.crt`, y ejecuta `sudo update-ca-certificates --fresh`. Retira la confianza del cliente y las líneas hosts añadidas usando tu registro. Antes de reutilizar la VM con otro sitio, conserva las claves y copias necesarias según la política del ejercicio y deshabilita su servidor virtual.

Si necesitas volver al sitio Nginx inicial, mantén la red aislada, inspecciona y retira sólo el enlace `sites-enabled/wp-aula` creado por esta práctica y restaura el enlace `sites-enabled/default` desde su copia **si existía originalmente**. No restaures listeners wildcard en una VM expuesta. Valida con `nginx -t`, recarga sólo si es correcto y vuelve a comprobar `ss`. La copia completa permite recuperar otros ajustes que hayas documentado, sin sobrescribir cambios posteriores a ciegas.

## 8. Mantenimiento y actualización controlada

Mantén un inventario con núcleo, PHP, servidor, motor SQL, temas y complementos. Cada cambio debe tener motivo, versión origen/destino, copia previa, pruebas y reversión. Instala sólo extensiones necesarias desde fuentes oficiales; elimina las que no se usan después de comprobar que no aportan una dependencia.

Con el modelo de permisos de esta guía, el mantenimiento se realiza en una copia de pruebas mediante una identidad de despliegue con permisos adecuados. Para actualizar el núcleo:

1. Genera una copia coherente y comprueba que puedes restaurarla.
2. Reproduce el sitio en pruebas, con una base distinta y sin envíos de correo reales.
3. Descarga el artefacto oficial de la versión elegida y revisa las instrucciones de actualización manual de esa versión.
4. Sustituye los archivos del núcleo indicados por el procedimiento oficial, conservando `wp-config.php` y el contenido propio. No copies ciegamente una carpeta vacía sobre `wp-content` ni uses `rsync --delete` sin exclusiones verificadas.
5. Ejecuta la migración de base cuando el CMS la solicite, prueba roles, contenidos, enlaces y subida, y revisa registros.
6. Repite el cambio en el laboratorio principal sólo después de aceptar las pruebas. Conserva la combinación anterior para revertir archivos **y base** conjuntamente si la migración lo requiere.

No basta con devolver archivos antiguos después de una actualización que cambió el esquema SQL. La reversión debe recuperar un conjunto compatible. [Actualización de WordPress](https://wordpress.org/documentation/article/updating-wordpress/).

## 9. Copia consistente y restauración

En el laboratorio, anuncia una ventana y detén **el acceso a la aplicación** mientras haces la copia. Si Nginx atiende otros servicios en tu VM, no lo detengas sin aislar este sitio; usa un clon dedicado o un bloqueo temporal del servidor virtual documentado. Con un único sitio didáctico, detener Nginx y el pool FPM durante la ventana elimina nuevas escrituras de la aplicación; asegúrate de que no hay tareas programadas o herramientas externas que escriban.

Crea un directorio de copia fuera de `/srv/www`. Un ejemplo administrativo que solicita la contraseña si utilizas un usuario dedicado es:

```bash
sudo install -d -o root -g root -m 0700 /var/backups/smr-web
sudo sh -c 'umask 077; mariadb-dump --single-transaction --routines --triggers \
  wp_aula > /var/backups/smr-web/wp_aula.sql'
sudo tar -czf /var/backups/smr-web/archivos.tar.gz \
  -C /srv/www wp-aula
sudo cp /etc/nginx/sites-available/wp-aula /var/backups/smr-web/nginx.conf
```

La autenticación administrativa local por socket es la configuración de referencia de Debian; si la cambiaste, utiliza el mecanismo autorizado. `--single-transaction` ayuda a obtener una vista consistente de tablas transaccionales, pero no captura archivos ni garantiza coherencia con motores no transaccionales o cambios de estructura concurrentes. Por eso se pausa la aplicación y se documentan sus escritores. La copia de archivos contiene secretos: permisos, cifrado y acceso deben tratarla como material sensible.

Calcula hashes de los artefactos, guarda inventario y copia el conjunto a almacenamiento distinto. Verifica los comandos antes de reabrir la aplicación. No guardes una única copia con nombre fijo que se sobrescriba cada vez: crea directorios fechados y una retención definida.

La **prueba de restauración** se realiza en una VM aislada, con servicios compatibles: crea una base vacía, importa el SQL mediante el cliente MariaDB, restaura archivos conservando permisos, configura sus credenciales y URL de prueba y revisa contenido, roles, subidas y registros. Si cambias dominio, utiliza herramientas oficiales conscientes de datos serializados; un reemplazo de texto indiscriminado en el volcado puede corromper estructuras. Mantener el mismo nombre en una red de restauración separada simplifica la primera prueba.

Mide tiempo de recuperación y comprueba una entrada y una imagen creadas antes de la copia. Un archivo comprimido que existe no demuestra que el servicio pueda recuperarse. Consulta [copias de WordPress](https://developer.wordpress.org/advanced-administration/security/backup/).
