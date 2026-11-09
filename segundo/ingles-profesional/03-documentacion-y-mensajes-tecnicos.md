# Documentación operativa y cuarenta mensajes técnicos

[Índice del módulo](README.md) · [Simulaciones resueltas](04-simulaciones-y-defensa.md)

## 1. Una comunicación que permita decidir

Un mensaje técnico útil responde a cuatro preguntas: qué se ha observado, qué consecuencia tiene, qué se propone hacer y cuándo se informará de nuevo. El destinatario debe distinguir un dato comprobado de una posibilidad. Escribe “The DNS query timed out” cuando eso sea lo observado; “The DNS server is down” requiere evidencia adicional. El primer enunciado informa de una prueba; el segundo atribuye una causa.

El grado de detalle depende de la persona que recibe el mensaje. Una persona usuaria necesita saber si puede seguir trabajando, qué acción realizar y qué debe evitar. Otro técnico necesita equipo, versión, intervalo temporal, estímulo y salida. La coordinación necesita impacto, decisión pendiente y siguiente actualización. Mantén un mismo hecho técnico en tres versiones adaptadas, sin alterar la certeza de lo que sabes.

Evita pronombres ambiguos en operaciones. “Restart it after changing it” no permite saber qué se reinicia y qué archivo cambia. Escribe el objeto: “After saving the DHCP configuration, validate the file and restart the DHCP service.” Si el cambio puede cortar una sesión, añade la precondición correspondiente. No conviertas una recomendación general en una orden que cualquier persona deba ejecutar inmediatamente.

## 2. Leer un procedimiento antes de traducirlo

Realiza una lectura en tres pasadas. Primero identifica producto, versión, rol y objetivo. Después marca requisitos, advertencias, privilegios y objetos modificados. Finalmente reconstruye entrada, acción, resultado esperado y reversión. Una traducción correcta de cada palabra puede seguir produciendo un procedimiento incorrecto si corresponde a otra edición de Windows o a otro rol de Samba.

Presta atención a condiciones: “unless”, “provided that”, “only if”, “before” y “after” cambian cuándo se aplica una instrucción. “Do not remove the device until the operation completes” exige esperar una finalización comprobada; no basta con un intervalo arbitrario. “May” puede expresar posibilidad o permiso según contexto. “Must” suele indicar obligación; “should”, recomendación. Conserva esa diferencia al escribir tu memoria.

En una ficha bilingüe conserva sin traducir nombres de comandos, parámetros, rutas y mensajes exactos. Explica en español su finalidad y contexto. No traduzcas `ReadOnly` dentro de código ni una clave de configuración que el programa espera literalmente. Identifica por separado una traducción explicativa y el texto que debe introducirse en la aplicación.

## 3. Registro de fechas, cifras y alcance

Para evitar ambigüedad internacional usa fechas como `2026-11-08` y añade zona horaria a los eventos. En prosa inglesa escribe “8 November 2026” si el contexto requiere una fecha legible. `03/04/2026` puede interpretarse de maneras distintas. Confirma oralmente cifras sensibles: “That is fifteen, one-five, not fifty.” Repite unidades, prefijos y nombre de interfaz cuando una confusión pueda cambiar el objeto de la intervención.

Los modelos siguientes son originales y emplean datos sintéticos. No afirman que las pruebas se hayan realizado. Adapta cada mensaje al resultado real de la práctica y conserva su intención comunicativa. Los números identifican situaciones, no una secuencia que deba enviarse completa.

## 4. Recepción y delimitación: mensajes 1–10

### 1. Solicitar reproducción

> Could you describe the steps immediately before the error appears? Please include the application name, the approximate time and the exact error message. Do not send passwords or the contents of personal documents.

Pide una secuencia reproducible y limita la información. “Exact error message” aporta precisión sin solicitar una captura indiscriminada. La cortesía no elimina la necesidad de una petición concreta.

### 2. Determinar el alcance

