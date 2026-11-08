# Correo local: arquitectura, entrega y límites

Este laboratorio observa SMTP, cola y entrega local dentro de una única VM desechable. No publica correo en la red ni intenta enviar a Internet. Complementa la arquitectura del módulo: no constituye una receta de servidor de correo de producción ni demuestra IMAP, reputación o entrega entre organizaciones.

## 1. Recorrido de un mensaje

Un MUA redacta el correo. Un servicio de submission autentica al usuario cuando el envío procede de un cliente de red. Un MTA acepta y transporta; un agente de entrega coloca el mensaje en el buzón. IMAP permite consultar y sincronizar ese buzón, mientras que POP ofrece otro modelo de acceso.

En esta práctica `sendmail`, proporcionado por Postfix, introduce un mensaje localmente sin una sesión SMTP de usuario. Postfix lo procesa y entrega a un usuario local en formato Maildir. Una segunda prueba habla SMTP sólo con `127.0.0.1` para distinguir ambos caminos.

El dominio `aula.test` identifica datos de laboratorio. Un MX dentro del BIND de la asignatura explica cómo se publicaría el destino de un dominio, pero no obliga a Postfix a escuchar en la IP LAB. En este ejercicio SMTP permanecerá en loopback.

## 2. Preparación

Utiliza una VM separada si ya hay un MTA o buzones importantes. Conserva instantánea y consola. Instala `postfix` desde el repositorio de Debian y selecciona la modalidad **Local only / Sólo correo local** en el diálogo del paquete. No selecciones «Internet Site» para seguir este ejercicio.

Después de instalar, detén Postfix y desconecta los adaptadores de red de la VM mientras preparas la configuración. No necesitas red para las pruebas de loopback. Guarda `/etc/postfix/main.cf` y `master.cf` antes de editar. Comprueba versión con `postconf mail_version`.

Crea un usuario exclusivamente para el buzón:

~~~bash
sudo adduser --disabled-password --gecos "" labmail
~~~

Si ya existe, inspecciónalo y elige otro nombre en vez de modificar una cuenta real. Esta cuenta no necesita acceso SSH. Un usuario de sistema y una dirección de correo son conceptos distintos, aunque esta configuración utilice usuarios locales como destinatarios.

## 3. Configuración mínima

Las siguientes líneas son parámetros de `/etc/postfix/main.cf`. Conserva los demás ajustes del paquete y sustituye cualquier definición previa de estos parámetros; no acumules copias contradictorias:

~~~text
myhostname = srv01.aula.test
mydomain = aula.test
myorigin = $mydomain
mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain
inet_interfaces = loopback-only
mynetworks = 127.0.0.0/8, [::1]/128
relayhost =
relay_domains =
smtpd_relay_restrictions = reject_unauth_destination
home_mailbox = Maildir/
mailbox_command =
default_transport = error:salida externa deshabilitada en laboratorio
relay_transport = error:relay deshabilitado en laboratorio
~~~

`inet_interfaces` restringe escucha. `mydestination` identifica dominios que se entregan localmente. La política SMTP rechaza destinos no autorizados y los transportes de error impiden que la cola local utilice los transportes normales para destinos externos o relay. Estas medidas son deliberadamente redundantes para que el ejercicio no dependa de una red NAT.

No se incluye `permit_mynetworks` en la regla SMTP de este ejercicio porque se desea rechazar destinos no locales incluso desde loopback. Para una infraestructura real las políticas de submission, autenticación y transferencia se diseñan por separado; no copies estas restricciones como configuración universal.

Revisa `master.cf` para asegurar que no existe otra escucha con IP explícita que amplíe el alcance. Tampoco habilites submission, SMTPS o interfaces de administración para este laboratorio.

~~~bash
sudo postfix check
sudo systemctl restart postfix
sudo postconf -n
sudo ss -lntp
~~~

Un cambio en `inet_interfaces` requiere detener/iniciar el servicio; no dependas sólo de recargarlo. La escucha SMTP debe corresponder únicamente a loopback. Si aparece `0.0.0.0:25` o la IP LAB, detén Postfix y corrige antes de continuar.

Las instalaciones Debian pueden utilizar varias unidades de instancia Postfix. Consulta `systemctl list-units 'postfix*'` y no interpretes un wrapper «active (exited)» como prueba suficiente de que el proceso de la instancia responde.

## 4. Mensaje local y buzón

En una terminal del usuario de práctica, introduce un mensaje sintético:

~~~bash
printf 'From: alumno@aula.test\nTo: labmail@aula.test\nSubject: Prueba local SMR\n\nMensaje de laboratorio sin datos personales.\n' | /usr/sbin/sendmail -i labmail@aula.test
~~~

