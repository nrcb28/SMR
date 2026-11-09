# 05 · Medición del rendimiento y dimensionamiento

[Índice de la asignatura](README.md) · [Fundamentos](01-fundamentos.md)

## 1. Traducir una queja en una magnitud

«El ordenador es lento» describe una experiencia, pero no identifica el recurso que limita el trabajo. Un puesto puede tardar en arrancar porque carga muchos servicios, abrir un documento lentamente por latencia de almacenamiento y bloquearse durante una videollamada por falta de memoria. Comprar una CPU más rápida no resuelve necesariamente ninguna de esas tres causas. El primer trabajo técnico consiste en definir una acción, un estado inicial y una medida.

Un requisito de prueba útil sería: abrir un proyecto sintético de 200 MiB desde almacenamiento local, después de iniciar sesión y esperar a que terminen las actualizaciones, registrando tres ejecuciones y distinguiendo la primera de las siguientes. Hay que anotar versión de aplicación, tamaño real del conjunto, energía, otros procesos y si el disco es virtual. Los resultados son comparables sólo dentro de condiciones suficientemente parecidas.

Separa el tiempo total en fases observables. En una importación: lectura, descompresión, análisis, transformación y escritura. Si la lectura dura dos segundos y el análisis treinta, mejorar la lectura al doble sólo ahorra un segundo. Esta descomposición permite justificar un cambio con su efecto probable, en lugar de asociar cualquier retraso al componente más antiguo.

## 2. Latencia, caudal e IOPS

La **latencia** es el tiempo de completar una operación; el **caudal** es la cantidad procesada por unidad de tiempo; las **IOPS** cuentan operaciones de entrada/salida por segundo. Sin el tamaño de la operación, una cifra de IOPS no se puede transformar en MB/s. Para operaciones uniformes de 4 KiB, 25.000 IOPS representan aproximadamente 97,66 MiB/s de datos útiles: `25000 × 4096 / 1048576`.

La relación no convierte un dispositivo en «rápido para todo». Una copia de vídeo grande puede depender del caudal secuencial; iniciar miles de archivos pequeños introduce búsquedas, metadatos, permisos, caché y peticiones pequeñas. Además, la profundidad de cola y la concurrencia cambian el resultado. Un dispositivo con muchas peticiones pendientes puede entregar un caudal alto mientras cada petición individual sufre más demora.

| Trabajo | Medida especialmente útil | Dato que falta si sólo se muestra una cifra |
| --- | --- | --- |
| Abrir una aplicación | Tiempo de respuesta y distribución de latencias | Estado de caché y servicios activos |
| Copiar un archivo grande | MiB/s sostenidos y tiempo total | Origen, destino, caché y temperatura |
| Servir archivos pequeños | IOPS, tamaño de bloque y percentiles | Cola y patrón de acceso |
| Exportar vídeo | Tiempo de tarea y uso de motores | Códec, aceleración y calidad |
| Navegar con varias aplicaciones | Respuesta interactiva y presión de memoria | Cantidad de datos activos y paginación |

Utiliza mediana cuando algunas ejecuciones aisladas sufran ruido, pero conserva también los valores individuales. Si los tiempos son 8,1; 8,3 y 21,4 segundos, la mediana es 8,3 y el valor alto exige investigar, no borrarlo automáticamente. Una actualización o análisis en segundo plano puede explicar una observación; una pausa térmica recurrente puede formar parte del problema.

## 3. CPU, paralelismo y límites del cambio

La frecuencia nominal no define por sí sola el rendimiento. Influyen arquitectura, instrucciones por ciclo, memoria, caché, número de núcleos, capacidad térmica y características de la aplicación. Comparar GHz entre familias distintas es una aproximación insuficiente; comparar número de hilos sin saber si la tarea es paralelizable produce el mismo error.

Un ejercicio de límite superior aclara el efecto. Supón una tarea cuyo 60 % del tiempo puede acelerarse cuatro veces y cuyo 40 % permanece igual. El tiempo relativo esperado es `0,40 + 0,60/4 = 0,55`; la aceleración ideal es `1/0,55 ≈ 1,82`, antes de sobrecargas. No se espera multiplicar por cuatro todo el trabajo. Este razonamiento es un modelo didáctico, no un resultado medido de una CPU concreta.

