# Complementos de servicios exigidos por los RA

[Alineación RA/CE](10-alineacion-ra.md) · [Retos](11-retos-por-ra.md) · [Índice](README.md)

Los RA incluyen funciones que no quedan demostradas únicamente con DNS autoritativo, SFTP, una página HTTPS y correo entregado a un archivo local. Este capítulo desarrolla caché recursiva, FTP, acceso IMAP, escritorio remoto y una pasarela con proxy. Las configuraciones son propuestas para VMs y equipos de formación; no se han desplegado durante la elaboración de estas guías.

## 1. Caché DNS controlada · RA2.e

Usa una copia de `srv01` con `.56.10`, sin controlador AD y con el diseño BIND básico ya comprobado. La NIC LAB sigue sin gateway; la NIC NAT puede dar salida para consultas. Conserva configuración previa y revisa reglas del entorno: algunos centros exigen un resolver ascendente autorizado en lugar de consultas iterativas directas.

En el único bloque `options` efectivo, configura escucha y clientes de recursión. Este ejemplo admite loopback y el cliente concreto; si añades clientes, documenta la nueva población. No pegues un segundo bloque `options` ni combines este ejercicio automáticamente con todas las réplicas anteriores:

```text
acl "clientes_ra2" { 127.0.0.1; 192.168.56.20; };
options {
    directory "/var/cache/bind";
    listen-on { 127.0.0.1; 192.168.56.10; };
    listen-on-v6 { none; };
    allow-query { clientes_ra2; };
    recursion yes;
    allow-recursion { clientes_ra2; };
    allow-query-cache { clientes_ra2; };
    dnssec-validation auto;
    allow-transfer { none; };
    dump-file "/var/cache/bind/ra2-cache.db";
};
```

Conserva las zonas propias en su archivo de inclusión. Si la red requiere forwarding, añade únicamente los servidores autorizados después de identificarlos, sin inventar una IP universal de NAT. Valida con `named-checkconf`, recarga según el servicio instalado y verifica listeners. La ACL de aplicación y el firewall limitan el ejercicio a LAB.

Consulta desde `.20` un nombre público permitido, por ejemplo `www.debian.org`, y repite. Registra estado, flags, TTL y servidor consultado. Dos respuestas rápidas no prueban por sí solas caché. En el servidor, `sudo rndc dumpdb -cache` produce el archivo definido; examina únicamente la entrada de prueba, sin publicar una caché completa con consultas ajenas. No vacíes globalmente una caché de trabajo para conseguir un primer fallo.

