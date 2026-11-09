# Alineación de Seguridad informática con RA y criterios oficiales

[Índice del módulo](README.md) · [Retos desarrollados](10-retos-por-ra.md) · [Datos de trazabilidad](alineacion-ra.json)

Esta matriz identifica los **5 resultados de aprendizaje y 39 criterios** del módulo **0226** en el anexo I del [Real Decreto 1691/2007](https://www.boe.es/eli/es/rd/2007/12/14/1691). Se ha contrastado el marco de adaptación del [Real Decreto 499/2024, artículo séptimo](https://www.boe.es/eli/es/rd/2024/05/21/499). Consulta: **09/11/2026**. La distribución de curso y horas se consulta en el [currículo de Madrid](../../docs/curriculo-madrid.md); no se trasladan las antiguas horas mínimas del BOE a la tabla madrileña.

Los enunciados de RA se reproducen como texto normativo, normalizando únicamente los espacios. Las filas de criterios son **paráfrasis didácticas propias** y conservan la letra de la norma para localizarla. Las actividades, pruebas, evidencias y condiciones de aceptación son propuestas del repositorio: no modifican los criterios oficiales ni fijan ponderaciones del centro.

## Cómo utilizar la matriz

Lee el enunciado y localiza su letra de criterio antes de escoger una práctica. Consulta los materiales, prepara el reto y conserva artefactos y observaciones reales. Un enlace representa apoyo documental; no acredita que una persona haya adquirido el resultado. Distingue evidencia disponible, ensayo, limitación material y revisión pendiente.

Los criterios que exigen instalar, capturar, sincronizar, usar un periférico o restaurar necesitan una actuación observable. Un diseño o una captura de ejemplo no sustituye esa actuación. Si no dispones del recurso, documenta preparación y pendiente de ejecución, sin marcar el criterio como demostrado.

<a id="ra1"></a>
## RA1 · Seguridad pasiva y SAI

> Aplica medidas de seguridad pasiva en sistemas informáticos describiendo características de entornos y relacionándolas con sus necesidades.

**Localizador normativo:** RD 1691/2007, anexo I, módulo 0226, resultado 1 y criterios a)–i).

**Actividad:** [0226-RA1-A1 · Seguridad pasiva y SAI](10-retos-por-ra.md#ra1). El reto desarrolla la secuencia completa; las filas siguientes permiten revisar cada parte por separado.

**Materiales:** [05-riesgos-bia-y-diseno-de-controles.md](05-riesgos-bia-y-diseno-de-controles.md) · [10-retos-por-ra.md](10-retos-por-ra.md).

| Criterio | Qué se trabaja —paráfrasis— | Evidencia propuesta | Aceptación didáctica |
| --- | --- | --- | --- |
| 1.a | Justificar protección de información | Inventario e impacto | Se relaciona un dato con pérdida, alteración o exposición |
| 1.b | Distinguir seguridad física y lógica | Mapa de amenazas y controles | No se atribuye a un control una función distinta |
| 1.c | Definir ubicación y ambiente | Plano y ficha de condiciones | Acceso, ventilación y riesgos se justifican con el entorno |
| 1.d | Proteger físicamente equipos | Plan de acceso y anclaje | Se comprueban las medidas sin obstruir operación segura |
| 1.e | Verificar funcionamiento del SAI | Ensayo supervisado y registro | El fabricante y la supervisión permiten la prueba sin improvisar cortes |
| 1.f | Seleccionar puntos protegidos por SAI | Lista de cargas y cálculo | Se justifican capacidad, autonomía y dependencias de red |
| 1.g | Diseñar política mediante ACL | Matriz de identidades y operaciones | Los permisos coinciden con la función y se prueba denegación |
| 1.h | Justificar política de contraseñas | Política y proceso de recuperación | Se consideran fortaleza, MFA y custodia sin exponer claves |
| 1.i | Valorar biometría | Comparación y necesidad | Se analizan límites, alternativas y datos implicados |

La evidencia se conserva con versión, contexto y resultado real. Cada operación pendiente queda identificada; la aceptación de una parte no se extrapola a las demás letras del resultado.

<a id="ra2"></a>
## RA2 · Almacenamiento y recuperación verificable

> Gestiona dispositivos de almacenamiento describiendo los procedimientos efectuados y aplicando técnicas para asegurar la integridad de la información.

**Localizador normativo:** RD 1691/2007, anexo I, módulo 0226, resultado 2 y criterios a)–j).

