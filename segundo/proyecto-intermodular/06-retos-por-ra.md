# Retos de Proyecto intermodular por resultados de aprendizaje

[Alineación y criterios](05-alineacion-ra.md) · [Índice del módulo](README.md) · [Datos de trazabilidad](alineacion-ra.json)

## Encargo común y reglas de evidencia

El caso de entrenamiento es una pequeña organización que necesita mantener doce puestos, compartir documentación por grupos, ofrecer una web interna y recuperar el servicio después de un incidente. El alumnado diseña un piloto reproducible en el laboratorio y un plan de implantación. La organización, los costes y los sucesos del ejemplo son ficticios; las evidencias reales se registran cuando se realiza cada actividad.

El proyecto no se reduce a instalar servicios. Sus cinco RA incluyen conocer empresas, comparar soluciones, planificar, seguir el trabajo y comunicarlo. Una única memoria puede reunir varios criterios, pero debe indicar dónde se demuestra cada uno. Utiliza los identificadores `1713-RA1-A1` a `1713-RA5-A1` y conserva los productos con fecha y versión.

La base técnica está descrita en el [laboratorio común](../../docs/laboratorio.md): `srv01` en `.56.10`, cliente en `.56.20`, dominio de servicios `aula.test` y una red LAB sin gateway. El piloto puede usar Samba independiente, DNS y web en escenarios compatibles. Si se necesita un directorio, utiliza el controlador separado y revisa sus dependencias; no añadas a la vez servidores DNS incompatibles en una misma dirección.

Antes de ejecutar, prepara una copia y una ruta de recuperación. No se necesitan cuentas públicas, compras ni datos reales de clientes. Cuando una tarea exige una empresa o una presentación observada, la documentación ficticia enseña el procedimiento pero no sustituye esa evidencia. La programación del centro concreta calendario, tutoría, instrumentos y calificación.

<a id="ra1"></a>
## RA1 · Caracterizar una empresa y su estrategia de servicio

**Actividad `1713-RA1-A1`.** El objetivo es explicar cómo se organiza un servicio informático y qué relación existe entre demanda, recursos y resultados. No empieces por elegir un servidor. Primero identifica qué servicio necesita el cliente y qué organización podría prestarlo.

### Preparación y procedimiento

Selecciona documentación primaria de dos empresas reales representativas del sector: páginas de servicios, información corporativa publicada o memorias accesibles. Registra organización, título, fecha, enlace y alcance. No copies datos de clientes ni deduzcas volumen de negocio de un catálogo de productos. Si una información no es pública, marca el campo como desconocido y evita atribuírselo a esa empresa.

Construye después el caso ficticio del taller. Dibuja un organigrama funcional con recepción/comercial, administración, operación técnica y responsable de servicio. Una pequeña organización puede reunir varias funciones en una persona; explica esa acumulación en lugar de inventar departamentos y personal que no existen en el modelo. Para cada función indica entrada, decisión, salida y destinatario.

Define una demanda ilustrativa: número de puestos atendidos, solicitudes de soporte por periodo y tipos de servicio. Estima el volumen de trabajo mediante operaciones reproducibles. Por ejemplo, doce intervenciones de una hora no equivalen a doce horas de disponibilidad del servicio: se necesita además recepción, preparación, documentación y comprobación. Si elaboras una facturación hipotética, separa cantidad, tarifa y periodo; no la presentes como facturación de las empresas consultadas.

Redacta una estrategia breve: qué necesidad prioriza, qué nivel de soporte puede sostener y qué trabajos debe derivar. Relaciona recursos humanos y materiales con esa estrategia. Un segundo servidor sin procedimiento de recuperación no demuestra continuidad, y una persona asignada simultáneamente a dos tareas exclusivas no aporta dos capacidades independientes.

### Solución razonada y comprobación

Una caracterización defendible conecta las funciones con el recorrido de la solicitud: recepción la registra, operación diagnostica, administración conserva información económica y el responsable valida alcance y aceptación. La estrategia puede priorizar conservación de datos y recuperación antes de automatizar nuevas funciones, si ésa es la necesidad identificada.

