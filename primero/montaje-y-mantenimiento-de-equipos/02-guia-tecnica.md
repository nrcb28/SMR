# 02 · Procedimientos de montaje y mantenimiento

[Volver al módulo](README.md) · [Realizar las prácticas](03-practicas.md)

## 1. Preparar una orden de trabajo

Una intervención empieza con el estado inicial y el alcance autorizado. Registra identificador de activo, síntomas, cuándo aparecen, cambios recientes, disponibilidad necesaria y ubicación de las copias. No escribas contraseñas, números de serie personales, claves de cifrado ni nombres reales en evidencias públicas. Si el equipo contiene datos de producción, la autorización de mantenimiento no implica autorización para inspeccionarlos.

Una ficha útil contiene:

```text
Activo: LAB-PC-01
Objetivo: sustituir un SSD de laboratorio por otro compatible
Estado inicial: arranque correcto; capacidad insuficiente
Datos que conservar: conjunto ficticio de la práctica
Copia verificada: identificador de copia y prueba de restauración
Cambio previsto: modelo y puerto del nuevo dispositivo
Plan de reversión: reinstalar el dispositivo original sin alterarlo
Pruebas de aceptación: arranque, integridad, reinicio y carga representativa
```

Establece un punto de parada: humo, olor, líquido, batería deformada, daños en conectores o pérdida de una copia obligan a detener la intervención y comunicarla al responsable. Probar repetidamente un dispositivo dañado puede empeorar el estado.

## 2. Inventario por software: operaciones de consulta

En Debian, los siguientes comandos leen información. Algunos paquetes pueden no estar instalados. Utiliza `apt policy nombre-paquete` antes de decidir su instalación; instalar software sí modifica el equipo y se hace en una VM o puesto autorizado.

```bash
cat /etc/os-release
uname -r
lscpu
free -h
lsblk -o NAME,TYPE,SIZE,MODEL,SERIAL,FSTYPE,MOUNTPOINTS
lspci -nnk
lsusb
sudo dmidecode --type memory
```

`lscpu` identifica arquitectura y CPU lógicas. `free` distingue memoria usada, disponible y caché: poca memoria marcada como libre no demuestra presión si existe caché recuperable. `lsblk` relaciona dispositivos, particiones y puntos de montaje; el número de serie permite no confundir dos discos del mismo tamaño. Ocúltalo en la entrega pública. `lspci -nnk` muestra identificadores y controlador del kernel en uso. SMBIOS puede proporcionar datos incompletos o genéricos, especialmente dentro de una VM; `dmidecode` no sustituye una inspección del modelo físico.

En PowerShell de Windows 11, estas consultas no necesitan cambiar la configuración:

```powershell
Get-CimInstance Win32_Processor |
    Select-Object Name, NumberOfCores, NumberOfLogicalProcessors
Get-CimInstance Win32_PhysicalMemory |
    Select-Object Capacity, Speed, ConfiguredClockSpeed, PartNumber
Get-CimInstance Win32_BaseBoard |
    Select-Object Manufacturer, Product, Version
Get-Disk | Select-Object Number, FriendlyName, PartitionStyle, Size, OperationalStatus
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, Size
Get-PnpDevice -PresentOnly | Where-Object Status -ne 'OK'
```

`HealthStatus` depende de lo que expongan el controlador y el dispositivo. No es equivalente a un análisis físico completo. `Speed` y `ConfiguredClockSpeed` pueden diferir y algunos firmwares no informan correctamente; conserva ambas y contrasta con UEFI. En una VM puedes ver el modelo del disco virtual y ningún dato SMART del dispositivo físico.

## 3. Seleccionar una configuración

Transforma una necesidad general en requisitos comprobables. Para un puesto ofimático pueden ser suficientes gráficos integrados, baja sonoridad y almacenamiento moderado; una estación con grandes máquinas virtuales necesita más RAM y capacidad. Define un trabajo representativo y el tiempo máximo aceptable antes de presupuestar.

| Elemento | Comprobación obligatoria | Evidencia |
| --- | --- | --- |
| CPU y placa | Zócalo, soporte del modelo y firmware mínimo | Lista de soporte del fabricante |
| RAM | Generación, capacidad máxima, ranuras y configuración de canales | Manual y referencia exacta |
| SSD M.2 | Longitud, llave, protocolo y reparto de líneas | Diagrama del manual |
| Fuente | Conectores, potencia disponible y recomendación de GPU | Ficha técnica y esquema |
| Caja | Formato de placa, altura del disipador, longitud de GPU | Cotas en milímetros |
| Refrigeración | Anclaje, capacidad y acceso para mantenimiento | Compatibilidad y disposición |
| SO | CPU admitida, arranque, TPM y controladores cuando proceda | Requisitos oficiales de la versión |

Compara el coste total, incluida licencia, adaptación, consumo, garantía y mano de obra. Una placa barata que obliga a sustituir la RAM o actualizar firmware sin CPU compatible puede salir más cara. No inventes precios vigentes: fecha y proveedor forman parte de cualquier presupuesto real.

## 4. Montaje seguro paso a paso

Este procedimiento se aplica a una torre de laboratorio. Portátiles, equipos compactos y sistemas de fabricante requieren su manual de servicio específico.

