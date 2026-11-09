# Selección profesional, comunicación y organización de equipos

[Índice del módulo](README.md) · [Viabilidad avanzada](05-viabilidad-y-tesoreria-avanzada.md) · [Casos resueltos](06-casos-profesionales-resueltos.md)

## 1. Elegir ofertas mediante requisitos y evidencia

Una búsqueda profesional comienza definiendo funciones, ámbito geográfico o modalidad, condiciones relevantes y nivel de autonomía. No utilices el título del puesto como único filtro: «técnico de sistemas» puede describir soporte de escritorio o una función de administración con responsabilidades diferentes. La lectura debe identificar verbos de trabajo, tecnologías, experiencia, comunicación y condiciones.

Prepara una matriz con cuatro columnas: requisito literal resumido, obligatoriedad según la oferta, evidencia disponible y brecha. Separa «no consta» de «no lo cumplo». Si la oferta no aclara turnos o desplazamientos, se formula una pregunta. No se interpreta que una condición ausente queda garantizada a favor de una u otra parte.

| Requisito ficticio | Evidencia propia | Calidad actual | Próxima acción |
| --- | --- | --- | --- |
| Diagnóstico TCP/IP | Caso de rutas/DNS y pruebas desde cliente | Aplicado en laboratorio | Preparar variante sin guía |
| Windows de escritorio | Gestión de usuarios y resolución de incidencia | Aplicado con ayuda | Añadir criterio de reversión |
| Documentación | Ticket con impacto y aceptación | Revisado por otra persona | Reducir jerga en resumen |
| Linux valorable | Permisos y servicio sencillo | Inicial | Explicar límites y versión |
| Inglés de soporte | Diálogo y correo sintético | Ensayado | Practicar aclaración de síntomas |

Una puntuación propia ayuda a priorizar, pero no predice contratación. Por ejemplo, asigna peso tres a requisitos imprescindibles, dos a tareas frecuentes y uno a elementos valorables. Puntúa evidencia de cero a dos: ausente, parcial o demostrable. Si el total posible es treinta y obtienes veintidós, eso describe ajuste en ese modelo, no una probabilidad del 73,3 % de ser contratado.

No sumes una puntuación alta para ignorar un requisito excluyente explícito. Si necesitas una acreditación obligatoria que no posees, primero verifica su naturaleza y posibilidad de obtenerla. La matriz también puede concluir que otra oferta se ajusta mejor al itinerario actual.

## 2. Construir un CV verificable y legible

El CV organiza información relevante para una decisión. Para un perfil inicial puede dar visibilidad a formación, proyectos y prácticas académicas, siempre con su contexto. Una entrada eficaz identifica acción, tecnología, resultado y alcance: «configuré en VM un recurso Samba con dos roles y comprobé lectura, escritura y denegación» informa más que «experto en servidores».

La adaptación utiliza el vocabulario de la oferta cuando describe lo realizado. No convierte «observé una restauración» en «responsable de recuperación». Una afirmación ambigua puede superar una primera lectura y fracasar en la entrevista; la precisión facilita que se valore la capacidad real.

Respecto a sistemas ATS, no existe una plantilla universal que garantice pasar cualquier filtro. Usa secciones reconocibles, texto seleccionable, estructura lógica y formatos admitidos por el portal. Comprueba el archivo exportado: copiar su texto a un editor permite detectar orden extraño o contenido convertido en imagen. No escondas palabras ni metas tecnologías que no puedes explicar.

### Ejemplo trabajado

Texto inicial: «Soy muy trabajador y domino redes y seguridad». Revisión: «Proyecto académico: diseño de una LAN virtual, cálculo de subredes y diagnóstico de DNS; documentación de tres pruebas y de una recuperación. Trabajo realizado en Debian y Windows de laboratorio». La revisión describe evidencia y evita atribuir responsabilidad de producción. Puede enlazar una memoria sanitizada donde se vea qué parte realizó la persona.

Prepara una versión breve para la oferta y conserva una base privada de proyectos. Revisa enlaces, título del PDF y datos de contacto por el canal de candidatura. En la entrega pública del ejercicio utiliza una identidad ficticia; no necesitas publicar un teléfono o dirección para demostrar adaptación de contenido.

