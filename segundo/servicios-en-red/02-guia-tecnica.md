# Guía técnica: DNS, DHCP, SSH y HTTPS

## 1. Preparación y control de cambios

Trabaja dentro de `srv01`, Debian 13, con una NIC NAT para instalar paquetes y una NIC LAB aislada con `192.168.56.10/24`. LAB no tiene gateway. El nombre `ens19` debe sustituirse por la interfaz real obtenida con `ip -br link` y comparada con la MAC del hipervisor.

Antes de instalar, verifica que LAB no está conectada en puente a la red física y que el DHCP incorporado en el hipervisor está deshabilitado para esa red. Conserva consola, instantánea y copia de la configuración existente. Los paquetes pueden iniciar servicios al instalarse; la red debe estar aislada desde el principio.

~~~bash
cat /etc/os-release
ip -br address
ip route
sudo ss -lntup
sudo apt update
sudo apt install bind9 bind9-utils dnsutils kea-dhcp4-server openssh-server nginx openssl curl tcpdump
~~~

Anota las versiones con `dpkg-query -W`. Detén Kea hasta completar su configuración:

~~~bash
sudo systemctl stop kea-dhcp4-server
~~~

Identifica unidades reales con `systemctl list-unit-files`. En los paquetes Debian se emplean `named` para BIND, `kea-dhcp4-server` para DHCPv4, `ssh` para SSH y `nginx` para web; algunas versiones incorporan alias. Un error «unit not found» debe llevar a comprobar el paquete, no a inventar un nombre de servicio.

Copia cada fichero existente antes de editarlo, por ejemplo `sudo cp -a /etc/bind/named.conf.options /etc/bind/named.conf.options.pre-smr`. Usa un sufijo diferente si ya existe una copia con ese nombre. Documenta ubicación y fecha. Los bloques siguientes son contenidos de fichero, no comandos de terminal.

## 2. DNS autoritativo con BIND9

### Configuración de escucha y acceso

En `/etc/bind/named.conf.options`, conserva un único bloque `options` adaptado al laboratorio:

~~~text
acl "lab" {
    127.0.0.1;
    192.168.56.0/24;
};

options {
    directory "/var/cache/bind";
    listen-on { 127.0.0.1; 192.168.56.10; };
    listen-on-v6 { none; };
    recursion no;
    allow-query { lab; };
    allow-transfer { none; };
};
~~~

La ACL limita quién consulta y `listen-on` limita dónde se escucha. `recursion no` hace que este ejemplo no resuelva Internet para clientes. No mezcles esta configuración con una expectativa de resolver general: para Internet utiliza el resolver apropiado en la interfaz NAT o un diseño de DNS dividido deliberado.

Se desactiva escucha IPv6 sólo en este servicio de laboratorio porque no se ha diseñado todavía direccionamiento IPv6 para él. No es una instrucción para deshabilitar IPv6 en todo el SO. Para una ampliación de doble pila, configura direcciones, ACL y pruebas IPv6 expresas.

En `/etc/bind/named.conf.local` añade las zonas, conservando otras definiciones que pertenezcan al entorno:

~~~text
zone "aula.test" {
    type primary;
    file "/etc/bind/db.aula.test";
};

zone "56.168.192.in-addr.arpa" {
    type primary;
    file "/etc/bind/db.192.168.56";
};
~~~

El archivo principal de Debian debe incluir tanto `named.conf.options` como `named.conf.local`. Comprueba la inclusión antes de atribuir un fallo a los datos de zona.

### Zona directa

Crea `/etc/bind/db.aula.test`:

~~~dns
$TTL 300
@ IN SOA ns1.aula.test. hostmaster.aula.test. (
    2026110801
    3600
    900
    604800
    300
)
@     IN NS    ns1.aula.test.
@     IN MX 10 mail.aula.test.
ns1   IN A     192.168.56.10
srv01 IN A     192.168.56.10
www   IN CNAME srv01.aula.test.
mail  IN A     192.168.56.10
cli01 IN A     192.168.56.20
~~~

