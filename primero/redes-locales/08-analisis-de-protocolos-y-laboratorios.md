# Análisis de protocolos y laboratorio de evidencias

[Índice de Redes locales](README.md) · [Método de diagnóstico](../../docs/metodo-de-diagnostico.md)

## 1. Una captura responde preguntas concretas

Antes de capturar, escribe una hipótesis. «La consulta DNS sale por NAT en vez de LAB» se puede contrastar eligiendo interfaz y observando destino. «La red va mal» no indica dónde capturar ni qué estímulo generar. Define máquina, interfaz, tiempo, filtro, servicio, identidad y resultado esperado. Después relaciona cada paquete con la prueba que realizaste.

Las tablas de este capítulo son **secuencias sintéticas para aprender**. No son capturas ejecutadas ni archivos PCAP obtenidos en el entorno. Los tiempos, números de secuencia y direcciones ilustran mecanismos. En tus prácticas debes conservar el archivo real y sus condiciones, con tráfico de laboratorio y sin datos personales.

Una captura en el cliente observa un punto distinto de una captura en el servidor. NAT, túneles, offloading y cifrado pueden cambiar lo visible. Una trama no observada puede haberse descartado antes del punto de captura, quedar fuera del filtro o viajar por otra interfaz. Expresa siempre «no aparece en esta captura», en vez de convertir esa ausencia en una afirmación universal.

## 2. Preparar una captura limitada

En Debian 13 de laboratorio instala `tcpdump`, `iputils-ping`, `iputils-tracepath` y, si se necesita una prueba de rendimiento, `iperf3` desde repositorios oficiales. La guía técnica describe instalación y aislamiento. Identifica LAB con `ip -br address`; `ens19` sigue siendo sólo el nombre de ejemplo.

```bash
sudo tcpdump -ni ens19 -s 0 -c 120 -w /tmp/smr-protocolos.pcap \
  'arp or icmp or icmp6 or port 53 or tcp port 443'
```

`-s0` solicita capturar el paquete completo según las posibilidades de la herramienta; `-c120` limita el número, no la duración. Si no se generan paquetes, el comando sigue esperando: termina con Ctrl+C cuando haya pasado la ventana prevista. El archivo se conserva con los permisos de quien lo creó. Transfiérelo a una carpeta privada de evidencias y revisa su contenido antes de publicar cualquier extracto.

Un filtro de captura reduce lo que se guarda. Un filtro de visualización sólo cambia lo que muestra Wireshark de lo ya capturado. Si excluiste ICMP al capturar, ningún filtro posterior puede recuperarlo. Si observas un SYN en una captura filtrada por 443, no deduzcas que no hubo antes una consulta DNS que el filtro descartó.

## 3. Caso ARP y selección del siguiente salto

Escenario base: cliente `.20/24` y servidor `.10/24` en LAB. El cliente necesita la MAC de `.10` y no dispone de entrada válida. Una secuencia sintética es:

| Orden | Origen de enlace | Destino de enlace | Mensaje |
| --- | --- | --- | --- |
| 1 | MAC cliente | Broadcast | ARP: quién tiene 192.168.56.10; responder a 192.168.56.20 |
| 2 | MAC servidor | MAC cliente | ARP: 192.168.56.10 está en MAC servidor |
| 3 | MAC cliente | MAC servidor | Paquete IPv4 destinado a 192.168.56.10 |

Si el destino estuviese en otra subred, el cliente buscaría la MAC del siguiente salto según la ruta. No enviaría una pregunta ARP para descubrir la MAC del servidor remoto a través de routers ordinarios. Una máscara errónea puede hacer que el cliente intente ARP por un destino que debería ser remoto.

La caché evita repetir ARP en cada petición. Para estudiar un intercambio inicial, identifica primero la entrada de vecino y su estado. No borres toda la caché de una máquina de trabajo real; en laboratorio puedes esperar expiración o eliminar exclusivamente la entrada del destino con el procedimiento del SO. Documenta el cambio porque altera el estado inicial de la prueba.

Una respuesta ARP demuestra que alguien reclama esa IP en el enlace. No prueba identidad criptográfica, que el puerto 443 esté activo o que la aplicación responda. Para una IP duplicada, correlaciona cambios de MAC, respuestas múltiples y configuración de ambos equipos; no selecciones arbitrariamente cuál «parece correcto».

## 4. Neighbor Discovery e IPv6

IPv6 utiliza ICMPv6 para descubrimiento de vecinos. Una Neighbor Solicitation busca la dirección de enlace de un vecino o realiza otras funciones según contexto; Neighbor Advertisement aporta información de respuesta. El destino multicast y los estados de vecino requieren interpretación, no una traducción literal de todos los campos de ARP.

Distingue también Router Solicitation y Router Advertisement. Un host puede pedir información de routers; un RA puede anunciar prefijos y parámetros. Una dirección SLAAC válida no demuestra que el router tenga conectividad a Internet. Una dirección de enlace local permite ciertas comunicaciones del enlace aunque falte una dirección global o ULA del diseño.

