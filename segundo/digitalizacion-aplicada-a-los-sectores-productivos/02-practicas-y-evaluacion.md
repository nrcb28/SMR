# Prácticas y evaluación de Digitalización

## Caso común: taller con doce puestos

Una pequeña organización registra veinte incidencias por semana. Actualmente copia datos de mensajes a una hoja de cálculo; el registro consume doce minutos por incidencia. Se propone un formulario con campos validados, número de activo y estados definidos. El tiempo objetivo es cinco minutos. Los números son supuestos educativos, no resultados medidos ni precios de mercado.

## Práctica 1. Modelar el proceso y sus datos

1. Dibuja las fases desde solicitud hasta cierre. Identifica qué persona valida cada cambio de estado.
2. Crea diez solicitudes sintéticas con datos mínimos: número, activo, fecha, categoría, descripción, prioridad justificada y estado.
3. Introduce de forma deliberada dos duplicados y dos valores de categoría incorrectos. Diseña reglas para detectarlos sin eliminar información automáticamente.
4. Define al menos seis requisitos: registro, búsqueda, control de roles, exportación, recuperación y trazabilidad.
5. Para cada requisito, escribe una prueba con entrada y resultado esperado.
6. Documenta qué información no se recoge y por qué.

**Solución razonada:** el identificador del ticket debe ser único, pero un mismo activo puede tener varias incidencias en fechas distintas. No elimines registros sólo porque comparten activo. Un estado `cerrado` requiere comprobación y fecha de cierre; la palabra por sí sola no prueba que el problema desapareció. El acceso se concede por función: solicitante, soporte y responsable, con permisos mínimos.

**Entregables:** diagrama, diccionario de datos, CSV sintético, reglas de validación y matriz requisito/prueba. La aceptación exige que otra persona pueda interpretar un registro sin preguntar qué significan sus campos.

## Práctica 2. Comparar solución local y SaaS

Compara tres alternativas conceptuales: hoja compartida, aplicación local y SaaS de tickets. No hace falta contratar servicios. Usa una tabla que incluya roles, MFA, exportación, disponibilidad, dependencia de Internet, copia, recuperación, mantenimiento y salida del proveedor. Consulta documentación oficial de cualquier producto que cites y registra versión o fecha.

Para un ejemplo económico, se plantean estas hipótesis: implantación de 180 €, cuota de 18 € por periodo de cuatro semanas y valoración del tiempo en 15 €/hora. El ahorro estimado de registro es:

```text
20 incidencias/semana × (12 − 5) min/incidencia = 140 min/semana
140 / 60 = 2,333... horas/semana
2,333... × 4 semanas de cálculo = 9,333... horas por periodo
Valor estimado = 9,333... × 15 = 140 € por periodo
Beneficio neto recurrente supuesto = 140 − 18 = 122 €
Recuperación simple de implantación = 180 / 122 ≈ 1,48 periodos
```

El periodo de cuatro semanas es una simplificación; no se ha usado la media real de semanas de un mes. El valor del tiempo no es necesariamente una reducción de gasto salarial: puede representar capacidad para otras tareas. No mezcles ahorro monetario efectivo y capacidad liberada. Añade formación, migración y soporte si existen; el resultado anterior no es un coste total completo.

**Entregables:** comparación, hipótesis económicas, cálculo reproducible y decisión argumentada. Un producto con más funciones puede ser peor si no permite exportar los datos necesarios o requiere mantenimiento que el equipo no puede asumir.

## Práctica 3. Piloto, automatización y uso crítico de IA

Implementa un prototipo con las herramientas ya disponibles en el centro. Usa una hoja con validación o una aplicación de pruebas; evita cuentas y datos reales de empresa. Prepara diez tareas equivalentes antes y después del cambio, alterna quién las realiza y registra tiempo, errores y campos faltantes. Mantén la misma definición de “tarea terminada”.

Calcula mediana de tiempo y porcentaje de registros completos. Si antes hay ocho completos de diez y después nueve, la mejora es de diez puntos porcentuales, no de un 10 % relativo: pasa de 80 % a 90 %, equivalente a un aumento relativo de 12,5 %. El tamaño de muestra es pequeño; presenta el resultado como piloto.

Añade una automatización de lectura: exportación a CSV o comprobación de identificadores duplicados. Registra entradas, salidas y tratamiento de errores. Si pruebas IA para sugerir categorías, usa únicamente descripciones sintéticas, oculta la categoría esperada y revisa manualmente todas las respuestas. Cuenta confusiones por tipo de incidencia y explica cuándo descartarías el sistema.

**Criterios de aceptación:** datos exportables sin pérdida de campos, acceso coherente con roles, recuperación demostrada en una copia del prototipo y métricas comparables. Conserva un procedimiento para volver a la forma de trabajo anterior y un registro de qué datos habría que trasladar.

## Rúbrica propia y cuestiones razonadas

| Criterio | Peso | Evidencia |
| --- | --- | --- |
| Análisis del proceso | 20 % | Identifica necesidad y cuellos de botella. |
| Arquitectura y responsabilidades | 20 % | Justifica componentes y operación. |
| Datos, privacidad y seguridad | 25 % | Minimiza, valida y protege información. |
| Piloto y métricas | 25 % | Compara con línea base sin inventar resultados. |
| Documentación y salida | 10 % | Permite repetir, exportar y revertir. |

1. **¿Una copia sincronizada es siempre un backup?** No: puede propagar borrados o corrupción. Comprueba versiones, retención y restauración independiente.
2. **¿Es suficiente acertar un 95 % de tickets?** Depende del reparto de clases y del daño de los errores. Hay que examinar qué falla y quién revisa la decisión.
3. **¿Instalar más sensores mejora los datos?** Sólo si la medida es pertinente, fiable y contextualizada con unidad, hora y mantenimiento.
4. **¿Puede ser mejor conservar un paso manual?** Sí, cuando aporta revisión necesaria o el coste/riesgo de automatizar supera el beneficio medido.
5. **¿Qué demuestra un piloto sin comparación previa?** Que una solución se pudo usar en esas condiciones; no demuestra cuánto mejoró el proceso.

[Guía](01-guia.md) · [Índice](README.md)
