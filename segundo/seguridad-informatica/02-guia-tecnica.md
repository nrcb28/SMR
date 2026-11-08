# 2. Guía técnica de protección y recuperación

## 2.1 Línea base y gestión del cambio

En una VM Debian 13 del laboratorio registra primero sistema, paquetes, cuentas, interfaces, servicios y capacidad. Son operaciones de observación:

```bash
cat /etc/os-release
uname -r
ip -br address
ip route
systemctl --failed
systemctl list-unit-files --state=enabled
sudo ss -lntup
df -hT
sudo journalctl --disk-usage
```

Una escucha en `0.0.0.0` o `::` puede alcanzar varias interfaces; no prueba por sí sola que el firewall la publique, pero merece contrastarse con la matriz de flujos. Un servicio que no se necesita se retira o limita después de conocer sus dependencias. No deshabilites servicios por una lista genérica sin comprobar qué función cumplen en esa VM.

Antes de actualizar guarda un punto de recuperación apropiado, comprueba espacio y revisa los cambios propuestos:

```bash
sudo apt update
apt list --upgradable
sudo apt upgrade
```

La necesidad de reinicio depende de los paquetes y procesos afectados. La planificación incluye ventana, retorno y prueba posterior. Una actualización instalada no demuestra que todos los procesos estén usando ya sus bibliotecas nuevas. Registra la versión final y el funcionamiento del servicio relevante.

En Windows 11, revisa Windows Update, protección activa y servicios necesarios. PowerShell puede mostrar estado sin desactivar controles:

```powershell
Get-MpComputerStatus
Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, OwningProcess
Get-BitLockerVolume
```

Algunas funciones dependen de edición, componentes y privilegios. `Get-MpComputerStatus` presupone Microsoft Defender disponible. BitLocker exige planificación de recuperación; no se activa antes de custodiar la clave y comprobar el procedimiento de arranque de la VM. Esa clave nunca forma parte del repositorio.

## 2.2 SSH con clave y administración limitada

En `srv01`, crea una cuenta de administración propia de la práctica con acceso controlado a `sudo`; no reutilices las cuentas `nologin` de Samba. Instala el servidor si no existe:

```bash
sudo apt install openssh-server
sudo adduser adminlab
sudo usermod -aG sudo adminlab
systemctl status ssh --no-pager
```

En un cliente autorizado genera la clave, eligiendo una frase de paso cuando la herramienta la solicite:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/smr_adminlab -C 'SMR laboratorio'
```

La pública termina en `.pub`. La privada, sin esa extensión, no se envía al servidor ni se sube a Git. Si el cliente es Windows OpenSSH, utiliza una ruta bajo `$env:USERPROFILE\.ssh` y comprueba su existencia. Una huella pública no es una contraseña, pero tampoco hace falta publicar identidades personales del equipo.

Antes de aceptar el servidor, compara desde su consola la huella de su clave de host:

```bash
sudo ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

Autoriza la clave pública en `~adminlab/.ssh/authorized_keys`, mediante `ssh-copy-id` desde un cliente Linux con acceso inicial autorizado o desde la consola. El directorio debe pertenecer a `adminlab`, tener modo `0700` y el archivo `0600`; no basta con pegar la clave si su propietario o permisos son incorrectos.

Abre una segunda sesión con `ssh -i ~/.ssh/smr_adminlab adminlab@192.168.56.10` y comprueba que la clave funciona y que `sudo -v` solicita o valida el mecanismo esperado. Mantén abierta la consola del hipervisor. Sólo después prepara un archivo dedicado en `/etc/ssh/sshd_config.d/`, verificando que la configuración principal incluye ese directorio:

```text
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
KbdInteractiveAuthentication no
AllowUsers adminlab
```

Esta política es específica de la VM de práctica y dejaría fuera a otras cuentas legítimas. No la copies a un servidor que necesite otras formas de autenticación, MFA mediante PAM o cuentas automatizadas. OpenSSH resuelve muchas opciones tomando el primer valor aplicable; el nombre del archivo, el orden de inclusiones y bloques `Match` importan. No se demuestra el valor efectivo mirando sólo el archivo recién escrito.

Valida antes de recargar y examina la configuración efectiva para el origen de prueba:

```bash
sudo /usr/sbin/sshd -t
sudo /usr/sbin/sshd -T -C user=adminlab,host=cli01,addr=192.168.56.20
sudo systemctl reload ssh
```

Después abre otra sesión nueva con la clave. Prueba que un intento de autenticación por contraseña se rechaza, sin repetir intentos masivos. Si falla la nueva sesión, conserva la anterior y corrige desde consola. Retirar el archivo de práctica y recargar tras validar permite revertir el cambio si se guardó el estado previo.

