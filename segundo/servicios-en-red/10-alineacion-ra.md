# Servicios en red · alineación con resultados de aprendizaje

[Índice del módulo](README.md) · [Retos por RA](11-retos-por-ra.md) · [Datos trazables](alineacion-ra.json)

## Fuente y alcance

La numeración y los enunciados de los 8 RA se toman del [anexo I del RD 1691/2007](https://www.boe.es/eli/es/rd/2007/12/14/1691), módulo 0227. Se conservan sus 63 criterios y letras. Consulta normativa: 09/11/2026. La organización actual del ciclo y sus módulos transversales se explica en el [currículo de Madrid](../../docs/curriculo-madrid.md).

Los enunciados RA que aparecen en las citas son transcripción normativa con espacios normalizados. Los resúmenes CE, actividades, evidencias y condiciones de aceptación de las tablas son elaboración didáctica propia; sirven para preparar y revisar el trabajo, sin modificar la norma ni fijar la calificación del centro.

La cobertura de una fila significa que existe material y un reto para trabajar ese criterio. La adquisición requiere evidencia real y revisión en las condiciones de la programación. Distingue ejecución propia, observación supervisada, simulación y pendiente de equipamiento. Una salida esperada escrita en la guía no es un resultado obtenido por el estudiante.

## Cómo usar la matriz

1. Identifica el RA y lee su enunciado completo; después localiza los materiales de preparación.
2. Realiza el reto enlazado desde un estado inicial conocido y con el equipamiento que necesita.
3. Conserva un artefacto por criterio o un artefacto común con referencias claras a las letras que demuestra.
4. Compara el resultado real con la condición de aceptación y registra qué falta, sin copiar la expectativa como evidencia.
5. Repite sólo la operación pendiente o incorrecta y documenta recuperación, cambios y límites.

Un mismo dossier puede responder a varios criterios, siempre que se señale dónde se observa cada uno. Por ejemplo, una configuración y un registro de cliente se complementan: el primero declara la intención y el segundo muestra una condición del uso. No son intercambiables.

## Carencias curriculares que cierra esta ampliación

El [complemento de implantación](12-complementos-curriculares-ra.md) desarrolla la caché recursiva, FTP anónimo y activo/pasivo, recogida IMAPS, escritorio remoto y pasarela/proxy. Esos comportamientos no se deducen de tener DNS autoritativo, SFTP, correo local o una única web. El reto de servidor web añade dos sitios, ejecución cliente/servidor y un módulo instalado y comprobado.

La operación se divide en escenarios para mantener roles, puertos y alcance coherentes. FTP se limita a una VM efímera sin acceso exterior; SMTP conserva loopback y el acceso remoto al buzón usa TLS. La red exterior simulada prepara mecanismos de pasarela, pero no se describe como una conexión pública de operador ya realizada. La parte inalámbrica mantiene su exigencia de radio y dispositivos observables.

<a id="ra1"></a>
## RA1 · Expediente DHCP: dinámica, reserva y opciones efectivas

> Instala servicios de configuración dinámica, describiendo sus características y aplicaciones.

La evidencia central es la configuración recibida y su origen. Una dirección del rango no prueba que Kea la haya entregado. El reto exige dinámica y reserva, opciones y correlación temporal, con clientes de laboratorio de identidades diferentes. La NIC LAB conserva su diseño sin router; la salida a Internet pertenece a otra NIC. La verificación permite reconocer parámetros no aplicados y evitar que un segundo servidor DHCP produzca una demostración engañosa.

**Actividad desarrollada:** [`0227-RA1-A1`](11-retos-por-ra.md#ra1).

**Preparación:** [02-guia-tecnica.md](02-guia-tecnica.md), [07-dhcp-dual-stack-y-operacion.md](07-dhcp-dual-stack-y-operacion.md), [11-retos-por-ra.md](11-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Reconocer la configuración automatizada de red | Diagrama temporal de solicitud, oferta, selección y concesión | Relaciona mensajes, clientes y servidor sin confundir concesión con DNS. |
| b) | Identificar ventajas de la automatización | Comparativa manual/dinámica para el aula | Justifica coherencia, renovación y gestión, incluyendo dependencia del servicio. |
| c) | Ilustrar el procedimiento de solicitud | Secuencia anotada y registro correlacionado del cliente | Explica quién solicita y responde y qué parámetros se negocian. |
| d) | Instalar el servicio dinámico | Versiones, validación y estado de Kea | Servicio y listener corresponden a la NIC LAB y al diseño aislado. |
| e) | Asignar parámetros básicos de la LAN | Pool y tabla de dirección, prefijo y opciones del cliente | Los parámetros efectivos coinciden y no hay gateway ficticio en LAB. |
| f) | Realizar asignación dinámica y estática | Dos clientes con identidades distintas y reserva .50 | Cada concesión procede del servidor previsto y respeta la reserva. |
| g) | Incorporar opciones adicionales | Opción pertinente configurada y comprobada en el cliente | Explica soporte del cliente y diferencia declaración y aplicación efectiva. |
| h) | Verificar la configuración asignada | Matriz cliente–identificador del servidor–parámetros–tiempo | Detecta valores inesperados y distingue un segundo DHCP o una NIC distinta. |

