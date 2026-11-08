# 02 · Instalación y administración del puesto

[Volver al módulo](README.md) · [Continuar con las prácticas](03-practicas.md)

## 1. Convenciones y control de cambios

Los bloques de consulta se pueden utilizar para observar un sistema autorizado. Los bloques marcados como cambio requieren una VM de laboratorio, datos ficticios y recuperación disponible. No ejecutes comandos sobre un disco por copiar una ruta de un ejemplo: nombres como `/dev/sda` pueden cambiar entre arranques y dispositivos.

Antes de cada modificación registra estado inicial, objetivo, acción exacta, resultado esperado y reversión. Una captura acredita lo que muestra, pero una salida de texto anonimizada y una explicación suelen facilitar más la revisión. No incluyas claves, tokens, contraseñas, direcciones personales ni contenido ajeno.

## 2. Preparar e instalar Debian 13

### Preparación

1. Descarga la imagen desde Debian y verifica su suma con el archivo publicado. La verificación criptográfica de los archivos de sumas añade comprobación de autenticidad si se realiza con claves y procedimiento oficiales.
2. Crea una VM amd64 con firmware UEFI, red NAT para descargar paquetes y un único disco virtual nuevo. Como punto inicial de aula pueden servir 2 vCPU, 4 GiB de RAM y 40 GiB de disco para un escritorio moderado; ajusta al entorno y espacio del anfitrión.
3. Anota nombre, ubicación y tamaño del disco virtual. No conectes discos físicos ni unidades del anfitrión a la VM.
4. Reserva un destino de copia independiente y documenta el mecanismo de recuperación. Un snapshot anterior a una instalación vacía no sustituye una copia del trabajo posterior.

### Instalación guiada

Arranca la ISO en UEFI y selecciona idioma, teclado, zona horaria y nombre de equipo de laboratorio. Elige una cuenta ordinaria. El comportamiento de `sudo` depende de cómo configures la cuenta root y el usuario durante la instalación: compruébalo al finalizar en vez de asumirlo.

En particionado identifica el único disco virtual vacío por capacidad. La opción guiada sobre todo el disco **elimina su contenido**; solo se utiliza porque se ha preparado un dispositivo desechable. Revisa el resumen antes de confirmar escritura. El instalador creará los elementos de arranque y sistemas de archivos adecuados al modo elegido. Si se practica LVM o cifrado, documenta las capas y el procedimiento aprobado para recuperar claves sin publicarlas.

Selecciona un conjunto de software coherente, repositorios oficiales y el cargador de arranque correspondiente. Al terminar retira la ISO virtual y reinicia desde el disco. Conserva notas de decisiones, no fotografías de contraseñas.

### Comprobar la instalación: consulta

```bash
cat /etc/os-release
test -d /sys/firmware/efi && printf 'Arranque UEFI\n'
lsblk -o NAME,TYPE,SIZE,FSTYPE,UUID,MOUNTPOINTS
findmnt /
id
systemctl --failed
journalctl -b -p err
```

El directorio EFI ayuda a identificar el modo del arranque actual. `lsblk` y `findmnt` relacionan disco, particiones y montaje real. La ausencia de unidades fallidas no demuestra que todas las aplicaciones funcionen, pero detecta problemas de integración que deben revisarse. Examina los mensajes en contexto; no todos implican una instalación inválida.

