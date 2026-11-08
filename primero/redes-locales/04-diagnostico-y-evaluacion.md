# Diagnóstico, ejercicios y autoevaluación

## 1. Método de resolución de incidencias

Una incidencia debe formularse como una observación comprobable: «desde cli01, el puerto 443 de 192.168.56.10 no responde desde las 10:15» aporta más información que «la red va mal». Identifica alcance, momento de inicio, cambios recientes y quién resulta afectado.

Sigue un ciclo pequeño: reúne estado; plantea una hipótesis; elige una prueba que la confirme o descarte; realiza un solo cambio; verifica la recuperación y efectos secundarios. Guarda valores anteriores. Cambiar IP, DNS, cable y firewall a la vez puede recuperar el servicio, pero impide saber qué fallaba y dificulta volver atrás.

El orden de capas es una guía, no una obligación mecánica. Si varios equipos de distintas redes acceden a una aplicación salvo un usuario, empieza por las diferencias de ese usuario. Si todo un switch perdió enlace después de mover el armario, la alimentación y los uplinks merecen prioridad.

| Síntoma | Hipótesis | Prueba útil | Interpretación prudente |
| --- | --- | --- | --- |
| Interfaz sin enlace | Cable, puerto, NIC o VM desconectada | LEDs, estado de enlace, cable conocido | No cambies DNS todavía |
| IPv4 169.254.x.x inesperada | No se obtuvo DHCP | Captura de Discover/Offer y concesiones | Puede existir política local explícita |
| Misma subred, vecino incompleto | VLAN, enlace, IP destino o filtro ARP | Vecinos, tabla MAC, captura en ambos extremos | Una ruta por defecto no arregla el enlace local |
| IP funciona y nombre no | Resolución o nombre equivocado | Consulta DNS explícita al servidor previsto | No prueba que el navegador use ese mismo resolver |
| IP intermitente, MAC cambia | Posible duplicidad o alta disponibilidad | Correlación de ARP, inventario y diseño | Un cambio MAC no siempre es malicioso |
| Archivos grandes fallan | MTU, pérdida o aplicación | Tamaños, capturas, mensajes ICMP | Un ping pequeño resulta insuficiente |
| Un VLAN no cruza switches | Lista trunk o pertenencia | Tabla VLAN y trunk en ambos extremos | No basta con que el enlace físico esté arriba |
| Lentitud bajo carga | Saturación, colas, CPU o Wi-Fi | Utilización, pérdida, CPU y medición controlada | No atribuyas todo al ancho de banda contratado |

## 2. Casos desarrollados

### Caso A: máscara equivocada

El cliente tiene `192.168.56.20/16` y debe alcanzar `192.168.80.10` a través de un router. Con /16, interpreta ese destino como local e intenta resolverlo por ARP. Aunque exista una ruta por defecto, gana la ruta conectada /16 por ser más específica.

La prueba decisiva es consultar la ruta que se selecciona y capturar ARP. La corrección consiste en aplicar el prefijo del diseño, no en crear una entrada ARP permanente ni borrar la ruta por defecto. Después hay que verificar destino local, remoto y persistencia.

### Caso B: dos puertas de enlace

Una VM tiene LAB y NAT, y se añadió erróneamente una puerta de enlace a LAB. Algunos destinos salen por la interfaz equivocada dependiendo de métricas y rutas. La aplicación puede fallar de forma aparentemente variable.

Registra ambas tablas y usa `ip route get` para varios destinos. Elimina únicamente la ruta por defecto añadida a LAB mediante el gestor correspondiente. Comprueba que la red LAB sigue directamente conectada y que Internet utiliza NAT. No elimines todas las rutas ni desactives el adaptador necesario para los servicios.

### Caso C: ARP correcto, HTTPS inaccesible

El vecino se resuelve y ping responde, pero TCP/443 falla. La conectividad de enlace y parte de IP funcionan. Revisa si hay proceso escuchando en la dirección LAB, firewall, ruta de respuesta y puerto exacto. Si TCP se establece pero TLS falla, cambia la hipótesis hacia certificado, nombre, reloj o protocolo.

Esta separación evita «arreglar la red» cambiando una IP cuando el problema es que Nginx sólo escucha en loopback o presenta un certificado para otro nombre.

### Caso D: Wi-Fi con señal alta y bajo rendimiento

El cliente muestra buena intensidad de señal pero la tasa útil cae por la tarde. Revisa ocupación de canal, número de clientes, ancho de canal, retransmisiones y enlace cableado del AP. Repite medición con cable y en horas de baja carga.

Cambiar todos los AP a máxima potencia puede aumentar interferencia y crear enlaces asimétricos: el cliente oye al AP, pero su radio no puede responder con la misma potencia. El ajuste requiere medición del entorno.