> Does the problem affect only this workstation, or can another authorised user reproduce it on a different workstation? Please keep using the normal account; an administrator account could hide a permissions issue.

La comparación entre usuarios y equipos ayuda a separar identidad y dispositivo. El mensaje evita recomendar privilegios elevados como solución inicial y explica por qué alterarían la prueba.

### 3. Preguntar por el último estado correcto

> When did the connection last work as expected? Were there any updates, cable changes or account changes afterwards? These details will help us compare the current state with the last known working configuration.

“Last known working” designa una referencia observada. Preguntar por cambios no presupone que la persona usuaria haya causado el fallo ni convierte una correlación temporal en causa confirmada.

### 4. Confirmar prioridad

> I understand that four users cannot access the shared folder. Is there a deadline or business task currently blocked? I will use the impact and urgency to assign a priority according to the agreed support procedure.

Separa impacto y urgencia. No promete prioridad máxima a cualquier solicitud ni hace depender la clasificación de que alguien escriba “urgent” en el asunto.

### 5. Resumir lo entendido

> To confirm my understanding: local files open normally, but files on the shared drive fail to open from this account. The issue started this morning and affects one user. Please correct anything I have misunderstood.

El resumen permite corregir una hipótesis de alcance antes de intervenir. Evita convertir “shared drive” en un diagnóstico: aún puede haber red, permisos, bloqueo de archivos o aplicación implicados.

### 6. Distinguir solicitud y avería

> The requested application is not installed on this workstation. This appears to be a software installation request rather than an outage. I will check the approved catalogue and the required authorisation before scheduling the installation.

No promete instalar un producto por haber recibido un ticket. Identifica el tipo de trabajo y la dependencia de autorización y catálogo, con vocabulario comprensible.

### 7. Acordar un canal accesible

> Would written instructions be easier to follow than a phone call? I can provide one step at a time and wait for your confirmation. Let me know if you need the text enlarged or explained differently.

Ofrece opciones sin atribuir una dificultad personal. La accesibilidad de la comunicación incluye ritmo, canal y formato, además del idioma o la precisión de los términos.

### 8. Confirmar una dirección

> Please read the address shown next to the LAB adapter. We need the address of that adapter, not the default gateway or the NAT adapter. I will repeat it back before we change any settings.

El objeto se define por función. Repetir la dirección reduce errores de transcripción; identificar la NIC evita que una prueba de laboratorio termine cambiando la conexión de Internet.

### 9. Pedir una evidencia mínima

> Please copy only the error code and the two lines immediately around it. Remove names, document contents and unrelated addresses. If you are unsure whether the extract is appropriate to share, ask your supervisor first.

Un extracto acotado suele ser más útil que un registro completo. La instrucción identifica el contenido necesario y un canal de consulta cuando la clasificación de la información no esté clara.

### 10. Registrar una observación sin diagnóstico

> The client received no response to three DNS queries directed at the laboratory server. We have not yet established whether the cause is the service, a firewall rule or the selected network path. Further checks are required.

La frase enumera hipótesis sin elegir una por intuición. “No response” describe el resultado; no equivale automáticamente a “server unavailable” ni a pérdida total de conectividad.

## 5. Diagnóstico y cambios: mensajes 11–20

### 11. Explicar una prueba de sólo lectura

> I would like to check the current IP configuration and routes. These commands only display information; they do not change the network settings. We will review the output before deciding whether a configuration change is necessary.

Describe propósito y efecto. Esta explicación ayuda a conseguir cooperación y permite comprobar que el comando propuesto coincide con una consulta, no con una modificación encubierta.

### 12. Comparar nombre y dirección

> The HTTPS connection works when the destination address is specified while preserving the expected host name. The normal name lookup returns a different address. We will investigate DNS selection and cached answers before changing the web server.

La mención al nombre preservado importa para TLS y servidores virtuales. No se recomienda simplemente abrir una IP e ignorar que eso cambia nombre, SNI y validación del certificado.

