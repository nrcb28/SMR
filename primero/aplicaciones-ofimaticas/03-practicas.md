# Prácticas de Aplicaciones ofimáticas

Las cuatro prácticas forman un proyecto de soporte a un taller ficticio. Utiliza únicamente los datos sintéticos incluidos. Los tiempos son orientativos y las rúbricas son propuestas didácticas del repositorio; el docente decide su evaluación oficial. Consulta antes la [guía técnica](02-guia-tecnica.md).

## Práctica 1 · Informe de mantenimiento y correspondencia

**Duración estimada:** 3–4 horas. **Objetivo:** entregar un informe que pueda revisarse y actualizarse sin rehacer su estructura. **Requisitos:** Writer, acceso a una carpeta local y un visor PDF independiente.

### Procedimiento

1. Crea `informe-mantenimiento.odt` y define idioma español. Añade una portada y los apartados «Objetivo», «Inventario», «Procedimiento», «Resultados» y «Recomendaciones» con estilos de título.
2. Configura el cuerpo con encabezado y pie; la portada no debe mostrar el número de página. Documenta los estilos de página utilizados.
3. Introduce una tabla de al menos seis equipos ficticios con código, ubicación y estado. Identifica las unidades y configura encabezados repetidos.
4. Inserta un diagrama propio o una imagen con licencia identificada. Añade texto alternativo, pie y una referencia cruzada desde el procedimiento.
5. Genera el índice. Después añade un nuevo apartado intermedio y actualiza campos: guarda evidencias de que se actualizan índice y referencias.
6. Registra cambios, modifica una recomendación y añade un comentario de revisión. Guarda una copia de revisión y otra limpia con los cambios resueltos.
7. Crea una carta de aviso usando [destinatarios.csv](ejemplos/destinatarios.csv). Conserva los ceros de `codigo` y genera tres cartas locales, sin utilizar correo electrónico.
8. Revisa propiedades y exporta el informe a PDF con estructura y marcadores. Abre el PDF con otro visor y comprueba texto seleccionable y enlaces.

### Aceptación y entregables

Entrega el ODT limpio, la copia de revisión, el PDF, las tres cartas y una ficha que explique cómo actualizar el índice y qué metadatos revisaste. Un título nuevo debe aparecer en el índice al actualizarlo; no se acepta corregirlo escribiendo encima. El texto no puede desbordar tablas o quedar oculto por imágenes.

**Rúbrica sobre 10:** estructura y estilos 3; referencias y actualización 2; correspondencia correcta 2; accesibilidad/exportación 2; explicación reproducible 1. Una imagen que sólo lleva texto alternativo genérico no cumple la finalidad de accesibilidad.

**Recuperación:** si el formato se desordena, inspecciona estilos y anclajes en una copia. No elimines el trabajo completo para volver a montarlo visualmente. Si la fuente de datos se pierde al mover carpetas, vuelve a vincularla y verifica los tres registros antes de regenerar.

## Práctica 2 · Inventario económico con Calc

**Duración estimada:** 3–5 horas. **Objetivo:** importar datos sin pérdida de significado y construir un análisis trazable. **Requisitos:** Calc y [inventario.csv](ejemplos/inventario.csv).

### Procedimiento

1. Importa el CSV con el contrato descrito en fundamentos. Anota opciones de separador, codificación, fechas y decimales; guarda como `inventario.ods`.
2. Añade base, impuesto y total utilizando el tipo en `$L$2`, según la guía técnica. Copia fórmulas hasta la fila 9 y verifica manualmente las líneas de EQ-001, EQ-006 y EQ-008.
3. Calcula base e impuesto totales. Cambia temporalmente L2 a 10% y demuestra que todas las líneas usan el mismo parámetro. Devuelve después el tipo al 21%.
4. Añade búsqueda exacta por código. Prueba EQ-003 y EQ-999; el primero debe devolver «Monitor 24 pulgadas» y el segundo una ausencia explícita. Explica la alternativa de compatibilidad elegida.
5. Configura validación de unidades y estado. Prueba cero unidades y un estado ajeno a la lista. No guardes valores inválidos como datos finales.
6. Filtra los equipos de Aula 1 y crea una tabla dinámica que sume base por aula y estado. Conserva el total general y contrástalo con el resumen original.
7. Añade un gráfico con título, categorías y unidad monetaria. Protege las fórmulas dejando entradas editables; conserva aparte una copia de trabajo sin protección si la necesitas.
8. Exporta un PDF del resumen y un CSV de una hoja de datos. Explica qué características se pierden al exportar a CSV.

