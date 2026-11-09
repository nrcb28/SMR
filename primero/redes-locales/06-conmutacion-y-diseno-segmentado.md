# Conmutación avanzada y diseño de una red segmentada

[Índice de Redes locales](README.md) · [Direccionamiento avanzado](05-direccionamiento-y-ejercicios-avanzados.md)

## 1. Del dibujo de enlaces al modelo de funcionamiento

Un diseño L2 debe indicar cómo circula cada VLAN en estado normal y qué sucede si falla un enlace. Un dibujo con dos switches y dos cables no demuestra redundancia: puede representar un bucle, una agregación bien configurada o una ruta bloqueada por STP. La diferencia está en la configuración, el protocolo y el estado efectivo.

Utiliza tres tablas antes de cambiar puertos: inventario físico, pertenencia de VLAN y matriz de comunicaciones. La primera identifica armario, switch, interfaz y extremo remoto. La segunda describe puertos de acceso, trunks, VLAN permitidas y tratamiento de tramas sin etiqueta. La tercera declara qué identidades o subredes necesitan comunicar y dónde se aplica la política. Una VLAN separa enlaces; la autorización entre VLAN pertenece al punto de enrutamiento y filtrado.

En el laboratorio base host-only no se da por supuesto soporte de 802.1Q. Para este capítulo se utiliza una **topología distinta**, con dos switches administrables o simulados y un router que soporte subinterfaces. Se plantea `10.70.10.0/24` para usuarios, `10.70.20.0/24` para servicios y `10.70.99.0/24` para gestión. No se añade un gateway ficticio a `192.168.56.0/24`.

## 2. Qué aprende y qué no aprende un switch

Cuando llega una trama válida, el switch puede aprender su MAC origen asociada al puerto y a la VLAN. Busca la MAC destino en el contexto adecuado. Una dirección conocida se reenvía por su puerto; una desconocida se replica por los puertos permitidos de esa VLAN, salvo el de entrada. Los estados de STP y los filtros de puerto limitan el proceso.

La edad de una entrada MAC no expresa cuánto tiempo lleva un ordenador encendido. Una MAC puede no transmitir durante un periodo, moverse legítimamente por roaming o migración de VM, o reaparecer por un bucle. Un cambio reiterado entre dos puertos debe correlacionarse con la topología y los registros antes de declarar fallo de hardware.

La tabla MAC no descubre por sí sola direcciones IP, usuarios o permisos. Las funciones adicionales de un equipo pueden inspeccionar ARP, DHCP o autenticación y construir otras tablas. Mantén separadas las fuentes: «el switch aprendió MAC X en puerto 7/VLAN 10» es una observación; «la persona de administración estaba usando ese equipo» requiere otra evidencia.

Un contador de errores FCS puede apuntar a un problema físico o de recepción, mientras que descartes por cola suelen relacionarse con congestión. Colisiones en un enlace moderno full-duplex merecen revisar qué mide realmente el contador, negociación y modo de puerto. No modifiques dúplex a ciegas: forzar sólo un extremo puede crear otro problema.

## 3. Etiquetas 802.1Q y significado de un trunk

Una etiqueta de VLAN añade información de control a la trama Ethernet. El identificador de VLAN permite clasificarla dentro de un enlace que transporta varias redes. Los campos de prioridad no garantizan por sí solos calidad de servicio de extremo a extremo; necesitan políticas de clasificación y planificación coherentes.

Un puerto de acceso asocia normalmente las tramas sin etiqueta a una VLAN. Un trunk admite un conjunto explícito de VLAN y un tratamiento acordado del tráfico sin etiqueta. Algunos fabricantes denominan de modo distinto VLAN nativa, VLAN no etiquetada y PVID. Lee la semántica del modelo antes de trasladar una receta. «Native 99» en un dispositivo no garantiza que el otro interprete igual todas las tramas.

La lista de VLAN permitidas reduce errores y tráfico innecesario. Si el enlace entre switches sólo necesita 10,20 y 99, no lo configures de forma genérica para transportar cualquier VLAN futura. La lista también se verifica en ambos extremos; permitir una VLAN en un extremo y excluirla en el otro puede producir un fallo parcial que se confunda con routing.

No utilices la VLAN de gestión como red ordinaria de alumnado. Define desde qué estación o subred se administra el switch, cómo se autentica y cómo se recupera la configuración. Cambiar la VLAN de gestión desde una sesión que depende de ella requiere consola o un camino alternativo probado. Guarda la configuración de arranque conforme al procedimiento del equipo.

## 4. El bucle como problema de estabilidad

