# 8. Incidentes, privacidad y casos resueltos

[Índice del módulo](README.md) · [Riesgos](05-riesgos-bia-y-diseno-de-controles.md) · [Hardening](06-hardening-y-cambios-seguros.md) · [Continuidad](07-criptografia-copias-y-continuidad.md)

## 8.1 De la alerta a una decisión fundada

Una alerta indica una condición que merece investigación; no establece por sí sola que exista una intrusión. Puede originarse en un error de configuración, una operación autorizada o un uso no autorizado. Empieza por identificar activo, fuente, instante, regla y comportamiento observado. Preserva el mensaje original y separa hechos, inferencias y preguntas pendientes.

El tratamiento de un incidente necesita coordinar operaciones técnicas y decisiones. El administrador puede observar conexiones y aplicar una contención autorizada; el propietario del servicio decide sobre ciertas consecuencias operativas; el responsable del tratamiento y las funciones competentes evalúan obligaciones de privacidad. En un aula, esos papeles se simulan explícitamente. No se notificará un incidente ficticio a organismos o personas reales.

Define un canal alternativo de coordinación. Si el correo o la identidad corporativa están afectados, depender exclusivamente de ellos puede impedir la respuesta. La lista de contactos y autorizaciones debe estar disponible por un mecanismo protegido que no dependa únicamente del sistema averiado. El registro de acciones incluye responsable, momento, alcance, motivo y resultado.

## 8.2 Cronología y calidad de la evidencia

Una línea temporal combina eventos de varios sistemas con zonas horarias, retrasos y relojes que pueden diferir. Mantén la marca original, la zona indicada y una columna normalizada a UTC cuando se pueda justificar. Si no conoces el desfase, registra incertidumbre; no cambies el reloj de una evidencia para hacer que encaje en la hipótesis.

La siguiente tabla es **totalmente sintética**, preparada para un ejercicio. No corresponde a una captura real ni prueba un ataque:

| Hora UTC del caso | Fuente ficticia | Hecho descrito | Lo que no demuestra por sí solo |
| --- | --- | --- | --- |
| 09:10 | Servicio SSH LAB | Tres autenticaciones fallidas de una cuenta de prácticas | No identifica intención ni éxito posterior |
| 09:12 | Servicio SSH LAB | Sesión abierta para otra cuenta sintética | No prueba que sea la misma persona |
| 09:16 | Registro de cambios | Se modifica una configuración web | Falta autorización y motivo para evaluarlo |
| 09:18 | Monitor HTTP | La portada devuelve 503 | No distingue aplicación, mantenimiento o fallo del monitor |
| 09:24 | Tutor del caso | Confirma que no había cambio planificado | Aporta contexto, no determina por sí solo el alcance |

La investigación relaciona usuario, proceso, conexión y cambio con evidencia adicional. Que dos sucesos estén próximos no establece causalidad. Un intento fallido antes de una sesión válida puede ser una persona que escribió mal una contraseña, dos actividades independientes o parte de otro escenario. Evita redactar «el atacante entró» antes de confirmar qué identidad y mecanismo intervinieron.

En Debian, una consulta acotada puede producir evidencia legible:

```bash
sudo journalctl --utc -u ssh --since '2026-11-08 09:00:00 UTC' \
  --until '2026-11-08 09:30:00 UTC' --no-pager -o short-iso-precise
```

Ajusta fecha y servicio al laboratorio real. La disponibilidad depende de retención, unidad y configuración de registros. Un resultado vacío no demuestra que no ocurrió nada: puede haberse consultado una unidad, ventana o almacén equivocado. En Windows, revisa Visor de eventos y directiva de auditoría aplicable; no todos los eventos están habilitados de la misma forma y una colección de IDs sin contexto puede inducir a error.

## 8.3 Contener conservando capacidad de investigar

La contención limita daño y debe guardar relación con el alcance. En una VM de laboratorio puede aislarse la interfaz virtual, restringirse un recurso o detenerse una aplicación concreta desde consola. Cada acción cambia el estado y puede eliminar información volátil; registra qué se hizo y por qué. No borres archivos sospechosos ni reinstales inmediatamente si necesitas entender su origen y efecto.

La prioridad depende del incidente. Si hay una actividad que amenaza integridad o seguridad de personas, se siguen los protocolos y responsables pertinentes. En esta práctica sólo se utilizan cambios de configuración y datos sintéticos, por lo que se puede estudiar la secuencia sin malware ni acciones ofensivas. El aislamiento no debe afectar al anfitrión ni a equipos del centro que no forman parte del caso.

Distingue credencial comprometida de sistema comprometido. Cambiar una contraseña puede no retirar sesiones, tokens o claves independientes; reconstruir un servidor puede dejar intacta una credencial expuesta en otro lugar. El plan debe identificar mecanismos de acceso y realizar su revocación por los procedimientos apropiados. No se publican claves o contraseñas como evidencia de haber encontrado el problema.

## 8.4 Recuperar y aprender