## 3. Entrevista: reconstruir decisiones, no recitar respuestas

En una entrevista técnica de soporte interesa cómo preguntas, priorizas, contrastas y explicas límites. Ante «no abre la aplicación», no empieces por reinstalar: delimita usuario/equipo/servicio, momento, error, cambios y pruebas seguras. Si faltan datos, explicar qué preguntarías puede ser una respuesta más sólida que inventar una causa.

Para relatar experiencia usa una estructura: situación, tarea, acción propia, resultado y aprendizaje. STAR ayuda a ordenar, pero no obliga a fabricar una historia heroica. Indica participación y ayuda. Un resultado medido debe tener método; «reduje el tiempo a la mitad» requiere explicar comparaciones y alcance.

### Relato de ejemplo

Situación: en una práctica dos clientes resolvían un nombre de forma distinta. Tarea: encontrar la causa sin cambiar el servidor. Acción: registré resolutores de cada cliente, consulté directamente el DNS LAB y comparé caché/configuración. Resultado: identifiqué que un cliente usaba el resolutor de NAT; tras el cambio autorizado repetí consulta y acceso. Aprendizaje: una respuesta por IP no probaba que DNS estuviera bien. La historia identifica laboratorio, responsabilidad y prueba final.

Si no has trabajado con una tecnología solicitada, dilo y relaciona bases transferibles. Conocer permisos UNIX ayuda a entender autorización, pero no equivale a dominar GPO. Propón un primer itinerario y fuentes. La sinceridad se acompaña de método; no consiste en responder únicamente «no sé» cuando puedes explicar cómo aprenderías con seguridad.

## 4. Prueba práctica de selección

Antes de comenzar lee objetivo, tiempo, entorno y acciones permitidas. Identifica datos a preservar y cómo pedir aclaración. No supongas autorización para escanear sistemas externos o usar credenciales ajenas porque se trate de una entrevista. Una prueba legítima debe delimitar su escenario.

Organiza el tiempo entre lectura, ejecución, comprobación y entrega. Si te bloqueas, registra lo probado y una hipótesis siguiente. Una captura de un error acompañada de razonamiento puede mostrar más que ocultar el fallo. No borres registros ni simules una salida exitosa.

Al entregar explica estado final, requisitos cumplidos, pendiente, riesgo y reversión. Si la prueba incluye un script, comenta las decisiones relevantes y evita cambios globales innecesarios. La persona evaluadora debe poder ver qué haría el script antes de ejecutarlo; un modo de consulta o simulación ayuda a discutir alcance.

## 5. Comunicación de servicio en tres capas

Un ticket operativo puede separar resumen para usuario, detalle técnico y seguimiento. El usuario necesita impacto, estado, siguiente paso y momento de próxima información. El técnico que releva necesita entorno, pruebas, cambios y datos relevantes. El responsable necesita alcance y dependencias para priorizar. No es necesario copiar todos los logs en los tres niveles.

| Nivel | Ejemplo adecuado | Problema de una alternativa vaga |
| --- | --- | --- |
| Usuario | «El puesto sigue sin acceder; hemos delimitado el fallo y revisaremos su configuración de red» | «Es un problema complicado» no da estado ni próximo paso |
| Técnico | «Consulta directa a DNS LAB correcta; resolutor del cliente difiere del previsto» | «DNS arreglado» no permite reproducir |
| Coordinación | «Afecta a un puesto; servicio común responde; no se requiere aún reinicio global» | «Hay fallos de red» sobredimensiona alcance |

No prometas una resolución que depende de un repuesto o de otra entidad sin explicar la dependencia. Puedes comprometer una próxima actualización si controlas ese acto. Un mensaje profesional indica incertidumbre concreta: «falta comprobar si el error se reproduce con otro perfil», no una certeza falsa ni una evasiva genérica.

## 6. Gestión de desacuerdos y feedback

Describe conducta observable, efecto y petición. «En los tres tickets revisados falta la prueba de usuario; sin ella no podemos confirmar cierre. Propongo añadirla antes de pasar a terminado» permite una respuesta. «Siempre trabajas mal» generaliza y desplaza la conversación a la defensa personal.

