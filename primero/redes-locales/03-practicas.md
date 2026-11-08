# Prácticas completas de Redes locales

Estas prácticas producen documentación y pruebas que otra persona puede repetir. Todos los cambios se realizan en equipos del laboratorio. Conserva una instantánea y un registro de la configuración inicial; al finalizar, restaura únicamente lo que hayas cambiado. Las cifras de tiempo son orientativas y no equivalen a horas oficiales del módulo.

## Práctica 1. Inventario y enlace físico

**Objetivo:** demostrar la correspondencia entre toma, latiguillo, puerto y equipo.\
**Duración orientativa:** 2–3 sesiones.\
**Material:** dos equipos, switch de laboratorio, dos latiguillos identificados y comprobador. Con VMs puede realizarse la parte lógica, pero no se considerará verificada la calidad del cableado físico.

### Procedimiento

1. Dibuja el recorrido completo de cada conexión: NIC, latiguillo, toma, panel, latiguillo y switch. Si hay una conexión directa al switch, indícalo en vez de inventar elementos.
2. Asigna etiquetas independientes de la IP: `AULA01-T03` para toma y `SW01-P08` para puerto. Registra fabricante, modelo, número de puerto y uso.
3. Comprueba continuidad en un latiguillo desconectado del equipamiento activo. Guarda el resultado y explica qué defectos puede detectar tu comprobador.
4. Conecta los equipos y anota estado de enlace, velocidad y dúplex. Si se negocia una velocidad inferior a la esperada, cambia sólo un latiguillo por otro conocido y vuelve a observar.
5. Configura `192.168.56.10/24` y `192.168.56.20/24` sin gateway sobre LAB, siguiendo el gestor real de cada SO.
6. Obtén una prueba IP y una tabla de vecinos. Relaciona las MAC con las etiquetas físicas.
7. Desconecta durante unos segundos el cable del equipo cliente, identifica el cambio observable y reconéctalo. Esta interrupción sólo se hace sobre el puesto de la práctica.

### Aceptación y entrega

Entrega un plano, una tabla de puertos, las evidencias del comprobador y dos estados de red: antes y después de la conexión. La explicación debe distinguir «hay continuidad» de «el enlace cumple una categoría». Añade una incidencia con causa, prueba de descarte y solución.

**Solución de referencia:** con ambas IP dentro de `192.168.56.0/24`, los equipos se comunican directamente por LAB y resuelven MAC mediante ARP; no necesitan router. Si el ping se bloquea por firewall, una conexión a un servicio conocido puede demostrar transporte sin desactivar el firewall completo.

**Reversión:** devuelve direcciones y reglas al estado inicial; conserva el etiquetado únicamente si se acordó como parte del inventario del laboratorio.

## Práctica 2. Plan de direccionamiento con crecimiento

**Objetivo:** obtener un diseño VLSM verificable y justificar el dimensionamiento.\
**Escenario:** una empresa ficticia dispone de `10.44.8.0/23`. Necesita administración con 90 puestos, aula con 45, taller con 20 y servicios con 10. Cada segmento requiere una dirección de gateway y se reserva un 20 % de crecimiento sobre el número de puestos.

### Procedimiento

1. Calcula necesidad de cada segmento como puestos más crecimiento redondeado hacia arriba más gateway. Si añades otros equipos, explícitalos.
2. Ordena las necesidades de mayor a menor y selecciona el prefijo mínimo que cubra cada una.
3. Asigna bloques alineados dentro del /23. No utilices una dirección cualquiera como comienzo de una /26.
4. Anota red, máscara, broadcast, primer y último host, dirección de gateway, estáticos y pool DHCP.
5. Identifica el espacio libre y propón una ampliación que no requiera renumerar los segmentos existentes.
6. Comprueba solapamientos mediante cálculo binario o una herramienta independiente. La herramienta verifica el trabajo; no sustituye a la justificación.
7. Dibuja el router y sus interfaces. Describe qué ruta necesita cada host y qué comunicaciones se permitirán entre segmentos.

### Solución razonada

Administración necesita `90 + 18 + 1 = 109` direcciones: /25, capacidad convencional 126. Aula necesita `45 + 9 + 1 = 55`: /26, capacidad 62. Taller necesita `20 + 4 + 1 = 25`: /27, capacidad 30. Servicios necesita `10 + 2 + 1 = 13`: /28, capacidad 14.

| Segmento | Red | Broadcast | Hosts | Gateway propuesto |
| --- | --- | --- | --- | --- |
| Administración | 10.44.8.0/25 | 10.44.8.127 | .1–.126 | 10.44.8.1 |
| Aula | 10.44.8.128/26 | 10.44.8.191 | .129–.190 | 10.44.8.129 |
| Taller | 10.44.8.192/27 | 10.44.8.223 | .193–.222 | 10.44.8.193 |
| Servicios | 10.44.8.224/28 | 10.44.8.239 | .225–.238 | 10.44.8.225 |

Quedan libres `10.44.8.240/28` y `10.44.9.0/24`. Son dos bloques, no una única subred /algo con límites arbitrarios. El /23 original abarca `10.44.8.0–10.44.9.255` porque su tercer octeto comienza en un límite par.

