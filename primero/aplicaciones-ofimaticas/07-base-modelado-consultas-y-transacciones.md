# 7. Base avanzado: modelo relacional, consultas e integridad

[Índice](README.md) · [Esquema inicial](ejemplos/taller.sql) · [Consultas avanzadas](ejemplos/consultas-avanzadas.sql)

## 1. De una hoja única a relaciones explícitas

Supón una hoja con código de equipo, nombre de aula, responsable, fecha de incidencia, síntoma y estado. Si cada equipo tiene varias incidencias, se repiten sus datos en varias filas. Al renombrar el aula debes modificar muchas celdas; si una queda diferente, la base contiene dos versiones de un mismo hecho. El problema no se resuelve ordenando mejor la hoja: la estructura mezcla entidades con ciclos de vida distintos.

El modelo de la guía inicial separa `AULA`, `EQUIPO` e `INCIDENCIA`. Un aula puede existir sin equipos y un equipo puede no tener incidencias. Cada incidencia pertenece a un equipo. Las claves numéricas representan identidad interna; el código de inventario conserva una clave de negocio con restricción de unicidad. Una descripción no identifica de forma estable, porque puede cambiar o repetirse.

Antes de dibujar relaciones, redacta reglas de negocio. «Cada equipo se asigna a una sola aula actual» implica una clave foránea en equipo; «queremos conservar todos sus traslados» exige además una entidad de historial con periodos. No añadas una columna `aula_anterior` cada vez que se produzca un traslado. Una estructura que admite sólo un número fijo de eventos termina trasladando el problema a columnas nuevas.

## 2. Normalización con un caso de mantenimiento

La primera forma normal exige trabajar con valores adecuados al dominio de cada atributo y evitar grupos repetidos dentro de una fila. Para este caso, una celda que guarda `PC-001, PC-002, PC-003` no representa una relación administrable entre revisión y equipos. Una lista puede ser presentación, pero no es un sustituto de una tabla de detalle con una fila por asociación.

La segunda forma normal es relevante al analizar dependencias de una clave compuesta. Imagina una tabla `DETALLE_REVISION(ID_REVISION, ID_EQUIPO, FECHA_REVISION, CODIGO_EQUIPO, RESULTADO)`. La fecha depende de la revisión y el código del equipo, mientras el resultado pertenece a la combinación. Separa cabecera de revisión, datos de equipo y detalle. Así no repites una fecha de cabecera para cada equipo ni un código para cada revisión.

La tercera forma normal evita guardar dependencias transitivas inapropiadas. Si una fila de equipo incluye `ID_AULA` y `NOMBRE_AULA`, el nombre pertenece al aula y se deriva de la clave foránea. Mantenerlo en cada equipo introduce posibilidades de divergencia. Al consultar, une las tablas y obtén el nombre vigente. Si necesitas una «fotografía histórica» del nombre, justifica expresamente ese dato y su política de conservación.

La normalización es un método para analizar dependencias, no una competición por aumentar tablas. Un valor calculable puede materializarse por rendimiento o trazabilidad, pero requiere una regla para mantenerlo. En una base escolar pequeña resulta preferible calcular un recuento mediante consulta antes que almacenar un contador que debe actualizarse en cada alta o borrado.

### Ejercicio de diseño resuelto

**Regla:** una intervención puede utilizar varios repuestos y un repuesto puede aparecer en muchas intervenciones. Guardar `repuesto1`, `repuesto2` y `repuesto3` fija un límite artificial y dificulta calcular consumos. Crea `REPUESTO`, `INTERVENCION` y una tabla de unión con claves de ambos y cantidad positiva. Si el mismo repuesto sólo puede figurar una vez por intervención, la pareja puede ser clave primaria; si deben distinguirse lotes, amplía el modelo con una entidad o clave adecuada.

