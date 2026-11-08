# Auditoría de un aula y propuesta de mejora

## Práctica 1. Inventario y límites

Selecciona un aula o inventario simulado de doce puestos. Si usas equipos reales, limita la recogida a lo autorizado. Registra tipo, antigüedad aproximada, capacidad de ampliación, soporte, estado y necesidad que cubre. No identifiques a las personas que utilizan cada equipo. Incluye monitor y periféricos indicando si se medirán juntos o separados.

1. Define periodo y alcance: por ejemplo, consumo eléctrico de puestos y monitores durante veinte jornadas de ocho horas.
2. Dibuja el límite de medida y lista lo que queda fuera: servidor, red, climatización o fabricación, según el caso.
3. Identifica tres opciones: política de energía, reparación/ampliación y sustitución.
4. Para cada una, explica evidencia necesaria, riesgo, coste estimado y efecto sobre el servicio.
5. Selecciona un piloto y documenta cómo volverías a la configuración previa.

**Solución orientativa:** si las medidas incluyen ordenador y monitor en una misma regleta, no sumes después un consumo de monitor por separado. Un equipo antiguo con soporte vigente y rendimiento suficiente puede mantenerse; otro sin soporte para un sistema seguro requiere una alternativa que valore compatibilidad, función y coste. La edad sola no decide.

## Práctica 2. Cálculo por estados

Supuestos didácticos para cada uno de doce puestos completos:

| Estado | Potencia | Duración por jornada |
| --- | --- | --- |
| Trabajo | 100 W | 5 h |
| Reposo | 50 W | 3 h |
| Fuera de uso | 4 W | 16 h |

Para una jornada de veinticuatro horas:

```text
E_puesto = (100 × 5 + 50 × 3 + 4 × 16) / 1000 = 0,714 kWh
E_12_puestos = 0,714 × 12 = 8,568 kWh
```

La política propuesta conserva cinco horas de trabajo y sustituye las tres horas de reposo por suspensión de 3 W. Fuera de uso, permanece el mismo estado de 4 W; esta es una hipótesis específica y debe comprobarse con medidas:

```text
E_nueva_puesto = (100 × 5 + 3 × 3 + 4 × 16) / 1000 = 0,573 kWh
E_nueva_12 = 6,876 kWh
Ahorro por jornada = 1,692 kWh
Ahorro por 20 jornadas = 33,84 kWh
```

Si el precio supuesto es 0,20 €/kWh, el ahorro de energía variable es 6,768 €, aproximadamente 6,77 €. Este cálculo no incluye términos fijos, impuestos ni cambios de tarifa. Con un factor de ejemplo de 0,25 kg CO2eq/kWh, el ahorro de emisiones de uso sería 8,46 kg CO2eq. **Ese factor es exclusivamente didáctico y no se presenta como oficial ni actual.**

Repite el cálculo en una hoja, conserva precisión interna y redondea al presentar. Cambia duración y potencia para un escenario distinto. Si sólo hay diez días de medida, no lo presentes como una medición anual; una extrapolación necesita supuestos sobre el resto del calendario.

**Entregables:** hoja con fórmulas, unidades, límite de cálculo, supuestos y análisis de sensibilidad. La aceptación exige que otra persona pueda recalcular el resultado y localizar cada dato de entrada.

## Práctica 3. Reparar, reutilizar o retirar

Una unidad de almacenamiento falla en un equipo de prácticas con RAM suficiente y sistema soportado. Diseña una intervención: diagnóstico, autorización, recuperación de datos si procede, sustitución compatible, instalación/restauración, pruebas y gestión del soporte retirado. No ejecutes operaciones de borrado sobre discos reales en esta actividad documental.

Compara tres escenarios: reparación, reasignación a una tarea menos exigente y compra. Anota coste, tiempo, soporte restante, accesibilidad y riesgos. Si no tienes datos de fabricación, indica que no puedes cuantificar la huella total; no asignes emisiones inventadas para forzar una conclusión.

Diseña además una ficha de retirada con identificador didáctico, motivo, responsable, estado del saneamiento de datos, destino y comprobante. Utiliza un modelo sin datos reales. La evidencia de retirada no debe limitarse a una fotografía del equipo junto a un contenedor.

## Rúbrica propuesta

| Criterio | Peso | Evidencia |
| --- | --- | --- |
| Límites y calidad del inventario | 20 % | Evita doble conteo y aclara exclusiones. |
| Cálculos y unidades | 30 % | Distingue W, kWh, coste y CO2eq. |
| Viabilidad y continuidad del servicio | 20 % | Prueba impacto y permite revertir. |
| Reparación, datos y residuos | 20 % | Justifica decisión y trazabilidad. |
| Comunicación de incertidumbre | 10 % | Diferencia medida, hipótesis y estimación. |

## Preguntas razonadas

1. **¿Una fuente de 650 W consume 650 W todo el día?** No: su capacidad nominal no equivale al consumo del equipo. Hay que medir o estimar por estados.
2. **¿Cuánto consume un equipo de 80 W durante 2,5 h?** `80 × 2,5 / 1000 = 0,2 kWh`.
3. **¿Se puede aplicar PUE a una CPU?** No con su significado de centro de datos: requiere energía total de instalación y de equipos IT con límites coherentes.
4. **¿Ahorrar electricidad demuestra menor huella completa?** No: sólo prueba una parte del uso. Fabricación, transporte y fin de vida requieren datos adicionales.
5. **¿Qué falta si un informe dice “se reciclaron diez equipos”?** Identificación o agregación controlada, autorización, tratamiento de datos, canal de gestión y comprobantes adecuados.

[Guía](01-guia.md) · [Índice](README.md)
