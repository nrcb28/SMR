# Configuración, observación y análisis de una LAN

## 1. Condiciones del procedimiento

Estos ejemplos se ejecutan dentro de las VMs del [laboratorio](../../docs/laboratorio.md), no en el equipo de trabajo del administrador. Toma una instantánea y conserva acceso por consola antes de modificar una interfaz. Cambiar una IP o una ruta puede cortar una sesión SSH. Las salidas indicadas son resultados que debes buscar; no son pruebas ejecutadas en este repositorio.

No hay un único fichero de configuración válido para todo Linux. Debian puede utilizar ifupdown, NetworkManager o systemd-networkd según instalación. La instrucción correcta empieza por averiguar qué componente administra la interfaz; mezclar gestores causa estados que reaparecen al reiniciar.

## 2. Inventario inicial en Linux

Ejecuta sin modificar la configuración:

~~~bash
ip -br link
ip -br address
ip route show
ip -6 route show
ip neigh show
systemctl is-active NetworkManager systemd-networkd networking
~~~

`ip -br` resume nombres y estado. Correlaciona la MAC con la configuración del hipervisor para distinguir LAB y NAT. Un nombre `ens19` es un ejemplo, no una garantía. `ip route` debe mostrar `192.168.56.0/24 dev ens19` si LAB ya está configurada. La ruta por defecto, si existe, debe pertenecer a NAT. En LAB no añadas un gateway inventado.

Registra versión de SO con `cat /etc/os-release` y versión de las herramientas con `ip -V`. Si existe NetworkManager, `nmcli device status` y `nmcli connection show` identifican el perfil que realmente aplica cada ajuste. Un servicio activo por sí solo no demuestra qué interfaz controla.

Para probar una IP temporal en una VM cuyo gestor ya se haya detenido o configurado expresamente para no manejar LAB:

~~~bash
sudo ip link set dev ens19 up
sudo ip address add 192.168.56.10/24 dev ens19
ip -br address show dev ens19
~~~

No ejecutes `address add` si esa IP ya existe. La operación no es persistente y puede entrar en conflicto con un gestor; se usa aquí para comprender el efecto. La reversión de esta adición concreta es:

~~~bash
sudo ip address del 192.168.56.10/24 dev ens19
~~~

No utilices `ip address flush` como limpieza general: podría eliminar direcciones que no añadiste. Para persistencia, conserva una sola autoridad por interfaz y utiliza su mecanismo.

### Ejemplo persistente con ifupdown

Sólo si ifupdown administra LAB, edita un fichero dentro de `/etc/network/interfaces.d/` que el fichero principal incluya:

~~~text
auto ens19
iface ens19 inet static
    address 192.168.56.10/24
~~~

No se define `gateway`. Conserva la configuración NAT existente. Aplica desde consola con el procedimiento del gestor y verifica tanto LAB como acceso NAT. En equipos con NetworkManager cambia el perfil mediante `nmcli connection modify`, dejando `ipv4.never-default yes` para LAB. Documenta el nombre real del perfil y sus valores anteriores antes de modificarlos.

## 3. Inventario y configuración en Windows 11 Pro

Abre PowerShell y observa:

~~~powershell
Get-NetAdapter
Get-NetIPConfiguration
Get-NetIPAddress -AddressFamily IPv4
Get-NetRoute -AddressFamily IPv4
Get-DnsClientServerAddress
~~~

Relaciona `InterfaceIndex` y MAC con el adaptador LAB. No copies un índice de otro equipo. Para configurar una VM de cliente con IP fija, usa la consola gráfica de propiedades IPv4 del adaptador identificado: IP `192.168.56.20`, máscara `255.255.255.0`, puerta de enlace vacía y DNS `192.168.56.10` sólo después de instalar el servicio de nombres.

Una alternativa en PowerShell elevado, suponiendo que LAB sea el índice 12 y que no exista una configuración estática incompatible, es:

~~~powershell
New-NetIPAddress -InterfaceIndex 12 -IPAddress 192.168.56.20 -PrefixLength 24
Set-DnsClientServerAddress -InterfaceIndex 12 -ServerAddresses 192.168.56.10
~~~

Comprueba primero si el adaptador usa DHCP y guarda ese estado. No añadas una segunda IP innecesariamente. Para volver al estado previo elimina sólo la dirección añadida mediante `Remove-NetIPAddress` y restablece DHCP y DNS automáticos cuando ésa fuese la situación original. No retires una configuración preexistente sólo para conseguir que el ejemplo funcione.

