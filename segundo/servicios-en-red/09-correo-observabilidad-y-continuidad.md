# Correo, observabilidad y continuidad de los servicios

[Índice de Servicios en red](README.md) · [Correo local](05-correo-local.md) · [Plantilla de copias](../../recursos/plantillas/plan-de-copias.md)

## 1. Del servicio que arranca al servicio que se mantiene

Un proceso activo puede escuchar en la interfaz equivocada, responder con datos antiguos o denegar a todos los usuarios. La operación combina estado del sistema, protocolo, identidad, datos y experiencia del cliente. No construyas una única luz verde a partir de `systemctl is-active` y la llames disponibilidad de toda la aplicación.

Define para cada servicio un contrato: quién lo usa, qué resultado necesita, qué dependencias tiene, cómo se mide y cómo se recupera. DNS depende de configuración y datos de zona; DHCP de interfaz, ámbito y estado; web de contenido, permisos, certificados y, si existe, backend. Correo añade colas, identidades y acceso a buzones. La comprobación debe seguir ese contrato.

En este capítulo se conserva la separación de escenarios. El correo desplegado en la [práctica anterior](05-correo-local.md) sigue limitado a loopback y con salida externa deshabilitada. La ampliación de arquitectura no autoriza publicar SMTP, submission o IMAP en Internet ni convierte un laboratorio `.test` en un sistema de correo público.

## 2. Correo: cinco identidades que suelen confundirse

El nombre presentado en EHLO identifica al cliente SMTP según su declaración y contexto; el remitente de sobre `MAIL FROM` participa en transporte y devoluciones; la cabecera visible `From` declara el autor del mensaje; la identidad autenticada pertenece al acceso al servicio; el destinatario de sobre determina entrega aunque las cabeceras indiquen otras cosas. Esas identidades pueden ser distintas por motivos legítimos o por abuso.

Un alias o una lista de distribución puede cambiar destinatarios de transporte sin reescribir todas las cabeceras. Un mensaje reenviado puede llegar desde una IP distinta de la infraestructura del dominio del autor. Por ello evaluar autenticación de correo requiere saber qué identidad comprueba cada mecanismo y en qué punto del flujo se aplica.

En el laboratorio local se utiliza un usuario sintético `labmail` y mensajes sin datos personales. Introducir un mensaje mediante la interfaz local `sendmail` no demuestra autenticación de un cliente de red. Conversar con SMTP en loopback demuestra otra parte del recorrido. Un servidor IMAP sería un componente adicional, con su propio proceso, configuración, identidad y TLS.

## 3. SMTP, submission y acceso a buzones

SMTP entre servidores transporta mensajes; submission ofrece entrada controlada desde clientes; IMAP permite gestionar un buzón y sus estados; POP ofrece otro modelo de acceso. No sustituyas un protocolo por otro al diagnosticar: que Outlook o un cliente móvil lea mensajes no prueba que pueda enviar, y un envío aceptado no prueba que el destinatario lo vea.

Los puertos convencionales ayudan a identificar funciones, pero la aceptación exige observar protocolo y configuración. En un diseño protegido distingue TLS implícito y negociación STARTTLS según servicio. STARTTLS necesita una política que impida el envío de credenciales o datos cuando no se pueda negociar conforme al requisito; no se acepta «a veces cifrado» como equivalente a una obligación de cifrado.

La autenticación de cliente requiere un canal protegido y un backend de identidad adecuado. No habilites contraseñas en una escucha pública para continuar una práctica que sólo requería estudiar arquitectura. Los intentos de acceso y políticas de bloqueo también necesitan límites para no impedir a usuarios legítimos ni almacenar secretos en logs.

Para una futura práctica IMAP aislada, planifica ubicación Maildir, usuario propietario, permisos, base de identidad y CA. Dovecot tiene cambios relevantes entre ramas; utiliza el manual de la versión instalada y no mezcles bloques de configuración de 2.3 y 2.4. La aceptación debería leer el mensaje sintético, reflejar estado del buzón y rechazar otra identidad, con listeners expresamente limitados.

## 4. SPF: autorización de origen de transporte

SPF permite que un dominio publique una política sobre qué orígenes están autorizados a enviar para una identidad de transporte pertinente. El receptor evalúa IP de conexión y dominio según reglas del protocolo. No firma el contenido y no autentica por sí solo que el autor visible de `From` sea la persona que afirma ser.

