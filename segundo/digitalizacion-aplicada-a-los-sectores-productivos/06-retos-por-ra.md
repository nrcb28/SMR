# Retos de Digitalización por resultados de aprendizaje

[Mapa de RA y criterios](05-alineacion-ra.md) · [Índice del módulo](README.md)

Estos cinco retos desarrollan los cinco RA del módulo 1664 de grado medio. Se utiliza un taller ficticio que recibe, repara y prepara equipos para doce puestos. Las cifras y eventos proporcionados son datos sintéticos para razonar; los resultados de tu piloto deben registrarse por separado. Los criterios de aceptación son propuestas docentes y no sustituyen la programación del centro.

Trabaja sobre diagramas, hojas, registros y, cuando proceda, un prototipo local con datos ficticios. No es necesario contratar nube, conectar sensores al edificio o automatizar decisiones de equipos reales. La guía de [datos e integraciones](03-datos-integraciones-y-gobierno.md) aporta diccionario, CSV/JSON y semántica para conservar las evidencias.

<a id="ra1"></a>
## RA1. Del equipo desechable al ciclo de retorno

**Encargo y preparación.** Compara dos formas de prestar el mismo servicio: mantener doce puestos funcionales durante un periodo definido. En la primera se compra, utiliza y retira cada equipo sin plan de retorno; en la segunda se diagnostica, repara, reutiliza y, cuando corresponde, se entrega por el circuito autorizado de residuos. Conserva requisitos de soporte, seguridad y accesibilidad: no puedes declarar circular una opción que deja de prestar el servicio necesario.

**Procedimiento.** Dibuja los dos flujos desde la compra hasta la salida. En cada etapa identifica material, energía, transporte, datos y trabajo. Marca qué entradas conoces y cuáles faltan. La economía circular requiere examinar los bucles que conservan utilidad; reciclar es relevante para materiales que ya no pueden seguir en uso, pero no equivale a reparar un equipo ni elimina impactos anteriores.

Después busca dos procesos **reales** observados o documentados: uno que presente una secuencia lineal y otro que incluya recuperación de productos o componentes. Utiliza un procedimiento del centro autorizado para estudio o documentación primaria del responsable del proceso. Guarda título, organización, fecha, enlace y fragmento de evidencia pertinente. El taller ficticio sirve para practicar el método, pero no cumple por sí solo los CE que piden identificar procesos reales. Si la fuente no permite conocer el destino final, registra esa incertidumbre en lugar de completarla con una suposición.