El reto RA1 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

<a id="ra2"></a>
## RA2 · DNS: autoridad, caché restringida y réplica colaborativa

> Instala servicios de resolución de nombres, describiendo sus características y aplicaciones.

Este RA reúne funciones distintas. El servidor de la guía inicial era autoritativo y por sí solo no evidencia la caché de respuestas externas del criterio e. El complemento añade un resolver restringido y la guía de réplica una segunda autoridad. La actividad también pide colaboración: operar dos VMs a solas practica transferencias, pero no demuestra que se haya trabajado en grupo. Se conservan contribuciones y revisión entre participantes, además de las pruebas de zona.

**Actividad desarrollada:** [`0227-RA2-A1`](11-retos-por-ra.md#ra2).

**Preparación:** [02-guia-tecnica.md](02-guia-tecnica.md), [06-dns-replicacion-y-ciclo-de-cambio.md](06-dns-replicacion-y-ciclo-de-cambio.md), [12-complementos-curriculares-ra.md](12-complementos-curriculares-ra.md), [11-retos-por-ra.md](11-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Identificar necesidades de resolución | Tres casos: nombre interno, nombre externo permitido y segunda autoridad | Distingue necesidad y función de servidor antes de configurar. |
| b) | Clasificar mecanismos de resolución | Tabla de hosts, DNS autoritativo y resolver/caché | Explica qué mecanismo responde en cada prueba normal o dirigida. |
| c) | Describir jerarquía y nomenclatura | Esquema de etiquetas, zonas, delegación y registros | No confunde alias, redirección HTTP, delegación y réplica. |
| d) | Instalar el servicio jerárquico | Configuración BIND validada y consulta a zona propia | Responde la instancia prevista y se conoce su función autoritativa. |
| e) | Almacenar y servir respuestas externas | Entrada de caché de una consulta permitida y ACL de recursión | Prueba almacenamiento real y rechazo fuera del alcance, no sólo menor latencia. |
| f) | Añadir zona, correo y alias | Archivos de zona y consultas A/PTR/MX/CNAME | Los destinos y nombres son válidos y las respuestas corresponden a la zona. |
| g) | Realizar transferencias en grupo | Primaria .10, secundaria .30 y registro de contribuciones | Ambas responden al serial nuevo y se acredita colaboración; un trabajo individual se declara así. |
| h) | Comprobar funcionamiento del servidor | Consultas positivas/negativas de autoridad, recursión y réplica | Interpreta estados, TTL y participantes, sin publicar TSIG ni consultas ajenas. |

El reto RA2 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

<a id="ra3"></a>
## RA3 · FTP aislado: identidades, límites y dos modos de datos

> Instala servicios de transferencia de ficheros, describiendo sus características y aplicaciones.

El material añade deliberadamente FTP porque los criterios citan acceso anónimo y modos activo/pasivo. Una transferencia SFTP es otra tecnología y no acredita esas operaciones. El complemento limita FTP sin protección a una VM efímera, sin NAT ni puente y con datos inventados. La solución identifica canales y permisos, registra transferencias verdaderas y destruye o detiene el escenario al terminar; nunca presenta ese diseño como una publicación recomendada para una red de trabajo.