Un resultado de SPF debe interpretarse con su identidad y contexto. `pass` indica que el origen evaluado satisface la política para ese dominio, no que el mensaje sea seguro o deseado. Una cuenta comprometida de un proveedor autorizado puede enviar mensajes maliciosos que cumplan SPF. `fail` o `softfail` tampoco sustituyen una decisión completa de filtrado.

En un diseño de dominio real se enumeran proveedores y flujos legítimos, se evita exceder límites de evaluación y se mantiene la política al cambiar servicios. Añadir inclusiones sin revisar su cadena puede introducir fallos o ampliar confianza de forma no prevista. Las herramientas de prueba deben conservar dominio evaluado, IP, mecanismo y resultado, no sólo una etiqueta verde.

En `.test` y loopback este capítulo no ejecuta una validación SPF de Internet. Se puede dibujar una tabla sintética con dos servidores autorizados y uno ajeno y explicar qué decisión produciría una política propuesta. No publiques un registro copiado con direcciones privadas como receta para un dominio público ni afirmes que el laboratorio demuestra reputación de entrega.

## 5. DKIM: firma y supervivencia a modificaciones

DKIM aplica una firma asociada a un dominio y selector. La clave privada firma en el emisor y el receptor obtiene la clave pública correspondiente del DNS. La firma cubre cabeceras y cuerpo según parámetros y canonicalización. Una modificación posterior puede invalidarla; el resultado depende de qué se firmó y cómo se modificó.

El selector permite administrar claves y rotaciones. La planificación debe dar tiempo a que mensajes firmados con una clave anterior puedan verificarse mientras siguen en tránsito, conforme a la política de retención y publicación. Borrar el registro anterior inmediatamente puede romper verificaciones de mensajes aún pendientes. La clave privada nunca se guarda en un repositorio de documentación.

Un `dkim=pass` demuestra una propiedad de la firma y dominio firmante en ese contexto. No confirma que el texto sea verdadero ni que la persona del nombre visible tenga autorización humana. Múltiples firmas pueden coexistir; un intermediario puede agregar otra sin que todas tengan la misma relación con el autor visible.

Como ejercicio, prepara un mensaje sintético y marca qué cambios conservan o alteran partes cubiertas por una firma conceptual. No inventes una firma base64 y la presentes como válida. Si no se ha montado un firmante y un verificador reales en un entorno aislado, el entregable es análisis de arquitectura, no evidencia de ejecución criptográfica.

## 6. DMARC: alineación y política

DMARC relaciona resultados de SPF o DKIM con el dominio de la cabecera visible `From` mediante reglas de alineación. Por eso SPF y DKIM pueden pasar para dominios que no alinean con ese autor y no satisfacer DMARC. La política publicada ayuda al receptor a tratar fallos y puede proporcionar informes según mecanismos y condiciones aplicables.

Ejemplo conceptual: autor visible `avisos@empresa.example`, retorno de sobre de un proveedor distinto y firma válida con dominio de ese mismo proveedor. Que ambos mecanismos pasen no demuestra alineación con `empresa.example`. Si el proveedor firma además con un dominio que alinea de forma válida conforme a la configuración, el análisis cambia. El sufijo de ejemplo ilustra nombres, sin introducir un dominio real ajeno.

Una implantación real comienza inventariando flujos y observando resultados, incluidos reenvíos, aplicaciones y terceros. Pasar directamente a una política restrictiva sin conocer emisores legítimos puede provocar pérdidas de entrega. Los informes pueden contener información de infraestructura y requieren minimización, acceso y retención apropiados.

