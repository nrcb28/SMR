# Redes locales · alineación con resultados de aprendizaje

[Índice del módulo](README.md) · [Retos por RA](10-retos-por-ra.md) · [Datos trazables](alineacion-ra.json)

## Fuente y alcance

La numeración y los enunciados de los 6 RA se toman del [anexo I del RD 1691/2007](https://www.boe.es/eli/es/rd/2007/12/14/1691), módulo 0225. Se conservan sus 51 criterios y letras. Consulta normativa: 09/11/2026. La organización actual del ciclo y sus módulos transversales se explica en el [currículo de Madrid](../../docs/curriculo-madrid.md).

Los enunciados RA que aparecen en las citas son transcripción normativa con espacios normalizados. Los resúmenes CE, actividades, evidencias y condiciones de aceptación de las tablas son elaboración didáctica propia; sirven para preparar y revisar el trabajo, sin modificar la norma ni fijar la calificación del centro.

La cobertura de una fila significa que existe material y un reto para trabajar ese criterio. La adquisición requiere evidencia real y revisión en las condiciones de la programación. Distingue ejecución propia, observación supervisada, simulación y pendiente de equipamiento. Una salida esperada escrita en la guía no es un resultado obtenido por el estudiante.

## Cómo usar la matriz

1. Identifica el RA y lee su enunciado completo; después localiza los materiales de preparación.
2. Realiza el reto enlazado desde un estado inicial conocido y con el equipamiento que necesita.
3. Conserva un artefacto por criterio o un artefacto común con referencias claras a las letras que demuestra.
4. Compara el resultado real con la condición de aceptación y registra qué falta, sin copiar la expectativa como evidencia.
5. Repite sólo la operación pendiente o incorrecta y documenta recuperación, cambios y límites.

Un mismo dossier puede responder a varios criterios, siempre que se señale dónde se observa cada uno. Por ejemplo, una configuración y un registro de cliente se complementan: el primero declara la intención y el segundo muestra una condición del uso. No son intercambiables.

## Carencias curriculares que cierra esta ampliación

Las guías previas profundizan en direccionamiento, conmutación y análisis. Los retos RA añaden la evidencia de despliegue físico: canalizaciones, armario, paneles, tomas, etiquetado y pruebas por enlace; terminaciones de cobre y fibra; instalación de adaptadores/AP; y observación preventiva. VLSM o una captura de Wireshark aportan conocimientos importantes, pero no demuestran por sí solos esos montajes.

La parte de radio exige condiciones de dispositivo, posición y entorno. La prevención se prepara antes del montaje y se observa durante él, incluida la retirada selectiva de residuos. Si el centro no dispone de un kit de fibra o certificador, se identifica qué trabajo preparatorio sí se ha hecho y qué operación o alcance de prueba queda pendiente.

<a id="ra1"></a>
## RA1 · Dossier físico y lógico de un aula de seis puestos

> Reconoce la estructura de redes locales cableadas analizando las características de entornos de aplicación y describiendo la funcionalidad de sus componentes.

La lectura de este RA empieza en las necesidades del espacio. El resultado combina reconocimiento y representación: un inventario sin conexiones no es un mapa y una lista de IP no sustituye al plano físico. La comparación de estructuras obliga a contar los puertos de puestos, servicios y enlaces entre equipos, además de explicar qué ocurre al fallar un elemento. El dossier sirve después como entrada del montaje; todavía no acredita que se haya realizado ese montaje.

**Actividad desarrollada:** [`0225-RA1-A1`](10-retos-por-ra.md#ra1).

**Preparación:** [01-fundamentos.md](01-fundamentos.md), [06-conmutacion-y-diseno-segmentado.md](06-conmutacion-y-diseno-segmentado.md), [10-retos-por-ra.md](10-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Explicar el funcionamiento de una LAN | Recorrido de una comunicación puesto–recurso, anotado por capas | Relaciona trama, dirección, conmutación y servicio sin confundirlos. |
| b) | Distinguir tipos de redes por alcance y uso | Comparación de LAN, enlace entre dependencias y salida exterior | Clasifica cada escenario y explica qué necesidad satisface. |
| c) | Identificar componentes y su función | Inventario de tomas, paneles, adaptadores, switch, AP y servidor | Cada componente tiene función, conexiones y dependencia identificadas. |
| d) | Clasificar medios de transmisión | Tabla de cobre, fibra y radio con conectores y limitaciones | Justifica la elección con entorno y ficha técnica, sin mezclar formato y protocolo. |
| e) | Reconocer el mapa físico | Plano con puestos, armario, recorridos y extremos | Permite localizar una conexión sin deducirla del direccionamiento IP. |
| f) | Representar el mapa mediante una aplicación | Diagrama editable con leyenda, cotas o escala y etiquetas | El archivo se abre y conserva todos los extremos y cambios del diseño. |
| g) | Distinguir topologías de red | Comparativa de estrella y enlace entre switches | Explica recorrido, dominio de fallo y capacidad compartida. |
| h) | Proponer estructuras alternativas | Dos diseños comparados frente a puertos, coste y crecimiento | La alternativa satisface requisitos y contabiliza servicios y uplinks. |

