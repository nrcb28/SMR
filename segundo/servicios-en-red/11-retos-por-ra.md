# Retos de Servicios en red por resultados de aprendizaje

[Matriz RA/CE](10-alineacion-ra.md) · [Complementos de implantación](12-complementos-curriculares-ra.md) · [Índice](README.md)

## Condiciones de trabajo y significado de la evidencia

El módulo 0227 tiene ocho RA, con sesenta y tres criterios, según el [anexo I del RD 1691/2007](https://www.boe.es/eli/es/rd/2007/12/14/1691). Los retos siguientes conservan ese orden. Las configuraciones y actividades son propuestas de aprendizaje; no se atribuyen a la norma unas ponderaciones, marcas de producto o salidas que no establece.

Prepara VMs, consola, copia y registro de versiones. Cada reto especifica qué añade a las guías anteriores y cómo comprobarlo desde un cliente. Los resultados descritos son expectativas para el estudiante, no pruebas ejecutadas durante la elaboración. Registra como pendiente cualquier operación sin equipo, conexión o autorización suficiente.

La LAB base mantiene `srv01` `.56.10/24`, cliente `.20`, secundaria DNS opcional `.30`, reserva `.50` y DHCP `.100–150`, sin gateway en esa interfaz. Las topologías de FTP, Wi-Fi-router y pasarela se declaran por separado. No se reutiliza la política de firewall de un ejercicio como si sirviera para todos los servicios. Los casos negativos se limitan a cuentas, datos y redes de formación.

<a id="ra1"></a>
## RA1 · Configuración dinámica con reserva y opciones

**Actividad:** `0227-RA1-A1`. Cubre a–h. Parte del despliegue Kea de la [guía técnica](02-guia-tecnica.md) y construye un expediente de asignación, no una captura aislada de una IP.

### Procedimiento

1. Dibuja solicitud y respuesta de configuración y explica qué parámetros necesita un puesto. Compara configuración manual y dinámica: coherencia, renovación, trazabilidad y dependencia del servicio.
2. Identifica NIC LAB y comprueba que no existe DHCP del hipervisor en ese segmento. Instala/configura Kea sólo en la VM prevista y valida la sintaxis con el procedimiento de la versión instalada antes de iniciarlo.
3. Configura pool y opciones básicas coherentes. La LAB sin router no anuncia una puerta de enlace ficticia. Documenta máscara, DNS y dominio de búsqueda cuando se utilicen.
4. Usa dos clientes temporales con identidades diferentes: uno recibe concesión dinámica y otro la reserva `.50` definida para su identificador. No clones una MAC para obtener una demostración aparente.
5. Añade una opción pertinente al escenario y verifica cómo la interpreta el cliente. Una opción declarada en el servidor pero no aplicada por el cliente requiere explicación, no una marca de éxito automática.
6. Relaciona concesión del cliente, identificador del servidor, registros de Kea y secuencia temporal. Renueva sólo el adaptador de laboratorio y observa qué permanece o cambia.

### Solución, aceptación y recuperación

Una IP dentro del rango no prueba que la haya servido Kea: otro servidor puede usar el mismo rango. La evidencia incluye origen de la concesión, identidad del cliente y opciones efectivas. Una reserva no publica por sí sola registros A/PTR en DNS. Si el cliente obtiene DNS incorrecto, investiga origen y selección de interfaz antes de editar BIND.

Entrega diseño de parámetros, configuración saneada, validación, dos asignaciones y tabla servidor/cliente. Se acepta cuando dirección, prefijo, DNS y alcance coinciden con el diseño y se interpreta el proceso de solicitud/renovación. Como prueba negativa, usa un cliente de laboratorio con identificador diferente y verifica que no recibe por error la reserva del otro. Conserva acceso administrativo por IP fija; al terminar detén el servicio si el siguiente escenario no lo necesita y restaura los clientes temporales.

<a id="ra2"></a>
## RA2 · Autoridad, caché y réplica como funciones distintas

**Actividad:** `0227-RA2-A1`. Cubre a–h. El expediente combina zona propia, un resolver restringido y una transferencia entre participantes. Separa los estados de configuración para evitar confundir un servidor únicamente autoritativo con uno recursivo.

### Procedimiento y colaboración

Define tres necesidades: localizar el servidor interno por nombre, resolver un nombre externo permitido y mantener una segunda autoridad. Compara archivo hosts, resolución jerárquica y caché. Dibuja etiquetas, zona, delegación y tipos A/PTR/MX/CNAME: un alias no es una redirección HTTP ni un NS una copia automática.

Instala y valida BIND con zona nueva y sus registros de servidor, correo y alias. Realiza primero consulta directa a autoridad y después resolución normal desde cliente. Para el criterio de caché, ejecuta la [ampliación recursiva controlada](12-complementos-curriculares-ra.md); conserva ACL y evidencia de una entrada almacenada, no sólo una comparación informal de tiempos.

Reparte funciones entre dos personas: una administra primaria `.10` y otra secundaria `.30`. Cada una conserva configuración, pruebas y revisión del trabajo de la otra. Configura la transferencia con la [guía de réplicas](06-dns-replicacion-y-ciclo-de-cambio.md), aumenta serial, valida y demuestra que ambas responden al cambio. El trabajo individual de un único estudiante puede practicar el mecanismo, pero se registra como individual y no prueba colaboración realizada.

### Aceptación y casos negativos

Entrega mapa de resoluciones, archivos de zona saneados, pruebas de registros, caché autorizada, réplica y contribuciones. La transferencia sin clave se rechaza en condiciones que permitan distinguir firewall y aplicación; la consulta recursiva de un cliente fuera de ACL también se deniega. No publiques TSIG ni contraseñas en las evidencias.

La solución explica por qué un serial igual no demuestra que todos los resolutores externos hayan actualizado su caché. La autoridad publica datos; el resolver conserva respuestas bajo sus temporizadores. Si una prueba falla, consulta los participantes y sus logs antes de copiar archivos manualmente. Al cerrar restaura el escenario elegido y retira la recursión temporal que no deba permanecer activa.

<a id="ra3"></a>
## RA3 · Transferencia FTP completa y comparación de alternativas

**Actividad:** `0227-RA3-A1`. Cubre a–g. Sigue la [implantación FTP aislada](12-complementos-curriculares-ra.md), que añade expresamente lo que SFTP no demuestra: acceso anónimo y canales FTP activo/pasivo.

### Procedimiento

Prepara la VM `ftplab` `.40`, con interfaces externas desconectadas y datos sintéticos. Antes de iniciar el servidor, identifica canales de control/datos y quién inicia cada conexión. Establece grupo y usuario temporales, árbol anónimo y árbol autenticado, permisos del sistema de archivos y límites de escritura/concurrencia.

Realiza cuatro recorridos: anónimo pasivo, anónimo activo, usuario autenticado pasivo y usuario autenticado activo. Usa cliente CLI y gráfico; anota su modo y la configuración relevante. Compara hashes de un archivo descargado y comprueba que cada identidad sólo ve el árbol autorizado. Un inicio de sesión sin transferencia no demuestra funcionamiento del canal de datos.

Intenta una subida sintética con una identidad de lectura. La denegación es una prueba esperada. Observa cómo un puerto de control permitido puede coexistir con un canal de datos bloqueado y explica el ajuste específico de firewall del laboratorio, sin abrir rangos indiscriminados en una red real.

### Solución y entrega

Entrega esquema de conexiones de ambos modos, instalación/configuración saneada, cuentas/grupo sin secretos, permisos, matriz de clientes y hashes. Se acepta cuando las transferencias solicitadas y las denegaciones corresponden a la política y se identifican los dos canales. Una sesión SFTP adicional permite comparar protección y simplicidad de firewall, pero no sustituye las pruebas FTP exigidas por esos criterios.

FTP de esta práctica no es una recomendación de exponer un servicio sin protección. Retira cuentas y servicio después, o restaura la VM efímera, verificando que la escucha no permanece. Los informes no contienen contraseñas ni capturas con credenciales legibles; una captura de protocolo se limita a datos y identidades inventadas.

<a id="ra4"></a>
## RA4 · Mensaje, alias, buzón y recogida remota

**Actividad:** `0227-RA4-A1`. Cubre a–g. Completa el laboratorio de [Postfix local](05-correo-local.md) con Dovecot IMAPS y un cliente remoto de formación, conforme al [complemento RA4](12-complementos-curriculares-ra.md).

### Procedimiento

Dibuja el recorrido de un mensaje y distingue SMTP, entrega al buzón e IMAP. Instala/configura Postfix en el alcance loopback indicado y crea cuentas de prueba. Prepara un mensaje con un identificador único, asunto y cuerpo sintéticos. Crea un alias que entregue a un buzón existente y reconstruye la base de alias mediante el procedimiento del servicio.

Comprueba entrega local y después instala/configura acceso IMAPS compatible con la versión real de Dovecot. Sigue la [preparación de la cuenta IMAPS](12-complementos-curriculares-ra.md#cuenta-imaps): `labmail` tenía contraseña bloqueada; antes de establecer su credencial temporal por consola se excluye esa identidad de SSH conservando el acceso administrativo. Establece identidad y ruta Maildir sin mezclar opciones de Dovecot 2.3 y 2.4. Valida certificado y nombre desde cliente antes de introducir credenciales. Comprueba autenticación IMAPS positiva y rechazo de un usuario de prueba inexistente. Configura el envío por el túnel SSH con otra cuenta administrativa y SMTP local sin autenticación, según la política Postfix del complemento; no reutilices ahí la contraseña IMAPS, no abras relay ni publiques SMTP.

Envía al usuario y a su alias y comprueba ambos mensajes en el cliente. Relaciona identificador de cola, entrega y acceso remoto; una cola vacía puede significar más de una cosa. Comprueba también que otro usuario no recibe acceso al buzón ajeno.

### Uso indebido y aceptación

Prueba un destinatario externo de ejemplo mediante `RCPT TO`, sin aportar DATA ni utilizar direcciones reales. Debe rechazarse por la política del laboratorio. Distingue la aceptación del destinatario local de una promesa de entrega a Internet. Revisa listeners efectivos y métodos de acceso: la protección no se deduce del nombre del paquete instalado.

Entrega diagrama de protocolos, configuración saneada, usuarios/alias, mensaje recibido y prueba de rechazo. Se acepta cuando el cliente envía y recibe el contenido conocido, la autenticación/TLS se comprueban y no existe retransmisión no prevista. Al cerrar retira túnel, conexiones y confianza temporal; conserva sólo mensajes sintéticos necesarios. Si no se ha realizado recogida remota, marca RA4.f/g pendientes, aunque exista un Maildir correcto en el servidor.

<a id="ra5"></a>
## RA5 · Sitios virtuales, ejecución y módulos con TLS

**Actividad:** `0227-RA5-A1`. Cubre a–i. Parte de HTTPS ya preparado, en un clon dedicado que no aloja simultáneamente otros escenarios incompatibles. Utiliza dos nombres de prueba y dos directorios con contenido distinto, ambos limitados a LAB.

### Implantación y pruebas

Configura dos virtual hosts y documenta cómo se seleccionan por IP/puerto y nombre. Solicita ambas URLs desde el mismo cliente y prueba un nombre que no esté previsto. En TLS considera SNI y SAN: una conexión por IP o un `Host` distinto no produce automáticamente un certificado apropiado.

En el primer sitio prepara una página HTML con un botón que cambie texto mediante JavaScript. En el segundo usa un backend configurado, por ejemplo PHP-FPM, que devuelva un JSON sintético de hora del servidor. Compara código enviado al navegador, peticiones y resultado: el PHP se ejecuta en servidor y no debe entregarse como fuente. El JavaScript recibido sí puede inspeccionarse; ocultar una clave en él no protege un secreto.

Instala un módulo de servidor compatible desde el repositorio oficial. Por ejemplo, si la versión candidata de Debian ofrece `libnginx-mod-http-headers-more-filter`, revisa sus dependencias, archivos de carga e instrucciones antes de instalar. En un virtual host de formación una directiva `more_set_headers "X-RA5: modulo-lab";` permite comprobarlo. Confirma módulo y configuración efectiva; una cabecera puesta sólo con la directiva incorporada `add_header` no demuestra haber instalado ese módulo.

Valida sintaxis antes de recargar y prueba las dos páginas, el backend y la cabecera. Aplica permisos mínimos, protege archivos de configuración y comprueba comunicaciones por nombre con CA confiada, sin `-k`. Si el paquete elegido no está disponible o no es compatible, documenta alternativa soportada y prueba; no descargues un binario arbitrario para forzar el requisito.

### Aceptación y retorno

Entrega fundamentos HTTP/TLS, instalación, dos sitios y criterio de selección, política de seguridad, pruebas de clientes, comparación de ejecución y módulo instalado. La prueba negativa detecta nombre no autorizado, archivo inexistente o acceso prohibido según diseño. No equipares un error 404 con ausencia de transporte.

Retira primero las directivas que dependen del módulo si vas a desinstalarlo; después valida y recarga. Restaura sitios/certificados sólo en el clon y conserva la evidencia de que no quedan listeners wildcard fuera de LAB. El mantenimiento y las operaciones de usuario se apoyan en [Aplicaciones web](../aplicaciones-web/README.md), sin confundir el CMS con todos los criterios de este RA.

<a id="ra6"></a>
## RA6 · Línea de comandos, escritorio y sistemas heterogéneos

**Actividad:** `0227-RA6-A1`. Cubre a–g. Establece una sesión SSH de Windows hacia Linux y una sesión gráfica RDP de Linux hacia un Windows Pro de laboratorio, según el [complemento de acceso remoto](12-complementos-curriculares-ra.md).

Documenta propósito, autenticación, identidad del host, alcance de red y tareas autorizadas de cada método. Instala los servicios y clientes necesarios, comprueba edición, versión y puertos efectivos. La cuenta con acceso remoto no debe obtener administración universal por el simple hecho de conectarse.

En cada sesión identifica equipo, usuario y rol y realiza una tarea de consulta o administración prevista. Conserva estado inicial y resultado, y prueba una cuenta no autorizada sin bloquear cuentas reales. Para una modificación que requiera elevación, registra la autorización y el cambio concreto, además del procedimiento de vuelta atrás.

Compara uso de ancho de banda, capacidad de automatización, dependencia de escritorio, auditoría y riesgos de portapapeles/unidades redirigidas. Cierra canales que el ejercicio no necesite. Una captura de una ventana RDP abierta sin identificar destino y cuenta no basta para probar administración heterogénea.

Entrega instalación/configuración saneada, pruebas de ambos métodos y una tabla de ventajas y límites. Se acepta cuando se demuestra acceso y tareas en sistemas de distinta naturaleza, con identidades y denegación correctas. Retira las reglas, cuentas y habilitaciones temporales al cerrar. Si sólo se ha realizado SSH, el acceso gráfico continúa pendiente aunque el cliente posea escritorio local.

<a id="ra7"></a>
## RA7 · AP y encaminador inalámbrico con escenarios comparados

**Actividad:** `0227-RA7-A1`. Cubre a–g. Requiere AP/router configurable y clientes reales o un entorno que implemente las funciones que se pretenden observar. Distingue la práctica de AP de primero del objetivo adicional de un encaminador con servicios LAN y enlace exterior.

### Procedimiento

Instala el AP dentro de una LAN aislada y registra protocolos, modo, canales, ancho, seguridad y capacidades. Compara dos escenarios: AP que enlaza clientes a una LAN existente y router inalámbrico con LAN y WAN diferenciadas. Identifica quién realiza DHCP, NAT y filtrado en cada uno; dos servidores DHCP no coordinados no son redundancia.

Selecciona parámetros frente a requisitos de cobertura y capacidad, apoyándote en [ingeniería Wi-Fi](../../primero/redes-locales/07-ingenieria-wifi-y-capacidad.md). Usa distintos tipos de cliente y posiciones autorizadas. Conserva condiciones y resultados medidos, sin atribuir una captura sintética a una radio real.

En el router configura WAN y LAN con prefijos distintos. Para preparar el mecanismo sin operador, la WAN puede conectarse a la red exterior simulada del siguiente reto. Una conexión real a red pública sólo se realiza con equipos y autorización del centro/operador; no se presenta como ejecutada cuando sólo hay dos redes internas del hipervisor.

Prueba administración del router desde un equipo LAN, acceso previsto hacia exterior y denegación de gestión desde el lado no autorizado. No habilites administración pública ni desactives cifrado para evitar un diagnóstico. Guarda configuración sin claves y restaura el equipo de formación al finalizar.

### Aceptación

Entrega montaje, capacidad/protocolos, dos diseños, decisión de parámetros, seguridad, matriz de cobertura por dispositivo y pruebas del router. Se acepta el mecanismo observado en el alcance declarado; la parte física/radio y la conexión real pendiente se identifican expresamente si no se han realizado. Un router virtual no sustituye la evidencia de clientes inalámbricos reales.

<a id="ra8"></a>
## RA8 · Pasarela, proxy y acceso entrante controlado

**Actividad:** `0227-RA8-A1`. Cubre a–j. Usa la [topología exterior simulada y reglas](12-complementos-curriculares-ra.md), separada de la LAB base. La finalidad es observar rutas, aplicación de pasarela, acceso de clientes, control, caché, reenvío entre interfaces y publicación de un servicio privado.

### Secuencia

1. Instala/configura las dos interfaces de la pasarela y las rutas de clientes y servidores. Dibuja origen/destino antes y después de NAT; no trates routing y traducción como sinónimos.
2. Configura reenvío y controles con una única política conocida. Comprueba desde consola y conserva retorno. Las reglas de ejemplo no justifican sustituir un firewall de producción.
3. Prepara la aplicación proxy, restringida a LAN, y compara funciones con routing/NAT. La aplicación debe comprobarse instalada y efectiva, no sólo mencionarse en una memoria.
4. Prueba acceso desde red privada a web exterior simulada; registra qué regla lo permite. Intenta un acceso que el diseño prohíba y explica el resultado sin enviar tráfico a redes ajenas.
5. Solicita un objeto cacheable mediante proxy, identifica almacenamiento/validación en logs y compara con un objeto no almacenable. No concluyas «hay caché» sólo porque la segunda petición tarda menos.
6. Desde exterior solicita el puerto publicado de la pasarela y verifica contenido de la web privada. Comprueba ruta de retorno y traducción; una prueba desde la propia web no evidencia acceso desde otra red.

### Solución y aceptación

Un cliente de una red necesita una ruta hacia el siguiente salto apropiado, y la respuesta necesita retorno. NAT puede simplificar un escenario, pero no sustituye toda política de acceso. Un proxy explícito requiere que la aplicación cliente lo utilice; no captura automáticamente todas las conexiones por estar instalado en el router.

Entrega topología, aplicaciones/versiones, rutas, reglas, clientes configurados, logs de caché y acceso entrante/denegado. Para afirmar una conexión real con red pública debe existir además evidencia autorizada de ese entorno. La simulación es preparación verificable de mecanismos y se etiqueta como tal. Retira reglas y servicios de la práctica, restaura reenvío y comprueba que no se mantienen rutas o listeners que unan escenarios posteriores.

## Revisión de evidencias y recuperación de aprendizajes

Para cada criterio registra evidencia obtenida, insuficiente o pendiente. Si una captura contiene sólo «servicio activo», identifica qué falta para comprobar el comportamiento desde cliente. Si no hay equipamiento o autorización, conserva diseño y pasos de ejecución previstos sin inventar observaciones.

Para recuperar un criterio concreta la carencia: «falta cliente gráfico FTP en modo activo», «falta prueba de alias», «falta usuario fuera de ACL» o «no hay medición con un segundo adaptador Wi-Fi». La siguiente actividad se diseña para esa carencia, no para repetir todo el módulo indiscriminadamente.

Los instrumentos de autoevaluación son propios. Una revisión docente puede utilizar observación, memoria, preguntas y demostración práctica, con las condiciones que establezca su programación. El [JSON trazable](alineacion-ra.json) permite comprobar la relación de los 63 criterios con los retos y sus evidencias; no certifica adquisición del alumnado.