Antes de devolver el servicio, establece qué estado consideras confiable. Puede requerir restaurar configuración conocida, revisar identidades y permisos, actualizar un componente y recuperar datos desde un punto anterior. Una copia reciente no es necesariamente correcta si ya incluye el cambio dañino. El criterio de selección debe documentarse junto al coste de perder cambios posteriores.

La aceptación incluye funcionamiento desde cliente, acceso permitido/denegado, integridad de datos, registro y seguimiento. Un proceso arrancado no basta. Mantén una fase de observación con métricas relacionadas con el incidente, sin convertirla en vigilancia indiscriminada de usuarios. Define cuándo se cierra y qué evidencia falta, en lugar de afirmar seguridad absoluta.

La revisión posterior identifica causa confirmada, condiciones que permitieron el efecto y mejoras. Si la causa fue un cambio sin validación, añadir capacidad de disco no la trata. Si la demora se debió a no localizar una clave, la mejora debe abordar custodia y procedimiento. Las recomendaciones tienen responsable, plazo y una prueba que demuestre su aplicación.

## 8.5 Datos personales, brechas y ENS

Un incidente puede afectar a disponibilidad, integridad o confidencialidad de datos personales; no se limita a que alguien publique una base. La evaluación debe considerar datos, personas, alcance, consecuencias y medidas. El técnico recoge información y la traslada a las funciones competentes. No decide automáticamente «notificar todo» o «no notificar porque no se vio salida de datos» sin el análisis correspondiente.

La AEPD explica la obligación de notificación del responsable a la autoridad cuando procede y el marco temporal de 72 horas desde que se tiene constancia, con las condiciones del RGPD. La comunicación a personas afectadas tiene su propio umbral y debe realizarse sin dilación indebida cuando corresponda. Son decisiones diferentes y no debe presentarse la segunda como un simple plazo idéntico. Documenta el incidente y consulta el procedimiento de la organización y fuentes oficiales.

Para el caso de aula usa datos inventados y una simulación de informe, sin enviar comunicaciones reales. La minimización también se aplica a la memoria: una captura completa puede contener nombres, direcciones, tokens o datos de otros usuarios. Describe hechos con identificadores sintéticos y conserva evidencia sensible sólo en el espacio autorizado del ejercicio.

El ENS establece un marco para los sistemas comprendidos en su ámbito. Su aplicación requiere determinar responsabilidades, categoría y medidas según el contexto. Instalar un firewall o realizar estas prácticas no equivale a obtener conformidad ni certificación ENS. El estudio debe relacionar principios de gestión, prevención, detección, respuesta y mejora con evidencias, utilizando la norma publicada y su desarrollo aplicable.

## 8.6 Laboratorio de incidente reversible

### Preparación y desarrollo

El tutor o estudiante prepara una copia de la configuración de un sitio web LAB y un marcador de contenido sintético. El caso simula un cambio no autorizado de portada o una configuración que devuelve error. No se cambia software del anfitrión y no se utiliza malware. Un segundo archivo conserva el estado válido y está fuera del árbol servido.

1. Define roles de técnico, propietario del servicio y responsable del caso.
2. Escribe el alcance autorizado, estado conocido y canal de coordinación.
3. Introduce un único cambio reversible en el clon y anota su momento en un sobre o registro separado para contrastarlo al finalizar.
4. Detecta el síntoma mediante una petición de cliente y conserva respuesta y logs mínimos.
5. Construye una cronología con hechos e hipótesis separadas.
6. Propón contención proporcional y explica qué evidencia puede alterar.
7. Recupera desde la configuración válida, valida sintaxis y prueba la aplicación.
8. Comprueba permiso de edición, lectura anónima si se permite y acceso administrativo.
9. Redacta informe de cierre y dos mejoras relacionadas con la causa.

### Aceptación

La práctica se acepta si el servicio vuelve a cumplir su contrato y la explicación distingue lo observado de lo supuesto. No se exige atribuir una persona real ni simular una investigación penal. La copia de configuración permite retorno y los datos sintéticos eliminan la necesidad de publicar información de terceros.

**Entregables:** alcance, cronología, decisiones, evidencia sanitizada, recuperación y revisión. **Rúbrica propia:** investigación 25 %, contención justificada 20 %, recuperación funcional 30 % y comunicación/aprendizaje 25 %.

## Quince problemas con solución razonada

### 1. Tres fallos de contraseña

¿Prueban un ataque? No: muestran fallos de autenticación bajo unas condiciones. Investiga identidad, origen autorizado, frecuencia y contexto. Una persona puede cometer errores y un atacante puede usar una credencial correcta sin generar fallos. El número aislado no permite atribución.

### 2. Puerto abierto

Una prueba TCP a 443 funciona, pero el navegador muestra error de certificado. ¿Se descarta un problema de seguridad? El transporte funciona hasta cierto punto; faltan identidad, confianza, fechas y nombre de TLS. Cambiar firewall no resuelve una CA no confiada. Verifica el certificado presentado y el almacén del cliente.

