# Casos de IPE I: procedimiento, cálculo y evidencia

Todos los nombres de roles, importes y condiciones de estos casos son ficticios. Las soluciones son orientaciones didácticas y no una resolución de un conflicto laboral real.

## Práctica 1. Inspección preventiva de un taller

**Situación:** seis puestos de reparación, cables de alimentación en una zona de paso, una caja pesada en un estante alto, reflejos sobre dos pantallas y un equipo con batería visiblemente deformada. Duración sugerida: dos sesiones. La inspección se realiza sin energizar, abrir o mover los equipos peligrosos.

### Procedimiento

1. Dibuja un plano ficticio de zonas de trabajo y evacuación.
2. Registra cada hallazgo con un identificador, tarea y personas expuestas.
3. Propón la acción inmediata y una medida duradera.
4. Asigna responsable y evidencia de cierre.
5. Revisa si la solución introduce otro problema: una canaleta no debe bloquear un paso ni crear un resalte peligroso.

### Solución orientativa

| Hallazgo | Primera actuación | Medida de cierre verificable |
| --- | --- | --- |
| Cable cruzando el paso | Comunicar y evitar el tránsito por la zona según protocolo | Distribución de tomas y canalización revisada |
| Caja pesada en altura | No improvisar el descenso | Reubicación con medios adecuados y criterio de almacenamiento |
| Reflejos | Registrar orientación y momento | Ajuste del puesto y nueva comprobación con la persona usuaria |
| Batería deformada | Detener uso y avisar | Retirada por personal autorizado y gestión de residuo |

Para priorizar en clase puede usarse una matriz propia de probabilidad y consecuencia de 1 a 3. El producto de ambos valores ayuda a discutir prioridades, pero **no sustituye un método profesional ni autoriza a continuar una actividad peligrosa**. Con consecuencia 3 y probabilidad 2 se obtiene 6; la decisión no es únicamente numérica: un peligro inmediato exige detener la actividad conforme al procedimiento.

**Entregables:** plano, tabla de hallazgos, justificación de prioridades, propuesta y comprobación de cierre. **Aceptación:** cada medida tiene responsable y evidencia; no se presenta la pulsera ESD como protección eléctrica ni se propone abrir un SAI.

## Práctica 2. Nómina simplificada en una hoja de cálculo

**Datos del supuesto:** salario base 1.500 €, complemento 150 € y prorrata de extras 250 €. No hay otros devengos. Se fija para el ejercicio una base de cotización de 1.900 € y una base de retención de 1.900 €. La cuota conjunta del trabajador se modela, solo a efectos de aprendizaje, con un parámetro del 6,50 % y la retención con el 10 %. Estos porcentajes **no se presentan como tipos legales vigentes** ni desglosan contingencias.

```text
Devengado = 1.500 + 150 + 250 = 1.900,00 €
Cuota del trabajador del supuesto = 1.900 × 0,065 = 123,50 €
Retención del supuesto = 1.900 × 0,10 = 190,00 €
Deducciones = 123,50 + 190,00 = 313,50 €
Neto = 1.900 − 313,50 = 1.586,50 €
```

Si se añade una aportación empresarial ficticia de 570 €, el coste simplificado es 2.470 €. El neto del trabajador sigue siendo 1.586,50 €: esa aportación empresarial no se vuelve a descontar del recibo.

### Construcción

En Calc configura la región y el formato monetario. Sitúa los devengos en B2:B4; en B5 usa `=SUMA(B2:B4)`. Introduce base de cotización en B7 y base de retención en B8. Guarda tipos del ejercicio en E2 y E3 con formato porcentaje. Calcula en B10 `=REDONDEAR(B7*$E$2;2)` y en B11 `=REDONDEAR(B8*$E$3;2)`. El neto en B13 será `=B5-SUMA(B10:B11)`.

No escribas `6,50` en una celda sin formato esperando que sea 6,50 %: representa 650 % si luego se interpreta como proporción. Introduce `6,50%` o `0,065` con la configuración regional correspondiente. Añade una comprobación: devengado menos deducciones menos neto debe ser cero al céntimo.

### Variación y diagnóstico

Sube la retención del supuesto al 12 %. La nueva retención es 228 € y el neto 1.548,50 €. La diferencia de neto es 38 €, sin variación del bruto. Si la hoja muestra 3,80 €, hay un error en la escala porcentual. Si resta 570 € adicionales al neto, se han confundido aportaciones empresariales y del trabajador.

**Entregables:** archivo editable, PDF del recibo ficticio, parámetros y limitaciones del modelo. **Aceptación:** los cambios se propagan mediante fórmulas y se identifican al menos cuatro datos que faltan para una nómina real.

## Práctica 3. Leer una oferta y preparar preguntas de contrato

El escenario ofrece soporte presencial y remoto, gestión de inventario y desplazamientos puntuales. El anuncio menciona «técnico informático», una cantidad anual y disponibilidad, pero no aporta convenio ni distribución de jornada.

Construye una ficha con información conocida, inferencias y dudas. No conviertas «disponibilidad» automáticamente en una obligación ilimitada. Pregunta por funciones, grupo, centros de trabajo, jornada, compensaciones, modalidad contractual y convenio. Compara la retribución anual con el número de pagas y los conceptos incluidos antes de comparar importes mensuales.

La solución correcta no elige un convenio al azar por contener la palabra informática. Explica cómo verificar su ámbito con la actividad real de la empresa y su publicación. Para cada duda aporta una fuente oficial o identifica qué documento necesitas. Los anuncios orientan la búsqueda; no sustituyen el contrato ni el marco normativo.

**Entregables:** ficha de una página, cinco preguntas pertinentes y mapa de fuentes con fecha de consulta. **Aceptación:** distingue información ausente de incumplimiento probado y no incorpora datos personales de candidatos.

## Práctica 4. Plan personal de mejora de seis semanas

Escoge una competencia técnica y otra de comunicación. Ejemplo: recuperar permisos en Linux y explicar una intervención a una persona no técnica. El diagnóstico inicial consiste en una práctica breve sin instrucciones paso a paso. Conserva errores y tiempos como punto de partida, sin competir por rapidez a costa de seguridad.

Planifica dos sesiones semanales: una de estudio y una de aplicación. En la tercera semana realiza una prueba intermedia con una variante; en la sexta, repite el problema inicial con datos distintos. Usa criterios constantes: resultado, integridad, autonomía y explicación.

**Solución de planificación:** semanas 1–2, usuarios y permisos; 3–4, ACL y recuperación; 5, documentación de una incidencia; 6, prueba y revisión. Si la semana 3 revela que falta comprender grupos, se reajusta la secuencia y se registra el motivo. Cambiar el plan por evidencia es progreso, no fracaso.

**Entregables:** diagnóstico, calendario, registro de dos errores investigados y comparación final. No basta adjuntar certificados de asistencia: tiene que existir una tarea que antes no pudieras resolver y ahora puedas explicar y repetir.
