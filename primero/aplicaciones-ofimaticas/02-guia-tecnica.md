# Guía técnica de producción y mantenimiento ofimático

## 1. Preparar una instalación verificable

Descarga la suite desde el proyecto o desde el repositorio oficial de tu distribución. En Debian utiliza el gestor de paquetes; en Windows comprueba editor y firma del instalador antes de ejecutarlo. No mezcles extensiones de procedencia desconocida con el perfil de trabajo. Un paquete de idioma no implica que el formato regional haya cambiado: revisa ambos ajustes.

En una VM Debian preparada para la práctica, estas consultas son de lectura:

```bash
libreoffice --version
locale
apt-cache policy libreoffice libreoffice-base
```

La primera identifica la suite instalada. `locale` muestra el entorno del proceso, que no tiene por qué coincidir con todas las opciones internas de Calc. `apt-cache policy` permite comprobar versión disponible y origen de paquetes. Si faltan componentes, instálalos con el administrador de la VM después de revisar la propuesta del gestor. Algunas funciones de Base requieren un entorno Java compatible; utiliza únicamente uno soportado e identifica su ruta en las opciones avanzadas. No instales runtimes antiguos para seguir una captura de un manual.

Crea carpetas `fuentes`, `trabajo`, `exportaciones` y `evidencias`. Guarda primero el original y realiza una exportación independiente. El nombre `informe_v03_2026-11-08.odt` es más informativo que `final_definitivo_ahora_si.odt`; el historial de versiones debe explicar qué cambió y quién revisó cada revisión.

## 2. Writer: construir un informe mantenible

### 2.1 Estructura, estilos e índice

Crea un informe de mantenimiento con portada, resumen, inventario, procedimiento, resultados y anexos. Aplica `Título 1` a los apartados y `Título 2` a las subdivisiones. Define su aspecto modificando el estilo. La secuencia 1, 1.1, 1.2, 2 se configura con la numeración de títulos, no escribiendo esos números dentro de cada encabezado.

Inserta saltos deliberados. Un salto de página expresa que un apartado debe empezar en otra página; diez párrafos vacíos sólo simulan el mismo resultado con una fragilidad mucho mayor. Para una portada sin numeración y un cuerpo numerado, utiliza estilos de página y el salto que los conecta. Diferencia número de página impreso de posición física del PDF: una portada puede ocupar la primera página del archivo sin mostrar el número uno.

Inserta el índice desde el menú de sumario o tabla de contenido y selecciona los niveles que quieres mostrar. Después de editar títulos, actualiza los campos. Como verificación, cambia un título de lugar y comprueba que el navegador, el índice y la numeración reflejen el cambio. Si un título no aparece, revisa su nivel de esquema y su estilo antes de modificar el índice manualmente.

### 2.2 Tablas, imágenes y referencias

Una tabla de inventario debe tener encabezados que se repitan si continúa en otra página. Alinea los importes por su significado numérico y explica la unidad de las columnas. Evita combinar celdas en tablas que después deban importarse o leerse de forma secuencial. Si necesitas una disposición visual compleja, considera separar la tabla de datos del diseño de portada.

Inserta imágenes con una resolución adecuada a su tamaño final. Para una imagen de 10 cm a 150 ppp necesitas aproximadamente `10 / 2,54 × 150 = 591` píxeles de ancho. Aumentar una imagen de 200 píxeles no recupera detalle. Para diagramas sencillos utiliza SVG cuando el flujo de exportación lo soporte; conserva una alternativa rasterizada si el destinatario tiene un visor incompatible.

Añade pies mediante el mecanismo de títulos de ilustración e inserta referencias cruzadas hacia ellos. Si cambias el orden de las figuras, actualiza campos. Copiar «véase la figura 3» como texto fija un número que puede dejar de corresponder. El texto alternativo debe explicar el contenido relevante; «captura1.png» sólo identifica el archivo.

### 2.3 Combinación de correspondencia

Usa [destinatarios.csv](ejemplos/destinatarios.csv), cuyos datos son ficticios. Importa `codigo` como texto. Registra o selecciona la fuente de datos, crea una carta con campos `nombre`, `aula` y `fecha_revision`, y utiliza la vista previa para recorrer todos los registros antes de generar las salidas. No envíes correos: la práctica termina en documentos locales.

