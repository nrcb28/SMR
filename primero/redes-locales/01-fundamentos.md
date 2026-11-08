# Fundamentos y diseño de una red local

## 1. De la necesidad al diseño

Una LAN conecta dispositivos bajo una misma administración y en un ámbito limitado. «Local» no significa que todos deban compartir el mismo dominio de broadcast ni que deban tener permiso para comunicarse. Un aula, un laboratorio y una red de invitados pueden usar el mismo armario y, aun así, pertenecer a redes lógicas diferentes.

Antes de comprar equipos, recoge requisitos: número de puestos actual y previsto, aplicaciones, disponibilidad, movilidad, velocidad por usuario, consumo PoE, presupuesto y restricciones físicas. Añade quién administra cada elemento, dónde se guardará la configuración y cómo se recuperará. Un enlace de 10 Gb/s no resuelve una autenticación lenta causada por DNS ni una cobertura Wi-Fi mal situada.

Produce tres documentos distintos: plano físico con ubicación de tomas y armarios; esquema lógico con subredes, VLAN, gateways y servicios; inventario con modelos, puertos, versión de firmware, propietarios y etiquetado. La dirección IP puede cambiar; la etiqueta física debe seguir permitiendo localizar el cable.

## 2. Modelos, encapsulación y unidades de datos

OSI divide la comunicación en siete capas: física, enlace, red, transporte, sesión, presentación y aplicación. TCP/IP suele agrupar las funciones en acceso a red, Internet, transporte y aplicación. Son modelos para razonar; un producto real puede combinar funciones de varias capas.

Una petición HTTPS contiene datos HTTP dentro de TLS; TLS utiliza normalmente un flujo TCP; TCP se transporta en paquetes IP; éstos viajan en tramas Ethernet o 802.11. Cada capa añade información de control y el receptor la interpreta en orden inverso. En HTTP/3 el transporte cambia a QUIC sobre UDP, por lo que «todo HTTPS es TCP» es una simplificación incorrecta.

| Identificador | Ejemplo | Función |
| --- | --- | --- |
| Nombre DNS | `www.aula.test` | Identifica un nombre dentro del espacio DNS |
| Dirección IP | `192.168.56.10` | Permite seleccionar destino y ruta en la red |
| Puerto TCP/UDP | `443/TCP` | Distingue servicios y conversaciones de transporte |
| Dirección MAC | `02:00:00:00:00:10` | Identifica una interfaz en el enlace Ethernet local |
| VLAN ID | `20` | Separa dominios lógicos de enlace |

En un salto a través de un router, la trama se sustituye por otra adecuada al enlace siguiente. En el caso normal sin NAT, la IP origen y destino permanecen; cambian las MAC del enlace y disminuye el TTL de IPv4 o el Hop Limit de IPv6. Un switch Ethernet ordinario no necesita cambiar las direcciones IP para reenviar.

La MTU es el tamaño máximo de la unidad de nivel de red que un enlace admite sin mecanismos adicionales. En Ethernet habitual es 1500 bytes, pero no debe deducirse de la velocidad. Si un túnel añade cabeceras, el tamaño útil puede disminuir. Una web que abre parcialmente puede revelar un problema de descubrimiento de MTU; hacer que responda un ping pequeño no demuestra que todos los tamaños funcionen.

## 3. Medios físicos y cableado estructurado

El par trenzado reduce el acoplamiento del ruido aprovechando señalización diferencial y trenzados. Las categorías indican prestaciones normalizadas del sistema de cableado. No basta con que el cable tenga impresa una categoría: latiguillos, conectores, instalación y comprobación deben ser compatibles. Cat 6A es una elección habitual para enlaces 10GBASE-T de hasta 100 m dentro de los límites normalizados del canal; Cat 6 tiene restricciones adicionales para 10 Gb/s según longitud e interferencias.

Un canal horizontal típico contempla hasta 90 m de enlace permanente y hasta 10 m de latiguillos combinados, sujeto al estándar y a la aplicación. No planifiques al límite sin considerar armario, curvas y cambios. Evita tracción excesiva, aplastamientos, destrenzado largo en terminaciones y recorridos incompatibles con las exigencias eléctricas o contra incendios.

T568A y T568B describen ordenaciones de pares. Un cable directo utiliza la misma ordenación en ambos extremos. Un cable cruzado clásico intercambia pares para equipos sin Auto-MDI/MDIX, pero los equipos modernos suelen adaptarse automáticamente. Eso no convierte cualquier cableado incorrecto en válido: un par dividido puede conservar continuidad y fallar al transportar datos.

Un comprobador de continuidad detecta abiertos, cortocircuitos y algunos errores de orden. Un certificador mide parámetros como pérdidas e interferencias frente a un límite de categoría. La aceptación profesional de un enlace no debe basarse sólo en que un portátil negocie una velocidad o en que un LED se ilumine.