Prepara un cuadro de seguimiento con tres indicadores: solicitudes que llegan, tareas terminadas con aceptación y tareas reabiertas. Define denominador e intervalo. Una reducción de tiempo no significa mejora si aumenta retrabajo o deja de comprobar permisos. Usa una fila sintética para ensayar el cálculo y conserva una columna distinta para observaciones reales.

Relaciona un servicio con una meta ODS pertinente. Por ejemplo, prolongar vida útil necesita evidencia de función conservada, soporte y destino de piezas; el icono ODS por sí solo no demuestra impacto. Declara qué fases externas no puedes medir.

**Entregables:** dos fichas reales con fuente, organigrama del caso, matriz de funciones, estimación de demanda y recursos, estrategia, cuadro de seguimiento y ficha ODS. **Aceptación:** otra persona distingue hechos publicados, hipótesis y decisiones; puede reproducir cálculos y explicar quién hace qué. **Revisión:** plantea una demanda un 25 % mayor y justifica qué recurso se saturaría primero, sin suponer crecimiento idéntico de todos los costes.

<a id="ra2"></a>
## RA2 · Comparar soluciones y elaborar un pequeño proyecto

**Actividad `1713-RA2-A1`.** La organización plantea «guardar documentos de forma segura». Debes convertir la petición en requisitos, comparar alternativas y presentar una solución viable con costes y calidad definidos.

### De la necesidad a la decisión

Entrevista en una simulación a los roles de persona usuaria y responsable. Registra necesidad, problema observado y requisito comprobable. Un ejemplo es que el grupo lector pueda abrir documentos sin modificarlos, el editor pueda crearlos y una cuenta ajena reciba denegación. «Todo seguro» o «que vaya rápido» no permite elegir una prueba sin más precisión.

Plantea en grupo al menos dos alternativas, por ejemplo un recurso independiente administrado por grupos y una solución integrada con un directorio existente. El acta debe conservar aportaciones, documentación consultada y motivos de descarte. No introduzcas un dominio si el requisito no lo necesita sólo para que el proyecto parezca más complejo. Si sí lo requiere, incorpora DNS, tiempo, identidad y recuperación al diseño.

Consulta versiones y requisitos de las herramientas en sus fuentes primarias. Clasifica cada conclusión como comprobada en laboratorio, revisada documentalmente o pendiente. La innovación puede ser mejorar la trazabilidad y restauración de un proceso existente; debe aportar valor concreto, no limitarse a utilizar una herramienta nueva.

Divide el proyecto en diseño, base de sistema, identidades/permisos, servicio web, copia, aceptación y entrega. Para cada parte registra entrada, producto y dependencia. Los [requisitos y decisiones](03-cuaderno-de-requisitos-y-planificacion.md) ayudan a mantener la relación entre necesidad y arquitectura.

### Presupuesto trabajado y límites

Para practicar, utiliza estas hipótesis independientes de una cotización real:

| Concepto sintético | Cantidad y coste | Importe |
| --- | --- | ---: |
| Equipos nuevos compatibles | 4 × 500 € | 2.000 € |
| Switch previsto | 1 × 120 € | 120 € |
| Medios de copia separados | 2 × 100 € | 200 € |
| SAI compatible por confirmar | 1 × 180 € | 180 € |
| Trabajo estimado | 40 h × 20 €/h | 800 € |
| Subtotal | Suma de los conceptos | 3.300 € |
| Reserva del 10 % del subtotal | 3.300 × 0,10 | 330 € |
| Total del supuesto | Subtotal más reserva | 3.630 € |

El ejemplo excluye impuestos, desplazamientos, cambios de precios y licencias que no estén ya legítimamente disponibles. Si una alternativa necesita licencias o soporte adicional, se incorpora como coste y requisito, sin asignarle cero por omisión. El SAI exige dimensionamiento técnico y compatibilidad: su precio hipotético no demuestra que sea adecuado.

### Calidad, presentación y retorno

