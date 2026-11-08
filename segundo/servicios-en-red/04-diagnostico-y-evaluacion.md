# Diagnóstico y autoevaluación de servicios

## 1. Árbol de decisión práctico

Empieza por una transacción concreta: nombre consultado, IP de origen, destino, puerto, hora y error. Un navegador puede resumir varios fallos diferentes con mensajes parecidos.

1. **¿El proceso existe y está sano?** Revisa unidad, reinicios y logs. Si no arranca, valida sintaxis y permisos antes de investigar el router.
2. **¿Escucha donde debe?** `ss -lntup` distingue loopback, LAB, todas las interfaces y puertos ocupados por otro programa.
3. **¿El cliente puede llegar a ese transporte?** Comprueba rutas, retorno y firewall; para UDP la ausencia de respuesta requiere interpretación cuidadosa.
4. **¿El protocolo devuelve una respuesta válida?** Lee códigos y campos, no sólo «conectó».
5. **¿La identidad y autorización son correctas?** Contrasta certificado, huella, usuario y permisos.
6. **¿El usuario consigue su operación?** Una consulta DNS válida no demuestra que el fichero solicitado por HTTPS exista.

Guarda eventos con fecha y zona horaria. Si correlacionas un error de cliente a las 10:15 con un log del servidor a las 09:15, comprueba el reloj antes de concluir que no existe registro.

## 2. Tabla de síntomas y pruebas

| Síntoma | Causas posibles | Próxima comprobación |
| --- | --- | --- |
| BIND no inicia | Sintaxis, zona inválida, IP ausente o puerto ocupado | `named-checkconf -z` y logs |
| DNS responde SERVFAIL | Carga de zona o resolución fallida según rol | Logs y tipo de servidor configurado |
| Nombre devuelve NXDOMAIN tras crearlo | Caché negativa o consulta a otro servidor | Consulta explícita y serial SOA |
| DNS funciona por UDP pero no por TCP | Firewall o escucha incompleta | `dig +tcp` y socket TCP/53 |
| Cliente no obtiene DHCP | Red equivocada, segundo DHCP, servicio o firewall | Captura en LAB y logs Kea |
| Kea valida pero no inicia | Socket, permisos o recurso no comprobado por `-t` | Journal y estado de interfaz |
| Reserva no coincide | MAC/identificador distinto o política de reservas | Mensajes del cliente y versión Kea |
| SSH rechaza clave | Cuenta, permisos, clave pública o política | Logs y valores efectivos de sshd |
| Advertencia de host SSH | Reinstalación, cambio de IP o suplantación | Huella desde consola independiente |
| HTTPS falla por nombre | SAN no coincide con URL | Inspección de certificado y SNI |
| HTTPS falla por confianza | Certificado desconocido o cadena incompleta | Certificado público y almacén usado |
| Nginx devuelve 404 | Ruta o sitio virtual equivocado | Host, root, ubicación y access log |
| Nginx devuelve 403 | Permisos o política del sitio | Error log y permisos del camino |
| Mail queda en cola | Destino, transporte, permisos o política | Cola y logs, sin abrir relay |

## 3. Casos resueltos

### Un registro existe pero el cliente sigue sin verlo

Primero consulta directamente BIND. Si devuelve el registro con el serial actualizado, el servidor posee el cambio. Consulta después el DNS que realmente utiliza el cliente y compara respuestas y TTL. Revisa caché negativa, sufijos de búsqueda y si la aplicación usa otro resolver.

Vaciar todas las cachés y reiniciar todos los servicios oculta el origen. La corrección depende de la causa: cambiar el servidor configurado, esperar el TTL razonable, retirar una entrada hosts o corregir el nombre absoluto.

### DHCP ofrece una IP válida y aun así falla Internet

Revisa si el cliente recibió una puerta de enlace en LAB que no existe o si cambió la preferencia de rutas. En el diseño base, Internet sale por NAT y LAB no anuncia router. Si DNS autoritativo local está configurado como único resolver general, los nombres externos pueden fallar porque BIND tiene recursión deshabilitada.

No habilites recursión para cualquiera como solución rápida. Decide cómo se resolverán las zonas locales y los nombres externos en el cliente o diseña un resolver limitado a la red apropiada. Documenta esa ampliación como cambio arquitectónico.

### SSH autentica pero no permite escribir un archivo

El transporte cifrado y la autenticación pueden estar funcionando. Consulta propietario, grupo y permisos de todos los directorios del camino. Identifica si la cuenta debe escribir allí. Dar `chmod 777` resuelve a veces el síntoma a costa de permitir escritura indebida.