El reto RA1 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

<a id="ra2"></a>
## RA2 · Maqueta de cableado, dos tomas y panel de parcheo

> Despliega el cableado de una red local interpretando especificaciones y aplicando técnicas de montaje.

El verbo desplegar exige una actuación sobre la instalación o maqueta autorizada. La documentación prepara y explica, pero no convierte un dibujo en una canalización montada. También importa el alcance de los instrumentos: un mapa de hilos puede detectar una terminación incorrecta y no certifica automáticamente la categoría del enlace. Conserva informes unidos a la identificación de cada toma y registra como pendiente la operación física que no se haya podido realizar.

**Actividad desarrollada:** [`0225-RA2-A1`](10-retos-por-ra.md#ra2).

**Preparación:** [02-guia-tecnica.md](02-guia-tecnica.md), [03-practicas.md](03-practicas.md), [10-retos-por-ra.md](10-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Relacionar funcionamiento de LAN y despliegue | Esquema del trayecto que se va a instalar | El plan de tendido responde al funcionamiento y necesidades del segmento. |
| b) | Identificar la red del montaje | Ficha del tipo de red y su alcance en la maqueta | No atribuye routing o radio a componentes que no los implementan. |
| c) | Diferenciar medios antes de instalar | Selección de medio, producto y herramientas por enlace | El medio elegido y sus terminaciones son compatibles con el entorno. |
| d) | Interpretar categoría, recorrido y soporte | Ficha de cableado con canalización, longitudes y restricciones del fabricante | Las decisiones corresponden al producto y al espacio, con supuestos visibles. |
| e) | Seleccionar y montar canalizaciones | Registro de montaje supervisado y fijaciones de la bancada | La canalización queda estable y mantenible, sin intervenir instalaciones ajenas. |
| f) | Montar armario y accesorios | Observación del bastidor, fijación, organización y ventilación | Respeta montaje del fabricante y manipulación segura de cargas. |
| g) | Terminar tomas y paneles | Fichas de terminación y fotografías autorizadas con sus identificadores | Los dos extremos mantienen el esquema y la técnica del producto. |
| h) | Probar los enlaces toma–panel | Resultado por enlace, instrumento, modalidad y límite de la prueba | La prueba corresponde a ese enlace y no se presenta continuidad como certificación. |
| i) | Etiquetar cables y tomas | Tabla de etiquetas concordante con plano y bancada | Cada identificador permite encontrar origen y destino sin ambigüedad. |
| j) | Mantener calidad y seguridad | Checklist de ejecución, revisión y desviaciones corregidas | La instalación supera su aceptación y la observación preventiva del centro. |

