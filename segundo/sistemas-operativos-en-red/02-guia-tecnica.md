# 2. Guía técnica de administración

## 2.1 Inventario antes de modificar

En Debian, abre una consola de la VM y registra el estado inicial. Estos comandos son de observación:

```bash
hostnamectl
ip -br address
ip route
resolvectl status  # sólo si este sistema utiliza systemd-resolved
lsblk -f
findmnt -T /srv
df -hT
free -h
systemctl --failed
```

`ens19` será la interfaz LAB sólo si el inventario lo confirma. No cambies la dirección de una interfaz basándote en su posición en una captura ajena. En una instalación sin `systemd-resolved`, inspecciona `/etc/resolv.conf` y el gestor de red activo. No configures simultáneamente NetworkManager, ifupdown y systemd-networkd sobre la misma interfaz.

En Windows, ejecuta PowerShell como administrador para administrar roles y red:

```powershell
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
Get-NetAdapter | Select-Object Name, InterfaceIndex, Status, MacAddress
Get-NetIPConfiguration
Get-DnsClientServerAddress -AddressFamily IPv4
Get-Volume | Select-Object DriveLetter, FileSystem, SizeRemaining, Size
Get-Service DNS, NTDS -ErrorAction SilentlyContinue
```

Guarda sólo información de laboratorio. En un informe de un entorno real, elimina números de serie, nombres personales y datos de red que no sean necesarios. La ausencia de `NTDS` antes de instalar AD es normal.

## 2.2 Linux: cuentas, grupos y ACL

En `srv01` utiliza una cuenta administradora con `sudo`. Instala las herramientas desde los repositorios configurados de Debian; revisa los cambios que proponga el gestor antes de aceptarlos:

```bash
sudo apt update
sudo apt install acl samba smbclient
sudo groupadd soporte
sudo useradd --no-create-home --shell /usr/sbin/nologin ana
sudo useradd --no-create-home --shell /usr/sbin/nologin bruno
sudo usermod -aG soporte ana
id ana
id bruno
```

Los comandos de creación son para un laboratorio limpio. Si `getent group soporte` o `getent passwd ana` ya devuelve una entrada, no repitas el alta: examina el objeto existente. `nologin` impide una sesión interactiva convencional; no significa que todos los servicios ignoren la cuenta.

Prepara un recurso nuevo, sin reutilizar una ruta con datos anteriores:

```bash
sudo install -d -o root -g soporte -m 2770 /srv/samba/manuales
sudo setfacl -m u::rwx,g::rwx,m::rwx,o::--- /srv/samba/manuales
sudo setfacl -m d:u::rwx,d:g::rwx,d:m::rwx,d:o::--- /srv/samba/manuales
getfacl /srv/samba/manuales
namei -l /srv/samba/manuales
sudo -u ana sh -c 'printf "Prueba de acceso\n" > /srv/samba/manuales/prueba.txt'
sudo -u bruno cat /srv/samba/manuales/prueba.txt
```

La última lectura debe fallar por permisos. Ése es un resultado esperado de seguridad y debe registrarse. Los directorios padre deben permitir atravesar la ruta. `setgid` mantiene el grupo en nuevas entradas y la ACL por defecto define herencia. No uses `chmod -R` indiscriminadamente: marcar todos los archivos como ejecutables cambia su significado y recorrer enlaces o árboles grandes puede afectar información ajena al ejercicio.

Para conservar una ACL antes de un experimento:

```bash
sudo getfacl -Rp /srv/samba/manuales > acl-manuales.antes.txt
```

`-p` conserva las rutas absolutas para que la recuperación no dependa del directorio desde el que se ejecuta. Una restauración con `setfacl --restore=archivo` modifica ACL de las rutas registradas. Examina primero el archivo, confirma que corresponde a este laboratorio y simula la operación con `sudo setfacl --test --restore=acl-manuales.antes.txt` antes de aplicarla. No la ejecutes sobre un árbol renombrado o de producción. Una copia de ACL no contiene el contenido de los archivos.

## 2.3 Samba independiente: configuración mínima verificable

Haz una copia de `/etc/samba/smb.conf`, con fecha y acceso restringido. Sustituye o adapta el archivo únicamente en la VM nueva prevista para esta práctica. La configuración siguiente publica un solo recurso y exige autenticación y cifrado SMB en ese recurso:

```ini
[global]
    workgroup = AULA
    server role = standalone server
    security = user
    map to guest = never
    interfaces = lo ens19
    bind interfaces only = yes
    server min protocol = SMB3_00
    log file = /var/log/samba/log.%m
    max log size = 1000

[manuales]
    path = /srv/samba/manuales
    browseable = yes
    read only = no
    valid users = @soporte
    guest ok = no
    create mask = 0660
    directory mask = 2770
    smb encrypt = required
```

