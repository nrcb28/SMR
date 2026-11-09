# Acceso remoto, PKI y publicación web mantenible

[Índice de Servicios en red](README.md) · [Guía inicial](02-guia-tecnica.md) · [Seguridad informática](../seguridad-informatica/README.md)

## 1. Diseñar el acceso antes de restringirlo

Una política de acceso remoto define identidades, origen, método de autenticación, privilegios y recuperación. Desactivar contraseñas es una medida incompleta si nadie ha comprobado la clave pública, la identidad del servidor o la consola de emergencia. Un administrador puede endurecer tanto un servicio que quede inaccesible para el propio equipo responsable.

El escenario conserva `srv01/.10`, `cli01/.20` y LAB aislada. Utiliza la consola del hipervisor durante cambios de SSH y mantén una sesión existente mientras pruebas otra. Una sesión que ya estaba autenticada no demuestra que una sesión nueva pueda abrirse después del cambio. No cierres el último acceso operativo hasta comprobar la aceptación y el procedimiento de retorno.

Separa la clave de host del servidor y la clave de usuario del cliente. La primera permite reconocer a qué servidor te conectas; la segunda prueba posesión de la credencial de una identidad autorizada. Rotar una no rota automáticamente la otra y ambas tienen inventarios y procedimientos de baja distintos.

## 2. Verificar configuración efectiva de OpenSSH

En Debian, el servicio del paquete suele ser `ssh`, pero el daemon se llama `sshd`. Identifica unidad y archivo reales. Los archivos incluidos y el orden de opciones importan: no asumas que una línea al final siempre sobrescribe lo anterior. OpenSSH aplica reglas de obtención de valores que deben comprobarse en su manual y en la configuración efectiva.

```bash
sudo /usr/sbin/sshd -t
sudo /usr/sbin/sshd -T -C user=alumno,host=cli01,addr=192.168.56.20,laddr=192.168.56.10,lport=22
```

`-t` valida sintaxis y condiciones requeridas de claves; `-T` presenta configuración efectiva. `-C` aporta contexto para evaluar bloques `Match`. La salida debe guardarse de forma privada y revisarse buscando las opciones relevantes; no equivale a una prueba de red o autenticación real.

Un diseño de laboratorio puede restringir escucha a `.10`, denegar inicio directo de root, utilizar claves públicas y limitar usuarios. Antes de aplicarlo, instala y comprueba la clave de `alumno` con permisos correctos en su cuenta. No escribas un archivo completo que borre ajustes propios del paquete; modifica la configuración prevista y contrasta el efecto con `sshd -T`.

```text
ListenAddress 192.168.56.10
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
KbdInteractiveAuthentication no
AllowUsers alumno
```

Este bloque es una selección de directivas, no una política universal. Si ya hay `ListenAddress` adicionales, revisa si continúan activas; si el usuario real tiene otro nombre, ajusta `AllowUsers` antes de recargar. El bloqueo de contraseña sólo se acepta después de abrir una sesión nueva por clave desde el origen permitido. Conserva procedimiento de consola para restaurar el archivo anterior.

## 3. Claves, agentes y cambios de identidad

Una clave privada debe permanecer en el cliente o mecanismo de custodia previsto, con frase de paso apropiada al flujo de uso. No copies la misma clave privada a cada servidor para «facilitar acceso». Una clave pública autorizada en varios destinos debe tener propietario, finalidad y procedimiento de revocación. La baja consiste en retirar autorización en los destinos pertinentes, no sólo borrar un archivo del portátil.

El agente facilita el uso de claves desbloqueadas. Reenviar el agente a otros equipos cambia el modelo de confianza: un destino comprometido puede abusar de ciertas capacidades mientras exista acceso al agente. No habilites `ForwardAgent yes` globalmente como solución de comodidad. Un salto con `ProxyJump` puede resolver acceso sin copiar claves privadas al bastión ni reenviar el agente indiscriminadamente.

Ejemplo de configuración **del cliente**, en su archivo SSH personal:

```text
Host smr-servidor
    HostName 192.168.56.10
    User alumno
    IdentityFile ~/.ssh/id_ed25519_smr
    IdentitiesOnly yes
    ForwardAgent no
```

El archivo de clave indicado debe existir y pertenecer a esa cuenta. `IdentitiesOnly` evita presentar todas las identidades del agente, pero no protege por sí mismo una clave sin custodia. Una conexión fallida se investiga con `ssh -v` y registros del servidor, evitando publicar nombres de usuario, rutas personales o metadatos innecesarios de un entorno real.

Si cambia la clave de host tras reinstalar una VM, comprueba la nueva huella desde la consola y relaciona el cambio con una intervención autorizada. No respondas automáticamente borrando todo `known_hosts` o desactivando comprobación estricta. Retira sólo la entrada del host de laboratorio después de validar su identidad. Una alerta puede ser esperable por reinstalación o indicar un problema; el procedimiento decide cuál con evidencia.

## 4. Transferencia SFTP con alcance limitado

SFTP opera sobre SSH y no necesita publicar los puertos de FTP. Una cuenta de intercambio puede requerir transferencia sin shell general. La configuración debe separar la raíz del chroot, propiedad de root y no modificable por el usuario, de la carpeta donde éste escribe. Dar propiedad de todo el chroot al usuario rompe las condiciones de seguridad que verifica SSH.

Escenario adicional dentro de una copia de `srv01`: cuenta `intercambio` preparada por el administrador, con su grupo homónimo y clave pública válida. El árbol `/srv/sftp` no se reutiliza si contiene datos de otras prácticas. Crea la jerarquía con componentes padres que cumplan los requisitos:

```bash
sudo install -d -o root -g root -m 0755 /srv/sftp
sudo install -d -o root -g root -m 0755 /srv/sftp/intercambio
sudo install -d -o intercambio -g intercambio -m 0750 /srv/sftp/intercambio/datos
namei -l /srv/sftp/intercambio/datos
```

La política debe autorizar `intercambio` si `AllowUsers` está limitado. Añade un bloque `Match` según la estructura real del archivo y valida su contexto, sin arrastrar directivas a usuarios no previstos:

```text
Match User intercambio
    ChrootDirectory /srv/sftp/intercambio
    ForceCommand internal-sftp -d /datos
    DisableForwarding yes
    PermitTTY no
    PermitTunnel no
```

`ForceCommand` limita el comando de sesión, pero no desactiva por sí solo reenvíos de puertos o sockets. `DisableForwarding yes` elimina esas vías, incluidos agente, X11 y sockets UNIX, para esta cuenta dedicada. `PermitTTY no` evita asignar un terminal y `PermitTunnel no` mantiene deshabilitado el túnel de red. Verifica la configuración efectiva para ese usuario y prueba una sesión SFTP nueva. Debe poder escribir en `/datos`, no modificar la raíz y no obtener una shell general. Prueba con un archivo sintético conocido y compara hash después de recuperar. La aceptación incluye rechazo a escribir fuera del área prevista y cierre del acceso cuando se retira la autorización.

El chroot no es una garantía absoluta de aislamiento de cualquier fallo del software o del kernel. Define un alcance concreto de acceso y reduce acciones; su seguridad depende también de versiones, permisos y servicio. No lo presentes como sustituto de separación de máquinas o contenedores cuando los requisitos exijan otra frontera.

## 5. Ciclo de vida de un certificado

Un certificado de servidor relaciona una clave pública con nombres y condiciones de validez bajo una autoridad. La clave privada es el elemento que debe protegerse; el certificado público puede distribuirse para validación. Cadena, SAN, fechas, algoritmos y uso extendido tienen funciones diferentes. Un certificado no se vuelve correcto sólo porque el archivo termine en `.crt`.

En el laboratorio `.test` se utiliza una CA propia, siguiendo la guía inicial o la práctica web. No se solicita un certificado público para un dominio reservado que no controlas como nombre de producción. Mantén la clave de CA fuera del árbol web, con permisos restrictivos, y no instales confianza de laboratorio en equipos ajenos.

