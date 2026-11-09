# Estudiar, practicar y recoger evidencias por resultados de aprendizaje

[Índice general](../README.md) · [Mapa de RA y CE](mapa-ra.md) · [Optativas aplicables a SMR](../optativas/README.md)

## 1. Qué organiza esta ampliación

Un resultado de aprendizaje, o RA, describe una capacidad que el estudiante debe poder demostrar al terminar una parte de la formación. Sus criterios de evaluación, o CE, concretan las actuaciones y comprobaciones con las que se valora esa capacidad. Los contenidos explican conceptos y procedimientos necesarios para realizar esas actuaciones.

Esta ampliación organiza el estudio mediante la secuencia **RA → criterio → actividad → evidencia → comprobación**. Cada módulo dispone de una guía de alineación y de retos desarrollados. El mapa global permite localizar las rutas; la guía de cada asignatura explica las decisiones técnicas y qué parte requiere un equipo físico, una aplicación instalada, una interacción oral o una ejecución de laboratorio.

Una lista de temas ayuda a preparar una práctica, pero un RA exige demostrar una actuación. Para estudiar transferencia de ficheros, por ejemplo, conviene explicar el protocolo y configurar un servicio; para demostrar un criterio de acceso activo y pasivo hay que comprobar ambos modos en el escenario previsto y conservar evidencias. La documentación y el equipo utilizado deben corresponder a esa finalidad.

Las actividades, soluciones y rúbricas de este repositorio son propuestas didácticas. Los enunciados normativos y sus criterios se identifican con su fuente. La programación del centro determina instrumentos, ponderaciones, condiciones de evaluación y recuperación. No se atribuyen porcentajes oficiales a una tabla elaborada para estudiar.

## 2. Fuentes y numeración

