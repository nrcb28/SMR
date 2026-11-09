# Retos prácticos por resultado de aprendizaje · 0221

[Mapa completo de RA y criterios](09-alineacion-ra.md) · [Índice](README.md) · [Datos de trazabilidad](alineacion-ra.json)

## Preparación del taller y del dossier

Cada reto produce evidencia vinculada a letras concretas del [mapa curricular](09-alineacion-ra.md). Los nombres A1/A2 son identificadores didácticos del repositorio. No sustituyen los instrumentos o calificaciones del centro. Para cada actuación registra equipo, versión o ficha, persona que ejecuta/supervisa, estado inicial, acción, resultado y recuperación. Separa los datos observados de los números sintéticos que se ofrecen para calcular.

Antes de una práctica física se necesita autorización, banco preparado, manual del modelo y supervisión apropiada. Una VM permite preparar inventario, imagen o arranque; no demuestra inserción de RAM, calidad de una conexión, temperatura física, reparación mecánica ni uso de instrumentación. Si falta equipo, se entrega el plan y se marca la parte de ejecución pendiente. Esto hace visible la carencia y permite recuperarla posteriormente con una sesión real.

El dossier puede organizarse como ocho carpetas RA1–RA8 con índice de criterios, documentos saneados y matriz de pruebas. No publiques imágenes de discos, claves, datos personales o números de serie innecesarios. Usa la [memoria de práctica](../../recursos/plantillas/memoria-practica.md) y registra las limitaciones observadas, incluso si el conjunto funciona.

<a id="ra1"></a>
## RA1 · 0221-RA1-A1: configurar para una necesidad

### Encargo y procedimiento

Prepara tres propuestas: puesto de ofimática con una VM ligera, estación de captura de vídeo y equipo compacto para presentar contenidos. Para cada una identifica aplicación, resolución de pantalla, periféricos, posibilidad de ampliación y periodo de soporte. Selecciona dos plataformas documentadas y compara CPU, buses, memoria, placa, caja, refrigeración, almacenamiento, vídeo, red y accesorios.

1. Dibuja los bloques funcionales y un trayecto de datos, por ejemplo cámara–interfaz–memoria–almacenamiento. Explica dónde puede aparecer un límite.
2. Crea una matriz de compatibilidad con evidencia por pareja: CPU/placa/firmware, RAM/controlador, unidad/protocolo/conector, tarjeta/ranura, caja/formato y fuente/conectores.
3. Registra qué componentes ya incluye una plataforma semiensamblada y qué cables, tornillos, controlador o adaptador necesita. Una fotografía comercial no garantiza la lista de accesorios.
4. Identifica físicamente piezas reales autorizadas y practica su manipulación sin energía según el manual. Esta observación se registra aparte de la comparación documental.
5. Justifica una selección por uso; una puntuación total no puede compensar un requisito obligatorio incumplido.

### Cálculo y solución razonada

Datos **sintéticos**: CPU 65 W, placa 35 W, RAM 8 W, almacenamiento 6 W, ventilación 6 W y periféricos alimentados 15 W suman 135 W de carga estimada. Añadir una GPU de 140 W eleva el modelo a 275 W. Un margen didáctico del 20 % sobre esa carga da 330 W, antes de considerar restricciones del fabricante, transitorios y conectores. No se elige una fuente sólo por superar esa cifra: importa qué raíles y conectores sostienen la configuración y bajo qué condiciones térmicas.

La eficiencia relaciona entrada y salida, no amplía la potencia de salida nominal. Tampoco todos los consumos máximos se comportan igual en una carga real. Presenta el cálculo como hipótesis de dimensionamiento y contrástalo con fichas y medición cuando sea posible.

### Evidencia y aceptación

Entrega las tres fichas de uso, dos alternativas por ficha, diagrama, matriz, lista de accesorios y registro físico. La prueba negativa puede ser una CPU sin gráficos integrados conectada a la salida de placa como **supuesto documental**, sin montar una combinación incompatible: explica por qué esa salida puede no producir imagen. La solución correcta identifica la dependencia del modelo; no declara universal que todas las salidas de placa funcionen.

<a id="ra2"></a>
## RA2 · 0221-RA2-A1: montaje con puntos de control

### Preparación y ejecución