La otra persona puede aportar una limitación real: el formulario no permite registrar la prueba o el usuario no estaba disponible. El acuerdo debe cambiar el proceso: estado pendiente de validación, responsable y siguiente acción. No se exige marcar como cerrado para cumplir una métrica si falta el criterio.

El feedback técnico se separa de la decisión disciplinaria o personal. Durante una revisión de código o memoria señala un fallo, muestra evidencia y propone alternativa. Si no estás seguro, formula una pregunta comprobable. Admitir una corrección fundada evita mantener un error por orgullo o jerarquía.

## 7. Kanban, límites y trabajo interrumpido

Un tablero puede tener pendiente, preparado, en curso, bloqueado, validación y terminado. «Preparado» exige objetivo, permiso y datos suficientes. «Terminado» exige comprobación, registro y aceptación definida. Si las columnas no tienen criterio, mover tarjetas sólo cambia su apariencia.

Limita trabajo en curso según capacidad y revisa bloqueos. Para un grupo de tres personas, un límite didáctico de tres tareas activas permite estudiar flujo; no es una regla universal. Una incidencia urgente puede requerir reorganizar, pero registra qué se interrumpe y cómo se conserva estado. Abrir diez tareas no multiplica capacidad.

Mide tiempo de ciclo desde un punto definido hasta la finalización; separa espera y trabajo cuando sea útil. No compares equipos con criterios de inicio distintos. La tasa de cierre debe analizarse junto a reaperturas, dificultad y calidad: una mejora aparente puede ser resultado de cerrar antes de verificar.

## 8. Scrum como referencia y elección de método

Scrum propone una organización específica con responsabilidades, eventos y artefactos. Consultar su guía ayuda a evitar que cualquier reunión diaria se llame Scrum. Un servicio de soporte con entradas imprevisibles puede necesitar otra organización de flujo; adoptar vocabulario no garantiza ajuste.

En un proyecto académico con producto y revisiones periódicas se pueden practicar objetivos de iteración, incremento verificable y retrospectiva. Aclara si se aplica el marco completo o sólo una actividad inspirada en él. Las rúbricas y el currículo del centro no se sustituyen por la terminología de un método de gestión.

Una decisión razonada compara demanda, estabilidad de requisitos, dependencias, tamaño de equipo y coste de coordinación. El método es un medio para entregar valor y aprender, no un fin que justifique documentos sin utilidad. Si el tablero revela bloqueo por falta de permisos, la solución es resolver esa dependencia, no añadir otra ceremonia.

## 9. Taller de selección y colaboración

Forma un grupo con roles rotatorios de candidatura, selección y observación. Trabaja con una oferta ficticia y dos evidencias académicas. La candidatura dispone de una matriz de requisitos y un CV breve; selección prepara preguntas técnicas y de comunicación; observación registra afirmaciones apoyadas, preguntas de aclaración y límites respetados.

Después simulad una incidencia que requiera relevo: la primera persona diagnostica, otra continúa y la tercera verifica. Cada rol sólo puede utilizar el ticket y los archivos entregados, sin explicaciones orales adicionales durante el relevo. Identificad qué información faltó y modificad la plantilla. El ejercicio valora transmisión y organización, sin atribuir experiencia laboral real.

Entregables: matriz, CV ficticio, guion de entrevista, dos respuestas estructuradas, ticket de relevo y retrospectiva. Rúbrica propia: ajuste y honestidad 25 %, razonamiento técnico 25 %, comunicación 20 %, colaboración y seguimiento 20 %, privacidad/formato 10 %.

## 10. Referencias primarias

- [Europass](https://europa.eu/europass/es): herramientas para presentar competencias y experiencia.
- [SEPE: empleo](https://www.sepe.es/HomeSepe/personas/encontrar-trabajo.html): canales e información para la búsqueda.
- [Guía oficial de Scrum](https://scrumguides.org/scrum-guide.html): referencia del marco, no obligación curricular.
- [Kanban Guide](https://kanbanguides.org/): referencia para estudiar flujo y criterios explícitos.
- [INCIBE: protección y uso seguro de información](https://www.incibe.es/): consulta de recursos al preparar evidencias y candidatura.

Los anuncios, puntuaciones, mensajes y roles de este capítulo son ficticios. Los ejemplos no implican enviar candidaturas o contactar con entidades reales.
