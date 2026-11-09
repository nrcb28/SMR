# 5. Writer avanzado: documentos largos, revisión y publicación

[Índice de la asignatura](README.md) · [Guía inicial](02-guia-tecnica.md)

## 1. El documento como sistema de información

Un informe de soporte puede contener instrucciones, evidencias, advertencias, tablas, anexos y referencias. Su calidad depende de que esas piezas sigan relacionadas cuando cambia el contenido. Si se añade un procedimiento, deben actualizarse la numeración, el índice y las referencias que apuntan a él. Un documento construido como una sucesión de párrafos con formato directo obliga a mantener esas relaciones manualmente y favorece errores silenciosos.

Antes de escribir, define propósito, audiencia y productos de salida. Una memoria de prácticas se entrega al profesorado para valorar el razonamiento; un procedimiento operativo se utiliza para ejecutar tareas y necesita precondiciones y recuperación; un informe ejecutivo justifica una decisión y debe presentar impacto, coste y evidencia. Pueden compartir datos, pero no requieren el mismo orden ni nivel de detalle.

Para el caso de estudio, crea un informe sintético de renovación de un aula con doce puestos. Tendrá portada, resumen, inventario, método de medición, resultados, propuesta, aceptación y anexos. El archivo editable será ODT; el PDF servirá para consulta. Los datos de costes se elaborarán en [Calc](06-modelos-calc-y-calidad-de-datos.md). Mantén identificadores estables de equipos y pruebas en ambos archivos para poder rastrear cada conclusión.

## 2. Diseñar una jerarquía de estilos

Un estilo de párrafo reúne propiedades de presentación y estructura: fuente, espaciado, sangría, comportamiento de salto, nivel de esquema y otras opciones. Crea o adapta una familia pequeña: cuerpo, títulos de niveles uno a tres, leyenda, nota técnica, bloque de comandos y encabezado de tabla. No es necesario crear un estilo diferente por cada párrafo; sí separar funciones que deban evolucionar de manera independiente.

Define el espaciado desde el estilo, evitando insertar párrafos vacíos para producir huecos. Configura los títulos para que se mantengan con el párrafo siguiente, de modo que un encabezado no quede al pie de una página separado de su contenido. Revisa las opciones de viudas y huérfanas en el texto corrido, pero evita imponer «mantener todos los párrafos juntos»: puede crear grandes áreas vacías y parecer un error de paginación.

El estilo de carácter expresa una diferencia dentro de un párrafo. Utilízalo para comandos, términos o énfasis cuando se necesite una presentación uniforme. Si un nombre de archivo debe conservar una fuente monoespaciada, un estilo de carácter permite corregir todos los casos de una vez. Aplicar un estilo de párrafo a una palabra seleccionada y esperar que sólo cambie esa palabra confunde los niveles de formato.

Comprueba qué procede de estilo y qué de formato directo. Un título puede tener estilo correcto y un tamaño aplicado manualmente que lo haga diferente de sus equivalentes. Elimina el formato directo de una copia del párrafo y observa si recupera la apariencia prevista. No borres indiscriminadamente formato de un documento ajeno: podrías perder cursivas o distinciones que todavía no se han trasladado a estilos.

### Procedimiento de preparación

1. Guarda una copia de trabajo y activa los caracteres no imprimibles para detectar saltos y párrafos vacíos.
2. Asigna estilo a cada sección antes de ajustar su apariencia.
3. Revisa el navegador de Writer: la jerarquía debe representar el contenido, sin saltar arbitrariamente de nivel uno a tres.
4. Modifica el estilo de título y comprueba que todos los títulos de ese nivel cambian juntos.
5. Inserta una sección nueva y verifica que adopta formato y nivel sin copiar manualmente otro encabezado.

El resultado esperado es consistencia estructural y visual. Que todos los títulos parezcan iguales no demuestra que tengan el mismo nivel de esquema; el navegador y el índice aportan una comprobación adicional.

## 3. Estilos de página, secciones y numeración

El estilo de página organiza tamaño, márgenes, columnas, encabezados y pies. La portada puede usar uno sin número visible; el cuerpo, otro con numeración. Ocultar un número de página no equivale a cambiar el número lógico de esa página. Decide si el cuerpo comienza en uno o continúa la secuencia y configura el salto correspondiente, en lugar de escribir números manuales en el pie.

Una sección permite aplicar disposiciones o propiedades a una región del contenido; no es sinónimo de estilo de página. Si el informe necesita una tabla ancha en orientación horizontal, lo habitual es emplear un estilo de página específico y saltos de entrada y salida. Si sólo necesitas dos columnas dentro de una página, una sección puede resultar más apropiada. El objetivo determina el mecanismo.

