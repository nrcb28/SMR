# Fundamentos y arquitectura de los servicios

## 1. Qué significa que un servicio funcione

Que un paquete esté instalado sólo demuestra que existen archivos de software. Que un proceso esté activo no demuestra que escuche en la IP correcta. Que el puerto responda no demuestra que la aplicación devuelva datos válidos. Una comprobación completa recorre instalación, configuración, ejecución, escucha, acceso de red, protocolo, autorización y operación de usuario.

Un servidor puede escuchar en loopback, en una dirección concreta o en todas las interfaces. `127.0.0.1` limita el acceso IPv4 al propio equipo; `0.0.0.0` normalmente representa todas sus direcciones IPv4. En IPv6 `::` puede tener implicaciones de doble pila según aplicación y configuración. No deduzcas la exposición a partir de una única línea de configuración: comprueba sockets y prueba desde otro equipo.

El proceso se ejecuta con una identidad del sistema y accede a archivos según permisos. El servicio puede recibir configuración válida pero fallar porque no puede leer una clave o escribir una base de concesiones. Permisos Unix, AppArmor, unidades systemd y firewall pueden intervenir en puntos diferentes.

Documenta dependencias. Para resolver `www.aula.test` hace falta un mecanismo de resolución; para TLS hace falta un reloj razonable y un certificado adecuado; para SFTP hace falta autenticar y autorizar al usuario. Si cambias varias dependencias a la vez resulta difícil identificar la causa de un fallo.

## 2. Transporte, puertos y estado

TCP proporciona un flujo ordenado de bytes con control de retransmisión y congestión. La apertura habitual utiliza SYN, SYN/ACK y ACK. Una respuesta de rechazo inmediato y un silencio por filtrado no son el mismo síntoma. Una conexión TCP establecida tampoco demuestra que la aplicación haya autenticado al usuario.

UDP envía datagramas sin establecer una conexión TCP. La aplicación decide cómo detectar pérdidas o reintentar. DNS utiliza UDP con frecuencia, pero también requiere TCP en situaciones comunes; configurar sólo 53/UDP produce fallos parciales. DHCPv4 utiliza UDP y mecanismos de broadcast porque un cliente puede no tener IP utilizable al iniciar.

| Servicio | Transporte habitual | Función |
| --- | --- | --- |
| DNS | UDP y TCP 53 | Consultas y otras operaciones DNS |
| DHCPv4 | UDP 67 servidor / 68 cliente | Concesión de configuración IPv4 |
| SSH/SFTP | TCP 22 | Administración y transferencia sobre SSH |
| HTTP | TCP 80 | Peticiones web sin TLS |
| HTTPS | TCP 443; QUIC usa UDP en HTTP/3 | Web protegida por TLS |
| SMTP | TCP 25 entre servidores | Transferencia de correo |
| Submission | TCP 587 o 465 según diseño | Envío autenticado del usuario |
| IMAP | TCP 143 con STARTTLS o 993 con TLS implícito | Acceso a buzones |

Los puertos son convenciones; un proceso puede escuchar en otros. Cambiar un puerto no sustituye autenticación ni permisos. En la guía de correo se utiliza sólo loopback y no se despliega una infraestructura pública.

## 3. DNS: nombres, delegación y caché

DNS es una base de datos distribuida y jerárquica. Un nombre absoluto termina conceptualmente en la raíz: `srv01.aula.test.`. En archivos de zona, el punto final evita que un nombre se interprete como relativo al origen de la zona. Su omisión puede crear nombres inesperados como `srv01.aula.test.aula.test.`.

Un servidor autoritativo responde sobre zonas para las que mantiene datos. Un resolver recursivo realiza el trabajo de buscar respuestas para sus clientes y puede almacenarlas en caché. Un mismo producto puede hacer ambas funciones, pero mezclar roles aumenta complejidad y exposición. El laboratorio configura BIND como autoritativo local sin recursión; no se pretende convertirlo en resolver de Internet.

