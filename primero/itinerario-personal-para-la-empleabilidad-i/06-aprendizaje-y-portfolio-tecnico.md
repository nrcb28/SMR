# Aprendizaje autónomo, evidencias y portfolio técnico

[Índice del módulo](README.md) · [Prevención aplicada](04-evaluacion-preventiva-completa.md) · [Candidatura de segundo](../../segundo/itinerario-personal-para-la-empleabilidad-ii/04-seleccion-comunicacion-y-equipos.md)

## 1. Definir una competencia con condiciones de ejecución

Una competencia técnica combina conocimiento, procedimiento y decisión. «Sé Linux» no especifica ninguna de esas partes. Una formulación evaluable sería: «en una VM Debian de laboratorio, asigno permisos a un recurso nuevo para dos grupos, demuestro lectura y escritura autorizadas, rechazo acceso ajeno y recupero la configuración previa». La condición evita extrapolar una práctica a toda administración de producción.

Define resultado, contexto, recursos permitidos y límites. Utilizar documentación oficial puede formar parte del trabajo; copiar una solución sin comprenderla no demuestra el mismo nivel. El objetivo no es actuar siempre de memoria, sino saber consultar, adaptar y validar. Una persona competente identifica también cuándo debe detenerse y pedir supervisión.

El portfolio documenta pruebas seleccionadas de ese desempeño. No es una carpeta de todo lo descargado ni una colección de capturas. Debe permitir comprender qué hiciste, qué parte era tuya, qué ayuda recibiste y qué comprobaron los resultados. Conserva errores relevantes: una hipótesis descartada con evidencia puede mostrar mejor razonamiento que una pantalla final sin contexto.

## 2. Diagnóstico inicial por tareas

Elige tres tareas pequeñas de ámbitos distintos y dales un estado inicial claro. Ejemplo: calcular dos subredes, explicar permisos de un directorio y redactar un ticket. Mantén el mismo nivel de dificultad en las revisiones posteriores; cambiar a un caso trivial sólo para mejorar la puntuación impide comparar.

| Dimensión | Pregunta de observación | Evidencia |
| --- | --- | --- |
| Comprensión | ¿Explica el concepto antes de ejecutar? | Predicción escrita de resultado |
| Procedimiento | ¿Selecciona acciones en un orden razonable? | Registro de pasos y fuentes |
| Integridad | ¿Protege estado y datos? | Copia/reversión y límites identificados |
| Verificación | ¿Comprueba desde el usuario o cliente? | Pruebas positivas y negativas |
| Transferencia | ¿Resuelve una variante? | Segundo caso con datos distintos |
| Comunicación | ¿Otra persona entiende la conclusión? | Revisión de memoria por un compañero |

Una escala propia puede ir de cero a tres: sin evidencia, con guía completa, con apoyo puntual y con ejecución/justificación autónoma dentro del contexto. No sumes mecánicamente la escala para anunciar «nivel profesional avanzado». Utilízala para decidir dónde estudiar y qué apoyo solicitar.

### Caso 1: rápido pero sin verificación

Una estudiante configura un recurso en doce minutos y no prueba acceso desde el cliente. Otro tarda veinte y comprueba identidades permitidas y denegadas. La rapidez aislada no demuestra mejor desempeño. Si la tarea exigía acceso por rol, la primera evidencia está incompleta. La mejora consiste en incorporar comprobaciones sin perder seguridad, no en premiar el cronómetro por encima del requisito.

## 3. Diseñar actividades que cambian el desempeño

Relaciona cada carencia con una actividad y una prueba. Si fallas por confundir grupo propietario y grupo efectivo, leer comandos durante otra hora quizá no sea suficiente. Construye dos usuarios y grupos sintéticos, predice el acceso y contrasta. Si el problema era interpretar una consigna, practica descomponer requisitos antes de tocar la VM.

Alterna explicación, práctica guiada, recuperación sin la guía y variante. Recuperar una idea después de un intervalo obliga a reconstruirla; una lectura seguida puede producir familiaridad sin capacidad de aplicación. Revisa el error y repite el razonamiento con datos nuevos. El aprendizaje no se mide por cuántas veces ejecutaste el mismo bloque copiado.

Mantén un registro de errores clasificado: concepto, lectura, sintaxis, entorno, autorización o validación. Un error de sintaxis se puede corregir en el manual; uno de alcance puede exigir detener una acción; uno conceptual necesita otro ejemplo. La clasificación conduce a un siguiente paso, no a una etiqueta personal como «soy malo en redes».

