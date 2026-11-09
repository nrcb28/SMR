# Alineación con resultados de aprendizaje · 0221

[Índice de la asignatura](README.md) · [Retos por RA](10-retos-por-ra.md) · [Datos de trazabilidad](alineacion-ra.json)

## Referente, interpretación y alcance

Este mapa identifica los **8 RA y 60 criterios de evaluación** del módulo Montaje y mantenimiento de equipos en el anexo I del [Real Decreto 1691/2007](https://www.boe.es/eli/es/rd/2007/12/14/1691). Se ha contrastado el [RD 499/2024, artículo séptimo](https://www.boe.es/eli/es/rd/2024/05/21/499), que adapta la organización del título. Consulta: 09/11/2026. El reparto horario madrileño se explica en [currículo](../../docs/curriculo-madrid.md); no se utilizan aquí las antiguas horas de mínimos como horas de Madrid.

Los enunciados numerados de RA se reproducen del texto legal, normalizando espacios. Las descripciones de criterios de las tablas son **paráfrasis didácticas**, conservando sus letras; la norma enlazada contiene su redacción completa. Las actividades, evidencias y comprobaciones son propuestas originales. No son una escala oficial ni acreditan que una persona haya adquirido el RA por leer o completar un documento.

Usa cuatro estados en tu seguimiento: preparado, ejecutado, verificado y pendiente. «Preparado» significa que existe el plan; «ejecutado», que hubo una actuación real; «verificado», que la evidencia satisface la comprobación; «pendiente», que falta medio, supervisión o prueba. Conserva resultados reales e identifica por separado los ejemplos sintéticos. Las tareas físicas, colaborativas o de un producto no disponible no se dan por adquiridas mediante una sustitución declarativa.

## Cómo construir el dossier

Abre una ficha por RA, añade los documentos de estudio y prepara los objetos de laboratorio. Antes de ejecutar escribe qué criterio pretende demostrar cada paso y qué resultado lo contradice. Después conserva artefacto, contexto, identidad, versión y conclusión. Una captura aislada sin procedimiento puede mostrar un estado, pero no la secuencia que lo produjo ni su recuperación.

La actividad A1 integra los criterios del RA salvo que se indique A2. Las actividades A2 separan actuaciones que requieren otro entorno, material o supervisión. Esta separación permite registrar la parte real pendiente sin ocultarla detrás de un informe. Las guías de estudio enlazadas se complementan con el nuevo reto; un enlace no demuestra por sí solo cobertura práctica.

<a id="ra1"></a>
## RA1

> Selecciona los componentes de integración de un equipo microinformático estándar, describiendo sus funciones y comparando prestaciones de distintos fabricantes.

El resultado exige una decisión técnica basada en uso y compatibilidad. Una lista de componentes o un presupuesto sin comprobar conectores, soporte y refrigeración deja criterios sin evidencia. La comparación no tiene que favorecer al fabricante más conocido: se valora la relación demostrable entre necesidad, prestaciones y restricciones.

**Estudio:** [01-fundamentos.md](01-fundamentos.md) · [02-guia-tecnica.md](02-guia-tecnica.md) · [05-medicion-y-rendimiento.md](05-medicion-y-rendimiento.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 1.a | Explicar bloques funcionales y su relación | Diagrama CPU–memoria–E/S con flujos | Cada bloque tiene función y una dependencia explicada |
| 1.b | Reconocer buses e interconexiones | Tabla de interfaces y enlace de cada componente | Distingue formato físico, protocolo y capacidad del trayecto |
| 1.c | Comparar propiedades de microprocesadores | Fichas de dos CPU con socket y requisitos | No usa frecuencia como único criterio y verifica soporte de placa |
| 1.d | Relacionar refrigeración y carga | Plan térmico con disipador y ventilación | Respeta límites y montaje del fabricante sin inventar ensayos |
| 1.e | Interpretar la configuración de placa | Ficha firmware, conectores y opciones | Explica efecto y compatibilidad de cada opción elegida |
| 1.f | Seleccionar chasis compatible | Plano de espacio, formato y fijaciones | Encaja placa, refrigerador, fuente y unidades sin supuestos ocultos |
| 1.g | Identificar y manipular componentes básicos | Inventario y registro de manipulación supervisada | Identificación exacta y manipulación segura; una VM no suple evidencia física |
| 1.h | Justificar adaptador gráfico y monitor | Comparativa de salidas, resolución y uso | CPU/GPU/salida/cable/pantalla admiten el modo requerido |
| 1.i | Seleccionar adaptadores de expansión | Tabla de adaptadores y ranuras disponibles | Comprueba carriles, conectores y controladores necesarios |
| 1.j | Reconocer documentación y accesorios | Lista de documentación, cables y controladores | Separa lo incluido de lo que debe adquirirse y cita procedencia |

**Actividades vinculadas:** [0221-RA1-A1: Configuración justificada para tres usos](10-retos-por-ra.md#ra1) — CE a, b, c, d, e, f, g, h, i, j

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra2"></a>
## RA2

> Ensambla un equipo microinformático, interpretando planos e instrucciones del fabricante aplicando técnicas de montaje.

Ensamblar exige desempeño observable sobre equipos reales de entrenamiento. Preparar un plano o identificar piezas en una VM ayuda a estudiar, pero no demuestra haber usado fijaciones, montado refrigeración o manipulado memoria. El acta debe separar preparación, ejecución supervisada y verificación; no presentar una fotografía del equipo ya montado como toda la prueba.

**Estudio:** [02-guia-tecnica.md](02-guia-tecnica.md) · [03-practicas.md](03-practicas.md) · [06-diagnostico-por-subsistemas.md](06-diagnostico-por-subsistemas.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 2.a | Preparar herramientas y útiles | Checklist de banco y herramientas | Herramienta adecuada, protección ESD y recuento previo |
| 2.b | Interpretar manuales de componentes | Secuencia anotada con referencias del fabricante | Cada decisión de montaje está respaldada por el manual exacto |
| 2.c | Identificar apertura y sistemas de fijación | Plano o fotos saneadas del chasis | Describe orden de apertura/cierre y evita tornillos o separadores sobrantes |
| 2.d | Ensamblar placa, CPU y refrigeración | Registro de dos configuraciones autorizadas | Montaje real supervisado y conforme a cada conjunto; no simulado como hecho |
| 2.e | Ensamblar memoria, unidades y expansión | Hoja de conexiones y posiciones | Comprueba canal, ranura, conector y fijación antes de energizar |
| 2.f | Configurar firmware básico | Registro antes/después de parámetros mínimos | Cambia sólo opciones justificadas y conserva retorno |
| 2.g | Comprobar prestaciones tras montar | Acta de POST, memoria, disco y estabilidad | Pruebas adecuadas y resultados reales; no basta un único arranque |
| 2.h | Documentar el montaje | Informe con inventario, incidencias y aceptación | Otra persona puede reconstruir la configuración y sus límites |

**Actividades vinculadas:** [0221-RA2-A1: Montaje con aceptación por subsistemas](10-retos-por-ra.md#ra2) — CE a, b, c, d, e, f, g, h

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra3"></a>
## RA3

> Mide parámetros eléctricos, identificando el tipo de señal y relacionándola con sus unidades características.

El RA contiene medidas eléctricas de fuente y SAI, una carencia que un benchmark o la lectura de un sensor no cubre. Se propone primero diseño de instrumentación y después una sesión real en banco protegido preparado por el docente. Sin formación, equipo o supervisión, los criterios de medida se dejan pendientes; no se sustituyen por datos sintéticos declarados como reales.

**Estudio:** [01-fundamentos.md](01-fundamentos.md) · [05-medicion-y-rendimiento.md](05-medicion-y-rendimiento.md) · [10-retos-por-ra.md](10-retos-por-ra.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 3.a | Elegir instrumento según la señal | Ficha de señal, instrumento y manual | Distingue continua/alterna y magnitud sin improvisar puntos de contacto |
| 3.b | Seleccionar función, rango y conexión | Plan de medida revisado por docente | Sondas, entrada y rango adecuados; continuidad/resistencia sólo sin energía |
| 3.c | Comparar medida y referencia | Tabla de nominal, tolerancia y observación | Unidades, rango y criterio proceden del fabricante; no confunde error con avería |
| 3.d | Reconocer bloques de fuente de PC | Diagrama funcional de fuente cerrada | Identifica funciones sin abrir ni intervenir el primario |
| 3.e | Enumerar salidas de una fuente típica | Tabla de raíles según modelo y documentación | No extrapola colores/pines entre conectores modulares de fabricantes |
| 3.f | Medir salidas de fuente mediante puesto protegido | Registro real de medidas supervisadas | Sólo comprobador o puntos preparados y protegidos; datos simulados quedan pendientes |
| 3.g | Reconocer bloques y función de SAI | Esquema rectificador, batería, inversor y bypass cuando exista | Describe topología concreta y distingue potencia, autonomía y VA/W |
| 3.h | Medir señales del SAI en banco autorizado | Acta real de prueba y supervisión | Sólo puntos y procedimiento autorizados; no abrir batería/SAI ni medir red improvisadamente |

**Actividades vinculadas:** [0221-RA3-A1: Banco de instrumentación y alimentación supervisada](10-retos-por-ra.md#ra3) — CE a, b, c, d, e, g; [0221-RA3-A2: Mediciones reales supervisadas con banco protegido](10-retos-por-ra.md#ra3) — CE f, h

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra4"></a>
## RA4

> Mantiene equipos informáticos interpretando las recomendaciones de los fabricantes y relacionando las disfunciones con sus causas.

Mantener no equivale a intercambiar piezas hasta que el equipo arranque. Se necesita relacionar aviso y causa, realizar una corrección compatible y cerrar la intervención con evidencia. Las prácticas usan fallos reversibles o un equipo ya averiado autorizado; nunca se provoca sobretemperatura o daño para fabricar una avería.

**Estudio:** [03-practicas.md](03-practicas.md) · [04-diagnostico-y-evaluacion.md](04-diagnostico-y-evaluacion.md) · [06-diagnostico-por-subsistemas.md](06-diagnostico-por-subsistemas.md) · [07-almacenamiento-integridad-y-vida-util.md](07-almacenamiento-integridad-y-vida-util.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 4.a | Interpretar avisos acústicos y visuales | Código observado y manual del modelo | No atribuye significado universal a pitidos o LED |
| 4.b | Diagnosticar y corregir sobrecalentamiento | Serie de datos y mantenimiento autorizado | No provoca calor deliberadamente y revalida bajo carga controlada |
| 4.c | Resolver averías habituales | Árbol con al menos tres hipótesis y pruebas | Cada cambio responde a una evidencia y una causa verificable |
| 4.d | Sustituir una pieza deteriorada | Acta de retirada y sustitución | Equipo seguro y pieza identificada; no se repara físicamente una pieza peligrosa |
| 4.e | Verificar compatibilidad del repuesto | Matriz original–repuesto–firmware | Incluye restricciones eléctricas, físicas y de soporte |
| 4.f | Actualizar o ampliar componentes | Plan de cambio y ensayo antes/después | Conserva copia, retorno y pruebas de funcionamiento relevante |
| 4.g | Redactar informe de avería o ampliación | Parte técnico y explicación para usuario | Distingue causa confirmada, contención e hipótesis pendiente |

**Actividades vinculadas:** [0221-RA4-A1: Parte de reparación y ampliación con causa demostrada](10-retos-por-ra.md#ra4) — CE a, b, c, d, e, f, g

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra5"></a>
## RA5

> Instala software en un equipo informático utilizando una imagen almacenada en un soporte de memoria y justificando el procedimiento a seguir.

Crear y restaurar una imagen es una competencia distinta de instalar el SO desde cero o comprimir una carpeta. Importan consistencia de origen, identidad del destino, medios de arranque y funcionamiento posterior. El reto añade generalización e identidades para que una clonación no produzca dos equipos aparentemente iguales en la red.

**Estudio:** [03-practicas.md](03-practicas.md) · [07-almacenamiento-integridad-y-vida-util.md](07-almacenamiento-integridad-y-vida-util.md) · [10-retos-por-ra.md](10-retos-por-ra.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 5.a | Distinguir instalación estándar y preinstalación | Comparativa de procesos y responsabilidades | Explica personalización, generalización, licencia e identidad |
| 5.b | Probar secuencias de arranque del firmware | Registro de orden anterior y pruebas | Verifica UEFI/medio/arquitectura sin cambiar modos de disco a ciegas |
| 5.c | Arrancar desde medios diferentes | Acta de dos medios legítimos de recuperación | Documenta firma/origen y estado de Secure Boot sin desactivar controles por rutina |
| 5.d | Crear imagen de preinstalación | Manifiesto de imagen y procedimiento de captura | Fuente consistente, identificación exacta y copia protegida |
| 5.e | Restaurar imagen sobre destino de laboratorio | Acta con identidad de disco y pruebas posteriores | Destino desechable inequívoco y verificación de arranque, datos e identidad |
| 5.f | Comparar herramientas de imagen | Matriz de funciones y limitaciones | Distingue imagen de archivo, clon, snapshot y copia independiente |

**Actividades vinculadas:** [0221-RA5-A1: Preinstalación, imagen y restauración controlada](10-retos-por-ra.md#ra5) — CE a, b, c, d, e, f

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra6"></a>
## RA6

> Reconoce nuevas tendencias en el ensamblaje de equipos microinformáticos describiendo sus ventajas y adaptándolas a las características de uso de los equipos.

Las expresiones barebone, HTPC, PDA y modding proceden del texto legal del título. Se mantienen como referentes curriculares y se estudia su evolución sin fingir que los dispositivos de 2007 representan todo el mercado de 2026. El análisis debe comparar funciones y restricciones técnicas, no hacer publicidad de modelos.

**Estudio:** [01-fundamentos.md](01-fundamentos.md) · [05-medicion-y-rendimiento.md](05-medicion-y-rendimiento.md) · [10-retos-por-ra.md](10-retos-por-ra.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 6.a | Comparar formas de integración placa/chasis | Matriz ATX, SFF y SoC/equipo integrado | Relaciona formato con expansión, reparación y refrigeración |
| 6.b | Evaluar plataformas semiensambladas | Dos fichas de barebones vigentes al consultar | Aclara componentes incluidos, RAM/almacenamiento admitidos y soporte |
| 6.c | Diseñar un HTPC | Ficha de vídeo, audio, red, ruido y control | Comprueba códecs/salidas/pantalla y no sólo potencia de CPU |
| 6.d | Diferenciar equipos por aplicación | Comparativa aula, quiosco y captura multimedia | Vincula cada requisito a una decisión técnica medible |
| 6.e | Valorar informática móvil y su evolución | Informe de movilidad, reparación y soporte | Contextualiza PDA/navegadores del texto histórico frente a dispositivos actuales |
| 6.f | Evaluar modding con criterios técnicos | Diseño reversible y análisis de efectos | Mantiene seguridad, ventilación, garantía y accesibilidad; no modifica red eléctrica |

**Actividades vinculadas:** [0221-RA6-A1: Diseño de barebone, HTPC y equipo especializado](10-retos-por-ra.md#ra6) — CE a, b, c, d, e, f

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra7"></a>
## RA7

> Mantiene periféricos, interpretando las recomendaciones de los fabricantes de equipos y relacionando disfunciones con sus causas.

El resultado incluye mecánica de periféricos y tecnologías profesionales además de controladores. Una cola virtual permite estudiar envío y autorización, pero no demuestra sustitución de consumible o reparación de alimentación de papel. Cada evidencia debe nombrar el equipo, el alcance y qué parte física sigue pendiente.

**Estudio:** [01-fundamentos.md](01-fundamentos.md) · [08-perifericos-mantenimiento-y-casos.md](08-perifericos-mantenimiento-y-casos.md) · [10-retos-por-ra.md](10-retos-por-ra.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 7.a | Resolver fallos mecánicos de impresión | Parte de atasco o alimentación de papel | Procedimiento del modelo, desconexión/enfriamiento y prueba física posterior |
| 7.b | Cambiar consumibles | Registro de consumible y sustitución | Pieza compatible, tratamiento de residuos y prueba de calidad |
| 7.c | Resolver fallo mecánico de entrada | Acta de teclado/ratón/dispositivo autorizado | Distingue suciedad/conexión/software y evita desmontaje no autorizado |
| 7.d | Relacionar captura de imagen fija y vídeo con usos | Comparativa escáner/cámara y muestra sintética | Resolución, frecuencia, interfaz y permisos satisfacen el uso |
| 7.e | Seleccionar otros periféricos multimedia | Ficha de audio, videoconferencia o proyección | Verifica compatibilidad, latencia y controles de acceso pertinentes |
| 7.f | Reconocer impresión profesional y filmado | Diagrama de flujo y comparación de tecnologías | Distingue impresión de oficina, producción, preimpresión y filmadora sin atribuir experiencia inexistente |
| 7.g | Planificar mantenimiento preventivo | Calendario y desencadenantes por dispositivo | Cada tarea tiene frecuencia razonada, responsable y comprobación |

**Actividades vinculadas:** [0221-RA7-A1: Taller de periféricos y captura multimedia](10-retos-por-ra.md#ra7) — CE a, b, c, d, e, f, g

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra8"></a>
## RA8

> Cumple las normas de prevención de riesgos laborales y de protección ambiental, identificando los riesgos asociados, las medidas y equipos para prevenirlos.

La prevención y protección ambiental se integran en las tareas de montaje y mantenimiento. Completar una tabla de riesgos no acredita haber operado una máquina con seguridad; una práctica real debe seguir las indicaciones del centro y registrar condiciones de parada. La matriz usa una valoración didáctica y no reemplaza una evaluación preventiva profesional.

**Estudio:** [02-guia-tecnica.md](02-guia-tecnica.md) · [08-perifericos-mantenimiento-y-casos.md](08-perifericos-mantenimiento-y-casos.md) · [10-retos-por-ra.md](10-retos-por-ra.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 8.a | Identificar riesgos y peligrosidad | Inventario de tareas/peligros y valoración didáctica | Incluye herramientas, materiales, cargas y límites de competencia |
| 8.b | Operar equipos respetando seguridad | Observación supervisada y checklist | La ejecución real sigue procedimiento y se detiene ante condición insegura |
| 8.c | Analizar causas de accidentes | Tres escenarios y cadena causal | Distingue causa, exposición y medida; no culpa genéricamente al operador |
| 8.d | Seleccionar protecciones y EPI | Matriz tarea–protección–manual | Justifica protección y evita EPI incompatibles con la operación |
| 8.e | Relacionar manipulación y medidas preventivas | Secuencia de trabajo y controles | Aplica aislamiento, orden y ayuda de manipulación apropiados |
| 8.f | Identificar fuentes de contaminación | Mapa de residuos y emisiones del taller | Considera baterías, tóner, electrónicos y productos de limpieza |
| 8.g | Clasificar residuos para retirada selectiva | Registro de segregación y canal autorizado | No mezcla RAEE/baterías/tóner ni inventa certificación de tratamiento |
| 8.h | Comprobar orden y limpieza | Auditoría antes/después con lista objetiva | Puesto sin obstrucciones, herramientas controladas y residuos retirados |

**Actividades vinculadas:** [0221-RA8-A1: Orden de trabajo preventiva y ambiental](10-retos-por-ra.md#ra8) — CE a, b, c, d, e, f, g, h

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

## Recuperación y evaluación formativa

Una entrega incompleta se revisa por criterio, no se borra su historial. Identifica qué observación falta y prepara una segunda prueba con entradas o condiciones diferentes. Si el problema era conceptual, explica la corrección antes de repetir; si era de entorno, documenta cómo se identificó la dependencia. Una práctica repetida sin comprender el fallo no aporta la misma evidencia que una recuperación razonada.

Para la revisión entre participantes utiliza la [matriz de pruebas](../../recursos/plantillas/matriz-de-pruebas.md). Verifica que cada letra tenga actividad y artefacto, y que el resultado real no se haya copiado de la solución. La matriz no prescribe ponderaciones oficiales ni reemplaza la programación del centro. Una actividad puede aportar evidencia a varios criterios, pero cada uno conserva su comprobación concreta.

## Fuentes y mantenimiento

- [RD 1691/2007, anexo I](https://www.boe.es/eli/es/rd/2007/12/14/1691): enunciados y letras normativas de este módulo.
- [RD 499/2024, artículo séptimo](https://www.boe.es/eli/es/rd/2024/05/21/499): modificación del anexo I y organización adaptada.
- [Marco de SMR Madrid](../../docs/curriculo-madrid.md): horas, módulos transversales, proyecto y optatividad.

Si cambia una norma, contrasta enunciados y letras antes de actualizar la actividad. Si sólo cambia una herramienta, conserva el criterio y modifica procedimiento, versión, prueba y limitaciones. El JSON conserva los identificadores para revisar la trazabilidad de forma reproducible.