**Actividad desarrollada:** [`0227-RA3-A1`](11-retos-por-ra.md#ra3).

**Preparación:** [01-fundamentos.md](01-fundamentos.md), [12-complementos-curriculares-ra.md](12-complementos-curriculares-ra.md), [11-retos-por-ra.md](11-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Explicar utilidad y operación de FTP | Diagrama de control y datos, activo y pasivo | Identifica iniciador y destino de cada conexión y compara con SFTP sin equipararlos. |
| b) | Instalar un servicio de transferencia | Configuración y listener de vsftpd en ftplab .40 | La VM dedicada carece de conexión externa al ejecutar el ejercicio. |
| c) | Crear usuarios y grupos remotos | Inventario saneado de cuenta temporal, grupo y permisos | La identidad autenticada sólo accede al árbol autorizado del laboratorio. |
| d) | Configurar acceso anónimo | Descarga del archivo público y comparación de árbol visible | El anónimo obtiene únicamente lectura del árbol público previsto. |
| e) | Establecer límites de acceso | Política de escritura y concurrencia con prueba negativa | La subida de lectura se deniega y los límites corresponden a cada modo. |
| f) | Comprobar FTP activo y pasivo | Matriz de transferencias y canales con hashes | Los datos se transfieren en ambos modos y se explica su regla de firewall. |
| g) | Probar clientes CLI y gráficos | Registro de descarga autenticada/anónima en ambos tipos de cliente | Identifica cliente, modo y contenido; iniciar sesión sin transferir no basta. |

El reto RA3 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

<a id="ra4"></a>
## RA4 · Correo: entrega local, alias y recogida IMAPS remota

> Gestiona servidores de correo electrónico identificando requerimientos de utilización y aplicando criterios de configuración.

El correo entregado a un directorio local sólo prepara parte del resultado. La recogida remota requiere un servicio y un cliente que recuperen el contenido. El reto conserva Postfix en loopback y utiliza un túnel SSH para el envío de formación, mientras IMAPS está limitado a los clientes previstos. La configuración separa nombre, certificado, autenticación, ruta Maildir y permisos. La prueba de rechazo evita convertir un laboratorio de correo en un retransmisor público.

**Actividad desarrollada:** [`0227-RA4-A1`](11-retos-por-ra.md#ra4).

**Preparación:** [05-correo-local.md](05-correo-local.md), [09-correo-observabilidad-y-continuidad.md](09-correo-observabilidad-y-continuidad.md), [12-complementos-curriculares-ra.md](12-complementos-curriculares-ra.md), [11-retos-por-ra.md](11-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Describir envío y recogida de mensajes | Recorrido SMTP–cola–entrega–buzón–IMAP | Explica la función de cada protocolo y distingue entrega local y recepción remota. |
| b) | Instalar servidor de correo | Configuración Postfix y listener restringido | Conserva el alcance loopback y la política de destinos locales del ejercicio. |
| c) | Crear cuentas y comprobar acceso | Buzones temporales y autenticación con identidades de laboratorio | Cada usuario accede a su buzón y una identidad ajena se rechaza. |
| d) | Definir alias de cuentas | Alias creado, base reconstruida y mensaje identificable | La dirección alias entrega al buzón previsto y no se confunde con una cuenta nueva. |
| e) | Impedir usos indebidos | Prueba de destinatario externo y revisión de listeners | Se rechaza el destino no autorizado antes de DATA y no existe relay abierto. |
| f) | Instalar recogida remota | Dovecot compatible con versión, IMAPS y CA/nombre comprobados | Un cliente LAB recupera el mensaje conocido; Maildir local por sí solo no basta. |
| g) | Enviar y recibir con cliente | Mensajes al usuario y alias enviados por túnel y recibidos por IMAPS | Coinciden identificador, asunto y cuerpo sin ampliar SMTP ni publicar contraseñas. |

El reto RA4 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