Duplicate Address Detection comprueba la posible existencia previa de una dirección antes de utilizarla conforme al mecanismo aplicable. Ver paquetes asociados no significa que haya ocurrido una duplicación. Debes observar respuesta, estado del cliente y resultado. Del mismo modo, una entrada `STALE` de vecinos no equivale a una avería confirmada: el protocolo puede verificarla al necesitar comunicación.

Al capturar dual stack, prueba ambos protocolos de forma explícita. Una aplicación puede preferir una familia, intentar alternativas y ocultar un fallo parcial. Que el navegador abra un sitio no valida la ruta IPv6 si terminó usando IPv4. Registra la dirección realmente utilizada y su relación con DNS.

## 5. TCP: establecimiento y números de secuencia

Un ejemplo sintético de apertura entre cliente y 443 del servidor:

| Etapa | Emisor | Flags | Secuencia | ACK | Interpretación |
| --- | --- | --- | ---: | ---: | --- |
| 1 | Cliente | SYN | 1000 | — | Solicita abrir conexión |
| 2 | Servidor | SYN,ACK | 5000 | 1001 | Acepta y confirma el SYN |
| 3 | Cliente | ACK | 1001 | 5001 | Confirma el SYN del servidor |
| 4 | Cliente | PSH,ACK | 1001 | 5001 | Envía 600 bytes de datos de ejemplo |
| 5 | Servidor | ACK | 5001 | 1601 | Espera a continuación el byte 1601 |

SYN consume un número de secuencia; los 600 bytes abarcan 1001–1600. El ACK 1601 indica el siguiente byte esperado dentro del modelo. Las herramientas pueden mostrar números relativos para facilitar lectura. Debes saber qué presentación utiliza antes de comparar capturas de dos extremos.

Un SYN repetido sin SYN,ACK puede indicar que no llega la respuesta, que se descarta la petición o que falta servicio; la captura de un único extremo no elige automáticamente una causa. Un RST puede señalar rechazo o cierre según contexto. Un ACK de transporte confirma recepción de bytes por TCP, no que la aplicación haya procesado correctamente el contenido o lo haya guardado en disco.

La ventana anunciada limita lo que el receptor puede aceptar pendiente de confirmación. Una ventana cero puede reflejar que la aplicación no consume datos con suficiente rapidez. No se corrige necesariamente ampliando el enlace. El control de congestión del emisor y la ventana del receptor son mecanismos relacionados con límites distintos.

## 6. Retransmisión, pérdida y reordenación

Wireshark identifica ciertas situaciones mediante heurísticas. Una etiqueta de retransmisión describe lo que puede inferir de paquetes observados y su orden; no certifica el punto físico donde se perdió un paquete. Una captura incompleta puede producir interpretaciones engañosas. Comprueba calidad del punto de captura y contadores de paquetes descartados por la herramienta.

Secuencia sintética: el emisor envía segmentos con bytes 1001–1600,1601–2200 y 2201–2800. Si falta el segundo y llega el tercero, el receptor no puede confirmar de forma acumulativa todos los bytes hasta 2800. Puede seguir indicando 1601 y utilizar SACK cuando se negoció. La retransmisión del hueco permite avanzar después el ACK. Explica qué significa cada rango antes de contar «paquetes malos».

Una retransmisión puede deberse a pérdida, demora o reordenación que el algoritmo interpreta como pérdida. Para investigar, compara cliente y servidor con relojes suficientemente sincronizados y una carga repetible. Si un segmento aparece en el emisor y no en el receptor, el fallo está entre esos puntos de observación o en el mecanismo de captura; todavía no has identificado qué dispositivo lo descartó.

Cuando una prueba usa Wi-Fi, las retransmisiones de enlace pueden recuperar tramas antes de que TCP intervenga. Un contador TCP bajo no demuestra ausencia de problemas radio. Por eso el análisis de extremo a extremo necesita combinar métricas de capa 2, transporte y aplicación.

## 7. MTU, MSS y descubrimiento de camino

MTU limita el tamaño de paquetes de red transportados por un enlace. MSS es una opción TCP que comunica una cantidad de datos por segmento que el extremo puede aceptar bajo sus condiciones. Un camino con túneles puede admitir menos tamaño que la Ethernet local. Ajustar un parámetro sin identificar el camino puede esconder el problema y afectar otras comunicaciones.

En IPv4, un paquete con DF puede provocar un mensaje de que se necesita fragmentación si no cabe. En IPv6 los routers no fragmentan como en IPv4; el emisor necesita conocer restricciones y puede utilizar los mecanismos previstos. ICMP/ICMPv6 relevante para PMTUD debe tratarse correctamente. Filtrar todos los mensajes puede producir una conexión que abre con paquetes pequeños y se queda atascada al transferir datos.

Prueba didáctica en Linux, sólo hacia el cliente/servidor autorizado:

```bash
ping -4 -c 3 -M do -s 1472 192.168.56.10
tracepath 192.168.56.10
```