El comando usa la interfaz local de envío. `-i` evita que una línea con un único punto finalice por sí misma esa entrada; no debe confundirse con el intercambio SMTP manual.

Observa la cola:

~~~bash
mailq
sudo find /home/labmail/Maildir/new -maxdepth 1 -type f
~~~

El buzón Maildir se crea al producirse una entrega correcta. Si el directorio no aparece, consulta logs, estado del usuario, `home_mailbox` y permisos; no crees un directorio con escritura global para ocultar el fallo. Inspecciona únicamente el fichero de prueba identificado y comprueba cabeceras y cuerpo.

Los logs pueden estar en journal o en archivos gestionados por syslog según instalación. Comprueba `journalctl` y, si está configurado, `/var/log/mail.log`. Registra el identificador de cola y sigue sus eventos. Una cola vacía no basta como evidencia: el mensaje puede haberse entregado, rechazado o devuelto.

## 5. Conversación SMTP en loopback

Si tienes un cliente como `nc` instalado antes de desconectar la red, conecta con `nc 127.0.0.1 25` y escribe, esperando la respuesta a cada paso:

~~~smtp
EHLO cliente.aula.test
MAIL FROM:<alumno@aula.test>
RCPT TO:<labmail@aula.test>
DATA
From: alumno@aula.test
To: labmail@aula.test
Subject: Segunda prueba SMTP

Mensaje sintetico enviado por loopback.
.
QUIT
~~~

Se espera aceptación del destinatario local y del contenido. Los códigos precisos pueden incluir texto distinto según versión. Explica `250` como aceptación de una etapa, `354` como invitación a aportar datos y `221` como cierre. Un `250` tras DATA significa que el servidor aceptó responsabilidad sobre el mensaje; no certifica que cualquier destinatario humano lo haya leído.

Para el caso negativo inicia otra conversación, indica un remitente de prueba y ejecuta `RCPT TO:<destino@externo.test>`. Debe rechazarse el destino no local. No envíes DATA y no intentes dominios reales. Si se acepta por una regla adicional, detén el ejercicio, inspecciona configuración efectiva y corrige antes de reconectar adaptadores.

## 6. Qué falta para IMAP y correo real

Un lector IMAP no encontrará automáticamente un servicio sólo porque Postfix entregó Maildir. Hace falta un servidor de acceso a buzones, por ejemplo Dovecot, con ubicación de correo, identidad de usuarios, autenticación, TLS y permisos coherentes. Sus versiones tienen diferencias de configuración; utiliza la documentación correspondiente a la versión instalada en vez de copiar recetas de otra rama.

Como ampliación controlada, podría instalarse un servidor IMAP limitado inicialmente a loopback, comprobar que lee el Maildir de labmail y probar después acceso desde una red aislada con TLS. Eso requiere una práctica propia y no se considera completado aquí.

Para correo de Internet también hacen falta dominio real, DNS y PTR adecuados, acceso a puertos, políticas de proveedor y mecanismos como SPF, DKIM y DMARC. Estos mecanismos no son intercambiables: autorizan origen, firman mensajes y expresan políticas de alineación/evaluación, respectivamente. Ninguno garantiza por sí solo entrega o ausencia de spam.

## 7. Entrega, recuperación y evaluación

Entrega esquema de componentes, configuración saneada, escucha loopback, identificador de cola, mensaje sintético recibido y rechazo de un destinatario externo de prueba. Explica qué parte de la arquitectura se ha demostrado y cuál permanece como diseño.

Al finalizar detén Postfix si ya no se utiliza, restaura la instantánea o la configuración previa y conserva sólo las evidencias sintéticas necesarias. No borres colas globales ni buzones de otras cuentas. Si eliminas la cuenta de práctica, revisa primero sus archivos y usa el procedimiento normal de administración de usuarios.

La práctica se supera cuando puedes seguir el mensaje desde aceptación hasta archivo de buzón, distinguir envío local de SMTP, probar el rechazo previsto y confirmar que no hay escucha fuera de loopback.

## Referencias primarias

- [Postfix: configuración básica](https://www.postfix.org/BASIC_CONFIGURATION_README.html).
- [Postfix: parámetros](https://www.postfix.org/postconf.5.html).
- [Postfix: control de acceso SMTP](https://www.postfix.org/SMTPD_ACCESS_README.html).
- [Postfix: agente local](https://www.postfix.org/local.8.html).
- [Dovecot: documentación oficial](https://doc.dovecot.org/).
- [RFC 5321: SMTP](https://www.rfc-editor.org/rfc/rfc5321).
