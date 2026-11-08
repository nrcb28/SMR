# Fundamentos de una oficina técnica fiable

## 1. El documento como sistema de información

Una aplicación ofimática no se limita a aplicar formato. Gestiona contenido, estructura, presentación y metadatos. El contenido es lo que se afirma: una fecha, un importe o un procedimiento. La estructura expresa las relaciones: un título pertenece a un apartado y una fila representa un equipo. La presentación decide cómo se muestra esa información. Los metadatos describen autoría, revisiones, idioma y propiedades del archivo.

Si construyes un índice escribiendo títulos y números de página a mano, su apariencia puede ser correcta, pero la relación entre apartados y páginas no existe para la aplicación. Al insertar dos páginas, los números quedan obsoletos. Un índice automático utiliza estilos y campos; actualizarlo recalcula sus referencias. La misma idea se aplica a una hoja: escribir un total como número rompe la relación con las partidas, mientras que una fórmula conserva la regla de cálculo.

Antes de crear un archivo define quién lo utilizará, qué decisiones tomará con él, cuál es la fuente de los datos y cómo comprobará que sigue siendo válido. Un presupuesto necesita moneda, fecha, impuestos y vigencia. Un inventario necesita identificadores únicos, estados y fecha de revisión. Una presentación necesita un propósito y una secuencia, no una copia de todas las páginas del informe.

## 2. Formatos, compatibilidad y conservación

| Formato | Uso adecuado | Riesgo que se debe revisar |
| --- | --- | --- |
| ODT, ODS, ODP | Edición nativa de Writer, Calc e Impress | Funciones nuevas pueden depender de la versión de la suite |
| DOCX, XLSX, PPTX | Intercambio con Microsoft Office | Cambios de fuentes, saltos, fórmulas, campos, gráficos o animaciones |
| PDF | Distribución con presentación estable | Puede perder etiquetas, enlaces útiles, formularios o capacidad de edición |
| CSV | Intercambio de una tabla plana | No conserva fórmulas, estilos, hojas múltiples ni tipos de datos explícitos |
| TXT UTF-8 | Texto plano y datos sencillos | No representa estructura visual ni objetos incrustados |
| PNG/JPEG/SVG | Imágenes de mapa de bits o vectoriales | Resolución, compresión, contenido activo y compatibilidad del visor |

Los formatos OpenDocument y Office Open XML suelen ser contenedores ZIP con documentos XML y recursos. Su extensión no garantiza que estén completos o que su contenido sea seguro. No renombres `informe.odt` a `informe.docx` para convertirlo: utiliza `Guardar como`, conserva el original y abre el resultado para revisarlo.

CSV necesita un contrato de intercambio. Especifica codificación, separador de campos, delimitador de texto, representación decimal, formato de fecha y si existe fila de encabezados. Los ejemplos de este módulo usan UTF-8, `;`, comillas dobles cuando resulten necesarias, coma decimal y fechas ISO `AAAA-MM-DD`. Un código `00027` debe importarse como texto para no perder ceros. Un número de teléfono o una referencia de producto no se vuelven cantidades por contener dígitos.

La conversión no es necesariamente reversible. Guardar una hoja como CSV puede conservar únicamente la hoja activa y los resultados visibles. Exportar un documento a PDF produce un entregable; no sustituye al original editable. Conserva una versión fuente, una versión de intercambio y una versión final cuando el proyecto lo requiera.

## 3. Tipos de datos y significado

Una celda puede contener texto, número, fecha, hora, valor lógico o fórmula. El formato visual no cambia necesariamente el tipo almacenado. Si escribes `120,00 €` como texto, aplicar después un formato monetario no convierte siempre el contenido en número. Un síntoma habitual es que una suma ignore celdas que aparentemente contienen importes.

Las fechas suelen representarse internamente mediante números de serie; el origen y la interpretación pueden variar entre aplicaciones y configuraciones. Escribir `04/05/2026` sin acordar el formato deja una ambigüedad entre día y mes. Para intercambiar datos utiliza ISO y verifica que la importación produzca fechas, no cadenas. Para duraciones superiores a veinticuatro horas utiliza un formato de duración, como `[HH]:MM`, en lugar de una hora del día que vuelva a comenzar al superar veinticuatro.

En dinero distingue base imponible, impuesto, total y redondeo. Una celda que muestra dos decimales puede almacenar más; el total de valores mostrados podría diferir de la suma interna. Define si redondeas cada línea o únicamente el total y documenta la decisión. No construyas una hoja contable copiando cifras que parecen correctas sin explicar su regla.

## 4. Estilos, temas y plantillas

Un estilo es un conjunto de propiedades aplicado a elementos del mismo tipo. En Writer existen estilos de párrafo, carácter, página, lista y tabla. El estilo de párrafo `Título 1` expresa un nivel de la jerarquía; un estilo de carácter como `Énfasis` modifica una parte del texto. Un estilo de página regula márgenes, encabezados o numeración. Mezclarlos obliga a corregir manualmente problemas que deberían resolverse de forma centralizada.

Una plantilla añade una estructura reutilizable: estilos corporativos, portada, secciones, campos y elementos predefinidos. No debe contener datos personales de un encargo anterior. Antes de publicar una plantilla revisa propiedades, comentarios, cambios pendientes, objetos incrustados y vínculos externos. Eliminar únicamente el nombre de la portada no elimina necesariamente la identidad del autor.

