# Retos de Aplicaciones ofimáticas organizados por RA

[Mapa completo de RA y criterios](09-alineacion-ra.md) · [Índice del módulo](README.md)

Los nueve retos siguientes desarrollan los nueve resultados de aprendizaje del módulo 0223. Cada actividad tiene un identificador estable para enlazarla con sus criterios de evaluación. Son propuestas docentes nuevas: el enunciado oficial y la letra de cada criterio se consultan en el mapa; las instrucciones, datos y condiciones de aceptación de este documento son didácticos.

Trabaja en un perfil de prácticas con documentos sintéticos, una copia del original y una carpeta de salida identificada. Registra suite, versión, idioma, configuración regional y sistema. En las tareas con periféricos, cuentas o un segundo dispositivo, diferencia la evidencia efectivamente obtenida de la preparación o simulación. Un vídeo prefabricado no demuestra que hayas capturado una secuencia y un archivo ICS importado una vez no demuestra sincronización.

Las rutas de menú son orientativas para LibreOffice y Thunderbird en español; anota las equivalencias de tu versión. No se ha ejecutado la suite ni sus asistentes durante la elaboración de estos retos. Cada estudiante debe producir sus documentos y registrar sus pruebas.

<a id="ra1"></a>
## RA1 · 0223-RA1-A1: instalación, componentes y actualización controlada

**Encargo:** preparar una suite para un puesto que redacta informes, calcula presupuestos y usa una base de datos de aula. La instalación debe conservar posibilidad de retorno y respetar la licencia. El puesto de prueba es una VM sin datos anteriores; no se modifica una instalación de trabajo.

Antes de descargar nada, escribe una ficha con arquitectura, sistema, espacio, componentes necesarios, idiomas, formatos y dependencias. Distingue instalar la suite completa de instalar sólo Writer/Calc. Base puede requerir componentes adicionales para ciertas funciones; comprueba el motor y los asistentes de informes en la documentación de tu distribución y versión. La ausencia de una dependencia no se diagnostica instalando paquetes al azar.

1. Identifica origen oficial del paquete, licencia y mecanismo de actualización. Para paquetes Debian, conserva la información del repositorio y de `apt policy`; para otro instalador, verifica procedencia, firma o suma conforme a su distribuidor.
2. Obtén copia o instantánea y registra versión anterior, si existe. Define qué documento usarás para comprobar compatibilidad después.
3. Revisa la transacción antes de confirmarla. En una VM Debian preparada, `apt -s install libreoffice` permite estudiar una simulación: no es prueba de instalación realizada. La instalación real requiere administración y revisión de sus cambios.
4. Instala los componentes decididos y configura idioma, rutas de plantillas, formato de guardado y recuperación automática según el encargo.
5. Comprueba apertura y exportación de un documento, una hoja y una base nueva. Registra un caso de incidencia real si aparece; si no aparece, describe un escenario como hipotético.
6. Ensaya quitar y reponer un componente prescindible del clon. Explica qué deja de funcionar y comprueba que los documentos siguen conservados.
7. Revisa las actualizaciones ofrecidas, aplica las autorizadas en la VM y repite la comprobación de archivos. Actualizar no significa aceptar una migración de formato sin revisión.

**Solución razonada:** la selección se justifica por requisitos y soporte, no por preferencia personal. Una licencia libre permite ciertos usos bajo sus condiciones; no implica que todo complemento o fuente tipográfica tenga la misma licencia. Un registro útil relaciona fase, decisión, cambio y prueba.

**Entregables y aceptación:** plan de fases, ficha de requisitos/licencias, relación de componentes antes/después, configuración y pruebas de archivos. El reto cumple cuando se demuestra instalación, configuración, modificación de componentes y actualización, con una incidencia documentada o un diagnóstico explícito y un mecanismo de retorno. Una captura de un icono no cubre esas operaciones.

<a id="ra2"></a>
## RA2 · 0223-RA2-A1: plantilla de manual con macro revisada

