# Seis simulaciones de comunicación y defensa técnica

[Índice](README.md) · [Cuarenta modelos comentados](03-documentacion-y-mensajes-tecnicos.md)

## Cómo realizar una simulación

Trabaja por parejas, alternando soporte y persona usuaria. Una tercera persona puede observar si las preguntas discriminan causas y si las instrucciones respetan el ámbito. Cada simulación produce un ticket, un diálogo de cinco minutos, una nota de relevo y una reflexión breve. Los tiempos son didácticos; no fijan requisitos de evaluación del centro.

No se evalúa únicamente corrección gramatical. Se evalúan precisión técnica, claridad, manejo de la incertidumbre, adaptación al interlocutor y cierre verificable. Una frase simple que evita cambiar la interfaz equivocada tiene más valor operativo que una frase sofisticada con un objeto ambiguo. Conserva el primer borrador y una revisión que explique qué confusión has eliminado.

## Situación 1. Una web funciona por un camino de prueba

**Información inicial:** cli01 no abre `https://srv01.aula.test`. Otra persona afirma que “Internet is broken”. El servidor responde al puerto 443 en LAB. El ejercicio no ha confirmado todavía qué DNS usa el cliente. El alumno de soporte debe evitar modificar simultáneamente DNS, gateway y firewall.

Inicio posible:

> User: The website is down and I cannot continue.
>
> Technician: I understand that the intranet is unavailable from your workstation. Are other websites affected, or only this internal address? Please keep the current settings while we check the connection and name lookup separately.
>
> User: Public websites open normally.
>
> Technician: Thank you. That narrows the scope. I will check the LAB adapter and the DNS answer for the intranet. We have not yet confirmed a fault in the web service.

La solución comunicativa mantiene la hipótesis abierta y propone dos comprobaciones con propósito. Si una prueba con destino fijado y nombre preservado funciona, redacta una actualización que explique qué demuestra y qué queda pendiente. No escribas “fixed” hasta que la resolución normal del cliente y la URL completa sean correctas.

**Entrega:** ticket de 120–160 palabras y actualización de 50–70. **Aceptación:** distingue Internet e intranet, dirección y nombre, observación y causa. La prueba final debe utilizar la cuenta y el contexto previstos, sin dejar una modificación temporal indocumentada.

## Situación 2. Permisos y petición de un atajo

**Información inicial:** una cuenta puede leer y no guardar un archivo. La persona usuaria pide “just give everyone full access”. Existe una matriz que concede escritura sólo al grupo editor. Se debe investigar identidad efectiva, grupo y capas de autorización.

> User: Can you give everyone access so that we can finish?
>
> Technician: I can help restore the access required for your task, but granting access to everyone would also expose documents to unrelated accounts. I will check whether your account belongs to the approved editor group and test the effective permissions.
>
> User: I need to submit the report in twenty minutes.
>
> Technician: I have recorded that deadline. If the permanent correction cannot be validated in time, I will ask the coordinator to assess an authorised workaround. I will not change the access policy without that decision.

La solución reconoce urgencia sin ampliar permisos de manera implícita. Una mitigación puede permitir entregar por un canal autorizado, pero debe indicar quién decide y qué límites tiene. El cierre en inglés debe incluir prueba permitida para la cuenta correcta y denegada para una cuenta ajena.

**Entrega:** explicación para usuario y nota técnica para relevo. **Error crítico de autoevaluación:** confundir acceso de administrador con prueba de autorización del usuario, o declarar causa confirmada sin revisar el principal que utilizó realmente la conexión.

## Situación 3. Manual de otro producto o versión

**Información inicial:** el equipo recibe una guía que recomienda una opción no presente en la versión instalada. El alumno debe explicar cómo comprobar procedencia, requisitos y sintaxis sin desautorizar de forma vaga a quien aportó el documento.

> Colleague: The tutorial says we should add this option. Why are you not doing it?
>
> Technician: The tutorial describes a different release. I will compare the installed package version and its local manual with the procedure. The option may have changed, or it may belong to another operating mode. Applying it without checking could prevent the service from starting.
>
> Colleague: Can we remove the warning and continue?
>
> Technician: We should first identify what the warning refers to. I will record the current configuration, run the documented syntax check and propose the smallest compatible change. We will test it in the laboratory before reusing the procedure.

Prepara una ficha con producto, versión, sección, requisito y equivalencia comprobada. Si no encuentras una equivalencia, escribe “not established” en vez de inventar una opción. La incertidumbre se comunica junto con una acción de verificación, no como una renuncia genérica a investigar.

**Entrega:** ficha bilingüe de lectura y un correo de revisión. El texto de comandos y rutas permanece literal; la explicación se adapta al idioma de la persona que lo aplicará.

## Situación 4. Pérdida de archivos y expectativas de recuperación