<a id="ra5"></a>
## RA5 · Dos sitios web, ejecución cliente/servidor y módulo instalado

> Gestiona servidores web identificando requerimientos de utilización y aplicando criterios de configuración.

Los sitios virtuales y la ejecución de código se prueban desde el cliente y contra la configuración cargada. El ejercicio compara una acción JavaScript con un backend y añade un módulo compatible cuya presencia pueda demostrarse. Instalar un CMS o utilizar una directiva que ya incorpora el servidor no demuestra automáticamente todos esos criterios. La comunicación se acepta con nombre y confianza correctos, y el alcance de escucha se revisa además de los permisos de aplicación.

**Actividad desarrollada:** [`0227-RA5-A1`](11-retos-por-ra.md#ra5).

**Preparación:** [02-guia-tecnica.md](02-guia-tecnica.md), [08-ssh-pki-y-publicacion-web.md](08-ssh-pki-y-publicacion-web.md), [11-retos-por-ra.md](11-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Explicar fundamentos y protocolos web | Recorrido de petición, transporte, TLS y respuesta HTTP | Distingue conexión, negociación, código y contenido sin saltar directamente al CMS. |
| b) | Instalar servidor web | Versiones, configuración efectiva y estado del servidor | El listener está limitado a LAB y la sintaxis se valida antes de recargar. |
| c) | Crear sitios virtuales | Dos nombres y raíces con contenido diferente | Ambas URLs sirven su sitio y se conserva una configuración saneada. |
| d) | Discriminar el sitio de destino | Matriz por IP/puerto, Host y SNI | Explica la selección y el comportamiento de un nombre no previsto. |
| e) | Configurar seguridad | Política de permisos, directorios, listeners y acceso de administración | Sólo se permiten operaciones y orígenes del diseño y se prueba una denegación. |
| f) | Comprobar acceso de usuarios | Solicitudes desde cliente con identidades cuando proceda | Se obtiene contenido esperado y se interpreta correctamente un error o rechazo. |
| g) | Probar código del servidor y cliente | Página JavaScript y backend PHP con respuesta sintética | Identifica dónde se ejecuta cada código y no entrega el fuente PHP al cliente. |
| h) | Instalar un módulo del servidor | Paquete compatible, carga efectiva y cabecera de prueba | Demuestra un módulo realmente instalado; una directiva incorporada no suple la prueba. |
| i) | Proteger la comunicación | Nombre y certificado válidos, CA confiada y prueba HTTPS | TLS valida sin omitir confianza ni nombre; acceder por IP no sustituye la URL prevista. |

El reto RA5 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

<a id="ra6"></a>
## RA6 · Acceso y administración remota por SSH y escritorio gráfico

> Gestiona métodos de acceso remoto describiendo sus características e instalando los servicios correspondientes.

Una ventana remota abierta es evidencia insuficiente si se desconoce equipo, cuenta u operación. El reto utiliza dos sistemas y dos métodos para diferenciar acceso de administración. Un cambio que requiera elevación se autoriza y registra; no se amplían permisos para ocultar un fallo. La variante gráfica requiere una edición y un servicio compatibles, control de origen y retirada de habilitaciones temporales. Si sólo se practica SSH, lo gráfico sigue pendiente.

**Actividad desarrollada:** [`0227-RA6-A1`](11-retos-por-ra.md#ra6).

**Preparación:** [02-guia-tecnica.md](02-guia-tecnica.md), [08-ssh-pki-y-publicacion-web.md](08-ssh-pki-y-publicacion-web.md), [12-complementos-curriculares-ra.md](12-complementos-curriculares-ra.md), [11-retos-por-ra.md](11-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Describir métodos de acceso y administración | Comparativa SSH/RDP con propósito y controles | Distingue conectarse, consultar y efectuar un cambio autorizado. |
| b) | Instalar acceso remoto CLI | Servicio SSH y cliente Windows hacia Linux | Se contrasta la identidad del host y la cuenta posee el permiso necesario. |
| c) | Instalar acceso remoto gráfico | Windows Pro como host RDP y cliente Linux | La edición, cuenta, NLA, firewall y certificado se comprueban en LAB. |
| d) | Comprobar ambos métodos | Registro de sesión, host, usuario y operación de cada método | La sesión tiene destino e identidad verificables y se prueba su tarea. |
| e) | Comparar ventajas y limitaciones | Tabla de recursos, automatización, latencia, auditoría y redirecciones | Justifica un método para un caso y limita funciones no necesarias. |
| f) | Probar acceso entre sistemas diferentes | Sesiones Windows–Linux y Linux–Windows | Identifica ambos extremos y no presenta un escritorio local como acceso remoto. |
| g) | Probar administración heterogénea | Consulta/cambio autorizado, elevación y retorno documentados | Se demuestra la tarea administrativa prevista sin conceder privilegios universales. |