Los clientes pueden consultar distintos mecanismos: archivo hosts, resolver del SO, DNS configurado por adaptador o un mecanismo integrado en la aplicación como DNS sobre HTTPS. Una consulta explícita con `dig @servidor` verifica ese servidor, no prueba qué camino utiliza el navegador.

| Registro | Función | Precaución |
| --- | --- | --- |
| A | Nombre a dirección IPv4 | La existencia del registro no prueba que el host responda |
| AAAA | Nombre a dirección IPv6 | Publicarlo sin conectividad IPv6 puede causar fallos de doble pila |
| CNAME | Alias a otro nombre | No debe coexistir arbitrariamente con otros datos en el mismo nombre |
| MX | Servidor de correo de un dominio y preferencia | El destino es un nombre, no una IP |
| NS | Servidores autoritativos de la zona | El destino debe ser resoluble de forma coherente |
| SOA | Metadatos de autoridad, serial y temporizadores | El serial debe evolucionar al cambiar la zona |
| PTR | Dirección a nombre en zona inversa | No se crea automáticamente por añadir un A |
| TXT | Texto definido por aplicaciones | No equivale a una validación genérica de seguridad |

El TTL regula cuánto tiempo puede retenerse una respuesta en caché; no es el tiempo de vida del host. La caché negativa también existe y explica por qué un nombre recién añadido puede seguir pareciendo inexistente para un cliente.

`NXDOMAIN` significa que el nombre no existe en la respuesta considerada. `NOERROR` con conjunto de respuesta vacío puede indicar que existe el nombre pero no el tipo solicitado. `SERVFAIL` indica un fallo al procesar la resolución, con múltiples posibles causas. Leer únicamente «no devolvió una IP» pierde estas diferencias.

Una zona inversa IPv4 usa octetos en orden inverso dentro de `in-addr.arpa`. Para `192.168.56.0/24`, el origen es `56.168.192.in-addr.arpa` y el nombre `10` representa `192.168.56.10`. Prefijos no alineados en /24 pueden requerir técnicas de delegación adicionales; no generalices este ejemplo a cualquier subred.

## 4. DHCP: concesión y coherencia

DHCPv4 intercambia normalmente Discover, Offer, Request y ACK para que un cliente obtenga una concesión. Un servidor no debe ofrecer cualquier dirección libre a simple vista: necesita un pool coherente, exclusiones, estado de concesiones y reglas para reservas.

La IP de un servidor DNS o de un equipo con configuración fija debe quedar fuera del pool. Si el rango dinámico incluye `192.168.56.10` y ese equipo tiene la misma IP estática, puede aparecer duplicidad. Una reserva por MAC o identificador no es una autenticación fuerte: esos identificadores pueden cambiar o falsificarse.

El servidor ofrece opciones: máscara, DNS, dominio y, si existe un router, gateway. En el laboratorio no existe router en LAB; por tanto, no se envía una opción de routers ficticia. Una VM con NIC NAT puede mantener su ruta por defecto a través de esa otra interfaz.

La concesión dura un tiempo. El cliente intenta renovarla antes de que expire y puede reutilizar valores previos conforme al protocolo. Detener el servidor no retira inmediatamente todas las IP concedidas. Para comprobar renovación hay que observar el intercambio y el estado, no asumir que cualquier IP visible acaba de asignarse.

Un relay permite atravesar límites de broadcast entre subredes, pero requiere configuración explícita y selección correcta de pools. No se incluye en el diseño base. En IPv6, DHCPv6 tiene mensajes y opciones diferentes y no sustituye sin más a Router Advertisements.

## 5. Acceso remoto y transferencia

SSH negocia cifrado, verifica la identidad del servidor mediante su clave de host y autentica al cliente. La primera conexión debe contrastar la huella por un canal independiente, por ejemplo la consola de la VM. Aceptar cualquier huella sin comprobarla elimina gran parte de la protección frente a suplantación.

Las claves de host y las claves de usuario cumplen funciones distintas. Una clave privada de usuario debe permanecer en el cliente autorizado; el servidor recibe la pública. Una reinstalación puede cambiar la clave de host y provocar una advertencia legítima, pero también puede existir suplantación: investiga antes de borrar `known_hosts`.

