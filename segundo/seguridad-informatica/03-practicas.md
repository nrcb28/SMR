# 3. Prácticas de seguridad informática

Utiliza únicamente equipos del laboratorio. Cada práctica requiere evidencias propias, un caso negativo y un estado final documentado. Los resultados que se indican son expectativas que debes comprobar; no se presentan como pruebas ya realizadas.

## P1. Riesgos y endurecimiento de acceso SSH

**Objetivo:** relacionar un riesgo de administración con un control verificable. **Duración:** dos sesiones de 90 minutos. **Recursos:** VM Debian 13 nueva o instantánea dedicada, cliente autorizado y consola del hipervisor.

### Procedimiento

1. Define el activo «administración de srv01» y el escenario «uso de una credencial robada». Anota impacto y probabilidad con una escala propia y justifica cada valor. Incluye la pérdida de acceso por un error de configuración como riesgo del cambio.
2. Registra línea base: versión, interfaces, escucha y autenticación inicial. No recojas secretos. Comprueba la consola y la copia de configuración antes de tocar SSH.
3. Crea `adminlab` con privilegios definidos. Genera la clave en el cliente y compara la huella del host desde la consola. Copia sólo la clave pública al servidor con propietario y permisos correctos.
4. Abre una sesión nueva con clave y comprueba `sudo -v`. Mantén la consola disponible. Verifica que no dependes de una sesión antigua antes de deshabilitar contraseñas.
5. Añade las directivas de la guía en un archivo dedicado, valida con `sshd -t`, inspecciona la configuración efectiva con `sshd -T -C` y recarga el servicio.
6. Abre otra conexión nueva con clave. Prueba una conexión forzando autenticación por contraseña, sin reiteración masiva: debe rechazarse. Usa también una cuenta distinta no incluida en `AllowUsers`, si existe una cuenta de prueba segura.
7. Revisa los registros del intervalo. Explica qué eventos permiten afirmar autenticación correcta y qué no prueban. Actualiza el riesgo residual incluyendo robo del cliente, pérdida de clave y abuso de una sesión ya abierta.

### Aceptación y reversión

Debe funcionar una nueva sesión autorizada y debe rechazarse el método deshabilitado. La configuración debe superar el validador y el informe debe mostrar valores efectivos. Para revertir, retira el archivo de práctica o restaura la copia correspondiente desde consola, valida y recarga. No cierres todos los accesos antes de comprobar la reversión.

**Entrega:** matriz de riesgo antes/después, diagrama de autenticación, configuración sin claves privadas, dos pruebas positivas/negativas y explicación de una limitación que el control no resuelve. No se valora como finalizado si sólo funciona la sesión que ya estaba abierta.

## P2. Política de firewall y matriz de flujos

**Objetivo:** demostrar que la política permite el servicio previsto y bloquea una conexión nueva a un servicio de prueba. **Duración:** dos sesiones de 90 minutos. **Recursos:** VM específica del ejercicio, cliente LAB y consola. No ejecutes esta política encima del servidor de DNS, Samba o AD de otras prácticas.

### Diseño y ejecución

1. Escribe la matriz: origen LAB, destino srv01, SSH TCP 22 y HTTPS TCP 443; ICMP para diagnóstico y control; respuestas de conexiones iniciadas desde el servidor. Justifica la salida abierta como simplificación del aula.
2. Inventaría reglas y gestores. Si hay UFW, firewalld, Docker o reglas cuyo propósito desconoces, vuelve a una VM limpia o aclara el diseño antes de continuar. Guarda el estado actual, pero no supongas que una exportación reemplaza una política coherente.
3. Comprueba la escucha de SSH. Para HTTPS utiliza el servidor de la asignatura Servicios en red, si está disponible en esta VM de ejercicio; de lo contrario declara esa prueba pendiente en vez de fingir un resultado.
4. Prepara un directorio vacío con un archivo ficticio y ejecuta temporalmente un servidor de prueba en TCP 8080, enlazado sólo a la IP LAB. Si Python 3 está instalado, puede utilizarse `python3 -m http.server 8080 --bind 192.168.56.10 --directory /ruta/al/directorio-vacio`. Nunca apuntes al home ni a carpetas con secretos.
5. Antes del firewall, verifica desde el cliente que 8080 responde. Esto demuestra que existe un servicio detrás del puerto que después se bloqueará.
6. Revisa nombres de interfaces en `smr_guard.nft`, valida con `nft -c -f` y aplica la tabla de la guía desde consola. No ejecutes `flush ruleset`.
7. Desde LAB abre una conexión nueva de SSH: debe funcionar. Intenta una nueva conexión a 8080: debe quedar bloqueada por esta política. Revisa contadores. Verifica que el servidor 8080 sigue escuchando para descartar que la causa sea su cierre.
8. Si tienes una segunda red de laboratorio autorizada, prueba que SSH no es permitido desde ella; no uses un equipo ajeno o Internet como origen. Si no existe, documenta el límite de la comprobación.
9. Detén el servidor 8080 con `Ctrl+C` en su consola y retira el archivo ficticio cuando deje de necesitarse. Revierte la tabla con `nft delete table inet smr_guard` o conserva la política si ése es el estado final acordado.

### Aceptación

Entrega reglas, matriz y tabla de intentos con origen, destino, puerto, escucha previa y resultado. Debe diferenciarse filtrado, rechazo de aplicación, ausencia de servicio y fallo de resolución. Si una conexión anterior sigue abierta por seguimiento de estado, explícalo y repite con una nueva; no alteres conclusiones para que coincidan con el primer intento.

## P3. Copia restaurable y objetivos de recuperación