Comprueba el primer registro, el último, las tildes y un campo vacío. Una combinación puede terminar sin error técnico y producir una carta con espacios en blanco o datos del destinatario equivocado. Si exportas un PDF con todas las cartas, recuerda que quien reciba el archivo podrá ver todos los destinatarios. En trabajo real genera archivos separados cuando corresponda y verifica el permiso de cada salida.

### 2.4 Revisión y exportación

Activa el registro de cambios para una revisión, inserta comentarios con propósito concreto y acepta o rechaza cada cambio conscientemente. Antes de entregar, revisa los comentarios y propiedades. Una supresión registrada puede conservar texto que visualmente ya no se muestra en la vista final.

Exporta a PDF con etiquetas y marcadores cuando lo permita la aplicación. Si solicitas una variante de archivo, como PDF/A o PDF/UA, revisa sus requisitos: seleccionar una casilla no sustituye la validación ni garantiza que todo el contenido sea accesible. Abre el PDF, busca una frase, selecciona texto, recorre enlaces y comprueba que las imágenes aporten la información necesaria.

## 3. Calc: inventario, fórmulas y análisis

### 3.1 Importación controlada

Abre [inventario.csv](ejemplos/inventario.csv) mediante el diálogo de importación. Configura UTF-8, separador `;`, delimitador `"`, idioma regional español y columna `codigo` de tipo texto. Las columnas quedan así:

| Columna | Contenido | Tipo esperado |
| --- | --- | --- |
| A | codigo | Texto único |
| B | descripcion | Texto |
| C | aula | Texto |
| D | unidades | Entero positivo |
| E | precio_unitario | Número decimal |
| F | fecha_alta | Fecha |
| G | estado | Categoría |

Guarda como ODS antes de añadir fórmulas. Comprueba `=ESNUMERO(E2)` y `=ESNUMERO(F2)`; ambos deberían producir verdadero si se interpretaron correctamente los datos. Un formato visual de fecha no demuestra que una cadena se haya convertido en fecha. Conserva el CSV sin alterarlo para poder repetir la importación.

### 3.2 Referencias y reglas de cálculo

Añade H `base`, I `iva`, J `total`; en L1 escribe `Tipo IVA` y en L2 `21%`. Para la primera fila de datos:

```text
H2: =REDONDEAR(D2*E2;2)
I2: =REDONDEAR(H2*$L$2;2)
J2: =H2+I2
```

Copia hasta la fila 9. `D2` y `E2` son referencias relativas y avanzan con cada fila. `$L$2` fija tanto columna como fila, por lo que el tipo de impuesto permanece estable. `$L2` fija sólo la columna y `L$2` sólo la fila; las referencias mixtas son útiles, por ejemplo, en matrices de precios con productos por filas y descuentos por columnas.

En una celda de resumen utiliza `=SUMA(H2:H9)` para la base total, `=SUMA(I2:I9)` para los impuestos y `=SUMA(J2:J9)` para el importe completo. Con el archivo incluido y esta política de redondeo los resultados de referencia son **2.390,00**, **501,90** y **2.891,90**. Son valores calculados del conjunto didáctico, no el resultado de una prueba de escritorio realizada en tu instalación.

Para detectar cantidades no válidas establece validación de datos en D: entero entre 1 y el límite razonable del almacén. En G permite una lista `Operativo`, `En reparación`, `Baja`. Una validación no garantiza que datos pegados o importados se hayan revisado siempre; acompáñala de una comprobación de valores existentes. Protege las celdas con fórmulas y deja desbloqueadas las entradas cuando prepares una plantilla para otras personas. La protección de una hoja evita accidentes; no es un mecanismo de cifrado para secretos.

### 3.3 Condiciones, búsquedas y compatibilidad

Ejemplos de análisis sobre el mismo intervalo:

```text
=CONTAR.SI(G2:G9;"Operativo")
=SUMAR.SI(C2:C9;"Aula 1";H2:H9)
=SI(G2="Baja";"Retirar";"Mantener")
=SI.ERROR(INDICE(B2:B9;COINCIDIR("EQ-003";A2:A9;0));"No encontrado")
```

