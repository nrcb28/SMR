# Comunicación técnica en inglés

## 1. Dar información que permita actuar

El soporte exige comunicar el estado del sistema y la siguiente acción. Separa lo que observas de lo que deduces: “The printer is offline” describe un estado; “The network cable may be disconnected” plantea una causa. Antes de pedir cambios, pregunta por el alcance y por el momento en que apareció el problema. Cambiar varios parámetros a la vez dificulta relacionar una acción con el resultado.

Una secuencia útil para una conversación es identificar, delimitar, comprobar, informar y cerrar:

| Función | Expresión de trabajo | Sentido preciso |
| --- | --- | --- |
| Identificar | “Which computer are you using?” | Solicitar el equipo afectado. |
| Delimitar | “Does this happen on every website?” | Distinguir fallo general de fallo de una aplicación. |
| Obtener contexto | “When did you first notice the issue?” | Preguntar por el inicio sin atribuir culpa. |
| Pedir permiso operativo | “May I restart the application after you save your work?” | Evitar pérdida de trabajo. |
| Comprobar | “Please read the message exactly as it appears.” | Registrar el mensaje literal. |
| Confirmar | “Can you open the shared folder now?” | Validar desde la sesión de la persona afectada. |
| Cerrar | “I will document the change and the test results.” | Explicar el cierre del trabajo. |

Las peticiones “Please click…” y “Could you check…?” son claras y corteses. Evita “You did it wrong”; utiliza “The current setting does not match the required configuration”. Cuando no conozcas la respuesta, di qué vas a comprobar y cuándo informarás: “I need to check the server logs. I will send an update by 11:30.” Una estimación no es una garantía de reparación.

## 2. Vocabulario y falsos amigos

| Inglés | Español y uso |
| --- | --- |
| power supply | Fuente de alimentación; no confundir con el cable. |
| power outage | Corte eléctrico; diferente de un cierre de sesión. |
| motherboard / mainboard | Placa base. |
| drive / disk / partition | Unidad, disco y partición son conceptos distintos. |
| memory / storage | RAM y almacenamiento persistente, respectivamente según contexto. |
| network adapter | Adaptador de red físico o virtual. |
| gateway | Puerta de enlace, normalmente un router para otra red. |
| name resolution | Resolución de nombres, habitualmente mediante DNS. |
| credentials | Datos o mecanismos de autenticación; no solicitar su envío en texto claro. |
| permission denied | Operación rechazada por permisos; no prueba por sí sola un problema de contraseña. |
| backup / restore | Copia de seguridad / restaurar. |
| update / upgrade | Actualizar; el segundo suele indicar cambio de versión o capacidad. |
| issue / incident | Problema o incidencia; precisar impacto en el ticket. |
| workaround | Medida temporal que evita el síntoma sin eliminar necesariamente la causa. |
| root cause | Causa raíz demostrada, no la primera sospecha. |
| rollback | Reversión a un estado anterior documentado. |
| downtime | Tiempo en que el servicio no está disponible. |
| deployment | Despliegue o puesta en servicio. |
| log / logging | Registro de eventos / generación de registros. |
| support / maintenance | Soporte / mantenimiento. |

“Actually” suele significar “en realidad”; “currently”, “actualmente”. “Library” es biblioteca; “bookshop” es librería comercial. “Sensitive data” son datos sensibles; “sensible” significa razonable o sensato. “Eventually” expresa un resultado final, no algo que ocurre ocasionalmente. “To apply a patch” significa aplicar un parche; “to apply for a job”, solicitar un empleo.

No traduzcas identificadores que el usuario debe escribir: `ipconfig`, `Get-Service`, el nombre de una interfaz o una ruta deben mantenerse exactos. Puedes explicar en español el significado de una opción, pero una opción `--all` no se convierte en `--todo`.

## 3. Gramática que evita errores operativos

Utiliza presente simple para comportamiento habitual: “The server stores the shared files”. El presente continuo sirve para una acción en curso: “The backup is running”. El pasado simple documenta una acción terminada: “I restarted the service at 10:42”. El presente perfecto relaciona un cambio con el estado actual: “The user has confirmed access”. No escribas “resolved” si únicamente has aplicado un cambio sin verificarlo.

Los modales cambian la fuerza de una instrucción:

- “You must save your work before restarting” establece una condición obligatoria.
- “You should install supported updates” expresa recomendación.
- “The disk may be failing” indica posibilidad, no diagnóstico confirmado.
- “This setting can prevent access” describe capacidad o consecuencia posible.
- “Do not disconnect the power cable” prohíbe una acción concreta.

En manuales, “must”, “required”, “optional”, “deprecated” y “unsupported” determinan decisiones técnicas. “Deprecated” señala una función desaconsejada que puede seguir existiendo; “removed” indica retirada. “Unsupported” no significa que técnicamente sea imposible ejecutarla, sino que no dispone del soporte declarado para ese contexto.