Prueba recursión desde una VM de laboratorio fuera de la ACL y documenta denegación sin ampliar acceso. La autoridad de `aula.test` y la recursión son funciones distintas: que una funcione no prueba la otra. Restaura la política autoritativa inicial cuando termine este escenario. Contrasta las opciones con el [BIND ARM](https://bind9.readthedocs.io/en/stable/reference.html).

## 2. FTP anónimo, usuarios y canales activo/pasivo · RA3

### Aislamiento y preparación

FTP clásico transmite información sin la protección de SFTP. Aquí se observa su funcionamiento únicamente en una VM dedicada `ftplab`, IP `.56.40/24`, con datos sintéticos y credenciales temporales. Desconecta su NIC NAT y cualquier puente antes de iniciar el servicio, tras instalar paquetes desde repositorios oficiales. La dirección `.40` es una extensión de esta práctica y debe estar libre; no reemplaza `.30` de DNS ni `.50` de la reserva DHCP.

Prepara `vsftpd`, un cliente CLI y un cliente gráfico disponible en el centro. Consulta `man vsftpd.conf` de la versión instalada. Crea grupo `ftp_ra3`, cuenta de prueba `lector_ra3` con ese grupo y contraseña mediante solicitud interactiva. En esta VM exclusiva puede emplearse una shell admitida por PAM, sin habilitar por ello SSH. Comprueba antes que esos objetos no existan y que no contienen información anterior.

Crea `/srv/ftp-ra3` con propietario root y modo `0555`, y un archivo público de lectura. Prepara el directorio personal de la cuenta con propietario root, modo `0755` y un archivo distinto de lectura. Así el directorio raíz del chroot no es escribible por el usuario. No apliques cambios de propietario al home de una persona real.

### Configuración y límite

Guarda la configuración anterior y prepara `/etc/vsftpd.conf` para esta VM:

```ini
listen=YES
listen_ipv6=NO
listen_address=192.168.56.40
anonymous_enable=YES
no_anon_password=YES
anon_root=/srv/ftp-ra3
anon_world_readable_only=YES
local_enable=YES
write_enable=NO
chroot_local_user=YES
allow_writeable_chroot=NO
pam_service_name=vsftpd
userlist_enable=YES
userlist_deny=NO
userlist_file=/etc/vsftpd-ra3-users
port_enable=YES
connect_from_port_20=YES
pasv_enable=YES
pasv_min_port=40000
pasv_max_port=40009
max_clients=4
max_per_ip=2
ssl_enable=NO
```

El archivo de usuarios contiene sólo `anonymous`, `ftp` y `lector_ra3`, una entrada por línea, protegido contra edición ordinaria. La lista no concede permisos del sistema de archivos. El anónimo sólo obtiene el árbol público; el usuario local queda en su árbol. Ambos tienen lectura, con escritura deshabilitada. Revisa además PAM y la lista de usuarios prohibidos del paquete; no los vacíes para hacer funcionar una autenticación.

Arranca desde la consola únicamente después de revisar aislamiento y archivos. Comprueba `systemctl status vsftpd`, journal y `ss -lntp`. El canal de control escucha en `.40:21`; los canales de datos se abren según el modo. El firewall de laboratorio admite sólo los extremos y puertos previstos; no abras rangos en una red física.

Desde `.20`, un ejemplo de descarga pasiva con curl es:

```bash
curl --ftp-pasv --user anonymous: ftp://192.168.56.40/publico.txt -o publico-pasivo.txt
curl --ftp-port 192.168.56.20:40020-40029 --disable-eprt \
  --user anonymous: ftp://192.168.56.40/publico.txt -o publico-activo.txt
sha256sum publico-pasivo.txt publico-activo.txt
```

El segundo comando usa IPv4 activo y requiere que el cliente permita la conexión de datos en ese rango desde el servidor. Debe seleccionarse la IP real de LAB, no una de NAT. En pasivo el cliente conecta al puerto anunciado por el servidor; en activo anuncia dónde debe conectar éste. Si el control responde y los datos se bloquean, investiga ese segundo canal antes de cambiar cuentas.

Repite acceso con `lector_ra3` haciendo que el cliente solicite contraseña, sin incrustarla en la URL. Compara árbol visible y límites. Intenta una subida con un archivo sintético: debe denegarse. Repite descarga anónima y autenticada con cliente gráfico, guardando modo y resultados sin contraseñas. Detén el servicio al terminar y restaura o elimina exclusivamente la VM efímera. Una alternativa SFTP protege otro protocolo: es útil para comparar, pero no evidencia los modos FTP activo/pasivo. Referencias: [manual Debian](https://manpages.debian.org/trixie/vsftpd/vsftpd.conf.5.en.html) y [curl](https://curl.se/docs/manpage.html).

## 3. Recogida remota del buzón con IMAPS · RA4.f–g

Parte del laboratorio Postfix de [correo local](05-correo-local.md), con mensajes sintéticos entregados a `labmail/Maildir`. Añade Dovecot en la misma VM, sin ampliar SMTP fuera de loopback. Crea un A `mail.aula.test` a `.10` y un certificado propio que incluya ese nombre, firmado por la CA de formación y verificado desde cliente. No reutilices un certificado de otro nombre sólo porque utiliza la misma IP.

<a id="cuenta-imaps"></a>
### 3.1 Preparar la identidad del buzón y excluirla de SSH

La guía base creó `labmail` mediante `adduser --disabled-password`. Comprueba desde la consola que sigue siendo la cuenta exclusiva del ejercicio y observa su estado:

```bash
getent passwd labmail
sudo passwd -S labmail
```

Un estado `L` indica contraseña bloqueada; no esperes que la autenticación por contraseña de PAM funcione sólo porque Postfix ya pueda entregar mensajes. El home debe corresponder al buzón de prácticas y la cuenta no debe estar expirada. No reutilices ni desbloquees la cuenta de otra persona.

Antes de habilitar una contraseña de buzón, excluye `labmail` del servicio SSH. Conserva consola y una sesión administrativa válida, y guarda la configuración completa de SSH en una ubicación privada de root. Por ejemplo, en este clon:

```bash
respaldo_ssh_ra4="/root/ssh-antes-ra4-$(date +%Y%m%d-%H%M%S)"
sudo cp -a /etc/ssh "$respaldo_ssh_ra4"
sudoedit /etc/ssh/sshd_config
```

Revisa las inclusiones y bloques `Match`. En la configuración global, antes de los bloques `Match`, añade la cuenta a la política `DenyUsers`. La línea mínima del ejemplo es:

```text
DenyUsers labmail
```

Si ya existe una lista, conserva sus patrones y añade `labmail` sólo si no está cubierto; no la sustituyas por la línea mínima ni modifiques `AllowUsers` a ciegas. `DenyUsers` rechaza el acceso SSH de esa identidad, incluyendo sesiones que pudieran solicitar reenvíos. Cambiar únicamente la shell a `nologin` no se usa aquí como control de todos los canales SSH. La cuenta administrativa del túnel debe ser otra y conservar únicamente los permisos y reenvíos que tenga autorizados. Contrasta las opciones con [OpenSSH: sshd_config](https://man.openbsd.org/sshd_config.5).

Valida sintaxis y configuración efectiva para el cliente y usuario del ejercicio:

```bash
sudo /usr/sbin/sshd -t
sudo /usr/sbin/sshd -T -C user=labmail,host=cli01.aula.test,addr=192.168.56.20
```

Sustituye host y dirección por los reales de LAB y revisa también la configuración efectiva de la identidad administrativa. No recargues si hay error o si el administrador perdería acceso. Sólo después de esa revisión, en Debian con el servicio `ssh` de esta práctica, recarga con `sudo systemctl reload ssh`; prueba una segunda sesión administrativa y confirma que una conexión SSH como `labmail` se rechaza. No cierres la consola ni la sesión válida hasta comprobarlo. Si el resultado es distinto, recupera desde consola el cambio concreto y vuelve a validar.

Con la exclusión SSH comprobada, establece por consola una contraseña temporal y única para IMAPS:

```bash
sudo passwd labmail
sudo passwd -S labmail
```

`passwd` la solicita de forma interactiva; no se escribe en el comando, Git, capturas ni memoria. El estado habitual después de establecerla es `P`, pero eso no garantiza por sí solo que toda la política PAM permita autenticación: la prueba posterior debe realizarse contra Dovecot. Esta configuración usa contraseña del sistema con `passdb pam`; otra base de contraseñas requeriría su propio diseño. [Dovecot: usuarios de sistema y autenticación](https://doc.dovecot.org/2.4.1/core/config/auth/users/system.html).

### 3.2 Configurar y comprobar IMAPS

Comprueba `dovecot --version`. La siguiente configuración de referencia es para **Dovecot 2.4**, con sus nombres de opciones; una instalación 2.3 requiere su documentación. En una VM dedicada, conserva `/etc/dovecot` antes de sustituir la configuración principal por una versión completa de la práctica. Evita mezclarla con inclusiones antiguas no revisadas:

```text
dovecot_config_version = 2.4.0
dovecot_storage_version = 2.4.0
protocols {
  imap = yes
}
listen = 127.0.0.1, 192.168.56.10
mail_driver = maildir
mail_path = ~/Maildir
namespace inbox {
  inbox = yes
  separator = /
}
passdb pam {
}
userdb passwd {
}
ssl = yes
auth_allow_cleartext = no
ssl_server_cert_file = /etc/ssl/certs/mail-aula.crt
ssl_server_key_file = /etc/ssl/private/mail-aula.key
service imap-login {
  inet_listener imap {
    port = 0
  }
  inet_listener imaps {
    port = 993
    ssl = yes
  }
}
```

La clave se protege para root; el certificado público no contiene la clave. Conserva la política PAM del paquete para usuarios de sistema y comprueba que `labmail` tenga home y estado de autenticación adecuados. No habilites acceso de root. `doveconf -n` valida e informa de configuración; `doveadm user labmail` comprueba resolución de identidad, no su contraseña ni entrega de correo.

Después de validar y arrancar, comprueba que sólo 993 esté abierto para IMAP en los destinos previstos y autoriza el cliente LAB en el firewall. Desde el cliente:

```bash
openssl s_client -connect 192.168.56.10:993 -servername mail.aula.test \
  -verify_hostname mail.aula.test -verify_return_error -CAfile ca.crt
```

Con TLS validado, observa el saludo y autentica `labmail` con su credencial temporal para consultar `LIST`, `SELECT INBOX` y el mensaje conocido. No publiques el comando de autenticación con contraseña. En el cliente gráfico configura IMAPS por nombre, puerto 993, TLS y CA confiada, con la identidad `labmail` y su contraseña de sistema. Comprueba asunto y cuerpo, no sólo cantidad de mensajes. Realiza una prueba negativa con un nombre de usuario de laboratorio que hayas confirmado inexistente: debe rechazarse, mientras el caso positivo sigue funcionando. Un rechazo de ambos casos no demuestra una política correcta; investiga estado de la cuenta, PAM y logs sin registrar contraseñas ni repetir intentos indiscriminadamente.

Para enviar desde el cliente sin publicar SMTP, usa un túnel SSH cuya identidad de host ya haya sido verificada: `ssh -N -L 127.0.0.1:2525:127.0.0.1:25 administrador@srv01.aula.test`. `administrador` representa otra cuenta de laboratorio autorizada para ese túnel, no `labmail`; revisa el permiso de reenvío efectivo sin ampliar políticas globales para hacerlo funcionar.

Configura el servidor **SMTP** del cliente hacia `127.0.0.1`, puerto **2525**, con **autenticación ninguna**, según el Postfix loopback de esta práctica sin SASL. No introduzcas en ese perfil la contraseña IMAPS ni actives autenticación SMTP para eliminar una alerta del cliente. El tramo SMTP local de este diseño no negocia TLS; el tráfico entre cliente y servidor viaja dentro del túnel SSH verificado. El perfil **IMAPS** es distinto: `mail.aula.test:993`, TLS y autenticación de `labmail`. Postfix continúa escuchando sólo en loopback y aceptando únicamente destinatarios locales. No habilites relay ni submission pública. Añade un alias de formación en `/etc/aliases`, ejecuta `newaliases` y verifica entrega al buzón previsto. Un destinatario `externo.test` debe rechazarse antes de aportar contenido.

Al cerrar, detén Dovecot si no se necesita, retira túnel, cuentas y confianza conforme al procedimiento, preservando sólo evidencias sintéticas. Si conservas `labmail` únicamente para entrega local, vuelve a bloquear su contraseña con `sudo passwd -l labmail` desde consola y mantén la exclusión SSH. Si eliminas la cuenta y reviertes el ajuste SSH, retira sólo la modificación de este ejercicio y repite validación y prueba administrativa antes de recargar. Consulta [configuración 2.4](https://doc.dovecot.org/2.4.1/core/config/quick.html), [usuarios de sistema](https://doc.dovecot.org/2.4.1/core/config/auth/users/system.html) y [TLS](https://doc.dovecot.org/2.4.1/core/config/ssl.html). Este ejercicio no configura entrega de correo en Internet.

## 4. Acceso gráfico y administración heterogénea · RA6

Utiliza Windows 11 **Pro**, una cuenta temporal y la consola del hipervisor para preparar RDP; la edición Home no sirve como host del mismo modo. Habilita Escritorio remoto en Configuración, conserva NLA y añade sólo las identidades autorizadas. En el firewall identifica la regla efectiva y limita origen a la IP LAB del cliente Linux, sin exponer 3389 a Internet o a NAT mediante reenvíos.

En Linux instala el cliente RDP de la distribución, identifica el ejecutable realmente disponible y comprueba su ayuda. En Debian puede depender de la versión de FreeRDP; no supongas que siempre se llama igual. Introduce la contraseña por el diálogo del cliente, contrasta certificado/huella por el procedimiento del equipo y no uses aceptación global de certificados como solución permanente.

Desde Linux entra al host Windows, identifica equipo y usuario y realiza una operación de administración autorizada, como consultar servicios y registrar una configuración antes/después del ámbito de la práctica. Si necesita elevación, usa una identidad y consentimiento autorizados; no conviertas una cuenta lectora en administradora para ocultar un fallo. Desde Windows accede por SSH al servidor Linux y consulta versión, servicio y archivo sintético permitido. Así se observan ambos métodos y sistemas de distinta naturaleza.

Compara recursos gráficos, latencia, necesidad de escritorio, permisos, auditoría y alcance de una interrupción. Cierra sesión y conexiones al terminar, retira la regla y habilitación de RDP que hayas añadido y comprueba que no permanezcan cuentas o listeners imprevistos. Referencias: [Microsoft Learn, RDS y acceso remoto](https://learn.microsoft.com/windows-server/remote/remote-desktop-services/), [FreeRDP](https://www.freerdp.com/) y [OpenSSH](https://www.openssh.com/manual.html).

## 5. Pasarela y publicación en una red exterior simulada · RA8

### Topología independiente

No cambies la LAB base para fingir que `.56.1` es un router. Crea dos redes internas del hipervisor, sin puente ni conexión a un operador: privada `10.77.0.0/24` y exterior simulada `198.51.100.0/24`. El segundo prefijo es de documentación, no una red pública enrutable de tu propiedad.

| Equipo | Interfaz y dirección | Función |
| --- | --- | --- |
| Cliente privado | `10.77.0.20/24`, gateway `.1` | Acceso controlado hacia exterior |
| Web privada | `10.77.0.10/24`, gateway `.1` | Servicio que se publicará mediante DNAT |
| Pasarela | LAN `10.77.0.1/24`, WAN `198.51.100.1/24` | Routing, NAT, filtrado y proxy opcional |
| Equipo exterior | `198.51.100.10/24` | Web de prueba y cliente de entrada |

Los nombres `lan0` y `wan0` son ejemplos y se sustituyen tras inventario. No ejecutes estas reglas sobre una VM con políticas existentes: usa una pasarela dedicada, consola, copia y una única herramienta de firewall. El entorno exterior simulado permite observar mecanismos; una conexión real a red pública requiere además operador, autorización y pruebas de su entorno, y no se acredita con esta simulación.

### Routing y NAT

Configura direcciones y rutas mediante el gestor activo. Registra `ip route` y activa reenvío IPv4 en la pasarela para esta sesión de formación, documentando cómo volver al valor anterior. Prepara reglas de ejemplo en un archivo nuevo y valida con `nft -c -f` antes de aplicar. Las tablas exclusivas del ejercicio son:

```nft
table inet smr_ra8 {
  chain input {
    type filter hook input priority 0; policy drop;
    iifname "lo" accept
    ct state established,related accept
    iifname "lan0" ip saddr 10.77.0.0/24 tcp dport 3128 accept
  }
  chain forward {
    type filter hook forward priority 0; policy drop;
    ct state established,related accept
    iifname "lan0" oifname "wan0" ip saddr 10.77.0.0/24 tcp dport { 80, 443 } accept
    iifname "wan0" oifname "lan0" ip daddr 10.77.0.10 tcp dport 80 ct status dnat accept
  }
  chain output {
    type filter hook output priority 0; policy accept;
  }
}
table ip smr_ra8_nat {
  chain prerouting {
    type nat hook prerouting priority dstnat; policy accept;
    iifname "wan0" ip daddr 198.51.100.1 tcp dport 8080 dnat to 10.77.0.10:80
  }
  chain postrouting {
    type nat hook postrouting priority srcnat; policy accept;
    oifname "wan0" ip saddr 10.77.0.0/24 snat to 198.51.100.1
  }
}
```

No contienen `flush ruleset`; aun así otras cadenas efectivas pueden alterar el resultado, razón para usar la VM dedicada. La política de entrada obliga a administrar por consola y permite únicamente el proxy de formación desde LAN. Las cadenas de forwarding aceptan la salida web y la entrada traducida prevista; no equivalen a permitir toda conexión entre redes.

Comprueba desde el cliente privado una petición a `http://198.51.100.10/` y observa direcciones antes/después de NAT. Desde exterior pide `http://198.51.100.1:8080/` y comprueba contenido e identificación de la web privada. Después prueba un puerto no autorizado sin enviar tráfico a destinos reales. Si falla el retorno, revisa gateway de la web privada y estado de conexiones antes de ampliar reglas.

### Proxy y aceleración observable

Instala una versión de Squid soportada por la distribución y revisa su configuración de ejemplo. Limita `http_port` a `10.77.0.1:3128`, define ACL de origen privado y puertos seguros, conserva protecciones de administración y termina con denegación por defecto. No publiques un proxy abierto. La [semántica de `http_access`](https://www.squid-cache.org/Doc/config/http_access/) depende de su versión; la página oficial distingue las ramas compatibles.

En la web exterior sirve un objeto sintético con una política `Cache-Control: public, max-age=300`, tamaño y contenido conocidos. Desde el cliente solicita dos veces esa URL a través del proxy. Registra el log de acceso, el tiempo y si la política permite HIT/MISS; una segunda petición rápida no demuestra caché. No fuerces almacenamiento de contenido privado o `no-store` para fabricar una mejora. Para HTTPS, un túnel CONNECT no permite cachear el contenido cifrado por sí solo; no se introduce interceptación TLS en este ejercicio.

Compara acceso directo y proxy y documenta cuándo compensa, cuándo no puede almacenar y qué ocurre al invalidar el objeto. Al cerrar, detén proxy y servicios efímeros, elimina sólo las tablas `smr_ra8` y `smr_ra8_nat`, restaura reenvío y rutas y comprueba separación de redes. Consulta [nftables](https://wiki.nftables.org/wiki-nftables/index.php/Main_Page), [RFC 5737](https://www.rfc-editor.org/rfc/rfc5737) y [Squid](https://www.squid-cache.org/Doc/).