Verifica el nombre real de la interfaz LAB y conserva `lo`. SMB3 y el cifrado obligatorio presuponen clientes compatibles; Windows 11 y versiones actuales de `smbclient` lo son. No se habilita SMB1 para resolver un cliente obsoleto. `browseable` controla la visibilidad del recurso en consultas; no sustituye la autorización.

Habilita las cuentas Samba que realmente necesiten el servicio, introduciendo contraseñas distintas de las reales y sin incluirlas en el comando:

```bash
sudo smbpasswd -a ana
sudo smbpasswd -a bruno
sudo testparm -s
sudo systemctl restart smbd
systemctl status smbd --no-pager
sudo ss -lntp '( sport = :445 )'
smbclient -L //192.168.56.10 -U ana --client-protection=encrypt
smbclient //192.168.56.10/manuales -U ana --client-protection=encrypt
```

`testparm` comprueba la configuración, pero no demuestra que los permisos sean correctos. La escucha debe quedar limitada al laboratorio y a loopback; compruébalo. Si el ejercicio no requiere descubrimiento NetBIOS, no es necesario publicar sus servicios. Para el acceso moderno por dirección se utiliza TCP 445. Cualquier firewall del servidor debe permitir sólo el origen LAB para ese servicio, siguiendo una política única y documentada.

En el intérprete de `smbclient`, `ls`, `put archivo-local.txt`, `get prueba.txt` y `quit` permiten demostrar operaciones. Crea el archivo local antes de `put`. Desde Windows, usa `\\192.168.56.10\manuales` y una credencial del servidor. Las credenciales guardadas pueden provocar que una prueba con «otro usuario» siga usando la sesión previa. Inspecciona `Get-SmbConnection` y cierra sólo la conexión de laboratorio antes de repetir. No borres todas las conexiones de una sesión de trabajo real.

El usuario `bruno` se ha creado en Samba para demostrar una denegación de autorización: su contraseña puede validarse, pero no pertenece a `soporte`. Cuando se le añada al grupo, fuerza una sesión SMB nueva y repite. Si ya no se necesita, deshabilita la cuenta Samba con `smbpasswd -d bruno` y documenta la baja Unix por separado.

## 2.4 Windows Server: preparar un controlador de laboratorio

Utiliza Windows Server 2025 actualizado y con evaluación o licencia legítima. Prepara `dc01` antes de instalar AD. Haz copia del estado limpio de la VM. Usa una sola interfaz LAB durante la promoción; puede conectarse temporalmente una NIC NAT para instalar actualizaciones y retirarse después. No configures puerta de enlace en la LAB porque el segmento del ejercicio no incluye router.

Comprueba el nombre de la interfaz, su estado y la ausencia de una dirección de laboratorio previa. Los siguientes comandos son ejemplos de configuración para una VM nueva, no un script para reutilizar sobre cualquier servidor:

```powershell
Rename-Computer -NewName 'dc01' -Restart
```

Tras reiniciar, vuelve a abrir PowerShell elevado y configura la interfaz identificada:

```powershell
$LabAlias = 'Ethernet' # Sustituir por el nombre obtenido con Get-NetAdapter.
Get-NetIPConfiguration -InterfaceAlias $LabAlias
New-NetIPAddress -InterfaceAlias $LabAlias -IPAddress '192.168.56.11' -PrefixLength 24
Set-DnsClientServerAddress -InterfaceAlias $LabAlias -ServerAddresses '192.168.56.11'
Get-NetIPConfiguration -InterfaceAlias $LabAlias
Install-WindowsFeature AD-Domain-Services -IncludeManagementTools
```

Si existe DHCP u otra dirección, ajusta la configuración desde la consola después de identificarla; no acumules direcciones sin control. Una advertencia por no encontrar un DNS en la propia dirección es esperable antes de instalarlo, pero no justifica ignorar errores de instalación.

Promueve el bosque nuevo. La contraseña DSRM se solicita de forma interactiva y debe guardarse en un gestor protegido fuera de Git:

```powershell
$DsrmPassword = Read-Host 'Contraseña DSRM del laboratorio' -AsSecureString
Install-ADDSForest -DomainName 'ad.aula.test' -DomainNetbiosName 'AULA' `
  -InstallDNS -SafeModeAdministratorPassword $DsrmPassword