El serial usa un convenio de fecha y contador. Sustitúyelo por el correspondiente a tu cambio y aumenta su valor en modificaciones posteriores. El segundo nombre del SOA representa una dirección de contacto en notación DNS; no es una cuenta que BIND vaya a crear. El MX documenta el nombre previsto para correo; por sí solo no habilita SMTP y la práctica de correo seguirá aislada en loopback.

Para aprender AAAA, añade sólo después de configurar y verificar IPv6 un registro de la forma `srv01 IN AAAA direccion_ipv6_real_del_laboratorio`. El texto marcador no es una dirección válida y no debe copiarse al archivo. `2001:db8:56::10` puede usarse en diagramas de documentación, pero publicar ese AAAA sin una topología IPv6 funcional daría una respuesta engañosa.

### Zona inversa

Crea `/etc/bind/db.192.168.56`:

~~~dns
$TTL 300
@ IN SOA ns1.aula.test. hostmaster.aula.test. (
    2026110801
    3600
    900
    604800
    300
)
@  IN NS  ns1.aula.test.
10 IN PTR srv01.aula.test.
20 IN PTR cli01.aula.test.
~~~

No escribas `192.168.56.10` como propietario dentro de esta zona /24. El origen ya aporta el sufijo inverso. Tampoco necesitas un PTR diferente para cada alias A/CNAME del mismo servidor.

### Validación y pruebas

~~~bash
sudo named-checkconf
sudo named-checkzone aula.test /etc/bind/db.aula.test
sudo named-checkzone 56.168.192.in-addr.arpa /etc/bind/db.192.168.56
sudo named-checkconf -z
sudo systemctl restart named
sudo systemctl --no-pager status named
sudo journalctl -u named -n 40 --no-pager
sudo ss -lntup
~~~

La validación debe finalizar correctamente antes del reinicio. `named-checkconf -z` intenta cargar las zonas primarias además de revisar sintaxis. Un proceso activo no sustituye las consultas:

~~~bash
dig @192.168.56.10 srv01.aula.test A +norecurse
dig @192.168.56.10 www.aula.test A +norecurse
dig @192.168.56.10 aula.test MX +norecurse
dig @192.168.56.10 -x 192.168.56.10 +norecurse
dig @192.168.56.10 aula.test SOA +tcp
dig @192.168.56.10 inexistente.aula.test A +norecurse
~~~

Busca `status: NOERROR` y bandera `aa` en respuestas autoritativas válidas; para el nombre inexistente se espera `NXDOMAIN`. La prueba `+tcp` comprueba que 53/TCP también responde. El alias web debe devolver el CNAME y la dirección correspondiente.

Desde Windows, `Resolve-DnsName srv01.aula.test -Server 192.168.56.10` consulta expresamente ese servidor. Para comprobar el resolver del sistema realiza después una consulta sin `-Server` y registra los DNS configurados. Si el navegador usa otro mecanismo, documéntalo.

**Recuperación:** restaura sólo los ficheros cambiados, valida de nuevo y recarga. Si retiras una zona, elimina su declaración y después el archivo cuando ya no se use. No borres directorios completos de BIND ni claves de control que no creaste.

## 3. DHCPv4 con Kea

### Diseño previo

El servidor es estático en `.10` y el cliente fijo en `.20`. El pool dinámico va de `.100` a `.150`. El rango no incluye las IP estáticas. Para esta prueba añade un cliente nuevo o convierte sólo LAB del cliente en DHCP, preservando la configuración de NAT.

Kea es el servidor elegido para esta guía. La configuración de ISC DHCP tradicional utiliza otra sintaxis; no pegues un bloque `subnet ... netmask ...` dentro de un archivo JSON de Kea.

En `/etc/kea/kea-dhcp4.conf` prepara un objeto completo:

