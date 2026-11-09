# Casos completos: transformación, costes y evaluación de IA

[Índice](README.md) · [Datos e integraciones](03-datos-integraciones-y-gobierno.md)

Los escenarios siguientes son sintéticos. Precios, tiempos, volúmenes y umbrales son hipótesis de aprendizaje, no tarifas comerciales, resultados de una empresa real ni promesas de ahorro. El objetivo es construir una decisión que otra persona pueda recalcular y cuestionar.

## Caso 1. Rediseñar la recepción de un taller

### Situación y línea base

Un taller de doce puestos recibe veinte solicitudes por semana mediante llamadas y notas. La coordinación invierte doce minutos por solicitud en registrar, preguntar datos faltantes y localizar el activo. El tiempo inicial esperado de registro es 20 × 12 = 240 minutos, cuatro horas semanales. Ocho de veinte solicitudes llegan sin identificador de activo y cuatro se duplican en el registro.

El problema no se define como ausencia de una aplicación. Se concreta en información incompleta, duplicados y tiempo de coordinación. Una herramienta que sólo añada un formulario puede trasladar la carga a la persona solicitante sin resolver seguimiento o búsqueda. Antes de seleccionar producto, entrevista mediante un guion ficticio a solicitante, técnico y coordinador: qué necesitan saber, qué decisiones toman y qué errores cuestan más.

### Diseño propuesto

El formulario solicita activo o indicación explícita de que no se conoce, descripción, categoría inicial y momento del síntoma. No pide contraseña ni contenido de documentos. El sistema asigna identificador de solicitud, detecta coincidencias potenciales y conserva el contacto por el canal autorizado. La coincidencia no elimina automáticamente una solicitud: dos problemas del mismo equipo pueden ser distintos.

La coordinación revisa prioridad con impacto y urgencia, asigna técnico y solicita datos adicionales sólo cuando sean necesarios. La persona usuaria puede consultar estado y aportar información. El técnico registra prueba, actuación y resultado. El cierre requiere validación o una regla de seguimiento publicada para cuando no haya respuesta; esa regla no se inventa después para mejorar una métrica.

### Plan de piloto

Prepara veinte solicitudes sintéticas del mismo nivel de dificultad para cada alternativa. Alterna el orden para reducir el efecto de aprendizaje y define cuándo empieza y termina el cronómetro. Mide tiempo de registro, completitud, duplicados detectados correctamente y correcciones posteriores. No compares una semana de veinte averías difíciles con otra de diez solicitudes sencillas sin controlar la composición.

Un resultado hipotético reduce el tiempo a cinco minutos por solicitud: 20 × 5 = 100 minutos, ahorro estimado de 140 minutos semanales. Completitud pasa de 12/20 a 18/20: de 60 % a 90 %, mejora de treinta puntos porcentuales. El incremento relativo es (90 − 60) / 60 = 50 %; no confundas ambos indicadores.

### Interpretación y decisión

El tiempo liberado no equivale necesariamente a menor gasto salarial. Puede reducir cola, aumentar calidad o permitir otras tareas. Para convertirlo en beneficio económico debes explicar cómo cambia realmente el uso de recursos. Además, el registro puede ser más rápido y el cierre más lento si existe una validación necesaria que antes se omitía; mide el proceso completo antes de declarar éxito global.

Acepta el piloto si mantiene exportación, roles y recuperación y mejora las métricas sin aumentar errores críticos. Si la completitud mejora a costa de inventar valores obligatorios, el resultado no es válido. Entrega mapa antes/después, requisitos, diccionario, lote de pruebas, conteos, resultados y límites de la conclusión.

## Caso 2. Comparar coste total local y SaaS

### Supuestos homogéneos

Se comparan dos alternativas para doce usuarios durante veinticuatro meses, sin IVA ni valor residual y con igual conjunto mínimo de funciones. Los importes son deliberadamente ficticios. No se incluyen intereses ni descuento financiero; si la decisión lo necesitase, deberían añadirse de forma coherente a ambas alternativas.