## 4. Itinerario de ocho semanas con hitos

Este plan didáctico no fija una carga oficial. Adáptalo a horarios, otras asignaturas y apoyos. Se proponen dos bloques semanales de trabajo concentrado y una revisión breve, sin asumir que todas las personas tienen los mismos recursos en casa. Si falta equipo, utiliza actividades de cálculo, lectura y simulación documental hasta disponer del laboratorio autorizado.

| Semana | Trabajo principal | Producto | Condición para avanzar |
| --- | --- | --- | --- |
| 1 | Diagnóstico de permisos, subredes y comunicación | Línea base y dos dificultades prioritarias | Puedes explicar qué falta y cómo lo medirás |
| 2 | Usuarios/grupos y lectura de permisos | Caso mínimo con predicción | Diferencias identidad, grupo y autorización |
| 3 | Pruebas negativas y recuperación | Memoria con reversión | Una denegación prevista se interpreta correctamente |
| 4 | IPv4 y selección de rutas | Dos diseños con comprobación | Justificas red, rango y siguiente salto |
| 5 | Diagnóstico de un fallo preparado | Árbol de hipótesis | Cada prueba separa causas posibles |
| 6 | Explicación a usuario y documentación | Ticket y resumen de una página | Otra persona comprende impacto y siguiente paso |
| 7 | Variante integrada | Caso nuevo con tiempo registrado | No dependes de los valores originales |
| 8 | Revisión final y plan siguiente | Comparación de evidencias | Identificas progreso y límites pendientes |

La planificación reserva recuperación tras una sesión perdida. Si dos semanas no se pueden completar, reduce alcance o reordena dependencias; no llenes retrospectivamente un diario con trabajo no realizado. Revisar un plan por evidencia es una competencia de organización.

## 5. Métricas que se pueden interpretar

Usa pocas medidas con definición estable. En una tarea de diez requisitos, siete cumplidos representan 70 % de cobertura del caso, no 70 % de toda la asignatura. Si la siguiente tarea tiene requisitos distintos, compara por dimensiones antes de anunciar una mejora porcentual.

El tiempo puede separarse en lectura, búsqueda, ejecución, comprobación y documentación. Reducir ejecución a costa de eliminar pruebas puede bajar minutos y empeorar el resultado. Una métrica compuesta puede ocultar ese intercambio; conserva los componentes. La autonomía también requiere precisar ayuda: documentación consultada, indicación puntual o intervención completa de otra persona.

### Caso 2: interpretar una mejora

En dos ejercicios comparables, el primer intento cumple seis de diez requisitos y tarda cincuenta minutos. El segundo cumple nueve y tarda cincuenta y cinco. La cobertura aumenta treinta puntos porcentuales; el tiempo total aumenta un 10 %. Puede ser una mejora de calidad si los tres requisitos adicionales son necesarios. La conclusión explica ambos cambios y no declara «peor rendimiento» sólo por el cronómetro.

## 6. Estructurar un portfolio revisable

Cada proyecto seleccionado incluye ficha, requisitos, entorno, procedimiento, decisiones, pruebas, limitaciones y fuentes. El README de la pieza explica en pocas líneas qué resuelve y cómo recorrer los archivos. Añade una muestra pequeña de datos sintéticos y evita obligar al revisor a instalar un servidor para comprender la evidencia básica.

| Pieza | Qué demuestra | Qué no permite afirmar |
| --- | --- | --- |
| VLSM resuelto y justificado | Razonamiento de direccionamiento | Experiencia en una red empresarial real |
| Recurso con matriz de permisos | Identidad, ACL y comprobación | Administración de cualquier servicio de directorio |
| Informe de avería preparado | Método y comunicación | Haber atendido a un cliente real |
| Hoja económica editable | Fórmulas y coherencia de supuestos | Asesoramiento contable o fiscal profesional |
| Registro de restauración de laboratorio | Procedimiento y medición | Capacidad de recuperar todos los sistemas de producción |

Separa tres estados: realizado, realizado con ayuda y observado. Una práctica conjunta identifica contribuciones y revisión. No cambies el contexto de un proyecto para que parezca empleo. La selección mejora cuando explica límites con precisión y propone el siguiente aprendizaje pertinente.