Windows clasifica redes mediante perfiles. Una red aislada puede quedar como pública y bloquear ICMP entrante. No desactives el firewall completo; inspecciona el perfil y habilita únicamente la regla de prueba que la práctica necesite, para la dirección o subred LAB. `Test-NetConnection 192.168.56.10 -Port 22` comprueba un puerto TCP y aporta más información que un ping cuando ICMP está filtrado.

## 4. Pruebas en orden y significado

1. **Enlace:** interfaz presente, estado arriba y velocidad/dúplex cuando el controlador lo muestre. En VM, revisar «cable conectado» y red virtual.
2. **Dirección:** IP y prefijo coherentes, ausencia de duplicados y adaptador correcto.
3. **Ruta:** `ip route get 192.168.56.20` muestra por qué interfaz intentará salir Linux. En Windows consulta `Get-NetRoute` y `Test-NetConnection`.
4. **Vecino:** `ip neigh show dev ens19` permite comprobar si se resolvió la MAC.
5. **Transporte:** prueba un puerto del servicio que debería existir.
6. **Aplicación:** realiza una operación real, por ejemplo una consulta DNS o una petición HTTPS.

`ping -c 4 192.168.56.20` en Linux y `ping -n 4 192.168.56.10` en Windows verifican intercambio ICMP si el destino lo permite. Ausencia de respuesta no distingue por sí sola host apagado, filtro, ruta incorrecta o pérdida. Una respuesta no demuestra DNS, HTTPS ni autenticación.

`tracepath` o `tracert` pueden mostrar saltos gracias a respuestas ICMP provocadas por TTL/Hop Limit. Un salto que no responde puede seguir reenviando tráfico. En una red directamente conectada no debería aparecer un router intermedio; si aparece, revisa la selección de rutas o qué red se está probando.

## 5. Captura de tráfico

Instala herramientas sólo dentro de la VM preparada, tras revisar su origen:

~~~bash
sudo apt update
sudo apt install tcpdump iputils-ping traceroute dnsutils iperf3
~~~

Si el instalador de `iperf3` pregunta si debe arrancar un servidor permanente, elige que no: en esta práctica se ejecuta de forma interactiva y se detiene al terminar. `traceroute` es el comando instalado por el paquete homónimo; `tracepath` requiere el paquete `iputils-tracepath` si quieres utilizar esa alternativa.

Una captura sobre LAB evita mezclar el acceso a Internet. Para observar una cantidad limitada de tráfico del propio laboratorio:

~~~bash
sudo tcpdump -ni ens19 -c 30 'arp or icmp'
~~~

`-n` evita resoluciones de nombres durante la captura, `-i` selecciona interfaz y `-c` limita paquetes. Para guardar evidencias:

~~~bash
sudo tcpdump -ni ens19 -c 100 -w /tmp/lan-lab.pcap 'arp or icmp or port 53'
~~~

Copia después el fichero a una carpeta de evidencias con permisos adecuados. Las capturas pueden contener nombres, direcciones y datos de aplicaciones. Publica únicamente tráfico sintético de este laboratorio y no subas credenciales ni sesiones reales.

Wireshark distingue filtros de captura y de visualización. Un filtro de captura como `port 53` decide qué se guarda; un filtro de visualización como `dns` decide qué se presenta de lo ya capturado. Confundirlos causa errores de sintaxis o pérdida de evidencia.

| Filtro de visualización | Qué permite examinar |
| --- | --- |
| `arp` | Resolución IPv4 local |
| `icmp || icmpv6` | Errores, eco y funciones de control |
| `ip.addr == 192.168.56.10` | Paquetes IPv4 asociados a esa IP |
| `tcp.flags.syn == 1` | Intentos de apertura TCP |
| `tcp.analysis.retransmission` | Retransmisiones detectadas heurísticamente |
| `dns` | Preguntas y respuestas DNS visibles |
| `tls.handshake` | Mensajes de negociación TLS que sean visibles |

En una LAN con switch, una NIC no recibe automáticamente los unicast de todos los demás equipos. El modo promiscuo sólo solicita entregar tramas recibidas por esa interfaz; no obliga al switch a enviarlas. Para observar otro enlace usa un puerto espejo o TAP autorizado. En Wi-Fi, el modo monitor y el canal introducen requisitos diferentes.

