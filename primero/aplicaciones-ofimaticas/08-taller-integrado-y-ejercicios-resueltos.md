# 8. Taller integrado: comunicación, multimedia y problemas resueltos

[Índice de Ofimática](README.md) · [Documentos largos](05-documentos-largos-y-publicacion.md) · [Calc](06-modelos-calc-y-calidad-de-datos.md) · [Base](07-base-modelado-consultas-y-transacciones.md)

## 1. Una misma evidencia, varios productos

El trabajo ofimático de soporte no termina al obtener un cálculo. Hay que comunicarlo a quien decide, documentar sus límites y preparar instrucciones para quien ejecuta. Un único documento enorme que mezcle todos esos propósitos puede resultar difícil de utilizar. Produce una memoria técnica, una hoja verificable y una presentación breve conectadas por los mismos identificadores.

En el caso del aula sintética, la hoja calcula partidas, la base describe equipos e incidencias y el informe relaciona necesidades con una propuesta. La presentación comunica la decisión, no reproduce todas las celdas. La trazabilidad consiste en poder pasar de una conclusión de la diapositiva a una tabla del informe y de ahí a datos y fórmulas, sin inventar una fuente nueva en cada formato.

Define un diccionario común: `activo`, `aula`, `estado`, `fecha_corte`, `coste_neto` y `prueba`. Si una hoja dice «equipo» para una fila de un lote y la base lo usa para un activo individual, los recuentos no coincidirán aunque ambos archivos sean correctos según su propia estructura. Resuelve esa diferencia de granularidad antes de comparar cifras.

## 2. Diseñar una presentación que permita decidir

Empieza por una pregunta concreta: qué renovación es prioritaria, con qué coste y cómo se comprobará. Un guion útil tiene situación, evidencia, alternativas, propuesta, aceptación y próximos pasos. Cada diapositiva debe aportar una conclusión o una relación necesaria para comprenderla; una portada decorativa adicional no aporta evidencia por sí misma.

Usa un patrón para mantener títulos, numeración y créditos. La consistencia reduce trabajo de lectura, pero evita que el patrón imponga tamaños diminutos para encajar cualquier cantidad de texto. Si una tabla necesita ocho columnas y doce filas para justificarse, quizá pertenece al informe; en la presentación puede bastar un gráfico con el resultado y un enlace al anexo.

Un título como «El descuento reduce 191,90 de la oferta base» comunica la observación y permite comprobarla. «Análisis económico» sólo identifica una categoría. Acompaña la cifra con unidad y alcance: descuento de qué presupuesto, con qué fecha y bajo qué supuestos. Si presentas un porcentaje, indica el denominador.

Ensaya la exposición con el archivo final, pantalla y resolución previstos. Una fuente legible en tu portátil puede resultar insuficiente desde el fondo del aula. La exportación a PDF facilita consulta, pero no conserva necesariamente animaciones, medios o notas del orador. Entrega una alternativa textual a la información que sólo aparece al reproducir un vídeo.

## 3. Gráficos: precisión antes de decoración

Para comparar costes por categoría, usa barras con unidad monetaria y un orden justificado. Para una evolución temporal, una línea puede mostrar tendencia siempre que el eje temporal sea coherente. Un gráfico de dispersión relaciona dos magnitudes numéricas y no implica causalidad. Elegir por apariencia en lugar de por pregunta puede presentar una relación equivocada.

Un eje vertical recortado puede exagerar visualmente pequeñas diferencias en barras. En gráficos donde se use un intervalo distinto por una razón analítica, indícalo claramente y considera mostrar los valores. No combines euros y número de incidencias en un mismo eje como si fueran la misma magnitud. Un segundo eje exige explicación y puede hacer parecer relacionadas dos series que sólo comparten una escala escogida.

Incluye título informativo, leyenda útil y fuente. Usa etiquetas cuando ayuden a comparar, no para sobrecargar cada punto. El color no debe ser el único canal para distinguir categorías: posición, patrón, texto o símbolos pueden aportar redundancia. Para accesibilidad, añade un resumen textual del mensaje y facilita la tabla de datos cuando sea necesario.

