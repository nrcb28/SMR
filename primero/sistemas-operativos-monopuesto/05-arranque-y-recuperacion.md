# 05 · Arranque, configuración y recuperación por etapas

[Índice](README.md) · [Hardware y firmware](../montaje-y-mantenimiento-de-equipos/01-fundamentos.md)

## 1. Un mapa de dependencias antes de reparar

El arranque no es una operación única. Firmware, selección de dispositivo, cargador, kernel, acceso al volumen del sistema, servicios y sesión de usuario forman una cadena. Una reparación eficaz identifica la última etapa que funciona y la primera que falla. Si se ve un mensaje del kernel, ya se ha ejecutado más infraestructura que cuando el firmware indica que no encuentra medio de arranque.

Construye una tabla con cuatro columnas: etapa, objeto que necesita, evidencia observable y siguiente hipótesis. Por ejemplo, el cargador necesita sus archivos y configuración; el kernel necesita acceder al dispositivo y al sistema de archivos de raíz; un inicio de sesión necesita servicios y credenciales. Esta tabla evita aplicar una herramienta de cargador a un fallo de perfil de usuario o reinstalar un SO por una entrada de firmware mal seleccionada.

En una VM también hay dos entornos: el hipervisor configura firmware, discos y orden de arranque, mientras el invitado administra sus volúmenes y cargadores. Si se desconecta el disco virtual desde el hipervisor, cambiar `/etc/fstab` no puede volver a presentarlo. Registra ambos niveles y conserva la consola disponible durante los experimentos.

## 2. UEFI, ESP y entradas de firmware

En una instalación UEFI habitual, el firmware carga una aplicación EFI desde una partición de sistema adecuada. La partición ESP contiene archivos del entorno de arranque; no equivale a la partición donde reside todo el SO. GPT describe particiones, UEFI describe firmware y Secure Boot introduce comprobaciones de confianza de componentes. Son elementos relacionados, pero sus nombres no son intercambiables.

Un fallo de entrada de firmware puede coexistir con los archivos del cargador intactos. Una ESP accesible no demuestra que la entrada elegida apunte a ella. Tampoco demuestra que el resto de volúmenes esté correcto. Antes de modificar entradas, identifica discos, particiones, modo de arranque actual y configuración previa. No borres entradas «duplicadas» sin conocer su propósito y posibilidad de recuperación.

En Linux puedes consultar el contexto sin alterar el firmware:

```bash
test -d /sys/firmware/efi && printf '%s\n' 'Sesión iniciada en contexto UEFI'
lsblk -o NAME,TYPE,SIZE,FSTYPE,PARTUUID,UUID,MOUNTPOINTS
findmnt -T /boot
findmnt -T /boot/efi
```

`findmnt -T` identifica el sistema de archivos que contiene la ruta, pero una ruta existente no implica que la ESP esté montada allí: revisa tipo, origen y punto de montaje. Las consultas de UUID y particiones sirven para relacionar capas; los identificadores deben sanitizarse si contienen información que no necesitas compartir.

## 3. Linux: cargador, kernel e initramfs

El cargador permite seleccionar un kernel y sus argumentos. El kernel necesita los controladores y pasos que permitan localizar y montar el sistema raíz; un initramfs aporta un entorno temprano con herramientas y módulos según la instalación. Si esa etapa no puede encontrar el volumen esperado, puede aparecer una consola de rescate temprana aunque los archivos de usuario sigan existiendo.

Distingue nombre de dispositivo y UUID. Los nombres como `/dev/sda` dependen de enumeración y pueden cambiar al añadir discos; un UUID referencia un volumen identificado. Si clonaste una VM o modificaste su almacenamiento, verifica si existen identificadores duplicados o referencias antiguas. Cambiar todas las referencias por el primer disco visible es una corrección peligrosa cuando no se ha trazado la instalación.

Desde un sistema que sí arranca, consultas útiles son:

```bash
uname -r
cat /proc/cmdline
ls -lh /boot
systemctl --failed
journalctl -b -p warning --no-pager
```