Observa uso por núcleo, no sólo el promedio. En un equipo de ocho núcleos, un hilo saturado puede aparecer como un porcentaje total modesto y aun así limitar una operación secuencial. Por el contrario, una CPU con utilización alta puede estar realizando correctamente el trabajo en el tiempo requerido. Saturación no equivale automáticamente a avería; hay que relacionarla con el requisito de servicio.

En Linux, `lscpu` describe la CPU visible; en una VM puede describir una presentación virtual. `top` o `htop` muestran actividad, pero sus convenciones de porcentajes pueden representar un núcleo como 100 % o sumar varios. En Windows, Administrador de tareas permite cambiar la gráfica a procesadores lógicos. Registra la convención utilizada para no comparar porcentajes incompatibles.

## 4. Memoria, canales y carga activa

La capacidad de RAM resuelve un problema de capacidad cuando el conjunto activo no cabe cómodamente y el sistema necesita recuperar páginas o paginar de forma perjudicial. Un canal adicional puede mejorar el ancho de banda para determinadas cargas, pero no convierte automáticamente una tarea de disco en una tarea de memoria. Latencia, ancho de banda y capacidad son dimensiones diferentes.

Comprueba la población de ranuras en el manual de placa. Dos módulos en ranuras contiguas pueden no corresponder al reparto recomendado por canales. Una combinación que arranca puede funcionar con una velocidad común inferior o un perfil conservador. Los perfiles de memoria aumentados respecto a especificaciones base no se presentan como una obligación de mantenimiento; cualquier cambio debe seguir compatibilidad, estabilidad y soporte del fabricante.

En una prueba comparativa mantén constante la cantidad de aplicaciones y datos. Abrir diez documentos distintos para «llenar la RAM» no reproduce necesariamente la misma carga dos veces. Utiliza un conjunto sintético fijo, anota procesos y espera un estado estable. No desactives la paginación ni vacíes cachés del sistema por rutina: cambiarías el comportamiento que intentas medir y podrías causar fallos ajenos a la hipótesis.

## 5. Enlaces PCIe y límites de trayecto

Un dispositivo opera dentro de un trayecto: controlador, enlace, ranura, chipset, CPU, memoria y software. La forma física de una ranura no garantiza su conexión eléctrica máxima. Un conector largo puede tener menos líneas activas; una ranura M.2 puede compartir recursos con un puerto SATA. La documentación de la placa es la fuente para ese modelo exacto.

Una lectura de capacidad anunciada no confirma la negociación real. En Linux, `lspci -vv` puede mostrar capacidades y estado del enlace para dispositivos accesibles; pertenece al paquete `pciutils` y algunas partes requieren privilegios. Si no está instalado, prepara ese paquete sólo en el entorno autorizado antes de seguir el procedimiento. Si el dispositivo admite más generación o ancho del que negocia, investiga configuración, compatibilidad, reparto de líneas y estado físico antes de concluir que está averiado. En una VM esa información puede no representar el cableado físico del anfitrión.

El cálculo de caudal bruto sirve para comprobar orden de magnitud. No debe presentarse como rendimiento de aplicación: codificación, protocolo, control, patrón de acceso y otros recursos reducen el caudal útil. Compara un resultado con el límite del trayecto más estrecho; un SSD no puede trasladar al sistema más datos útiles que los que admite su enlace efectivo y la carga completa.

## 6. Temperatura, potencia y comportamiento sostenido

Una prueba de pocos segundos puede aprovechar límites de potencia y temperatura distintos de una tarea larga. Si el rendimiento cae después de varios minutos, observa temperatura, frecuencia efectiva, potencia y ventilación durante la misma ventana temporal. El objetivo es correlacionar eventos; ver una temperatura alta aislada no identifica por sí sola el motivo de la caída.