Una cifra con tres decimales parece precisa, pero puede proceder de una estimación muy incierta. Ajusta el detalle mostrado al método de obtención. Si el consumo se estima por perfiles de carga, comunica los supuestos y el intervalo; mostrar `123,456789 kWh` no añade fiabilidad. Conserva mayor precisión interna si la operación la necesita y explica el redondeo de presentación.

## 4. Imágenes, audio, vídeo y OCR

Una captura de interfaz debe mostrar el contexto imprescindible para interpretar el paso. Recorta áreas irrelevantes, pero no elimines el nombre de una opción o un mensaje que sostiene la conclusión. Conserva original privado cuando proceda y publica una copia sanitizada. Difuminar texto puede dejar formas reconocibles; para eliminar datos de una imagen, utiliza un procedimiento de redacción y revisa el resultado exportado.

La resolución se calcula según tamaño final. Una imagen de 12 cm a 150 ppp requiere aproximadamente `12 / 2,54 × 150 ≈ 709` píxeles de ancho. Si se amplía una imagen pequeña, la interpolación suaviza o estima píxeles, pero no reconstruye la información que no se capturó. Para diagramas creados por ti, un formato vectorial puede conservar nitidez y facilitar edición.

En audio distingue frecuencia de muestreo, profundidad y compresión. En vídeo distingue resolución, fotogramas por segundo, bitrate, códec y contenedor. Reducir bitrate disminuye tamaño, pero puede introducir artefactos que hagan ilegible el texto de una demostración. Para una grabación de pantalla, ensaya un fragmento corto con la interfaz real antes de grabar una sesión larga.

Los archivos enlazados dependen de rutas; los incrustados viajan dentro del documento, aunque aumenten su tamaño. Prueba la entrega desde una carpeta limpia o un segundo equipo sin acceso al directorio original. Un medio que funciona únicamente porque todavía existe una ruta absoluta en tu perfil no está correctamente empaquetado.

El reconocimiento óptico de caracteres transforma una imagen en una propuesta de texto. Requiere revisión de cifras, signos, nombres técnicos y orden de lectura. Un `0` confundido con `O` puede romper un código de activo; una coma perdida altera un precio. Conserva la imagen como fuente y marca las dudas pendientes, en lugar de presentar la salida de OCR como transcripción comprobada.

## 5. Paquete de entrega y control de versiones

Organiza los archivos en carpetas de originales, datos sintéticos, resultados y documentación. Evita nombres como `final_final_bueno2`; utiliza identificador, versión y fecha cuando ayuden al proceso. El nombre no sustituye un historial: añade un registro de cambios que explique qué se modificó y por qué.

Incluye un README del trabajo con aplicaciones/versiones, productos, datos de entrada, instrucciones de apertura y limitaciones. Si usas una tipografía no disponible en el equipo receptor, comprueba la sustitución o utiliza una opción compatible con la política del centro. La apariencia puede cambiar por fuentes, impresora predeterminada o diferencias de motor de maquetación.

No incluyas datos reales de clientes, claves o capturas con información innecesaria. Revisa también notas de presentador, hojas ocultas, nombres definidos, comentarios, propiedades y vínculos externos. Ocultar una hoja no la elimina del archivo. Un PDF de publicación y el editable tienen superficies distintas de información y ambos necesitan revisión.

La copia de seguridad debe permitir recuperar el trabajo, no sólo contener una carpeta con ese nombre. Ensaya abrir un archivo desde una copia en otra ruta, confirmar registros y regenerar al menos un resultado. Para Base incrustado, copia con la aplicación cerrada; para archivos conectados a fuentes externas, conserva además la relación de dependencias.

## 6. Práctica integrada A: expediente de renovación

**Contexto:** el centro ficticio pide comparar la propuesta base de ocho partidas con una variante que eleva un 10 % los equipos y otra que reduce dos monitores. Trabaja con [modelo-costes.csv](ejemplos/modelo-costes.csv); no requiere comprar ni contratar nada.

