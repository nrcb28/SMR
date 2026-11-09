# Alineación de Aplicaciones web con RA y criterios oficiales

[Índice del módulo](README.md) · [Retos desarrollados](10-retos-por-ra.md) · [Datos de trazabilidad](alineacion-ra.json)

Esta matriz identifica los **5 resultados de aprendizaje y 40 criterios** del módulo **0228** en el anexo I del [Real Decreto 1691/2007](https://www.boe.es/eli/es/rd/2007/12/14/1691). Se ha contrastado el marco de adaptación del [Real Decreto 499/2024, artículo séptimo](https://www.boe.es/eli/es/rd/2024/05/21/499). Consulta: **09/11/2026**. La distribución de curso y horas se consulta en el [currículo de Madrid](../../docs/curriculo-madrid.md); no se trasladan las antiguas horas mínimas del BOE a la tabla madrileña.

Los enunciados de RA se reproducen como texto normativo, normalizando únicamente los espacios. Las filas de criterios son **paráfrasis didácticas propias** y conservan la letra de la norma para localizarla. Las actividades, pruebas, evidencias y condiciones de aceptación son propuestas del repositorio: no modifican los criterios oficiales ni fijan ponderaciones del centro.

## Cómo utilizar la matriz

Lee el enunciado y localiza su letra de criterio antes de escoger una práctica. Consulta los materiales, prepara el reto y conserva artefactos y observaciones reales. Un enlace representa apoyo documental; no acredita que una persona haya adquirido el resultado. Distingue evidencia disponible, ensayo, limitación material y revisión pendiente.

Los criterios que exigen instalar, capturar, sincronizar, usar un periférico o restaurar necesitan una actuación observable. Un diseño o una captura de ejemplo no sustituye esa actuación. Si no dispones del recurso, documenta preparación y pendiente de ejecución, sin marcar el criterio como demostrado.

<a id="ra1"></a>
## RA1 · CMS con foro y mantenimiento

> Instala gestores de contenidos, identificando sus aplicaciones y configurándolos según requerimientos.

**Localizador normativo:** RD 1691/2007, anexo I, módulo 0228, resultado 1 y criterios a)–j).

**Actividad:** [0228-RA1-A1 · CMS con foro y mantenimiento](10-retos-por-ra.md#ra1). El reto desarrolla la secuencia completa; las filas siguientes permiten revisar cada parte por separado.

**Materiales:** [02-guia-tecnica.md](02-guia-tecnica.md) · [10-retos-por-ra.md](10-retos-por-ra.md).

| Criterio | Qué se trabaja —paráfrasis— | Evidencia propuesta | Aceptación didáctica |
| --- | --- | --- | --- |
| 1.a | Determinar requisitos del CMS | Ficha de compatibilidad | SO, PHP, base de datos y recursos encajan con la versión |
| 1.b | Gestionar roles de usuarios | Matriz de cuentas y operaciones | Cada rol ejerce sólo las funciones previstas |
| 1.c | Personalizar la interfaz | Tema o configuración documentada | La navegación y aspecto responden al encargo |
| 1.d | Probar funcionamiento del CMS | Plan de pruebas inicial | El visitante consulta y el editor publica contenido esperado |
| 1.e | Actualizar con atención a seguridad | Registro de actualización y retorno | Se valida compatibilidad, copia y resultado después del cambio |
| 1.f | Configurar módulos y menús | Inventario de extensiones y menú | Sólo se habilitan componentes necesarios y mantenidos |
| 1.g | Activar mecanismos de protección del gestor | Ajustes y pruebas negativas | Registro, roles y controles de edición limitan acciones indebidas |
| 1.h | Habilitar un foro con reglas de acceso | Foro y matriz de moderación | Usuario autorizado participa y el ajeno es rechazado |
| 1.i | Repetir pruebas tras cambios | Pruebas de regresión | Menú, foro y publicación siguen funcionando |
| 1.j | Respaldar contenidos del CMS | Copia de datos y configuración | Una restauración separada conserva contenido y roles |

La evidencia se conserva con versión, contexto y resultado real. Cada operación pendiente queda identificada; la aceptación de una parte no se extrapola a las demás letras del resultado.

<a id="ra2"></a>
## RA2 · LMS instalado y curso restaurado

> Instala sistemas de gestión de aprendizaje a distancia, describiendo la estructura del sitio y la jerarquía de directorios generada.

**Localizador normativo:** RD 1691/2007, anexo I, módulo 0228, resultado 2 y criterios a)–h).