### Entregables y criterio

Presenta los cálculos, la tabla, el esquema y una matriz de acceso. Se considera esencial que no haya solapamientos, que el crecimiento esté incluido y que gateway no coincida con red, broadcast u otro equipo. Una tabla numéricamente correcta con una explicación errónea debe corregirse antes de implementarse.

## Práctica 3. Leer una conversación en una captura

**Objetivo:** reconstruir una comunicación sin atribuir a los paquetes información que no contienen.\
**Prerequisitos:** servidor y cliente del laboratorio; si no hay DNS instalado, realiza sólo ARP/ICMP y utiliza después el módulo de Servicios en red.

### Procedimiento

1. Guarda IP, rutas y vecinos antes de empezar. Comprueba si ya existe una entrada ARP para el destino.
2. Inicia una captura limitada en LAB con `arp or icmp or port 53`.
3. Ejecuta cuatro ecos ICMP al otro equipo. Si había caché de vecinos puede no aparecer ARP; explica por qué en vez de borrar indiscriminadamente toda la caché.
4. Cuando exista BIND, consulta de forma explícita `dig @192.168.56.10 www.aula.test A`.
5. Detén la captura, ábrela con Wireshark y localiza MAC origen/destino, IP origen/destino, protocolo y campos de ICMP.
6. Para DNS, relaciona pregunta y respuesta por identificador y comprueba nombre, tipo, código de respuesta y registros devueltos.
7. Realiza una segunda captura para la conexión HTTPS del módulo de Servicios. Identifica TCP y TLS; explica qué contenido no puedes leer sin material adicional autorizado.

### Resultado esperado y límites

Un destino local utiliza la MAC de ese destino. Un destino remoto utiliza la MAC del siguiente salto. El identificador ICMP no equivale a un puerto TCP. Las respuestas DNS con `NOERROR` pueden carecer de datos del tipo solicitado; `NXDOMAIN` tiene otro significado. Una negociación TLS visible no revela automáticamente el contenido HTTP cifrado.

Entrega un fichero de captura sólo con tráfico sintético, seis paquetes comentados y un diagrama temporal. No se necesita una captura enorme: se valora la relación causal entre paquetes. Si no observaste ARP, documenta la caché; no inventes una captura de una secuencia que no ocurrió.

**Reversión:** detén capturas y servicios temporales. Borra del directorio compartido cualquier captura accidental con tráfico ajeno al laboratorio.

## Práctica 4. Segmentar sin perder la capacidad de administrar

**Objetivo:** crear dos VLAN y demostrar aislamiento y acceso controlado.\
**Material:** switch administrable y router adecuados, o un simulador que implemente ambos. No basta con renombrar dos redes host-only como VLAN.

### Procedimiento

1. Usa una topología separada con VLAN 10 `10.20.10.0/24` y VLAN 20 `10.20.20.0/24`. Guarda configuración inicial y acceso de consola.
2. Asigna un puerto a un cliente de cada VLAN; configura otro puerto de la VLAN 10 en un segundo switch si está disponible.
3. Establece el trunk con una lista explícita de VLAN permitidas y acuerdo sobre tráfico sin etiqueta. Verifica estado STP.
4. Antes del router, comprueba comunicación dentro de cada VLAN y ausencia de comunicación entre VLAN.
5. Configura interfaces de gateway y rutas. Asegura que existe camino de vuelta.
6. Define una política: VLAN 10 puede consultar DNS y HTTPS del servidor en VLAN 20; SSH queda reservado a un puesto administrador de VLAN 20.
7. Prueba cada casilla de la matriz desde el origen real. Un intento denegado debe fallar por la política prevista, no porque el servicio esté apagado.
8. Reinicia de forma controlada un equipo de laboratorio y comprueba qué configuración persiste.

### Entrega

Incluye configuración relevante saneada, tabla MAC por VLAN, esquema, matriz de pruebas con hora y resultado, y procedimiento de recuperación por consola. Explica por qué LACP y STP no son intercambiables.

**Solución de referencia:** el aislamiento previo al routing se debe a dominios de enlace separados. Al habilitar routing aparece conectividad potencial que debe filtrarse expresamente. Si el trunk omite VLAN 20, el fallo estará en el enlace lógico y una regla permisiva de firewall no lo resolverá.

**Reversión:** restaura los puertos de prueba y gateways a su estado inicial desde consola, confirma acceso de administración y retira las reglas temporales.

## Rúbrica didáctica común

| Dimensión | Peso orientativo | Evidencia |
| --- | --- | --- |
| Diseño y cálculo | 25 % | Rango correcto, etiquetas, diagramas consistentes |
| Implementación | 25 % | Ajustes mínimos y persistencia comprobada |
| Verificación | 30 % | Casos positivos y negativos explicados |
| Documentación y recuperación | 20 % | Procedimiento repetible, datos saneados, rollback |

Estos porcentajes son una herramienta de autoevaluación. No sustituyen a los criterios publicados por el centro.