Ethernet no incorpora un contador de saltos equivalente al TTL IP dentro de una LAN. Un broadcast que circula por un bucle puede reproducirse y consumir capacidad. Las tablas MAC pueden alternar puertos al recibir la misma MAC por caminos distintos. La consecuencia afecta a muchos equipos a la vez, no sólo al que originó la trama.

STP intercambia información entre puentes y selecciona una topología lógica sin bucles. El puente raíz se elige por un identificador que incorpora prioridad y dirección; los costes y desempates determinan los caminos. Configurar una prioridad intencional evita que el equipo menos apropiado se convierta en raíz por accidente. No basta con dejar todos los valores por defecto y dibujar dónde te gustaría que estuviera la raíz.

RSTP define roles y transiciones que permiten una convergencia más rápida en escenarios compatibles. No promete interrupción cero ante cualquier fallo. El tiempo observado depende de enlaces, negociación, dispositivos y modo de compatibilidad. La aceptación de redundancia debe medir pérdida de paquetes y tiempo de recuperación con una carga controlada.

Las funciones de puerto de borde aceleran puertos destinados a terminales. BPDU Guard puede deshabilitar o proteger un puerto de usuario si recibe BPDUs inesperadas. Estas funciones requieren un mapa de puertos fiable: activar un control de borde en un enlace entre switches o conectar un switch donde sólo se permitía un terminal puede interrumpir el servicio. Registra el procedimiento de recuperación y la causa antes de reactivar un puerto.

## 5. Redundancia mediante LACP

LACP coordina un conjunto de enlaces físicos que funciona como un enlace lógico entre equipos compatibles. Ambos extremos deben acordar parámetros de agregación y los miembros deben ser coherentes en velocidad, dúplex y política de VLAN según la plataforma. No añadas puertos a un grupo sólo porque están libres.

El reparto habitual usa una función sobre campos del flujo. Una transferencia TCP puede permanecer en un único miembro aunque haya dos enlaces de 1 Gb/s. Dos conversaciones independientes pueden utilizar enlaces distintos y alcanzar un total mayor. Por eso la prueba debe separar capacidad agregada de velocidad de una sola conexión.

Un cálculo de ejemplo: cuatro clientes envían cada uno 180 Mb/s a un servidor por una agregación de dos enlaces 1 Gb/s. La suma teórica de demanda es 720 Mb/s, pero la distribución puede ser desigual. Si la función coloca tres clientes en el mismo miembro, ese enlace recibe 540 Mb/s y el otro 180. No hay garantía de reparto 50/50. Cuando la demanda se acerca al límite, el patrón de flujos importa tanto como la suma.

No agregues enlaces que terminan en switches independientes salvo que exista una tecnología expresamente compatible con esa arquitectura. Un par de switches sin coordinación no es automáticamente un único extremo LACP. En SMR conviene dominar primero una agregación entre dos dispositivos y explicar el límite antes de estudiar agregación multichasis.

## 6. Política entre segmentos y rutas de retorno

El router del escenario tiene una dirección en cada VLAN y los clientes utilizan esa interfaz como siguiente salto para destinos remotos. La política propuesta permite que usuarios accedan a DNS y web de servicios, impide administración de switches desde usuarios y permite administración desde una estación de gestión. El protocolo exacto y la identidad necesaria deben constar en la matriz.

| Origen | Destino | Flujo | Decisión propuesta |
| --- | --- | --- | --- |
| Usuarios | Servicios | DNS y HTTPS previstos | Permitir |
| Usuarios | Gestión | SSH/HTTPS de administración | Denegar |
| Gestión autorizada | Switches/router | Administración necesaria | Permitir |
| Servicios | Usuarios | Nuevas conexiones no justificadas | Denegar |

La tabla es una política didáctica, no una configuración de firewall universal. La implementación debe tener en cuenta conexiones establecidas, ICMP de diagnóstico y errores necesarios, DNS sobre TCP/UDP e IPv6 si está habilitado. Un filtrado de retorno incorrecto puede permitir el SYN y descartar la respuesta, dando apariencia de puerto inaccesible.

Comprueba ruta de ida y de vuelta. Si un servidor tiene dos NIC, una respuesta puede salir por NAT aunque la petición entrara por LAB o por la VLAN de servicios. Evita solucionar la asimetría desactivando globalmente controles sin entenderla. Observa tabla de rutas, origen elegido y captura en ambos extremos.

## 7. Calidad de servicio, colas y sobresuscripción

Sobresuscripción significa que la suma de capacidades de acceso puede superar la capacidad de los enlaces de salida. Veinticuatro puertos de 1 Gb/s y un uplink de 1 Gb/s no garantizan 24 Gb/s hacia el servidor. Sin embargo tampoco implican que todo uso real esté saturado: hay que medir concurrencia y demanda.