Realiza dos montajes autorizados que permitan observar diferencias de fijación o formato. Pueden ser equipos de entrenamiento reutilizables; no es necesario adquirir componentes. Conserva la ficha exacta de cada conjunto y acuerda qué elementos puede manipular el alumnado. No se abren fuentes de alimentación ni se trabaja con componentes internos energizados.

Prepara una hoja de proceso con herramientas y útiles, recuento, protección ESD y orden de trabajo. Identifica apertura del chasis, separadores de placa, fijaciones de unidades, posiciones de RAM y trayecto de cables. Antes de poner una placa comprueba que no existe un separador en una posición sin agujero: una pieza oculta puede causar un fallo que no se ve después de atornillar.

Monta CPU y refrigeración mediante el procedimiento del fabricante. Documenta orientación, fijación y conexión de ventilación, sin dar una cantidad universal de pasta o una secuencia de apriete válida para todos los zócalos. Instala RAM y unidades en posiciones compatibles y conecta sólo cables propios de la fuente utilizada; los cables modulares no son intercambiables por parecer iguales.

Antes de energizar, otra persona revisa conexiones, tornillos, herramientas, ventiladores libres y cierres. Registra parámetros básicos del firmware sin cambiar perfiles de rendimiento o modos de disco a ciegas. El primer arranque se sigue de comprobaciones de memoria, almacenamiento, puertos, refrigeración y reinicio, según las [guías de montaje y diagnóstico](02-guia-tecnica.md).

### Solución, errores y recuperación

Si falta imagen, separa pantalla/cable/entrada de POST e inicialización; no reinstales el SO antes de saber que se está llegando a él. Si un módulo no se detecta, apaga y sigue el procedimiento antes de recolocarlo; conserva una hipótesis por cambio. No aprietes o fuerces un conector que el manual no identifica como compatible.

La aceptación exige registro real de los dos conjuntos y pruebas ajustadas al uso. Una única fotografía del equipo terminado no muestra todos los criterios de ensamblado. Si sólo se ha montado un conjunto, se conserva como evidencia parcial y se planifica la segunda observación.

**Entregables:** hoja de herramientas, referencias técnicas, secuencia, puntos de inspección, inventario final e informe de montaje con incidencias. La recuperación incluye retirar el cambio defectuoso mediante desconexión y supervisión y repetir la comprobación afectada. No se desmonta una pieza peligrosa para completar el ejercicio.

<a id="ra3"></a>
## RA3 · instrumentación y alimentación: A1 y A2

### 0221-RA3-A1: diseñar una medida válida

Este reto separa preparar una medida de realizarla. Identifica primero señal, magnitud, unidad, instrumento, función, entrada, rango, incertidumbre relevante y referencia del fabricante. El manual del instrumento y el procedimiento del centro determinan su uso; no se ofrece aquí una receta de contacto con red eléctrica, interior de fuente o batería de SAI.

Construye el esquema funcional de una fuente de PC y un SAI sin abrirlos. Distingue rectificación/conversión, regulación, protecciones y salidas, según la topología concreta. Un SAI puede incorporar bypass u otras funciones; no dibujes como presentes bloques que el modelo no tiene. Registra raíles de una fuente típica mediante su etiqueta y documentación, incluyendo qué salidas son opcionales o históricas según diseño.

**Cálculo sintético:** en una ficha de entrenamiento se establece nominal de 12,00 V y tolerancia de ±5 %. El intervalo de esa ficha es 11,40–12,60 V. Una lectura ficticia de 12,08 V supone una desviación de `0,08 / 12 × 100 ≈ 0,667 %`. Estar dentro de ese intervalo bajo una condición no demuestra estabilidad de rizado, respuesta a transitorios o funcionamiento a toda carga. La tolerancia del ejemplo no se atribuye a cualquier fuente existente.

Para el SAI, diferencia W y VA. Una carga sintética de 250 W con factor de potencia 0,80 representa 312,5 VA; la autonomía no se calcula simplemente dividiendo VA nominales entre W. Depende de energía de batería, carga, eficiencia y condiciones publicadas. Usa la curva o herramienta del fabricante para el modelo y conserva la hipótesis.

### 0221-RA3-A2: ejecutar sólo en banco preparado

Los CE 3.f y 3.h necesitan registro **real de medición supervisada**. El docente debe preparar un banco protegido, comprobador apropiado, conectores y puntos accesibles autorizados, con el procedimiento del equipo y del centro. No se enseñan puentes improvisados de encendido, sondas sobre el primario, desmontaje de SAI ni ensayo sobre baterías expuestas. Tampoco se convierte una tarea de resistencia o continuidad en una medida sobre un circuito energizado.