La referencia del protocolo revisada en noviembre de 2026 es [RFC 9989](https://www.rfc-editor.org/rfc/rfc9989), que sustituye a RFC 7489 y RFC 9091. Conviene distinguir la especificación actual del comportamiento de receptores y herramientas que implementan versiones anteriores. Este capítulo trabaja las propiedades de alineación y política; no presupone que todas las funciones de la nueva especificación estén desplegadas por cualquier proveedor.

SPF, DKIM y DMARC no garantizan lectura, entrega en bandeja de entrada o ausencia de spam. Reputación, contenido, políticas receptoras, configuración y comportamiento de usuarios también influyen. La práctica SMR debe distinguir propiedades verificadas de promesas comerciales sobre «correo seguro».

## 7. Cola, entrega y semántica de errores

Un código 2xx acepta una etapa conforme al protocolo;4xx representa un fallo temporal que suele permitir reintento;5xx, un rechazo permanente en ese contexto. El texto y el momento importan. Aceptar un destinatario no equivale a aceptar todo el contenido; aceptar DATA no equivale a que la persona haya leído el mensaje.

Sigue un identificador de cola a través de registros y archivo de buzón. Si la cola está vacía, el mensaje pudo entregarse, rechazarse antes de encolarse o terminar en devolución. Una cola que crece puede revelar destino no alcanzable, DNS, política o servicio local de entrega; no se soluciona borrándola completa sin preservar las causas y la responsabilidad sobre los mensajes.

En el ejercicio loopback, un destinatario externo de prueba debe rechazarse o tratarse conforme a los transportes de error explícitos. Si se acepta una ruta externa no prevista, detén el escenario y revisa antes de reconectar adaptadores. La política de «sólo local» se verifica por escucha y comportamiento, no por ausencia de tráfico durante unos segundos.

## 8. Observabilidad: registros, métricas y pruebas sintéticas

Un registro describe eventos; una métrica resume una magnitud a lo largo de tiempo; una prueba sintética ejecuta una operación prevista para observar experiencia. Pueden complementarse. Un servicio puede fallar a una parte de clientes mientras el promedio global parece normal. Elige señales relacionadas con requisitos y conserva dimensiones útiles sin recopilar datos innecesarios.

Para DNS, observa consultas de registros conocidos, respuestas negativas previstas, latencia y coherencia de autoridades. Para DHCP, capacidad de pool, asignaciones y renovaciones. Para web, códigos, duración total, tiempo del backend y errores. Para correo local, aceptación, cola, entrega y acceso al mensaje sintético cuando el componente exista.

Los timestamps necesitan zona y sincronización suficientes para correlacionar. Guardar «10:30» sin fecha ni zona dificulta relacionar máquinas. Añade identificadores de solicitud cuando la aplicación y la privacidad lo permitan. Evita registrar contraseñas, cookies de sesión o contenido completo por defecto para facilitar diagnóstico.

Un pequeño conjunto de [registros sintéticos](ejemplos/registros-servicios-sinteticos.csv) acompaña el capítulo. Es un material para calcular indicadores e interpretar causas; no es una exportación del laboratorio ni representa tiempos reales. Las fechas y duraciones se eligieron como datos didácticos.

## 9. Indicadores y percentiles con números explícitos

Supón 1.000 peticiones válidas de prueba en una ventana y dos respuestas que incumplen el contrato. La tasa de éxito definida para ese conjunto es 998/1000=99,8%. Si excluyes ciertas peticiones, documenta por qué: cambiar denominador después de ver resultados altera el indicador. Un 404 esperado en una prueba negativa no necesariamente cuenta como fallo del servicio.

Para diez latencias ordenadas `10,12,13,15,16,18,20,25,40,200ms`, la mediana es(16+18)/2=17 ms. La media es 369/10=36,9 ms. El promedio oculta que una petición tardó 200 ms. Con la convención de rango más próximo, el p95 usa la posición ceil(0,95×10)=10 y vale 200 ms. Con tan pocas observaciones, el percentil es inestable; indica método y muestra.

Un objetivo hipotético de 99,5% sobre 30 días completos de 24 horas admite 0,5% de 43.200 minutos, es decir 216 minutos fuera del contrato, si esa definición cuenta todos los minutos por igual. No se trata de un SLA oficial del centro ni de un compromiso real con un cliente. Mantenimiento, degradación parcial y método de muestreo necesitan definirse antes de evaluar.

Una comprobación cada cinco minutos puede no observar una caída de dos minutos entre muestras. Por tanto «todos los sondeos dieron 200» no demuestra disponibilidad continua perfecta. Equilibra frecuencia, coste y sensibilidad. No ejecutes sondeos masivos desde el aula contra servicios ajenos para crear una serie estadística.

## 10. Alertas que conducen a una acción

Una alerta útil contiene servicio, condición, ventana, impacto y enlace al procedimiento de diagnóstico. «CPU alta» no explica si afecta al contrato; puede ser un trabajo previsto. Combina síntomas de experiencia con señales de causa. Dos fallos consecutivos de una consulta crítica pueden merecer investigación, pero el umbral depende del entorno y del coste de falsas alarmas.

Ejemplo didáctico de TLS: avisar si el certificado servido al cliente vence dentro del margen acordado. La acción consiste en revisar inventario, renovación, cadena y despliegue, no en ampliar confianza o ignorar la validación. Para DNS secundario: avisar si el serial permanece incoherente durante una ventana superior a la prevista y confirmar antes que se consulta el servidor correcto.

Gestiona silencios y ventanas de mantenimiento de forma explícita, con responsable y expiración. Silenciar para siempre una alerta molesta convierte el monitor en una decoración. Después de un incidente revisa si el aviso llegó a tiempo y si su instrucción permitía distinguir las causas más probables.

## 11. Continuidad y dependencias de restauración

RPO expresa pérdida de datos admisible en tiempo y RTO tiempo objetivo para recuperar el servicio. Son objetivos que se deben contrastar con procedimientos medidos. Una copia diaria no demuestra RPO 24 h para una base que cambió sin coherencia o para una clave que no se incluyó nunca. Un RTO 20 min no se cumple porque el backup «terminó bien».

Caso sintético: arrancar VM tarda 5 min; preparar red/DNS,3; restaurar datos,12; validar desde cliente,5. Total 25 min si esas tareas son secuenciales y completas. Con objetivo 20 min la recuperación incumple por cinco. La mejora puede ser automatizar preparación o reducir restauración, pero hay que volver a medir. No restes la validación para declarar éxito antes de que el servicio funcione.

Si una copia se tomó a las 18:00 y el incidente ocurre a las 20:30, podrían faltar 2 h 30 de cambios según el sistema y método. El RPO real se calcula respecto al último punto recuperable coherente, no simplemente la hora de inicio del trabajo de copia. Un archivo corrupto o una exportación incompleta no constituye un punto válido por tener timestamp reciente.

Las dependencias deben restaurarse en orden: red y nombres necesarios, identidad según arquitectura, secretos por canal protegido, datos, configuración y aplicación. Un servidor web puede arrancar antes que su base y seguir dando 502. Un servicio autenticado puede requerir directorio y hora. Documenta el orden y prueba desde cliente con una identidad ordinaria.

## 12. Práctica integradora: una caída explicada y recuperada

Escoge DNS, HTTPS o correo local ya desplegado en la VM de prácticas. Define contrato y dos comprobaciones, una positiva y otra negativa. Conserva copia e instantánea, y registra estado inicial. Elige un fallo reversible y único: detener un daemon desde consola, cambiar un registro sintético o retirar temporalmente una referencia de certificado en un clon.

Recoge eventos y pruebas en una ventana corta. Propón al menos dos hipótesis, una prueba que las discrimine y una corrección mínima. Restaura y valida datos, autorización, certificado cuando proceda y coherencia con los demás servicios. Si mides RTO, inicia y termina el reloj conforme a la definición escrita antes de ejecutar.

Entrega cronología, evidencias saneadas, indicador calculado, causa confirmada o limitación explícita y procedimiento de retorno. Añade una mejora operativa relacionada con la causa: validación antes de recargar, revisión de seriales, custodia de clave o capacidad de pool. No cierres con una lista genérica de buenas prácticas que no explique el incidente.

La rúbrica propia asigna 20% contrato/diseño,25% evidencia/interpretación,25% recuperación y 20% medición; el 10% restante valora claridad y privacidad. Las pruebas se ejecutan sólo en equipos propios autorizados y no se consideran realizadas por leer las tablas de ejemplo.

## Referencias primarias

- [RFC 5321: SMTP](https://www.rfc-editor.org/rfc/rfc5321).
- [RFC 6409: submission](https://www.rfc-editor.org/rfc/rfc6409).
- [RFC 8314: TLS para correo](https://www.rfc-editor.org/rfc/rfc8314).
- [RFC 7208: SPF](https://www.rfc-editor.org/rfc/rfc7208).
- [RFC 6376: DKIM](https://www.rfc-editor.org/rfc/rfc6376).
- [RFC 9989: DMARC, referencia actual](https://www.rfc-editor.org/rfc/rfc9989).
- [RFC 7489: versión anterior, para interpretar documentación y herramientas heredadas](https://www.rfc-editor.org/rfc/rfc7489).
- [Postfix: registros y diagnóstico](https://www.postfix.org/DEBUG_README.html).
- [Dovecot: documentación por versión](https://doc.dovecot.org/).
- [Nginx: formato de logs](https://nginx.org/en/docs/http/ngx_http_log_module.html).
- [systemd: journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html).