### 13. Comunicar un acceso denegado

> Authentication succeeded, but the account does not have write permission on this folder. I will compare the group membership and effective permissions with the approved access matrix. I will not grant broad access as a temporary shortcut.

Distingue autenticación de autorización y relaciona el cambio con un requisito. La frase “effective permissions” evita fijarse sólo en un permiso de una capa del servicio.

### 14. Solicitar una ventana

> The proposed change may interrupt access for approximately ten minutes. Could you confirm a suitable maintenance window and the person who will validate the service afterwards? We will keep the previous configuration available for rollback.

La duración es estimada, no garantizada. Se solicita una decisión operativa concreta: cuándo intervenir y quién valida. La disponibilidad de una copia requiere haberla preparado realmente.

### 15. Proponer un plan de reversión

> If the client cannot obtain a valid configuration after the change, we will restore the saved DHCP configuration, validate it and restart the service from the console. We will then repeat the client test and record the outcome.

Una reversión útil identifica condición, objeto y validación posterior. La consola se especifica porque una sesión remota puede depender de la red que se está modificando.

### 16. Detener una acción fuera de alcance

> This request includes a firewall change on the production router. That device is outside the scope of the current laboratory task. I can document the required traffic, but the authorised network administrator must review and apply the change.

Negocia alcance sin discutir la necesidad del servicio. Se ofrece un entregable útil y se identifica el rol que puede decidir sobre una infraestructura distinta.

### 17. Confirmar un respaldo

> Before proceeding, please confirm the identifier and completion time of the backup we intend to use. We also need evidence of a recent restore test. A successful copy job alone does not demonstrate that the service can be recovered.

No confunde ejecución de una copia con recuperabilidad. Identificador y momento permiten seleccionar el punto de recuperación y evitar hablar de “the backup” como un objeto ambiguo.

### 18. Comunicar una dependencia

> Domain enrolment depends on the client using the directory DNS server and having a consistent clock. We will verify those prerequisites first. Repeating the enrolment command will not correct an unresolved DNS or time synchronisation problem.

El mensaje explica el orden de trabajo. “Prerequisites” es vocabulario importante al leer manuales: una advertencia de requisito no es un paso opcional que se pueda saltar.

### 19. Pedir aprobación de un cambio concreto

> Please review change C-07: update the laboratory DNS record for the intranet, validate the zone and test resolution from the client. No other records are included. The proposed window and rollback steps are attached for review.

La decisión se refiere a un cambio delimitado y revisable. El ejemplo no autoriza enviar mensajes reales: en clase se redacta como simulación con datos ficticios.

### 20. Reconocer una limitación de evidencia

> We have confirmed that the process is running and listening on the intended address. The end-to-end client test is still pending. I will report the service as verified only after the client receives the expected response with the correct permissions.

Relaciona estado de proceso, escucha y aceptación funcional. Evita presentar un resultado parcial como cierre y deja visible la prueba pendiente.

## 6. Seguimiento y recuperación: mensajes 21–30

### 21. Primera actualización de un incidente

> We are investigating an access problem affecting the shared documentation service. Local applications remain available. Please avoid repeated password resets while we check the cause. The next update will be provided at 11:00 UTC, even if the investigation is ongoing.

Expone impacto y siguiente contacto. Una hora de actualización no es una hora de reparación; mantener esa distinción evita promesas que los datos todavía no permiten hacer.

### 22. Informar de una mitigación

> A temporary read-only copy is available for the agreed documents. It supports consultation but does not accept changes. This workaround reduces the immediate impact; it does not mean that the original service has been fully restored or the cause confirmed.

Explica los límites del recurso alternativo. “Workaround” no equivale a solución definitiva, y el modo de sólo lectura debe reflejarse en la comunicación para evitar pérdida de trabajo.

### 23. Actualizar sin avances concluyentes