SFTP transporta operaciones de archivos dentro de SSH. No es FTP con cifrado TLS. FTP utiliza conexiones de control y de datos separadas; FTPS añade TLS a FTP y requiere considerar modo activo/pasivo y sus puertos. Para transferencias sencillas de administración se utiliza SFTP en esta guía, evitando desplegar FTP sin cifrado.

El permiso de autenticar no implica permiso de escribir cualquier archivo. Un usuario SFTP sigue sujeto a propiedad, permisos y restricciones del servidor. Si se diseña un chroot, los requisitos de propiedad del directorio raíz de la jaula deben cumplirse; dar escritura global para evitar un error rompe el modelo.

## 6. HTTP, TLS y nombres

HTTP define métodos, rutas, cabeceras y códigos de respuesta. `200` indica éxito del recurso solicitado; `301/308` son redirecciones; `403` deniega acceso; `404` no encuentra el recurso en el contexto de la aplicación; `502` suele relacionarse con una respuesta problemática del upstream en un proxy. El diagnóstico debe leer el servidor y ruta seleccionados, no sólo el número.

En hosting virtual varios nombres pueden compartir IP. HTTP incluye el nombre de destino y TLS suele usar SNI durante la negociación para seleccionar certificado. Una prueba por IP puede recibir otro sitio o un certificado cuyo nombre no coincide.

TLS protege confidencialidad e integridad durante el transporte y autentica según la cadena de confianza y el nombre validado. No certifica que el contenido sea bueno ni corrige permisos de la aplicación. Un certificado para `www.aula.test` no valida automáticamente una conexión a `192.168.56.10`.

En un laboratorio puede usarse una CA privada o un certificado autofirmado con confianza explícita. El dominio `.test` está reservado para pruebas y no se solicita como nombre público a una CA de Internet. La guía utiliza un certificado de laboratorio con SAN y comprobación mediante `curl --cacert`; no enseña a ignorar globalmente errores TLS.

## 7. Correo, tiempo y operación

El envío de correo involucra un cliente de usuario, un servidor de envío, servidores de transferencia y un almacén de buzones. SMTP transmite; IMAP o POP acceden a buzones. MX informa sobre destinos de transferencia, pero no configura cuentas ni concede permiso de relay.

Un servidor que retransmite mensajes de cualquiera a cualquier destino puede convertirse en open relay. Para aprender la arquitectura no hace falta publicar 25/TCP ni permitir retransmisión: el laboratorio de esta asignatura trabaja exclusivamente con el propio host. La entrega real en Internet añade DNS inverso, reputación, SPF, DKIM, DMARC, políticas de proveedores y gestión de abuso.

La hora coherente ayuda a interpretar logs y validar certificados. No se necesita desplegar un servidor NTP para cada práctica, pero sí comprobar que el SO sincroniza con una fuente apropiada mediante el servicio de tiempo elegido. Las capturas de varios equipos deben incluir zona horaria para correlacionarse.

Un servicio debe tener propietario, copia de seguridad, procedimiento de restauración y criterio de aceptación. Respaldar sólo configuración puede omitir datos críticos: concesiones DHCP, zonas dinámicas, claves, buzones o contenido web. Guarda las claves fuera de repositorios públicos y prueba una restauración controlada.

## Referencias primarias

- [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) y [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035): DNS.
- [RFC 2131: DHCPv4](https://www.rfc-editor.org/rfc/rfc2131).
- [RFC 4251: arquitectura SSH](https://www.rfc-editor.org/rfc/rfc4251).
- [RFC 9110: semántica HTTP](https://www.rfc-editor.org/rfc/rfc9110).
- [RFC 8446: TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446).
- [RFC 5321: SMTP](https://www.rfc-editor.org/rfc/rfc5321).
- [RFC 6761: nombres de uso especial](https://www.rfc-editor.org/rfc/rfc6761).