El reto RA6 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

<a id="ra7"></a>
## RA7 · AP y router inalámbrico con clientes y escenarios comparados

> Despliega redes inalámbricas seguras justificando la configuración elegida y describiendo los procedimientos de implantación.

El RA incluye un router inalámbrico y una conexión exterior, además del AP. Una topología interna puede preparar routing y controles, pero no debe describirse como una conexión real a un operador. La cobertura requiere dispositivos y condiciones observables; las tablas sintéticas sirven para practicar interpretación. El expediente conserva qué se ha montado, qué mecanismo se ha simulado y qué parte requiere equipamiento o autorización adicionales, sin dar por cumplidas evidencias ausentes.

**Actividad desarrollada:** [`0227-RA7-A1`](11-retos-por-ra.md#ra7).

**Preparación:** [07-dhcp-dual-stack-y-operacion.md](07-dhcp-dual-stack-y-operacion.md), [11-retos-por-ra.md](11-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Instalar un AP en una LAN | Montaje y conexión del AP con su plano y puerto | El AP integra la LAN de formación y se registra qué funciones no realiza. |
| b) | Reconocer protocolos, modos y parámetros | Inventario de capacidades y configuración del AP | Distingue modo AP/router, banda, canal, seguridad y responsabilidades de red. |
| c) | Seleccionar configuración por escenario | Comparación de al menos dos escenarios y decisiones | Los parámetros satisfacen requisitos y capacidades de los equipos utilizados. |
| d) | Aplicar seguridad inalámbrica | Política y pruebas de asociación/gestión autorizadas y denegadas | El mecanismo es compatible y no se publica la clave del ejercicio. |
| e) | Comprobar cobertura con varios dispositivos | Matriz de clientes, posiciones y condiciones de radio | Registra mediciones reales y no equipara una VM a un adaptador inalámbrico físico. |
| f) | Instalar router con LAN y enlace público | Plano WAN/LAN, configuración y evidencia del alcance real o simulado | Separa el mecanismo simulado de una conexión de operador no realizada. |
| g) | Configurar y probar router desde LAN | Acceso de gestión, salida permitida y denegación desde el lado exterior | Los prefijos son distintos y la administración permanece en los orígenes previstos. |

El reto RA7 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

<a id="ra8"></a>
## RA8 · Pasarela entre redes, proxy, caché y publicación controlada

> Establece el acceso desde redes locales a redes públicas identificando posibles escenarios y aplicando software específico.

El reto usa una pasarela dedicada y una red exterior de documentación, separadas de la LAB base. Se ejercitan reenvío, control, proxy, almacenamiento y entrada a un servicio privado. Los criterios se observan mediante aplicaciones y tráfico desde clientes de redes diferentes; instalar paquetes o consultar desde el propio servidor no basta. Una conexión real a una red pública requiere las condiciones y autorizaciones de ese entorno, por lo que la simulación se identifica como preparación del mecanismo y no como ejecución pública.

