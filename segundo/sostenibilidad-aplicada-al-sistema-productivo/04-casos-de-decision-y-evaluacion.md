# Tres casos de decisión con cálculos y evaluación

[Índice](README.md) · [Método de medida y trazabilidad](03-medicion-ciclo-de-vida-y-trazabilidad.md)

Todos los datos de estos casos son hipótesis didácticas. Las potencias representan medias supuestas de los conjuntos indicados y los factores de emisiones son ficticios. No se afirma que exista una medición real, una tarifa comercial o un análisis de ciclo de vida completo.

## Caso 1. Política de energía para un aula heterogénea

### Inventario y condiciones

El aula dispone de ocho puestos ligeros, cuatro intensivos, un switch y un servidor. Cada puesto incluye ordenador y monitor. No se volverá a sumar el monitor por separado. El calendario supuesto contiene 220 días de trabajo y 145 días sin actividad de usuarios; el año del modelo tiene 365 días. El servidor y el switch permanecen activos.

| Grupo | Cantidad | Trabajo por jornada | Reposo por jornada | Fuera de uso por jornada |
| --- | ---: | --- | --- | --- |
| A · ligero | 8 | 65 W durante 4 h | 35 W durante 4 h | 3 W durante 16 h |
| B · intensivo | 4 | 95 W durante 6 h | 45 W durante 2 h | 5 W durante 16 h |
| Switch | 1 | 15 W durante 24 h | Incluido | Incluido |
| Servidor | 1 | 55 W durante 24 h | Incluido | Incluido |

Para A, energía por puesto en día laboral: (65 × 4 + 35 × 4 + 3 × 16)/1000 = 0,448 kWh. Ocho puestos suman 3,584 kWh. Para B: (95 × 6 + 45 × 2 + 5 × 16)/1000 = 0,740 kWh; cuatro suman 2,960 kWh. Switch y servidor añaden 0,360 y 1,320 kWh. El total diario laboral es 8,224 kWh.

### Mejora propuesta y validación

Se sustituyen las cuatro horas de reposo de A por suspensión de 2 W, y las dos horas de reposo de B por suspensión de 3 W. El resto no cambia. A pasa a 0,316 kWh por puesto y B a 0,656. El nuevo total laboral es 8 × 0,316 + 4 × 0,656 + 0,360 + 1,320 = 6,832 kWh.

El ahorro por día laboral es 1,392 kWh. Fuera de días laborales, A permanece a 3 W y B a 5 W durante veinticuatro horas, sin diferencia entre alternativas. La energía de esos puestos es (8 × 3 + 4 × 5) × 24/1000 = 1,056 kWh diarios; más red y servidor, 2,736 kWh.

~~~text
Base anual = 8,224 × 220 + 2,736 × 145 = 2206,00 kWh
Mejora anual = 6,832 × 220 + 2,736 × 145 = 1899,76 kWh
Ahorro = 306,24 kWh/año
Reducción respecto a la base = 306,24 / 2206 × 100 ≈ 13,88 %
~~~

Con precio variable supuesto de 0,22 €/kWh, ahorro de 67,3728 €, presentado como 67,37 €. Con factor ficticio 0,18 kg CO2eq/kWh, el efecto sobre emisiones eléctricas de uso sería 55,1232 kg CO2eq, aproximadamente 55,12. No incluyas esos datos como factor oficial ni como huella total del aula.

Antes de recomendar el cambio, prueba suspensión, reanudación, guardado, conexión de red y tareas necesarias. Si un puesto intensivo ejecuta una tarea larga, necesita una excepción documentada o una política distinta. No excluyas equipos que fallan de la muestra sólo para mejorar el porcentaje: registra qué ocurre y por qué.

### Incertidumbre y aceptación

Como ejercicio conservador, supón un límite de ±5 % en ambos totales anuales. La base tendría ±110,30 kWh y la mejora ±94,988. Restando extremos, el ahorro quedaría entre 100,952 y 511,528 kWh. Es un intervalo conservador construido con hipótesis, no un intervalo estadístico de confianza, y no modela la correlación del sesgo de un mismo medidor.

Si se usa el mismo procedimiento y equipo, parte del error podría ser compartido; para tratarlo correctamente necesitas un análisis adicional. La conclusión permitida es que el modelo central estima 306,24 kWh y muestra cómo varía bajo los límites supuestos. Un informe real debe utilizar especificaciones y variabilidad observadas.

**Entregables:** inventario, hoja por estados, calendario, pruebas de servicio y sensibilidad. **Aceptación:** todas las horas de cada jornada suman veinticuatro, no existe doble conteo y los cambios se relacionan con una configuración que podría verificarse y revertirse.

## Caso 2. Reparar o sustituir un puesto

### Equivalencia de servicio

Un equipo cumple la tarea y puede mantenerse con soporte adecuado durante tres años si se repara el almacenamiento. Se compara esa reparación con un equipo nuevo que realiza la misma función. Ambos se usarían 1 600 horas anuales. La decisión queda condicionada a compatibilidad, seguridad, soporte y rendimiento; si el equipo antiguo no puede cumplirlos, el cálculo energético no basta para aprobar su continuidad.

Supuestos: equipo existente 90 W durante las horas consideradas; nuevo 45 W. No se modelan otros estados, idénticos por hipótesis o fuera del alcance parcial. La diferencia anual de energía es (90 − 45) × 1600/1000 = 72 kWh. En tres años, 216 kWh.

### Comparación económica parcial