```

El asistente valida requisitos y solicita confirmación antes del reinicio. No suprimas las comprobaciones. Para el laboratorio aislado puede aparecer un aviso de delegación DNS porque no existe una zona padre administrada; hay que distinguirlo de un error de instalación. No se fija aquí un nivel funcional por números históricos: elige uno compatible con los controladores que realmente vayan a existir y consulta la documentación de la versión.

Después del reinicio:

```powershell
Get-ADDomain
Get-ADForest
Get-Service NTDS, DNS, Netlogon
Resolve-DnsName '_ldap._tcp.dc._msdcs.ad.aula.test' -Type SRV -Server '192.168.56.11'
dcdiag /test:dns
w32tm /query /status
```

Debe existir una respuesta SRV que señale al controlador y cuyo destino tenga dirección correcta. Revisa también los registros de AD DS y DNS en el Visor de eventos. Un aviso no se archiva automáticamente como «todo correcto»: se describe y se explica su efecto en esta topología.

## 2.5 OU, cuentas y grupos

En `dc01`, usa el módulo ActiveDirectory. Las cuentas de ejemplo no son personas reales. Las OU distinguen identidades y estaciones de trabajo; evita mover los controladores de su OU predeterminada como parte de esta práctica.

```powershell
Import-Module ActiveDirectory
$Base = 'DC=ad,DC=aula,DC=test'
New-ADOrganizationalUnit -Name 'Laboratorio' -Path $Base
New-ADOrganizationalUnit -Name 'Usuarios' -Path "OU=Laboratorio,$Base"
New-ADOrganizationalUnit -Name 'Equipos' -Path "OU=Laboratorio,$Base"
New-ADOrganizationalUnit -Name 'Grupos' -Path "OU=Laboratorio,$Base"
$ClaveAna = Read-Host 'Contraseña inicial de Ana' -AsSecureString
New-ADUser -Name 'Ana Laboratorio' -SamAccountName 'ana' `
  -UserPrincipalName 'ana@ad.aula.test' -Path "OU=Usuarios,OU=Laboratorio,$Base" `
  -AccountPassword $ClaveAna -Enabled $true -ChangePasswordAtLogon $true
New-ADGroup -Name 'GG_Soporte' -GroupScope Global -GroupCategory Security `
  -Path "OU=Grupos,OU=Laboratorio,$Base"
New-ADGroup -Name 'DL_Manuales_RW' -GroupScope DomainLocal -GroupCategory Security `
  -Path "OU=Grupos,OU=Laboratorio,$Base"
Add-ADGroupMember -Identity 'GG_Soporte' -Members 'ana'
Add-ADGroupMember -Identity 'DL_Manuales_RW' -Members 'GG_Soporte'
Get-ADGroupMember 'DL_Manuales_RW' -Recursive
```

Los comandos no son idempotentes: si el objeto existe, se comprueba en lugar de crearlo de nuevo. No reduzcas la complejidad de contraseñas para resolver una elección inválida. No uses la cuenta del dominio para abrir correo o navegar fuera del aula. Una baja implica deshabilitar, revocar sesiones y revisar recursos o tareas que dependan de la identidad; eliminar inmediatamente puede dificultar la investigación o transferencia de datos.

## 2.6 Unión del cliente y GPO acotada

En `cli01`, Windows 11 Pro, configura LAB como `192.168.56.20/24` y DNS `192.168.56.11`. La interfaz adicional no debe anunciar un DNS público que compita con el del dominio. Verifica la configuración resultante, no sólo el campo editado en una pantalla:

```powershell
Resolve-DnsName '_ldap._tcp.dc._msdcs.ad.aula.test' -Type SRV
Test-NetConnection 'dc01.ad.aula.test' -Port 389
w32tm /query /status
$JoinCredential = Get-Credential 'AULA\Administrator'
Add-Computer -DomainName 'ad.aula.test' `
  -OUPath 'OU=Equipos,OU=Laboratorio,DC=ad,DC=aula,DC=test' `
  -Credential $JoinCredential -Restart