Define pruebas de lectura/escritura/denegación, DNS, HTTPS y restauración, además de una prueba de recuperación de configuración. La calidad se observa en comportamiento, datos y documentación, no sólo en el aspecto de la memoria. Cada requisito debe tener entrada, estímulo y resultado que permita aceptar o rechazar.

Presenta la propuesta a un grupo de clase o tutoría, si está disponible. Conserva preguntas, respuestas y cambios de diseño. Entregar diapositivas no acredita por sí solo una presentación pública. **Entregables:** requisitos, acta de alternativas, fuentes y versiones, estudio de viabilidad, estructura de proyecto, recursos, presupuesto editable, memoria de diseño, plan de calidad y registro de presentación. **Aceptación:** los cálculos se reproducen y una segunda persona localiza todas las dependencias. **Caso adverso:** una herramienta deja de ser compatible; explica alternativa, coste y efecto sobre el plan antes de adoptarla.

<a id="ra3"></a>
## RA3 · Planificar ejecución, prevención y contingencias

**Actividad `1713-RA3-A1`.** El diseño aceptado se convierte en tareas realizables. El calendario debe conservar precedencias, disponibilidad, autorizaciones y posibilidad de recuperación, no sólo fechas de entrega.

### Secuencia y logística

Como ejercicio de planificación, reparte cuarenta horas-persona estimadas:

| Tarea | Esfuerzo supuesto | Dependencia principal |
| --- | ---: | --- |
| A · requisitos y estado inicial | 4 h | Encargo y alcance |
| B · diseño y revisión | 6 h | A |
| C · base de sistema y red | 8 h | B |
| D · identidades y archivos | 6 h | C |
| E · web interna | 4 h | C y nombres preparados |
| F · copia y recuperación | 4 h | D y datos de prueba |
| G · aceptación y correcciones | 6 h | D, E y F |
| H · entrega y defensa | 2 h | G |

La suma es cuarenta horas de trabajo presupuestado; no constituye una distribución oficial de las cincuenta horas curriculares ni obliga a realizar cada tarea en un único día. Con dos personas puede haber paralelismo, pero cada recurso exclusivo y cada revisión necesitan disponibilidad. No dupliques capacidad por escribir el mismo nombre en dos filas simultáneas.

Asigna a cada tarea responsable de ejecución y de revisión. Registra VM, consola, medio de copia, espacio, cuentas necesarias y documentación. Si una tarea usa hardware físico, comprueba material y competencia antes de programarla. Mantén los nombres de equipos y direcciones en un registro para evitar conflictos como reutilizar `.30` del DNS secundario para otro dispositivo.

### Permisos y prevención

Elabora una ficha de autorización por intervención. Indica alcance, equipo, datos, hora o condición y quién valida. Tener una cuenta con privilegios no implica permiso para modificar todos los sistemas que alcanza. En el laboratorio la autorización se limita a sus VMs y datos ficticios.

Relaciona cada tarea con riesgos y controles. En montaje se aplican los procedimientos de desconexión y manipulación autorizada; no se abren fuentes ni se improvisan trabajos eléctricos. En administración se preservan datos y se prepara retorno antes de cambiar permisos, red o firewall. El acceso remoto debe poder recuperarse mediante consola si una regla lo interrumpe.

### Contingencias razonadas

Registra al menos tres imprevistos: copia no utilizable, cambio de versión incompatible y falta de un equipo reservado. Para cada uno determina señal de detección, impacto, persona que decide y alternativa. La alternativa puede ser reprogramar o reducir alcance con aprobación del tutor; no consiste en presentar una prueba pendiente como realizada.

Define condiciones de parada: la validación de sintaxis falla, el destino de copia no es el previsto o una ruta contiene datos ajenos. El plan debe decir qué se conserva y cómo se vuelve al estado anterior. Una instantánea puede servir para ciertos ejercicios, pero no sustituye el procedimiento específico de recuperación de un directorio o base de datos.