**Actividad:** [0226-RA2-A1 · Almacenamiento y recuperación verificable](10-retos-por-ra.md#ra2). El reto desarrolla la secuencia completa; las filas siguientes permiten revisar cada parte por separado.

**Materiales:** [07-criptografia-copias-y-continuidad.md](07-criptografia-copias-y-continuidad.md) · [10-retos-por-ra.md](10-retos-por-ra.md).

| Criterio | Qué se trabaja —paráfrasis— | Evidencia propuesta | Aceptación didáctica |
| --- | --- | --- | --- |
| 2.a | Interpretar una política de almacenamiento | Requisitos y retención | Se identifican datos, responsable, RPO y conservación |
| 2.b | Considerar rendimiento y acceso | Tabla de factores y carga | Se relacionan capacidad, latencia, disponibilidad y permisos |
| 2.c | Clasificar métodos de almacenamiento | Inventario local y de red | Se distingue dispositivo, volumen, protocolo y servicio |
| 2.d | Explicar redundancia y distribución | Esquema y modos de fallo | Se distingue continuidad de respaldo independiente |
| 2.e | Elegir estrategias de backup | Plan justificado | Datos y objetivos determinan el tipo de copia |
| 2.f | Definir frecuencia y rotación | Calendario y puntos recuperables | El peor intervalo y retención están calculados |
| 2.g | Ejecutar estrategias distintas | Registros de dos métodos | Se verifica qué contiene cada copia y cómo restaurarla |
| 2.h | Identificar medios remotos y extraíbles | Ficha de soporte y custodia | Se explican riesgos y compatibilidad del medio |
| 2.i | Utilizar medios remotos y extraíbles | Copia y prueba desde destino | Se comprueba identidad del almacenamiento y acceso |
| 2.j | Crear y restaurar imagen de sistema operativo | Imagen coherente y VM recuperada | Se demuestra estado del sistema y arranque restaurado, no sólo un archivo |

La evidencia se conserva con versión, contexto y resultado real. Cada operación pendiente queda identificada; la aceptación de una parte no se extrapola a las demás letras del resultado.

<a id="ra3"></a>
## RA3 · Protección activa y recuperación de datos

> Aplica mecanismos de seguridad activa describiendo sus características y relacionándolas con las necesidades de uso del sistema informático.

**Localizador normativo:** RD 1691/2007, anexo I, módulo 0226, resultado 3 y criterios a)–f).

**Actividad:** [0226-RA3-A1 · Protección activa y recuperación de datos](10-retos-por-ra.md#ra3). El reto desarrolla la secuencia completa; las filas siguientes permiten revisar cada parte por separado.

**Materiales:** [06-hardening-y-cambios-seguros.md](06-hardening-y-cambios-seguros.md) · [10-retos-por-ra.md](10-retos-por-ra.md).

| Criterio | Qué se trabaja —paráfrasis— | Evidencia propuesta | Aceptación didáctica |
| --- | --- | --- | --- |
| 3.a | Seguir contingencia ante un fallo | Cronología y decisiones | La contención y retorno siguen un procedimiento conocido |
| 3.b | Clasificar malware | Matriz de comportamiento | Se distingue tipo, vía y efecto sin ejecutar muestras reales |
| 3.c | Actualizar para corregir vulnerabilidades | Versiones y comprobación | Se revisan avisos, dependencias y regresión después de actualizar |
| 3.d | Verificar procedencia de aplicaciones | Firma o repositorio validado | El origen se contrasta por un mecanismo de confianza |
| 3.e | Instalar y comprobar antimalware | Motor, firmas y prueba inocua | Se registra detección controlada y recuperación, sin malware real |
| 3.f | Recuperar datos | Ensayo sobre copia de un medio sintético | Se conserva origen y se verifica contenido recuperado |

La evidencia se conserva con versión, contexto y resultado real. Cada operación pendiente queda identificada; la aceptación de una parte no se extrapola a las demás letras del resultado.

<a id="ra4"></a>
## RA4 · Privacidad de las comunicaciones e identidad

> Asegura la privacidad de la información transmitida en redes informáticas describiendo vulnerabilidades e instalando software especifico.

**Localizador normativo:** RD 1691/2007, anexo I, módulo 0226, resultado 4 y criterios a)–h).