Una captura local puede mostrar checksums aparentemente incorrectos por offloading de la tarjeta, que termina el cálculo después del punto de captura. Correlaciona con una captura en el receptor antes de afirmar corrupción de red.

## 6. Rendimiento y calidad

Define una pregunta antes de medir: ¿cuánto tarda una petición?, ¿qué tasa útil se obtiene?, ¿hay pérdidas al aumentar carga? Latencia es tiempo; ancho de banda es capacidad; throughput es tasa observada; jitter es variación temporal. Expresa unidades: 1 Gb/s no equivale a 1 GB/s.

Para una prueba de rendimiento controlada usa `iperf3` sólo entre VMs propias, con límite de duración y conocimiento de la carga. En el receptor:

~~~bash
iperf3 -s -B 192.168.56.10
~~~

En el cliente:

~~~bash
iperf3 -c 192.168.56.10 -t 10
~~~

Detén el servidor después de la práctica. Compara ambos sentidos, CPU, número de flujos y uso del hipervisor. Un resultado bajo entre VMs puede depender del equipo anfitrión y no de la tecnología Ethernet física. No extrapoles una cifra de un laboratorio virtual a la capacidad del cableado del edificio.

## 7. VLAN con equipos que las soporten

Un switch host-only de un hipervisor puede no ofrecer VLAN configurables ni garantizar transparencia de etiquetas. Para esta práctica utiliza dos switches administrables o un simulador explícito. Diseña antes:

| VLAN | Nombre | Subred | Gateway planificado |
| --- | --- | --- | --- |
| 10 | Alumnado | 10.20.10.0/24 | 10.20.10.1 |
| 20 | Gestión | 10.20.20.0/24 | 10.20.20.1 |

Estas direcciones pertenecen a una topología alternativa; no las mezcles con el laboratorio común sin modificar su diseño. En switches, configura puertos de acceso para cada VLAN y el enlace entre switches como trunk permitiendo únicamente 10 y 20. Los comandos varían por fabricante; conserva la configuración anterior, consulta la documentación de la versión instalada y guarda la configuración de arranque.

Los puertos conectados a PCs ordinarios deben quedar en acceso salvo que el PC sea parte de un diseño de trunk. Verifica tabla MAC por VLAN, pertenencia de puertos, VLAN permitidas y estado STP. Una prueba entre dos PCs de la VLAN 10 en switches diferentes debe funcionar sin router; entre VLAN 10 y 20 debe fallar si no hay routing.

Para añadir routing usa un router con subinterfaces 802.1Q o un switch de capa 3. Cada interfaz lógica actúa como gateway de su subred. Antes de habilitar tráfico define una matriz: alumnado puede consultar DNS y HTTPS en gestión, pero no acceder a SSH de administración. Implementa y prueba ambos casos permitidos y denegados.

## 8. Wi-Fi: despliegue verificable

Haz un plano de puntos de acceso y registra banda, canal, ancho y potencia. Separa la medición de señal de la de rendimiento. Un RSSI adecuado no garantiza baja interferencia ni capacidad suficiente cuando hay muchos clientes.

Configura SSID, mecanismo de autenticación, política de invitados y su asociación a VLAN. Desactiva funciones de administración remota innecesarias; actualiza firmware siguiendo al fabricante y conserva copia de configuración. No publiques una contraseña compartida dentro del repositorio.

Las pruebas deben incluir asociación, obtención de dirección, DNS, acceso autorizado, aislamiento de invitados y reconexión. Registra modelo y controlador del cliente: dos dispositivos en la misma mesa pueden negociar capacidades distintas. Para roaming, mide una aplicación durante el movimiento; cambiar de BSSID en una pantalla no demuestra continuidad de sesión.

## Referencias

- [iproute2: manuales Debian](https://manpages.debian.org/trixie/iproute2/).
- [Debian Reference: configuración de red](https://www.debian.org/doc/manuals/debian-reference/ch05.en.html).
- [Microsoft Learn: módulo NetTCPIP](https://learn.microsoft.com/powershell/module/nettcpip/).
- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/).
- [tcpdump: manual](https://www.tcpdump.org/manpages/tcpdump.1.html).
- [ESnet: iperf3](https://software.es.net/iperf/).