> The latest checks ruled out an incorrect client address, but we have not isolated the remaining fault. We are now comparing service logs with the connection attempt timestamps. There is no confirmed restoration estimate yet; the next update remains scheduled for 11:30 UTC.

Informar de lo descartado aporta progreso sin inventar certezas. La frase conserva una cadencia de comunicación aunque no exista una estimación fiable de finalización.

### 24. Avisar de una restauración en pruebas

> The selected data set has been restored to an isolated test location. We are comparing file contents, permissions and application behaviour before making any recovery decision. The original data and the only backup copy have not been overwritten by this test.

El destino de ensayo es explícito. La afirmación final sólo se conserva si coincide con lo realizado; es una condición de diseño, no un texto que se copia sin verificar.

### 25. Comunicar el punto de recuperación

> The latest verified recovery point is 18:00 UTC yesterday. Changes made after that point may not be included. Please identify any critical updates from the affected period so that the recovery owner can assess them before the restored service is accepted.

Permite comprender la ventana de pérdida de datos. No promete recuperar información posterior sin haber comprobado fuentes adicionales o procedimientos específicos.

### 26. Solicitar validación del usuario

> Please sign in with your normal account, open the agreed test document and save a new copy in the authorised folder. Tell us whether all three steps complete successfully. Do not use an administrator account for this acceptance test.

La validación contiene acciones observables y un contexto de permisos. “It works now” resulta insuficiente si sólo se ha probado lectura cuando el requisito también incluía escritura.

### 27. Cerrar con causa confirmada

> Access has been restored and validated from the client. The confirmed cause was an incorrect group assignment introduced during a documented account change. The assignment has been corrected, and a negative access test confirmed that unrelated accounts remain excluded.

Separa causa, corrección y prueba de control. La evidencia negativa importa tanto como que la cuenta afectada pueda abrir el recurso.

### 28. Cerrar una mitigación con investigación pendiente

> Users can continue working through the temporary service. The original fault remains under investigation in problem record P-04. This incident is being transferred according to the agreed procedure; the unresolved cause and follow-up owner are recorded explicitly.

No oculta la falta de causa raíz. El procedimiento de cierre o transferencia depende de la organización; la comunicación debe conservar propietario y trabajo pendiente.

### 29. Explicar una reapertura

> The same symptom reappeared after the workstation restarted. We have reopened the incident and retained the previous test results. We will check configuration persistence and start-up dependencies before assuming that the earlier corrective action addressed the root cause.

Una recuperación temporal puede no persistir. “Root cause” sólo debe usarse cuando el razonamiento y la evidencia la sostengan; el ejemplo evita atribuirla por mera coincidencia.

### 30. Resumir una revisión posterior

> The review identified a missing validation step in the change procedure. We will add a client-side test after renewal and record its result before closing future changes. This action addresses the process gap without attributing blame to an individual.

La mejora se vincula a una omisión concreta y verificable. Evita revisiones que sólo recomiendan “be more careful” sin introducir un control que pueda comprobarse.

## 7. Documentación y trabajo profesional: mensajes 31–40

### 31. Aclarar la versión de un manual

> This procedure was written for a different software release. Before applying it, I will compare the package version, configuration path and supported options with the installed system. Similar product names do not guarantee identical commands or defaults.

La compatibilidad se verifica por datos de versión y contexto. No se rechaza una guía únicamente por su antigüedad ni se acepta sólo porque su fecha sea reciente.

### 32. Detectar una advertencia

> The manual states that the service must be stopped before this maintenance action. We need to identify the affected users, plan the interruption and confirm the restart checks. The warning is part of the procedure, not optional background information.

Conserva el carácter obligatorio de “must”. El estudiante debe explicar qué acción cambia si se omite esa condición, además de traducir la frase.

### 33. Revisar una instrucción ambigua

> The instruction “change the address and restart it” is ambiguous. Please specify the adapter, the new address, the service or machine to restart, and the expected result. I will not infer those objects from an unrelated screenshot.