## 2.3 nftables: una política pequeña y comprobable

Usa exclusivamente una VM de ejercicio sin Docker, UFW, firewalld u otros gestores que creen reglas. Trabaja desde consola y confirma con `sudo nft list ruleset` que conoces el estado. No ejecutes `flush ruleset` sobre una máquina compartida: borraría controles ajenos. La configuración siguiente crea una tabla propia, `inet smr_guard`, y sólo se aplica si no existe ya otra versión de esa tabla.

La matriz de este ejemplo permite administración SSH y un HTTPS ya instalado en LAB; bloquea nuevas conexiones de otros servicios. No incluye DNS, DHCP servidor, Samba ni AD. La NIC NAT `ens18` puede recibir las respuestas DHCP del hipervisor si ese método le asigna dirección. Sustituye ambos nombres por los observados.

```nft
table inet smr_guard {
    chain input {
        type filter hook input priority 0; policy drop;
        iifname "lo" accept
        ct state invalid drop
        ct state established,related accept
        iifname "ens18" udp sport 67 udp dport 68 accept
        ip protocol icmp accept
        meta l4proto ipv6-icmp accept
        iifname "ens19" ip saddr 192.168.56.0/24 tcp dport { 22, 443 } ct state new accept
        counter drop
    }
    chain forward {
        type filter hook forward priority 0; policy drop;
    }
    chain output {
        type filter hook output priority 0; policy accept;
    }
}
```

`inet` abarca IPv4 e IPv6. Se permite ICMP en este ejercicio para diagnóstico y control de red, incluido ICMPv6 necesario para funciones como descubrimiento de vecinos y avisos de tamaño de paquete. El permiso de SSH/HTTPS se expresa sólo para IPv4 de LAB; no concede esos servicios por IPv6. La política de salida abierta simplifica el aula: no equivale a un control de exfiltración completo.

Guarda el bloque como `smr_guard.nft` en tu directorio de trabajo. Comprueba sintaxis y después cárgalo desde consola:

```bash
sudo apt install nftables
sudo nft list ruleset
sudo nft -c -f smr_guard.nft
sudo nft -f smr_guard.nft
sudo nft list table inet smr_guard
```

Un validador de sintaxis no comprueba que la matriz sea correcta. Prueba una conexión nueva de SSH desde LAB, HTTPS con servidor realmente escuchando y un servicio de prueba que deba quedar bloqueado. Una sesión establecida puede seguir permitida por `ct state established`; por eso se usan conexiones nuevas. No des por demostrado el bloqueo sólo porque un puerto sin servicio no responda.

Para revertir únicamente el control de esta práctica, desde consola:

```bash
sudo nft delete table inet smr_guard
```

Sólo borra esa tabla, no el resto. La configuración cargada manualmente no queda persistida automáticamente. Para persistirla, integra el archivo en el método de arranque de `nftables` de una VM dedicada, revisa `/etc/nftables.conf` y realiza una prueba de reinicio con consola. No arranques otro gestor sobre la misma política. Evita cargar repetidamente definiciones de reglas sin saber si se acumulan; observa el conjunto final y conserva una versión única.

## 2.4 Hash y validación TLS

Crea un archivo ficticio y observa su resumen antes y después de una modificación:

```bash
printf 'Inventario ficticio del laboratorio\n' > inventario-lab.txt
sha256sum inventario-lab.txt > inventario-lab.sha256
sha256sum -c inventario-lab.sha256
printf 'Cambio de prueba\n' >> inventario-lab.txt
sha256sum -c inventario-lab.sha256
```

La segunda verificación debe indicar diferencia. El hash no impide la modificación y el manifiesto debe custodiarse si sirve como referencia. En Windows puede obtenerse el resumen con `Get-FileHash -Algorithm SHA256`.

Para examinar un HTTPS de laboratorio necesitas un servidor configurado, nombre correcto y una CA de laboratorio pública cuyo certificado hayas verificado por un canal fiable. `ca-lab.pem` contiene ese certificado de confianza, no una clave privada. Este comando comprueba nombre y cadena y solicita que los errores de validación sean considerados fallo:

```bash
openssl s_client -connect 192.168.56.10:443 -servername web.aula.test \
  -verify_hostname web.aula.test -verify_return_error -CAfile ca-lab.pem </dev/null
```

Comprueba el código de verificación, SAN, emisor y fechas. `-servername` selecciona el servidor virtual mediante SNI; no sustituye a `-verify_hostname`. Para una petición HTTP con nombre resuelto explícitamente:

```bash
curl --cacert ca-lab.pem --resolve web.aula.test:443:192.168.56.10 https://web.aula.test/
```

