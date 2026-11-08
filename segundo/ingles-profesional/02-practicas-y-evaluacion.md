# Prácticas de Inglés profesional

Estas tareas son propuestas de aprendizaje. Las salidas técnicas y el progreso lingüístico deben recogerse durante su realización; los ejemplos no acreditan una intervención ya ejecutada.

## Práctica 1. Convertir una queja en un ticket reproducible

**Situación:** una persona dice: “The intranet does not work after I changed the network settings.” Dispones de `cli01`, un servidor de laboratorio y permiso para consultar su configuración. No cambies parámetros en esta actividad: el objetivo inicial es recopilar información.

1. Redacta cinco preguntas en inglés sobre alcance, momento, equipo, mensaje y cambios realizados.
2. Registra versión del sistema, nombre del equipo y hora. Usa una fecha completa para evitar confusiones entre día y mes.
3. Consulta configuración IP y DNS mediante la herramienta indicada para el sistema del laboratorio. Copia sólo datos de la red de prácticas.
4. Diferencia una prueba al nombre, una consulta DNS explícita y una prueba al servicio. Explica qué demuestra cada una y qué deja pendiente.
5. Redacta un ticket de 120–180 palabras con observaciones, hipótesis y siguiente acción.
6. Revisa que no haya contraseñas, datos personales ni información de otras interfaces de tu equipo físico.

**Solución orientativa:** preguntas válidas son “Can other users open the intranet?”, “What error message do you see?”, “When did the issue start?”, “Which settings did you change?” y “Can you open any other internal service?”. Si el equipo usa un DNS distinto del servidor de aula y una consulta explícita a `192.168.56.10` responde correctamente, existe evidencia compatible con una configuración de cliente incorrecta. No es prueba suficiente para descartar todos los fallos del navegador o del servidor web. El ticket debe conservar esa diferencia.

**Entregables:** preguntas, ficha técnica, resultados reales y ticket final. La actividad se acepta cuando otra persona puede repetir las pruebas sin adivinar nombres, equipo o herramienta.

## Práctica 2. Guiar una llamada y confirmar la recuperación

**Situación:** una aplicación de escritorio se ha bloqueado con un documento sin guardar. Una persona interpreta a soporte y otra a la persona usuaria; después se intercambian los papeles.

Prepara un guion de tres minutos: presentación, confirmación del problema, advertencia sobre datos no guardados, consulta del procedimiento de recuperación de la aplicación y siguiente paso. No utilices como primera instrucción “restart the computer”. Explica la posible pérdida de trabajo y pide que la persona lea los mensajes. Si no existe una recuperación segura conocida, documenta y escala.

Ejemplo original de fragmento: “Before we close the application, please check whether it offers a recovery option. Do you see an error message or a recovery window? I cannot guarantee that unsaved changes will be recovered.” Después de la actuación, confirma que se abre una copia de prueba, no el documento original sensible.

**Cierre válido:** “The test document opens correctly. The user has confirmed that the application responds. The unsaved changes could not be verified.” Este cierre evita confundir disponibilidad de la aplicación con recuperación de todo el contenido.

**Entregables:** guion, grabación sólo si todas las personas autorizan su uso educativo o transcripción alternativa, lista de instrucciones y revisión por pares. Evalúa claridad, cortesía, escucha y precisión del cierre. El acento no debe penalizarse por sí mismo si el mensaje se entiende.

## Práctica 3. Interpretar un aviso y redactar un correo de mantenimiento

Selecciona una página oficial de un producto usado en el laboratorio. Anota URL, producto, versión y fecha de consulta. Localiza cinco expresiones que indiquen obligación, posibilidad, incompatibilidad o cambio de estado. Parafraséalas sin copiar grandes fragmentos.

Supón una actualización de un servidor de prácticas. Redacta un correo de 120–160 palabras que indique ventana, impacto previsto, acción de las personas usuarias, contacto y confirmación posterior. Incluye un procedimiento de reversión en un anexo técnico en inglés de seis pasos, sin enviar el correo a nadie.

**Solución orientativa:** un mensaje correcto distingue “planned maintenance” de una incidencia en curso; expresa “may be unavailable” cuando la indisponibilidad es posible y no confirmada; no incluye credenciales ni direcciones de producción. El anexo debe ordenar copia previa, verificación de la copia, aplicación del cambio, prueba del servicio, criterio de reversión y registro del resultado. Cada paso necesita objeto: “check the service” es insuficiente si no especifica cuál y cómo.

## Rúbrica propuesta

| Criterio | Peso | Evidencia de logro |
| --- | --- | --- |
| Exactitud técnica | 30 % | Distingue observación, hipótesis, cambio y validación. |
| Comprensión y estructura | 25 % | Incluye información necesaria y orden lógico. |
| Lengua y vocabulario | 20 % | Usa términos y tiempos verbales adecuados. |
| Interacción profesional | 15 % | Pregunta, escucha y confirma sin culpabilizar. |
| Privacidad y revisión | 10 % | Minimiza datos y corrige ambigüedades. |

No se trata de la rúbrica oficial del centro. Un resultado lingüísticamente fluido no compensa una instrucción que provoca una pérdida de datos evitable; identifica el riesgo y corrige el procedimiento antes de repetir la actividad.

## Preguntas razonadas

1. **¿“The server may be down” equivale a “The server is down”?** No: la primera expresa una hipótesis; la segunda afirma un estado y exige evidencia de disponibilidad.
2. **¿Puedes traducir los nombres de las opciones de un comando?** No dentro del comando. La explicación puede traducirse, pero la sintaxis debe coincidir con el producto y su versión.
3. **¿Qué falta en “I fixed the network”?** Síntoma inicial, cambio, alcance y prueba final. Debe explicarse qué se corrigió y cómo se comprobó desde el equipo afectado.
4. **¿“Deprecated” permite eliminar una función sin comprobar dependencias?** No. Debe revisarse la alternativa soportada, la compatibilidad y la reversión.
5. **¿Cuál es el mejor indicador de una instrucción clara?** Que otra persona pueda ejecutarla y comunicar su resultado sin completar información implícita.

[Guía](01-guia.md) · [Índice](README.md)