Identifica exactamente qué falta y evita rellenarlo con suposiciones. La calidad de un procedimiento puede medirse por las preguntas que necesita hacer alguien que lo ejecuta por primera vez.

### 34. Entregar una configuración saneada

> The attached example preserves the configuration structure but replaces private names and removes all credentials. The required secret values must be supplied through the approved channel. This file is suitable for technical review, not for direct production deployment.

Una configuración sin secretos puede necesitar información adicional para funcionar. El mensaje distingue documento de revisión y artefacto listo para desplegar.

### 35. Hacer una revisión entre técnicos

> I reviewed the proposed rule against requirement R-03. It permits the intended client traffic, but it also allows access from the management network without a stated need. Please narrow the source range or document the additional requirement and its acceptance test.

La objeción referencia requisito, efecto y cambio propuesto. Es más revisable que valorar la configuración como “unsafe” sin explicar qué comunicación añade.

### 36. Negociar una entrega

> We can deliver the documented laboratory service and restore test by Friday. Adding a second site would require a revised scope, additional configuration and separate acceptance tests. Which deliverable should take priority within the available time?

Presenta una decisión entre alcance, esfuerzo y plazo. No acepta silenciosamente una ampliación que comprometa la calidad de lo ya acordado.

### 37. Explicar experiencia en entrevista

> In a training laboratory, I configured a shared folder with separate reader and editor groups. I tested access with different accounts and documented a restore to another location. I have not administered a production directory independently, and I would follow the organisation's supervision procedure.

La experiencia se presenta con precisión y resultados. Reconocer el entorno de aprendizaje evita atribuir experiencia profesional no adquirida y permite explicar capacidad real.

### 38. Pedir aclaración de una tarea

> Could you clarify whether the goal is to restore access quickly or investigate the underlying cause without changing the current state? I can prepare both activities, but they require different evidence preservation and change decisions.

Recuperación e investigación pueden exigir secuencias distintas. Preguntar por objetivo y restricciones forma parte de una intervención competente, no de una falta de iniciativa.

### 39. Preparar un relevo

> The current configuration and last successful test are recorded in the handover note. The remaining task is the permission check from the second client. No further changes are scheduled. Please contact the named coordinator before extending the scope.

Un relevo debe dejar estado, evidencia, pendiente y coordinación. No basta con enumerar comandos ejecutados; quien continúa necesita saber qué decisión falta.

### 40. Comunicar un límite de confidencialidad

> I can explain the troubleshooting method using a synthetic example, but I cannot share the customer's logs or screenshots outside the approved system. I will prepare a sanitised learning note and request the supervisor's review before using it in my portfolio.

Ofrece una alternativa que conserva el aprendizaje. “Sanitised” no garantiza anonimización por sí solo: una revisión debe considerar identificadores indirectos y contexto.

## 8. Taller de revisión

Elige seis modelos de categorías diferentes y adáptalos a una misma incidencia ficticia. Mantén coherentes alcance, tiempo verbal, evidencias y hora de próxima actualización. Otra persona debe distinguir recepción, hipótesis, cambio, mitigación y cierre sin que le expliques el orden oralmente.

Para revisar, subraya cada afirmación factual y relaciónala con una evidencia prevista. Rodea promesas de plazo y comprueba si son compromisos confirmados o estimaciones. Marca términos ambiguos como “it”, “soon” y “the server” cuando haya varios objetos. Reescribe sólo las frases que impiden actuar; una comunicación técnica no mejora por hacerse innecesariamente larga.

La documentación de [Microsoft sobre comandos PowerShell](https://learn.microsoft.com/powershell/scripting/learn/ps101/02-help-system) permite practicar lectura de sintaxis y ayuda. Las [guías de accesibilidad de W3C](https://www.w3.org/WAI/tips/writing/) ayudan a revisar claridad de títulos e instrucciones. Las expresiones de este capítulo son ejemplos originales, no plantillas oficiales de esos proveedores.
