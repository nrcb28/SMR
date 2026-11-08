# 01 · Arquitectura y fundamentos del hardware

[Volver al módulo](README.md) · [Continuar con la guía técnica](02-guia-tecnica.md)

## 1. Del problema de uso a la arquitectura

Un equipo procesa datos mediante CPU, memoria y dispositivos de entrada y salida. El sistema operativo coordina estos recursos y los controladores permiten utilizar dispositivos concretos. Un fallo visible en una aplicación puede proceder de cualquiera de estas capas: una compilación lenta puede deberse a CPU, memoria insuficiente, almacenamiento saturado, antivirus o refrigeración deficiente. Por ello se diagnostica el recurso que limita el trabajo antes de recomendar una ampliación.

La arquitectura x86-64 describe un conjunto de instrucciones y un modelo de ejecución; no identifica una generación ni garantiza la compatibilidad entre todas las CPU. AMD e Intel pueden ejecutar gran parte del mismo software y utilizar zócalos, chipsets y plataformas incompatibles. También existen equipos ARM64: una imagen o controlador x86-64 no se instala automáticamente en ellos.

En un sistema moderno la CPU integra controladores de memoria y parte de las líneas PCI Express. El chipset ofrece conectividad adicional. Esto explica por qué dos ranuras con el mismo aspecto pueden tener diferente rendimiento y compartir recursos. La decisión de instalar otro SSD puede deshabilitar un puerto SATA o reducir las líneas disponibles de una ranura; el manual de la placa es la fuente de referencia.

## 2. CPU: rendimiento, compatibilidad y temperatura

Un núcleo ejecuta instrucciones; un hilo lógico es un contexto que el sistema operativo puede planificar. El multihilo simultáneo comparte recursos del núcleo y no duplica su rendimiento. La frecuencia indica ciclos por segundo, pero el trabajo completado también depende de instrucciones por ciclo, caché, memoria, límites de energía y paralelismo del programa. No compares procesadores solo por GHz.

La jerarquía de caché reduce accesos a RAM. La caché L1 suele ser pequeña y cercana al núcleo; L2 y L3 aumentan capacidad a costa de latencia. Si el conjunto de trabajo no cabe en caché, el sistema depende más del ancho de banda y latencia de memoria. El aumento de núcleos apenas ayuda a una operación estrictamente secuencial; puede ayudar mucho a compresión o renderizado paralelos.

Antes de elegir CPU verifica:

1. Zócalo y lista de CPU admitidas por la placa.
2. Versión de firmware mínima necesaria. Una placa puede necesitar actualización antes de reconocer una CPU nueva.
3. Capacidad de alimentación de la placa y límites térmicos del disipador.
4. Gráficos integrados y conectores de vídeo disponibles. Un conector HDMI en la placa no implica que cualquier CPU produzca vídeo.
5. Requisitos de virtualización, cifrado y sistema operativo previstos.

TDP y denominaciones equivalentes no son una medición universal del consumo máximo ni de la potencia en el enchufe. Los límites y algoritmos de turbo varían según fabricante y modelo. La refrigeración debe elegirse con documentación específica y espacio físico disponible, no mediante una cifra aislada.

El *thermal throttling* reduce frecuencia o potencia para contener temperatura. Si un trabajo empieza rápido y se ralentiza tras unos minutos, compara frecuencia, temperatura y carga antes de comprar otra CPU. El montaje del disipador, el polvo, la curva de ventilación y la temperatura ambiente son variables causales.

## 3. Memoria RAM

La RAM conserva instrucciones y datos en uso, pierde contenido sin alimentación y se gestiona mediante direcciones. La memoria virtual del sistema operativo proporciona aislamiento y un espacio de direcciones para cada proceso; cuando necesita mover páginas al almacenamiento, la latencia aumenta varios órdenes de magnitud. Ampliar RAM puede eliminar ese cuello de botella, pero añadir memoria que nunca se usa no acelera necesariamente una tarea.