El precio actual del catálogo y el precio realmente aplicado son hechos distintos. Una intervención histórica no debe cambiar de coste porque se actualice el catálogo. Guardar precio aplicado en el detalle es una decisión justificada de trazabilidad, mientras duplicar la descripción sin motivo puede seguir siendo innecesario. El significado del dato determina su dependencia.

## 3. Cardinalidad, obligatoriedad y ciclo de vida

La cardinalidad expresa cuántas entidades se relacionan; la obligatoriedad determina si una asociación puede faltar. En el esquema existente, `EQUIPO.ID_AULA` es `NOT NULL`, por lo que todo equipo necesita un aula existente. Si un equipo puede estar en tránsito, hay que decidir si se crea una ubicación de tránsito o si se admite ausencia. No cambies a nulo sólo para sortear una validación sin revisar el significado.

Una clave foránea impide referencias a filas inexistentes. No decide por sí sola si borrar un aula debe borrar sus equipos. El esquema de prácticas no aplica borrado en cascada; esto obliga a tratar la eliminación conscientemente. Para activos con historia suele ser más adecuado registrar baja o estado de archivo que eliminar una fila que sostiene incidencias y evidencias.

Prueba las restricciones con operaciones sobre una copia nueva: código duplicado, equipo con aula inexistente, incidencia con fecha de cierre anterior a apertura y estado cerrado sin fecha. Registra error real del motor y qué requisito protege. Que una pantalla de formulario marque un campo obligatorio no sustituye la restricción del motor: otros clientes podrían escribir sin pasar por ese formulario.

## 4. NULL y lógica de tres valores

`NULL` representa ausencia de un valor conocido o aplicable según el diseño. No equivale a cero ni a texto vacío. Una comparación como `FECHA_CIERRE = NULL` no pregunta si el valor está ausente; utiliza `IS NULL`. En expresiones lógicas, las comparaciones con nulo pueden producir desconocido, que no se conserva como verdadero en `WHERE`.

En el taller, una fecha de cierre nula significa que todavía no se ha cerrado una incidencia. Esa interpretación la refuerzan los `CHECK` que relacionan estado y fecha. Si mañana aparece «cancelada», habrá que definir qué fecha necesita y modificar modelo, validaciones, consultas y formularios de forma coordinada. No basta con añadir una opción al desplegable.

Las agregaciones suelen ignorar valores nulos en su expresión. `COUNT(*)` cuenta filas del resultado; `COUNT(I.ID_INCIDENCIA)` cuenta valores no nulos de esa columna. Con un `LEFT JOIN`, un equipo sin incidencia produce una fila con columnas derechas nulas; contar el identificador de incidencia obtiene cero, mientras contar todas las filas obtiene uno. Ese pequeño detalle puede falsear un panel de actividad.

`COALESCE` selecciona el primer valor no nulo y puede resultar útil para una presentación. No lo utilices para ocultar incertidumbre del modelo. Mostrar «sin cierre» es diferente de convertir una fecha ausente en una fecha ficticia que después participe en medias de duración.

## 5. Uniones, filtros y recuentos correctos

La consulta de incidencias abiertas relaciona las tres tablas mediante `JOIN`. Para mostrar todas las aulas, incluidas las que no tengan equipos, parte de aula y utiliza `LEFT JOIN`. El orden conceptual y las condiciones determinan qué universo conservas. No existe una unión «más completa» que deba utilizarse en todos los informes.

Una condición sobre la tabla derecha en `WHERE` puede eliminar las filas conservadas por una unión izquierda. Para contar incidencias abiertas por equipo, sitúa la condición `I.FECHA_CIERRE IS NULL` dentro de `ON` y cuenta la clave no nula. Así conservas los equipos cuyo recuento debe ser cero:

```sql
SELECT E.CODIGO, COUNT(I.ID_INCIDENCIA) AS ABIERTAS
FROM EQUIPO E
LEFT JOIN INCIDENCIA I
  ON I.ID_EQUIPO = E.ID_EQUIPO
 AND I.FECHA_CIERRE IS NULL
GROUP BY E.CODIGO
ORDER BY E.CODIGO;
```

