# Alineación con resultados de aprendizaje · 0222

[Índice de la asignatura](README.md) · [Retos por RA](10-retos-por-ra.md) · [Datos de trazabilidad](alineacion-ra.json)

## Referente, interpretación y alcance

Este mapa identifica los **5 RA y 41 criterios de evaluación** del módulo Sistemas operativos monopuesto en el anexo I del [Real Decreto 1691/2007](https://www.boe.es/eli/es/rd/2007/12/14/1691). Se ha contrastado el [RD 499/2024, artículo séptimo](https://www.boe.es/eli/es/rd/2024/05/21/499), que adapta la organización del título. Consulta: 09/11/2026. El reparto horario madrileño se explica en [currículo](../../docs/curriculo-madrid.md); no se utilizan aquí las antiguas horas de mínimos como horas de Madrid.

Los enunciados numerados de RA se reproducen del texto legal, normalizando espacios. Las descripciones de criterios de las tablas son **paráfrasis didácticas**, conservando sus letras; la norma enlazada contiene su redacción completa. Las actividades, evidencias y comprobaciones son propuestas originales. No son una escala oficial ni acreditan que una persona haya adquirido el RA por leer o completar un documento.

Usa cuatro estados en tu seguimiento: preparado, ejecutado, verificado y pendiente. «Preparado» significa que existe el plan; «ejecutado», que hubo una actuación real; «verificado», que la evidencia satisface la comprobación; «pendiente», que falta medio, supervisión o prueba. Conserva resultados reales e identifica por separado los ejemplos sintéticos. Las tareas físicas, colaborativas o de un producto no disponible no se dan por adquiridas mediante una sustitución declarativa.

## Cómo construir el dossier

Abre una ficha por RA, añade los documentos de estudio y prepara los objetos de laboratorio. Antes de ejecutar escribe qué criterio pretende demostrar cada paso y qué resultado lo contradice. Después conserva artefacto, contexto, identidad, versión y conclusión. Una captura aislada sin procedimiento puede mostrar un estado, pero no la secuencia que lo produjo ni su recuperación.

La actividad A1 integra los criterios del RA salvo que se indique A2. Las actividades A2 separan actuaciones que requieren otro entorno, material o supervisión. Esta separación permite registrar la parte real pendiente sin ocultarla detrás de un informe. Las guías de estudio enlazadas se complementan con el nuevo reto; un enlace no demuestra por sí solo cobertura práctica.

<a id="ra1"></a>
## RA1

> Reconoce las características de los sistemas de archivo, describiendo sus tipos y aplicaciones.

El primer RA une arquitectura, representación de información, procesos y archivos. Por eso no basta con saber copiar carpetas. El reto relaciona un carácter con sus bytes, un proceso con su estado y un archivo con permisos y estructura. La elección de un sistema de archivos requiere entender qué protege un journal y qué se recupera mediante copia.

**Estudio:** [01-fundamentos.md](01-fundamentos.md) · [07-archivos-permisos-y-consistencia.md](07-archivos-permisos-y-consistencia.md) · [10-retos-por-ra.md](10-retos-por-ra.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 1.a | Describir elementos funcionales del sistema | Mapa hardware–SO–aplicación–datos | Relaciona cada elemento con una operación del caso |
| 1.b | Codificar y relacionar representaciones | Cuaderno binario/hexadecimal/Unicode y bytes reales | Conversión comprobada; diferencia carácter, punto de código y byte |
| 1.c | Identificar procesos y estados | Listado temporal con PID y estado | Distingue proceso, hilo y estado sin confundir reposo con fallo |
| 1.d | Describir organización del sistema de archivos | Árbol y esquema de metadatos | Distingue ruta, entrada, contenido, partición y volumen |
| 1.e | Diferenciar atributos de archivo y directorio | Tabla de propiedades Linux/Windows | Explica significado y límites de cada atributo |
| 1.f | Reconocer permisos en archivos y directorios | Pruebas con identidades y ACL | Distingue lectura/listado/recorrido/escritura y acceso efectivo |
| 1.g | Valorar sistemas transaccionales para elegir FS | Decisión ext4/NTFS y análisis de consistencia | No confunde journal con copia, versionado o transacción de base de datos |

**Actividades vinculadas:** [0222-RA1-A1: Representación, procesos y elección del sistema de archivos](10-retos-por-ra.md#ra1) — CE a, b, c, d, e, f, g

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra2"></a>
## RA2

> Instala sistemas operativos, relacionando sus características con el hardware del equipo y el software de aplicación.

La instalación se justifica antes de arrancar el instalador: hardware, aplicaciones, licencias, particiones y retorno. El medio no se considera seguro sólo por tener un nombre conocido. La evidencia debe permitir reconstruir decisiones y detectar una instalación que arranca pero usa firmware, edición o cuenta inadecuados.

**Estudio:** [02-guia-tecnica.md](02-guia-tecnica.md) · [03-practicas.md](03-practicas.md) · [05-arranque-y-recuperacion.md](05-arranque-y-recuperacion.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 2.a | Analizar funciones del sistema operativo | Mapa de necesidades y funciones | Relaciona gestión de recursos, protección e interfaz con el uso |
| 2.b | Describir arquitectura del SO | Diagrama kernel/servicios/controladores/aplicaciones | Explica privilegios y un trayecto de E/S |
| 2.c | Comprobar adecuación del hardware | Checklist de requisitos oficiales | Verifica arquitectura, memoria, espacio, firmware y requisitos de edición |
| 2.d | Elegir SO justificado | Matriz de compatibilidad y soporte | La elección satisface aplicaciones y condiciones de licencia |
| 2.e | Preparar plan de instalación | Documento de particiones/cuentas/actualización/retorno | Identifica disco destino y recuperación antes de ejecutar |
| 2.f | Configurar parámetros iniciales | Acta de zona, idioma, cuenta y red | Sin datos reales y con valores coherentes con LAB |
| 2.g | Configurar gestor de arranque | Registro de modo UEFI y entradas | Prueba arranque y rescate sin reparar discos ajenos |
| 2.h | Registrar incidencias de instalación | Bitácora con error, hipótesis y solución | Incluye resultado real y límites de lo no ejecutado |
| 2.i | Respetar condiciones del software | Inventario de licencias y procedencia | No publica claves ni elude activación/requisitos |
| 2.j | Actualizar el SO | Registro de versión antes/después y reinicio si procede | Canal oficial y comprobación de servicios tras actualizar |

**Actividades vinculadas:** [0222-RA2-A1: Instalación comparada con plan y licencia](10-retos-por-ra.md#ra2) — CE a, b, c, d, e, f, g, h, i, j

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra3"></a>
## RA3

> Realiza tareas básicas de configuración de sistemas operativos, interpretando requerimientos y describiendo los procedimientos seguidos.

La configuración básica se organiza alrededor de un requerimiento del puesto y su recuperación. Se comparan GUI y CLI, se ajusta un perfil de pruebas y se ensaya una utilidad y una tarea programada. Un parámetro temporal no equivale a una configuración persistente; una operación que afecta a toda la máquina necesita más privilegio y alcance que una preferencia personal.

**Estudio:** [02-guia-tecnica.md](02-guia-tecnica.md) · [05-arranque-y-recuperacion.md](05-arranque-y-recuperacion.md) · [08-automatizacion-y-taller-resuelto.md](08-automatizacion-y-taller-resuelto.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 3.a | Distinguir interfaces y sus propiedades | Comparativa GUI/CLI y accesibilidad | Selecciona interfaz según tarea y contexto |
| 3.b | Aplicar preferencias personales | Acta de ajustes y reversión | Cambia sólo el perfil de prueba y justifica accesibilidad/usabilidad |
| 3.c | Gestionar sistemas de archivos propios del SO | Registro de operaciones sobre volumen sintético | Identifica objeto y evita confundir disco/partición/carpeta |
| 3.d | Aplicar recuperación del sistema | Ensayo en copia o VM desechable | Estado recuperado y datos preservados según objetivo |
| 3.e | Configurar actualización | Política de canal, comprobación y horario | Distingue buscar actualizaciones de instalarlas y documenta reinicio |
| 3.f | Instalar y desinstalar utilidades | Registro de una utilidad de prueba | Origen legítimo y retirada sin eliminar dependencias ajenas |
| 3.g | Usar asistentes de red y dispositivos | Acta de NIC/dispositivo y prueba funcional | Verifica objeto real y no añade gateway ficticio a LAB |
| 3.h | Automatizar una tarea del sistema | Tarea programada sobre datos sintéticos | Registra ejecución, fallo y retirada sin ocultar errores |

**Actividades vinculadas:** [0222-RA3-A1: Puesto configurable y recuperable](10-retos-por-ra.md#ra3) — CE a, b, c, d, e, f, g, h

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra4"></a>
## RA4

> Realiza operaciones básicas de administración de sistemas operativos, interpretando requerimientos y optimizando el sistema para su uso.

La administración debe actuar sobre identidades, procesos, servicios, memoria y almacenamiento sin perder el razonamiento. Se trabaja con procesos propios y servicios de demostración para que las acciones sean observables y reversibles. No se emplea la cuenta administrativa para ocultar fallos de autorización ni se vacían cachés por rutina para mejorar una captura.

**Estudio:** [02-guia-tecnica.md](02-guia-tecnica.md) · [06-procesos-memoria-y-observabilidad.md](06-procesos-memoria-y-observabilidad.md) · [07-archivos-permisos-y-consistencia.md](07-archivos-permisos-y-consistencia.md) · [08-automatizacion-y-taller-resuelto.md](08-automatizacion-y-taller-resuelto.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 4.a | Configurar perfiles, usuarios y grupos | Matriz de identidades locales y operaciones | Cuenta ordinaria, privilegio mínimo y pruebas de acceso |
| 4.b | Usar herramientas gráficas para explorar archivos del sistema | Capturas explicadas del gestor autorizado | Identifica organización sin alterar archivos protegidos |
| 4.c | Actuar sobre procesos propios | Registro de proceso de laboratorio y señal | Sólo PID propio identificado y efecto verificado |
| 4.d | Actuar sobre servicios según necesidad | Unidad o servicio exclusivo y estado antes/después | Inicio/parada/reinicio justificados con retorno |
| 4.e | Optimizar memoria disponible | Comparativa de carga y métricas | Actúa sobre causa y no confunde caché con memoria desperdiciada |
| 4.f | Analizar trazas del sistema | Línea temporal con eventos pertinentes | Correlaciona hora, contexto y síntoma sin exponer datos personales |
| 4.g | Optimizar almacenamiento | Plan y ensayo controlado de espacio/actividad | Usa medidas apropiadas al dispositivo y no desfragmenta SSD por rutina |
| 4.h | Configurar recursos compartibles | Prueba de recurso local o compartido acotado | Identidad y permisos definidos; no acceso universal |
| 4.i | Interpretar configuración del SO | Informe de estado efectivo y persistente | Distingue parámetro guardado de estado realmente cargado |

**Actividades vinculadas:** [0222-RA4-A1: Administración local mediante hipótesis y métricas](10-retos-por-ra.md#ra4) — CE a, b, c, d, e, f, g, h, i

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

<a id="ra5"></a>
## RA5

> Crea máquinas virtuales identificando su campo de aplicación e instalando software específico.

El RA requiere experiencia con software libre y propietario y con invitados de ambos tipos. La guía diferencia estudiar un producto de instalarlo y deja pendientes los desempeños que el equipo o la licencia no permiten. Las pruebas de rendimiento deben conservar condiciones comparables; el objetivo no es proclamar ganador a un hipervisor.

**Estudio:** [01-fundamentos.md](01-fundamentos.md) · [03-practicas.md](03-practicas.md) · [06-procesos-memoria-y-observabilidad.md](06-procesos-memoria-y-observabilidad.md) · [10-retos-por-ra.md](10-retos-por-ra.md)

| CE | Paráfrasis didáctica | Evidencia propuesta | Comprobación de aceptación |
| --- | --- | --- | --- |
| 5.a | Distinguir máquina física y VM | Diagrama de capas y dispositivos expuestos | Explica qué evidencia física no puede aportar la VM |
| 5.b | Comparar ventajas y límites de virtualización | Matriz de aislamiento, recursos y recuperación | No presenta snapshot como copia independiente ni aislamiento absoluto |
| 5.c | Instalar software libre y propietario de virtualización | Actas de instalación en anfitriones compatibles | Licencias y versiones admitidas; estudiar uno no demuestra instalar ambos |
| 5.d | Crear invitados libres y propietarios | Inventario de dos invitados legítimos | Medios oficiales y edición/arquitectura compatibles |
| 5.e | Configurar VMs | Ficha de CPU/RAM/disco/NIC/firmware | Dimensiona sin sobreasignación injustificada y aísla LAB |
| 5.f | Relacionar invitado y anfitrión | Tabla de integración y límites | Distingue carpetas compartidas, dispositivos y rutas de red |
| 5.g | Realizar pruebas de rendimiento | Serie comparable con método y carga | Controla caché/concurrencia y evita atribuir al hardware físico lo visto en VM |

**Actividades vinculadas:** [0222-RA5-A1: Virtualización libre y propietaria contrastada](10-retos-por-ra.md#ra5) — CE a, b, c, d, e, f, g

**Revisión del aprendizaje:** explica una decisión, muestra una operación y presenta una prueba que podría fallar. Si la evidencia sólo cubre parte del criterio, registra el alcance y el siguiente paso; no marques automáticamente todo el RA como superado.

## Recuperación y evaluación formativa

Una entrega incompleta se revisa por criterio, no se borra su historial. Identifica qué observación falta y prepara una segunda prueba con entradas o condiciones diferentes. Si el problema era conceptual, explica la corrección antes de repetir; si era de entorno, documenta cómo se identificó la dependencia. Una práctica repetida sin comprender el fallo no aporta la misma evidencia que una recuperación razonada.

Para la revisión entre participantes utiliza la [matriz de pruebas](../../recursos/plantillas/matriz-de-pruebas.md). Verifica que cada letra tenga actividad y artefacto, y que el resultado real no se haya copiado de la solución. La matriz no prescribe ponderaciones oficiales ni reemplaza la programación del centro. Una actividad puede aportar evidencia a varios criterios, pero cada uno conserva su comprobación concreta.

## Fuentes y mantenimiento

- [RD 1691/2007, anexo I](https://www.boe.es/eli/es/rd/2007/12/14/1691): enunciados y letras normativas de este módulo.
- [RD 499/2024, artículo séptimo](https://www.boe.es/eli/es/rd/2024/05/21/499): modificación del anexo I y organización adaptada.
- [Marco de SMR Madrid](../../docs/curriculo-madrid.md): horas, módulos transversales, proyecto y optatividad.

Si cambia una norma, contrasta enunciados y letras antes de actualizar la actividad. Si sólo cambia una herramienta, conserva el criterio y modifica procedimiento, versión, prueba y limitaciones. El JSON conserva los identificadores para revisar la trazabilidad de forma reproducible.