Los ocho módulos técnicos se contrastan con el anexo I del [Real Decreto 1691/2007](https://www.boe.es/eli/es/rd/2007/12/14/1691), teniendo en cuenta la adaptación del título por el [Real Decreto 499/2024](https://www.boe.es/eli/es/rd/2024/05/21/499). Los módulos transversales utilizan el desarrollo autonómico de la [Orden 3537/2025 de Madrid](https://www.bocm.es/boletin/CM_Orden_BOCM/2025/08/27/BOCM-20250827-6.PDF). Proyecto se referencia al anexo II del RD 499/2024.

La oferta optativa se delimita mediante el catálogo de la [Orden 3536/2025](https://www.bocm.es/boletin/CM_Orden_BOCM/2025/08/27/BOCM-20250827-5.PDF) y su [modificación de 2026](https://www.bocm.es/boletin/CM_Orden_BOCM/2026/09/25/BOCM-20260925-20.PDF). El catálogo explica qué códigos pueden aplicarse a SMR, sus variantes y las condiciones de curso. La oferta concreta requiere la información del centro.

La numeración identifica al módulo y al resultado: `0227-RA3` es el RA3 de Servicios en red; `1709-RA1` es el RA1 de IPE I según la numeración madrileña empleada en este repositorio. Las letras de sus criterios se conservan. Una guía antigua o de otra administración puede organizar de forma distinta contenidos similares, por lo que se comprueba la fuente antes de trasladar un identificador.

IPE I presenta un caso especialmente relevante: en el desarrollo madrileño se comienza por prevención de riesgos, después relación laboral y luego sector profesional. No se mezclan esos números con los de una lista estatal diferente. El nombre del tema permite orientarse, pero la trazabilidad formal necesita código, RA, letra y versión normativa.

## 3. Cómo empezar desde un RA

Primero identifica tu módulo y abre su guía de alineación. Lee el enunciado completo y revisa todos sus criterios. Pregunta qué acciones concretas aparecen: seleccionar, instalar, configurar, medir, comparar, comprobar, comunicar o documentar. Cada verbo requiere un tipo de evidencia que debe prepararse antes de iniciar el ejercicio.

Después revisa los materiales enlazados. Algunos RA necesitan varios capítulos: instalar un sistema requiere compatibilidad, almacenamiento, arranque, licencia y actualización. Un capítulo avanzado sobre rendimiento no sustituye una operación de instalación si el criterio la exige. La ruta enlaza los conceptos y la práctica que los hace observables.

Abre el reto asociado y registra su estado inicial. Comprueba qué equipo y software necesitas, qué permisos tienes y cómo recuperar el entorno. Si te falta un recurso, identifica los criterios que no podrás observar todavía. Puedes completar la preparación conceptual y conservar esa limitación sin presentar una ejecución inexistente.

Finalmente prepara una ficha de prueba por criterio o conjunto coherente de criterios. Utiliza la [matriz de aceptación](../recursos/plantillas/matriz-de-pruebas.md) y la [memoria de práctica](../recursos/plantillas/memoria-practica.md). Separa resultado esperado, resultado obtenido e interpretación. La conclusión debe corresponder a lo que realmente has podido comprobar.

## 4. Ejemplo trabajado: transferencia de ficheros

El RA3 de Servicios en red se refiere a instalar servicios de transferencia de ficheros. Su criterio f) requiere comprobar el acceso tanto en modo activo como pasivo; también aparecen usuarios/grupos, acceso anónimo, límites y clientes de línea de comandos y gráficos. La guía del módulo trata esos puntos con un escenario aislado y datos sintéticos.

Una actividad puede comenzar describiendo control y datos, identificando puertos y preparando el servicio del laboratorio. Después se configuran cuentas, modos de acceso y límites. Las pruebas deben distinguir una conexión correcta de control de una transferencia real: obtener un saludo del servidor no demuestra que el canal de datos funcione.

Para el criterio de modos activo/pasivo se conserva qué cliente y modo se han utilizado, el archivo sintético transferido, el resultado y una observación que permita interpretar la diferencia de conexiones. Si sólo se ha probado un modo, el otro permanece pendiente. Una captura se acompaña de una explicación de origen, destino y función, sin publicar credenciales.

Para el acceso anónimo se prepara únicamente el escenario didáctico previsto, con permisos y datos de prueba. Se comprueba el alcance permitido y una operación denegada. Para los límites se define el valor configurado y la prueba que lo verifica. El objetivo es reconocer y controlar el comportamiento de cada modalidad.

SFTP tiene otras propiedades y mecanismos: su uso en administración segura se estudia también en el repositorio. Una transferencia SFTP correcta aporta evidencia de ese protocolo, mientras los criterios que mencionan activo/pasivo o anonimato necesitan el escenario correspondiente. La comparación entre tecnologías debe conservar qué comportamiento se está evaluando.

La evidencia completa relaciona configuración, operación desde cliente e interpretación. Un dossier puede reunir varios criterios, pero indica qué archivo, sección o prueba responde a cada letra. Esta relación evita dar por demostrada toda una competencia porque existe una única captura final.

## 5. Ejemplo trabajado: montaje y medición física

En Montaje, algunas capacidades requieren manipular componentes y medir magnitudes en condiciones apropiadas. Una VM es útil para instalación o diagnóstico del sistema invitado; no permite demostrar por sí sola la manipulación de conectores, la fijación física, una medida eléctrica real o la ejecución de un procedimiento de trabajo seguro.

Prepara el material y las instrucciones del fabricante antes de actuar. La intervención requiere la supervisión, formación, medios y autorización del entorno educativo. No se abren fuentes de alimentación ni se realizan mediciones peligrosas siguiendo únicamente un texto del repositorio. El reto indica las condiciones de parada y qué parte se reserva a equipamiento y personal adecuados.

Una ficha de evidencia física identifica componente, operación, instrumento o herramienta, procedimiento seguido y comprobación. Se puede acompañar de fotografía saneada, lista de control u observación de tutoría. La fotografía de un multímetro no demuestra una medición si no se registra qué se midió, cómo y con qué interpretación.

Si se trabaja con una tabla sintética de tensiones o fallos, se puede evaluar el razonamiento sobre esos datos. Debe indicarse que se interpreta un supuesto y que la medición física sigue pendiente. Esa distinción permite avanzar en el aprendizaje sin falsear la naturaleza de la prueba.

## 6. Ejemplo trabajado: comprensión y producción oral

Los RA de Inglés incluyen actuaciones orales y escritas. Un guion redactado sirve para preparar vocabulario, estructura e intención comunicativa; escuchar o producir un mensaje exige después una situación oral observable. Las guías incluyen instrucciones para trabajar con una pareja, grabación autorizada o lectura por otra persona según los recursos disponibles.

Para comprensión, una persona emite el mensaje sin mostrar inmediatamente el texto completo. El estudiante identifica contexto, finalidad, información relevante y respuesta necesaria. Después se contrasta con el guion y se explica qué pistas se han utilizado. Si el estudiante leyó previamente todas las respuestas, debe registrarse esa condición porque cambia lo que la actividad permite observar.

Para producción e interacción, se realiza una conversación o exposición con un objetivo y una incidencia que exige responder. Se observa claridad, adecuación, vocabulario, organización y capacidad de pedir aclaraciones. Memorizar un discurso puede ser una fase de entrenamiento; una interacción que necesita ajustar el mensaje añade otra evidencia.

Las pautas socioculturales se trabajan con situaciones y fuentes verificables, evitando atribuir conductas uniformes a todas las personas de un país. Una respuesta profesional identifica registro, contexto y preferencias del interlocutor. La evidencia puede ser una revisión razonada de dos mensajes y una interacción que muestre la adaptación.

## 7. Diseñar un reto que cubra varios criterios

Una actividad integradora comienza con una necesidad y termina con un producto verificable. Por ejemplo, preparar un recurso de archivos implica identidad, permisos, servicio, prueba desde cliente, recuperación y explicación. Es posible relacionar varias letras o módulos si cada relación describe una actuación real de la actividad.

Para diseñarla, enumera los criterios objetivo y las pruebas que los hacen observables. Después ordena dependencias: sistema y red, identidad, servicio, configuración, cliente y recuperación. Reserva tiempo para recopilar evidencia y analizar fallos. Ejecutar muchos pasos sin comprobarlos puede producir un resultado difícil de interpretar.

Define al menos un caso positivo y, cuando tenga sentido, uno negativo. En permisos, la cuenta autorizada opera y la cuenta ajena recibe denegación. En validación de datos, la entrada válida se acepta y la incorrecta se explica. En una recuperación, los datos vuelven y se comprueba que los permisos siguen cumpliendo el diseño.

El retorno al estado anterior se prepara antes del cambio. Para algunos ejercicios basta una copia de configuración y un entorno limpio; para otros se necesita una copia consistente de datos o un procedimiento específico de la aplicación. Una instantánea no resuelve del mismo modo todos los roles y sistemas.

El dossier final contiene requisitos, procedimiento, artefactos, pruebas, interpretación y pendientes. La tabla RA/CE señala dónde se encuentra cada evidencia. El mismo documento puede apoyar varios criterios si sus secciones muestran actuaciones diferenciadas y revisables.

## 8. Qué debe contener una evidencia

| Elemento | Pregunta que responde | Ejemplo de laboratorio |
| --- | --- | --- |
| Identificación | ¿Qué módulo, RA y criterio se observa? | `0227-RA3.f` |
| Contexto | ¿Dónde y con qué versión se hizo? | Cliente, servidor, software y topología |
| Estado inicial | ¿Qué condiciones existían? | Configuración previa, usuarios y archivos sintéticos |
| Acción | ¿Qué se ejecutó y con qué identidad? | Transferencia o prueba de acceso definida |
| Resultado | ¿Qué ocurrió realmente? | Archivo, registro o comportamiento obtenido |
| Interpretación | ¿Qué demuestra y qué queda abierto? | Modo confirmado y dependencia identificada |
| Revisión | ¿Quién y cómo lo comprobó? | Autoevaluación o revisión docente según el ejercicio |

Conserva los archivos editables cuando permitan comprobar fórmulas, estructura o configuración. Una captura puede complementar un resultado, pero no siempre contiene los datos necesarios para reproducirlo. Evita publicar claves, información de clientes, datos personales o contenido que no estés autorizado a compartir.

Una evidencia necesita alcance. Un archivo pequeño recuperado con éxito demuestra esa prueba; no certifica automáticamente la recuperación de toda una empresa. Una consulta DNS dirigida demuestra respuesta de un servidor, y una resolución normal permite estudiar además qué mecanismo usa el cliente.

## 9. Registro de seguimiento

La [plantilla de seguimiento de CE](../recursos/ra/plantilla-seguimiento-ce.csv) contiene una fila por criterio, con módulo, RA, clave, actividad, guía, evidencia esperada y comprobación. Las columnas de evidencia obtenida, fecha y observaciones empiezan vacías; el estado inicial es `sin_realizar`.

Copia la plantilla a tu espacio de trabajo antes de completarla. La herramienta de generación actualiza la plantilla base del repositorio. Tu registro personal debe conservarse como un archivo separado, con la privacidad que corresponda al entorno y a las indicaciones del centro.

Se propone un vocabulario de seguimiento: `sin_realizar`, `en_preparacion`, `evidencia_recogida`, `pendiente_revision` y `revisada`. Son estados organizativos. La revisión puede requerir correcciones, ampliación de evidencia o una nueva ejecución; no equivalen por sí solos a una calificación académica.

No marques un criterio como observado sólo porque has leído su capítulo. Registra qué ejercicio hiciste y qué evidencia permite revisar esa actuación. Si un resultado esperado se copia en la columna de resultado obtenido, se pierde la distinción entre diseño y observación.

## 10. Autoevaluación con una escala propia

Puedes usar una escala descriptiva para decidir qué necesitas practicar. La siguiente es una herramienta didáctica del repositorio, sin pesos ni umbrales oficiales:

| Situación | Descripción observable | Siguiente paso |
| --- | --- | --- |
| Preparación pendiente | Falta concepto, material o condición de trabajo | Estudiar el recurso y preparar el entorno |
| Ejecución guiada | Completa pasos con ayuda, pero no interpreta todo el resultado | Repetir con datos distintos y explicar decisiones |
| Ejecución comprobada | Realiza la tarea y presenta evidencias coherentes | Añadir caso negativo y recuperación si corresponde |
| Transferencia razonada | Adapta el procedimiento y justifica límites y alternativas | Resolver un caso nuevo y documentar su validación |

Esta escala ayuda a orientar estudio y retroalimentación. La valoración oficial se realiza con los instrumentos y reglas publicados por el centro. No se deduce una nota global de contar enlaces, páginas, actividades declaradas o casillas completas.

## 11. Resolver carencias por criterio

Si no puedes demostrar una actuación, identifica su causa: concepto no comprendido, entorno no preparado, recurso no disponible, procedimiento incompleto, interpretación equivocada o evidencia insuficiente. Cada causa exige una respuesta diferente. Leer un capítulo adicional puede resolver un concepto, pero no reemplaza instalar una aplicación que todavía no se ha probado.

Selecciona un ejercicio de refuerzo vinculado al criterio y define qué cambiará respecto al primer intento. Cambia datos o escenario para comprobar transferencia de aprendizaje. Si repites exactamente una solución memorizada, añade una pregunta que te obligue a explicar el efecto de una opción o a distinguir dos causas posibles.

Para una dependencia técnica, vuelve al módulo que la fundamenta. Un fallo al unir un equipo a un dominio puede requerir repasar DNS y tiempo; un permiso incorrecto puede depender de identidad, sesión o herencia. El mapa permite cruzar materiales, conservando cuál es el resultado que se quiere demostrar en cada módulo.

Cuando falte equipamiento físico, deja una actividad pendiente identificada y coordina su ejecución con el centro. Puedes preparar un plan de prueba y analizar datos sintéticos mientras tanto. La documentación debe indicar con precisión qué se ha ensayado y qué requiere observación posterior.

## 12. Particularidades de optativas y variantes

El catálogo reúne las optativas transversales y específicas de Informática y Comunicaciones aplicables al contexto de SMR revisado. Hay códigos diferentes para francés, inglés y alemán que comparten currículo. Cada guía adapta las tareas al idioma y conserva la identificación oficial correspondiente.

El curso declarado en el catálogo y el encaje de una duración en el plan de SMR se muestran de forma diferenciada. Una asignatura específica de 50 o 90 horas se relaciona con las cargas de la organización madrileña; la decisión de oferta y programación corresponde al centro dentro del marco autorizado.

Las propuestas complementarias de Git y soporte que existían en las carpetas de optativa se conservan como talleres propios. El nuevo catálogo añade las guías de códigos oficiales. Elegir una ruta de estudio no significa cursar simultáneamente todas las variantes ni obtener una convalidación por completar un taller del repositorio.

## 13. Incidencias literales de las fuentes

Los referentes conservan peculiaridades de la publicación para que se pueda auditar la numeración. En Proyecto, el RA5 del anexo II del RD 499/2024 imprime dos criterios a). Las claves editoriales `a.1` y `a.2` distinguen ambos registros, manteniendo la letra oficial y las otras letras b) y c). No se inventa un criterio d) para esconder la repetición.

