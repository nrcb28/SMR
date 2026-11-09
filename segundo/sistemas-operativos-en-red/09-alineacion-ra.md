# Alineación con resultados de aprendizaje · 0224

[Índice de la asignatura](README.md) · [Retos por RA](10-retos-por-ra.md) · [Datos de trazabilidad](alineacion-ra.json)

## Referente, interpretación y alcance

Este mapa identifica los **6 RA y 48 criterios de evaluación** del módulo Sistemas operativos en red en el anexo I del [Real Decreto 1691/2007](https://www.boe.es/eli/es/rd/2007/12/14/1691). Se ha contrastado el [RD 499/2024, artículo séptimo](https://www.boe.es/eli/es/rd/2024/05/21/499), que adapta la organización del título. Consulta: 09/11/2026. El reparto horario madrileño se explica en [currículo](../../docs/curriculo-madrid.md); no se utilizan aquí las antiguas horas de mínimos como horas de Madrid.

Los enunciados numerados de RA se reproducen del texto legal, normalizando espacios. Las descripciones de criterios de las tablas son **paráfrasis didácticas**, conservando sus letras; la norma enlazada contiene su redacción completa. Las actividades, evidencias y comprobaciones son propuestas originales. No son una escala oficial ni acreditan que una persona haya adquirido el RA por leer o completar un documento.

Usa cuatro estados en tu seguimiento: preparado, ejecutado, verificado y pendiente. «Preparado» significa que existe el plan; «ejecutado», que hubo una actuación real; «verificado», que la evidencia satisface la comprobación; «pendiente», que falta medio, supervisión o prueba. Conserva resultados reales e identifica por separado los ejemplos sintéticos. Las tareas físicas, colaborativas o de un producto no disponible no se dan por adquiridas mediante una sustitución declarativa.

## Cómo construir el dossier

Abre una ficha por RA, añade los documentos de estudio y prepara los objetos de laboratorio. Antes de ejecutar escribe qué criterio pretende demostrar cada paso y qué resultado lo contradice. Después conserva artefacto, contexto, identidad, versión y conclusión. Una captura aislada sin procedimiento puede mostrar un estado, pero no la secuencia que lo produjo ni su recuperación.

La actividad A1 integra los criterios del RA salvo que se indique A2. Las actividades A2 separan actuaciones que requieren otro entorno, material o supervisión. Esta separación permite registrar la parte real pendiente sin ocultarla detrás de un informe. Las guías de estudio enlazadas se complementan con el nuevo reto; un enlace no demuestra por sí solo cobertura práctica.

<a id="ra1"></a>
## RA1

> Instala sistemas operativos en red describiendo sus características e interpretando la documentación técnica.

Instalar un servidor combina diseño de almacenamiento, componentes y automatización con actualización y prueba desde clientes. No se limita a una captura de escritorio. La propuesta amplía instalación repetible mediante ficheros de respuesta saneados, sin entregar un script listo para borrar discos o incrustar credenciales.

**Estudio:** [02-guia-tecnica.md](02-guia-tecnica.md) · [07-operacion-automatizacion-y-recuperacion.md](07-operacion-automatizacion-y-recuperacion.md) · [10-retos-por-ra.md](10-retos-por-ra.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 1.a | Estudiar compatibilidad del servidor | Matriz de recursos, arquitectura y soporte | Requisitos oficiales y funciones previstas satisfechos |
| 1.b | Distinguir modos de instalación | Comparativa interactiva, desatendida y actualización | Explica cuándo se usa cada modo y sus riesgos |
| 1.c | Planificar y realizar particionado del servidor | Plano y acta sobre disco virtual nuevo | Destino inequívoco y separación justificada; sin comandos genéricos de borrado |
| 1.d | Seleccionar y aplicar sistemas de archivos | Decisión y estado posterior | Compatibilidad con roles, permisos y recuperación |
| 1.e | Elegir componentes a instalar | Inventario de roles y paquetes | Sólo lo necesario y conflictos de puertos identificados |
| 1.f | Automatizar instalaciones | Plan de respuestas o preseed saneado y ensayo | Datos sintéticos, ningún secreto y ejecución sólo en destino desechable |
| 1.g | Aplicar preferencias de entorno | Acta de perfil administrativo de laboratorio | Configuración personal sin debilitar controles del servidor |
| 1.h | Actualizar el sistema de red | Registro de versión, cambio y validación | Copia/retorno y prueba de dependencias tras reinicio si procede |
| 1.i | Comprobar conectividad servidor–clientes | Matriz IP, DNS y servicio desde cliente | No confunde proceso activo con operación remota aceptada |

**Actividades vinculadas:** [0224-RA1-A1: Servidor instalado y documentado mediante plan repetible](10-retos-por-ra.md#ra1) — CE a, b, c, d, e, f, g, h, i

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra2"></a>
## RA2

> Gestiona usuarios y grupos de sistemas operativos en red, interpretando especificaciones y aplicando herramientas del sistema.

Gestionar identidades incluye cuentas de equipo y perfiles además de usuarios y grupos. Se planifica un perfil móvil con soporte y restricciones antes de desplegarlo; sincronizar una carpeta no demuestra que exista un perfil itinerante. La membresía se comprueba en la sesión que utiliza el recurso y no sólo en una consola administrativa.

**Estudio:** [02-guia-tecnica.md](02-guia-tecnica.md) · [05-directorio-identidades-y-gpo.md](05-directorio-identidades-y-gpo.md) · [07-operacion-automatizacion-y-recuperacion.md](07-operacion-automatizacion-y-recuperacion.md) · [10-retos-por-ra.md](10-retos-por-ra.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 2.a | Administrar cuentas de usuario | Altas/cambios/baja de cuentas sintéticas | Propiedades verificadas y ninguna cuenta real afectada |
| 2.b | Administrar perfiles de usuario | Ficha de perfil y prueba de preferencias | Distingue cuenta, perfil, carpeta personal y redirección |
| 2.c | Administrar cuentas de equipo | Inventario de objetos y cliente unido | Objeto corresponde al equipo y se comprueba canal del dominio |
| 2.d | Distinguir tipos y ámbitos de grupos | Matriz local/global/universal/local de dominio | Ámbito compatible con función y pertenencias del diseño |
| 2.e | Administrar grupos | Acta de grupos funcionales y de permiso | Nombres y finalidad definidos; sin privilegios excesivos |
| 2.f | Gestionar membresía | Matriz antes/después y sesión efectiva | Acceso cambia conforme al grupo tras renovar contexto |
| 2.g | Reconocer cuentas y grupos especiales | Inventario crítico con función | No modifica o elimina cuentas integradas sin motivo autorizado |
| 2.h | Planificar perfiles móviles | Diseño de versiones, almacenamiento, permisos y conflicto | Incluye soporte, capacidad y prueba; no confunde sincronizar documentos con perfil móvil |
| 2.i | Usar herramientas de administración | Registro GUI/PowerShell o herramientas Linux | Explica objeto y ámbito de cada herramienta |

**Actividades vinculadas:** [0224-RA2-A1: Ciclo de vida de identidades y planificación de perfiles](10-retos-por-ra.md#ra2) — CE a, b, c, d, e, f, g, h, i

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra3"></a>
## RA3

> Realiza tareas de gestión sobre dominios identificando necesidades y aplicando herramientas de administración de dominios.

Este RA incluye establecer una relación de confianza, no sólo definirla. Se añade una extensión aislada con dos dominios y evidencia real de dirección, autenticación y autorización. Si sólo existe un DC, se puede preparar el diseño y la prueba, pero el criterio de establecimiento se marca pendiente de laboratorio.

**Estudio:** [01-fundamentos.md](01-fundamentos.md) · [02-guia-tecnica.md](02-guia-tecnica.md) · [05-directorio-identidades-y-gpo.md](05-directorio-identidades-y-gpo.md) · [10-retos-por-ra.md](10-retos-por-ra.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 3.a | Explicar servicio de directorio y nomenclatura | Mapa de DN, objetos, OU y atributos | Distingue nombre DNS, DN, UPN y grupo |
| 3.b | Reconocer dominio y funciones | Diagrama de límites de autenticación y administración | Distingue dominio, bosque y grupo de trabajo |
| 3.c | Establecer confianza entre dominios | Acta de relación real en extensión aislada | Dirección y alcance comprobados; confianza no concede permisos automáticamente |
| 3.d | Instalar directorio | Acta de instalación de DC dedicado | DNS/hora/red correctos y credenciales fuera del repositorio |
| 3.e | Configurar directorio básico | Pruebas de descubrimiento y salud | Cliente localiza servicios y autentica con DNS de dominio |
| 3.f | Crear agrupaciones administrativas | Modelo OU y delegación limitada | OU para administración/GPO y grupos para autorización |
| 3.g | Analizar estructura del directorio | Inventario jerárquico y dependencias | Justifica árbol/bosque/OU y consecuencias de cambios |
| 3.h | Administrar dominios con herramientas | Registro de consultas y cambios controlados | Herramientas oficiales y privilegio mínimo según operación |

**Actividades vinculadas:** [0224-RA3-A1: Directorio, modelo administrativo y confianza aislada](10-retos-por-ra.md#ra3) — CE a, b, d, e, f, g, h; [0224-RA3-A2: Establecer confianza en extensión de dos dominios](10-retos-por-ra.md#ra3) — CE c

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra4"></a>
## RA4

> Gestiona los recursos compartidos del sistema, interpretando especificaciones y determinando niveles de seguridad.

La compartición combina permisos, derechos, interfaz gráfica, impresión y revisión entre participantes. Las pruebas deben representar operaciones del cliente y no sólo la vista administrativa. Una impresora virtual es válida para determinados pasos de cola, pero no prueba una salida física que no se ha producido.

**Estudio:** [02-guia-tecnica.md](02-guia-tecnica.md) · [06-linux-permisos-y-capacidad.md](06-linux-permisos-y-capacidad.md) · [10-retos-por-ra.md](10-retos-por-ra.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 4.a | Distinguir permiso y derecho | Caso de acceso a archivo frente a privilegio del sistema | Explica por qué iniciar sesión y leer un recurso son decisiones distintas |
| 4.b | Identificar recursos y condiciones de compartición | Inventario de carpetas/colas y usuarios | Cada recurso tiene propósito, alcance y responsable |
| 4.c | Asignar permisos a recursos | Matriz de grupos y ACL | Pruebas de lectura/escritura/denegación coinciden con requisito |
| 4.d | Compartir impresoras en red | Cola y prueba desde cliente autorizado | Controlador/IPP compatibles y salida comprobada; sin bajar seguridad de drivers |
| 4.e | Usar GUI para compartir recursos | Acta del asistente y configuración efectiva | No confunde casilla visible con permisos realmente aplicados |
| 4.f | Controlar acceso de clientes | Pruebas desde identidades permitidas y ajenas | No usa invitado universal, SMB1 o permisos amplios como solución |
| 4.g | Comprobar recursos en equipo | Revisión cruzada y pruebas entre participantes | Roles y contribuciones registrados; ensayo individual no acredita trabajo grupal |

**Actividades vinculadas:** [0224-RA4-A1: Recursos e impresión con seguridad efectiva](10-retos-por-ra.md#ra4) — CE a, b, c, e, f, g; [0224-RA4-A2: Impresora compartida y prueba de cliente](10-retos-por-ra.md#ra4) — CE d

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra5"></a>
## RA5

> Realiza tareas de monitorización y uso del sistema operativo en red, describiendo las herramientas utilizadas e identificando las principales incidencias.

La monitorización se relaciona con hipótesis y acciones de mantenimiento. Un log puede mostrar un evento cercano al fallo sin demostrar su causa; una métrica de capacidad no equivale a latencia. La automatización produce registros y estados de error explícitos, y se prueba sobre objetos de laboratorio.

**Estudio:** [04-diagnostico-y-evaluacion.md](04-diagnostico-y-evaluacion.md) · [06-linux-permisos-y-capacidad.md](06-linux-permisos-y-capacidad.md) · [07-operacion-automatizacion-y-recuperacion.md](07-operacion-automatizacion-y-recuperacion.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 5.a | Describir herramientas de monitorización | Catálogo de señales, herramientas y límites | Cada herramienta se vincula a una pregunta concreta |
| 5.b | Detectar problemas de rendimiento de almacenamiento | Serie temporal y prueba discriminante | Separa capacidad, latencia, IOPS y carga de red |
| 5.c | Observar actividad mediante trazas | Cronología correlacionada cliente/servidor | Fecha/zona y servicio identificados sin inferir causa sólo por proximidad |
| 5.d | Mantener software del servidor | Plan de actualización y comprobaciones | Canal soportado, copia, retorno y validación del servicio |
| 5.e | Automatizar tareas operativas | Tarea de laboratorio con registro y error previsto | No oculta fallos y comprueba destino/privilegios antes de actuar |
| 5.f | Interpretar configuración de red del SO | Informe de configuración efectiva y persistencia | Relaciona NIC, DNS, rutas, roles y gestores activos |

**Actividades vinculadas:** [0224-RA5-A1: Observabilidad, mantenimiento y automatización operativa](10-retos-por-ra.md#ra5) — CE a, b, c, d, e, f

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra6"></a>
## RA6

> Realiza tareas de integración de sistemas operativos libres y propietarios, describiendo las ventajas de compartir recursos e instalando software específico.

La integración heterogénea exige demostrar que clientes de distintos sistemas utilizan recursos con seguridad. Compartir un nombre de usuario no crea por sí solo una identidad común. Se añade impresión desde Linux y Windows y relevo colaborativo, dejando claro qué se ha ejecutado con equipo real y qué permanece simulado.

**Estudio:** [02-guia-tecnica.md](02-guia-tecnica.md) · [06-linux-permisos-y-capacidad.md](06-linux-permisos-y-capacidad.md) · [08-laboratorios-y-casos-resueltos.md](08-laboratorios-y-casos-resueltos.md) · [10-retos-por-ra.md](10-retos-por-ra.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 6.a | Justificar recursos entre sistemas diferentes | Caso de uso y requisitos de interoperabilidad | No presupone que compartir nombre implique identidad común |
| 6.b | Comprobar conectividad heterogénea | Matriz Linux/Windows con ruta y servicio | Prueba ambas direcciones pertinentes y no sólo ping |
| 6.c | Describir servicio de compartición | Diagrama SMB/IPP, identidades y datos | Distingue protocolo, proceso, puerto y autorización |
| 6.d | Instalar/configurar servicio de recursos | Acta del servidor y configuración validada | Sólo LAB, versiones soportadas y sin roles incompatibles |
| 6.e | Acceder a archivos entre SO distintos | Pruebas Linux→servidor y Windows→servidor | Lectura/escritura y metadatos interpretados correctamente |
| 6.f | Acceder a impresoras desde diferentes SO | Pruebas de cola y salida desde Linux y Windows | Identifica driver/protocolo y distingue cola virtual de impresión física |
| 6.g | Trabajar colaborativamente | Bitácora de roles, revisión y relevo | Otro participante puede repetir y revisar las pruebas |
| 6.h | Aplicar seguridad a recursos heterogéneos | Matriz de accesos efectivos por identidad | Caso positivo y negativo sin desactivar protecciones |
| 6.i | Verificar funcionamiento final | Acta desde clientes y plan de recuperación | Cubre operación útil, persistencia y límites pendientes |

**Actividades vinculadas:** [0224-RA6-A1: Integración heterogénea de archivos e impresión](10-retos-por-ra.md#ra6) — CE a, b, c, d, e, g, h, i; [0224-RA6-A2: Impresión desde Linux y Windows](10-retos-por-ra.md#ra6) — CE f

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

## Recuperación y evaluación formativa

Una entrega incompleta se revisa por criterio, no se borra su historial. Identifica qué observación falta y prepara una segunda prueba con entradas o condiciones diferentes. Si el problema era conceptual, explica la corrección antes de repetir; si era de entorno, documenta cómo se identificó la dependencia. Una práctica repetida sin comprender el fallo no aporta la misma evidencia que una recuperación razonada.

Para la revisión entre participantes utiliza la [matriz de pruebas](../../recursos/plantillas/matriz-de-pruebas.md). Verifica que cada letra tenga actividad y artefacto, y que el resultado real no se haya copiado de la solución. La matriz no prescribe ponderaciones oficiales ni reemplaza la programación del centro. Una actividad puede aportar evidencia a varios criterios, pero cada uno conserva su comprobación concreta.

## Fuentes y mantenimiento

- [RD 1691/2007, anexo I](https://www.boe.es/eli/es/rd/2007/12/14/1691): enunciados y letras normativas de este módulo.
- [RD 499/2024, artículo séptimo](https://www.boe.es/eli/es/rd/2024/05/21/499): modificación del anexo I y organización adaptada.
- [Marco de SMR Madrid](../../docs/curriculo-madrid.md): horas, módulos transversales, proyecto y optatividad.

Si cambia una norma, contrasta enunciados y letras antes de actualizar la actividad. Si sólo cambia una herramienta, conserva el criterio y modifica procedimiento, versión, prueba y limitaciones. El JSON conserva los identificadores para revisar la trazabilidad de forma reproducible.