Una condición clara tiene estructura “If…, then…”: “If the service is stopped, record its status before starting it”. Es importante no omitir la condición. La instrucción original “Restart the computer if the installer requests it” no autoriza reiniciar todos los equipos después de cualquier instalación.

## 4. Leer documentación de fabricantes

Empieza comprobando producto, versión, plataforma y fecha. Un procedimiento para Windows Server no se aplica automáticamente a Windows 11; una opción de una versión de Samba puede no existir en otra. Identifica prerrequisitos, privilegios, cambios persistentes y advertencias. Después busca la sección de verificación y de recuperación.

Haz una ficha de lectura con estas columnas: término original, interpretación, evidencia y acción permitida. Por ejemplo, ante “Run the command from an elevated terminal”, registra que se requieren privilegios administrativos; no significa elevar permisos de todas las tareas. Ante “This operation overwrites the destination”, identifica exactamente cuál es el destino y comprueba que el procedimiento permite perder sus datos.

Para resumir un manual utiliza tus propias palabras y enlaza la sección utilizada. No copies páginas enteras. Si empleas un traductor o asistente, compara el resultado con los identificadores originales y revisa especialmente negaciones, unidades, comodines y nombres de discos. Una traducción puede mantener una apariencia correcta y cambiar una condición crítica.

## 5. Tickets y correos profesionales

Un ticket útil incluye equipo, síntoma, impacto, alcance, hora y zona horaria, cambios previos, pruebas con resultados y siguiente responsable. Utiliza un título concreto: “CLI01 cannot resolve intranet.aula.test” es más útil que “Internet broken”. Una IP responde a una prueba diferente de un nombre DNS; no escribas que “the network works” únicamente porque responde `ping`.

Ejemplo original de registro:

```text
Title: CLI01 cannot resolve intranet.aula.test
Environment: Windows 11 Pro, classroom lab, 2026-11-08 10:20 UTC
Impact: The user cannot open the training intranet by name.
Observed: The server is reachable at 192.168.56.10.
Test: nslookup intranet.aula.test 192.168.56.10
Result: Record the actual command output here.
Hypothesis: The DNS record may be missing or incorrect.
Next action: Check the zone on the authorised lab server.
Status: Investigating; resolution has not been confirmed.
```

El campo de resultado es un espacio para una observación real, no una salida ya demostrada. Al cerrar, añade el cambio exacto, el procedimiento de reversión y la confirmación de la persona usuaria. Si una mitigación temporal permite trabajar, registra “workaround applied” y conserva la investigación de causa.

Para un correo, emplea asunto específico, contexto breve, acción solicitada y plazo. Ejemplo: “Subject: Maintenance window for the training file server”. En el cuerpo: “We plan to update the training server on Tuesday from 16:00 to 16:30 UTC. Please save your files and sign out before 16:00. We will confirm when the service is available again.” No prometas ausencia de riesgos ni plazos sin autorización de quien coordina el servicio.

## 6. Comunicación oral, cifras y accesibilidad

Pronuncia cifras y direcciones en grupos y pide confirmación. Para `192.168.56.10`, di los números y “dot”; para una ruta, distingue “slash” `/` de “backslash” `\`. “Dash” puede referirse al guion `-`; para evitar errores, comparte también texto accesible. Aclara “zero” y “letter O”, “one” y “lowercase L” cuando proceda. Las contraseñas no deben dictarse ni anotarse en un ticket.

Habla con frases breves, pausa después de una instrucción y permite que la otra persona confirme su resultado. En una llamada sin vídeo no asumas que ve tu pantalla. Sustituye “click there” por “select Settings, then Network and Internet”. Para una persona que utiliza lector de pantalla, ofrece nombres de controles y secuencia con teclado cuando sea posible.

Una entrevista profesional debe mostrar un ejemplo real del trabajo aprendido. Estructura la explicación con situación, tarea, acción y resultado: “In a classroom lab, I configured a shared folder for two user groups. I tested both allowed and denied access and documented the rollback.” No atribuyas experiencia empresarial a una práctica escolar. Si todavía no has realizado la práctica, utiliza futuro o una descripción del diseño.

## Fuentes y ampliación

- [British Council: English for emails](https://learnenglish.britishcouncil.org/free-resources/business/english-emails), para practicar organización y registro de correos.
- [Microsoft Learn](https://learn.microsoft.com/en-us/), como material auténtico de lectura por versión y producto.
- [Debian Reference](https://www.debian.org/doc/manuals/debian-reference/), para interpretar procedimientos, avisos y términos de administración.
- [INCIBE: empresas](https://www.incibe.es/empresas), para contrastar buenas prácticas de comunicación de incidentes y protección de información.

[Prácticas y evaluación](02-practicas-y-evaluacion.md) · [Índice del módulo](README.md)