En una IPv4 sin opciones,1472 bytes de datos ICMP más 8 de cabecera ICMP y 20 de IPv4 suman 1500. Este cálculo depende de esas cabeceras; no se traslada sin cambios a IPv6, túneles u opciones. La prueba puede fallar por política ICMP aunque la MTU permita el tamaño. Combina con los mensajes de error y las condiciones de la red.

No alteres la MTU permanente de todas las interfaces para completar el ejercicio. Para estudiar un enlace reducido utiliza una topología separada o una interfaz de laboratorio identificada y conserva el valor anterior. Después restaura y comprueba que otros servicios sigan funcionando.

## 8. DNS y TLS: correlacionar sin inventar visibilidad

En DNS ordinario puedes observar nombre, tipo, identificador y respuesta. Correlaciona también IP/puerto y dirección de la conversación, porque un identificador por sí solo puede repetirse. Una respuesta NXDOMAIN indica inexistencia de nombre en ese contexto; no equivale a SERVFAIL, que puede reflejar fallo de resolución o validación.

Si la aplicación utiliza DNS cifrado, una captura de red ordinaria no muestra necesariamente sus nombres. Puede haber caché local y no aparecer ninguna consulta durante la prueba. Antes de afirmar que una aplicación «no usa DNS», comprueba estado inicial, método de resolución y si hubo una consulta previa.

En TLS puedes observar ciertos metadatos de negociación según versión y mecanismos utilizados. El contenido HTTP queda protegido por el canal, y algunas extensiones pueden ocultar más información de la negociación. No deduzcas URL completa, contraseña o código HTTP de una captura cifrada sin un mecanismo de descifrado autorizado y correctamente documentado.

El registro del servidor y una petición controlada con `curl` pueden aportar el código HTTP sin descifrar capturas. Es una fuente distinta que debe correlacionarse por hora, cliente y solicitud. Una captura de TCP no prueba que el certificado sea de confianza para el navegador; esa validación ocurre en el cliente y requiere comprobar nombre, cadena y fechas.

## 9. Práctica de investigación con cuatro hipótesis

Prepara un cliente y un servidor propios de LAB, con HTTPS ya funcional según Servicios en red. Conserva su configuración. Elige uno de cuatro fallos: DNS del cliente incorrecto, listener detenido, regla del laboratorio que impide el puerto o nombre de certificado equivocado. Modifica una sola variable y registra cómo volver atrás. No introduzcas simultáneamente todos los fallos.

Captura una ventana limitada y ejecuta tres pruebas: consulta al DNS previsto, conexión TCP al destino y petición HTTPS con validación. Ordena las evidencias por hipótesis. Si llega SYN,ACK y falla TLS por nombre, la red y transporte han completado parte del trabajo; no clasifiques el incidente como «cable roto». Si no sale ningún paquete hacia LAB, revisa ruta y resolución antes de cambiar servidor.

Entrega el PCAP real privado o un extracto saneado autorizado, tabla de cinco eventos, hipótesis descartadas, causa y recuperación. No publiques contenido sensible. Si sólo puedes realizar el análisis con las tablas sintéticas de este capítulo, identifica el trabajo como interpretación de datos de ejemplo y deja la ejecución pendiente.

La rúbrica propia asigna 20% al estado inicial,25% a pruebas discriminantes,25% a interpretación por capas,20% a recuperación y 10% a claridad/privacidad. Una lista de filtros sin razonamiento no sustituye el análisis. El objetivo es poder explicar qué demuestra cada prueba y qué sigue sin conocerse.

## 10. Preguntas para defender la conclusión

¿Por qué un ACK no equivale a confirmación de aplicación? Porque TCP entrega un flujo y la aplicación tiene sus propios estados. ¿Por qué no aparece FCS? Porque el punto de captura o la NIC puede retirarlo. ¿Por qué un checksum parece incorrecto al salir? Puede calcularse después por offloading; compara el receptor. ¿Por qué hay datos IPv6 aunque sólo se configuró IPv4? El SO puede utilizar enlace local y control IPv6 sin esa configuración manual.

Una conclusión rigurosa utiliza la evidencia mínima necesaria y declara los límites del punto de observación. «El cliente envía tres SYN sin respuesta en LAB; el servidor no registra esos SYN y su listener está activo» orienta la siguiente prueba. «El servidor está roto» expresa una causa que aún no se ha demostrado.

## Referencias primarias

- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/).
- [tcpdump: manual](https://www.tcpdump.org/manpages/tcpdump.1.html).
- [RFC 9293: TCP](https://www.rfc-editor.org/rfc/rfc9293).
- [RFC 2018: TCP SACK](https://www.rfc-editor.org/rfc/rfc2018).
- [RFC 1191: PMTUD IPv4](https://www.rfc-editor.org/rfc/rfc1191).
- [RFC 8201: PMTUD IPv6](https://www.rfc-editor.org/rfc/rfc8201).
- [RFC 4861: descubrimiento de vecinos IPv6](https://www.rfc-editor.org/rfc/rfc4861).