**Actividad desarrollada:** [`0227-RA8-A1`](11-retos-por-ra.md#ra8).

**Preparación:** [01-fundamentos.md](01-fundamentos.md), [09-correo-observabilidad-y-continuidad.md](09-correo-observabilidad-y-continuidad.md), [12-complementos-curriculares-ra.md](12-complementos-curriculares-ra.md), [11-retos-por-ra.md](11-retos-por-ra.md).

| CE | Resumen didáctico | Evidencia observable | Condición de aceptación propuesta |
| --- | --- | --- | --- |
| a) | Configurar hardware con lado privado y exterior | Dos interfaces y tabla de rutas de la pasarela dedicada | Cada interfaz y prefijo corresponde al plano, sin alterar la LAB base. |
| b) | Instalar aplicación de pasarela | Proxy instalado, versión y listener limitado a LAN | La aplicación está operativa y no funciona como proxy abierto. |
| c) | Reconocer funciones de la aplicación | Comparación de proxy, routing, NAT, filtrado y caché | Explica qué componente realiza cada función y qué no intercepta automáticamente. |
| d) | Configurar clientes de la red privada | Gateway y proxy explícito aplicados donde corresponde | El cliente utiliza el trayecto previsto y se conserva ruta de retorno. |
| e) | Controlar tráfico a través de la pasarela | Reglas efectivas y petición permitida/denegada | Sólo atraviesan protocolos, destinos y sentidos definidos por la práctica. |
| f) | Implementar aceleración | Objeto cacheable y evidencia HIT/MISS o revalidación en logs | La política permite almacenar y no se deduce caché sólo de una petición rápida. |
| g) | Identificar escenarios de aceleración | Comparativa de contenido público cacheable y privado/no-store | Justifica dónde aporta valor y reconoce límites de CONNECT y contenido cifrado. |
| h) | Reenviar entre interfaces | Reenvío IPv4 y reglas de forwarding documentados | Distingue routing y NAT, observa ambos sentidos y dispone de retorno por consola. |
| i) | Comprobar acceso entre redes | Petición privada a servidor exterior simulado | La prueba parte de otra red y explica dirección observada antes/después de NAT. |
| j) | Publicar servicio privado hacia exterior | DNAT y acceso desde cliente exterior al contenido privado esperado | Verifica puerto, reglas y retorno; la red simulada no acredita acceso de operador real. |

El reto RA8 detalla preparación, secuencia, resultado esperado y cierre. Al revisar, identifica la fila concreta que falta: un estado de proceso, una declaración de configuración o una foto sin contexto no demuestran automáticamente todas las condiciones de la tabla. Conserva versiones, identidad, origen y destino de las pruebas que procedan.

## Instrumentos de revisión y recuperación

La revisión puede combinar observación del procedimiento, dossier, archivos saneados, demostración desde cliente y preguntas sobre decisiones. El estudiante señala en qué artefacto se observa cada criterio. El docente aplica las condiciones y los instrumentos de su programación; esta matriz no asigna pesos oficiales ni transforma una simulación en una operación física.

Usa la [matriz de pruebas](../../recursos/plantillas/matriz-de-pruebas.md) y la [memoria de práctica](../../recursos/plantillas/memoria-practica.md). Registra fecha, entorno, resultado obtenido, evidencia y revisión pendiente. Si no has ejecutado una operación, conserva el diseño y explica qué falta para probarla. Una recuperación de aprendizaje concreta pide, por ejemplo, repetir una terminación, demostrar un modo de acceso o verificar una identidad distinta, no rehacer todo el trabajo sin diagnosticar la carencia.

Antes de compartir, elimina contraseñas, claves privadas, TSIG, mensajes y datos reales. Conserva configuraciones con secretos saneados y evidencias sintéticas. No ejecutes pruebas sobre redes ajenas para rellenar una fila; el alcance del laboratorio y la autorización preceden a la actividad.

## Lectura de los datos trazables

El archivo [alineacion-ra.json](alineacion-ra.json) contiene 8 RA, 63 CE y una actividad desarrollada por RA. Cada criterio indica resumen, identificador de actividad, evidencia y aceptación. Las rutas de ese JSON parten de la raíz del repositorio; las de esta guía son relativas a su carpeta. El validador global compara números, enunciados, letras y relaciones con el referente normativo local.

Los datos describen oportunidades de aprendizaje y trazabilidad editorial. Para acreditar trabajo individual o en grupo hacen falta resultados y contribuciones observados. Conserva especialmente esa distinción en actividades con dos participantes, operaciones físicas y conexiones a redes públicas.
