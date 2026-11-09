# Medición, ciclo de vida y trazabilidad de equipos

[Índice](README.md) · [Tres casos resueltos](04-casos-de-decision-y-evaluacion.md)

## 1. Formular una pregunta con límites

Un estudio útil comienza por una pregunta específica: cuánta energía consume el aula en un periodo, cuánto reduce una política de suspensión o qué alternativa mantiene una función con menos recursos. “Medir sostenibilidad” es demasiado amplio para determinar instrumento, dato y conclusión. La dimensión ambiental debe relacionarse también con continuidad, accesibilidad, seguridad y condiciones de uso.

Define una unidad funcional. Para comparar puestos podría ser “proporcionar a doce personas las aplicaciones acordadas durante tres años, con los requisitos de seguridad y rendimiento establecidos”. Comparar un equipo que ejecuta esas aplicaciones con otro que no puede hacerlo produce una cifra de energía sin equivalencia de servicio. También deben ser comparables disponibilidad, periféricos y duración.

Dibuja el límite físico y temporal. Si mides una regleta con ordenador y monitor, el dato ya incluye ambos y no debes sumarlos otra vez. Si la regleta alimenta también un switch, identifícalo o separa la medición. Declara si quedan fuera servidor, red, climatización, fabricación, transporte y tratamiento final. Una exclusión explícita permite interpretar el resultado; una exclusión escondida puede llevar a una afirmación falsa sobre huella total.

Una medición de diez días no describe automáticamente un año. Para extrapolar necesitas calendario de trabajo, fines de semana, vacaciones, estados fuera de horario y cambios de carga. Conserva datos observados y escenario extrapolado en columnas diferentes. El escenario puede ser útil si sus supuestos son visibles y se analiza cómo afectaría que fueran distintos.

## 2. Inventario energético por funciones

Clasifica equipos en familias con comportamiento semejante: puesto ligero, puesto intensivo, servidor, switch, monitor y periférico. Registrar sólo cantidad y potencia de la fuente de alimentación no basta. La cifra máxima de la fuente es capacidad nominal, no consumo sostenido del sistema ni medida del uso real.

| Campo del inventario | Propósito |
| --- | --- |
| Identificador sintético | Relacionar medidas sin identificar personas. |
| Función y requisitos | Comprobar equivalencia de servicio. |
| Componentes incluidos | Evitar doble conteo de monitor y periféricos. |
| Estado operativo | Asociar potencia a trabajo, reposo, suspensión o apagado conectado. |
| Duración del estado | Convertir potencia en energía con un periodo explícito. |
| Instrumento y fecha | Reconstruir cómo se obtuvo la medida. |
| Origen del dato | Distinguir medición, ficha de fabricante e hipótesis. |
| Soporte y reparabilidad | Relacionar energía con vida útil y mantenimiento. |

“Apagado” puede seguir consumiendo si permanece conectado. “Suspensión” depende de hardware, firmware, sistema y configuración; debe probarse también reanudación, acceso a recursos, actualizaciones y tareas programadas. No desactives indiscriminadamente funciones de seguridad para ahorrar una cantidad pequeña que no has medido.

Para una familia de equipos no uses un único ejemplar como si representara a todos sin contrastar variabilidad. Una muestra puede contener configuraciones, monitores y cargas diferentes. Registra cómo elegiste las unidades y si observaste condiciones comparables. Si sólo dispones de un equipo, presenta el resultado como un caso, no como una estimación estadística del conjunto.

## 3. Protocolo de medida

Utiliza un medidor de energía de enchufe adecuado, en buen estado y dentro de su rango, siguiendo las instrucciones del fabricante y las normas del aula. No abras fuentes ni cuadros eléctricos. Cualquier medida que requiera intervenir en partes energizadas queda fuera del ejercicio de usuario de SMR y debe realizarla personal competente con su procedimiento.

Antes de medir, identifica qué alimenta el punto, fija fecha/hora y registra energía inicial. Para cargas variables, integra energía durante un intervalo representativo en lugar de multiplicar una lectura instantánea casual por todo el año. Repite con el mismo conjunto de aplicaciones y documenta actividad, brillo de pantalla, periféricos y condiciones que puedan afectar.