Una solución adecuada crea un directorio de trabajo del usuario o asigna un grupo y permisos deliberados. Comprueba también restricciones del subsistema SFTP y confinamiento cuando formen parte del diseño.

### Una web funciona con curl inseguro

`curl -k` omite verificaciones TLS. Que devuelva contenido demuestra una parte del transporte y la aplicación, pero no que el cliente pueda autenticar al servidor. Repite con nombre correcto y material de confianza explícito. Si falla, interpreta el error exacto: nombre, validez, cadena o confianza.

En producción se utiliza una PKI y un ciclo de renovación adecuados. En este laboratorio la aceptación correcta utiliza `--cacert` y un nombre SAN coincidente, sin añadir una excepción global a todos los sitios.

## 4. Preguntas con respuesta razonada

**1. ¿Por qué DNS necesita UDP y TCP?**\
UDP se utiliza en muchas consultas, pero TCP forma parte del funcionamiento normal, incluyendo respuestas que no caben o se recuperan por otros motivos y operaciones como transferencias de zona. Permitir sólo UDP es una configuración incompleta.

**2. ¿Un CNAME es una redirección HTTP?**\
No. Es información DNS que apunta a otro nombre. El navegador conserva su URL y el nombre HTTP/TLS correspondiente. Una redirección HTTP es una respuesta de la aplicación con un destino.

**3. ¿Cambiar el SOA crea una réplica automáticamente?**\
No. El serial ayuda a coordinar versiones, pero secundarios y transferencias requieren configuración y autorización. No debes permitir transferencias a cualquiera para que una consulta común funcione.

**4. ¿Puede el cliente conservar una IP tras detener DHCP?**\
Sí, puede mantener una concesión válida durante un tiempo. Para demostrar disponibilidad del servicio observa adquisición o renovación, logs y estado de concesiones.

**5. ¿Por qué no hay opción routers en el ejemplo?**\
Porque LAB no tiene un router. Ofrecer `192.168.56.1` sin comprobar su función puede crear una ruta que no sirve. La NIC NAT es una red distinta.

**6. ¿El hostname de una reserva Kea crea un A en BIND?**\
No automáticamente en este diseño. DDNS requiere componentes y permisos explícitos. Una etiqueta en DHCP no sustituye la actualización del DNS.

**7. ¿SFTP necesita abrir puertos FTP pasivos?**\
No. Utiliza el transporte SSH configurado. FTP/FTPS son protocolos diferentes y tienen un modelo de conexiones distinto.

**8. ¿La clave pública de host puede compartirse?**\
Sí, sirve para identificar al servidor; la privada debe permanecer protegida. No se debe confundir con la clave pública de un usuario autorizada para entrar.

**9. ¿Un certificado para www.aula.test sirve por IP?**\
Sólo si también contiene un SAN IP correspondiente y se valida ese acceso de forma apropiada. El certificado de la guía contiene un SAN DNS, por lo que la URL debe utilizar ese nombre.

**10. ¿Qué demuestra un 404?**\
Que un servidor HTTP respondió con ese estado para la petición considerada. Puede indicar recurso inexistente o selección de sitio/ruta incorrecta; no demuestra que toda la infraestructura DNS/TLS esté bien.

**11. ¿MX permite que cualquiera envíe correo a cualquier destino?**\
No. MX informa de destinos de recepción del dominio. Las políticas de relay y autenticación pertenecen al servidor SMTP y deben restringirse.

**12. ¿Por qué no se guarda una clave TLS privada en Git?**\
Porque otorga capacidad de identidad y debe protegerse. Borrarla en un commit posterior no elimina necesariamente su presencia del historial. Si se expone una clave real, hay que tratar su sustitución y revocación según la PKI y el alcance.

## 5. Ficha mínima de operación

Por cada servicio registra: responsable, paquete y versión, ficheros de configuración, datos persistentes, identidad de ejecución, escucha, firewall, dependencia de nombres y tiempo, validadores, pruebas desde cliente, ubicación de respaldo y recuperación.

Distingue evidencia observada de hipótesis. «El servicio está bien» es demasiado amplio; «la consulta A por TCP y UDP desde cli01 devuelve .10 con autoridad y el nombre inexistente devuelve NXDOMAIN» permite revisar el resultado.

La autoevaluación final consiste en entregar esa ficha a otra persona y comprobar si puede verificar el servicio sin adivinar nombres, interfaces, contraseñas o pasos omitidos.