**Procedimiento:** importa, valida y guarda el ODS. Construye cálculos y controles, compara los escenarios y redacta un informe en Writer con estilos, tabla de resultados y referencia a la hoja. Crea después seis diapositivas que expliquen decisión y aceptación. Registra qué cifras se copian como resultados fijos y cuáles se mantienen mediante vínculo, evitando vínculos frágiles a rutas personales.

**Pruebas:** modifica una cantidad y demuestra cómo se actualiza la hoja; actualiza después el informe y comprueba si la presentación conserva un valor antiguo. Esa prueba descubre el riesgo de duplicar resultados entre archivos. No hace falta automatizar todos los vínculos, pero sí establecer una revisión de coherencia antes de publicar.

**Entregables:** CSV original, ODS, ODT, PDF, ODP y registro de pruebas. Los valores de referencia deben coincidir con la política de redondeo descrita en Calc. **Rúbrica propia:** cálculos y escenarios 30 %, informe estructurado 25 %, comunicación 20 %, accesibilidad y empaquetado 15 %, pruebas de mantenimiento 10 %.

## 7. Práctica integrada B: panel de mantenimiento

**Contexto:** utiliza una copia nueva de la base del taller. Prepara consultas de equipos sin incidencias, incidencias abiertas por equipo y actividad del periodo. Incorpora a una copia los casos de aula vacía y equipo nuevo antes de aceptar el panel.

Exporta resultados a CSV con tipos y codificación documentados. Impórtalos en Calc y construye un resumen que conserve los ceros de entidades sin actividad. Redacta una página de interpretación: un equipo con cero incidencias registradas no demuestra que nunca haya fallado; puede reflejar falta de registro. Diferencia el hecho observado de la inferencia.

**Prueba negativa:** modifica una copia de la consulta para filtrar una columna derecha de un `LEFT JOIN` en `WHERE` y compara qué equipos desaparecen. Explica el cambio sin entregar esa consulta defectuosa como solución final. **Aceptación:** recuentos contrastados con las tablas, periodo explícito, ausencia conservada y fuente de cada gráfico identificada.

## 8. Práctica integrada C: procedimiento multimedia accesible

**Objetivo:** explicar cómo revisar una copia de seguridad de un documento, utilizando un archivo ficticio. Crea una guía de dos páginas y un vídeo corto o una secuencia de capturas comentadas. El contenido debe poder entenderse también sin audio y sin reproducir el vídeo.

Guioniza antes de grabar: estado inicial, copia, apertura desde otro destino y comprobación. Usa una captura con datos sintéticos, revisa legibilidad al tamaño final y añade subtítulos o transcripción. Ensaya desde una carpeta sin los originales para comprobar que no falten recursos.

**Entregables:** guion, editable, medios utilizados, versión de consulta y matriz de aceptación. **Criterios propios:** exactitud y recuperación 30 %, claridad del procedimiento 25 %, alternativas y accesibilidad 25 %, empaquetado y privacidad 20 %. No se valora una animación por su complejidad si dificulta seguir el paso.

## 9. Quince problemas con soluciones razonadas

### 1. Un índice pierde un título al actualizar

**Problema:** el texto tiene el mismo tamaño que los títulos, pero no aparece. **Solución:** comprobar estilo y nivel de esquema. La apariencia puede proceder de formato directo. Asigna el nivel correcto y actualiza el índice; escribir el título manualmente dentro del índice no corrige su origen.

### 2. La referencia «figura 2» apunta a una figura distinta

**Solución:** identificar si se escribió como texto o como campo. En el primer caso, sustituirla por una referencia cruzada al objeto y ensayar inserción de otra figura anterior. En el segundo, comprobar destino y actualización; el número visible no demuestra que la relación sea correcta.

### 3. Un código `0018` aparece como `18`

**Solución:** revisar el tipo de importación. Si el código es identificador, debe tratarse como texto. Un formato de cuatro dígitos puede reparar la apariencia, pero no garantiza exportar el mismo significado; repite la importación desde el original conservado y verifica la salida.

### 4. La suma no cambia después de añadir filas