**Encargo:** entregar una plantilla para un manual de soporte de seis páginas que otra persona pueda reutilizar. Debe conservar jerarquía, tabla de contenido, numeración, una imagen y marca de revisión, y abrirse correctamente después de un intercambio de formato.

Define estilos para título, niveles de apartado, cuerpo, advertencia y pie de figura. Configura una barra o acceso rápido útil y documenta cómo volver a la configuración anterior. Introduce texto mediante teclado y una imagen adquirida por un periférico autorizado. Si usas OCR, conserva la captura original y corrige dos errores de reconocimiento; no presentes el OCR como transcripción garantizada.

Construye una plantilla y genera dos documentos distintos desde ella. El documento generado debe poder cambiar sin modificar la plantilla. Añade un índice automático, referencias y pies que no dependan de números escritos a mano. Exporta a PDF y a un formato de intercambio editable que puedas abrir en otra aplicación o perfil, comparando estilos, paginación, imágenes y campos.

El criterio de macros requiere crear y utilizar una macro; no lo sustituye una fórmula ni un estilo. En una copia sintética de Writer se puede crear una macro Basic que inserte una marca de revisión en el cursor:

```vb
Sub InsertarMarcaRevision
    Dim doc As Object
    doc = ThisComponent
    If Not doc.supportsService("com.sun.star.text.TextDocument") Then
        MsgBox "Abra el documento Writer de prácticas."
        Exit Sub
    End If
    doc.Text.insertString(doc.CurrentController.ViewCursor, _
        "Revisión local: " & Format(Now, "YYYY-MM-DD HH:MM"), False)
End Sub
```