### 3. Hash correcto

El archivo y su listado SHA-256 coinciden, pero ambos estaban en una carpeta editable por la misma cuenta. ¿Se demuestra autenticidad? Sólo se demuestra coincidencia con esa referencia actual. Si ambos pueden cambiar, se necesita una referencia protegida o mecanismo de autenticación apropiado. Integridad comparada y origen autorizado son cuestiones distintas.

### 4. Disco cifrado y sesión abierta

¿El cifrado impide que una aplicación con permisos borre documentos? No necesariamente. Cuando la sesión tiene acceso a los datos, la autorización y el comportamiento de las aplicaciones siguen siendo determinantes. La protección frente a pérdida del dispositivo apagado no sustituye copias ni mínimo privilegio.

### 5. Dos carpetas de backup

¿Dos carpetas del mismo disco satisfacen independencia frente a avería de ese disco? No. Comparten la causa física de pérdida. Pueden servir para versionado de laboratorio, pero el análisis debe declarar esa limitación y preparar otra copia en un destino separado.

### 6. RPO y tarea programada

Una copia diaria estaba prevista a medianoche, pero la tarea lleva tres días fallando. ¿Cuál es el punto de recuperación? El último punto correcto y utilizable, no el calendario previsto. Revisa catálogo, integridad y restauración. La supervisión debe detectar el fallo antes del incidente.

### 7. RTO parcial

Restaurar datos tarda 20 minutos y comprobar la aplicación otros 25. ¿El RTO observado es 20? No: el tiempo de recuperación de la función incluye las fases pertinentes hasta su aceptación. Si además hubo preparación e identificación, deben sumarse según el alcance del objetivo.

### 8. Credencial cambiada

Se cambia la contraseña tras un incidente y una sesión antigua continúa. ¿Se prueba que el cambio no funcionó? No necesariamente: una sesión o token existente puede mantenerse. Deben revisarse los mecanismos de revocación del servicio y las claves o accesos alternativos, sin concluir a partir de una única conexión.

### 9. Registros vacíos

`journalctl -u ssh` no muestra un evento esperado. ¿Se puede cerrar el caso? No sin comprobar ventana, zona, unidad, retención y configuración. La ausencia de evidencia en una consulta no demuestra ausencia universal de actividad. Registra la limitación.

### 10. Alerta tras una actualización

Un cambio legítimo coincide con un 503. ¿Se clasifica automáticamente como ataque? No. Relaciona versión, logs, validación y plan de cambio. La actualización puede contener un error operativo, y la respuesta necesita recuperar función e identificar causa sin inventar un adversario.

### 11. Control preventivo único

¿Una política de contraseñas elimina la necesidad de backup? No. No trata averías, errores de datos, borrados autorizados ni todas las formas de compromiso. Las medidas se seleccionan por escenarios y dependencias, no como sustitutos universales.

### 12. Cifrado y notificación

Se pierde un dispositivo cifrado. ¿Se notifica siempre o nunca? Ninguna respuesta automática es correcta. Se valoran robustez, claves, acceso, datos y riesgo para personas conforme al procedimiento y normativa. El técnico aporta hechos para la decisión competente.

### 13. Correo a personas afectadas

¿La comunicación de una brecha a interesados es exactamente la misma obligación que notificar a la autoridad? No. Tienen condiciones y finalidades distintas. Consulta fuentes AEPD y registra la evaluación; no uses una plantilla de aula como decisión jurídica definitiva.

### 14. Escáner y cumplimiento

Una herramienta muestra cero hallazgos. ¿El sistema cumple ENS? No. Una herramienta examina un alcance y reglas determinados. El marco exige gestión y evidencias adicionales según el sistema. Cero alertas tampoco demuestra ausencia de vulnerabilidades desconocidas o mal configuradas fuera del alcance.

### 15. Vuelta al servicio

La web vuelve a responder 200 después de restaurar. ¿Se cierra el incidente? Falta comprobar contenido, permisos, identidad, dependencias y seguimiento relacionado con la causa. Un código 200 puede corresponder a contenido incorrecto. El cierre debe basarse en el contrato funcional y las decisiones documentadas.

## Referencias primarias

- [AEPD: notificación de brechas a la autoridad](https://www.aepd.es/derechos-y-deberes/cumple-tus-deberes/medidas-de-cumplimiento/brechas-de-datos-personales-notificacion).
- [AEPD: comunicación de brechas a interesados](https://www.aepd.es/derechos-y-deberes/cumple-tus-deberes/medidas-de-cumplimiento/comunicacion-de-brechas-de-datos).
- [BOE: Reglamento General de Protección de Datos](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807).
- [BOE: Real Decreto 311/2022, ENS](https://www.boe.es/eli/es/rd/2022/05/03/311/con).
- [systemd: journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html).
- [INCIBE: respuesta a incidentes para empresas](https://www.incibe.es/empresas).
