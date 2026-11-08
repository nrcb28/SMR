# Sostenibilidad en la operación de sistemas microinformáticos

## 1. Alcance y decisiones

La sostenibilidad estudia cómo una actividad satisface necesidades teniendo en cuenta recursos, efectos ambientales, personas y continuidad económica. En un servicio informático, no se limita a reducir la factura eléctrica: incluye extracción de materiales, fabricación, transporte, reparación, accesibilidad, condiciones de trabajo y tratamiento de residuos.

Antes de calcular, delimita el sistema. ¿Analizas sólo doce ordenadores o también monitores, switches, servidor, climatización y copias? ¿El periodo es una semana lectiva o un año completo? ¿Comparas equipos que realizan la misma tarea y prestan el mismo servicio? Sin límites equivalentes, una alternativa puede parecer mejor simplemente porque has excluido una parte de su impacto.

Relaciona las decisiones con necesidades concretas. Comprar un equipo nuevo puede reducir energía durante el uso, pero incorpora el impacto de producirlo y retirar el anterior. Reparar puede ser preferible si conserva seguridad, prestaciones suficientes y soporte; no lo será si mantiene un equipo incapaz de ejecutar las herramientas necesarias de forma segura. Justifica cada caso con evidencia.

## 2. Ciclo de vida y economía circular

El ciclo de vida incluye materias primas, fabricación, distribución, uso, mantenimiento y fin de vida. Un análisis formal de ciclo de vida exige metodología, datos y límites específicos; una práctica de SMR puede comparar aspectos seleccionados, pero no debe presentarse como certificación ambiental completa.

La economía circular busca conservar utilidad y valor de productos y materiales. En informática implica prevenir compras innecesarias, compartir cuando resulte viable, mantener, reparar, ampliar, reutilizar y gestionar residuos a través de los canales adecuados. Reciclar recupera materiales, pero normalmente no conserva todo el valor funcional de un equipo reparable.

Ejemplo de decisión: un ordenador con almacenamiento defectuoso, memoria ampliable y sistema soportado puede recuperar utilidad al sustituir su unidad por otra compatible. Antes de hacerlo, verifica compatibilidad, coste, garantía, copia, tratamiento del soporte retirado y pruebas. “Funciona al encender” no basta: evalúa estabilidad, necesidades del usuario y actualizaciones del sistema.

Para compras, compara disponibilidad de piezas, acceso a batería y almacenamiento, documentación de reparación, periodo de soporte, garantía, consumo y accesibilidad. Una certificación o etiqueta puede aportar información sobre aspectos concretos; registra su alcance y vigencia. No conviertas una afirmación comercial genérica de “ecológico” en una conclusión técnica.

## 3. Potencia y energía

La **potencia** es la tasa de transferencia de energía y se expresa en vatios, W. La **energía** acumulada suele expresarse en Wh o kWh. Para potencia constante:

```text
E (kWh) = P (W) × tiempo (h) / 1000
```

Si un ordenador consume 90 W durante ocho horas, utiliza 0,72 kWh. Si el consumo varía, calcula la suma por estados o mide directamente la energía durante un periodo representativo. Un medidor enchufable adecuado registra el conjunto conectado; identifica si incluye monitor y periféricos para no contarlos después otra vez.

La potencia nominal de una fuente de 500 W indica capacidad de suministro en sus condiciones especificadas, no que el ordenador consuma constantemente 500 W. Tampoco el TDP de una CPU representa el consumo total del equipo desde el enchufe. No mezcles potencia de un componente con energía medida del conjunto.

La expresión con un factor de carga sirve sólo si defines la potencia de referencia:

```text
E = P_referencia × factor_de_carga_medio × tiempo / 1000
```

Es una aproximación y el factor debe proceder de datos o hipótesis justificadas. No multipliques un consumo medio ya medido por otro factor de carga: lo reducirías dos veces. Para potencia variable, es preferible registrar estados de actividad, reposo y apagado con duraciones separadas.

La energía anual necesita un calendario realista: días lectivos, vacaciones, horarios y estados fuera de uso. Un equipo apagado puede seguir consumiendo por alimentación de espera; un puerto USB con carga o un periférico independiente puede mantener consumo. Describe qué apagado se ha medido y no asumas siempre cero.

## 4. Gestión de energía sin perder servicio

Configura suspensión de pantalla y equipo según uso, compatibilidad y necesidades de acceso. La suspensión puede ahorrar energía en puestos de oficina, pero un servidor que debe ofrecer un servicio no puede suspenderse simplemente por inactividad de teclado. Define excepciones justificadas y comprueba actualizaciones, copias nocturnas y recuperación de sesión.

En un piloto, registra configuración previa, aplica la política a un equipo de prueba, mide consumo y comprueba que el trabajo se conserva. Si se utiliza Wake-on-LAN, revisa compatibilidad de hardware, configuración de firmware y exposición de red; no presupongas que siempre funcionará. Mantén un procedimiento para recuperar la disponibilidad tras un fallo de suspensión.