El alumnado identifica el punto aprobado, confirma instrumento/función/rango con la supervisión y registra señal, referencia, valor, unidad, condición y conclusión. Una lectura de telemetría por software puede complementar, pero no acredita por sí sola haber utilizado el instrumento exigido por la actividad.

**Aceptación y recuperación:** si no hay banco, formación o supervisión, A2 queda pendiente; la tabla sintética sólo demuestra cálculo e interpretación. Ante una condición no prevista se detiene la actividad y se aplica el procedimiento del centro. La evidencia permite distinguir una medida mal planteada de una lectura fuera de referencia sin forzar un diagnóstico de avería.

<a id="ra4"></a>
## RA4 · 0221-RA4-A1: reparación o ampliación con contraste

### Caso y secuencia

El docente prepara una incidencia reversible o proporciona un equipo autorizado con un fallo ya existente. Elige un caso de aviso POST, rendimiento térmico, almacenamiento no detectado o ampliación. No se provoca sobretemperatura, cortocircuito, rotura ni pérdida de datos. Registra síntoma, último estado conocido y condiciones antes de abrir la caja.

Interpreta los avisos con el manual exacto. Dos hipótesis compatibles con un síntoma deben separarse mediante una prueba: por ejemplo, seleccionar la entrada correcta del monitor y usar un cable conocido distingue parte del trayecto de imagen de la inicialización del equipo. Un LED encendido o ventilador girando no confirma el funcionamiento completo de la CPU.

Si procede sustituir una pieza, verifica antes compatibilidad física, eléctrica, firmware y soporte. Anota modelo de origen y repuesto, conserva recuperación y actualiza inventario. Para una ampliación, mide una operación relevante antes y después en condiciones comparables: aumentar RAM puede aportar capacidad sin acelerar una tarea que no sufría presión de memoria.

El caso térmico se estudia mediante observación y mantenimiento autorizado. Compara temperatura, carga y comportamiento sostenido; una cifra aislada de temperatura sin condiciones no permite decidir. La corrección puede requerir montaje adecuado o limpieza permitida por el fabricante, no un cambio arbitrario de tensiones o límites de protección.

### Solución y entrega

Presenta un árbol de hipótesis con qué predice cada una y qué observaste. Si al recolocar un componente vuelve el servicio, explica la evidencia sin asegurar que el chip estaba averiado. Si la causa sigue abierta, identifica la medida de contención y la prueba pendiente.

El parte incluye daño o condición observada, decisión, repuesto, pruebas y recomendación para usuario. Se acepta cuando el comportamiento objetivo vuelve y la prueba no introduce pérdida, incompatibilidad o riesgo nuevo. No se da por resuelto sólo porque el equipo arranque una vez.

**Recuperación:** conserva la pieza anterior cuando sea segura, registra cómo retirar la ampliación y no devuelve a uso una pieza dañada para demostrar una reversión. El centro decide la retirada y tratamiento de componentes inseguros.

<a id="ra5"></a>
## RA5 · 0221-RA5-A1: una imagen que se puede restaurar

### Entorno y decisiones

Usa una VM de referencia sin datos personales y un destino virtual **nuevo y desechable**. Añade almacenamiento separado para la imagen, con capacidad e identidad registradas. Un directorio con nombre `backup` no demuestra que esté en otro medio: comprueba el almacenamiento que lo contiene. La captura y restauración requieren herramientas y medios oficiales compatibles con arquitectura, firmware y sistemas de archivos.

Compara instalación estándar y preinstalación: selección de paquetes, configuración base, personalización por equipo e identidades. En Windows se estudia la generalización con Sysprep cuando corresponda a su escenario y licencia; no se distribuye una imagen de software que no permita esa distribución. En Linux se revisan las identidades que deben ser únicas según su procedimiento de clonación. Los clones permanecen sin NIC activa hasta resolver nombre, dirección y claves que no deben duplicarse.

### Captura y ensayo guiado

