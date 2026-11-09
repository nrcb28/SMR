# Ampliación de contenidos · 9 de noviembre de 2026

[Índice general](../README.md) · [Todos los capítulos](../INDICE.md)

La edición ampliada conserva las guías publicadas y añade monografías, casos, prácticas y material de integración. La estructura curricular de primero y segundo de Madrid permanece como referencia organizativa; las nuevas actividades son una profundización didáctica propia, con fuentes técnicas y normativas indicadas en sus capítulos.

## Alcance de la ampliación

| Indicador | Primera edición | Edición ampliada |
| --- | ---: | ---: |
| Archivos del repositorio | 107 | 189 |
| Documentos Markdown | 91 | 156 |
| Palabras aproximadas en Markdown | 98.000 | 225.000 |

Se añaden 65 documentos y 82 archivos en total. El recuento aproximado incluye texto y ejemplos de los documentos; el validador permite reproducir el conteo de la versión consultada. Los contenidos nuevos se distribuyen entre módulos, talleres y cuaderno integrador según el mapa siguiente.

## Asignaturas técnicas de primero

| Asignatura | Profundización añadida |
| --- | --- |
| [Montaje y mantenimiento](../primero/montaje-y-mantenimiento-de-equipos/README.md) | Medición de rendimiento, diagnóstico por subsistemas, integridad y vida útil de almacenamiento, periféricos y mantenimiento preventivo |
| [Sistemas monopuesto](../primero/sistemas-operativos-monopuesto/README.md) | Arranque y recuperación, procesos/memoria, permisos y consistencia de archivos, automatización con taller resuelto |
| [Redes locales](../primero/redes-locales/README.md) | VLSM e IPv6 avanzados, conmutación y segmentación, ingeniería Wi-Fi y análisis de protocolos con laboratorios |
| [Aplicaciones ofimáticas](../primero/aplicaciones-ofimaticas/README.md) | Documentos largos y publicación, modelos de cálculo y calidad de datos, modelado/consultas/transacciones y taller integrado |

Las monografías desarrollan conceptos y decisiones antes del procedimiento. Incluyen ejemplos trabajados, condiciones de uso, interpretación de resultados, averías y comprobaciones. Los ejemplos de código y datos se enlazan desde el módulo que los utiliza.

## Asignaturas técnicas de segundo

| Asignatura | Profundización añadida |
| --- | --- |
| [Sistemas operativos en red](../segundo/sistemas-operativos-en-red/README.md) | Directorio e identidades, Kerberos y GPO, Linux y permisos, capacidad, operación y recuperación, laboratorios de administración |
| [Seguridad informática](../segundo/seguridad-informatica/README.md) | Riesgo y BIA, controles, hardening con cambios recuperables, criptografía, continuidad, incidentes, privacidad y casos resueltos |
| [Servicios en red](../segundo/servicios-en-red/README.md) | Réplica DNS y cambios de zona, DHCP y dual stack, SSH/PKI/publicación web, correo, observabilidad y continuidad |
| [Aplicaciones web](../segundo/aplicaciones-web/README.md) | Frontend progresivo y accesibilidad, HTTP/cachés/sesiones, mantenimiento y migración de CMS, prácticas avanzadas |

La ampliación utiliza escenarios separados cuando necesita nuevos servidores, VLAN o roles incompatibles con el laboratorio base. Un servidor secundario DNS adicional no ocupa la dirección reservada al controlador de dominio. Los capítulos indican sus precondiciones y no atribuyen ejecución real a sus ejemplos sintéticos.

## Empleabilidad, transversales y optativas

[IPE I](../primero/itinerario-personal-para-la-empleabilidad-i/README.md) incorpora evaluación preventiva completa, relación laboral/nómina y aprendizaje profesional. [IPE II](../segundo/itinerario-personal-para-la-empleabilidad-ii/README.md) amplía selección, comunicación, trabajo en equipo, viabilidad y tesorería, con nuevos casos y CSV sintéticos. Los ejemplos económicos explicitan supuestos y distinguen beneficio, caja e impuestos.

[Inglés](../segundo/ingles-profesional/README.md) añade mensajes técnicos y simulaciones de atención/defensa; [Digitalización](../segundo/digitalizacion-aplicada-a-los-sectores-productivos/README.md), modelos de datos, integraciones, gobierno y casos; [Sostenibilidad](../segundo/sostenibilidad-aplicada-al-sistema-productivo/README.md), medición y decisiones de ciclo de vida; el [Proyecto](../segundo/proyecto-intermodular/README.md), un cuaderno de requisitos y una memoria modelo con defensa.

Las propuestas complementarias de [optativa de primero](../primero/modulo-optativo/README.md) y [optativa de segundo](../segundo/modulo-optativo/README.md) se desarrollan como talleres. No identifican una oferta oficial común a todos los centros. La [formación en empresa](formacion-en-empresa.md) añade casos de seguimiento y evidencia, y el [apartado histórico](../plan-anterior/README.md) profundiza en expedientes de FOL, EIE y FCT sin incorporarlos como módulos autónomos al plan actual.

## Cuaderno integrador

El [cuaderno](../cuaderno-integrador/README.md) complementa el estudio por asignaturas con problemas que atraviesan varias áreas:

1. [Magnitudes y cálculos](../cuaderno-integrador/01-magnitudes-y-calculos-resueltos.md): dieciséis problemas trabajados de unidades, rendimiento, capacidad, copias, disponibilidad, energía y costes.
2. [Incidencias encadenadas](../cuaderno-integrador/02-incidencias-encadenadas.md): diez escenarios que separan síntoma, hipótesis, pruebas, causa y recuperación.
3. [Simulacro de primero](../cuaderno-integrador/03-simulacro-primero.md): puesto, permisos, direccionamiento, presupuesto, prevención y documentación.
4. [Simulacro de segundo](../cuaderno-integrador/04-simulacro-segundo.md): nombres, identidad, acceso, TLS, archivos, continuidad y comunicación en inglés.
5. [Entrega y operación](../cuaderno-integrador/05-entrega-y-operacion.md): requisitos, decisiones, cambios, runbooks, aceptación y transferencia.

Los tiempos y pesos de los simulacros son herramientas de entrenamiento. Las pruebas y calificaciones oficiales se rigen por la programación del centro. Las soluciones explican razonamientos y alternativas; no convierten una salida esperada en una evidencia que el estudiante haya obtenido.

## Navegación, datos y herramientas

El nuevo [índice completo](../INDICE.md) enlaza todos los documentos por carpeta y se puede regenerar sin servicios externos. Se mantienen los índices de asignatura como guías pedagógicas. La herramienta de [análisis de mediciones](../scripts/analizar_mediciones.py) permite comprobar datos sintéticos y estudiar media, mediana, percentil y caudal agregado.

Se añaden plantillas para [decisiones técnicas](../recursos/plantillas/decision-tecnica.md), [cambios](../recursos/plantillas/plan-de-cambio.md) y [procedimientos operativos](../recursos/plantillas/procedimiento-operacion.md). Las comprobaciones de la ampliación y sus límites se registran en [revisión de entregas](validacion.md).
