# Retos de Redes locales por resultados de aprendizaje

[Alineación y criterios](09-alineacion-ra.md) · [Índice del módulo](README.md) · [Laboratorio común](../../docs/laboratorio.md)

## Cómo realizar y documentar estos retos

Los seis retos corresponden a los seis RA del módulo 0225. Su numeración sigue el [anexo I del RD 1691/2007](https://www.boe.es/eli/es/rd/2007/12/14/1691), no el orden de los capítulos del repositorio. Las actividades, soluciones, instrumentos y condiciones de aceptación son propuestas didácticas propias; el centro determina la evaluación oficial.

Prepara una carpeta de evidencias por RA con diseño, versión, entradas, procedimiento, resultados reales, incidencias y recuperación. Una fotografía de un montaje debe poder relacionarse con su plano y etiqueta. Una captura de conectividad necesita indicar origen, destino, interfaz y servicio. Conserva sólo información sintética o autorizada.

Una VM permite comprobar configuración lógica, pero no demuestra que hayas montado una canalización, terminado una fibra o utilizado con seguridad una herramienta. Identifica cada evidencia como **ejecución propia**, **observación supervisada**, **simulación** o **pendiente de equipamiento**. El material no convierte esos estados diferentes en una calificación equivalente. Antes del montaje consulta también el reto RA6 y sus condiciones de parada.

<a id="ra1"></a>
## RA1 · Del espacio real al modelo de red

**Actividad:** `0225-RA1-A1`, dossier comparado de un aula de seis puestos. Cubre los criterios a–h. El aula ficticia necesita puestos cableados, un AP y un recurso de archivos; el plano de ejemplo debe sustituirse por un espacio del centro autorizado o por una maqueta declarada.

### Preparación y procedimiento

1. Define qué se quiere comunicar y con qué alcance: LAN del aula, conexión entre dependencias y salida a otra red. Separa necesidad de usuario y tecnología elegida. Un grupo de trabajo no es un tipo de cable ni una topología física.
2. Haz inventario de puestos, adaptadores, tomas, paneles, switches, AP, medios y puntos de alimentación. Para cada elemento explica su función y sus conexiones. Una tabla MAC del switch y una tabla de rutas resuelven problemas distintos.
3. Dibuja un mapa físico con sala, armario, recorridos y ambos extremos de cada enlace. Usa una aplicación de diagramas, Draw u otra herramienta disponible; conserva el archivo editable, escala o cotas y una leyenda. Un dibujo a mano puede servir para reconocimiento inicial, pero añade representación mediante aplicación para evidenciar el criterio f.
4. Dibuja por separado el mapa lógico: segmentos, VLAN previstas, direcciones y servicios. Clasifica los medios observados y justifica elección por entorno, conectores, distancias y prestaciones que puedas acreditar con ficha técnica.
5. Compara dos estructuras: una estrella con switch central y una alternativa con enlace entre dos switches. Explica costes de puertos, dependencia del uplink y efecto de un fallo. No instales un bucle para demostrar una topología en una red de trabajo.

### Pruebas y solución razonada

Selecciona un puesto y sigue su camino hasta el recurso: latiguillo, toma, enlace permanente, panel, latiguillo de armario, switch y destino. Un plano que omite paneles puede servir como esquema lógico, pero no permite localizar físicamente un enlace. Pide a otra persona que encuentre la toma usando sólo el dossier; registra ambigüedades y corrige etiquetas.

Para seis puestos y un AP se requieren siete conexiones de acceso más las conexiones de servicios y uplinks que defina el diseño. No concluyas que un switch de ocho puertos basta sin contar todos los extremos y crecimiento. La alternativa de dos switches no elimina la necesidad de contar el enlace entre ellos y su capacidad compartida.

**Entrega:** inventario funcional, clasificación de redes/medios, plano físico editable, plano lógico y comparación de estructuras. **Aceptación:** cada conexión del plano tiene dos extremos identificados y cada componente una función explicada; las alternativas se comparan frente a requisitos. **Caso negativo:** una toma sin etiqueta se marca como no trazable, en lugar de adivinar su destino. No se configura equipamiento en este reto, por lo que el retorno consiste en retirar únicamente marcas temporales autorizadas.

<a id="ra2"></a>
## RA2 · Despliegue físico con trazabilidad y control de calidad

**Actividad:** `0225-RA2-A1`, maqueta de dos tomas y un panel de parcheo. Cubre a–j. Necesita materiales y herramientas del centro, superficie de montaje autorizada, guía de instalación del fabricante y supervisión. Si falta equipamiento, prepara el diseño y deja la ejecución física pendiente.

### Plan de montaje

Identifica categoría y construcción del cable, compatibilidad de módulos y panel, esquema de terminación elegido, recorrido, soporte, radios de curvatura y condiciones de instalación. Consulta límites del producto y normas aplicables al proyecto: no universalices una separación eléctrica o una fijación sin considerar su contexto. La categoría escrita en la cubierta no demuestra que todo el enlace instalado mantenga ese desempeño.

Prepara una ficha por enlace con identificador, origen, destino, longitud prevista, medio, módulo y criterio de aceptación. En una maqueta ficticia, `AULA-A-T01` puede llegar a `R01-PP01-P01`; ambos códigos deben aparecer en plano y etiquetas. Deja reservas ordenadas sin aplastar pares ni utilizar el cable como elemento de soporte de otros objetos.

### Secuencia de ejecución

1. Revisa zona de trabajo, herramientas y medidas de RA6 antes de cortar o perforar. No taladres paredes ni intervengas en instalaciones energizadas como parte improvisada de un ejercicio.
2. Selecciona y monta canalización y accesorios según soporte y especificación de la maqueta. Comprueba fijación, acabado y posibilidad de mantenimiento. Si sólo dibujas la canalización, regístralo como diseño, no como montaje realizado.
3. Instala el armario o bastidor de formación y sus accesorios bajo el procedimiento del centro. Comprueba estabilidad, accesibilidad y organización. La colocación de un equipo pesado requiere el método de manipulación y ayuda previsto.
4. Tiende los dos enlaces y termina tomas/paneles con herramientas y esquema compatibles. Conserva el trenzado lo más próximo posible a la terminación según la guía del fabricante; evita pellizcos y esfuerzos de tracción sobre módulos.
5. Etiqueta ambos extremos y registra cualquier cambio de recorrido o longitud. El plano final representa el montaje real y conserva las desviaciones del plan.
6. Prueba cada línea entre toma y panel. Guarda identificador del instrumento, prueba aplicada y resultado. Una prueba de continuidad o mapa de hilos no equivale a una certificación de categoría del enlace.

### Resultado esperado, fallos y retorno

Las dos líneas deben corresponder al esquema y superar la prueba definida para el instrumento disponible. Si el equipo sólo comprueba continuidad, declara ese alcance; si se dispone de certificador, selecciona el estándar y tipo de enlace correctos y conserva el informe sin alterar su identificación. Un «PASS» de otra toma no prueba ésta.

En una maqueta, el docente puede preparar una terminación incorrecta o una etiqueta intercambiada sin generar riesgo. Compara síntoma y prueba antes de rehacer todo el tendido. Corrige sólo la parte identificada, vuelve a probar y registra antes/después. Una pareja separada puede requerir instrumentos que no ofrezca un comprobador muy básico; explica ese límite.

**Entrega:** plano conforme a obra, fichas de materiales, fotografías autorizadas, etiquetas y tabla de pruebas por enlace. **Aceptación:** trazabilidad completa y resultados coherentes con el alcance del instrumento, además de observación de calidad y seguridad. **Retorno:** desconecta y desmonta sólo la maqueta asignada, conserva material reutilizable y clasifica recortes; no alteres canalizaciones del edificio.

<a id="ra3"></a>
## RA3 · Montaje de interfaces y conexiones en cobre y fibra

**Actividad:** `0225-RA3-A1`, interconexión de dos puestos mediante una instalación documentada. Cubre a–g. El objetivo es convertir el esquema lógico en conexiones concretas y verificar que el montaje responde a ese esquema; no basta con conectar dos VMs a un switch virtual.

### Preparación

Reúne el plan de montaje, dos equipos de prácticas, adaptadores compatibles, switch, panel, latiguillos y material de conectores. Incluye una sesión específica de fibra con equipos y procedimiento del fabricante. Los fragmentos de fibra requieren gestión específica y nunca se mira un extremo óptico para comprobar si transmite. Aísla fuentes ópticas y aplica la supervisión y protección previstas.

Comprueba compatibilidad del adaptador: interfaz física, controlador, versión de SO, conector y prestaciones. Si es interno, sigue el procedimiento seguro del equipo; si es USB u otro externo, documenta por qué satisface el escenario. Conserva la evidencia de reconocimiento por el SO y su relación con el elemento físico.

### Montaje y comprobación

1. Localiza en el plan qué puerto corresponde a cada equipo y a cada panel. Identifica el recorrido sin confundir número de toma, posición del panel y puerto de switch.
2. Monta y verifica el adaptador en el equipo asignado. Registra interfaz y controlador, sin publicar identificadores innecesarios de un equipo real.
3. Termina conectores de cobre con herramienta y producto compatibles. Comprueba el mapa de hilos antes de conectarlo a equipos. No mezcles esquemas en extremos sin una finalidad y un tipo de enlace que lo justifiquen.
4. Realiza la práctica de montaje de conectores de fibra que autorice el centro, con el kit y la técnica previstos. Distingue terminación mecánica, fusión y uso de un latiguillo ya terminado. Enchufar un latiguillo de fábrica enseña conexión, pero no demuestra por sí solo haber terminado su conector.
5. Monta el switch en el bastidor de formación con su fijación y ventilación; conecta el panel mediante latiguillos identificados. Evita que los conectores sostengan peso o queden sometidos a tensión.
6. Comprueba enlace y conectividad por capas: estado físico, configuración IP coherente, vecinos y una comunicación de prueba. En la LAB base las IP siguen `.56.10/24` y `.56.20/24`, sin gateway en esa interfaz.

### Interpretación y solución

Un enlace físico activo no garantiza una IP correcta. Una IP correcta tampoco prueba que el conector tenga el desempeño previsto bajo carga. Combina pruebas físicas y lógicas, conservando qué demuestra cada una. Si el switch muestra enlace pero falla la comunicación, revisa VLAN, dirección, firewall y servicio antes de volver a crimpar.

La evidencia debe separar lo realmente montado por el estudiante de lo observado en una demostración. Para criterio c se prevén cobre y fibra; la ausencia de kit se registra como pendiente y no se oculta con una captura de una VM. Puedes entregar el análisis de procedimiento y riesgos como preparación, sin declarar ejecución inexistente.

**Entrega:** plan lógico anotado, reconocimiento de adaptadores, fichas de terminación de ambos medios, montaje de switch y matriz de conectividad. **Aceptación:** coincidencia entre plan, conexiones y pruebas, con técnica observada y calidad documentada. **Retorno:** desmontaje de la bancada autorizada, protección de puertos ópticos, retirada segura de fragmentos y restauración de la configuración de los equipos de formación.

<a id="ra4"></a>
## RA4 · Instalación Wi-Fi y VLAN con política comprobable

**Actividad:** `0225-RA4-A1`, red mixta de formación. Cubre a–j. Requiere un AP configurable, dos tipos de cliente cuando sea posible y un switch o simulador que implemente VLAN. Un adaptador virtual ordinario no demuestra cobertura de radio ni etiquetado real.

### Diseño y ejecución

Define SSID, modo de funcionamiento, seguridad compatible, red de gestión, VLAN y direccionamiento de la práctica. Elige banda/canal según equipos, entorno y regulación aplicable, y documenta la razón. No publiques la clave del SSID. Usa un secreto exclusivo y retíralo al terminar.

1. Inventaría AP y adaptadores, sus capacidades y software/controladores. Identifica diferencias entre modo de infraestructura, punto de acceso y funciones de router; no todo AP realiza NAT o DHCP.
2. Instala AP y adaptadores según la documentación del fabricante. Actualiza sólo mediante el procedimiento y ventana que autorice el centro, con copia y posibilidad de retorno.
3. Configura SSID y parámetros básicos, selecciona mecanismo de seguridad apropiado y desactiva servicios que no necesita el ejercicio. Una red abierta de demostración, si se utiliza para observar diferencias, permanece aislada y no maneja credenciales o datos reales.
4. Configura dos VLAN en la topología compatible. Identifica puertos de acceso y, si hace falta, trunk hacia AP o equipo de capa 3. La interfaz de administración debe seguir siendo accesible por el camino previsto.
5. Prueba asociación con distintos clientes, dirección, acceso al recurso permitido y denegación del tráfico no previsto. Si no existe routing entre VLAN, la ausencia de comunicación entre ellas puede ser el resultado correcto.
6. Repite en dos posiciones físicas autorizadas y registra condiciones: canal, ancho, distancia aproximada, obstáculos y carga. Usa [ingeniería Wi-Fi](07-ingenieria-wifi-y-capacidad.md) para interpretar RSSI, SNR y capacidad sin reducirlo todo a barras de señal.

### Solución y validación

Una asociación correcta no demuestra acceso a un servidor: pueden fallar DHCP, VLAN o firewall. Una transferencia lenta con señal alta puede depender de interferencia o tiempo de aire. Relaciona las pruebas con protocolos y parámetros concretos, incluyendo el adaptador y versión utilizados.

El criterio de VLAN necesita creación y configuración, no sólo un dibujo con dos colores. Conserva configuración saneada y una prueba de pertenencia/aislamiento. Elige una prueba negativa que responda al diseño, como una identidad no autorizada al SSID o un acceso intersegmento prohibido; no intentes redes ajenas.

**Entrega:** capacidades, software, parámetros sin secretos, topología/VLAN, justificación de seguridad y matriz de clientes/posiciones. **Aceptación:** asociación, comunicación autorizada y aislamiento coherentes; las funciones disponibles del equipo coinciden con lo afirmado. **Retorno:** restaura sólo los valores de la bancada, elimina el SSID temporal y comprueba que no permanecen DHCP o interfaces puente imprevistas.

<a id="ra5"></a>
## RA5 · Mantenimiento con dos fallos y una causa comprobada

**Actividad:** `0225-RA5-A1`, expediente de reparación. Cubre a–h. Prepara una red de formación funcional y conserva línea base de conexiones, versiones y pruebas. Un docente o compañero introduce, dentro del alcance autorizado, un fallo físico sencillo y otro lógico en momentos separados.

Un ejemplo apropiado de fallo físico es un latiguillo de formación identificado que no supera su prueba; uno lógico puede ser una dirección o VLAN incorrecta. No provoques bucles de broadcast, cortocircuitos ni interrupciones sobre la red del centro. Las secuencias sintéticas de los capítulos anteriores sirven para preparar hipótesis, pero no son evidencia de una reparación ejecutada.

### Investigación paso a paso

1. Describe el síntoma con equipo, momento, alcance y resultado esperado. Conserva mensajes, LEDs y estado del puerto; una captura posterior no reconstruye necesariamente el estado inicial.
2. Decide qué pruebas separan hardware y software. Comprueba enlace y mapa físico, luego dirección/ruta, protocolo y aplicación. Cambia una variable cada vez para poder atribuir efecto.
3. Consulta indicadores visuales del equipo y la documentación que explica su significado. Una luz de enlace no certifica ausencia de errores ni el funcionamiento de DNS.
4. Comprueba protocolos con comandos y capturas del tráfico propio, limitadas a LAB. Identifica si la petición sale, si llega respuesta y qué código o estado contiene.
5. Localiza la causa con evidencia y aplica sustitución del elemento de formación o corrección lógica necesaria. Si se reinstala software, justifica por qué y cómo se conservan configuración y datos.
6. Repite las mismas pruebas de línea base y una prueba de persistencia cuando proceda. Si hay más de un fallo, no declares cerrado todo el expediente al corregir sólo uno.

### Solución y cierre

Supón que cambiar un latiguillo restaura el enlace, pero la web sigue fallando por nombre. La primera reparación tiene evidencia física y no demuestra que todo el servicio esté sano. Comprueba dirección, resolución y aplicación antes de atribuir al cable el segundo síntoma. El informe distingue causas, cambios y dependencias.

**Entrega:** parte de incidencias, cronología, indicadores, hipótesis descartadas, elemento sustituido, cambio lógico y resultados antes/después. **Aceptación:** el razonamiento permite localizar una causa y la red recupera el comportamiento previsto sin ampliar permisos innecesarios. **Retorno:** conserva el componente defectuoso identificado para revisión docente y restaura el estado limpio del laboratorio, evitando reintroducirlo sin control.

<a id="ra6"></a>
## RA6 · Prevención y protección ambiental durante el trabajo

**Actividad:** `0225-RA6-A1`, plan preventivo aplicado a la bancada. Cubre a–h. Se prepara antes de RA2–RA4 y se completa con observación de su ejecución. Un listado genérico de riesgos no demuestra operación segura; el plan debe relacionarse con materiales y tareas concretas.

### Preparación y actuación

Elabora una tabla con tarea, peligro, daño posible, nivel de peligrosidad según el método didáctico elegido, medida, equipo de protección si procede y comprobación. Incluye corte/pelado, herramientas de impacto, fijación, manipulación de bastidor, latiguillos en zonas de paso y fibra. El método escolar no sustituye una evaluación profesional del puesto.

1. Revisa instrucciones de cada herramienta, estado, protecciones y superficie de trabajo. Retira la que no esté en condiciones y comunica la incidencia; no la repares de forma improvisada para continuar.
2. Identifica causas previsibles de accidente: herramienta inadecuada, mano en trayectoria de corte, cables de paso, soporte inestable o restos de fibra. Relaciona medidas concretas con cada causa.
3. Verifica elementos de seguridad de los equipos y la protección que corresponda a la tarea. El EPI se selecciona por riesgo y procedimiento, no como sustituto de organización, resguardos o eliminación del peligro.
4. Realiza una observación supervisada del montaje y anota desviaciones. Si el riesgo supera el alcance de formación, se detiene la tarea y se solicita supervisión. No se provoca un accidente para demostrar que un control funciona.
5. Identifica residuos y posibles fuentes de contaminación: recortes, componentes, envases y fragmentos de fibra. Prepara recipientes adecuados, separación y retirada por el circuito autorizado del centro; los residuos no se mezclan por conveniencia.
6. Deja la zona ordenada y comprueba que no hay conectores, fragmentos o herramientas en lugares de tránsito. El cierre del trabajo es parte de la prevención, no una tarea opcional posterior.

### Entrega y aceptación

Entrega evaluación didáctica, checklist previo, registro de observación y plan de residuos. El criterio se observa durante el uso de herramientas, además del documento. Si sólo se ha elaborado una tabla o visto una demostración, indica ese alcance; no marques como realizada una operación que no has ejecutado.

**Caso resuelto:** si aparece un cable atravesando un paso durante el tendido, la medida inmediata es detener y reorganizar el recorrido o protegerlo mediante el procedimiento autorizado. Es insuficiente escribir «andar con cuidado» y seguir trabajando. Después se revisa por qué el plan no reservó espacio y se corrige el diseño.

**Retorno:** banco despejado, residuos clasificados, equipos protegidos y estado final registrado. Para ampliar consulta [IPE I](../itinerario-personal-para-la-empleabilidad-i/README.md), las instrucciones del centro y [INSST](https://www.insst.es/), que permiten contrastar medidas sin inventar una lista universal de EPI.

## Cómo revisar el conjunto de evidencias

La [matriz RA/CE](09-alineacion-ra.md) relaciona los criterios con las actividades. Marca cada evidencia como obtenida, insuficiente o pendiente y explica la razón. Una corrección de un plano puede cerrar un criterio documental, pero no reemplaza una terminación física que estaba pendiente.

Para una revisión entre compañeros, intercambia el dossier y pide localizar una toma, interpretar una prueba y seguir una reparación. Si faltan datos, registra la incidencia de documentación y corrígela. La autonomía se demuestra explicando las decisiones y límites; no se mide únicamente por cantidad de capturas.

## Fuentes de trabajo

- [RD 1691/2007, anexo I, módulo 0225](https://www.boe.es/eli/es/rd/2007/12/14/1691): RA y criterios.
- [RD 499/2024](https://www.boe.es/eli/es/rd/2024/05/21/499): adaptación de la estructura del título.
- [INSST](https://www.insst.es/): prevención y selección de medidas según el trabajo.
- [Debian Reference](https://www.debian.org/doc/manuals/debian-reference/) y [Microsoft Learn](https://learn.microsoft.com/): configuración y observación de interfaces.
- Manuales del fabricante del cable, terminación, comprobador, AP y switch realmente utilizados: procedimientos y alcance de sus pruebas.