**Entregables:** calendario con precedencias, fichas logísticas, matriz de responsabilidades, autorizaciones, inventario preventivo, contingencias y procedimientos versionados. **Aceptación:** ninguna tarea comienza sin sus dependencias y cada riesgo relevante tiene control y comprobación. **Revisión de solución:** retira temporalmente una VM del calendario sobre el papel y recalcula qué tareas pueden seguir y qué hito cambia; conserva el motivo de la decisión.

<a id="ra4"></a>
## RA4 · Seguir ejecución y gestionar una desviación

**Actividad `1713-RA4-A1`.** Aplica el plan de seguimiento a una práctica realizada o a una simulación explícita. Distingue los estados «previsto», «observado» y «sintético». Un servicio puede estar activo sin cumplir sus requisitos desde el cliente.

### Procedimiento de seguimiento

Antes de la sesión acuerda qué se revisa y cuándo: inicio, final de una tarea o hito que afecte a otras. El registro contiene tarea, responsable, estado, esfuerzo observado, producto, prueba y pendiente. No es necesario implantar una plataforma compleja; una tabla versionada puede servir si mantiene identificadores y decisiones.

Al completar DNS, consulta desde cliente nombres previstos y uno inexistente. Al completar archivos, ejecuta la matriz de identidades. Al completar HTTPS, usa nombre y confianza correctos. Al completar copia, restaura en otro destino y comprueba datos y permisos. Cada resultado se registra con contexto y fecha; una captura del proceso activo no sustituye esas operaciones.

### Caso de desviación con solución

Se proporciona una cronología sintética: incidente detectado a las 12:30; último punto recuperable de datos a las 09:00; servicio aceptado otra vez a las 13:15. El objetivo didáctico es perder como máximo dos horas de datos y recuperar servicio en una hora desde detección.

La pérdida potencial temporal es de tres horas y treinta minutos; supera el objetivo de dos horas. La recuperación del servicio tarda cuarenta y cinco minutos y sí cumple el objetivo de una hora definido en este caso. No se conoce cuántas operaciones se perdieron sin observar el contenido: la cronología permite calcular la distancia al punto recuperable.

El registro de desviación debe comunicar ambos resultados. «Se restauró en menos de una hora» no permite ocultar el incumplimiento de pérdida admisible. Una mejora razonable estudia frecuencia y éxito de las copias o mecanismos compatibles con la aplicación. Crear una tarea más frecuente sin supervisar fallos no garantiza por sí solo el nuevo objetivo.

### Intervención, comunicación y calidad

Prepara un cambio con motivo, alcance, copia, validación y retorno. Prueba en una copia del laboratorio cuando proceda y conserva la configuración anterior en una ubicación protegida. Si una actualización migra datos, explica si el retorno del código también revierte el esquema; no lo supongas.

Informa a los roles afectados del estado, impacto y siguiente paso. Presenta causa confirmada o pendiente, no una hipótesis como hecho. Después de corregir, repite la prueba que detectó el fallo y un caso de denegación o funcionamiento que podría haberse roto. Documenta resultados y pendientes de manera separada.

**Entregables:** procedimiento de seguimiento, bitácora de sesión, matriz de pruebas, desviación cuantificada, comunicación, plan de cambio, intervención y evaluación del conjunto. **Aceptación:** otra persona puede reconstruir qué cambió, por qué y qué evidencia apoya el cierre. **Caso negativo:** una prueba falla; el informe conserva el fallo y propone el siguiente paso, en lugar de sustituirlo por la salida esperada del manual.

<a id="ra5"></a>
## RA5 · Defender el proyecto y transferir información

**Actividad `1713-RA5-A1`.** Prepara una memoria, una defensa y una transferencia a otra persona. El anexo II imprime dos letras a); en esta actividad se usan las claves `a.1` para orden y método y `a.2` para comunicación verbal horizontal/vertical, además de b) para medios digitales y c) para términos de otras lenguas. Las claves son editoriales, no una renumeración oficial.

### Preparación de la defensa