`/proc/cmdline` muestra parámetros de la sesión actual; no demuestra qué ocurrirá en la siguiente selección del cargador. El listado de `/boot` permite comprobar archivos presentes, pero no certifica su coherencia. `journalctl -b` consulta el arranque actual que el journal ha podido registrar; un fallo anterior al montaje o al servicio de registros puede no aparecer ahí.

## 4. `/etc/fstab` y modos de emergencia

`fstab` describe montajes y opciones persistentes. Una entrada errónea de un volumen secundario puede impedir alcanzar el objetivo normal según sus opciones y dependencias. Eso no implica que todo el sistema raíz esté destruido. El diagnóstico compara identificador declarado, dispositivo disponible, tipo de sistema de archivos y requisitos del montaje.

Antes de editar, conserva copia con permisos apropiados y registra la línea exacta. Utiliza un editor y la documentación de `fstab`; no ejecutes una sustitución global que cambie identificadores similares. En un laboratorio desechable puedes estudiar el efecto de una entrada de montaje secundaria preparada por el docente, con snapshot y medio de rescate. No se enseña a romper la referencia de raíz o de un volumen cifrado real para provocar una incidencia.

Las opciones como `nofail` cambian dependencias y comportamiento frente a un recurso ausente; no reparan un disco ni garantizan que una aplicación pueda continuar sin sus datos. Si el volumen contiene datos requeridos por un servicio, iniciar el servicio sin montarlo puede provocar escrituras en el directorio subyacente. Antes de elegir la opción, decide qué debe hacer la aplicación cuando falta almacenamiento.

## 5. Windows: entorno de arranque y BCD

Windows Boot Manager utiliza información de configuración para seleccionar y cargar componentes. El almacén BCD contiene objetos del entorno de arranque; una aplicación de usuario dañada o un perfil que no inicia no se arreglan necesariamente reconstruyendo ese almacén. El mensaje, momento y alcance del fallo orientan la etapa.

Consulta primero el modo de firmware y la configuración del sistema mediante Información del sistema y las herramientas de recuperación admitidas. `bcdedit /enum` es una consulta que puede requerir elevación según el almacén y el contexto. No copies identificadores de ejemplo como si pertenecieran a tu instalación, y no utilices opciones de modificación sin conocer el objeto afectado.

En Windows RE, las letras de unidades pueden ser distintas a las de la sesión normal. Una partición de Windows que normalmente es `C:` puede aparecer con otra letra. Debes identificar contenido, tamaño y función; elegir una letra por costumbre puede hacer que una herramienta copie archivos desde el sistema equivocado o escriba en la partición incorrecta.

BCDBoot es una herramienta de configuración de archivos de arranque, no una rutina para aplicar indiscriminadamente. Su uso requiere identificar directorio de Windows, partición de destino, modo de firmware y propósito de la operación. Por esa razón aquí se estudia el procedimiento y la referencia oficial, sin ofrecer una orden universal de reparación con letras inventadas.

## 6. Cifrado, TPM y claves de recuperación

Cuando existe cifrado del dispositivo o BitLocker, algunos cambios de firmware, arranque o hardware pueden hacer necesaria una recuperación. La clave se conserva por un canal autorizado separado del equipo y no se escribe en la memoria pública ni en el repositorio. Antes de intervenir, comprueba que existe un procedimiento real para recuperarla; «creo que está en la cuenta» no constituye una prueba suficiente.

Un volumen bloqueado no equivale a datos borrados y un pedido de clave no prueba necesariamente un ataque. Pero tampoco debes desactivar controles de seguridad para ocultar el síntoma. Identifica cambio reciente, política y estado del protector, y sigue el procedimiento de soporte. En una práctica con datos sintéticos, ensaya acceso a la documentación de recuperación sin publicar la clave.