Consolidar servicios mediante virtualización puede aumentar aprovechamiento de un servidor y reducir máquinas físicas. Sin embargo, obliga a dimensionar RAM, almacenamiento, copias y recuperación del host. Un equipo sobrecargado puede empeorar servicio y generar sustituciones prematuras. Evalúa energía por servicio útil y disponibilidad, no sólo cantidad de máquinas virtuales.

## 5. PUE: uso y límites

PUE relaciona energía total de una instalación de centro de datos con energía de sus equipos IT, utilizando el mismo periodo y límites coherentes:

```text
PUE = energía total del centro de datos / energía de equipos IT
```

Si una instalación consume 12 000 kWh y sus equipos IT 8 000 kWh, PUE = 1,5. La energía adicional corresponde al resto de servicios incluidos en el límite, como alimentación y refrigeración. Es una relación adimensional, no un porcentaje.

No calcules PUE dividiendo el consumo de un ordenador de escritorio entre el de su CPU ni lo uses como “eficiencia de un portátil”. Tampoco permite deducir por sí solo emisiones, eficiencia del software o huella de fabricación. Dos instalaciones con PUE distinto pueden tener diferente clima, ocupación, mix eléctrico y servicio. Para la metodología formal consulta la referencia técnica aplicable y no presentes una estimación escolar como medición certificada.

## 6. Emisiones y factores de emisión

La estimación de emisiones de electricidad parte de energía y factor:

```text
Emisiones (kg CO2eq) = energía (kWh) × factor (kg CO2eq/kWh)
```

El factor cambia según año, fuente, comercializadora y metodología pertinente. Guarda documento, versión, año y unidad. El [MITECO publica factores y recursos de cálculo](https://www.miteco.gob.es/es/cambio-climatico/temas/registro-huella.html); hay que elegir los adecuados al inventario y ejercicio analizado. Un valor de ejemplo no debe etiquetarse como factor oficial español actual.

CO2eq permite expresar distintos gases según su efecto climático con una metodología determinada. Una estimación de emisiones del consumo eléctrico no cubre automáticamente fabricación, transporte ni fin de vida del equipo. Si sólo has medido energía de uso, titula el resultado como tal. No restes compensaciones para ocultar límites o falta de datos.

Una mejora debe comparar escenarios equivalentes. Si el cambio reduce 100 kWh pero amplía el horario o incorpora otro servidor, incluye esas variaciones. El efecto rebote aparece cuando la mayor eficiencia lleva a un uso superior que reduce el ahorro esperado. Presenta tanto valor absoluto como unidad funcional: kWh por jornada de servicio o por tarea, siempre explicando su alcance.

## 7. RAEE, soportes y trazabilidad

Los residuos de aparatos eléctricos y electrónicos requieren recogida y tratamiento específicos. En España, el [Real Decreto 110/2015](https://www.boe.es/eli/es/rd/2015/02/20/110/con) establece su marco de gestión; la [Comisión Europea explica el régimen WEEE](https://environment.ec.europa.eu/topics/waste-and-recycling/waste-electrical-and-electronic-equipment-weee_en). El tratamiento concreto depende de tipo de aparato, titular y canal autorizado.

Antes de retirar un equipo, distingue si aún puede reutilizarse o ya es residuo. Registra activo, motivo, componentes y autorización. Un soporte con datos no debe salir del control de la organización hasta completar el procedimiento de borrado o destrucción apropiado y guardar evidencia. Un borrado de archivos o formateo rápido no demuestra saneamiento de todas las celdas de un SSD.

Aplica el procedimiento del fabricante y la política de seguridad para el soporte concreto; verifica el resultado y documenta limitaciones. Si no puedes acreditar un saneamiento apropiado, escala la decisión a la persona responsable. No publiques números de serie vinculados a inventarios reales ni certificados con información de empresa.

Separa baterías dañadas y otros elementos conforme al procedimiento de seguridad y al canal de gestión; no las perfores ni manipules para intentar recuperarlas. No desmontes fuentes de alimentación o equipos con riesgos eléctricos fuera de la competencia y medios del taller. La prioridad ambiental no justifica exponer a personas a un riesgo no controlado.

## 8. Dimensión social y gobierno

Una política sostenible también considera ergonomía, accesibilidad, formación y carga de trabajo. Un equipo de bajo consumo que excluye una tecnología de apoyo necesaria no satisface el servicio. Incluir a las personas usuarias en el piloto evita cambios que trasladan esfuerzo a quienes tienen menos recursos para adaptarse.

Para que las mejoras continúen, asigna responsables, calendario y métricas. Un informe sin responsable de apagar equipos fuera de uso puede quedarse en una recomendación. Define quién revisa contratos de soporte, quién autoriza retiradas y dónde se conservan evidencias. Evita comprar instrumental o servicios innecesarios sólo para obtener indicadores: selecciona datos proporcionales al objetivo.

[Prácticas y evaluación](02-practicas-y-evaluacion.md) · [Índice del módulo](README.md)
