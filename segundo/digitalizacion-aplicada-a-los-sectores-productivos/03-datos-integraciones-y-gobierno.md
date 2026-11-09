# Datos, integraciones y gobierno de una mejora digital

[Índice](README.md) · [Casos completos](04-casos-de-transformacion-y-costes.md)

## 1. Del trabajo real a un sistema de información

Una mejora digital debe conservar la relación entre necesidad, proceso, dato y decisión. En un taller de soporte, registrar una incidencia sólo tiene utilidad si permite asignarla, conocer su estado y comprobar la intervención. Añadir campos o pantallas sin una finalidad clara puede aumentar el tiempo de registro y producir información que nadie mantiene.

Descompón el proceso en eventos y estados. Un evento es algo ocurrido, como la recepción de una solicitud; un estado describe la situación actual, como pendiente de diagnóstico. “Recibida”, “en curso” y “cerrada” no deben mezclarse con prioridades como “alta”. Si un campo admite ambas categorías, después no podrás interpretar correctamente las estadísticas ni diseñar transiciones.

En el caso de esta carpeta, una incidencia pasa de recibida a clasificada, de clasificada a asignada, de asignada a en curso y de ahí a pendiente de validación o bloqueada. El cierre exige un resultado, una prueba y una fecha. Una reapertura conserva el historial: no se elimina la fecha anterior como si la primera intervención nunca hubiera existido. El modelo debe reflejar esa necesidad y no obligar a sobrescribir información útil.

Define quién puede realizar cada transición y con qué condiciones. Un solicitante puede aportar información, pero no confirmar por sí mismo una tarea administrativa que no ha ejecutado. Un técnico puede proponer cierre; la validación puede corresponder a otra persona según el procedimiento. La automatización debe respetar esas decisiones, en vez de deducir permisos a partir de que una API técnicamente admita una operación.

## 2. Modelo relacional y diccionario de datos

Separa entidades que tienen ciclos de vida distintos. Un activo puede tener múltiples incidencias y cambiar de ubicación; una incidencia puede incorporar varias actuaciones y piezas. Guardar todo en una tabla con columnas reparacion_1, reparacion_2 y reparacion_3 impone un límite artificial y dificulta consultar actuaciones de forma uniforme.

| Entidad | Identificador estable | Datos principales | Relaciones |
| --- | --- | --- | --- |
| Activo | activo_id | Código visible, categoría, estado, ubicación actual | Tiene incidencias y movimientos. |
| Incidencia | incidencia_id | Activo, apertura, categoría, prioridad, estado | Tiene actuaciones y validaciones. |
| Actuación | actuacion_id | Incidencia, tipo, fecha, resultado sintético | No cambia la identidad de la incidencia. |
| Movimiento | movimiento_id | Activo, origen, destino, fecha | Conserva historia de ubicación. |
| Catálogo | Código por catálogo | Categorías y estados permitidos | Evita variantes de escritura libres. |

Un identificador interno no tiene que ser el nombre visible del equipo. PC-014 puede cambiar por una convención organizativa; la relación histórica debe seguir apuntando al mismo activo. Tampoco uses número de fila de una hoja como identidad permanente: insertar o ordenar filas lo cambia. Documenta el origen y la regla de generación, y comprueba unicidad antes de aceptar una importación.

Para cada atributo define tipo, unidad, obligatoriedad, rango, finalidad y fuente. ram_gib es un número no negativo expresado en GiB; fecha_alta es una fecha o instante según necesidad, no una cadena indeterminada; estado pertenece a un catálogo. Si no conoces un dato, conserva un nulo documentado en lugar de inventar cero. Cero RAM y RAM desconocida expresan situaciones diferentes.

La calidad no se resuelve imponiendo todos los campos como obligatorios. Un campo obligatorio sin dato disponible fomenta valores ficticios. Distingue información necesaria para abrir una incidencia y datos exigidos antes de cerrarla. La restricción se aplica en el punto del proceso donde existe información y responsabilidad para cumplirla.

## 3. Importación CSV con área de preparación