Prepara una comparación con la misma unidad funcional: «doce puestos que cumplen requisitos durante el periodo». Cuenta reparaciones, piezas, retiradas, horas y energía sólo cuando dispongas de datos. Si utilizas factores ilustrativos, márcalos como hipótesis. Relaciona una acción con una meta ODS pertinente consultando [Naciones Unidas](https://sdgs.un.org/goals); no presentes el icono de un objetivo como prueba de impacto conseguido.

**Solución razonada y aceptación.** Una propuesta circular defendible puede mantener equipos compatibles, cambiar piezas verificadas, reasignar usos y registrar salidas. Debe justificar cuándo deja de ser razonable conservar un equipo. Los dos diagramas deben mostrar todas sus etapas y cada etapa debe tener una repercusión explicada. La ficha real circular debe demostrar un retorno concreto, no sólo una frase comercial. Una afirmación que no pueda apoyarse en dato o fuente queda pendiente.

**Entregables y revisión.** Dos diagramas, dos fichas reales, tabla de impactos y comparación ODS. Somete la conclusión a una condición adversa: una reparación puede fallar o requerir transporte adicional. Explica qué cambiaría y cómo conservarías el servicio. No manipules residuos o baterías para obtener evidencia: observa el procedimiento competente y utiliza registros saneados.

<a id="ra2"></a>
## RA2. El evento físico que se convierte en servicio

**Problema.** El taller quiere detectar condiciones anómalas de un armario de equipos sin sustituir la supervisión humana por una automatización ciega. Diseña la evolución desde una revisión manual hasta un sistema que registra eventos y solicita una comprobación. El ejercicio es conceptual y usa lecturas sintéticas, no controla climatización ni alimentación.

Define un evento con identificador de sensor, fecha UTC, valor, unidad y calidad. Por ejemplo, una fila ficticia puede representar 31 °C; ese número no es un umbral universal de seguridad. El umbral y su significado dependen de equipos, ubicación, fabricante y protocolo de trabajo. Separa «lectura recibida», «lectura fiable» y «condición que requiere intervención».

**Pasos.** Primero describe el proceso anterior: una persona observa, anota y comunica. Después dibuja sensor, comunicación, recepción, almacenamiento, regla y persona que atiende la incidencia. Explica en qué punto una magnitud del mundo físico se representa como dato y qué acciones podrían volver al mundo físico. Una base de datos con números inventados permite probar el procesamiento, pero no demuestra calibración de un sensor ni un sistema ciberfísico implantado.

Compara automatización aislada y entorno conectado. Una regla local que enciende un indicador no comparte necesariamente información con recepción, soporte o mantenimiento. El cambio de organización incluye qué datos se relacionan, quién decide y cómo se sigue el resultado. Introduce tres eventos de prueba: lectura válida, valor con unidad ausente y repetición del mismo identificador. Decide qué se acepta, qué se pone en revisión y cómo evitas crear dos incidencias por el mismo evento.

**Resultado esperado.** La mejora propuesta podría reducir tiempo de registro o facilitar trazabilidad. Define la métrica: minutos entre observación y ticket válido, porcentaje de eventos completos o repetidos. Para un piloto compara tareas equivalentes y conserva denominadores. No conviertas una reducción estimada en productividad medida ni en dinero ahorrado automáticamente.

**Solución y aceptación.** El diseño debe conservar identidad, tiempo y unidad a lo largo del flujo; explicar qué parte física, software, IoT y comunicación intervienen; y relacionar el cambio con ventajas para cliente y empresa. Incluye un compromiso: más avisos pueden crear ruido o aumentar carga de revisión. Ante pérdida de conexión el sistema conserva o marca datos según un procedimiento y la supervisión prevista continúa.

**Entregables.** Línea temporal de evolución, diagramas antes/después, contrato del evento, tabla de tres pruebas y ficha de ventajas/compromisos por interesado. Si no hay sensor real, la prueba acredita tratamiento del registro sintético y la comprensión del diseño; la parte física se marca como pendiente.

<a id="ra3"></a>
## RA3. Situar cómputo y responsabilidades sin perder control

**Encargo.** El taller considera un servicio conectado para registrar incidencias y conservar históricos. Compara ejecución local, IaaS, PaaS y SaaS. La comparación no consiste en elegir la opción con más funciones: debes explicar dónde se procesa, quién opera cada componente, cómo se exportan los datos y qué ocurre cuando no hay conectividad.

Parte de la definición y modelos de [NIST SP 800-145](https://www.nist.gov/publications/nist-definition-cloud-computing). Clasifica funciones —procesamiento de datos, intercambio de información y ejecución de aplicación— y asigna responsabilidades de sistema operativo, dependencias, aplicación, identidad y datos. En SaaS el proveedor opera más capas, pero el cliente sigue tomando decisiones sobre usuarios, información y uso del servicio. Los contratos concretos deben revisarse; esta tabla no les atribuye garantías que no se han leído.

**Diseño distribuido.** Dibuja además una función cerca del origen: validar que una lectura tenga unidad antes de enviarla, por ejemplo. Explica edge como procesamiento próximo a la fuente o usuario y consulta [NIST SP 500-325](https://csrc.nist.gov/pubs/sp/500/325/final) para situar fog y mist en modelos IoT distribuidos. No son nombres intercambiables con IaaS/PaaS/SaaS: una dimensión expresa ubicación/organización del cómputo y la otra la forma de prestar y repartir responsabilidades del servicio. La terminología puede variar en productos; declara la definición usada.

Plantea un escenario de desconexión de veinte minutos. Decide qué puede seguir localmente, qué se pone en cola, qué información no debe repetirse y qué se comunica a la persona usuaria. También establece qué reloj, identificador y estado permiten reconciliar sin duplicar. No prometas continuidad por el simple hecho de escribir «edge» en el dibujo.

**Prueba sin contratar.** Exporta registros sintéticos de una hoja a CSV o JSON, verifica que conservan campos e identificadores y reimpórtalos a una copia. Esta prueba acredita un mecanismo local de intercambio; no prueba la exportación de un proveedor concreto. Para evaluar un producto, lee sus formatos, límites y procedimientos y marca lo no ensayado.

**Aceptación y solución.** La tabla debe distinguir todos los modelos y funciones del criterio, situar cloud/edge/fog/mist con zonas y límites, y justificar una alternativa con ventajas y dependencias. Un sistema que procesa alertas localmente y sincroniza históricos puede responder al escenario, pero añade operación y reconciliación. Un SaaS puede simplificar mantenimiento y seguir sin satisfacer un requisito de trabajo desconectado: la decisión depende de ese requisito, no de una preferencia universal.

**Entregables.** Matriz de responsabilidades, mapa de ubicación, secuencia de desconexión/retorno y prueba de exportación con resultado real o pendiente explícito.

<a id="ra4"></a>
## RA4. Elegir THD por función y comprobar su efecto

**Preparación.** El RA exige reconocer un abanico de tecnologías habilitadoras. Para no reducirlo a IA o nube, crea una ficha de cada grupo de la tabla y añade un ejemplo del sector. La ficha explica función, dato necesario, responsable, beneficio verificable y limitación; la referencia comercial de un producto no sustituye esa explicación.

| Tecnología | Aplicación que puede estudiarse en SMR | Límite que debe quedar explicado |
| --- | --- | --- |
| IoT | Lecturas de entorno vinculadas a mantenimiento | Calidad del sensor, conectividad y seguridad |
| IA | Sugerir categorías de tickets sintéticos | Errores, sesgo, revisión y datos de entrada |
| Big Data | Analizar grandes conjuntos heterogéneos de eventos | Un CSV pequeño no demuestra escala Big Data |
| 5G | Conectar ubicaciones con necesidades de movilidad | Cobertura, capacidad, coste y dependencia |
| Robótica colaborativa | Asistencia física en un proceso de producción | Evaluación de seguridad y competencia especializada |
| Blockchain | Registro compartido en una necesidad de varias partes | No garantiza veracidad de lo que se introduce |
| Ciberseguridad | Controlar acceso y trazabilidad del servicio | Un control aislado no cubre todo el riesgo |
| Fabricación aditiva | Prototipo de accesorio autorizado | Material, resistencia, propiedad y validación |
| Realidad virtual | Formación o visualización de una instalación | Accesibilidad, equipo y utilidad real |
| Gemelo digital | Representar un activo con datos y actualización definidos | Un dibujo estático no equivale a un gemelo conectado |

**Trabajo de integración.** Escoge dos tecnologías para el proceso del taller y descarta una tercera. Relaciona recepción, reparación, compras y dirección mediante datos: el estado del equipo no debe significar cosas distintas en cada unidad. Define quién crea y quién consume el registro y cómo se avisa un error.

Completa un modelo de almacenamiento no convencional, como documentos JSON u objetos con metadatos, y explica cómo accede cada unidad. Contrasta su estructura con la tabla relacional ya estudiada; «no convencional» no significa que carezca de reglas ni permisos. Especifica identidad del activo, versión, exportación y recuperación.

**Cálculo y solución.** Supón que una automatización ahorra cinco minutos de registro en veinte tickets semanales: libera cien minutos por semana bajo ese supuesto. Antes de valorarlo añade revisión, formación y mantenimiento. Si después genera retrabajo o desplaza captura a otra unidad, la mejora local puede no mejorar el sistema. Usa indicadores por etapa y del proceso completo, y etiqueta los valores de ejemplo como estimaciones.

**Aceptación.** Se describen todas las tecnologías pedidas, se justifican adopciones y descarte, y cada mejora tiene métrica, carga equivalente y límite. La solución debe explicar por qué digitalizar ayuda a una función concreta y qué nuevo coste o riesgo necesita gestionar.

<a id="ra5"></a>
## RA5. Transformar el taller por fases y con retorno

**Encargo final.** Integra los artefactos anteriores en un plan para un taller que trabajaba con recepción en papel y decisiones separadas de compras y reparación. La propuesta debe afectar al funcionamiento, a los recursos humanos y a la gestión de salidas. Un catálogo de software sin secuencia ni responsables no resuelve este resultado.

**Procedimiento.** Describe primero el diagrama actual y sus puntos de espera. Enumera necesidades y conserva una alternativa manual razonable. Para cada etapa selecciona una tecnología y un mecanismo de conexión con el resto: identificadores comunes, estado del activo, documentos y responsabilidades. El diagrama futuro muestra también actividades que siguen siendo manuales, como inspección o autorización.

Organiza tres fases: preparar datos y reglas; probar con registros sintéticos o activos autorizados; y decidir si se extiende. Cada fase necesita personas, tiempo, formación, revisión de permisos y condición para continuar. La adopción cambia tareas: quien antes registraba puede tener que validar o atender excepciones. Incluye ese trabajo en la capacidad, evitando presentar la automatización como eliminación automática de puestos.

Reutiliza el modelo económico del módulo, pero cambia una hipótesis. Si cuota, formación o mantenimiento aumentan, recalcula. Distingue beneficio supuesto, capacidad liberada y caja. Para el componente ambiental compara reparaciones, retrabajo, piezas y residuos; un proceso digital puede consumir más dispositivos o facilitar decisiones de sustitución, por lo que «sin papel» no demuestra por sí solo menor impacto total.

**Solución razonada.** Una secuencia defendible comienza por acordar datos y responsables, prueba la transferencia y la recuperación y amplía sólo tras validar. Si el piloto pierde identificadores al exportar, se detiene la extensión y se corrige el contrato. Si una fase falla, conserva una copia y un procedimiento para volver al registro anterior sin perder qué cambios habría que trasladar.

**Entregables y aceptación.** Diagrama actual/futuro, matriz etapa-tecnología, informe de viabilidad, comparación de residuos y plan secuenciado de recursos. La revisión comprueba coherencia entre nombres, estados, costes y evidencias. Cada CE a–h debe poder localizarse en un artefacto. Ningún dato del caso se presenta como una implantación ejecutada; el estudiante añade su resultado real, limitaciones y siguiente mejora.

## Revisión docente y defensa

La evaluación propuesta examina fidelidad al problema, trazabilidad de datos, coherencia técnica/económica, contraste de fuentes, pruebas y comunicación. No se asigna una ponderación oficial por RA. Si falta evidencia para un criterio, registra qué actividad lo desarrollará y qué condición permitirá aceptarlo. El [mapa de criterios](05-alineacion-ra.md) y el [JSON de alineación](alineacion-ra.json) conservan la referencia entre el número oficial, el material y la actividad didáctica.