Las copias también deben ser recuperables. Si una copia cifrada depende de una contraseña o certificado almacenado sólo dentro del equipo averiado, la copia puede no resolver el incidente. Relaciona datos, claves, herramientas y entorno de recuperación como dependencias separadas en la [plantilla de copias](../../recursos/plantillas/plan-de-copias.md).

## 7. Recuperación escalonada

Primero conserva el estado: fotografía o texto del error, cambios recientes, versiones y estructura conocida. Después prueba opciones reversibles que correspondan a la etapa: seleccionar la entrada correcta, utilizar una versión anterior de kernel ya instalada y admitida o entrar en un entorno de recuperación oficial. No elimines el estado anterior antes de comprobar que la alternativa funciona.

Si hace falta iniciar un medio externo, verifica procedencia y arranque en el modo adecuado. El entorno externo no reconoce mágicamente qué instalación quieres reparar. Enumera dispositivos, identifica el volumen y decide si primero debe montarse sólo para lectura o si procede una intervención supervisada. El rescate de Debian y Windows RE tienen herramientas y supuestos diferentes; no se mezclan recetas sin adaptar.

Una reinstalación completa puede ser una decisión válida cuando existe copia y el tiempo de recuperación lo justifica, pero debe describirse como tal. Reinstalar y perder el diagnóstico no confirma qué falló. Conserva al menos el incidente, motivo de la decisión, datos restaurados y pruebas del nuevo puesto.

## 8. Caso de estudio: SO llega a emergencia tras añadir disco

El equipo funcionaba y, después de añadir un disco de laboratorio, muestra una consola de emergencia. Hipótesis: una referencia por nombre de dispositivo cambió, se creó una entrada `fstab` con UUID equivocado, falta un volumen requerido o existe un problema de controlador. No asumas corrupción del sistema raíz antes de comprobar qué se ha montado.

Compara el inventario anterior con `lsblk` y el error de la unidad de montaje. Si la referencia antigua apunta a otro dispositivo, identifica correctamente el volumen y corrige sólo la entrada relacionada, con copia previa. Si el volumen no aparece en el SO pero sí en firmware, investiga controlador y kernel; si no aparece en ninguno, vuelve al trayecto físico o virtual.

La aceptación incluye arranque normal, origen de cada montaje, datos esperados y ausencia del fallo tras reiniciar. Debes comprobar que no se ha «solucionado» comentando un montaje que la aplicación realmente necesita. Documenta también qué ocurrirá si se vuelve a retirar el disco secundario.

## 9. Práctica ampliada: ensayo de recuperación sin destruir arranque

En una VM desechable, prepara medio oficial de recuperación, inventario de particiones, snapshot y un archivo sintético cuyo hash conozcas. Accede al entorno de rescate y localiza el volumen correcto sin modificarlo. Demuestra lectura de ese archivo o una copia autorizada hacia un destino de laboratorio y vuelve a iniciar la VM normalmente.

El objetivo es probar el procedimiento antes de necesitarlo. No hace falta romper el cargador ni borrar particiones. Entrega mapa de etapas, identificación del volumen en ambos entornos y evidencias de que el archivo conserva su contenido. Rúbrica propia: identificación 30 %, preparación 25 %, preservación 25 % y validación/comunicación 20 %.

## Fuentes primarias

- [Debian: inicialización del sistema](https://www.debian.org/doc/manuals/debian-reference/ch03.en.html).
- [Debian: recuperación de un sistema](https://www.debian.org/releases/stable/amd64/ch08s06.en.html).
- [Linux: initramfs](https://www.kernel.org/doc/html/latest/filesystems/ramfs-rootfs-initramfs.html).
- [Microsoft: opciones de BCDBoot](https://learn.microsoft.com/windows-hardware/manufacture/desktop/bcdboot-command-line-options-techref-di).
- [Microsoft: Windows Recovery Environment](https://learn.microsoft.com/windows-hardware/manufacture/desktop/windows-recovery-environment--windows-re--technical-reference).
- [Microsoft: recuperación de BitLocker](https://learn.microsoft.com/windows/security/operating-system-security/data-protection/bitlocker/recovery-overview).