El reto RA2 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

<a id="ra3"></a>
## RA3 · Interconexión de equipos con terminaciones de cobre y fibra

> Interconecta equipos en redes locales cableadas describiendo estándares de cableado y aplicando técnicas de montaje de conectores.

Este RA añade al tendido la interconexión de equipos y la aplicación de técnicas de conectores. El criterio c incluye cobre y fibra; una VM no aporta esa evidencia. La actividad permite preparar la técnica y observar una demostración, pero debe distinguirlo de una ejecución propia supervisada. La comprobación combina estado físico y comunicación; un enlace activo o una respuesta ICMP, por separado, no describen toda la calidad del montaje.

**Actividad desarrollada:** [`0225-RA3-A1`](10-retos-por-ra.md#ra3).

**Preparación:** [01-fundamentos.md](01-fundamentos.md), [02-guia-tecnica.md](02-guia-tecnica.md), [10-retos-por-ra.md](10-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Interpretar el plan lógico de montaje | Plan anotado con puertos, conexiones y segmentos | Las conexiones ejecutadas corresponden al plan y a sus cambios autorizados. |
| b) | Montar adaptadores de red | Registro de instalación, controlador y reconocimiento del adaptador | El equipo reconoce la interfaz correcta y su compatibilidad está documentada. |
| c) | Montar conectores en cobre y fibra | Ficha observada de terminación en ambos medios y prueba prevista | La técnica y el resultado corresponden al kit; enchufar un latiguillo no se declara terminación. |
| d) | Instalar conmutadores en el armario | Registro de fijación, espacio y ventilación del switch | La instalación respeta el procedimiento y no carga peso sobre conectores. |
| e) | Conectar switch y paneles | Tabla puerto–latiguillo–panel–toma | El recorrido físico coincide con las etiquetas y el diagrama final. |
| f) | Verificar conectividad de la instalación | Matriz de enlace, dirección y comunicación entre los extremos | Diferencia prueba física, IP y servicio y localiza la capa que falla. |
| g) | Aplicar calidad al montaje | Revisión de acabado, pruebas y correcciones | La bancada queda ordenada y sus resultados son trazables al enlace probado. |

El reto RA3 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

<a id="ra4"></a>
## RA4 · Red mixta Wi-Fi y VLAN con política de acceso

> Instala equipos en red, describiendo sus prestaciones y aplicando técnicas de montaje.

La instalación exige comprobar lo que permiten equipos, clientes y software. Las VLAN necesitan una implementación y una prueba; un diagrama de colores no basta. La radio requiere observaciones en posiciones y con dispositivos reales cuando se pretenda evidenciar cobertura. Si se utiliza un simulador para la parte lógica, su alcance se declara y las operaciones de radio quedan pendientes. El diseño controla también gestión, autenticación y relación entre DHCP, AP y router.