1. Prepara un manifiesto con versión, datos sintéticos, firmware y tamaño de disco; comprueba apagado consistente o mecanismo de captura admitido.
2. Arranca un medio aprobado, como Clonezilla Live, después de verificar su procedencia. Registra las dos secuencias de arranque ensayadas sin modificar modos de disco no relacionados.
3. Selecciona en la herramienta captura a imagen y distingue inequívocamente disco origen y destino de almacenamiento. El procedimiento real se consulta en la versión utilizada; no se proporciona una orden genérica de copia de discos.
4. Comprueba la imagen con el mecanismo de la herramienta, registra ubicación y manifiesto y conserva el origen.
5. Restaura **sólo** en la VM destino identificada, con tamaño compatible y sin datos previos. Revisa la selección antes de confirmar cualquier sobrescritura.
6. Prueba arranque, archivos de referencia, aplicaciones, recuperación e identidad antes de conectar el clon a LAB.

### Solución y aceptación

Una imagen verificable que no arranca en el destino obliga a revisar firmware, particiones, controladores y procedimiento; no demuestra necesariamente corrupción. Una instantánea del origen no es la imagen independiente requerida por este reto. Un hash de archivo ayuda a comparar integridad, pero no valida todas las propiedades de una restauración.

Entrega acta de captura y restauración, identidades de discos, configuración de arranque, restricciones de licencia y resultados. Si sólo has creado la imagen, 5.e queda pendiente hasta restaurar. La vuelta atrás consiste en preservar el origen y descartar el destino de prueba conforme al procedimiento; no sobrescribir de nuevo el origen para «comprobar» la imagen.

<a id="ra6"></a>
## RA6 · 0221-RA6-A1: tendencias con requisitos y límites

### Comparación trabajada

Selecciona documentación primaria de dos plataformas semiensambladas, una alternativa compacta y un sistema móvil actuales en la fecha de estudio. Registra qué información es de catálogo, qué has comprobado y qué no está disponible. Incluye la evolución de PDA y navegadores del texto normativo hacia dispositivos móviles y usos de 2026, sin cambiar la numeración del RA.

Diseña un HTPC para una sala ficticia. Define resolución, frecuencia, códecs, audio, conectividad, mando o accesibilidad, ruido, consumo y mantenimiento. Después verifica la cadena aplicación–decodificador–salida–cable–pantalla. Una CPU potente no asegura que una combinación de puerto y pantalla admita un modo de imagen o audio concreto.

Contrasta ese diseño con un quiosco y un puesto de captura. Un quiosco puede priorizar montaje y arranque recuperable; captura puede exigir caudal sostenido, sincronización y puertos; un equipo móvil debe considerar batería, reparación, actualizaciones y gestión de datos. Escribe qué requisito cambia cada decisión, sin elaborar una clasificación universal de «mejor equipo».

### Diseño y revisión

Propón una personalización reversible: organización externa, iluminación prevista por el fabricante o elementos estéticos que no afecten ventilación y acceso. Evalúa mantenimiento, consumo, garantía y seguridad. No se mecaniza una caja ni se modifica alimentación para completar el análisis si esa operación no forma parte de una práctica autorizada y equipada.

**Solución:** una plataforma compacta puede ahorrar volumen y reducir posibilidades de ampliación o reparación. Esa consecuencia no la descarta automáticamente: se compara con el objetivo. Una carcasa llamativa que tapa ventilación incumple un requisito técnico aunque satisfaga una preferencia estética.

Entrega fichas con fuente/fecha, mapa de componentes incluidos y no incluidos, tres perfiles de uso y decisión argumentada. La prueba negativa consiste en encontrar una combinación que incumpla un requisito documentado y explicar cómo detectarlo antes de comprar. Una descripción de producto no se presenta como ensayo realizado.

<a id="ra7"></a>
## RA7 · 0221-RA7-A1: periféricos de oficina y producción

### Taller y selección

Divide el reto en intervención mecánica autorizada, captura multimedia y flujo profesional. En la primera parte utiliza una impresora de entrenamiento con procedimiento del modelo para papel o consumibles y un periférico de entrada con fallo reversible. No se interviene el fusor caliente, láser, alimentador energizado ni mecanismo fuera del alcance autorizado. La supervisión determina desconexión, enfriamiento y herramientas.

Separa página de prueba interna, cola del SO, controlador, conexión y salida. Si falla la prueba interna del dispositivo, reinstalar controladores no corrige ese mecanismo. Si funciona, comprueba formato/papel y trayecto del trabajo. Tras sustituir un consumible realiza una muestra sintética y compara calidad conforme al modelo; una cola vacía no demuestra papel correcto.