Organiza la exposición como problema, requisitos, decisión, prueba y límite. Elige un ejemplo significativo en lugar de enumerar todas las herramientas. Debes poder explicar por qué una prueba demuestra un requisito y qué no demuestra. La memoria incluye índice, versiones, diagrama, decisiones, pruebas, recuperación y pendientes; los archivos editables permiten revisar cálculos y cambios.

Ensaya una explicación de noventa segundos para una persona usuaria y otra más técnica para un compañero. Cambia el detalle, manteniendo el mismo significado. Para el usuario interesa qué puede hacer, qué datos se recuperaron y cómo pedir ayuda; el compañero necesita dependencias, configuración y procedimiento. La comunicación vertical no es menos precisa: evita tecnicismos que impidan decidir, sin ocultar impacto o incertidumbre.

### Interacción observable

Realiza una reunión de revisión con roles de técnico, responsable y usuario si el entorno lo permite. Una persona pregunta por una prueba negativa, otra por recuperación y otra por un coste. Registra pregunta, respuesta, evidencia citada y corrección necesaria. No basta con leer diapositivas: la interacción exige comprender la pregunta y justificar una respuesta.

Prepara un ticket de incidente y un resumen de entrega con identificadores comunes. Utiliza control de versiones y una ubicación compartida autorizada. Las contraseñas y claves privadas se transmiten sólo por su canal protegido; no se añaden a la memoria para hacerla aparentemente autosuficiente. Un enlace a un secreto público no mejora la documentación.

### Términos técnicos y solución comentada

El glosario debe aplicar términos como `backup`, `restore`, `throughput`, `latency`, `least privilege` y `rollback` a decisiones concretas. Explicar `backup` exige distinguir copia disponible y recuperación comprobada; `rollback` debe indicar qué estado vuelve y qué datos podrían retroceder. El uso de una palabra inglesa sin comprenderla no aporta evidencia del criterio.

Pregunta modelo: «¿Por qué el lector no debe escribir?». Una respuesta defendible relaciona requisito y grupo, identifica la sesión utilizada y muestra la prueba denegada; no afirma simplemente que «Linux es seguro». Pregunta modelo: «¿Qué pasa si falta el DNS?». La respuesta identifica servicios dependientes, método de diagnóstico y procedimiento de recuperación previsto, sin atribuir alta disponibilidad que no se haya diseñado.

**Entregables:** guion, memoria, presentación, registro de interacción, ticket digital, procedimiento de transferencia y glosario aplicado. **Aceptación:** la exposición permite reconstruir la decisión, responde a preguntas con evidencia y distingue hecho, hipótesis y pendiente. Si no existe público o tutoría para observar la interacción, conserva el ensayo y marca esa parte como pendiente, sin declararla realizada.

## Rúbrica didáctica y cierre por criterio

La revisión puede utilizar cuatro descriptores: sin evidencia, evidencia parcial, comportamiento demostrado y justificación autónoma con límites. Se aplican a cada criterio y producto según la programación docente; aquí no se fijan pesos oficiales ni un umbral académico de superación.

Antes de cerrar, recorre la [matriz de alineación](05-alineacion-ra.md). Comprueba que el expediente contiene evidencia diferenciable para todos los criterios de cada RA. Una misma acta puede apoyar varios, pero cada conclusión debe señalar qué parte demuestra el criterio. Si un resultado necesita ejecución física, datos de una empresa real o una interacción observada, indica lo que aún falta.

Una revisión final por otra persona debe permitir localizar requisitos, decisiones, versiones y pruebas sin haber asistido a la práctica. Esa persona identifica un pendiente y reproduce una comprobación segura en el laboratorio cuando esté disponible. Las dudas de interpretación sirven para mejorar el procedimiento y la memoria.

## Referencias

- [Real Decreto 499/2024, anexo II: Proyecto intermodular de grado medio](https://www.boe.es/eli/es/rd/2024/05/21/499).
- [Currículo de SMR en Madrid y organización del proyecto](../../docs/curriculo-madrid.md).
- [Memoria modelo y defensa técnica](04-memoria-modelo-y-defensa-tecnica.md).
- [Plantillas de memoria, pruebas y cambios](../../recursos/README.md).