## 7. Privacidad, propiedad y conservación

Antes de publicar revisa texto, metadatos, imágenes y archivos de configuración. Un documento puede omitir nombres visibles y conservar autor, rutas, comentarios o historial. Una captura puede mostrar pestañas, notificaciones o identificadores fuera del área principal. La revisión se realiza sobre el archivo exportado, no sólo sobre la pantalla del editor.

No incluyas credenciales aunque sean de una VM que crees apagada. Tampoco reutilices secretos reales en ejemplos. Si una evidencia procede de formación en empresa, el tutor y los procedimientos determinan qué se puede conservar y mostrar. Recrear un caso con datos sintéticos puede ser una alternativa, identificada como recreación y sin afirmar que sea el registro original.

Un portfolio público es una selección estable; el cuaderno privado puede contener más detalle. Define copias, versiones y retirada de información. Si detectas que se publicó un secreto, eliminarlo del último archivo no garantiza retirarlo del historial o de copias: avisa y sigue el procedimiento pertinente de revocación y saneamiento.

## 8. Utilizar IA y otras ayudas sin falsear la evidencia

Una herramienta de IA puede proponer preguntas, explicar un error o revisar claridad. Trátala como una fuente de sugerencias que requiere contraste. Una respuesta plausible no demuestra que un comando exista, que una opción sea segura o que una norma siga vigente. Consulta el manual de la versión y verifica en el ámbito autorizado.

Registra ayuda significativa cuando influya en la autoría o en la evaluación. Por ejemplo: «usé una herramienta para proponer la estructura; comprobé las opciones en documentación oficial y ejecuté las pruebas descritas». No afirmes ejecución de pruebas que la herramienta sólo escribió. Las normas del centro determinan el uso permitido en una actividad concreta.

### Caso 3: solución generada que no se comprende

La herramienta entrega un script que cambia permisos recursivamente. Antes de ejecutarlo, identifica objetos, alcance, privilegios, supuestos, posibles enlaces y recuperación. Si no puedes explicarlo, la actividad siguiente es descomponerlo, no probarlo sobre datos reales. Un ejercicio correcto puede rechazar el script y utilizar un caso mínimo de consulta. La evidencia es el razonamiento y la prueba controlada.

### Caso 4: cita que no existe

Una explicación incluye un artículo legal y una dirección que no resuelve. Busca norma, identificador y texto oficial; no cambies la cita por un enlace cualquiera que parezca apoyar la frase. Si no se confirma, elimina o reformula la afirmación. En asuntos laborales distingue una hipótesis didáctica de una regla que afectaría a una persona.

## 9. Entrega y revisión entre compañeros

Selecciona dos piezas técnicas y una de comunicación. Acompáñalas de una matriz requisito-evidencia y de una reflexión de unas pocas páginas: dificultad inicial, actividad que la abordó, cambio observado, ayuda recibida y siguiente objetivo. El tamaño no sustituye a la trazabilidad; enlaza archivos exactos y evita duplicar la misma captura en varios documentos.

La persona revisora comprueba si puede encontrar la prueba, interpretar el resultado y reproducir al menos un razonamiento sin ayuda. Propone una mejora de contenido y otra de presentación. La respuesta del autor explica qué cambia y por qué; no acepta sugerencias que alteren un hecho o eliminen un límite necesario.

Rúbrica propia: definición de objetivos 20 %, calidad de evidencias 30 %, transferencia y análisis de errores 20 %, organización y fuentes 15 %, honestidad y privacidad 15 %. Estos criterios son de autoevaluación del material, sin sustituir la programación oficial.

## 10. Referencias y conexiones

- [SEPE: formación y trabajo](https://www.sepe.es/HomeSepe/formacion-trabajo.html): orientación para seguir investigando itinerarios.
- [Europass: herramientas europeas para competencias y cualificaciones](https://europa.eu/europass/es): presentación de experiencia y aprendizaje.
- [AEPD: ciudadanía](https://www.aepd.es/areas-de-actuacion): consulta de materiales sobre protección de información y derechos.
- [Guías de diagnóstico de SMR](../../docs/metodo-de-diagnostico.md) y [plantilla de memoria](../../recursos/plantillas/memoria-practica.md): estructura de evidencias del laboratorio.

El plan, las escalas y los casos de este capítulo son originales. No se presentan como una metodología académica oficial ni como certificación de nivel profesional.