**Actividad:** [0228-RA2-A1 · LMS instalado y curso restaurado](10-retos-por-ra.md#ra2). El reto desarrolla la secuencia completa; las filas siguientes permiten revisar cada parte por separado.

**Materiales:** [11-complementos-curriculares.md](11-complementos-curriculares.md) · [10-retos-por-ra.md](10-retos-por-ra.md).

| Criterio | Qué se trabaja —paráfrasis— | Evidencia propuesta | Aceptación didáctica |
| --- | --- | --- | --- |
| 2.a | Reconocer estructura del LMS | Mapa de código, datos y base | Se distingue document root de almacenamiento privado |
| 2.b | Cambiar aspecto del sitio | Tema y portada | La apariencia varía sin romper navegación ni permisos |
| 2.c | Crear perfiles personalizados | Cuentas y matrículas | Cada perfil accede al curso y funciones previstos |
| 2.d | Probar comunicaciones del curso | Foro y consulta sintética | Docente y estudiante intercambian mensajes según sus roles |
| 2.e | Importar y exportar contenidos | Paquete y copia importada | El contenido conserva estructura y no se confunde con copia completa |
| 2.f | Respaldar y restaurar | Copia del curso y restauración | Se recupera en curso o instancia separada con comprobaciones |
| 2.g | Obtener informes de uso | Informe saneado | Se interpretan eventos y límites sin atribuir actividad inexistente |
| 2.h | Comprobar seguridad del LMS | Matriz de acceso y almacenamiento | No se accede al curso o a datos privados sin permiso |

La evidencia se conserva con versión, contexto y resultado real. Cada operación pendiente queda identificada; la aceptación de una parte no se extrapola a las demás letras del resultado.

<a id="ra3"></a>
## RA3 · Gestión web de archivos

> Instala servicios de gestión de archivos web, identificando sus aplicaciones y verificando su integridad.

**Localizador normativo:** RD 1691/2007, anexo I, módulo 0228, resultado 3 y criterios a)–h).

**Actividad:** [0228-RA3-A1 · Gestión web de archivos](10-retos-por-ra.md#ra3). El reto desarrolla la secuencia completa; las filas siguientes permiten revisar cada parte por separado.

**Materiales:** [11-complementos-curriculares.md](11-complementos-curriculares.md) · [10-retos-por-ra.md](10-retos-por-ra.md).

| Criterio | Qué se trabaja —paráfrasis— | Evidencia propuesta | Aceptación didáctica |
| --- | --- | --- | --- |
| 3.a | Justificar gestión web de archivos | Caso de uso | Se distingue del acceso local y del simple listado público |
| 3.b | Comparar aplicaciones de archivos | Tabla de alternativas | Funciones, mantenimiento y control de acceso están contrastados |
| 3.c | Instalar y adaptar el gestor | Instancia y configuración | La instalación se completa con datos privados fuera del área pública |
| 3.d | Clasificar cuentas por permisos | Usuarios y grupos | La cuenta ajena no recibe acceso por defecto |
| 3.e | Gestionar archivos y directorios | Árbol y operaciones de prueba | Crear, mover, renombrar y recuperar conservan integridad |
| 3.f | Añadir información complementaria | Descripción o archivo README sintético | El contexto de cada conjunto es comprensible |
| 3.g | Aplicar indexación | Búsquedas y estructura | Se encuentra un archivo permitido sin revelar el privado |
| 3.h | Probar seguridad del gestor | Pruebas directas y por usuario | URL y búsqueda no eluden los permisos del recurso |

La evidencia se conserva con versión, contexto y resultado real. Cada operación pendiente queda identificada; la aceptación de una parte no se extrapola a las demás letras del resultado.

<a id="ra4"></a>
## RA4 · Ofimática web instalada y colaborativa

> Instala aplicaciones de ofimática web, describiendo sus características y entornos de uso.

**Localizador normativo:** RD 1691/2007, anexo I, módulo 0228, resultado 4 y criterios a)–g).