DDR4 y DDR5 tienen requisitos eléctricos y disposición de contactos diferentes. No son intercambiables aunque ambos módulos sean DIMM. Los portátiles suelen utilizar SO-DIMM o memoria soldada; en esta última una ampliación puede ser imposible. Los canales permiten transferencias en paralelo: poblar correctamente las ranuras puede aumentar el ancho de banda, pero la posición recomendada depende de la placa.

La tasa se expresa normalmente en MT/s. Un módulo DDR no debe compararse confundiendo la frecuencia del reloj con la tasa efectiva de transferencia. La latencia CAS expresa ciclos; para compararla en tiempo hay que relacionarla con el reloj, además de considerar el resto de temporizaciones. En una aproximación útil, latencia CAS en ns ≈ `2000 × CL / tasa en MT/s`. Por ejemplo, CL16 a 3200 MT/s equivale aproximadamente a 10 ns; no representa toda la latencia de acceso del sistema.

XMP y EXPO son perfiles de configuración. Su uso puede implicar frecuencias fuera de la especificación base del controlador de memoria; no debe asumirse estabilidad. Empieza con valores admitidos por la plataforma y activa perfiles únicamente con autorización y validación. Un arranque correcto no sustituye varias pasadas de una prueba de memoria.

ECC añade mecanismos de detección o corrección de errores, pero requiere compatibilidad de CPU, placa, firmware y módulos. El ECC interno de los chips DDR5 no equivale por sí solo a protección ECC de extremo a extremo visible para el sistema. Tampoco convierte al equipo en inmune a fallos de software, almacenamiento o alimentación.

## 4. Buses y expansión

PCI Express es una interconexión serie punto a punto organizada en líneas. `x1`, `x4`, `x8` o `x16` describen número de líneas; el conector físico y el enlace negociado pueden diferir. Una tarjeta en ranura física x16 puede trabajar con cuatro líneas. La generación modifica la velocidad por línea y existen pérdidas de codificación y protocolo: el caudal útil es inferior al máximo teórico.

USB utiliza conectores y protocolos que no se deducen solo por la forma. USB-C describe principalmente un conector; no garantiza una velocidad concreta, salida de vídeo ni carga de determinada potencia. Hay que comprobar puerto, cable y dispositivo. Un cable adecuado para carga puede limitar datos, y una base con alimentación insuficiente puede producir desconexiones intermitentes.

En una tarjeta de red distingue interfaz interna, velocidad negociada y rendimiento de aplicación. Un enlace de 1 Gbit/s ofrece como máximo 125 MB/s antes de cabeceras y otras pérdidas; copiar a 90 MB/s no demuestra que el cable esté averiado. El disco, el protocolo, el tamaño de archivos y la CPU también limitan.

## 5. Almacenamiento: forma, protocolo y estructura lógica

| Concepto | Qué describe | Confusión frecuente |
| --- | --- | --- |
| HDD o SSD | Tecnología de almacenamiento | Un SSD no tiene por qué usar NVMe |
| 2,5 pulgadas o M.2 | Formato físico | M.2 no implica NVMe |
| SATA o PCIe | Enlace empleado | Un puerto M.2 puede admitir uno, otro o ambos |
| AHCI o NVMe | Interfaz/protocolo de acceso en los casos habituales | La forma no identifica el protocolo |
| GPT o MBR | Organización de particiones | No son sistemas de archivos |
| ext4, NTFS, FAT32 | Sistemas de archivos | Formatear una partición no equivale a borrar físicamente todas sus celdas |

Un HDD tiene componentes mecánicos y sufre especialmente accesos aleatorios. Un SSD usa memoria flash y un controlador que distribuye escrituras, corrige errores y administra espacio reservado. TRIM permite al sistema comunicar bloques lógicos que ya no necesita. No es una herramienta de recuperación y puede reducir la posibilidad de rescatar archivos eliminados.