| Concepto | Local | SaaS |
| --- | ---: | ---: |
| Equipo inicial | 900 € | 0 € en este supuesto |
| Migración | 240 € | 300 € |
| Formación | 180 € | 180 € |
| **Inversión inicial** | **1 320 €** | **480 €** |
| Energía mensual incremental | 8 € | Incluida en cuota del proveedor según hipótesis |
| Administración mensual | 1,5 h × 20 € = 30 € | 0,5 h × 20 € = 10 € |
| Copia/exportación mensual | 10 € | 12 € |
| Licencia o cuota de aplicación mensual | 0 € | 12 × 6 € = 72 € |
| **Recurrente mensual** | **48 €** | **94 €** |

La ausencia de licencia local en el ejemplo no significa que todas las aplicaciones locales sean gratuitas. El SaaS tampoco elimina el ordenador cliente, la conectividad o toda tarea administrativa. Se han excluido costes comunes a ambos diseños; si alguno cambia, se reincorpora a la comparación.

### Cálculos y horizonte

~~~text
TCO_local_24 = 1320 + 24 × 48 = 2472 €
TCO_SaaS_24 = 480 + 24 × 94 = 2736 €
Diferencia a 24 meses = 2736 − 2472 = 264 €

Cruce simple = (1320 − 480) / (94 − 48)
             = 840 / 46 ≈ 18,26 meses
~~~

Durante los primeros meses el SaaS requiere menos desembolso inicial; después del cruce simple el local tiene menor coste acumulado bajo estos supuestos. El cruce no mide calidad ni riesgo y no garantiza que haya dinero disponible para la inversión inicial. Para treinta y seis meses, local suma 3 048 € y SaaS 3 864 €, diferencia de 816 €.

Realiza sensibilidad. Si la administración local fuera tres horas mensuales, pasaría a 60 € y el recurrente local a 78 €. El TCO local a veinticuatro meses sería 1320 + 24 × 78 = 3192 €, mayor que 2 736 €. El cambio de una sola hipótesis revierte la preferencia económica. Por eso necesitas justificar horas y tareas, no elegir cifras que favorezcan una solución.

### Riesgos, salida y decisión

Compara recuperación, conectividad, administración, soporte, accesibilidad y salida. El local puede depender de un equipo y una persona; el SaaS puede depender de conectividad, contrato y exportación. Verifica qué incluye realmente la recuperación: disponer de papelera no equivale a restaurar una base completa con relaciones, adjuntos y permisos.

La prueba de salida exporta activos, incidencias y actuaciones y comprueba identificadores, fechas, relaciones y archivos. Un CSV con nombres visibles pero sin vínculos estables puede no permitir reconstruir el historial. Pide también un procedimiento de baja, retención y revocación de acceso. La decisión final combina coste y requisitos mínimos: una alternativa barata que no cumple una condición obligatoria no es admisible sólo por su TCO.

**Entregables:** hoja de cálculo con fórmulas, fuentes de supuestos, escenario base, sensibilidad y tabla de cumplimiento. **Solución razonada:** con el escenario base, local es 264 € más barato a dos años; con tres horas mensuales de administración, SaaS es 456 € más barato. La elección depende de capacidad y condiciones observadas.

## Caso 3. Integrar inventario e incidencias

Un inventario aporta seis filas con los errores del [capítulo de datos](03-datos-integraciones-y-gobierno.md). Diseña un flujo de entrada, preparación, validación y publicación. El sistema de incidencias sólo puede referenciar activos publicados; las filas rechazadas no desaparecen, sino que conservan motivo y lote para corregirse.

El primer ensayo acepta tres activos, detecta un duplicado exacto y rechaza dos filas. El segundo reenvía el mismo lote: el resultado esperado es cero altas nuevas y una respuesta que permita conocer el resultado anterior. El tercero envía PC-004 corregido con una nueva revisión de origen: se incorpora un activo, se mantiene la relación con el rechazo anterior y se verifica que la corrección no modifica otro código.

Define una incidencia para un activo inexistente. La integración debe rechazarla o mantenerla en un estado de preparación explícito; no debe crear un activo incompleto a escondidas. Define también qué ocurre si el inventario cambia el código visible. El identificador estable evita romper la relación, pero la migración debe conservar la correspondencia y comunicar el nuevo nombre.