La guía oficial de [instalación de Debian 13](https://www.debian.org/releases/trixie/installmanual) describe decisiones y variaciones por arquitectura.

## 3. Preparar e instalar Windows 11 Pro

Usa medio oficial, edición autorizada y requisitos admitidos. Configura firmware, Secure Boot y TPM virtual de acuerdo con el hipervisor y los requisitos oficiales. No utilices procedimientos para eludir comprobaciones como base del laboratorio. Mantén recursos suficientes también en el anfitrión; los mínimos de instalación no equivalen a una experiencia de trabajo adecuada.

1. Crea otra VM con un disco virtual nuevo claramente identificado. No reutilices el disco de Debian salvo que el objetivo explícito sea practicar un escenario distinto.
2. Arranca el medio en UEFI. Selecciona la edición correspondiente a la licencia o evaluación disponible.
3. En instalación personalizada, revisa el disco de destino. Sobre un disco de laboratorio vacío, selecciona espacio sin asignar y permite que el instalador cree las particiones necesarias. Borrar particiones destruye su contenido; no se hace sobre un equipo real como paso rutinario.
4. Completa el asistente con las opciones de identidad permitidas por la versión y política del centro. No introduzcas credenciales de producción en capturas ni en la documentación pública.
5. Instala controladores o herramientas del hipervisor desde procedencia oficial. Ejecuta Windows Update y revisa reinicios pendientes.
6. Verifica edición, activación por el canal legítimo, versión, almacenamiento, dispositivos y recuperación.

Consultas en PowerShell:

```powershell
Get-ComputerInfo |
    Select-Object WindowsProductName, WindowsVersion, OsBuildNumber, OsArchitecture
Get-Disk | Select-Object Number, PartitionStyle, Size, OperationalStatus
Get-Volume | Select-Object DriveLetter, FileSystem, HealthStatus, SizeRemaining, Size
Get-PnpDevice -PresentOnly | Where-Object Status -ne 'OK'
Get-Service | Where-Object Status -eq 'Running' | Select-Object -First 15 Name, Status
```

Corrobora la edición también en Configuración si alguna propiedad histórica devuelve una denominación inesperada. Las consultas WMI/CIM pueden mantener campos de compatibilidad. El criterio de aceptación incluye arrancar, actualizar, reiniciar y utilizar aplicaciones de prueba, no solo terminar el asistente.

Consulta [requisitos de Windows 11](https://learn.microsoft.com/windows/whats-new/windows-11-requirements) y [particionado para UEFI](https://learn.microsoft.com/windows-hardware/manufacture/desktop/windows-setup-installing-using-the-mbr-or-gpt-partition-style).

## 4. Linux: explorar sin modificar

```bash
pwd
ls -lah
df -hT
df -i
findmnt
ps -eo pid,ppid,user,stat,%cpu,%mem,comm --sort=-%cpu | head -15
free -h
vmstat 1 5
```

`df -hT` informa de capacidad por sistema de archivos y `df -i` del consumo de inodos; puede agotarse uno sin agotar el otro. `du` mide uso de árboles de directorios y puede diferir de `df` por archivos abiertos sin nombre, reservas, montajes o permisos. `vmstat` ofrece varias muestras; la primera suele resumir desde el arranque y las siguientes reflejan los intervalos solicitados.

Los porcentajes de CPU de distintas herramientas pueden tener escalas diferentes en sistemas multinúcleo. Registra herramienta y criterio antes de comparar. Para investigar un proceso, identifica PID, usuario, ejecutable y relación con el síntoma. No cierres procesos del sistema porque aparezcan arriba en una tabla.

## 5. Linux: usuarios y permisos en un directorio de práctica

**Cambio en VM.** Se crean dos identidades ficticias y un grupo. Comprueba antes ambos usuarios con `getent passwd alumno_smr` y `getent passwd visitante_smr`, y el grupo con `getent group taller_smr`. Comprueba también que `/srv/taller-smr-lab` no exista. Si alguno existe, detén y elige nombres exclusivos de laboratorio, adaptando todas las rutas y referencias; no modifiques cuentas ni directorios previos.

```bash
sudo groupadd taller_smr
sudo useradd --create-home --shell /bin/bash alumno_smr
sudo useradd --create-home --shell /bin/bash visitante_smr
sudo usermod --append --groups taller_smr alumno_smr
sudo install -d -o root -g taller_smr -m 2770 /srv/taller-smr-lab
```

El bit `2` inicial activa setgid para que nuevos objetos hereden el grupo del directorio. No se ha establecido contraseña a esas cuentas: las pruebas se realizan mediante cambio de identidad administrativo, sin habilitar acceso interactivo externo.

```bash
sudo -u alumno_smr sh -c 'umask 007; printf "dato ficticio\n" > /srv/taller-smr-lab/parte.txt'
ls -ld /srv/taller-smr-lab
ls -l /srv/taller-smr-lab/parte.txt
sudo -u alumno_smr cat /srv/taller-smr-lab/parte.txt
sudo -u visitante_smr cat /srv/taller-smr-lab/parte.txt
```

La última lectura debe ser denegada. Si no lo es, investiga identidad efectiva, permisos del camino y posibles ACL; no des por válida la práctica. `sudo -u` requiere privilegio autorizado y sirve para evaluar acceso local; no demuestra autenticación mediante contraseña.

Si el paquete `acl` está disponible, consulta con `getfacl /srv/taller-smr-lab`. Las ACL permiten excepciones adicionales y su máscara puede limitar derechos efectivos. Antes de introducirlas domina el modelo de propietario, grupo y resto. La reversión recomendada del ejercicio es restaurar la VM al punto documentado, no ejecutar borrados amplios de cuentas o directorios.

## 6. Windows: cuentas y ACL locales

Para observar identidades y permisos:

```powershell
whoami
whoami /groups
Get-LocalUser | Select-Object Name, Enabled
Get-LocalGroup | Select-Object Name
Get-Acl -LiteralPath 'C:\Users\Public' |
    Format-List Owner, AccessToString
```

**Cambio en VM con consola elevada.** Crea mediante Administración de equipos una cuenta local ficticia y un grupo de práctica. Si utilizas PowerShell para una contraseña, recógela con `Read-Host -AsSecureString`; no escribas su valor en comandos, historial ni archivos. La política y versión pueden limitar operaciones de cuenta: documenta el método admitido en tu entorno.

Para practicar NTFS crea una carpeta exclusiva `C:\SMR-Lab-Datos` y, desde Propiedades → Seguridad → Opciones avanzadas, revisa primero propietario y herencia. Conserva acceso de administración y SYSTEM; configura solo la carpeta de laboratorio. Concede lectura al grupo de visitantes y modificación al de edición. Evita añadir denegaciones si basta con no conceder un derecho.

Comprueba acceso efectivo y prueba con una sesión ordinaria de cada cuenta: leer un archivo, crear otro, modificarlo y eliminarlo. Anota cada resultado. Las sesiones ya abiertas pueden conservar pertenencias a grupos anteriores: cierra sesión y vuelve a entrar tras cambios. No cambies ACL recursivamente en `C:\`, `Windows` o perfiles reales para realizar el ejercicio.

## 7. Paquetes, actualizaciones y servicios

En Debian, consultas:

```bash
apt policy
apt policy bash
dpkg-query -W -f='${binary:Package}\t${Version}\n' bash
systemctl status cron --no-pager
systemctl is-enabled cron
journalctl -u cron -b --no-pager -n 30
```

El servicio `cron` puede no estar instalado; un mensaje de unidad inexistente es información de inventario, no una avería universal. El nombre real de una unidad se verifica con `systemctl list-unit-files`. Para practicar cambios elige un servicio no crítico instalado expresamente en la VM.

**Cambio en VM:** `sudo apt update` actualiza índices; después `apt list --upgradable` muestra candidatos. `apt -s upgrade` simula la resolución. Revisa cambios y espacio disponible antes de `sudo apt upgrade`. Algunas operaciones requieren reinicio; comprueba el estado del sistema y las recomendaciones de los paquetes. No añadas repositorios o claves de fuentes desconocidas para resolver un error de dependencias.

Iniciar un servicio con `systemctl start nombre.service` afecta al estado actual; habilitarlo con `systemctl enable nombre.service` afecta a activación prevista. Utiliza el nombre verificado, explica la diferencia y confirma ambos estados. Al acabar devuelve la configuración original o restaura la VM.

En Windows revisa Windows Update, Administrador de dispositivos y servicios. Antes de detener un servicio identifica dependencias, identidad y función. No deshabilites seguridad o actualizaciones para mejorar un resultado de rendimiento sin un objetivo de laboratorio delimitado y autorizado.

## 8. Copias de datos con verificación

Este ejemplo usa un directorio de usuario y un archivo tar; ambos pueden residir en el mismo disco y por ello **no constituyen una copia independiente frente a fallo físico**. Sirve para practicar el mecanismo. En una copia real mueve el artefacto a un destino aprobado e independiente y verifica acceso y retención.

**Cambio acotado en Linux:**

```bash
lab_dir="$HOME/smr-lab-copia"
mkdir -p "$lab_dir/origen" "$lab_dir/restaurado"
printf 'Contenido ficticio de SMR\n' > "$lab_dir/origen/documento.txt"
tar -C "$lab_dir/origen" -czf "$lab_dir/copia.tar.gz" .
tar -tzf "$lab_dir/copia.tar.gz"
tar -C "$lab_dir/restaurado" -xzf "$lab_dir/copia.tar.gz"
cmp "$lab_dir/origen/documento.txt" "$lab_dir/restaurado/documento.txt"
sha256sum "$lab_dir/origen/documento.txt" "$lab_dir/restaurado/documento.txt"
```

`cmp` sin salida y con código cero confirma igualdad del archivo comparado. Las sumas permiten detectar cambios de contenido, pero no verifican por sí solas permisos, propiedad, ACL, disponibilidad futura ni autenticidad si un atacante puede reemplazar datos y sumas. Para conservar metadatos complejos necesitas opciones y herramientas adecuadas, privilegios y una prueba explícita.

En Windows, ejemplo sobre archivos ficticios:

```powershell
$labPath = Join-Path $env:USERPROFILE 'SMR-Lab-Copia'
$sourcePath = Join-Path $labPath 'Origen'
$restorePath = Join-Path $labPath 'Restaurado'
New-Item -ItemType Directory -Force -Path $sourcePath, $restorePath | Out-Null
'Contenido ficticio de SMR' | Set-Content -LiteralPath (Join-Path $sourcePath 'documento.txt')
Copy-Item -LiteralPath (Join-Path $sourcePath 'documento.txt') -Destination $restorePath
Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $sourcePath 'documento.txt')
Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $restorePath 'documento.txt')
```

`Copy-Item` muestra una copia sencilla y no promete preservar todos los metadatos de seguridad. Para procedimientos con Robocopy revisa opciones, códigos de salida y simulación; evita `/MIR` sobre destinos con contenido que deba conservarse, porque puede eliminar archivos. La restauración debe verificarse en una ubicación separada antes de reemplazar el original.

## 9. Automatizar de forma mantenible

Un script de copia debe validar que existen origen y destino, controlar errores y registrar fecha, duración y resultado sin secretos. Utiliza rutas explícitas, comillas y una identidad que tenga solo los derechos necesarios. Prueba primero manualmente y después en el Programador de tareas de Windows o en un temporizador systemd de usuario.

Para el temporizador, consulta la documentación del sistema: entorno de usuario, disponibilidad tras cerrar sesión y comportamiento ante un horario perdido son decisiones distintas. Para el Programador de tareas registra si exige sesión iniciada, nivel de privilegio y directorio de inicio. No marques éxito por el hecho de que exista un archivo: compara su contenido y la fecha de la ejecución esperada.

## Referencias de comandos

- [Debian: apt](https://manpages.debian.org/trixie/apt/apt.8.en.html).
- [Debian: permisos access](https://manpages.debian.org/trixie/manpages-dev/access.2.en.html).
- [systemctl](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html).
- [Microsoft Learn: Get-Acl](https://learn.microsoft.com/powershell/module/microsoft.powershell.security/get-acl).
- [Microsoft Learn: Robocopy](https://learn.microsoft.com/windows-server/administration/windows-commands/robocopy).
- [GNU tar: manual](https://www.gnu.org/software/tar/manual/).