**Actividad desarrollada:** [`0225-RA4-A1`](10-retos-por-ra.md#ra4).

**Preparación:** [02-guia-tecnica.md](02-guia-tecnica.md), [06-conmutacion-y-diseno-segmentado.md](06-conmutacion-y-diseno-segmentado.md), [07-ingenieria-wifi-y-capacidad.md](07-ingenieria-wifi-y-capacidad.md), [10-retos-por-ra.md](10-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Caracterizar la red inalámbrica | Ficha de bandas, capacidades, medio compartido y necesidades | Relaciona prestaciones con equipo y entorno, no sólo con velocidad anunciada. |
| b) | Distinguir modos de funcionamiento | Comparativa AP, cliente y funciones de router disponibles | Identifica qué equipo hace puente, routing, NAT o DHCP en el escenario. |
| c) | Instalar adaptadores y AP | Registro de montaje y reconocimiento de dos tipos de cliente | Los equipos y controladores utilizados corresponden al diseño real. |
| d) | Configurar modo y parámetros iniciales | Configuración saneada de SSID, modo, banda y canal | Los valores son compatibles con dispositivos y regulación aplicable. |
| e) | Comprobar conectividad entre dispositivos | Matriz de asociación, IP y acceso permitido con varios clientes | Distingue asociación de acceso al recurso y registra fallos por dispositivo. |
| f) | Instalar software de los equipos | Versiones, procedencia y comprobación de controlador/utilidad | El software soportado reconoce el equipo sin desactivar controles para ocultar fallos. |
| g) | Identificar protocolos empleados | Esquema de Wi-Fi, direccionamiento, autenticación y servicios | Relaciona cada protocolo con la función que demuestra la prueba. |
| h) | Configurar parámetros de red | Tabla de IP, prefijos, VLAN, DNS y gestión efectivos | No introduce gateways ficticios ni duplicados; cada parámetro responde al plan. |
| i) | Aplicar seguridad básica | Política de autenticación, aislamiento y acceso de gestión | Identidades y orígenes no autorizados se rechazan con una prueba controlada. |
| j) | Crear y configurar VLAN | Configuración de puertos y prueba de pertenencia/aislamiento | El equipo o simulador implementa VLAN y su comportamiento coincide con el diseño. |

El reto RA4 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

<a id="ra5"></a>
## RA5 · Expediente de mantenimiento con fallo físico y lógico

> Mantiene una red local interpretando recomendaciones de los fabricantes de hardware o software y estableciendo la relación entre disfunciones y sus causas.

La actividad parte de una línea base que permita comparar. Se introducen fallos sólo en la bancada prevista y sin generar bucles ni interrupciones en la red del centro. Corregir el enlace puede revelar otro problema de nombres o aplicación: el informe separa causas y no atribuye todos los síntomas a una primera reparación. La memoria conserva por qué se sustituyó un componente o se cambió software, y qué prueba confirma la recuperación.

**Actividad desarrollada:** [`0225-RA5-A1`](10-retos-por-ra.md#ra5).

**Preparación:** [04-diagnostico-y-evaluacion.md](04-diagnostico-y-evaluacion.md), [08-analisis-de-protocolos-y-laboratorios.md](08-analisis-de-protocolos-y-laboratorios.md), [10-retos-por-ra.md](10-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Identificar anomalías e incidencias | Ticket con síntoma, alcance, momento y línea base | Define un comportamiento reproducible y el servicio esperado. |
| b) | Separar hipótesis hardware/software | Árbol de diagnóstico y pruebas discriminantes | Cada prueba reduce alternativas y evita cambiar varias variables a la vez. |
| c) | Observar indicadores visuales | Registro del estado de puerto y LED con su significado documentado | Interpreta el indicador del fabricante sin concluir salud completa por una luz. |
| d) | Comprobar protocolos | Consultas y capturas limitadas al tráfico propio | Distingue solicitud, respuesta, error y límites de la observación. |
| e) | Localizar la causa | Evidencia antes/después y alternativas descartadas | La causa explica el síntoma y se confirma con un cambio controlado. |
| f) | Restituir mediante sustitución física | Registro del elemento de formación cambiado y prueba repetida | La sustitución identificada recupera su función sin ocultar otro fallo. |
| g) | Corregir la disfunción de software | Cambio de configuración o reinstalación justificada y recuperación | Conserva datos y estado previo; el comportamiento vuelve a la línea base. |
| h) | Elaborar informe de incidencia | Expediente con causa, intervención, pruebas y prevención | Otra persona puede reconstruir la reparación y sus límites. |

El reto RA5 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

<a id="ra6"></a>
## RA6 · Plan preventivo aplicado y cierre ambiental de la bancada

> Cumple las normas de prevención de riesgos laborales y de protección ambiental, identificando los riesgos asociados, las medidas y equipos para prevenirlos.