Prueba una actualización concurrente: dos clientes leen versión 3, uno guarda versión 4 y el otro intenta escribir basándose en versión 3. El resultado esperado es un conflicto controlado, no una mezcla accidental ni la pérdida silenciosa del cambio anterior. Documenta cómo se presenta y resuelve el conflicto con información suficiente para decidir.

**Entregables:** contratos de entrada/salida, mapa de campos, conciliación, política de duplicados, respuesta de errores y matriz de pruebas. El caso se puede resolver documentalmente o con una implementación local; declara cuál de las dos opciones has realizado y no atribuyas ejecución a un diagrama.

## Caso 4. Evaluar un clasificador de tickets

### Diseño de la evaluación

El objetivo es sugerir si una incidencia necesita revisión prioritaria, no ejecutar cambios ni decidir por sí sola una emergencia. Prepara cien tickets sintéticos etiquetados por un criterio escrito: veinte requieren revisión prioritaria y ochenta no. Mantén separados los ejemplos usados para redactar instrucciones y el conjunto final de evaluación; corregir instrucciones mirando continuamente las respuestas de evaluación contamina el ensayo.

Una línea base que clasifica todo como no prioritario consigue 80 % de exactitud y no detecta ningún caso prioritario. Esto demuestra por qué la exactitud global es insuficiente. Define qué error tiene mayor coste y qué revisión humana seguirá existiendo. La clasificación de seguridad no debe depender únicamente de que un texto contenga una palabra llamativa.

### Matriz y métricas

Resultado supuesto de un modelo: detecta dieciséis de los veinte casos prioritarios y clasifica ocho de los ochenta ordinarios como prioritarios.

| Real / predicción | Prioritario | Ordinario | Total |
| --- | ---: | ---: | ---: |
| Prioritario | 16 | 4 | 20 |
| Ordinario | 8 | 72 | 80 |
| Total | 24 | 76 | 100 |

La exactitud es (16 + 72)/100 = 88 %. La precisión de prioritarios es 16/24 ≈ 66,7 %; su cobertura o recall es 16/20 = 80 %. F1 resulta 2 × 16 / (2 × 16 + 8 + 4) = 32/44 ≈ 72,7 %. Cuatro casos prioritarios siguen sin detectarse, aunque el resultado global mejore ocho puntos porcentuales respecto a la línea base.

### Sesgo, deriva y supervisión

Desglosa por longitud, vocabulario, idioma y tipo técnico, con muestras suficientes para interpretar cada grupo. Si todos los tickets de un grupo usan una plantilla distinta, el modelo puede aprender el formato en vez del problema. Evita usar nombres, edad o información personal que no sea necesaria para la tarea.

Ensaya texto que incluya instrucciones engañosas como parte de una descripción sintética: el sistema debe tratarlo como dato y conservar el contrato de clasificación. No otorgues al clasificador herramientas de administración para “resolver” lo que lea. Guarda versión del modelo o servicio, instrucciones, fecha, conjunto y parámetros disponibles para comparar repeticiones.

Define criterio de pausa o retirada: aumento de falsos negativos, cambios de proceso, pérdida de trazabilidad o imposibilidad de revisar la salida. Una nueva versión de un servicio puede cambiar comportamiento; no mantengas una aprobación indefinida basada en un ensayo antiguo. El resultado de este caso justificaría como máximo estudiar asistencia supervisada, no autorizar decisiones críticas autónomas.

## Evaluación y defensa

Rúbrica propia: modelo del proceso y datos 25 %, coherencia de integración 20 %, cálculos y sensibilidad 20 %, diseño de pruebas y métricas 25 %, claridad y gobierno 10 %. Los porcentajes suman cien y se aplican a evidencias, no al número de herramientas mencionadas.

Defiende tres decisiones: por qué un dato existe, cómo detectas que una importación perdió información y qué resultado haría rechazar la solución elegida. Una defensa sólida admite incertidumbre, muestra el efecto de cambiar una hipótesis y diferencia mejora estimada de mejora observada. Consulta las fuentes técnicas del [capítulo anterior](03-datos-integraciones-y-gobierno.md) para semántica y responsabilidades; las cifras y casos de este documento son elaboración didáctica original.