La fibra evita interferencias electromagnéticas en el medio óptico y permite distancias mayores según transceptor y tipo. Distingue multimodo y monomodo, longitud de onda, conectores, presupuesto óptico y compatibilidad de los módulos. No conectes un módulo elegido sólo por su forma SFP. Nunca mires directamente a una fibra o transceptor: la luz puede ser invisible y peligrosa.

PoE alimenta equipos como puntos de acceso y teléfonos. Deben coincidir compatibilidad del dispositivo alimentador, clase de potencia y presupuesto total del switch. Cuarenta y ocho puertos PoE no implican que los cuarenta y ocho puedan suministrar simultáneamente su potencia máxima. El cableado y la temperatura también influyen.

## 4. Ethernet, tablas MAC y bucles

Una trama Ethernet incluye MAC destino, MAC origen, campo de tipo/longitud, carga y comprobación FCS. La NIC verifica errores de trama; el FCS no es un mecanismo de autenticación criptográfica. En una captura puede faltar el FCS porque la tarjeta lo elimina antes de entregar los datos al sistema.

Un switch aprende la MAC origen de las tramas recibidas y la asocia a un puerto y una VLAN. Si conoce la MAC destino dentro de esa VLAN, reenvía al puerto correspondiente. Si no la conoce, hace flooding por los puertos de esa VLAN salvo el de entrada, de acuerdo con su estado y políticas. También replica el broadcast. La tabla MAC y la tabla ARP son cosas diferentes: la primera relaciona MAC y puertos; la segunda relaciona direcciones IPv4 y direcciones de enlace.

Una MAC no es una identidad fuerte. Puede modificarse, aleatorizarse o falsificarse. El control de acceso basado exclusivamente en listas de MAC no sustituye a una autenticación adecuada.

Un bucle de capa 2 puede multiplicar tramas broadcast y causar inestabilidad de aprendizaje. STP construye una topología sin bucles bloqueando lógicamente caminos redundantes. RSTP reduce el tiempo de convergencia en escenarios compatibles. Elige de forma intencional el puente raíz y protege puertos de usuario con funciones apropiadas como BPDU Guard, según fabricante. No desactives STP para que «todos los puertos estén activos».

La agregación de enlaces mediante LACP ofrece redundancia y capacidad agregada entre pares compatibles. No suele multiplicar el ancho de banda de una única conversación, porque el reparto se realiza mediante funciones de selección de flujos. Dos cables paralelos sin configuración coordinada de agregación pueden crear un bucle.

## 5. IPv4, prefijos y decisión local/remota

Una dirección IPv4 tiene 32 bits. El prefijo indica los bits de red. `192.168.56.20/24` equivale a máscara `255.255.255.0`: los primeros 24 bits identifican la red y quedan 8 bits para direcciones dentro de ella. La red es `192.168.56.0` y el broadcast dirigido es `192.168.56.255`; en una subred convencional, los hosts utilizables son `.1` a `.254`.

El host compara el destino con sus rutas. En términos simplificados, si pertenece a la subred directamente conectada, intenta alcanzarlo por el enlace; si no, necesita una ruta a través de un siguiente salto accesible. La selección utiliza el prefijo más específico, no la primera ruta escrita. La métrica suele resolver elecciones entre rutas comparables, con detalles dependientes del sistema.

Los rangos privados de RFC 1918 son `10.0.0.0/8`, `172.16.0.0/12` y `192.168.0.0/16`. No todos los prefijos que empiezan por 172 son privados. `169.254.0.0/16` corresponde a enlace local IPv4; verlo cuando esperabas DHCP sugiere que no se obtuvo una concesión, aunque es necesario comprobar la política del sistema.

Para un prefijo convencional /n con al menos dos bits de host, las direcciones totales son `2^(32-n)` y la capacidad habitual es ese valor menos dos. /31 en enlaces punto a punto y /32 en rutas de host requieren tratamiento específico; no apliques mecánicamente la resta de dos a cualquier prefijo.

### Ejemplo resuelto: /27

`192.168.56.77/27` tiene máscara `255.255.255.224`. El tamaño del bloque es `256 - 224 = 32`. Los límites del último octeto son 0, 32, 64, 96, etc. El 77 pertenece al bloque 64–95; por tanto, red `192.168.56.64`, broadcast `192.168.56.95`, hosts `.65–.94` y 30 hosts convencionales. El prefijo no se elige a partir del último número del host, sino de los bits de máscara.

### Ejemplo VLSM resuelto

Se dispone de `10.20.30.0/24` para 70 puestos, 30 puestos y 12 puestos. Asigna de mayor a menor para reducir huecos difíciles de aprovechar:

| Uso | Necesidad | Prefijo | Red | Rango de hosts | Broadcast |
| --- | --- | --- | --- | --- | --- |
| Aula A | 70 | /25 | 10.20.30.0 | .1–.126 | .127 |
| Aula B | 30 | /27 | 10.20.30.128 | .129–.158 | .159 |
| Taller | 12 | /28 | 10.20.30.160 | .161–.174 | .175 |