Con los datos iniciales, los valores esperados son uno para `PC-001`, uno para `PC-002` y cero para los otros dos equipos. Si agregas una nueva incidencia cerrada, no debe aumentar el recuento de abiertas. Este ensayo diferencia una consulta correcta de una que parece funcionar únicamente porque el conjunto original es pequeño.

Al unir varias relaciones uno a muchos, pueden multiplicarse filas. Si un equipo tiene dos incidencias y tres revisiones, unir ambas directamente puede generar seis combinaciones. Un `DISTINCT` añadido al final puede esconder el problema sin corregir sumas. Agrega primero cada relación al nivel de equipo o utiliza subconsultas con una estructura que preserve la granularidad del informe.

## 6. GROUP BY, HAVING y subconsultas

`WHERE` filtra filas antes de agrupar y `HAVING` filtra grupos después de la agregación. Para hallar equipos con al menos dos incidencias, agrupa por código y aplica `HAVING COUNT(I.ID_INCIDENCIA) >= 2`. Filtrar por fecha antes de agrupar cambia el periodo considerado; explica si quieres historial total o actividad de un intervalo.

Para detectar equipos sin incidencias, `NOT EXISTS` expresa directamente que no hay una fila relacionada:

```sql
SELECT E.CODIGO
FROM EQUIPO E
WHERE NOT EXISTS (
  SELECT 1 FROM INCIDENCIA I
  WHERE I.ID_EQUIPO = E.ID_EQUIPO
)
ORDER BY E.CODIGO;
```

Con el conjunto inicial deben aparecer `PC-003` y `PC-004`. Comprueba también un aula vacía y un equipo nuevo: los casos de ausencia son esenciales para aceptar consultas. No pruebes sólo entidades que tienen todas las relaciones pobladas.

Un informe temporal necesita intervalos sin ambigüedad. Para marcas de tiempo es habitual usar inicio incluido y final excluido, evitando construir un «último segundo del día» que no contemple precisión adicional. El esquema actual usa `DATE`, por lo que las consultas del archivo avanzado se basan en fechas. No mezcles tipos o sintaxis de MySQL, SQLite y Firebird sin revisar su documentación.

## 7. Transacciones y límites de la interfaz

Una transacción agrupa operaciones que deben tratarse como una unidad. Por ejemplo, registrar una intervención y su consumo de repuestos debería terminar completo o deshacerse si falla una parte. `COMMIT` confirma y `ROLLBACK` revierte cambios no confirmados de esa transacción; no es un mecanismo para deshacer cualquier modificación realizada días antes.

El cliente controla la conexión y puede activar autoconfirmación. El diálogo SQL de Base no debe presentarse como si fuera necesariamente una sesión interactiva que conserva una transacción entre varios botones. Antes de practicar control transaccional, utiliza una base de laboratorio nueva y una herramienta/conexión que permita conocer y configurar su política de autocommit. No ejecutes `ROLLBACK` esperando recuperar un `UPDATE` ya confirmado.

Los puntos de salvaguarda permiten volver a una etapa dentro de una transacción compatible, pero no equivalen a una copia de seguridad. Si la aplicación confirma al terminar cada sentencia, el flujo previsto cambia. El motor Firebird documenta `SET TRANSACTION`, `SAVEPOINT`, `ROLLBACK` y otros mecanismos; la forma de usarlos depende del cliente y de la versión incorporada.

En Base incrustado, conserva copias del `.odb` con el documento y conexiones cerrados antes de cambios de estructura. Una base servidor necesita un procedimiento propio de backup consistente. Copiar un archivo abierto de un motor sin comprender su formato y actividad no garantiza recuperar una transacción coherente.

## 8. Formularios que respetan el modelo