Trata un CSV recibido como una entrada que debe interpretarse, no como una tabla ya validada. Declara codificación, separador, comillas, decimal, formato de fecha y tratamiento de vacíos. La convención de [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180) describe CSV con comas; un archivo separado por punto y coma requiere documentar ese dialecto y configurar el lector en consecuencia.

Supón un archivo didáctico con seis filas de datos:

~~~csv
codigo;ram_gib;fecha_alta;estado
PC-001;16;2026-10-01;activo
PC-002;8;2026-10-02;activo
PC-002;8;2026-10-02;activo
PC-003;16 GiB;2026-10-03;activo
PC-004;-8;2026-10-04;activo
PC-005;16;2026-02-31;activo
~~~

La preparación conserva archivo original, identificador de lote y número de línea. Un primer paso interpreta delimitación; otro valida tipos y catálogos. La normalización de “16 GiB” a 16 sólo es admisible si el diccionario confirma esa unidad y la regla queda registrada. No conviertas silenciosamente cualquier texto que contenga un número en una cantidad válida.

En este ejemplo se aceptan PC-001, PC-002 y PC-003; una fila es duplicado exacto y dos quedan rechazadas por RAM negativa y fecha imposible. La conciliación es 6 = 3 aceptadas + 1 duplicada + 2 rechazadas. Si dos filas del mismo código tuvieran valores distintos, no usarías automáticamente la última: sería un conflicto que requiere decidir fuente y precedencia.

Produce un informe de importación con conteos y motivos, sin volcar datos innecesarios. La persona responsable debe poder corregir las filas rechazadas y enviarlas como nuevo lote relacionado con el anterior. Reejecutar el mismo lote no debe crear otros tres activos. Para ello utiliza una identidad del lote y claves de negocio controladas, con una estrategia explícita para cambios legítimos posteriores.

## 4. JSON y contratos de intercambio

JSON representa objetos, listas, números, booleanos y nulos, pero no asigna por sí solo significado a cada campo. Un número 16 necesita unidad y el valor entrecomillado "false" contiene texto, no el booleano false. Un contrato define campos, tipos, versión, límites y tratamiento de atributos desconocidos.

~~~json
{
  "schema_version": 1,
  "asset_id": "LAB-PC-003",
  "ram_gib": 16,
  "status": "active",
  "observed_at": "2026-11-08T10:15:00Z",
  "source": "synthetic-lab",
  "notes": null
}
~~~

Este objeto es un ejemplo sintético, no una lectura ejecutada del laboratorio. La fecha indica un instante UTC; no debe reemplazarse por una fecha sin zona si se compararán eventos entre sistemas. observed_at expresa cuándo se obtuvo la observación, mientras received_at podría registrar cuándo llegó al servicio. Una transmisión retrasada puede hacer que ambos momentos sean distintos.

La versión del contrato permite introducir cambios sin romper consumidores de manera silenciosa. Añadir un campo opcional puede ser compatible con algunos clientes; cambiar el significado de uno existente puede no serlo. Documenta qué ocurre con campos desconocidos, valores nulos y estados nuevos. Una integración que descarta información sin avisar puede aparentar éxito mientras corrompe el proceso.

## 5. API, semántica e idempotencia

Una API necesita algo más que una URL. Define recurso, método, autenticación, autorización, contenido, respuesta y errores. Por ejemplo, consultar un activo es distinto de registrar una actuación y de modificar su estado. Mantén la API del ejercicio como un diseño o una simulación local hasta disponer de implementación y pruebas: escribir una petición en una memoria no demuestra que exista un servidor que la acepte.

En HTTP, la seguridad e idempotencia de métodos tienen significados específicos recogidos en [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110). Idempotencia significa que repetir una misma solicitud tiene el mismo efecto pretendido sobre el estado; no exige una respuesta idéntica ni prohíbe registros de cada intento. Un GET no debe usarse como orden escondida de borrar o cambiar un activo.

Una pérdida de respuesta no demuestra que una operación haya fallado. Si el cliente envió una creación, el servidor la procesó y la respuesta se perdió, repetir sin control puede duplicar registros. Diseña una clave de operación con ámbito, periodo de conservación y comparación del contenido. Esa clave es una decisión de la aplicación; escribir una cabecera cualquiera no garantiza que el servidor la implemente.