**Actividad:** [0226-RA4-A1 · Privacidad de las comunicaciones e identidad](10-retos-por-ra.md#ra4). El reto desarrolla la secuencia completa; las filas siguientes permiten revisar cada parte por separado.

**Materiales:** [02-guia-tecnica.md](02-guia-tecnica.md) · [10-retos-por-ra.md](10-retos-por-ra.md).

| Criterio | Qué se trabaja —paráfrasis— | Evidencia propuesta | Aceptación didáctica |
| --- | --- | --- | --- |
| 4.a | Inventariar y controlar servicios | Puertos y responsables | Cada listener tiene necesidad y alcance justificados |
| 4.b | Analizar fraude por ingeniería social | Caso y señales | Se propone verificación independiente sin interacción con atacantes |
| 4.c | Reducir tráfico no deseado | Reglas y resultados sintéticos | Filtros distinguen mensajes válidos y descartados sin pérdida no justificada |
| 4.d | Evitar observación de red cableada | Diseño y comprobación de cifrado | Se explica qué protege el canal y qué metadatos siguen visibles |
| 4.e | Comparar seguridad Wi-Fi | Matriz de protocolos | La elección se fundamenta en autenticación, cifrado y compatibilidad |
| 4.f | Describir firma y certificado | Modelo de confianza | Se distinguen identidad, firma, hash y cifrado |
| 4.g | Usar identificación digital | Archivo firmado y verificación | Original valida y una modificación de copia invalida la firma |
| 4.h | Configurar un cortafuegos | Reglas y matriz de flujos | Accesos permitidos y denegados coinciden, con retorno desde consola |

La evidencia se conserva con versión, contexto y resultado real. Cada operación pendiente queda identificada; la aceptación de una parte no se extrapola a las demás letras del resultado.

<a id="ra5"></a>
## RA5 · Expediente normativo de un servicio

> Reconoce la legislación y normativa sobre seguridad y protección de datos analizando las repercusiones de su incumplimiento.

**Localizador normativo:** RD 1691/2007, anexo I, módulo 0226, resultado 5 y criterios a)–f).

**Actividad:** [0226-RA5-A1 · Expediente normativo de un servicio](10-retos-por-ra.md#ra5). El reto desarrolla la secuencia completa; las filas siguientes permiten revisar cada parte por separado.

**Materiales:** [08-incidentes-privacidad-y-casos-resueltos.md](08-incidentes-privacidad-y-casos-resueltos.md) · [10-retos-por-ra.md](10-retos-por-ra.md).

| Criterio | Qué se trabaja —paráfrasis— | Evidencia propuesta | Aceptación didáctica |
| --- | --- | --- | --- |
| 5.a | Explicar legislación de datos personales | Ficha de normas y contexto | Se distingue texto histórico del marco actual aplicable |
| 5.b | Controlar acceso a información personal | Matriz y minimización | Sólo roles necesarios acceden y queda trazabilidad definida |
| 5.c | Identificar intervinientes legales | Mapa de roles del caso | Responsable y encargado se asignan según decisiones y funciones reales |
| 5.d | Atender derechos de las personas | Procedimiento y caso sintético | Se verifica identidad proporcional y canal autorizado sin revelar terceros |
| 5.e | Explicar normativa de servicios digitales | Ficha del servicio y obligaciones | Se diferencia web interna, publicación y actividad comercial del supuesto |
| 5.f | Comparar marcos de gestión de seguridad | Mapa de alcance | No se afirma certificación o ENS aplicable sin analizar la entidad |

La evidencia se conserva con versión, contexto y resultado real. Cada operación pendiente queda identificada; la aceptación de una parte no se extrapola a las demás letras del resultado.

## Ampliación curricular y revisión

Esta edición refuerza las acciones que podían quedar ocultas tras explicaciones generales. En Ofimática se concretan macros, asistentes, adquisición multimedia, correo y agenda; en Web se separan CMS, LMS, archivos, ofimática y aplicaciones de escritorio web; en Seguridad se distinguen medidas pasivas, imágenes, protección activa, identidad y obligaciones. La proximidad temática entre dos herramientas no convierte sus operaciones en equivalentes.

Para autoevaluarte, relaciona cada artefacto con sus letras y escribe qué prueba lo hace suficiente. Utiliza datos sintéticos y mínima información necesaria. La evaluación académica y las adaptaciones concretas las establece el centro, con sus instrumentos y programación.