No establezcas un umbral universal de temperatura para todas las CPU y SSD. Los límites y estrategias de protección dependen del modelo. Un ventilador que gira demuestra movimiento, no necesariamente contacto correcto del disipador ni caudal adecuado. Comprueba montaje, obstrucción, orientación y curva configurada siguiendo el manual y con el equipo apagado para intervenciones físicas.

La potencia de salida nominal de una fuente no es el consumo constante del ordenador. Si una carga entrega 240 W a los componentes y la eficiencia en ese punto es 90 %, la entrada aproximada es `240/0,90 = 266,7 W`; las pérdidas son unos 26,7 W. Esa hipótesis no garantiza la eficiencia a cualquier carga ni evalúa calidad eléctrica o respuesta ante transitorios. Tampoco debes medir el interior de la fuente para demostrar el cálculo.

## 7. Diseñar una comparación honesta

Prepara una ficha con hardware, firmware, SO, versión de aplicación, configuración energética y conjunto de datos. Decide antes cuántas repeticiones y qué condición invalida una ejecución: por ejemplo, actualización que interrumpe la tarea. Conserva todas las mediciones y explica exclusiones; elegir únicamente la mejor convierte el informe en publicidad, no en una comparación.

Compara primero una variable. Para evaluar un SSD nuevo, no cambies simultáneamente RAM, antivirus, aplicación y sistema operativo. Si un cambio múltiple es inevitable, describe la mejora del conjunto sin atribuirla a una sola pieza. Incluye la incertidumbre: una diferencia de décimas dentro de una variación de varios segundos puede no justificar una compra.

El coste debe incluir compatibilidad, tiempo de intervención, migración y riesgo de parada. Una mejora del 20 % en una tarea que se ejecuta una vez al mes puede importar menos que una mejora pequeña en una tarea realizada cientos de veces al día. Cuantifica el tiempo de trabajo recuperado mediante hipótesis explícitas y separa esa capacidad del ahorro monetario efectivo.

## 8. Práctica ampliada: informe antes/después

En una VM de prácticas, elige una tarea inocua y reproducible como enumerar un árbol fijo de archivos sintéticos o comprimir una copia de ese árbol. La VM sirve para estudiar el método; no uses la cifra para certificar un SSD físico. Conserva al menos cinco ejecuciones, anota duración y actividad de fondo y cambia sólo un parámetro reversible, como la asignación de RAM dentro de los requisitos admitidos.

Antes del cambio apaga la VM si el hipervisor lo requiere, guarda su configuración y comprueba espacio y memoria del anfitrión. No sobreasignes recursos hasta afectar otras VMs. Tras el cambio ejecuta la misma tarea y registra el nuevo estado. Vuelve a la configuración original al terminar y comprueba que el laboratorio arranca correctamente.

Entrega un gráfico o tabla con valores individuales, mediana y descripción del entorno. Explica qué recurso pretendías evaluar, qué observaciones apoyan la hipótesis y qué limitaciones impiden generalizar. La aceptación exige una conclusión proporcional a la evidencia, no obtener una mejora obligatoria. Una ausencia de mejora bien explicada también es un resultado útil.

Rúbrica didáctica: diseño de prueba 25 %, control del entorno 20 %, registro y cálculo 25 %, interpretación 20 % y recuperación/documentación 10 %. No se consideran resultados propios las cifras de ejemplo de este capítulo; el estudiante debe obtenerlas en su laboratorio.

## Referencias primarias

- [Documentación PCI de Linux](https://docs.kernel.org/PCI/index.html): arquitectura y administración del subsistema.
- [lspci en Debian](https://manpages.debian.org/trixie/pciutils/lspci.8.en.html): significado y alcance de la inspección PCI.
- [Documentación de gestión térmica de Linux](https://docs.kernel.org/driver-api/thermal/index.html): relación entre sensores, políticas y dispositivos.
- [Microsoft: investigación de rendimiento](https://learn.microsoft.com/troubleshoot/windows-server/performance/troubleshoot-performance-problems-in-windows): correlación de contadores y carga.
- [GNU time](https://www.gnu.org/software/time/): medición de duración y recursos, distinguiéndola del tiempo interno de una aplicación.