~~~json
{
  "Dhcp4": {
    "interfaces-config": {
      "interfaces": [ "ens19" ]
    },
    "valid-lifetime": 3600,
    "renew-timer": 900,
    "rebind-timer": 1800,
    "lease-database": {
      "type": "memfile",
      "persist": true,
      "name": "/var/lib/kea/kea-leases4.csv"
    },
    "subnet4": [
      {
        "id": 1,
        "subnet": "192.168.56.0/24",
        "pools": [
          { "pool": "192.168.56.100 - 192.168.56.150" }
        ],
        "option-data": [
          { "name": "domain-name-servers", "data": "192.168.56.10" },
          { "name": "domain-name", "data": "aula.test" }
        ]
      }
    ]
  }
}
~~~

No se anuncia `routers` porque LAB no tiene router. `ens19` debe ser la interfaz real de LAB y no un comodín. La base memfile persiste concesiones; su archivo debe ser accesible con los permisos y confinamiento previstos por el paquete. Conserva la propiedad del directorio instalada por Debian.

### Validación y activación

~~~bash
sudo kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
sudo systemctl restart kea-dhcp4-server
sudo systemctl --no-pager status kea-dhcp4-server
sudo journalctl -u kea-dhcp4-server -n 60 --no-pager
sudo ss -lunp
~~~

El test `-t` comprueba la configuración, pero no abre todos los sockets ni verifica todos los recursos de ejecución; también son necesarios logs y prueba de cliente. La documentación del paquete explica esta limitación.

Captura exclusivamente en LAB:

~~~bash
sudo tcpdump -ni ens19 -c 40 'udp port 67 or udp port 68'
~~~

En Windows, identifica primero el nombre del adaptador. Después utiliza la opción de obtener IPv4 y DNS automáticamente en LAB. Para renovar por terminal, usa `ipconfig /renew "nombre_real_del_adaptador"` y no una operación indiscriminada sobre todas las interfaces. En Linux usa el gestor real: reconecta sólo el perfil LAB con DHCP. No presupongas que `dhclient` está instalado.

El cliente debe recibir una IP del pool, máscara /24 y DNS `.10`; no debe aparecer una puerta de enlace nueva en LAB. Correlaciona la MAC y la dirección con logs y concesiones. Si aparecen dos Offers de servidores diferentes, detén Kea y revisa el aislamiento y el DHCP del hipervisor antes de continuar.

### Reserva opcional

Para aprender reservas, añade dentro de la subred un bloque `reservations` con la MAC real del cliente de práctica:

~~~json
"reservations": [
  {
    "hw-address": "02:00:00:00:00:50",
    "ip-address": "192.168.56.50",
    "hostname": "cli-reserva"
  }
]
~~~

Este fragmento no es un archivo completo: exige una coma correcta entre propiedades y una MAC sustituida por la real. La IP reservada `.50` está dentro de la subred y fuera del pool dinámico; `.30` se conserva para `ns2` en la ampliación DNS. Si utilizaste `.30` en una sesión anterior, revisa y retira esa reserva o dirección del cliente antes de incorporar la secundaria, mediante un cambio controlado y sin borrar indiscriminadamente concesiones. Comprueba la política de reservas de la versión instalada y posibles identificadores de cliente antes de explicar un fallo. El campo `hostname` no añade automáticamente un registro a BIND: DDNS requiere configuración adicional explícita.

**Recuperación:** detén el servicio antes de devolver el cliente a IP fija. Restaura su estado previo y el del hipervisor. No borres la base de concesiones para resolver cualquier incidencia; analiza primero su contenido y la configuración.

## 4. SSH y SFTP

Crea una cuenta de laboratorio sin privilegios innecesarios mediante `sudo adduser alumno` si no existe. Define su contraseña interactivamente; no la escribas en scripts ni en Git. Identifica la huella de host en la consola:

~~~bash
sudo ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
sudo /usr/sbin/sshd -t
sudo systemctl --no-pager status ssh
~~~

Desde el cliente, contrasta esa huella al conectar:

~~~bash
ssh alumno@192.168.56.10
~~~

Para claves de usuario, genera una clave en el cliente:

~~~bash
ssh-keygen -t ed25519 -a 64
~~~

Conserva la ruta predeterminada sólo si no sobrescribe una clave existente y protege la privada con frase de paso. En Linux, `ssh-copy-id alumno@192.168.56.10` instala la pública tras autenticación. En Windows OpenSSH puede copiarse el contenido del archivo `.pub` por un canal ya autenticado y añadirlo a `~/.ssh/authorized_keys` del usuario. El directorio `.ssh` debe ser privado del usuario y el archivo no debe ser escribible por otros.

Prueba una segunda sesión con clave antes de cambiar políticas. Para limitar la escucha y el acceso, utiliza un fichero nuevo en `/etc/ssh/sshd_config.d/` sólo después de comprobar que el fichero principal incluye ese directorio:

~~~text
ListenAddress 192.168.56.10
PermitRootLogin no
PubkeyAuthentication yes
AllowUsers alumno
~~~

`AllowUsers` restringe cuentas: incluye al administrador legítimo si tu diseño lo necesita antes de aplicar. No desactives contraseñas hasta demostrar que las claves funcionan y conservar consola. Valida `sshd -t` y revisa valores efectivos con `sshd -T`; bloques `Match` pueden alterar el resultado para cada conexión.

Recarga con `sudo systemctl reload ssh` manteniendo abierta la sesión anterior. Prueba otra conexión desde LAB y verifica `ss -lntp`. SFTP utiliza:

~~~text
sftp alumno@192.168.56.10
sftp> pwd
sftp> put evidencia.txt
sftp> get evidencia.txt evidencia-descargada.txt
sftp> bye
~~~

Compara hashes del archivo original y descargado. No publiques claves privadas; las claves de host tampoco son plantillas reutilizables. Al recuperar una configuración, restaura el fichero concreto, valida y recarga desde consola si se perdió acceso.

## 5. HTTPS con Nginx y confianza explícita

### Contenido y certificado de laboratorio

Crea `/var/www/smr/index.html` con una página estática de prueba y propiedad de root, legible por el proceso web. Por ejemplo:

~~~bash
sudo install -d -m 0755 /var/www/smr
sudo install -d -m 0700 /etc/nginx/tls
~~~

Edita la página con `sudoedit`. No otorgues escritura general al árbol web para evitar errores de permisos. Genera una clave y un certificado autofirmado exclusivamente para el laboratorio:

~~~bash
sudo openssl req -x509 -newkey rsa:3072 -sha256 -days 30 -noenc -keyout /etc/nginx/tls/www.aula.test.key -out /etc/nginx/tls/www.aula.test.crt -subj "/CN=www.aula.test" -addext "subjectAltName=DNS:www.aula.test" -addext "basicConstraints=critical,CA:FALSE" -addext "keyUsage=critical,digitalSignature,keyEncipherment" -addext "extendedKeyUsage=serverAuth"
sudo chmod 0600 /etc/nginx/tls/www.aula.test.key
sudo openssl x509 -in /etc/nginx/tls/www.aula.test.crt -noout -subject -dates -ext subjectAltName
~~~

`-noenc` deja la clave sin contraseña para el arranque desatendido; por eso sus permisos y almacenamiento son críticos. Se usa un certificado de servidor autofirmado que el cliente aceptará como ancla explícita únicamente para esta prueba, no una CA que se deba distribuir globalmente.

Crea `/etc/nginx/sites-available/smr`:

~~~nginx
server {
    listen 192.168.56.10:80;
    server_name www.aula.test;
    return 308 https://www.aula.test$request_uri;
}