`CONTAR.SI` cuenta coincidencias; `SUMAR.SI` suma la columna indicada sólo en filas que cumplen la condición. La combinación `INDICE`/`COINCIDIR` busca una clave exacta y devuelve la descripción. El parámetro `0` de `COINCIDIR` evita una búsqueda aproximada que exigiría orden y tendría otro significado.

En LibreOffice desde 24.8 puede utilizarse BUSCARX; su disponibilidad y representación dependen de versión y configuración de nombres de funciones. Para un resultado escalar:

```text
=BUSCARX("EQ-003";A2:A9;B2:B9;"No encontrado";0)
```

Si tu asistente muestra `XLOOKUP`, utiliza ese nombre o cambia la configuración documentadamente. No entregues una hoja con una función desconocida para el destinatario: comprueba la suite receptora o utiliza una alternativa compatible. La ayuda oficial explica que esta función no pertenece al conjunto de fórmulas de ODF 1.3. Un archivo puede abrirse y conservar valores almacenados mientras falla al recalcular en otra aplicación. [Referencia oficial de BUSCARX](https://help.libreoffice.org/latest/es/text/scalc/01/func_xlookup.html).

`SI.ERROR` es útil para una ausencia prevista, pero puede ocultar referencias rotas si se aplica indiscriminadamente. Durante el desarrollo deja visibles los errores y corrige su causa. En la versión final distingue «no encontrado», «sin dato» y cero; representan situaciones distintas.

### 3.4 Filtros, tablas dinámicas y gráficos

Selecciona todo el rango con encabezados y activa el filtro automático. Filtrar oculta filas, no las elimina. Ordenar sólo una columna desasocia identificadores, descripciones e importes: verifica siempre la selección antes de ordenar. Una tabla con filas parcialmente seleccionadas puede quedar dañada sin que Calc emita un error.

Construye una tabla dinámica con `aula` en filas, `estado` en columnas y suma de `base` en datos. Al modificar el origen, actualiza la tabla. Si la suma aparece como recuento, comprueba si el campo contiene texto. Conserva un total general y contrástalo con la hoja de origen para detectar omisiones en el rango.

Elige un gráfico que responda una pregunta concreta. Barras para comparar aulas, líneas para una evolución temporal y dispersión para estudiar dos magnitudes continuas. Etiqueta ejes y unidades. Evita un eje recortado que exagere diferencias sin advertirlo y no uses un gráfico de sectores con categorías tan numerosas que ya no puedan compararse.

## 4. Base: taller relacional con Firebird incrustado

### 4.1 Crear el esquema

Crea una base nueva `.odb`, selecciona Firebird incrustado cuando esté disponible y guárdala antes de introducir datos. El archivo [taller.sql](ejemplos/taller.sql) contiene sentencias DDL e inserciones para este motor. En el diálogo `Herramientas → SQL` ejecuta **una sentencia cada vez**, sin el comentario introductorio si el diálogo no lo acepta; no todas las interfaces admiten un lote de sentencias. Actualiza la vista de tablas al terminar.

El modelo tiene `AULA → EQUIPO → INCIDENCIA`, con relaciones uno a muchos. La clave `ID_EQUIPO` de una incidencia debe existir en `EQUIPO`. No se incluye borrado en cascada: eliminar un equipo con historial debería requerir una decisión explícita, no borrar accidentalmente sus incidencias. El estado de una incidencia se limita mediante `CHECK` a los valores acordados.

Una base incrustada resulta útil para ejercicios individuales. No conviertas un `.odb` en servidor compartiéndolo para edición simultánea en una carpeta de red. Para concurrencia real utiliza un motor servidor y configura permisos, copias y conexiones según su documentación; Base puede actuar como cliente de ese motor.

### 4.2 Consultas y significado de las uniones

Abre [consultas.sql](ejemplos/consultas.sql). La consulta de incidencias abiertas utiliza `JOIN` para relacionar filas y `IS NULL` para fechas sin cerrar. La consulta con `LEFT JOIN` conserva equipos que todavía no tienen incidencias; si contaras `COUNT(*)`, cada equipo sin coincidencias seguiría aportando una fila y podrías obtener uno en lugar de cero. Por eso el ejemplo cuenta `I.ID_INCIDENCIA`.

Un filtro aplicado en `WHERE` sobre la tabla derecha de un `LEFT JOIN` puede descartar las filas sin coincidencia y cambiar el efecto de la unión. Decide si la condición pertenece a la relación o al resultado. Comprueba siempre la consulta con un equipo sin incidencias, no únicamente con registros que tienen coincidencias.

### 4.3 Formularios e informes

Crea un formulario principal de equipos y un subformulario de incidencias enlazado mediante `ID_EQUIPO`. Para elegir aula utiliza un cuadro de lista que muestre el nombre y almacene el identificador. Un cuadro de texto libre permite escribir un nombre que no coincida con ninguna aula o crear variaciones ortográficas.

Configura campos obligatorios y orden de tabulación. Ensaya alta, modificación y cancelación; cerrar una ventana no siempre equivale a descartar el registro. Un informe debe basarse en una consulta definida, mostrar fecha de generación y aclarar su filtro. «Incidencias» no explica si se incluyen cerradas, anuladas o únicamente las abiertas.

Guarda una copia del `.odb` **con el documento cerrado** antes de una modificación de estructura. Copiarlo mientras se están escribiendo datos puede producir una copia inconsistente. Una restauración de prueba consiste en abrir una copia aparte, consultar tablas y comprobar un conjunto de registros conocidos.

## 5. Impress y material multimedia

Empieza con un guion de cinco ideas: situación, evidencia, causa, propuesta y comprobación. Utiliza el patrón para títulos, numeración y créditos. Cada diapositiva debe apoyar la explicación oral; si necesita un párrafo largo, probablemente pertenece al informe. Los títulos que contienen la conclusión, como «Tres equipos concentran el coste de sustitución», ayudan más que «Resultados».

En imágenes rasterizadas, relaciona píxeles con el tamaño de presentación; en capturas recorta la información relevante y elimina datos privados antes de compartir. PNG conserva bordes y texto con precisión; JPEG suele ser adecuado para fotografía; SVG mantiene trazos vectoriales. No elijas un formato sólo porque el archivo pesa menos: revisa artefactos y legibilidad.

Si insertas audio o vídeo, distingue recursos incrustados de vínculos externos y comprueba el archivo en otro equipo sin acceso a tu carpeta original. El contenedor y el códec son conceptos diferentes: una extensión `.mp4` no garantiza que cualquier reproductor pueda decodificar sus pistas. Conserva una transcripción o subtítulos para el contenido hablado y una alternativa cuando el vídeo no pueda reproducirse.

Antes de entregar, ensaya con la resolución real, comprueba tipografías y abre una exportación PDF. El PDF conserva las diapositivas, pero no sus animaciones, transiciones ni necesariamente sus notas. Añade las fuentes de imágenes y datos, e identifica el material sintético de las prácticas como tal.

## 6. Automatización responsable

Empieza automatizando con estilos, plantillas, campos y fórmulas. Una macro sólo compensa si la tarea requiere lógica que esos mecanismos no expresan de forma mantenible. Documenta entradas, efectos y forma de deshacer la operación. Prueba en copias y no almacenes contraseñas en código o documentos.

Las grabadoras generan secuencias dependientes de selección y estado de la interfaz. Si se selecciona otra celda, una macro puede operar sobre datos distintos. Para distribuir automatizaciones revisa API, firma cuando proceda y política de macros del centro. Una advertencia de seguridad no se resuelve enseñando al usuario a desactivar todas las protecciones.

### Fuentes primarias

- [Guías oficiales de Writer, Calc, Base e Impress](https://books.libreoffice.org/).
- [Ayuda de Base](https://help.libreoffice.org/latest/es/text/sdatabase/main.html).
- [Referencia de Firebird](https://firebirdsql.org/en/reference-manuals/).
- [Compatibilidad de formatos de LibreOffice](https://help.libreoffice.org/latest/es/text/shared/guide/ms_user.html).