**Objetivo:** medir qué datos se recuperan y cuánto tarda la recuperación. **Duración:** dos sesiones de 90 minutos. **Recursos:** directorio con datos ficticios, destino independiente realmente montado, `restic` y un gestor de contraseñas para el secreto del repositorio.

### Preparación

Elige RPO de dos horas y RTO de treinta minutos como objetivos educativos. No son garantías del producto. Prepara `/srv/datos-lab` y `/srv/restauracion-lab` como directorios nuevos, con propiedad de la cuenta de práctica. Un administrador puede crearlos con `install -d -o USUARIO -g GRUPO -m 0750 RUTA`, sustituyendo usuario, grupo y ruta después de verificarlos. No cambies la propiedad de todo `/srv`.

Crea tres archivos de texto ficticio y un subdirectorio. Guarda sus hashes y permisos. Confirma `findmnt /mnt/backup`, dispositivo, espacio y permiso de escritura; si no aparece el montaje esperado, detente para evitar guardar en el disco original.

### Ejecución y simulación

1. Inicializa el repositorio y custodia la contraseña. Realiza una primera copia con hora de finalización y revisión de salida.
2. Cambia un archivo y añade otro. Realiza una segunda copia. Identifica ambos snapshots y explica cuál recupera cada versión.
3. Ejecuta el comprobador del repositorio con lectura de datos para el pequeño conjunto del aula. Registra el resultado sin confundirlo con una prueba de servicio.
4. Simula la indisponibilidad del origen renombrando sólo el directorio ficticio después de asegurarte de que no hay procesos usándolo. No ejecutes borrados recursivos para representar el incidente.
5. Inicia el cronómetro y restaura el snapshot elegido en `/srv/restauracion-lab`. Comprueba la estructura de ruta recuperada, contenido, hashes, propietarios y permisos pertinentes. Si el soporte no conserva un metadato requerido, registra el fallo y corrige el diseño.
6. Calcula el punto temporal de los datos recuperados y el tiempo hasta que un usuario puede leerlos correctamente. Compáralos con los objetivos. Incluye validación y preparación, no sólo la transferencia.
7. Recupera el nombre del directorio original si ése es el estado final previsto. Conserva la restauración hasta que se revise la entrega y aplica después la retención acordada. No ejecutes `forget` o `prune` como parte de la primera comprobación.

### Entrega

Presenta línea temporal de cambios/copias/incidente/restauración, identidad de snapshots, evidencia de contenido y metadatos y cálculo de RPO/RTO. Añade una explicación de qué ocurriría si el mismo usuario pudiera borrar el origen y el repositorio. Concluye qué pasos faltan para una copia de aplicación completa o un directorio AD: consistencia, configuración, identidades y procedimiento específico.

## P4. Incidente simulado y decisión de comunicación

**Objetivo:** organizar hechos, hipótesis, evidencias y decisiones sin ejecutar malware ni enviar comunicaciones reales. **Duración:** una sesión de 90 minutos y elaboración de informe. **Escenario:** el servicio de archivos ficticio muestra numerosos rechazos de acceso y un archivo ha cambiado de nombre sin que el responsable de la práctica lo esperase.

### Desarrollo

1. La persona que coordina el ejercicio entrega una cronología ficticia: hora de detección, cuenta, equipo y nombre del archivo. El alumnado marca claramente los datos entregados y los observados. No se atribuye una intrusión sólo por un cambio de nombre.
2. Clasifica información conocida y pendiente: ¿hubo acceso no autorizado?, ¿se alteró contenido?, ¿existe copia?, ¿son datos personales?, ¿qué servicios están afectados? Define pruebas mínimas para reducir incertidumbre.
3. Registra la hora y recoge únicamente registros del intervalo y el archivo ficticio. Copia evidencias de trabajo, calcula hashes y anota origen, responsable y movimientos. No modifiques el original si no es necesario para contener.
4. Propón contención proporcionada: aislar la VM LAB, deshabilitar una cuenta de prueba o retirar temporalmente un recurso. Explica el efecto sobre disponibilidad y qué evidencia podría perderse. Aplica sólo la acción autorizada por el ejercicio.
5. Formula al menos dos hipótesis compatibles con los datos, por ejemplo credencial mal utilizada y cambio legítimo no documentado. Indica qué observación distinguiría ambos casos. Los registros incompletos son una limitación, no prueba de ausencia de incidente.
6. Selecciona un estado de recuperación, verifica copia y define observación posterior. Comprueba que restaurar un archivo no resuelve por sí solo una credencial comprometida o un permiso excesivo.
7. Redacta una nota interna simulada de cinco a diez líneas con hechos, impacto, medidas y dudas. Si pudiera tratarse de una brecha de datos personales, escala al responsable y DPD según el procedimiento del supuesto. Usa las orientaciones de AEPD para razonar la evaluación; no se envía ninguna notificación real.

### Aceptación y entrega

Entrega cronología, registro de evidencias, hipótesis/pruebas, decisión de contención, plan de recuperación y nota simulada. Debe distinguirse información confirmada de inferencias y responsables técnicos de quienes toman decisiones legales. Incluye una mejora preventiva y una mejora de detección justificadas por el caso.

## Plantilla breve del registro de cambio

```text
Servicio y VM:
Riesgo que se quiere reducir:
Estado previo y acceso de recuperación:
Acción prevista y ventana:
Prueba positiva:
Prueba negativa:
Resultado observado:
Reversión y condición que la activa:
Estado final y responsable de la revisión:
```

El registro debe permitir reconstruir la decisión. No incluyas contraseñas, claves privadas, códigos de recuperación ni datos personales reales.