Registra: emisor, número de serie, SAN, inicio/fin de validez, ubicación de archivos, servicio que los utiliza, responsable y fecha de renovación. Una alerta de vencimiento debe dejar margen para generar, distribuir y verificar, no avisar cuando el certificado ya ha caducado. El plazo de aviso concreto se adapta a la política y al mecanismo de emisión.

```bash
openssl x509 -in /etc/ssl/certs/aula.crt -noout -subject -issuer -dates -ext subjectAltName
openssl x509 -in /etc/ssl/certs/aula.crt -noout -checkend 604800
```

Sustituye `aula.crt` por el archivo realmente configurado; si la guía previa usó otro nombre, no inventes uno nuevo sin actualizar el servidor. `604800` representa siete días en segundos. El código de salida ayuda a automatizar la comprobación, pero no valida por sí solo cadena, nombre del servicio o contenido entregado por Nginx.

## 6. Diagnóstico TLS desde el cliente

```bash
openssl s_client -connect 192.168.56.10:443 -servername www.aula.test \
  -CAfile ca.crt -verify_hostname www.aula.test -verify_return_error </dev/null
curl --cacert ca.crt --resolve www.aula.test:443:192.168.56.10 https://www.aula.test/
```

Los nombres y la CA deben coincidir con el certificado de tu práctica. `-servername` aporta SNI; `-verify_hostname` comprueba el nombre; la CA establece confianza. En `curl`, `--resolve` conserva URL y SNI y fija destino para esa ejecución. Después repite sin esa opción para verificar DNS real. No aceptes `-k` como solución de una cadena inválida.

Si la aplicación usa su propio almacén de CA, configurar el navegador o el SO puede no bastar. El ejemplo de WordPress de [Aplicaciones web](../aplicaciones-web/README.md) explica una selección de confianza restringida para su HTTP API. La prueba pertinente debe ejecutarse también desde el propio mecanismo que hará la petición, no sólo desde el terminal del administrador.

Un servidor puede presentar una cadena distinta de la almacenada en el disco porque no se recargó, se consultó otro virtual host o hay otro proxy delante. Compara certificado observado y configuración efectiva. Un `nginx -t` correcto confirma sintaxis y ciertos accesos a archivos, pero no garantiza que el usuario esté llegando al sitio y nombre esperados.

## 7. Rotar certificado y clave de forma recuperable

Trabaja en una carpeta privada de preparación, con nombres nuevos y sin sobrescribir la única clave anterior. Genera nueva pareja y certificado conforme a la política de CA del laboratorio. Valida que clave y certificado correspondan mediante su clave pública, revisa SAN/fechas y verifica cadena. No publiques la clave ni su salida privada como evidencia.

Instala archivos con permisos adecuados y cambia referencias del sitio de pruebas. Valida configuración y recarga Nginx sólo cuando sea correcta. Abre una conexión nueva desde cliente y observa el certificado servido; una conexión TLS existente puede seguir utilizando el contexto anterior. Después prueba contenido, autorización y servicios dependientes.

El retorno consiste en restituir referencias a los archivos anteriores aún válidos, validar y recargar. Conserva una ventana de observación y registra qué certificado presenta cada componente si existe proxy. No destruyas inmediatamente la clave previa antes de completar aceptación; su retención o destrucción posterior depende de política y necesidades justificadas.

Un certificado renovado con la misma fecha de vencimiento o con SAN erróneo no cumple el cambio. Acepta la operación por propiedades observadas, no por la ausencia de error del comando que generó el archivo. Incluye una comprobación desde un cliente limpio o con una conexión nueva.

## 8. Proxy inverso y límites de confianza

Un proxy recibe peticiones y las dirige a un backend. El cliente ve la dirección del proxy; la aplicación puede necesitar información del nombre, esquema y origen. Las cabeceras reenviadas sólo deben confiarse desde proxies autorizados. Si una aplicación acepta como identidad cualquier `X-Forwarded-For` enviado por un cliente, puede registrar o usar un origen falso.

Escenario separado: un backendsintético escucha sólo en `127.0.0.1:8080` dentro de una VM clonada y Nginx publica únicamente LAB. No se sustituye sin revisión el sitio de WordPress. Un fragmento conceptual de localización es:

```nginx
location /demo/ {
    proxy_pass http://127.0.0.1:8080/;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-For $remote_addr;
    proxy_connect_timeout 3s;
    proxy_read_timeout 15s;
}
```

La barra final de `proxy_pass` y la URI de la localización afectan a cómo se transforma el camino. Define si `/demo/x` debe llegar como `/x` y pruébalo; no copies una configuración de otra ruta suponiendo equivalencia. Los tiempos son hipótesis didácticas y deben ajustarse a la aplicación. Un timeout corto puede rechazar tareas legítimas; uno excesivo puede retener recursos.

El backend del ejemplo es local y no necesita quedar expuesto en todas las interfaces. Verifica listeners, sitio predeterminado de Nginx y configuración activa completa. Un proxy correctamente limitado no protege si el puerto del backendsigue abierto directamente a una red no prevista.

## 9. Caché y control de solicitudes

La caché de proxy puede reducir carga para respuestas reutilizables. No debe habilitarse globalmente para páginas personalizadas o autenticadas sin reglas que definan claves, exclusiones y tratamiento de cookies/autorización. Servir datos de una persona a otra por una clave de caché insuficiente es un fallo grave de diseño.

Empieza con contenido estático sintético y verifica hit/miss mediante registros o una cabecera de diagnóstico sólo de laboratorio. Cambia un recurso y observa vencimiento/invalidez. Explica diferencias entre caché de navegador, proxy y aplicación. Borrar una caché no actualiza automáticamente todas las demás.

Nginx permite limitar tasa mediante una zona compartida definida en el contexto `http` y una aplicación en `server` o `location`. Un bloque fuera de contexto no arrancará aunque su sintaxis aislada parezca razonable:

```nginx
# Dentro de http, no dentro de location:
limit_req_zone $binary_remote_addr zone=smr_demo:1m rate=5r/s;

# Dentro de la location de prueba:
limit_req zone=smr_demo burst=10 nodelay;
limit_req_status 429;
```

Son valores didácticos para una aplicación propia. En un aula tras NAT, varios usuarios pueden compartir IP y recibir un límite agregado. Limitar por IP no es lo mismo que limitar por usuario autenticado. Prueba pocos intentos controlados y evita herramientas de carga masiva; observa el 429, el registro y el retorno al estado normal.

## 10. Práctica avanzada y aceptación

Elige una de dos rutas: acceso SFTP limitado o rotación TLS con proxy de demostración separado. Entrega estado inicial, archivo modificado, validación, prueba positiva, rechazo esperado y retorno. Si completas ambas, conserva escenarios o instantáneas independientes para atribuir efectos.

Para SSH, una sesión nueva por clave y una denegación de la cuenta no autorizada son esenciales. Para TLS, exige coincidencia de nombre, cadena válida y certificado nuevo servido. Para proxy, demuestra que backend no es accesible por LAB, que la ruta se transforma como se diseñó y que el límite de solicitudes no se confunde con un fallo de autenticación.

La rúbrica propia asigna 20% diseño de confianza,25% ejecución explicada,30% aceptación/negativos y 25% recuperación/evidencias. No se considera un éxito mantener accesibilidad desactivando validación TLS, abriendo permisos globales o dejando una segunda escucha fuera de LAB.

## Referencias primarias

- [OpenSSH: sshd_config](https://man.openbsd.org/sshd_config).
- [OpenSSH: ssh_config](https://man.openbsd.org/ssh_config).
- [OpenSSL: s_client](https://docs.openssl.org/3.5/man1/openssl-s_client/).
- [OpenSSL: x509](https://docs.openssl.org/3.5/man1/openssl-x509/).
- [Nginx: proxy HTTP](https://nginx.org/en/docs/http/ngx_http_proxy_module.html).
- [Nginx: límite de solicitudes](https://nginx.org/en/docs/http/ngx_http_limit_req_module.html).
- [RFC 5280: certificados y PKI](https://www.rfc-editor.org/rfc/rfc5280).
- [RFC 8446: TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446).
