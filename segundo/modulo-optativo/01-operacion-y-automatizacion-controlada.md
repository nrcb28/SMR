# Operación y automatización controlada del soporte

[Índice de la propuesta](README.md) · [Casos y métricas](02-casos-metricas-y-evaluacion.md)

## 1. Finalidad y límites

Esta ampliación es material complementario de segundo, no la denominación ni el currículo oficial de la optativa del centro. Desarrolla una forma de operar servicios de laboratorio que conserva evidencia, limita cambios y permite un relevo. La automatización se introduce después de comprender el procedimiento manual.

La práctica utiliza máquinas virtuales autorizadas, datos sintéticos y las funciones documentadas en el [laboratorio](../../docs/laboratorio.md). El servidor de servicios conserva `.56.10`, el cliente `.56.20` y el controlador opcional `.56.11` pertenece a otro escenario. Una NIC adicional NAT no convierte la interfaz LAB en una red con gateway.

## 2. Convertir una tarea en procedimiento

Una tarea operativa necesita objetivo, alcance, precondiciones, pasos, condiciones de parada y validación. “Limpiar disco” es demasiado ambiguo: puede significar retirar temporales autorizados, aplicar retención o destruir datos. Antes de automatizar se identifica qué objetos pueden modificarse y quién decide.

Ejemplo: comprobar que un servicio dispone de copia recuperable. Se revisan ejecución, destino, punto recuperable y ensayo de restauración. Un directorio existente no demuestra que el almacenamiento esperado esté montado; un código de salida cero no demuestra por sí solo integridad de datos ni permisos. Esas diferencias deben figurar en el procedimiento.

Un runbook separa consultas y cambios. Consultar ocupación con `df` no equivale a borrar archivos; consultar unidades con fallo no autoriza reiniciar todos los servicios. Cada decisión se apoya en un resultado y un alcance conocido. La [plantilla de procedimiento](../../recursos/plantillas/procedimiento-operacion.md) ayuda a documentarlo.

## 3. Preparar una automatización de lectura

El primer ejercicio automatizado sólo recopila datos seleccionados. Su salida identifica instante y zona, equipo sintético, versión de la comprobación y estado observado. Recoger toda la configuración por comodidad puede revelar información innecesaria; define antes las preguntas que quieres responder.

En Linux puede registrarse información pública del sistema y recursos; en Windows, propiedades concretas mediante CIM o cmdlets. La herramienta no instala paquetes, no eleva permisos automáticamente y comunica si una consulta no está disponible. Un campo ausente no se sustituye por cero: se registra como desconocido o fallo de consulta según el esquema.

El resultado debe conservar tipos y unidades. Un porcentaje de ocupación, bytes libres y capacidad total son magnitudes relacionadas pero distintas. Para comparar ejecuciones, usa el mismo sistema de archivos y explica cambios de capacidad. Una lectura aislada no permite concluir una tendencia.

## 4. Diseñar acciones con revisión previa

Cuando una tarea requiera cambios, prepara primero un plan que enumere objetos y acciones sin ejecutarlos. El modo de simulación debe ser real: imprimir “simulación” y después escribir o borrar sigue siendo una mutación. Verifica el flujo con una copia o datos desechables antes de introducir ejecución.

Un plan de altas, por ejemplo, contiene identificador, grupo, motivo y validación; no lleva contraseñas en claro. La fase de aplicación comprueba de nuevo condiciones, porque el estado puede cambiar entre plan y ejecución. Si una cuenta existe con otro propósito, se detiene o deriva el conflicto en lugar de modificarla silenciosamente.

Define también comportamiento ante fallo parcial. Si una operación de cinco pasos falla en el tercero, el procedimiento debe identificar qué pasos se realizaron y qué recuperación corresponde. No repitas todo a ciegas si eso crea duplicados o deshace trabajo válido. La idempotencia se diseña para una operación y sus efectos; no aparece por añadir un bucle de reintentos.

## 5. Pruebas y registros útiles

Prueba entradas válidas, vacías, duplicadas y fuera de rango; destinos inexistentes; permiso insuficiente y dependencia ausente. Los casos negativos se realizan con objetos de laboratorio, sin provocar indisponibilidad en servicios de trabajo. Una denegación esperada es un resultado correcto del control que estás evaluando.

El log registra identificador de operación, paso, resultado e información mínima para investigar. No registra secretos ni volcados completos de datos personales. Diferencia fallo de la consulta, estado no conforme y estado desconocido. La ausencia de mensajes no demuestra éxito si el programa pudo terminar antes de escribirlos.

Conserva código de salida y salida legible. Una tarea programada necesita un responsable que revise fallos y una política de conservación. En el aula puede bastar con una bitácora manual; desplegar una plataforma de monitorización compleja no reemplaza entender qué significa cada señal.

## 6. Aceptación desde la persona usuaria

La prueba final se realiza desde el contexto adecuado. Un administrador puede leer donde una cuenta ordinaria no puede; una consulta local no demuestra que el cliente remoto alcance el servicio. Identifica identidad, ruta, operación y resultado para que la evidencia sea interpretable.

Incluye persistencia cuando corresponda. Un cambio temporal de interfaz puede permitir una prueba y desaparecer al reiniciar; documenta el gestor que conserva el estado. No reinicies un sistema de producción sólo para completar una rúbrica escolar: se ensaya en la VM y se adapta al procedimiento autorizado en empresa.

## 7. Fuentes y mantenimiento

Consulta [Debian Reference](https://www.debian.org/doc/manuals/debian-reference/), [PowerShell](https://learn.microsoft.com/powershell/), [Python](https://docs.python.org/3/) y documentación primaria del servicio. Registra versión y dependencias utilizadas. El ejemplo de una distribución no garantiza las mismas rutas o utilidades en otra.

Después de un cambio de versión, ejecuta de nuevo las comprobaciones pertinentes y actualiza procedimiento y expectativas. La salida que se obtuvo meses atrás no se convierte en evidencia actual por conservarse en el repositorio. El objetivo es mantener una operación entendible y recuperable, con límites explícitos.