Un procedimiento didáctico puede observar arranque, trabajo representativo, reposo, suspensión, reanudación y apagado conectado. Para cada estado indica duración, lectura inicial y final y cualquier evento fuera de lo previsto. Un proceso de actualización durante una muestra puede ser legítimo, pero debe registrarse para no atribuir todo el consumo al trabajo habitual.

La relación básica es energía en kWh = potencia media en W × tiempo en horas / 1 000. Si el medidor entrega directamente energía integrada, conserva esa lectura y no vuelvas a sumar estimaciones de la misma carga. Comprueba unidades: 80 W durante dos horas equivalen a 0,16 kWh; 80 Wh no son 80 W por hora.

## 4. Incertidumbre, resolución y variabilidad

Resolución es el incremento que muestra el instrumento; exactitud declarada expresa un límite de error bajo condiciones indicadas; variabilidad corresponde al comportamiento real de la carga. Mostrar tres decimales no demuestra que el resultado sea preciso hasta ese nivel. Consulta rango, carga mínima, método de cálculo y especificación del aparato.

Separa incertidumbre de potencia, tiempo y extrapolación. Una medida fiable de una mañana puede representar mal una semana con trabajo distinto. La duración estimada de cada estado puede dominar el error, aunque el medidor tenga buena especificación. Conserva un escenario bajo, central y alto para las horas, y explica cuál es razonable según la actividad.

Para un ejercicio puedes calcular límites conservadores aplicando porcentajes hipotéticos, pero no los presentes como intervalos de confianza estadísticos. Sumar límites absolutos produce una acotación diferente de un análisis probabilístico. Además, mediciones realizadas con el mismo instrumento pueden compartir sesgo: no asumas independencia sólo porque están en dos columnas.

Si la mejora calculada es pequeña frente a la incertidumbre, amplía periodo, mejora el procedimiento o expresa que el ensayo no permite una conclusión firme. Evita presentar una reducción de décimas como ahorro demostrado si la carga y las condiciones cambiaron más que esa diferencia.

## 5. De energía a coste y emisiones de uso

El coste variable se estima multiplicando energía por precio aplicable al mismo periodo y concepto. Un precio medio elegido para un ejercicio no reproduce una factura completa: pueden existir términos fijos, impuestos, discriminación temporal y otros componentes. Cuando compares alternativas, identifica cuáles cambian y cuáles son comunes.