En Impress, el patrón de diapositivas cumple una función parecida. Controla posición de títulos, tipografía y elementos comunes. Si cambias veinte títulos individualmente, introduces veinte posibilidades de inconsistencia. Un patrón reduce ese trabajo, pero no garantiza legibilidad: se deben revisar contraste, tamaño y cantidad de información.

## 5. Accesibilidad desde el archivo fuente

La accesibilidad permite que una persona use el documento mediante distintos dispositivos o formas de percibir la información. Un lector de pantalla necesita estructura y orden de lectura; una persona con baja visión necesita contraste y capacidad de ampliación. El color por sí solo no comunica correctamente que una cifra es negativa o que un equipo está averiado.

Aplica estas decisiones durante la edición:

1. Utiliza títulos jerárquicos y listas reales, sin simularlos con tamaño de fuente o guiones sueltos.
2. Declara el idioma del documento para facilitar pronunciación y corrección.
3. Describe imágenes informativas con texto alternativo que explique su función; una imagen decorativa debe identificarse como tal cuando la aplicación lo permita.
4. Evita tablas para construir diseños. En tablas de datos, añade encabezados y explica unidades.
5. Escribe enlaces con propósito: «manual de restauración» informa más que «haz clic aquí».
6. No escondas información imprescindible en comentarios, notas visuales o animaciones.
7. Revisa el PDF exportado: etiquetas, marcadores, selección de texto y orden de lectura.

El comprobador automático encuentra ciertos problemas, pero no puede decidir si el texto alternativo explica bien un gráfico o si un orden de lectura tiene sentido. Una revisión humana es parte de la aceptación.

## 6. Datos relacionados frente a listas duplicadas

Una hoja es útil para análisis flexible; una base relacional resulta adecuada cuando hay entidades, relaciones y restricciones persistentes. En un taller, cada equipo pertenece a un aula y puede generar muchas incidencias. Si repites el nombre y la ubicación del aula en todas las incidencias, una mudanza obliga a cambiar muchas filas. Las discrepancias posteriores son anomalías de actualización.

Separa `AULA`, `EQUIPO` e `INCIDENCIA`. Una clave primaria identifica cada fila. Una clave foránea obliga a que una relación apunte a un registro existente. La normalización elimina duplicaciones que producen inconsistencias; no consiste en crear el mayor número posible de tablas. Un número de inventario puede ser único y resultar útil como clave candidata, aunque se utilice un identificador numérico interno como clave primaria.

`NULL` representa ausencia o desconocimiento, no cero ni texto vacío. Una fecha de cierre nula indica que la incidencia sigue abierta o no tiene cierre registrado. Para buscarla se escribe `IS NULL`; comparar `= NULL` no tiene el mismo significado. Una base que impide referencias inexistentes detecta errores antes de que aparezcan en informes.

## 7. Seguridad, privacidad y trabajo compartido

Las macros son programas. Pueden automatizar tareas legítimas, pero también modificar archivos o comunicarse con sistemas. No habilites macros simplemente para poder leer un documento desconocido. Conserva deshabilitada la ejecución automática y utiliza un archivo de pruebas para las automatizaciones que desarrolles. LibreOffice Basic, VBA y las API de objetos de cada suite tienen diferencias; una macro de Excel puede no ejecutar correctamente en Calc.

Los enlaces externos pueden revelar rutas o recuperar datos de ubicaciones que ya no son válidas. Revisa si una hoja depende de otro archivo antes de moverla. En documentos compartidos, asigna roles de lectura, comentario y edición según la necesidad. Un enlace que permite editar a cualquiera que lo conozca es un permiso amplio, aunque no aparezca en un buscador.

La coedición de una plataforma web no equivale a abrir simultáneamente un archivo local desde una carpeta compartida. Los archivos de bloqueo de escritorio ayudan a prevenir conflictos, pero no proporcionan siempre un historial de cambios completo. Conserva versiones identificables y define quién acepta cambios. Usa datos ficticios en este repositorio: una práctica puede demostrar exactamente la misma técnica sin publicar listados reales de alumnado, correos o contraseñas.

## 8. Control de calidad y reproducibilidad

Una entrega debe incluir versión de aplicación, configuración relevante, fuentes de datos y procedimiento para recalcular o regenerar resultados. Las capturas son apoyo; no sustituyen el archivo editable ni una explicación de la fórmula. Si una captura muestra `2.475,00`, el evaluador necesita saber si ese importe surge de la regla correcta.

Comprueba siempre tres niveles. En el nivel estructural, los campos, fórmulas y claves deben relacionarse correctamente. En el nivel numérico, calcula a mano una muestra y revisa límites, vacíos y duplicados. En el nivel de uso, abre el archivo como lo recibiría otra persona, con su tamaño de pantalla y sus permisos. Una hoja sin protección puede permitir borrar fórmulas; una hoja excesivamente bloqueada puede impedir introducir los datos autorizados.

### Fuentes primarias para ampliar

- [Documentación de Writer, Calc, Impress y Base](https://books.libreoffice.org/).
- [Importar y exportar CSV en Calc](https://help.libreoffice.org/latest/es/text/scalc/guide/csv_files.html).
- [Estilos de Writer](https://help.libreoffice.org/latest/es/text/swriter/guide/stylist_fromselect.html).
- [Tutoriales de accesibilidad documental de W3C](https://www.w3.org/WAI/tutorials/).