### Resultados de referencia

Con IVA del 21%, las bases suman **2.390,00** y los impuestos **501,90**; el total es **2.891,90**. El Aula 1 concentra una base de **800,00**. Existen **seis** filas cuyo estado es Operativo. Estos valores describen el conjunto de ocho filas inicial; si modificas el origen deben cambiar coherentemente.

Entrega ODS, PDF, CSV exportado y una memoria breve con tres cálculos manuales, captura de una fórmula relativa y otra absoluta, prueba de ausencia y comparación de tabla dinámica. **Rúbrica:** tipos/importación 2; fórmulas/referencias 3; validación/búsqueda 2; análisis/gráfico 2; trazabilidad 1.

**Diagnóstico provocado:** sustituye en una copia el precio de EQ-002 por texto precedido de apóstrofo. Localiza el fallo mediante tipo y fórmula; no lo corrijas escribiendo un total fijo. Restaura el valor numérico y vuelve a contrastar el resultado.

## Práctica 3 · Base de datos de un taller

**Duración estimada:** 4–6 horas. **Objetivo:** representar relaciones, imponer integridad y consultar equipos con y sin incidencias. **Requisitos:** Base con motor Firebird incrustado operativo.

### Procedimiento

1. Dibuja el modelo con entidades, claves y cardinalidades antes de abrir Base.
2. Crea una base nueva llamada `taller.odb`. Ejecuta individualmente las sentencias de [taller.sql](ejemplos/taller.sql). Si una sentencia falla, conserva el mensaje y determina qué objetos ya existen antes de repetirla.
3. Comprueba que hay tres aulas, cuatro equipos y tres incidencias. Ejecuta las consultas de [consultas.sql](ejemplos/consultas.sql) por separado.
4. Intenta en una copia insertar una incidencia cuyo `ID_EQUIPO` sea 999. Debe rechazarse por integridad referencial. No desactives la restricción para obtener una captura de «éxito».
5. Intenta crear una incidencia Cerrada sin fecha de cierre. El diseño debe rechazarla porque contradice la regla de negocio. Explica por qué esta restricción complementa el formulario.
6. Construye un formulario principal/subformulario de equipos e incidencias. Usa un cuadro de lista para seleccionar aula y verifica el orden de tabulación.
7. Genera un informe de incidencias abiertas con código, aula, fecha, resumen y estado. Incluye fecha de generación y criterio de selección.
8. Cierra la base, copia el archivo y abre la copia en otra ubicación. Comprueba recuentos y una incidencia concreta: ésta es la prueba de restauración del ejercicio.

Entrega modelo, ODB cerrado correctamente, consultas guardadas, informe y ficha de pruebas positivas/negativas. **Rúbrica:** modelo 2; integridad 3; consultas 2; formulario/informe 2; recuperación 1.

**Resultado razonado:** PC-003 y PC-004 deben aparecer con cero incidencias en la consulta con unión izquierda. Si desaparecen, probablemente utilizaste una unión interna; si muestran uno, revisa si contaste todas las filas en lugar de la clave de la incidencia.

## Práctica 4 · Presentación y entrega interoperable

**Duración estimada:** 2–3 horas. **Objetivo:** explicar una decisión técnica apoyándose en evidencias comprensibles.

Crea una presentación de 6–8 diapositivas sobre el taller: propósito, inventario, distribución de costes, incidencias abiertas, propuesta de mantenimiento y verificación. Usa patrón, títulos informativos, un gráfico obtenido de Calc y un diagrama propio. Debe poder entenderse la conclusión sin distinguir colores concretos. Si incorporas multimedia, utiliza un clip propio breve con transcripción y prueba su reproducción desde otra carpeta.

Entrega ODP, PDF, recursos necesarios y notas del ponente. Abre la presentación en otro equipo o perfil; si no dispones de él, documenta esa limitación y revisa al menos con un visor independiente el PDF. Una conversión a PPTX es opcional y exige comparar sus diapositivas, no sólo comprobar que existe el archivo.

**Rúbrica:** secuencia argumental 3; evidencia numérica 2; legibilidad/accesibilidad 2; portabilidad 2; fuentes 1. Como cierre, escribe una recomendación de 150–250 palabras que conecte coste, estado y prioridad. No deduzcas que el equipo más caro es automáticamente el que debe sustituirse primero: relaciona la decisión con su función y diagnóstico.