Ensaya la orientación horizontal con una tabla de diez columnas en un documento de prueba. Añade texto antes y después, actualiza campos y exporta. Comprueba que el encabezado, el pie y la numeración siguen siendo coherentes. Si las páginas siguientes también quedan horizontales, revisa qué estilo sigue al estilo aplicado o el salto de salida; añadir saltos vacíos suele esconder el problema.

No utilices tabulaciones repetidas para construir tablas de datos. Las tabulaciones sirven para alineaciones simples, pero una tabla aporta encabezados, relaciones y comportamiento de filas. Evita fijar la altura exacta de filas con texto variable: puede ocultarse contenido al cambiar fuente, idioma o visor. Si una fila se parte entre páginas y pierde sentido, modifica esa opción sólo cuando sea necesario.

## 4. Campos, leyendas y referencias verificables

Un campo representa un valor generado o una relación: fecha, página, título de capítulo o referencia. Distingue una fecha de creación, una fecha actualizable y una fecha fijada de emisión. Para una memoria cerrada, una fecha que cambia al abrir el documento puede alterar su significado. Etiqueta el campo y verifica su comportamiento antes de usarlo como evidencia temporal.

Inserta leyendas a tablas y figuras mediante su mecanismo correspondiente. Después inserta una referencia cruzada al objeto, seleccionando qué debe mostrar: número, texto o página. Si escribes «tabla 4» como texto, ese número no se adapta al insertar otra tabla. Para probar la relación, mueve la figura, añade una anterior y actualiza campos: deben cambiar número y referencia sin reescribir la frase.

El índice se genera a partir de estructura. Un título que no aparece suele tener un estilo o nivel incorrecto; escribirlo a mano dentro del índice crea una corrección que desaparecerá al actualizar. Actualiza antes de exportar y verifica al menos primer título, último título, una subsección y un anexo. Las referencias internas deben seguir abriendo el destino correcto en el PDF cuando se exportan como enlaces.

En bibliografía registra autor o entidad, título, versión o fecha y enlace. Las referencias a software deben identificar la versión cuando afecta al procedimiento. Una página de documentación que se actualiza continuamente necesita fecha de consulta; una norma requiere identificador y publicación. No inventes números de página para fuentes web ni atribuyas a una fuente una conclusión obtenida de tus propios datos.

El gestor bibliográfico de Writer puede automatizar parte de la presentación, pero la exactitud de los metadatos sigue siendo responsabilidad de quien documenta. Una cita formalmente bien presentada no demuestra que la fuente apoye la afirmación. Revisa esa relación durante la corrección técnica, separada de la corrección de estilo.

## 5. Plantillas mantenibles y documentos derivados

Una plantilla de procedimiento debe proporcionar estructura y campos que reduzcan omisiones: propósito, ámbito, requisitos, copia previa, pasos, aceptación, recuperación y referencias. Los textos de ayuda se distinguen claramente del contenido final. Un campo vacío no se debe eliminar sin decidir si la información es irrelevante o falta obtenerla.

Guarda como plantilla y crea dos documentos desde ella. Cambia un estilo en una copia de la plantilla y observa qué opciones ofrece la aplicación al abrir los documentos derivados. El vínculo con la plantilla y la propagación de estilos dependen del flujo utilizado; no presupongas que modificar un archivo maestro transforma automáticamente todas las entregas existentes.

Versiona la plantilla por cambios de significado. Añadir una columna «prueba negativa» al plan de aceptación requiere comunicar cómo usarla; cambiar el color del encabezado no tiene la misma consecuencia. Mantén un historial breve con fecha, versión y motivo. Si varias personas editan, define quién acepta cambios y cuál es la copia vigente.

Un documento maestro puede reunir subdocumentos para trabajos largos. Es útil cuando se separan capítulos, pero añade dependencias de rutas, estilos y actualización. Practica primero con un conjunto pequeño y conserva una copia completa del directorio. No lo elijas únicamente por superar un número arbitrario de páginas: si complica más que ayuda al equipo, un documento bien estructurado puede ser preferible.

## 6. Revisión con cambios y control de publicación

Activa el registro de cambios antes de la revisión y acuerda qué significa cada estado: propuesta, comentario, aceptado y pendiente. Un comentario debe formular un problema verificable, por ejemplo «el total no coincide con la hoja Costes», en lugar de «revisar esto». Si hay una duda técnica, conserva el comentario hasta resolver la fuente o la medición.