Para captura, compara escáner y cámara: resolución óptica o de salida, frecuencia, profundidad/formato, interfaz, latencia y permisos de aplicación. Documenta para qué uso sirve cada uno. Una cámara que funciona en una aplicación puede estar bloqueada por permisos en otra; una resolución anunciada no garantiza cualquier frecuencia en toda conexión.

### Impresión profesional y mantenimiento

Elabora un flujo desde documento original a preimpresión y salida: gestión de color, pruebas, soporte, acabado y control. Compara una multifunción de oficina, impresión digital de producción y filmadora en su ámbito histórico/profesional. El término filmado de la norma no se interpreta como grabar un vídeo del ejercicio. Si no dispones de equipos de producción, la comparación es documental y no se atribuye una operación realizada.

Diseña un calendario por desencadenantes además de fechas: número de páginas, alertas, degradación de muestra y recomendaciones del fabricante. Incluye consumibles, limpieza permitida, revisión de conexiones y canal de residuos.

**Entregables y aceptación:** parte mecánico y consumible con prueba real, ficha de entrada, comparativa de captura y flujo profesional. Registra qué se realizó físicamente y qué se estudió en documentación. La recuperación incluye retirar un trabajo sintético atascado por el método autorizado y restablecer configuración; no vaciar todas las colas del centro.

<a id="ra8"></a>
## RA8 · 0221-RA8-A1: una intervención preventiva y ambiental completa

### Orden de trabajo

Planifica una intervención que incluya traslado, apertura, sustitución de una pieza, verificación y cierre. Para cada fase identifica peligro, exposición, daño, control colectivo/organizativo, protección personal cuando corresponda y condición de parada. La valoración es didáctica y debe ajustarse a la evaluación y procedimientos del centro.

Comprueba orden del puesto, rutas libres, herramientas, protecciones, iluminación y gestión de cables antes de comenzar. Distingue protección ESD de protección frente a choque eléctrico: una pulsera no autoriza trabajar energizado ni sustituye aislamiento. Para cargas, organiza peso, recorrido y ayudas; no conviertas una recomendación genérica en una técnica universal para cualquier persona o equipo.

Analiza tres casi incidentes sintéticos: separador sobrante, cable de paso y batería deformada. Reconstruye causa y controles que habrían interrumpido la cadena. Ante batería dañada se detiene la manipulación y se aplica el procedimiento del centro; no se perfora, aplasta ni ensaya para obtener una fotografía.

### Residuos y cierre

Clasifica por separado componentes electrónicos, baterías, consumibles y envases según el canal aplicable. Documenta quién custodia y entrega; no afirmes que se ha tratado o reciclado un residuo sólo porque se depositó en una caja. El borrado o destrucción segura de datos y la gestión física del residuo son responsabilidades relacionadas, pero distintas.

Realiza una revisión cruzada antes y después de la intervención. La persona observadora anota actuaciones reales y desviaciones, sin reemplazarlas por una checklist completada de memoria. Si trabajas a solas puedes preparar y autoevaluar el plan, pero no atribuyas una supervisión que no existió.

**Aceptación:** los controles se relacionan con riesgos concretos, la actuación se detiene ante condiciones previstas y el puesto vuelve a un estado ordenado. El cierre incluye inventario, residuos, herramientas, protecciones y comunicación. Recuperar una evidencia pendiente exige repetir la fase correspondiente en condiciones autorizadas, no modificar retrospectivamente la bitácora.

## Fuentes técnicas para los nuevos retos

- [Clonezilla Live: documentación](https://clonezilla.org/clonezilla-live-doc.php): captura y restauración según versión y modo.
- [Microsoft Learn: Sysprep overview](https://learn.microsoft.com/windows-hardware/manufacture/desktop/sysprep--system-preparation--overview): generalización y límites del escenario Windows.
- [UEFI Forum: especificaciones](https://uefi.org/specifications): firmware y medios de arranque.
- [INSST](https://www.insst.es/): criterios preventivos y documentación técnica; junto a manuales concretos de instrumento, fuente, SAI y periférico.
- [OpenPrinting CUPS](https://openprinting.github.io/cups/) y [Microsoft PrintManagement](https://learn.microsoft.com/powershell/module/printmanagement/): cola y administración, sin sustituir la observación mecánica.

Las instrucciones del fabricante y del centro se consultan antes de ejecutar. La documentación propuesta permite preparar y revisar; los resultados se rellenan con pruebas reales, y las actuaciones que no pueden realizarse se conservan como pendientes.