## 3. Ejercicios con solución razonada

**1. ¿Pertenecen 192.168.10.30/27 y 192.168.10.40/27 a la misma subred?**\
No. /27 divide en bloques de 32: el primer host está en `.0–.31` y el segundo en `.32–.63`. Para comunicarse necesitan routing y gateways adecuados, aunque compartan físicamente un switch.

**2. Una red tiene 62 ordenadores y necesita router. ¿Basta /26?**\
No bajo el modelo convencional: /26 aporta 62 direcciones de host y el router consume una adicional. Haría falta /25 o un rediseño. El recuento debe incluir todos los equipos con IP.

**3. ¿Qué MAC usa un cliente cuando conecta a un servidor situado en otra red?**\
La del siguiente salto del enlace local. La IP de destino continúa siendo la del servidor si no interviene NAT; la MAC del servidor remoto no se resuelve mediante ARP a través de routers.

**4. Un switch no conoce una MAC destino. ¿Descarta siempre la trama?**\
No. Normalmente hace flooding dentro de la VLAN por los puertos adecuados salvo el de entrada, sujeto a políticas y estado STP. Aprenderá a partir de las MAC origen de tramas recibidas.

**5. ¿Qué corrige STP?**\
Elimina lógicamente bucles de capa 2 manteniendo una topología sin ciclos activos. No calcula rutas IP ni cifra el tráfico. Su funcionamiento depende de la configuración y de las variantes implementadas.

**6. ¿Conectar dos cables duplica siempre la velocidad?**\
No. Sin agregación coordinada puede crear un bucle; con LACP ofrece capacidad agregada repartida entre flujos y redundancia, pero una sola conversación puede seguir limitada a un enlace.

**7. ¿Se puede tener conectividad IPv6 sin DHCPv6?**\
Sí. Se pueden configurar direcciones estáticas o usar SLAAC, según el diseño. El descubrimiento del router se basa normalmente en RA. La ausencia de DHCPv6 no equivale a ausencia de IPv6.

**8. ¿Un firewall que bloquea todo ICMPv6 deja una red segura y funcional?**\
Puede romper funciones esenciales. Debe permitirse el tráfico de control necesario con una política razonada, además de filtrar los servicios. «Bloquear ICMP» no expresa una política IPv6 correcta.

**9. ¿Por qué una captura no muestra contraseñas dentro de HTTPS?**\
Porque TLS cifra el contenido de aplicación. Pueden observarse metadatos y partes de la negociación, con diferencias según protocolo y opciones. No debe prometerse visibilidad completa ni extraerse claves de sesiones ajenas.

**10. ¿Qué significa que el puerto del switch negocie a 1 Gb/s?**\
Que se acordó una tasa física de enlace bajo ciertas condiciones. No demuestra rendimiento útil de aplicaciones, ausencia de pérdida, certificación del cableado ni capacidad de todo el camino.

**11. ¿Por qué aparece un checksum TCP incorrecto sólo en la captura del emisor?**\
Puede deberse a checksum offloading: la captura se produce antes de que la NIC finalice el campo. Debe comprobarse en el receptor y correlacionarse con fallos reales antes de diagnosticar corrupción.

**12. ¿Una VLAN equivale a una regla de firewall?**\
No. Define separación en enlace. Cuando existe routing, las políticas de paso entre subredes deben configurarse en el dispositivo correspondiente.

## 4. Modelo de parte técnico

Usa esta estructura para documentar una incidencia:

1. Identificador, fecha, responsable y alcance.
2. Síntoma reproducible, dirección de origen, destino, protocolo y puerto.
3. Topología y estado inicial: direcciones, rutas, VLAN y cambios recientes.
4. Hipótesis ordenadas y evidencia de cada prueba.
5. Cambio aplicado con valor anterior y procedimiento de reversión.
6. Verificación del servicio y de casos que deben seguir bloqueados.
7. Causa confirmada, incertidumbre pendiente y medida preventiva.

Evita guardar inventarios reales con datos personales o diagramas sensibles en un repositorio público. Un caso didáctico puede conservar el método usando nombres y direcciones sintéticos.

## 5. Lista de autoevaluación

Puedes considerar dominada una práctica cuando explicas cada dirección, identificas la ruta utilizada, distingues un fallo de enlace de uno de aplicación y demuestras el resultado desde el cliente. Si dependes de desactivar todo el firewall o de reiniciar repetidamente sin hipótesis, vuelve a recopilar evidencias.

Para la defensa oral, cambia una condición: máscara, VLAN, destino o estado de DNS. Predice primero qué ocurrirá y después compruébalo. Aprender a predecir y contrastar es más útil que memorizar una captura aislada.