El enunciado del RA6 de Sostenibilidad en el desarrollo madrileño incluye una frase que vuelve a aparecer como criterio a). La guía explica esa incidencia y conserva seis RA con sus criterios. La extracción de un PDF puede añadir además cortes de línea o encabezados; se revisa que esos elementos de maquetación no se conviertan en parte de un resultado.

Los enunciados se contrastan con los documentos oficiales y los CE de las guías se presentan como resúmenes didácticos. Cuando necesites la formulación íntegra, utiliza el referente y el enlace a la norma. Una actividad de este repositorio puede desarrollarse o adaptarse sin cambiar el identificador del criterio que pretende trabajar.

## 14. Datos y comprobaciones automáticas

Cada módulo incluye `alineacion-ra.json`. Sus datos relacionan resultados, criterios, actividades y rutas. El [referente normativo](../recursos/ra/referentes-oficiales.json) conserva el enunciado y las letras para comprobar que la alineación no omite ni añade resultados. Las [fuentes y huellas](../recursos/ra/fuentes-verificadas.json) identifican los documentos consultados.

El validador contrasta códigos, secuencias de RA, enunciados, claves de CE, actividades, entregables y enlaces locales. El generador produce mapa, inventario y plantilla. Utilizan la biblioteca estándar de Python y no requieren consultar un servicio externo durante la comprobación:

```bash
python3 scripts/validar_ra.py
python3 scripts/generar_mapa_ra.py
python3 scripts/generar_mapa_ra.py --check
python3 scripts/generar_indice.py
python3 scripts/validar_documentacion.py
```

Estas comprobaciones verifican consistencia estructural y trazabilidad documental. La revisión técnica contrasta si la actividad propuesta permite observar el criterio, y la ejecución aporta las evidencias reales. La combinación de esas tres capas hace que una guía sea revisable y útil para aprender y demostrar una actuación.