1. Apaga correctamente, retira alimentación de red y periféricos; espera el tiempo recomendado por el fabricante. En portátiles desconecta la batería solo mediante el procedimiento indicado.
2. Prepara mesa limpia, iluminación, recipientes para tornillos y control ESD. Utiliza pulsera y superficie apropiadas conforme a las instrucciones del puesto. No apoyes componentes sobre superficies conductoras inadecuadas ni sobre el exterior de una bolsa antiestática.
3. Revisa que la caja tenga separadores únicamente donde coinciden los orificios de la placa. Un separador sobrante puede provocar un cortocircuito.
4. Identifica orientación de CPU y zócalo. Manipula por los bordes, no toques contactos y no fuerces. En determinados zócalos los contactos delicados están en la placa.
5. Instala el sistema térmico con la cantidad de material y secuencia de apriete indicadas. Retira una eventual película protectora de la base. Conecta el ventilador al encabezado correcto.
6. Inserta los módulos RAM en las ranuras recomendadas para esa población. Comprueba cierres y asiento uniforme.
7. Monta almacenamiento y placa sin exceder los pares o presiones recomendados. Un SSD M.2 debe usar el separador de su longitud y no quedar flexionado.
8. Instala fuente y tarjetas. Usa exclusivamente sus cables compatibles. Conecta alimentación principal, CPU, GPU cuando exista, datos, panel frontal, USB y ventilación siguiendo etiquetas y manual.
9. Ordena cables para evitar aspas, tensión y obstrucción. No dobles conectores por encima de las recomendaciones. Cuenta herramientas y tornillos antes de energizar.
10. Realiza inspección cruzada y primer arranque con el mínimo hardware necesario. No conectes o retires componentes internos con tensión.

Antes de instalar un sistema operativo, entra en UEFI y verifica CPU, RAM, unidades, fecha, ventiladores y temperatura. Si la temperatura asciende rápidamente sin estabilizarse, apaga y revisa refrigeración. El primer entrenamiento de memoria puede tardar y reiniciar; consulta el manual antes de cortar alimentación repetidamente.

## 5. Verificar el equipo

Construye una línea base con versión de firmware, configuración, temperatura ambiente aproximada, carga de trabajo y duración. Los valores solo son comparables bajo condiciones semejantes.

- **Memoria:** utiliza una herramienta de arranque acreditada para pruebas de RAM y registra versión, pasadas y errores. Un solo error requiere investigación; cero errores reduce incertidumbre, pero no demuestra infalibilidad.
- **CPU y refrigeración:** aplica una carga acotada y autorizada, observa temperatura, frecuencia y errores. Detén si se alcanzan límites del fabricante o aparece inestabilidad. No hace falta forzar el máximo consumo para una aceptación ofimática.
- **Almacenamiento:** verifica modelo, interfaz, registros, espacio y lectura de un conjunto de archivos de prueba. Si hay indicios de fallo con datos valiosos, prioriza preservar datos sobre ejecutar pruebas intensivas.
- **Periféricos:** prueba puertos utilizados, audio, red, pantalla, suspensión cuando proceda e impresión. Verifica también reinicio y arranque en frío.

En Linux, `journalctl -b -p warning` ayuda a localizar avisos del arranque actual. Un aviso no siempre es una avería: correlaciónalo con el síntoma y con el dispositivo. En Windows utiliza el Visor de eventos y el Monitor de confiabilidad; un corte inesperado señala la consecuencia, no identifica por sí mismo una fuente defectuosa.

## 6. Salud de discos y SMART

Con `smartmontools` instalado, comienza por enumerar unidades y interfaces admitidas:

```bash
sudo smartctl --scan-open
```

La lectura puede despertar discos en reposo. Selecciona la ruta real por modelo y serie. En los comandos siguientes `/dev/sdX` es un marcador que hay que reemplazar; no se ejecuta literalmente:

```bash
sudo smartctl -a /dev/sdX
```

Para NVMe utiliza la ruta identificada por el escaneo, frecuentemente `/dev/nvme0`; adapta el comando a la salida real. Examina errores de medios, temperatura, registros y tendencia, no únicamente una palabra `PASSED`. Un puente USB puede ocultar datos o necesitar un tipo de dispositivo específico; consulta la ayuda del controlador antes de interpretar un fallo de lectura como fallo del disco.

Un autotest modifica el estado interno y genera carga. Después de asegurar los datos y elegir una ventana de mantenimiento, se puede iniciar un test corto con `smartctl -t short` aplicado al dispositivo verificado. El programa informa de cuándo consultar resultados; no supongas una duración fija. Lee el registro con `smartctl -l selftest` sobre la misma unidad. No ejecutes pruebas prolongadas sobre un medio con síntomas graves como paso previo obligatorio a rescatar información.

## 7. Mantenimiento preventivo y entrega

Programa inspecciones según polvo, uso y criticidad. Registra limpieza de filtros, estado de cables, ventiladores, actualizaciones justificadas, comprobación de copias y capacidad libre. No uses aspiradores o compresores que generen electricidad estática o humedad; emplea el material aprobado y evita hacer girar ventiladores por encima de sus condiciones de uso.

La entrega incluye qué cambió, por qué, piezas retiradas, pruebas realizadas, limitaciones y próxima revisión. El usuario necesita saber si sus aplicaciones funcionan y sus datos están disponibles. El inventario técnico conserva las referencias y resultados detallados; la explicación de entrega debe ser breve y comprensible.

## Fuentes de procedimiento

- [smartctl: opciones, pruebas y registros](https://manpages.debian.org/trixie/smartmontools/smartctl.8.en.html).
- [Microsoft Learn: Get-PhysicalDisk](https://learn.microsoft.com/powershell/module/storage/get-physicaldisk).
- [Microsoft Learn: Get-Disk](https://learn.microsoft.com/powershell/module/storage/get-disk).
- [Debian: lspci](https://manpages.debian.org/trixie/pciutils/lspci.8.en.html).
- [Memtest86+: documentación oficial](https://memtest.org/).