Queda libre `.176–.255`, que debe describirse como varios bloques alineados y no como una sola subred arbitraria. Si cada segmento necesita una puerta de enlace, ésta consume una dirección utilizable. Una necesidad de 30 ordenadores más un router ya no cabe en /27. Añade impresoras, AP, gestión y crecimiento antes de decidir.

## 6. ARP, routing y NAT

ARP resuelve una dirección IPv4 local en una MAC. Una petición pregunta por una IP en broadcast; el propietario suele contestar en unicast. Para comunicar con otra subred, el emisor busca la MAC del siguiente salto, no la MAC del servidor remoto. La caché reduce consultas, pero una entrada antigua o maliciosa puede producir fallos.

Un router mantiene rutas y reenvía entre interfaces. Cada red conectada debe disponer de un prefijo coherente; hace falta camino de ida y de vuelta. Habilitar el reenvío no crea automáticamente rutas en todos los equipos ni define una política de seguridad. Un firewall filtra según reglas; un router encamina; un mismo aparato puede hacer ambas funciones.

NAT cambia direcciones o puertos conforme a una tabla de traducción. Facilita ciertos usos de IPv4, pero no demuestra aislamiento suficiente ni sustituye a un firewall. La red NAT de un hipervisor también puede ocultar características del enlace; no es equivalente a un switch físico administrable.

## 7. IPv6 y descubrimiento de vecinos

IPv6 tiene 128 bits representados en hexadecimal. Se omiten ceros iniciales de grupos y se permite una sola compresión `::`. `2001:db8:56::10/64` es un ejemplo de documentación; `2001:db8::/32` no debe anunciarse en Internet como prefijo propio. Para un laboratorio local sin asignación global puede diseñarse un prefijo ULA conforme a RFC 4193.

Las direcciones de enlace local pertenecen a `fe80::/10` y requieren identificar la interfaz cuando un comando no puede deducirla. IPv6 utiliza multicast y Neighbor Discovery, basado en ICMPv6, para funciones que en IPv4 se distribuyen entre ARP y otros mecanismos. No dispone de broadcast equivalente al de IPv4.

Los Router Advertisements comunican información del enlace, incluidos anuncios de router y, según configuración, prefijos. SLAAC permite construir direcciones; DHCPv6 puede asignar direcciones o aportar otros parámetros. DHCPv6 no debe confundirse con el mecanismo habitual para aprender la puerta de enlace IPv6, que depende de RA. Las combinaciones reales requieren comprobar soporte y política del cliente.

No bloquees ICMPv6 de forma indiscriminada: interviene en descubrimiento de vecinos y descubrimiento de MTU, entre otras funciones. Tener conectividad IPv4 no demuestra que el firewall IPv6 esté bien configurado.

## 8. VLAN y Wi-Fi dentro del diseño

Una VLAN es un dominio lógico de enlace. Un puerto de acceso normalmente entrega tráfico sin etiqueta a un dispositivo final y lo asocia a una VLAN. Un trunk transporta varias VLAN, habitualmente con etiquetas 802.1Q. La VLAN nativa o sin etiqueta exige acuerdo entre extremos; una discrepancia puede comunicar segmentos no previstos o producir pérdidas.

Dos VLAN distintas requieren routing para comunicarse. La etiqueta separa dominios de broadcast; no expresa por sí misma una política completa de autorización. Debes decidir qué flujos pueden pasar entre subredes y en qué punto se filtran.

En Wi-Fi, SSID identifica una red anunciada y BSSID identifica una instancia de radio. Varios SSID pueden asignarse a diferentes VLAN. La señal compartida implica contención, interferencias y capacidades diferentes entre clientes; la velocidad anunciada por el fabricante es una tasa física bajo condiciones concretas, no el rendimiento útil de cada usuario.

Planifica canales, ancho de canal, colocación y densidad. En 2,4 GHz los canales se solapan en muchas combinaciones; usa un plan permitido en tu región y comprueba interferencias reales. En 5 y 6 GHz cambian requisitos y disponibilidad. Utiliza WPA3 cuando sea compatible y una política segura; WPA2 con AES puede ser necesario para equipos existentes. Evita WEP y TKIP. Para organizaciones, 802.1X con autenticación empresarial requiere certificados y un servicio de identidad correctamente administrados.

## Referencias primarias

- [RFC 791: IPv4](https://www.rfc-editor.org/rfc/rfc791).
- [RFC 1918: direccionamiento privado](https://www.rfc-editor.org/rfc/rfc1918).
- [RFC 3021: prefijos /31](https://www.rfc-editor.org/rfc/rfc3021).
- [RFC 8200: IPv6](https://www.rfc-editor.org/rfc/rfc8200).
- [RFC 4861: Neighbor Discovery](https://www.rfc-editor.org/rfc/rfc4861) y [RFC 4862: SLAAC](https://www.rfc-editor.org/rfc/rfc4862).
- [RFC 4193: ULA](https://www.rfc-editor.org/rfc/rfc4193).
- [IEEE 802: estándares de redes](https://www.ieee802.org/).