Revisa el código antes de guardarlo y prueba sólo en el documento de prácticas. La hora es local; la macro no afirma UTC ni firma digital del documento. Asigna la macro a un botón o menú del documento y explica su ámbito. Conserva la política de seguridad de macros: no habilites globalmente archivos desconocidos para hacer desaparecer un aviso. La [ayuda oficial de LibreOffice](https://help.libreoffice.org/latest/es/text/shared/guide/scripting.html) describe ámbitos y asignaciones.

**Pruebas:** inserta la marca en un lugar previsto, deshaz y verifica que no se altera el resto del contenido. Abre una hoja para comprobar el mensaje de contexto y vuelve a Writer. El código se incluye como ejemplo para revisar, no como macro certificada o ejecutada aquí.

**Entregables:** plantilla, dos documentos, exportaciones, código, configuración personalizada y manual breve de reutilización. La solución explica diferencias entre plantilla, documento, campo automático y macro; documenta cualquier pérdida de interoperabilidad y no la oculta con una captura del original.

<a id="ra3"></a>
## RA3 · 0223-RA3-A1: hoja de cálculo con controles, gráfico y automatización

**Encargo:** crear una plantilla de inventario con códigos de activo, fecha, cantidades y coste, más un panel con totales y un gráfico. Usa los CSV sintéticos del módulo y conserva una copia de entrada sin modificar.

Separa hojas `Datos`, `Parametros`, `Resumen` y `Control`. En la importación decide delimitador, codificación, decimal, tipo de fecha y tratamiento de códigos que empiezan por cero. Un código es texto identificador, aunque contenga sólo dígitos. Comprueba una fila manualmente antes de calcular toda la tabla.

Utiliza referencias relativas para repetir operaciones y absolutas para una tasa o parámetro común. Incluye una referencia entre hojas y explica qué se desplaza al copiarla. Añade fórmulas con al menos una condición, una agregación y una búsqueda compatible con la versión. Evita ocultar errores indiscriminadamente: una búsqueda sin coincidencia debe tener un tratamiento explícito, no convertirse automáticamente en un importe cero.

Ordena y filtra una lista sin separar columnas de la misma fila. Aplica validación de categorías y protege celdas de fórmula, conservando editables las entradas. Prueba un formulario de datos si la versión lo ofrece y compara la introducción directa con el formulario. Introduce un número o código mediante un periférico disponible —por ejemplo lector en modo teclado— y registra su efecto; si no hay equipo, deja esa observación pendiente.

Construye un gráfico adecuado al dato y muestra título, unidades, categorías y origen. Cambia un dato para confirmar actualización. Un gráfico de sectores con demasiadas categorías no facilita comparar cantidades pequeñas; justifica la elección en lugar de aceptar el primer estilo.

Para crear y usar una macro, prepara `Control!B2` como campo reservado de estado. Una macro Basic puede recalcular la hoja y escribir allí la marca local:

```vb
Sub RecalcularPlantilla
    Dim doc As Object, hojas As Object
    doc = ThisComponent
    If Not doc.supportsService("com.sun.star.sheet.SpreadsheetDocument") Then Exit Sub
    hojas = doc.getSheets()
    If Not hojas.hasByName("Control") Then
        MsgBox "Falta la hoja Control del ejercicio."
        Exit Sub
    End If
    doc.calculateAll()
    hojas.getByName("Control").getCellRangeByName("B2").setString( _
        "Recalculado: " & Format(Now, "YYYY-MM-DD HH:MM"))
End Sub
```

Ejecuta sólo sobre la plantilla prevista, con copia y comprobación de la celda reservada. No se utiliza sobre libros reales ni sustituye la revisión de fórmulas. Exporta a CSV y a otro formato de hoja, reabre y compara tipos, fórmulas, gráfico, protección y macro: CSV no conserva toda esa estructura.

**Aceptación:** códigos y tipos correctos; fórmulas contrastadas; referencias justificadas; gráfico actualizado; validación y protección comprobadas; macro creada y utilizada; diferencias de exportación descritas. Entrega una tabla de pruebas con un valor válido, uno rechazado y una búsqueda sin coincidencia.

<a id="ra4"></a>
## RA4 · 0223-RA4-A1: base de aula con asistentes y macro de formulario

**Encargo:** administrar equipos, aulas e incidencias en una base nueva. Usa [taller.sql](ejemplos/taller.sql) como modelo de referencia, pero demuestra también el uso de asistentes que exige el RA. Ejecutar sólo SQL no demuestra que sabes configurar un formulario o informe con su asistente.

Dibuja entidades, claves y relaciones antes de crear. Crea una base Firebird incrustada de prácticas y registra su ubicación. Comprueba los requisitos de Java o componentes para los asistentes de tu edición; documenta el mecanismo que realmente utilizas. Inserta, cambia y elimina registros sintéticos, respetando integridad referencial. Un equipo referenciado por incidencias no debe desaparecer por una eliminación accidental sin política definida.

Crea con el asistente una consulta de incidencias abiertas. Selecciona campos y filtros, guarda la consulta y compara la vista SQL con una consulta equivalente del módulo. Crea después un formulario de altas con campos obligatorios y un informe agrupado por aula. Identifica qué resuelve cada objeto: tabla almacena, consulta selecciona, formulario facilita interacción e informe presenta.

Para el criterio de macros, crea una macro Basic de ayuda al formulario y asígnala al evento de acción de un botón dentro del archivo de prácticas:

```vb
Sub AyudaAltaIncidencia
    MsgBox "Use un equipo existente, fecha válida y estado del catálogo. " & _
           "Al cerrar una incidencia, complete también su fecha de cierre.", _
           64, "Ayuda del formulario de prácticas"
End Sub
```

La macro muestra instrucciones y no escribe en tablas ni modifica el motor. Su ejecución debe observarse desde el control asignado, no sólo desde el editor. Explica dónde se almacena y qué política de macros se aplica. Una macro Basic no es una macro VBA intercambiable sin revisión ni un disparador del servidor de base de datos.

**Pruebas:** buscar un equipo, filtrar abiertas, intentar una referencia inexistente, registrar una incidencia válida y abrir el informe. Elimina sólo un registro de prueba que pueda retirarse sin romper relaciones. Guarda una copia cerrada y reábrela en otro perfil; una base externa requiere respaldar datos y configuración, no únicamente el `.odb`.

**Aceptación:** se entregan modelo, base, consultas, formulario, informe, macro y resultados. La solución debe explicar un rechazo de integridad y conservar el conjunto original. Un informe visual no demuestra que la consulta filtre correctamente: comprueba sus filas y recuentos.

<a id="ra5"></a>
## RA5 · 0223-RA5-A1: adquisición de imagen y preparación para dos destinos

**Encargo:** capturar una tarjeta de prueba sin datos personales y preparar una versión para manual impreso y otra para web. Utiliza cámara, escáner u otro periférico autorizado y registra dispositivo, dimensiones de captura y ajustes. Generar una imagen por código es útil para otros ejercicios, pero no sustituye la adquisición por periférico de este criterio.

Conserva el original y trabaja en copia. Describe formato, anchura/altura en píxeles, profundidad de color cuando se conozca y tamaño del archivo. Separa resolución espacial en píxeles de densidad de impresión: cambiar la etiqueta de ppp sin crear o eliminar píxeles no aumenta detalle real.

Recorta el encuadre, endereza si procede y ajusta exposición o contraste con moderación. Prepara un PNG para conservar bordes/texto y una versión JPEG para estudiar compresión de una imagen fotográfica. Compara una zona al mismo tamaño de visualización; no elijas calidad únicamente por el tamaño del archivo. Una imagen pequeña ampliada por interpolación no recupera información que nunca se capturó.

Calcula un ejemplo: una imagen de 1.200 × 900 píxeles impresa a 300 ppp ocupa cuatro por tres pulgadas, antes de considerar márgenes de página. Si se utiliza a 600 × 450 píxeles en web, describe el cambio de tamaño y prueba legibilidad real. El tamaño sin comprimir de RGB de ocho bits por canal sería `1.200 × 900 × 3 = 3.240.000 bytes`; PNG o JPEG no tienen por qué ocupar eso.

**Pruebas:** importar y exportar ambos formatos, reabrir los archivos y comprobar dimensiones, color y legibilidad. Revisa metadatos y retira localización u otros datos innecesarios antes de compartir. Entrega original de aula, versiones, tabla de propiedades y explicación de decisiones. Si falta el periférico, registra qué partes se han practicado con un archivo sintético y qué adquisición queda pendiente de evidencia real.

<a id="ra6"></a>
## RA6 · 0223-RA6-A1: videotutorial reproducible de una operación

**Encargo:** elaborar un videotutorial de 60–90 segundos que enseñe a filtrar el inventario de Calc sin alterar filas. Debe incluir captura propia, edición, narración o textos equivalentes y una exportación verificable. Usa sólo el escritorio de prácticas y datos ficticios.

Planifica un guion con objetivo, preparación, acción y comprobación final. Diferencia captura de pantalla, pista de audio, clips, transiciones y subtítulos. Registra dimensiones, frecuencia de imagen, formato contenedor y códecs. MP4 es un contenedor; H.264 describe un códec de vídeo y no todo archivo MP4 usa exactamente la misma codificación.

Captura un ensayo corto y revisa permisos, audio y tamaño del texto. Importa la secuencia en un editor disponible y mantenido, como Kdenlive, y guarda el proyecto. Recorta pausas, ordena clips y añade títulos que describan la acción sin cubrir el dato importante. Revisa subtítulos y sincronización; el texto automático sin corregir no demuestra una explicación fiable.

Exporta una copia para reproducción y vuelve a importarla o ábrela en un reproductor distinto. Comprueba inicio, final, audio, legibilidad y duración. Para una tasa de 2 Mbit/s durante 60 segundos, el vídeo representa aproximadamente 15 MB antes de otros flujos y sobrecarga; ese cálculo orienta, pero no sustituye medir el archivo final.

**Aceptación:** proyecto editable, secuencia capturada, guion, exportación y tabla de comprobaciones. Debe verse que el filtro conserva la relación entre columnas y que la operación se puede repetir. Si un clip de terceros se usó como demostración, decláralo y añade captura propia: importar no cubre capturar. Retira los archivos de grabación que contengan accidentalmente información real según el procedimiento de tu centro; no los publiques para ilustrar el error.

<a id="ra7"></a>
## RA7 · 0223-RA7-A1: presentación de una intervención técnica

**Encargo:** explicar el trabajo anterior en seis diapositivas: problema, entorno, decisión, procedimiento, pruebas y recuperación. El destinatario debe comprender la conclusión sin leer bloques de comandos en letra diminuta.

Reconoce vista normal, esquema, clasificador, notas y presentación. Construye una plantilla con patrón o diapositiva maestra, tipografía coherente y contraste suficiente. Los colores no deben ser el único mecanismo para distinguir «correcto» y «fallido». Conserva encabezados significativos y comprueba orden de lectura de objetos cuando la aplicación permita inspeccionarlo.

Incorpora un gráfico con unidades y una imagen optimizada del RA5. Si incluyes el vídeo del RA6, decide si estará incrustado o enlazado y comprueba la entrega en otra carpeta o equipo: una ruta absoluta de tu usuario puede romper la reproducción fuera de él. No añadas animaciones que oculten información esencial o dependan de una temporización demasiado rápida.

Realiza una exposición usando el periférico disponible, por ejemplo una pantalla externa o proyector de aula. Comprueba resolución, duplicación/extensión de pantalla y visualización de notas sin exponer información privada. Si sólo has exportado un PDF, deja pendiente la prueba del periférico; exportar no demuestra ejecución en el equipo de presentación.

**Solución razonada:** la plantilla establece coherencia, pero cada diapositiva debe comunicar una idea y su evidencia. Una gráfica sirve para comparar datos; una captura sirve para observar un estado concreto. Las notas pueden contener detalles técnicos que no necesitan saturar la proyección.

**Entregables:** plantilla, presentación editable, copia distribuible, recursos necesarios y registro de ensayo. Acepta el producto cuando no faltan medios, títulos y cifras son legibles y el relato explica la comprobación y la recuperación, no sólo la instalación.

<a id="ra8"></a>
## RA8 · 0223-RA8-A1: correo, contactos y agenda sincronizada

**Encargo:** configurar dos tipos de cuenta de correo de laboratorio y una agenda compartida entre equipo y dispositivo móvil. El centro debe proporcionar cuentas sintéticas o un servidor de pruebas autorizado; no se necesitan credenciales de personas reales. Thunderbird es una opción de cliente, sin que esta actividad obligue a utilizar un proveedor público.

Antes de configurar, identifica remitente, destinatarios, asunto, cuerpo, cabeceras y adjuntos. Diferencia `Para`, copia y copia oculta, y explica qué datos se revelan a cada destinatario. Define necesidades de almacenamiento, acceso desde varios dispositivos, filtros, búsqueda, contactos y calendario.

Configura una cuenta IMAP y otra POP cuando el servidor y la política del laboratorio lo permitan, indicando diferencias de sincronización y conservación. Comprueba servidor, puerto, TLS y autenticación con la información suministrada; no deduzcas que SMTP y recepción tienen la misma dirección o credencial. No reduzcas protección de transporte para que una contraseña real pueda circular por la red. Si el laboratorio utiliza un servidor local no accesible desde el móvil, prepara la topología autorizada y su confianza antes de probar.

Crea tres mensajes ficticios, uno con adjunto y otro destinado a probar una regla. Prepara carpetas, etiqueta, búsqueda y filtro, y confirma qué mensaje cumple cada condición. Crea contactos, una lista de distribución de prueba y exporta/reimporta una copia; compara campos, no sólo número de entradas.

Para agenda, utiliza un calendario CalDAV de prueba o un mecanismo bidireccional documentado. Registra URL, zona horaria, cuenta y permisos. El servidor se prepara en [el complemento web](../../segundo/aplicaciones-web/11-complementos-curriculares.md), o se usa el proporcionado por el docente. Instala en el móvil un cliente compatible y utiliza sólo la cuenta de laboratorio, con CA y conexión adecuadas. Crea una cita desde el equipo, comprueba recepción en móvil, cambia hora desde móvil y confirma actualización en el equipo. Añade recurrencia, recordatorio y tarea si los productos lo admiten.

**Prueba negativa:** una cuenta sin permiso no debe modificar el calendario. Revisa qué pasa al perder conexión y al reconectar. Un archivo ICS importado manualmente es intercambio; no demuestra sincronización bidireccional. Si no hay móvil o cliente compatible, la sincronización queda pendiente y se conserva evidencia de la preparación sin declararla realizada.

**Entregables:** ficha de cuentas sin secretos, mensajes `.eml` sintéticos o capturas saneadas, libreta exportada, reglas, calendario y secuencia de sincronización. La solución debe identificar qué estado mantiene cada cliente y cómo evitar duplicados al importar copias.

<a id="ra9"></a>
## RA9 · 0223-RA9-A1: servicio de soporte con recuperación y transferencia

**Encargo:** atender una incidencia reproducible del conjunto anterior y entregar una guía que permita resolverla a otra persona. Elige un caso controlado: CSV importado como texto, índice de Writer no actualizado, recurso multimedia enlazado a una ruta inexistente o calendario configurado en modo sólo lectura.

Registra síntoma, alcance, versión, pasos y resultado esperado antes de modificar. Busca documentación oficial de la versión y distingue información de usuario, ayuda técnica y soporte del producto. Formula una hipótesis que prediga una comprobación: si el problema es el tipo de dato, cambiar sólo el formato visual puede no transformar texto en número.

Prepara una copia y ensaya el cambio con un archivo de prueba. Explica al usuario qué ocurre y qué dato necesitas, sin atribuirle culpa. Usa una guía visual con recortes de las pantallas relevantes, texto alternativo o explicación equivalente y una secuencia de comprobación. Una colección de capturas sin decisiones no constituye un procedimiento.

En el caso CSV, importa de nuevo con delimitador y decimal adecuados en una hoja nueva; contrasta recuentos, códigos y una operación aritmética. En el caso de vídeo, conserva el original y sustituye el enlace roto o incorpora el recurso de acuerdo con la política de entrega. En calendario, verifica derechos y cuenta efectiva en lugar de conceder escritura a todos.

Solicita a un compañero que siga la guía con otro fichero sintético. Registra dudas y corrige el documento. Comprueba que puedes volver al estado anterior y recuperar el archivo original. Acuerda un tiempo didáctico antes de empezar y explica desviaciones; no inventes un SLA oficial de la asignatura.

**Aceptación:** parte de incidencia, fuentes, guía visual, copia y recuperación, resultado real y comprobación por otra persona. La respuesta debe resolver la causa demostrada, conservar datos y dejar instrucciones suficientes para que el mismo problema no dependa de la memoria del autor.

## Autoevaluación y evidencias individuales

Para cada letra de criterio del mapa marca `no iniciado`, `ensayado`, `evidencia disponible` o `revisión pendiente`. Son estados del portfolio, no calificaciones oficiales. Un resultado que se trabaja en grupo necesita indicar qué operación realizó cada integrante y cómo puede explicarla o repetirla.

La revisión debe observar exactitud, independencia, conservación de datos y capacidad para razonar. Si una función no existe en la edición elegida, identifica una alternativa compatible que demuestre la misma acción; no elimines el criterio de la matriz. Conserva versión y límites para que el docente determine si la evidencia es suficiente.

## Fuentes primarias de trabajo

- [LibreOffice: ayuda oficial](https://help.libreoffice.org/latest/es/) y [guías](https://books.libreoffice.org/): Writer, Calc, Base, Impress y diferencias de funciones.
- [API de LibreOffice](https://api.libreoffice.org/): servicios UNO utilizados por los ejemplos Basic.
- [Thunderbird Support](https://support.mozilla.org/es/products/thunderbird): cuentas, contactos, calendario y sincronización.
- [Kdenlive Manual](https://docs.kdenlive.org/): captura, edición y exportación según versión.
- [Radicale](https://radicale.org/v3.html): CalDAV/CardDAV y clientes admitidos para un laboratorio propio.