La reparación cuesta 80 € en pieza y dos horas a 20 €/h: 120 €. La compra cuesta 500 € más dos horas de preparación a 20 €/h: 540 €. La diferencia inicial es 420 €. A un precio supuesto de 0,20 €/kWh, el equipo nuevo ahorra 14,40 € por año en la electricidad considerada.

El cruce simple de esa diferencia sería 420/14,40 ≈ 29,17 años, muy superior al horizonte de tres. No significa que el equipo viejo dure ese periodo ni que la compra carezca de otros beneficios. Muestra que, con estos supuestos, el ahorro eléctrico por sí solo no justifica el sobrecoste durante el horizonte analizado.

En tres años, el ahorro variable sería 43,20 € y el sobrecoste inicial restante 376,80 €. Faltan riesgo de avería, garantía, valor residual, soporte y otras diferencias que deberían cuantificarse o describirse. Mantén esos conceptos fuera de un total numérico si no dispones de una base razonable, en lugar de introducir valores arbitrarios.

### Comparación ambiental ilustrativa

Supón exclusivamente para aprender que las emisiones de fabricación comparables atribuidas al equipo nuevo fueran 220 kg CO2eq y las de la pieza de reparación 15 kg. La diferencia inicial sería 205 kg. Con factor de uso ficticio de 0,20 kg CO2eq/kWh, el ahorro anual de uso del nuevo sería 14,40 kg; en tres años, 43,20.

El cruce simplificado sería 205/14,40 ≈ 14,24 años. Estos datos no se presentan como valores reales de ningún fabricante ni como análisis completo: faltan límites y etapas que podrían afectar. El ejercicio enseña que una mejora de eficiencia de uso y un efecto adicional de fabricación deben compararse con horizonte y unidades coherentes.

**Decisión razonada:** reparar puede ser preferible bajo las condiciones fijadas, pero se revisa si falla soporte, seguridad o equivalencia funcional. La recomendación identifica condición, coste, plazo de revisión y pruebas posteriores, sin afirmar una superioridad ambiental universal.

## Caso 3. Salida de seis equipos y protección de información

### Clasificación inicial

Un centro ficticio revisa seis unidades: dos admiten reparación, dos cumplen funciones de menor demanda, una puede aportar componentes tras diagnóstico y una no puede ponerse en servicio de forma segura. Ninguna se entrega antes de definir titularidad, autorización, tratamiento de datos y destino.

El inventario distingue producto que continúa utilizándose y aparato que pasa al flujo de residuos conforme al procedimiento aplicable. No declares que toda cesión es una preparación para reutilización ni que cualquier desmontaje puede realizarse sin condiciones. Consulta el marco RAEE y los procedimientos de la entidad para determinar actuación y operador apropiados.

### Plan de trabajo y evidencias

Para las dos unidades reparables registra fallo, pieza compatible, coste supuesto, autorización, intervención y pruebas de aceptación. Si se sustituye almacenamiento, el soporte retirado mantiene un registro de custodia separado. “Equipo reparado” no cierra automáticamente el tratamiento de la pieza que contenía datos.

Para las dos unidades reasignadas define nueva función, sistema soportado, accesibilidad, rendimiento y responsable receptor. Revisa cuentas, credenciales, licencias y datos previos. La simple instalación de un sistema nuevo no constituye por sí sola evidencia de saneamiento suficiente para cualquier soporte o nivel de sensibilidad.

Para la unidad destinada a componentes, distingue piezas comprobadas y piezas sin verificar. Cada componente reutilizado debe conservar compatibilidad y estado, y el resto sigue un destino documentado. No presentes un lote mezclado como “todo reciclado” si una parte continúa en uso y otra tiene un tratamiento pendiente.

Para la unidad no recuperable identifica soporte y posibilidad de saneamiento autorizado. Si el fallo impide verificar el método, registra la excepción y deriva según la política. Conserva comprobante de entrega al canal correspondiente, con datos mínimos y conciliación del lote.

### Conciliación y seguimiento

La conciliación inicial es seis equipos = dos reparados + dos reasignados + uno para componentes + uno para salida gestionada, pero debe revisarse con el resultado real. Si una reparación fracasa, cambia el estado con fecha y motivo; no alteres el inventario anterior para ocultar la desviación.

La matriz final contiene identificador sintético, estado inicial, decisión, resultado, responsable, soporte de datos, evidencia de saneamiento cuando proceda y destino. Otro técnico debe poder localizar qué falta sin acceder al contenido de los datos. Una fotografía de un contenedor no demuestra por sí sola cantidad, autorización ni trazabilidad.

**Entregables:** matriz de seis unidades, criterios de decisión, fichas de pruebas, registro de custodia y ejemplo vacío de comprobante. La actividad es documental: no se ejecuta destrucción o borrado de discos reales por seguir este caso.

## Evaluación y defensa

Rúbrica propia: delimitación y equivalencia funcional 20 %, método y datos 20 %, cálculos y sensibilidad 25 %, continuidad y reparabilidad 15 %, datos/RAEE/trazabilidad 15 %, comunicación de límites 5 %. No atribuye una certificación ambiental ni modifica criterios oficiales del módulo.

Preguntas para defender: ¿qué conclusión cambia si el calendario es distinto?, ¿qué contiene exactamente la medida de un puesto?, ¿qué dato es observado y cuál supuesto?, ¿qué haría rechazar la reparación?, ¿cómo demostrarías el destino sin publicar información sensible? Las respuestas deben relacionar una decisión con una evidencia, no limitarse a repetir “ahorrar”, “reciclar” o “ser eficiente”.