Para actualizar un registro, la concurrencia importa. Dos técnicos pueden leer la misma versión y guardar cambios distintos. Usa una versión o un mecanismo de precondición documentado para detectar que el dato cambió. Si se produce conflicto, presenta ambas versiones o pide recarga; no sobrescribas siempre con el último envío sin informar.

Define el tratamiento de fallos: autenticación inválida, permiso insuficiente, datos incorrectos, conflicto y saturación requieren acciones distintas. Un reintento automático sólo se justifica para condiciones previstas, con límite y espera. Reintentar indefinidamente un rechazo de autorización aumenta ruido y no corrige permisos. Registra identificadores de correlación y resultados sin incluir tokens ni cuerpos con datos sensibles.

## 6. IT/OT: intercambiar información sin controlar el proceso

En un ejercicio de convergencia, una pasarela recibe medidas sintéticas de temperatura y las exporta para análisis IT. El propósito es observar tendencias, no modificar un controlador real. Define dirección de flujo, frecuencia, unidad, tolerancia temporal y comportamiento ante ausencia de datos. No deduzcas que cero significa fallo de comunicación: puede ser una medida válida.

Separa el tiempo del sensor, el de la pasarela y el de recepción. Si hay retraso, una alerta debe indicar antigüedad de la última medida. Define cómo tratar duplicados, muestras fuera de orden y cambios de unidad. Un umbral sin duración y sin control de calidad puede generar alarmas por una única lectura espuria.

En la extensión de laboratorio utiliza redes virtuales independientes y una pasarela autorizada; no conectes la práctica a maquinaria ni a una red industrial. Un sistema OT necesita procedimientos de disponibilidad, seguridad funcional y soporte propios. La guía de [CISA sobre sistemas de control industrial](https://www.cisa.gov/topics/industrial-control-systems) sirve como punto de referencia para delimitar funciones, sin convertir este ejercicio en una intervención industrial autorizada.

## 7. Gobierno, responsabilidades y conservación

Asigna responsables por decisiones. El propietario del proceso valida el objetivo; el responsable del dato define significado y calidad; administración técnica mantiene servicio y recuperación; quien solicita puede validar que el resultado satisface su tarea. Una misma persona puede asumir varios papeles en una empresa pequeña, pero las decisiones no deben quedar implícitas.

Un catálogo de datos registra finalidad, ubicación, acceso, conservación y exportación. No copies todos los datos a todas las herramientas por comodidad. Un entorno de pruebas utiliza datos sintéticos o conjuntos preparados con autorización y garantías adecuadas. Cambiar nombres por códigos puede ser seudonimización y conservar posibilidad de identificación; no lo describas automáticamente como anonimización.

En servicios de nube, documenta responsabilidades por componente. La matriz de [responsabilidad compartida de Microsoft](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) ilustra que identidad, configuración y datos no desaparecen como responsabilidades del cliente. Para el producto concreto revisa contrato, retención, recuperación, administración y salida. Una certificación del proveedor no prueba que tu configuración sea correcta.

Para IA, registra tarea, entradas permitidas, salida, supervisión y criterio de retirada. Un clasificador de tickets no debe ejecutar cambios técnicos a partir de texto recibido. Separa evaluación lingüística de utilidad operativa: un resumen bien escrito puede omitir una advertencia o atribuir una causa inexistente. El [marco AI RMF de NIST](https://www.nist.gov/itl/ai-risk-management-framework) ofrece una referencia de gestión; los casos y umbrales de esta carpeta son propuestas didácticas propias.

## 8. Lista de aceptación del diseño

El diseño se acepta cuando permite seguir un registro desde su origen hasta una decisión, explicar quién puede modificarlo y reconstruir qué ocurrió ante un fallo. Debe existir una conciliación de entradas, un tratamiento de rechazados, un procedimiento de repetición y una exportación que pueda abrirse fuera del producto.

Pide a otra persona que intente resolver tres situaciones: lote repetido, valor desconocido y actualización concurrente. Si la respuesta depende de “el técnico sabrá qué hacer”, falta una regla. Si una regla destruye información que luego necesitas investigar, revisa conservación y trazabilidad antes de automatizarla.