**Solución:** comprobar el rango y la tabla dinámica por separado. Una fórmula que termina en la fila nueve no incluye la diez; actualizar una tabla tampoco garantiza ampliar un rango fijo. Documenta un rango controlado y prueba específicamente la incorporación de una fila nueva.

### 5. `SI.ERROR` hace que el presupuesto parezca más barato

**Solución:** si una búsqueda fallida se convierte en cero, el total deja de mostrar que falta un precio. Devuelve un diagnóstico y cuenta incidencias pendientes. La ausencia de mensajes de error no demuestra integridad del cálculo; puede significar que se han ocultado.

### 6. Un descuento del 5 % aparece como 500 %

**Solución:** se ha introducido `5` en lugar de `0,05` o no se ha utilizado una entrada porcentual apropiada. El formato porcentaje multiplica por cien la representación. Comprueba el valor, limita el dominio entre cero y uno y ensaya una partida conocida.

### 7. Dos formas de calcular tasas difieren un céntimo

**Solución:** comparar el punto de redondeo: por línea o sobre el agregado. Define una política y aplica el control correspondiente. No fuerces una celda para que coincida ocultando el céntimo; explica por qué la regla elegida produce esa diferencia.

### 8. Una tarea de 27 horas se muestra como 03:00

**Solución:** se está usando formato de hora del día, que se presenta dentro de un ciclo de 24 horas. Usa un formato de duración compatible o minutos enteros. Comprueba además que las fechas de inicio y fin estén registradas si la tarea cruza medianoche.

### 9. La base muestra un equipo sin incidencias con recuento uno

**Solución:** en una unión izquierda se ha usado `COUNT(*)`. La fila conservada existe aunque la incidencia sea nula. Cuenta la clave de incidencia y prueba el caso de ausencia. El resultado esperado es cero, sin eliminar el equipo del informe.

### 10. Un formulario permite elegir un aula inexistente

**Solución:** revisar lista de selección, valor almacenado y restricción de clave foránea. La interfaz debería mostrar nombres válidos y guardar su ID. Si el motor no protege la relación, otro cliente podría insertar un dato inválido aunque el formulario se corrija.

### 11. Se borra un equipo y desaparece su historia

**Solución:** revisar reglas de eliminación y si existe cascada. Para un historial de activos, puede ser necesario registrar baja y conservar relación. Restaura la copia de laboratorio en un destino separado y plantea una migración probada; no asumas que `ROLLBACK` recuperará una operación ya confirmada.

### 12. La presentación se abre pero el vídeo no funciona

**Solución:** distinguir recurso enlazado, códec y contenedor. Prueba desde una carpeta limpia y confirma que los medios viajan con la entrega o están incrustados según lo previsto. Conserva una alternativa textual para que la explicación no dependa de la reproducción.

### 13. Una captura queda borrosa en PDF

**Solución:** revisar resolución original, tamaño final, compresión y proceso de exportación. Reducir y volver a ampliar no recupera detalle. Calcula píxeles necesarios, recaptura el área relevante con datos sintéticos y verifica el PDF en un visor independiente.

### 14. Un OCR cambia `0,50` por `O,5O`

**Solución:** el resultado es una propuesta de reconocimiento, no un dato confirmado. Contrasta con la imagen, revisa columnas numéricas y registra dudas. La conversión automática a número puede fallar o, peor, producir un valor distinto si se aplican sustituciones sin criterio.

### 15. El PDF parece limpio, pero el ODT conserva información retirada

**Solución:** revisar cambios registrados, comentarios, metadatos y elementos ocultos del editable. Publica desde una copia revisada y conserva la versión de trabajo sólo en el ámbito autorizado. Eliminar el texto visible no demuestra que desaparezca todo su rastro del formato editable.

## Referencias y continuidad

Consulta [las guías oficiales de LibreOffice](https://books.libreoffice.org/), [la ayuda en español](https://help.libreoffice.org/latest/es/) y [los tutoriales WAI de W3C](https://www.w3.org/WAI/tutorials/). Para la implementación SQL utiliza la versión del [manual Firebird](https://firebirdsql.org/en/reference-manuals/) que corresponda a tu motor. Los criterios y ejercicios de este capítulo son propuestas didácticas propias.