La prevención se prepara antes de las operaciones de montaje y se verifica mientras se realizan y al cerrar. Una tabla escrita demuestra análisis; para el criterio de operar se requiere observación de esa actuación en condiciones autorizadas. El método de peligrosidad del aula es didáctico y no sustituye la evaluación profesional del puesto. La falta de herramienta, formación o protección obliga a parar y solicitar supervisión, dejando trazable lo pendiente.

**Actividad desarrollada:** [`0225-RA6-A1`](10-retos-por-ra.md#ra6).

**Preparación:** [03-practicas.md](03-practicas.md), [10-retos-por-ra.md](10-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Identificar riesgos y peligrosidad de tareas concretas | Tabla tarea–material–peligro–daño–control | Relaciona corte, fijación, carga, paso y fibra con el procedimiento autorizado. |
| b) | Operar respetando normas de seguridad | Lista de observación supervisada de herramientas y equipo | Se aplican instrucciones y condiciones de parada durante la operación real. |
| c) | Reconocer causas frecuentes de accidente | Análisis de situaciones de la bancada | Explica causas y medidas sin provocar un accidente para demostrarlo. |
| d) | Describir protecciones y EPI | Selección razonada por herramienta y tarea | Identifica resguardos, protecciones y EPI apropiados al riesgo previsto. |
| e) | Relacionar manipulación y protección | Secuencia de trabajo con controles y responsables | El control se utiliza en el momento de riesgo y no sustituye otros medios necesarios. |
| f) | Reconocer fuentes de contaminación | Inventario de residuos y posibles impactos del montaje | Identifica recortes, fibra, componentes y envases sin mezclarlos por conveniencia. |
| g) | Clasificar residuos para retirada | Registro de separación y circuito autorizado del centro | Los residuos se depositan y retiran por el procedimiento correspondiente. |
| h) | Valorar orden y limpieza como prevención | Inspección inicial/final con incidencias corregidas | No quedan fragmentos, herramientas o cables que generen peligro en la zona. |

El reto RA6 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

## Instrumentos de revisión y recuperación

La revisión puede combinar observación del procedimiento, dossier, archivos saneados, demostración desde cliente y preguntas sobre decisiones. El estudiante señala en qué artefacto se observa cada criterio. El docente aplica las condiciones y los instrumentos de su programación; esta matriz no asigna pesos oficiales ni transforma una simulación en una operación física.

Usa la [matriz de pruebas](../../recursos/plantillas/matriz-de-pruebas.md) y la [memoria de práctica](../../recursos/plantillas/memoria-practica.md). Registra fecha, entorno, resultado obtenido, evidencia y revisión pendiente. Si no has ejecutado una operación, conserva el diseño y explica qué falta para probarla. Una recuperación de aprendizaje concreta pide, por ejemplo, repetir una terminación, demostrar un modo de acceso o verificar una identidad distinta, no rehacer todo el trabajo sin diagnosticar la carencia.

Antes de compartir, elimina contraseñas, claves privadas, TSIG, mensajes y datos reales. Conserva configuraciones con secretos saneados y evidencias sintéticas. No ejecutes pruebas sobre redes ajenas para rellenar una fila; el alcance del laboratorio y la autorización preceden a la actividad.

## Lectura de los datos trazables

El archivo [alineacion-ra.json](alineacion-ra.json) contiene 6 RA, 51 CE y una actividad desarrollada por RA. Cada criterio indica resumen, identificador de actividad, evidencia y aceptación. Las rutas de ese JSON parten de la raíz del repositorio; las de esta guía son relativas a su carpeta. El validador global compara números, enunciados, letras y relaciones con el referente normativo local.

Los datos describen oportunidades de aprendizaje y trazabilidad editorial. Para acreditar trabajo individual o en grupo hacen falta resultados y contribuciones observados. Conserva especialmente esa distinción en actividades con dos participantes, operaciones físicas y conexiones a redes públicas.