La vista final puede ocultar texto eliminado que continúa dentro del archivo como cambio registrado. Antes de publicar, acepta o rechaza de manera consciente, revisa comentarios y comprueba propiedades del documento. Trabaja sobre una copia de publicación para conservar la historia de trabajo en el espacio autorizado. Quitar el nombre del autor visible no garantiza borrar todo rastro de metadatos o revisiones.

Al comparar dos versiones, busca modificaciones de valores, unidades, rutas y condiciones, además de cambios de redacción. Sustituir «puede» por «debe» cambia una recomendación en requisito. Cambiar MB por Mb altera una cifra por un factor de ocho. En procedimientos, verificar la semántica de una pequeña modificación importa más que el tamaño del bloque modificado.

### Lista de aceptación editorial

| Requisito | Prueba | Evidencia |
| --- | --- | --- |
| Estructura coherente | Navegar por encabezados sin leer todo el informe | Mapa de capítulos y niveles |
| Referencias actualizadas | Insertar una figura y actualizar campos | Números y enlaces correctos |
| Datos trazables | Elegir tres cifras y llegar a su fuente | Celda, consulta o prueba identificada |
| Publicación limpia | Revisar cambios, comentarios y propiedades | Registro de revisión de la copia final |
| PDF utilizable | Buscar texto, navegar marcadores y abrir enlaces | Resultado real del visor elegido |

## 7. Accesibilidad del contenido y exportación

La accesibilidad empieza en el original. Asigna idioma, título y jerarquía; aporta alternativas a gráficos y no uses únicamente posición o color para explicar una instrucción. «Selecciona la opción roja de la derecha» resulta frágil si cambia la disposición o no se percibe ese color. Identifica la opción por su nombre y propósito.

En tablas identifica encabezados y evita estructuras que obliguen a interpretar muchas celdas combinadas. Para una matriz compleja, puede ser más comprensible presentar varias tablas pequeñas o describir el resultado principal antes de la tabla. Las imágenes de texto impiden ajustar presentación y dificultan búsqueda: conserva texto real salvo que la imagen sea evidencia de una interfaz y vaya acompañada de explicación.

Revisa contraste y tamaño en condiciones reales de lectura, pero no equipares una comprobación visual a una validación completa. El comprobador de accesibilidad de la aplicación ayuda a detectar errores definidos; no interpreta por completo si una alternativa textual explica el diagrama. La lectura y las pruebas con tecnologías de apoyo aportan información adicional.

Al exportar, selecciona etiquetas y marcadores apropiados cuando la versión lo permita. PDF/A se relaciona con preservación y PDF/UA con accesibilidad; son objetivos distintos. Incrustar fuentes ayuda a conservar apariencia, pero no recupera una jerarquía ausente. Verifica el PDF en un visor diferente y compara orden de lectura y contenido, además de la apariencia.

## 8. Práctica avanzada: informe técnico reutilizable

**Producto:** una plantilla ODT y un informe derivado de ocho a doce páginas orientativas sobre la renovación del aula sintética. La longitud es una referencia para distribuir contenido, no un criterio que premie rellenar páginas.

1. Diseña el índice y explica la finalidad de cada capítulo.
2. Crea estilos de cuerpo, tres niveles, leyenda y nota técnica.
3. Inserta dos tablas, una figura propia y sus referencias automáticas.
4. Incluye una página horizontal y vuelve después a la disposición normal.
5. Añade una tabla de aceptación con pruebas que todavía se puedan marcar como pendientes.
6. Realiza una revisión con al menos tres comentarios técnicos y tres cambios justificados.
7. Publica una copia limpia y un PDF, conservando el original de revisión por separado.

**Prueba de mantenimiento:** otra persona inserta una figura al comienzo, cambia un nombre de aula y añade una subsección. Debe poder actualizar índice y referencias sin reconstruirlos. Si un número queda antiguo, documenta la causa y corrige el mecanismo, no sólo el resultado visible.

**Evaluación orientativa:** estructura y estilos 25 %, trazabilidad y precisión 25 %, mantenimiento de campos 20 %, accesibilidad y exportación 20 %, memoria de comprobación 10 %. No se presenta esta ponderación como criterio oficial del módulo.

## Referencias primarias

- [Guías oficiales de LibreOffice](https://books.libreoffice.org/): consulta el manual de Writer correspondiente a tu versión.
- [Referencias cruzadas de Writer](https://help.libreoffice.org/latest/en-US/text/swriter/guide/references.html): inserción y actualización de relaciones internas.
- [Ayuda de Writer](https://help.libreoffice.org/latest/es/text/swriter/main0000.html): estilos, campos y exportación según instalación.
- [Tutoriales de accesibilidad de W3C WAI](https://www.w3.org/WAI/tutorials/): relaciones, contenido e interpretación de alternativas.