Un formulario de incidencias debe seleccionar equipo por una lista que muestre el código y guarde el identificador. Escribir el ID manualmente expone al usuario a errores de referencia; guardar sólo el código visible puede duplicar una clave que el esquema ya representa. Separa el dato almacenado de la etiqueta que ayuda a elegirlo.

En un formulario principal de equipos y subformulario de incidencias, revisa el enlace entre campos maestro y detalle. Si sólo filtras visualmente una tabla pero no configuras la relación al insertar, una nueva incidencia podría asociarse al equipo incorrecto. Ensaya alta con dos equipos, cambia de registro y verifica directamente las claves guardadas.

Un botón «Cerrar» debe ejecutar una transición coherente: asignar estado y fecha según las reglas. No hace falta programarlo para comprender el requisito; se puede practicar con edición controlada y comprobar que el motor rechaza una combinación inválida. Si se automatiza, documenta la operación y cómo maneja un fallo parcial.

No muestres más datos de los necesarios. Un panel de incidencias puede presentar código, fecha, resumen y estado sin revelar datos personales. Usa las identidades sintéticas de estos ejercicios y evita convertir un fichero escolar compartido en un almacén de información real sin una política aprobada.

## 9. Rendimiento y mantenimiento proporcionados

Las claves y restricciones suelen implicar índices, pero añadir índices a todas las columnas no garantiza mejorar el rendimiento. Un índice ocupa espacio y añade trabajo a las escrituras. Empieza identificando consultas reales, volumen y filtros; en el laboratorio pequeño, mide y explica el plan cuando la herramienta lo permita sin extrapolar diferencias de milisegundos a un servidor empresarial.

Una consulta que devuelve pocas filas puede leer muchas; una consulta rápida con cuatro equipos no demuestra buen comportamiento con millones. Del mismo modo, el coste observado en una VM bajo carga del anfitrión puede no provenir del SQL. Registra versión del motor, datos, consulta, repeticiones y condiciones antes de proponer un cambio.

Para mantener el esquema, prepara una migración en una copia con pasos, precondiciones y comprobación posterior. Si se añade una restricción, primero detecta datos existentes que la incumplen. Guardar el archivo con una versión nueva de la suite puede afectar compatibilidad del destinatario; conserva una copia anterior y ensaya restauración, no sólo apertura.

## 10. Práctica avanzada de consultas y control

Parte de una base nueva creada mediante el esquema inicial. Ejecuta cada consulta del [archivo avanzado](ejemplos/consultas-avanzadas.sql) de manera independiente. Entrega resultado esperado, resultado real y explicación del universo de filas.

Añade en una copia un aula sin equipos, un equipo sin incidencias y una incidencia cerrada de un equipo que ya tenga otra abierta. Predice los resultados antes de ejecutar. Después prueba violaciones de integridad sin conservar datos inválidos y documenta qué requisito protege cada error. No repitas inserciones con la misma clave sobre la base original.

Rúbrica didáctica: modelo y reglas 25 %, uniones y agregaciones 30 %, interpretación de nulos y ausencia 20 %, formularios y recuperación 15 %, memoria y fuentes 10 %. Se valora que una solución explique por qué funciona también en casos que no aparecen en la captura inicial.

## Referencias primarias

- [Manuales de referencia de Firebird](https://firebirdsql.org/en/reference-manuals/): selecciona la versión del motor utilizada por tu instalación.
- [Firebird 3.0 Language Reference](https://www.firebirdsql.org/file/documentation/html/en/refdocs/fblangref30/firebird-30-language-reference.html): SQL del motor y diferencias de cliente.
- [Control de transacciones en Firebird](https://www.firebirdsql.org/file/documentation/chunk/en/refdocs/fblangref50/fblangref50-transacs.html): consulta conceptual y contrasta compatibilidad de versión antes de ejecutar.
- [Ayuda oficial de LibreOffice Base](https://help.libreoffice.org/latest/es/text/sdatabase/main.html): formularios, consultas y administración del documento.