**Actividad:** [0228-RA4-A1 · Ofimática web instalada y colaborativa](10-retos-por-ra.md#ra4). El reto desarrolla la secuencia completa; las filas siguientes permiten revisar cada parte por separado.

**Materiales:** [11-complementos-curriculares.md](11-complementos-curriculares.md) · [10-retos-por-ra.md](10-retos-por-ra.md).

| Criterio | Qué se trabaja —paráfrasis— | Evidencia propuesta | Aceptación didáctica |
| --- | --- | --- | --- |
| 4.a | Justificar ofimática web | Necesidades de colaboración | Se explican conectividad, privacidad y recuperación |
| 4.b | Comparar tipos de aplicaciones | Documento, hoja y presentación evaluados | La selección responde a funciones requeridas |
| 4.c | Instalar la aplicación ofimática | Editor integrado y backend registrado | Se demuestra despliegue propio, no sólo uso de un SaaS |
| 4.d | Gestionar cuentas | Dos usuarios y un lector | Roles y bajas se reflejan en la aplicación |
| 4.e | Controlar acceso de usuarios | Matriz y enlaces compartidos | Una identidad sin permiso no abre ni edita el documento |
| 4.f | Reconocer prestaciones específicas | Documento y hoja creados | Se prueban funciones reales y límites de interoperabilidad |
| 4.g | Trabajar colaborativamente | Historial de edición concurrente | Dos usuarios modifican y observan cambios con sus identidades |

La evidencia se conserva con versión, contexto y resultado real. Cada operación pendiente queda identificada; la aceptación de una parte no se extrapola a las demás letras del resultado.

<a id="ra5"></a>
## RA5 · Webmail y calendario web

> Instala aplicaciones web de escritorio, describiendo sus características y entornos de uso.

**Localizador normativo:** RD 1691/2007, anexo I, módulo 0228, resultado 5 y criterios a)–g).

**Actividad:** [0228-RA5-A1 · Webmail y calendario web](10-retos-por-ra.md#ra5). El reto desarrolla la secuencia completa; las filas siguientes permiten revisar cada parte por separado.

**Materiales:** [11-complementos-curriculares.md](11-complementos-curriculares.md) · [10-retos-por-ra.md](10-retos-por-ra.md).

| Criterio | Qué se trabaja —paráfrasis— | Evidencia propuesta | Aceptación didáctica |
| --- | --- | --- | --- |
| 5.a | Comparar aplicaciones web de escritorio | Tabla webmail y calendario | Se distingue cliente web de servidor de correo o CalDAV |
| 5.b | Instalar un cliente de correo web | Instancia de Roundcube u otra mantenida | El frontend se sirve mediante HTTPS de laboratorio |
| 5.c | Integrar con servidor de correo | Configuración saneada de IMAP y SMTP | Se verifican ambos trayectos sin publicar secretos |
| 5.d | Gestionar cuentas del servicio | Identidades y permisos | Se explica qué componente administra realmente la cuenta |
| 5.e | Comprobar acceso al correo | Mensajes sintéticos enviados y recibidos | El cliente web muestra el buzón y confirma el envío |
| 5.f | Instalar calendario web | Frontend de calendario y CalDAV | Existe aplicación desplegada, no sólo archivo ICS descargable |
| 5.g | Usar citas y tareas | Eventos, tareas y prueba de zona horaria | Las funciones disponibles se verifican entre sesiones autorizadas |

La evidencia se conserva con versión, contexto y resultado real. Cada operación pendiente queda identificada; la aceptación de una parte no se extrapola a las demás letras del resultado.

## Ampliación curricular y revisión

Esta edición refuerza las acciones que podían quedar ocultas tras explicaciones generales. En Ofimática se concretan macros, asistentes, adquisición multimedia, correo y agenda; en Web se separan CMS, LMS, archivos, ofimática y aplicaciones de escritorio web; en Seguridad se distinguen medidas pasivas, imágenes, protección activa, identidad y obligaciones. La proximidad temática entre dos herramientas no convierte sus operaciones en equivalentes.

Para autoevaluarte, relaciona cada artefacto con sus letras y escribe qué prueba lo hace suficiente. Utiliza datos sintéticos y mínima información necesaria. La evaluación académica y las adaptaciones concretas las establece el centro, con sus instrumentos y programación.