**Información inicial:** se solicita recuperar datos de hoy; el último punto verificado es de ayer a las 18:00 UTC. Todavía no se han revisado fuentes complementarias. Hay una copia para ensayo aislado y no se debe sobrescribir el conjunto de trabajo durante la prueba.

> User: Can you guarantee that every file from this morning will come back?
>
> Technician: I cannot confirm that yet. The latest verified recovery point is yesterday at 18:00 UTC. I will check whether additional versions exist, and we will test the selected backup in a separate location before making a recovery decision.
>
> User: How long will it take?
>
> Technician: The transfer estimate is only one part of recovery. Preparation, permissions and application checks also take time. I will provide an updated estimate after the initial restore test and will report progress at the agreed time.

La respuesta evita una garantía no sustentada. Explica RPO y RTO en lenguaje cotidiano, sin obligar al usuario a interpretar las siglas. Incluye quién validará los datos recuperados y cómo se registrarán los faltantes. Si se confirma una pérdida, el mensaje debe describirla con fechas y alcance precisos.

**Entrega:** actualización inicial, comunicación del resultado del ensayo y solicitud de aceptación. Distingue transferencia de archivos, recuperación del servicio y validación de información.

## Situación 5. Ampliación de alcance antes de la entrega

**Información inicial:** el equipo ha acordado un laboratorio de un servidor y un cliente, DNS, archivos y restauración. Una semana antes de la defensa se pide una segunda sede, VPN y alta disponibilidad sin ampliar plazo ni medios. El estudiante debe negociar alcance y prioridades con datos.

> Coordinator: Could you add a second office and automatic failover before the presentation?
>
> Technician: That would change the architecture and the acceptance criteria. The current plan covers the single-office laboratory and a documented restore. We can analyse the second-office design, but implementation would require additional routing, security and recovery tests.
>
> Coordinator: What can you deliver within the current schedule?
>
> Technician: We can complete the agreed service, the restore evidence and a separate extension proposal. If implementation of the second office becomes mandatory, we need to revise the scope and decide which current tasks are deferred.

La respuesta no reduce alta disponibilidad a añadir una VM al dibujo. Distingue propuesta, prototipo y despliegue verificado. Presenta el cambio mediante necesidad, esfuerzo adicional, dependencia y prueba. No atribuyas una decisión presupuestaria al técnico si corresponde a la coordinación.

**Entrega:** nota de cambio de 200 palabras y tabla de dos alternativas. Debe permitir una decisión explícita, con consecuencias sobre pruebas y documentación.

## Situación 6. Entrevista y defensa del proyecto

**Información inicial:** el estudiante debe explicar una solución de soporte sin atribuir experiencia de producción ni convertir resultados esperados en mediciones. Se utiliza una estructura de situación, objetivo, acción propia y resultado observado o pendiente.

> Interviewer: Tell me about a difficult technical problem you solved.
>
> Candidate: In a training laboratory, a user could read a shared folder but could not create files. My task was to identify the cause without granting unnecessary access. I compared the account, group membership and file-system permissions, then tested access with an editor and an unrelated account. I documented the result and the limits of the test. The environment was a laboratory, not a production customer system.

Una buena respuesta explica qué se hizo personalmente, qué ayuda se recibió y cómo se validó. Si la práctica sólo se diseñó, adapta el verbo: “I designed a test plan” en lugar de “I deployed the service”. Practica también una respuesta sobre un error propio: describe el control añadido para evitar repetición, sin inventar una recuperación perfecta.

Preguntas de seguimiento: ¿por qué esa prueba distinguía las hipótesis?, ¿qué permiso se cambió?, ¿qué no se había comprobado?, ¿cómo recuperaría otra persona el entorno?, ¿qué harías con más tiempo? Responde con decisiones y evidencia, no repitiendo una lista de tecnologías.

## Evaluación y mejora

Rúbrica propuesta: precisión técnica 30 %, claridad y adaptación 25 %, manejo de evidencias e incertidumbre 20 %, interacción y escucha 15 %, corrección lingüística suficiente para la tarea 10 %. No certifica un nivel oficial de inglés ni sustituye los criterios del centro.

Asigna a cada error una categoría: ambigüedad de objeto, certeza injustificada, unidad o fecha, alcance, secuencia o forma lingüística. Prioriza corregir aquello que cambiaría una acción. Después revisa gramática y estilo. Repite una simulación con información nueva: otra interfaz, otra hora o un usuario sin el mismo permiso. Así compruebas que dominas la intención y no sólo un texto memorizado.

Para ampliar la lectura utiliza [Debian Reference en inglés](https://www.debian.org/doc/manuals/debian-reference/) y [Microsoft Learn](https://learn.microsoft.com/windows-server/). Selecciona una sección breve y transforma sus requisitos en una lista operativa propia, manteniendo versión, alcance y advertencias.