No se utiliza `-k` para la prueba de aceptación. Si el certificado no es de confianza, ha caducado o no incluye el nombre, corrige la causa en el escenario de laboratorio. Una respuesta HTTP 403 puede indicar que TLS ha funcionado y que la aplicación está denegando autorización: separa capas.

## 2.5 Copia cifrada y restauración con restic

La práctica utiliza archivos pequeños y ficticios. Instala `restic` desde el repositorio de Debian. Verifica que `/mnt/backup` es un soporte o destino independiente y está realmente montado con `findmnt /mnt/backup`; si no lo está, detente. Crear una carpeta llamada `backup` en el mismo disco no aporta independencia.

```bash
sudo apt install restic
findmnt /mnt/backup
df -hT /mnt/backup
sudo install -d -o "$(id -un)" -g "$(id -gn)" -m 0700 /mnt/backup/smr-restic
restic -r /mnt/backup/smr-restic init
```

El comando de creación del directorio presupone que el montaje ya está comprobado, que esa ruta es nueva y que no contiene otro repositorio. `restic` solicitará una contraseña; guárdala en un gestor y pruébala desde el procedimiento de recuperación. No uses una contraseña literal en una variable o comando de esta guía. El repositorio de ejemplo pertenece a la cuenta que ejecuta la copia. Si el origen necesita privilegios, diseña una cuenta y un mecanismo apropiados antes de automatizar; no ejecutes siempre como administrador por comodidad.

Para un directorio `/srv/datos-lab` legible por la cuenta de práctica:

```bash
restic -r /mnt/backup/smr-restic backup /srv/datos-lab
restic -r /mnt/backup/smr-restic snapshots
restic -r /mnt/backup/smr-restic check --read-data
```

La lectura completa de datos es razonable con una copia pequeña del aula; en grandes repositorios requiere planificación de carga y tiempo. El comprobador del repositorio no demuestra que una aplicación pueda arrancar tras restaurar. Copias de bases de datos y directorios necesitan consistencia específica.

Restaura en un destino nuevo y revisado. El comando conserva la estructura de rutas bajo ese destino:

```bash
sudo install -d -o "$(id -un)" -g "$(id -gn)" -m 0750 /srv/restauracion-lab
restic -r /mnt/backup/smr-restic restore latest --target /srv/restauracion-lab
find /srv/restauracion-lab -maxdepth 4 -type f
```

Se espera el contenido bajo `/srv/restauracion-lab/srv/datos-lab`. Verifica contenido, propietarios, permisos y atributos que requiera el caso; algunas restauraciones de metadatos exigen privilegios y soporte del destino. No declares recuperada una ACL si no la has comprobado. No ejecutes políticas de borrado o purga durante la primera práctica: primero demuestra restauración y define retención.

## 2.6 Registro y respuesta a un incidente

Conserva horas y zona horaria. En Debian puedes inspeccionar `timedatectl`, `journalctl -u ssh --since '-30 min'` y los registros específicos del servicio. En Windows selecciona canales y eventos pertinentes, por ejemplo con `Get-WinEvent`, evitando exportaciones indiscriminadas. Una auditoría de acceso a archivos no aparece completa sólo por activar el Visor de eventos: necesita política y objetos auditados correctamente.

El procedimiento mínimo de incidente incluye: registrar el aviso, confirmar alcance, contener con el menor daño razonable, preservar evidencias pertinentes, erradicar la causa, recuperar desde un estado confiable y observar que no reaparece. El orden puede adaptarse a la urgencia. Apagar inmediatamente puede destruir datos volátiles; mantener conectado puede ampliar el daño. La decisión debe estar prevista y registrarse, no improvisarse como regla absoluta.

Para una sospecha de credencial comprometida considera revocación de sesiones, cambio de secretos desde equipo confiable y revisión de accesos, además del cambio de contraseña. Para ransomware simulado no se instala malware: se puede representar una pérdida de datos con un archivo ficticio renombrado y estudiar la detección y restauración. La comunicación real a afectados o autoridades sólo la realiza quien tenga esa responsabilidad y autorización.

## Referencias operativas

- [OpenSSH: sshd_config](https://man.openbsd.org/sshd_config) y la página `man sshd_config` instalada en Debian.
- [Debian Wiki: nftables](https://wiki.debian.org/nftables) y [manual oficial de nft](https://netfilter.org/projects/nftables/manpage.html).
- [OpenSSL: s_client](https://docs.openssl.org/master/man1/openssl-s_client/).
- [restic: documentación oficial](https://restic.readthedocs.io/en/stable/).
- [Microsoft: Get-MpComputerStatus](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpcomputerstatus).
- [INCIBE: empresas](https://www.incibe.es/empresas).