TBW expresa un volumen de escrituras asociado a la especificación de resistencia, no una fecha exacta de muerte. La salud depende de temperatura, firmware, errores, desgaste y condiciones de uso. SMART y los registros NVMe ofrecen indicadores útiles, pero un estado global correcto no garantiza que no vaya a fallar. Tampoco todos los atributos SATA tienen interpretación idéntica entre fabricantes.

Un RAID proporciona determinadas propiedades de disponibilidad o rendimiento; no sustituye una copia independiente. El borrado accidental, el cifrado malicioso o un fallo del controlador pueden afectar a todos los miembros. Mantén copias con versiones y comprueba restauraciones.

## 6. Firmware y arranque

UEFI inicializa hardware y ejecuta un gestor o cargador de arranque. GPT describe particiones y mantiene estructuras redundantes y verificaciones de integridad. En instalaciones UEFI habituales hay una partición del sistema EFI con formato FAT y ficheros de arranque; el sistema operativo suele residir en otras particiones. Secure Boot verifica componentes de la cadena de arranque mediante claves y firmas; no cifra los datos del disco.

Un TPM protege y utiliza claves dentro de un modelo de confianza. BitLocker puede vincular el desbloqueo automático a mediciones de la plataforma; cambiar firmware o configuración puede solicitar una clave de recuperación. Antes de modificar esos ajustes, el responsable debe comprobar que la recuperación está disponible por el canal aprobado. No guardes claves en el repositorio ni las fotografíes.

El orden de arranque no cambia el contenido del disco, pero modificar modos SATA/RAID, borrar claves o restablecer firmware puede impedir arrancar. Documenta estado anterior y consulta el manual. Actualizar firmware exige imagen exacta, alimentación estable y motivo concreto; no interrumpas el proceso.

## 7. Alimentación y refrigeración

La potencia eléctrica sigue `P = V × I`. Una carga de 60 W a 12 V necesita idealmente 5 A. La fuente debe atender cargas combinadas, picos transitorios, conectores y márgenes del fabricante. La certificación de eficiencia no equivale a una garantía general de calidad o protecciones.

No intercambies cables modulares entre fuentes por su apariencia. El pinout en el lado de la fuente puede variar y causar daños. Los conectores de CPU y GPU tampoco se sustituyen por semejanza. Se revisan cierre, inserción completa, radios de curvatura y recomendaciones específicas del fabricante.

La presión y dirección del flujo de aire dependen del conjunto caja, filtros, ventiladores, disipadores y obstáculos. Introducir más ventiladores no corrige siempre una mala disposición. La pasta térmica mejora el contacto microscópico entre superficies; no sustituye una fijación correcta y un exceso puede ensuciar contactos.

## 8. Periféricos, impresión y residuos

En impresión separa aplicación, cola, controlador, conexión y mecanismo físico. Si la página de prueba interna falla, el problema no depende de Windows ni de la red. Si la prueba interna funciona pero no la del sistema operativo, comprueba controlador, cola, puerto y conectividad.

En láser hay carga electrostática, revelado, transferencia y fijación; el fusor alcanza temperaturas elevadas. En inyección el estado de inyectores y consumibles condiciona la calidad. No limpies ni manipules mecanismos energizados. Sigue el procedimiento del fabricante y utiliza consumibles compatibles.

Los residuos de equipos, baterías y cartuchos se separan según su naturaleza y el procedimiento del centro. Antes de reutilizar un almacenamiento, hay que aplicar el método de saneamiento aprobado y verificarlo. Una eliminación lógica de archivos o un formateo rápido no demuestra saneamiento.

## Referencias técnicas

- [UEFI Forum: especificaciones de firmware](https://uefi.org/specifications).
- [NVM Express: especificaciones](https://nvmexpress.org/specifications/).
- [Microsoft Learn: relación entre modo de arranque y GPT](https://learn.microsoft.com/windows-hardware/manufacture/desktop/windows-setup-installing-using-the-mbr-or-gpt-partition-style).
- [Kernel Linux: documentación de fiabilidad, disponibilidad y servicio](https://docs.kernel.org/admin-guide/ras.html).
- [USB-IF: documentación técnica](https://www.usb.org/documents).