server {
    listen 192.168.56.10:443 ssl;
    server_name www.aula.test;
    root /var/www/smr;
    index index.html;

    ssl_certificate /etc/nginx/tls/www.aula.test.crt;
    ssl_certificate_key /etc/nginx/tls/www.aula.test.key;
    ssl_protocols TLSv1.2 TLSv1.3;

    location / {
        try_files $uri $uri/ =404;
    }
}
~~~

Enlaza este sitio desde `sites-enabled` sólo si el archivo de destino no existe. Revisa el sitio predeterminado de Debian: puede escuchar en todas las interfaces. Deshabilita únicamente el enlace del sitio predeterminado que hayas identificado y guardado, si no debe estar activo en esta VM. Conserva la copia de su estado para revertir.

### Validación y prueba desde cliente

~~~bash
sudo nginx -t
sudo systemctl reload nginx
sudo ss -lntp
sudo journalctl -u nginx -n 30 --no-pager
~~~

Copia únicamente el certificado público `.crt` al cliente por SSH/SFTP y contrasta su huella por consola. Nunca copies la clave `.key`. Desde un cliente con curl:

~~~bash
curl --resolve www.aula.test:443:192.168.56.10 --cacert ./www.aula.test.crt https://www.aula.test/
curl --resolve www.aula.test:80:192.168.56.10 -I http://www.aula.test/
~~~

`--resolve` fuerza esa correspondencia nombre/IP para esta petición, preservando nombre de TLS y HTTP. Sirve para separar DNS de HTTPS. `--cacert` limita la confianza al material indicado para la operación. Cuando DNS esté comprobado, repite sin `--resolve`.

Se espera contenido del sitio y una redirección HTTP a HTTPS. Comprueba además una ruta inexistente que devuelva `404`. Una petición a un nombre distinto debe fallar la validación del nombre aunque apunte a la misma IP. No uses `-k` como criterio de aceptación: omite verificaciones que precisamente se quieren aprender.

**Recuperación:** deshabilita el enlace del sitio de prácticas, valida y recarga; restaura el sitio previo si existía. Retira el certificado público de cualquier almacén de confianza al que se hubiese añadido sólo para la práctica. No elimines claves de otros sitios.

## 6. Firewall y evidencia final

La escucha en LAB reduce exposición, pero no sustituye al firewall. Revisa la herramienta utilizada en el módulo de Seguridad y aplica únicamente las reglas necesarias: DNS TCP/UDP 53, DHCPv4 según interfaz y mecanismo del servidor, SSH TCP 22 y web TCP 80/443, con orígenes apropiados. Un firewall que permita sólo IP `192.168.56.0/24` puede bloquear un DHCP Discover inicial con origen `0.0.0.0`; diseña la excepción de DHCP por interfaz aislada y puertos, sin abrir la red física.

Entrega por servicio una consulta o transacción válida, un caso negativo y los logs relacionados. Comprueba desde el cliente y desde una interfaz no autorizada del laboratorio que el alcance coincide con el diseño. No pruebes destinos de terceros.

## Referencias de implementación

- [BIND9 ARM](https://bind9.readthedocs.io/en/stable/) y [named-checkconf en Debian](https://manpages.debian.org/trixie/bind9-utils/named-checkconf.8.en.html).
- [Kea ARM](https://kea.readthedocs.io/en/stable/) y [kea-dhcp4 de Debian 13](https://manpages.debian.org/trixie/kea-dhcp4-server/kea-dhcp4.8.en.html).
- [Archivos del paquete kea-dhcp4-server](https://packages.debian.org/trixie/amd64/kea-dhcp4-server/filelist).
- [OpenSSH: sshd_config](https://man.openbsd.org/sshd_config).
- [Nginx: HTTPS](https://nginx.org/en/docs/http/configuring_https_servers.html).
- [OpenSSL req](https://docs.openssl.org/3.5/man1/openssl-req/).
- [curl: documentación de opciones](https://curl.se/docs/manpage.html).