```

La cuenta integrada puede tener nombre localizado o haberse renombrado: utiliza la cuenta de administración real. En un entorno gestionado debe delegarse el derecho de unión en vez de entregar credenciales de administrador de dominio. El puerto LDAP abierto es sólo una comprobación parcial; AD necesita más servicios y puertos.

Después del reinicio, inicia sesión como `ana@ad.aula.test`, cambia la contraseña si se solicita y comprueba `whoami /user` y `whoami /groups`. Crea en el controlador una GPO exclusiva para la OU Equipos de laboratorio. Ejemplo de directiva sencilla: desactivar reproducción automática en todas las unidades desde las Plantillas administrativas del equipo. Nombres y disponibilidad dependen del idioma y las plantillas ADMX.

En el cliente, desde una consola elevada para resultados de equipo:

```powershell
gpupdate /force
gpresult /r /scope computer
gpresult /h C:\Windows\Temp\resultado-gpo-lab.html
```

Identifica en el informe la GPO aplicada y la configuración resultante. Un vínculo a la OU Usuarios no aplica por sí mismo una configuración de equipo. El filtrado de seguridad, permisos de lectura, herencia, enlaces y ubicación del objeto explican muchas ausencias. Evita modificar la Default Domain Policy para una prueba aislada: vincula una GPO nueva y deja clara su reversión.

## 2.7 Permisos NTFS y SMB con grupos

Un servidor miembro separado sería el destino habitual de archivos. Para estudiar la mecánica con recursos limitados puede usarse una carpeta de datos aislada del laboratorio, explicando que no es el diseño recomendado para un DC de producción. No compartas `C:\Windows`, `SYSVOL`, `NTDS` ni todo el disco. La carpeta debe estar en un volumen NTFS y no contener datos existentes.

```powershell
New-Item -ItemType Directory -Path 'C:\DatosLab\Manuales'
icacls 'C:\DatosLab\Manuales'
icacls 'C:\DatosLab\Manuales' /grant 'AULA\DL_Manuales_RW:(OI)(CI)M'
New-SmbShare -Name 'ManualesLab' -Path 'C:\DatosLab\Manuales' `
  -ChangeAccess 'AULA\DL_Manuales_RW' -FullAccess 'AULA\Domain Admins' -EncryptData $true
Get-SmbShareAccess -Name 'ManualesLab'
icacls 'C:\DatosLab\Manuales'
```

El nombre del grupo integrado Domain Admins puede estar localizado. Sustitúyelo por su nombre real tras consultar AD. La carpeta puede heredar permisos de su padre: revisa `icacls` y «Acceso efectivo». No basta con añadir el grupo si otro permiso heredado concede escritura a todos. Antes de retirar herencia, guarda ACL y asegura acceso de SYSTEM y administradores; realiza el cambio desde consola, en un recurso de prueba y con un plan de recuperación.

Desde una sesión de Ana prueba crear, modificar y eliminar un archivo. Desde una cuenta de auditoría sin pertenencia al grupo prueba la denegación. Comprueba de nuevo tras una sesión nueva si cambias miembros. Conserva una tabla: principal, grupo funcional, grupo de recurso, derecho SMB, derecho NTFS y resultado observado.

## 2.8 Copia y recuperación del servidor

Para datos de Samba, una copia debe preservar contenido, propietarios, ACL y atributos necesarios. En el laboratorio puede detenerse brevemente la escritura, copiar con una herramienta que preserve esos metadatos a otro soporte y restaurar en una ruta alternativa. Un archivo comprimido guardado en el mismo volumen no protege frente a fallo del volumen. La base de credenciales Samba exige además una copia coherente y protegida siguiendo el método soportado para su backend; no se copia en caliente cualquier base de datos como si fuera texto.

Para AD, utiliza Windows Server Backup u otra solución compatible con AD y el estado del sistema. Instala la característica si procede, configura un destino independiente y verifica que la copia termina correctamente. `wbadmin get versions` permite consultar versiones disponibles. La recuperación del bosque tiene un procedimiento específico que incluye credenciales de recuperación, orden y comprobaciones; no se sustituye con «volver a una instantánea antigua» sobre controladores en funcionamiento.

En el aula puede restaurarse una VM aislada para estudiar el procedimiento. Desconecta su red de la del dominio original y evita dos controladores con la misma identidad en el mismo segmento. Mide tiempo de preparación, restauración y comprobación del servicio. La evidencia útil es que una cuenta, archivo o servicio recuperado funciona y mantiene permisos, además del mensaje de copia completada.

## Referencias operativas

- [Samba: manual de smb.conf](https://www.samba.org/samba/docs/current/man-html/smb.conf.5.html) y [smbclient](https://www.samba.org/samba/docs/current/man-html/smbclient.1.html).
- [Debian Reference: administración](https://www.debian.org/doc/manuals/debian-reference/).
- [Microsoft: instalación de AD DS](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-).
- [Microsoft: Add-Computer](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/add-computer).
- [Microsoft: New-SmbShare](https://learn.microsoft.com/en-us/powershell/module/smbshare/new-smbshare).
- [Microsoft: guía de recuperación del bosque AD](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-guide).

Consulta `man smb.conf`, `man setfacl`, `Get-Help` y las versiones de paquetes instaladas. La guía está diseñada para Debian 13 y Windows Server 2025; rutas de interfaz, nombres de grupos localizados y herramientas opcionales deben confirmarse en cada instalación.