Para una estimación de emisiones de uso, relaciona kWh con un factor que especifique unidad, ámbito geográfico, periodo y metodología. No confundas CO2 con CO2 equivalente ni factor de un año con un valor universal. Los factores de este material son ficticios y sólo sirven para aprender la operación. Para un inventario real consulta la fuente y metodología que correspondan, como los recursos oficiales de [MITECO sobre huella de carbono](https://www.miteco.gob.es/es/cambio-climatico/temas/mitigacion-politicas-y-medidas/registro.html).

Una reducción de consumo eléctrico medida no establece por sí sola una reducción de toda la huella del producto. Fabricación, transporte, mantenimiento y fin de vida necesitan datos y límites adicionales. Tampoco una mejora operativa demuestra que una organización sea “neutra en carbono”, “cero emisiones” o cumpla un sistema completo de reporte.

## 6. Ciclo de vida y decisión de sustitución

Considera extracción y fabricación, distribución, uso, reparación y fin de vida. Una decisión puede ahorrar energía de uso y requerir fabricar un equipo nuevo. Para comparar necesitas datos suficientemente homogéneos: mismo tipo de impacto, límites, función, periodo y reglas de asignación. Dos informes con títulos parecidos no son automáticamente comparables.

La vida útil técnica depende de estado y reparabilidad; la vida útil funcional, de que cumpla la tarea; la vida útil de soporte, de que mantenga una plataforma apropiada y segura. Un equipo que arranca no tiene por qué cumplir el servicio. Una antigüedad alta tampoco justifica por sí sola retirarlo si cumple necesidades, soporte y seguridad.

Antes de sustituir, estudia mantenimiento, ampliación compatible, cambio de función y reasignación. Documenta piezas, tiempo, garantía, pruebas y soporte restante. Una ampliación de RAM no corrige un fallo de almacenamiento; cambiar almacenamiento no convierte una CPU incompatible en una plataforma soportada. La opción debe resolver el límite real identificado.

Un cálculo de punto de equilibrio ambiental puede ser didáctico si los datos de fabricación son supuestos explícitos. No lo presentes como análisis de ciclo de vida completo o certificado. Si falta información, ofrece comparación parcial y sensibilidad en lugar de inventar cifras para producir una respuesta definitiva.

## 7. Reutilización, preparación y residuos

Mantener, reutilizar, reparar, reacondicionar y reciclar describen procesos diferentes. Reutilizar mantiene utilidad de un producto o componente; reciclar recupera materiales mediante una gestión adecuada. Cuando un aparato ya tiene condición de residuo, su preparación para reutilización pertenece a un marco específico. No conviertas una retirada en una “donación” para evitar obligaciones o controles.

El [Real Decreto 110/2015 sobre RAEE](https://www.boe.es/eli/es/rd/2015/02/20/110/con) es la referencia estatal para estudiar categorías, responsabilidades y gestión; el procedimiento real debe ajustarse a la organización y al gestor competente. Esta guía propone una trazabilidad educativa, no determina por sí sola la clasificación jurídica de una operación concreta.

Una ficha de decisión registra identificador, motivo, estado, requisitos que deja de cumplir, alternativas, autorización, datos contenidos, tratamiento del soporte y destino. La retirada de inventario no implica que se hayan eliminado los datos. El certificado o justificante de entrega tampoco sustituye una prueba de saneamiento cuando ésta corresponde al proceso.

## 8. Saneamiento de información y cadena de custodia

Antes de reasignar o retirar, identifica qué soportes existen y qué información podrían contener. No asumas que todos los datos están en el disco principal: puede haber almacenamiento extraíble, memoria interna de impresoras u otros componentes. La selección del método depende del soporte, sensibilidad, destino y posibilidades técnicas.

La guía [NIST SP 800-88 Rev. 2](https://csrc.nist.gov/pubs/sp/800/88/r2/final), publicada en 2025, proporciona una referencia primaria para programas de saneamiento. Un borrado de archivos o un formateo rápido no demuestra por sí solo que los datos sean irrecuperables. Tampoco ejecutar un comando que termina sin error certifica automáticamente el resultado para cualquier dispositivo.

En este módulo se diseña el procedimiento y se trabaja con soportes virtuales o datos sintéticos autorizados. No se incluyen órdenes destructivas listas para aplicar a discos reales. Registra identidad del soporte, responsable, método seleccionado, herramienta/versión cuando proceda, resultado de verificación, excepción y destino. Si un soporte falla e impide verificar el método, documenta esa limitación y deriva al procedimiento autorizado, en lugar de marcar “borrado correcto”.

La cadena de custodia identifica quién tiene el equipo y cuándo cambia de manos. Usa un inventario de entrega y comprobante del destino. El acceso a datos durante la recuperación o saneamiento debe limitarse a lo necesario. El material para clase sustituye identificadores reales y evita mostrar contenido personal, incluso cuando se pretende demostrar que un archivo ha desaparecido.

## 9. Informe de decisión

Un informe sólido contiene pregunta, unidad funcional, límites, datos, método, cálculos, incertidumbre, comparación y decisión. Distingue medidas obtenidas, supuestos y tareas pendientes. Incluye impactos sobre usuarios, soporte y recuperación, además de energía.

La recomendación debe decir bajo qué condiciones sigue siendo válida. Si depende de tres años adicionales de soporte, ésa es una condición verificable; si el soporte termina antes, debes revisar la decisión. Si el ahorro depende de suspensión fuera de horario, prueba que el usuario puede reanudar y que no se rompe una tarea necesaria. Una política que nadie puede mantener no ofrece el resultado previsto de forma sostenible.