Un ejemplo: veinte puestos transfieren simultáneamente 50 Mb/s útiles hacia un enlace de 1 Gb/s. La suma ya es 1.000 Mb/s antes de sobrecarga y ráfagas, de modo que el diseño está al límite. Si la aplicación produce ráfagas cortas, los buffers pueden absorber algunas; si la tasa sostenida supera la salida, crecerán colas y descartes. Aumentar el buffer puede reducir ciertos descartes y aumentar latencia; no crea capacidad adicional.

QoS clasifica y prioriza tráfico dentro de un presupuesto. No permite que dos flujos saturados reciban cada uno toda la capacidad del mismo enlace. Define qué tráfico necesita latencia acotada, cómo se identifica y qué confianza se da a marcas enviadas por terminales. Aceptar cualquier prioridad indicada por el cliente puede anular la política.

Las cifras nominales de backplane, puertos y paquetes por segundo describen dimensiones distintas. Una carga de paquetes pequeños puede exigir más procesamiento por bit útil que una de tramas grandes. Al comparar switches, relaciona especificación, tamaño de trama, funciones habilitadas y requisitos del entorno; no elijas por un único número publicitario.

## 8. Práctica: conmutación con fallo controlado

Prepara dos switches administrables o un simulador que implemente VLAN, STP y LACP. Documenta versión y limitaciones del simulador. Crea las tres VLAN del escenario y etiqueta puertos. Configura un único enlace interswitch, valida cada VLAN y realiza pruebas negativas entre segmentos antes de añadir redundancia.

Después configura dos enlaces como agregación según el manual de ambos extremos, o estudia dos caminos protegidos por STP en una práctica distinta. No combines ambos objetivos sin un diseño previo. Observa estado lógico, miembros, VLAN y rol de puertos. Ejecuta tráfico de prueba entre equipos propios y registra pérdida y tiempo al retirar un miembro o enlace previsto.

La recuperación consiste en restituir el enlace, comprobar convergencia, estado estable y persistencia de configuración. Si aparece inestabilidad MAC o aumento anormal de broadcast, desconecta el enlace agregado de la prueba desde consola y vuelve al último estado estable. No generes un bucle deliberado en una red compartida para obtener una captura espectacular.

**Entregables:** diagrama normal y de fallo, inventario de puertos, matriz de VLAN, política de comunicación, configuración saneada y tabla de resultados. La rúbrica propia valora 25% diseño,25% coherencia L2,25% pruebas de acceso/fallo y 25% recuperación/explicación. Una simulación que no implementa realmente STP no puede demostrar convergencia del protocolo.

## 9. Casos de diagnóstico razonados

**VLAN sólo falla en un switch.** Comprueba que exista localmente, que los puertos estén asociados y que se permita en el enlace. Una ruta IP correcta no transporta una VLAN ausente de un trunk.

**Todos pierden conectividad al conectar un cable nuevo.** Relaciona el evento con el mapa físico, estado STP, contadores de broadcast y movimientos MAC. Aísla el cambio reciente de forma controlada y conserva evidencia; no reinicies todos los switches a la vez.

**Un cliente llega al gateway pero no a web de servicios.** La conectividad local está parcialmente demostrada. Examina ruta entre VLAN, política, ruta de retorno y listener del servidor. No cambies el puerto de acceso a la VLAN de servicios sólo para eludir la política.

**Una copia no supera 1 Gb/s en LACP 2×1 Gb/s.** Puede ser el comportamiento esperado para un flujo. Añade conversaciones independientes y observa miembros; comprueba además disco y CPU del servidor. La velocidad de una aplicación no mide únicamente los enlaces.

**El switch ya no se administra tras cambiar su VLAN.** Usa consola y compara IP de gestión, VLAN, puerto/trunk, gateway y política. La prueba de recuperación exige devolver acceso autorizado, sin abrir administración a todas las redes.

## Referencias primarias

- [IEEE 802.1: trabajo y estándares de puentes y VLAN](https://1.ieee802.org/).
- [IEEE 802.1AX: agregación de enlaces](https://1.ieee802.org/tsn/802-1ax-rev/).
- [Linux bridge: documentación del kernel](https://docs.kernel.org/networking/bridge.html).
- [Cisco: documentación de switches](https://www.cisco.com/c/en/us/support/switches/index.html), para contrastar sintaxis y funciones del modelo concreto.
- [RFC 4594: clases de servicio](https://www.rfc-editor.org/rfc/rfc4594).
