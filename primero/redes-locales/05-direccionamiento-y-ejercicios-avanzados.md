# Direccionamiento avanzado: diseñar, demostrar y revisar

[Índice de Redes locales](README.md) · [Fundamentos](01-fundamentos.md) · [Laboratorio](../../docs/laboratorio.md)

## 1. Un plan de direcciones es un conjunto de decisiones

Un plan IP útil responde a más preguntas que «qué dirección tiene cada puesto». Debe explicar qué segmentos existen, por qué necesitan separación, qué capacidad se reserva, dónde se enruta, cómo se asignan las direcciones y quién registra los cambios. La tabla de direcciones no sustituye al plano de puertos ni a la política de acceso. Dos departamentos pueden compartir un prefijo y estar mal separados aunque ninguna IP se repita.

Empieza contando interfaces que realmente necesitan dirección en cada segmento: ordenadores, teléfonos, impresoras, interfaces de administración, gateways y reservas. Un equipo con dos interfaces puede consumir dos direcciones en redes distintas. Un AP puede tener dirección de gestión en una VLAN y transportar clientes de otras VLAN sin que cada SSID necesite una IP del AP en la red del usuario. Esta distinción evita sobredimensionar unas redes y olvidar dispositivos en otras.

Añade crecimiento con una hipótesis explícita. «El 25 % adicional de los 64 puestos previstos» significa reservar 16 puestos más, no elegir automáticamente una máscara concreta. Después suma infraestructura. Si el resultado queda en el límite de un prefijo, considera el coste operativo de renumerar frente al de reservar un bloque mayor. Las direcciones privadas no tienen un precio por unidad, pero el espacio desordenado complica VPN, fusión de sedes y sumarización.

## 2. Reconstruir una máscara sin memorizar tablas

Un prefijo `/n` fija los primeros n bits. Para IPv4, divide n entre ocho: cada octeto completo de red vale 255; el octeto parcial se obtiene sumando sus bits altos; los restantes valen cero. `/21` tiene dos octetos completos y cinco bits altos en el tercero: `128+64+32+16+8=248`. Por tanto la máscara es `255.255.248.0` y los bloques avanzan ocho unidades en el tercer octeto.

Para `172.22.19.200/21`, los límites cercanos del tercer octeto son 16 y 24. La red es `172.22.16.0`; su intervalo llega hasta `172.22.23.255`. El broadcast es ese último valor; el rango convencional es `172.22.16.1–172.22.23.254`. Hay `2^11=2048` direcciones y 2046 hosts convencionales. Contar sólo el último octeto daría una respuesta incorrecta porque el bloque atraviesa ocho valores del tercero.

Una comprobación alternativa convierte IP y máscara en enteros y realiza un AND para obtener la red. Es útil al programar, pero no hace falta convertir todos los octetos a binario en cada ejercicio. La técnica del salto funciona si identificas correctamente el octeto significativo y respetas los límites alineados. Después verifica el resultado por dos caminos independientes: fórmula y pertenencia del intervalo.

## 3. Caso VLSM completo de una sede

Una sede recibe `10.60.8.0/22`, que cubre `10.60.8.0–10.60.11.255`. Se necesitan 180 puestos de alumnado, 78 de administración, 43 dispositivos de taller y 18 dispositivos de gestión. Cada red necesita un gateway; las cifras de dispositivos no lo incluyen. Se propone reservar crecimiento antes de asignar:

| Segmento | Dispositivos previstos | Crecimiento supuesto | Gateway | Necesidad de hosts |
| --- | ---: | ---: | ---: | ---: |
| Alumnado | 180 | 30 | 1 | 211 |
| Administración | 78 | 12 | 1 | 91 |
| Taller | 43 | 8 | 1 | 52 |
| Gestión | 18 | 5 | 1 | 24 |

Se elige el menor prefijo convencional que contiene cada necesidad: `/24` da 254 hosts; `/25`, 126; `/26`, 62; `/27`, 30. Asigna de mayor a menor desde un límite válido:

| Segmento | Red | Primer host | Último host | Broadcast | Gateway propuesto |
| --- | --- | --- | --- | --- | --- |
| Alumnado | `10.60.8.0/24` | `10.60.8.1` | `10.60.8.254` | `10.60.8.255` | `10.60.8.1` |
| Administración | `10.60.9.0/25` | `10.60.9.1` | `10.60.9.126` | `10.60.9.127` | `10.60.9.1` |
| Taller | `10.60.9.128/26` | `10.60.9.129` | `10.60.9.190` | `10.60.9.191` | `10.60.9.129` |
| Gestión | `10.60.9.192/27` | `10.60.9.193` | `10.60.9.222` | `10.60.9.223` | `10.60.9.193` |

El gateway es una propuesta para un router que debe existir. No traslades esos gateways al laboratorio base sin router. Se han consumido 480 direcciones: 256+128+64+32. Quedan 544, descritas por `10.60.9.224/27`, `10.60.10.0/24` y `10.60.11.0/24`; los dos últimos se pueden agrupar como `10.60.10.0/23`. La reserva conserva alineación y puede alojar servicios o futuras aulas.

El consumo de bloques y la ocupación de hosts responden a preguntas diferentes. La necesidad inicial suma 378 hosts, mientras que los bloques asignados ofrecen 472 hosts convencionales y contienen 480 direcciones totales. No presentes 378/1024 como si midiera utilización de un pool DHCP: todavía no se han definido pools ni concesiones activas.

## 4. Detectar solapamientos y huecos falsos

Un plan falla si dos redes contienen alguna dirección común, aunque sus primeras direcciones escritas sean distintas. `10.60.9.0/25` y `10.60.9.64/26` se solapan porque el segundo intervalo está dentro del primero. Dos entradas de interfaz escritas como `.1/24` y `.129/25` no crean redes independientes: sus prefijos siguen solapándose.

Para revisar una tabla, normaliza cada entrada a red/prefijo, calcula límites inferior y superior y ordena por dirección. Compara el final de un intervalo con el comienzo del siguiente. Comprueba además que cada subred sea parte del bloque asignado a la sede. Una red puede no solaparse y aun así quedar fuera de la reserva autorizada.

La calculadora [subredes.py](../../scripts/subredes.py) permite contrastar un caso sin acceder a la red. Al leer la salida distingue la dirección introducida de la dirección de red normalizada. Para revisiones automatizadas de varias redes se puede utilizar `IPv4Network.overlaps()` y `subnet_of()` de `ipaddress`; documenta si el programa rechaza direcciones con bits de host o las normaliza de forma intencional.

## 5. Sumarización y selección de ruta

Una ruta resumida cubre varios prefijos mediante un prefijo menos específico. Para resumir exactamente `10.60.8.0/24` y `10.60.9.0/24`, observa que son bloques consecutivos y que el primero está alineado al tamaño de un `/23`: el resultado es `10.60.8.0/23`. Dos redes consecutivas no siempre cumplen esa alineación. `10.60.9.0/24` y `10.60.10.0/24` no constituyen un `/23` exacto.

El resumen que cubre estas últimas necesita incluir direcciones adicionales. Una ruta agregada puede ser válida por diseño si el equipo que la anuncia conoce todos los destinos o aplica un descarte controlado a los huecos; no debe anunciarse sin analizar su alcance. Un resumen incorrecto puede atraer tráfico destinado a otra sede y crear agujeros de conectividad difíciles de interpretar.

La regla de prefijo más largo sigue vigente. Si existen `10.60.8.0/22` hacia un router y `10.60.9.128/26` hacia otro, el destino `10.60.9.150` utiliza `/26` si ambas rutas son válidas y comparables en la tabla. Una métrica menor de la ruta `/22` no vence normalmente a un prefijo más específico. La preferencia administrativa y la métrica intervienen al elegir entre rutas hacia el mismo prefijo o conforme a la implementación.

No confundas sumarización con NAT. La primera representa rutas; la segunda transforma campos de direcciones y, en ciertas modalidades, puertos. También distingue una dirección de host `/32` de una interfaz de LAN: una ruta `/32` puede señalar un único destino sin que exista una subred de «menos un host».

## 6. `/31`, `/32` y por qué importa el tipo de enlace

En un enlace IPv4 punto a punto conforme a RFC 3021, un `/31` utiliza sus dos direcciones como extremos. Para `192.0.2.10/31` los extremos son `.10` y `.11`; no se restan red y broadcast como en una LAN convencional. Los equipos de ambos lados deben soportar este uso y el medio debe representar ese enlace de dos participantes. No adoptes `/31` para una VLAN de puestos con switches y múltiples equipos.

Un `/32` identifica una única dirección. Aparece en rutas de host, loopbacks lógicas o determinadas tecnologías de acceso. Su relación con un siguiente salto depende del diseño. Escribir una interfaz `/32` en un cliente Ethernet no crea por sí solo vecindad con cualquier gateway que se quiera indicar.

Estas direcciones `192.0.2.0/24` se utilizan aquí para documentación. No se configuran junto al laboratorio base como si pertenecieran a una red pública utilizable. Si construyes el ejercicio, crea una topología de dos extremos separada y conserva el estado anterior de las interfaces. La prueba debe verificar ida y vuelta y no sólo que el sistema acepte el comando de configuración.

## 7. Diseñar un esquema IPv6 legible

IPv6 separa problemas de capacidad, organización y autoconfiguración. Una LAN ordinaria que usa SLAAC se diseña normalmente con `/64`; no se reduce a `/120` porque sólo haya veinte equipos. Una sede que recibe un `/56` dispone de 256 subredes `/64`, porque quedan ocho bits de identificador de subred. La capacidad de identificar redes no es lo mismo que contar dispositivos reales.

Ejemplo documental: `2001:db8:6200:ab00::/56` permite `/64` desde `2001:db8:6200:ab00::/64` hasta `2001:db8:6200:abff::/64`. Asigna `ab10` a alumnado, `ab20` a administración, `ab30` a taller y `ab40` a gestión, conservando una tabla de significado. La relación con VLAN 10,20,30,40 es un convenio humano; los protocolos no la deducen automáticamente.

Dentro de una subred, distingue direcciones de enlace local, globales o ULA, temporales y estables. Un cliente puede tener varias direcciones válidas simultáneamente. No declares duplicación sólo por ver varias filas en `ip -6 address` o en PowerShell. Examina ámbito, estado de preferencia y método de asignación.

En un enlace interrouter específicamente diseñado puede usarse `/127` conforme a RFC 6164. Contiene dos direcciones; no existe broadcast IPv6. Eso no convierte `/127` en reemplazo de `/64` para clientes SLAAC. Para una ruta individual se utiliza `/128`. Las políticas de direcciones especiales y descubrimiento deben revisarse según la función del enlace.

## 8. Banco de problemas con solución razonada

**Problema A.** Se pide una red para 62 puestos, dos impresoras y un gateway. `/26` ofrece 62 hosts convencionales y no contiene los 65 requeridos. La solución mínima convencional es `/25`; si alguien respondió `/26` contando sólo ordenadores, el error fue de requisitos, no de aritmética.

**Problema B.** Una dirección `10.4.15.250/20` pertenece a `10.4.0.0/20`, con broadcast `10.4.15.255`. Los cuatro bits altos del tercer octeto fijan un bloque de 16. No pertenece a `10.4.15.0/20`, que no es un límite de red válido para ese prefijo.

**Problema C.** `10.4.16.0/20` y `10.4.32.0/20` son contiguas, pero no forman un `/19` exacto: los bloques `/19` comienzan en múltiplos de 32. Puede resumirse cada red por separado o diseñar una reserva alineada distinta; no basta con sumar tamaños.

**Problema D.** Dos clientes `.10/24` y `.200/25` pueden mostrar conectividad asimétrica según gateways, rutas y políticas. El primero considera local al segundo; el segundo considera `.10` fuera de su `/25`. Que una dirección sea única no valida su máscara.

**Problema E.** Un `/56` contiene 256 `/64`, un `/60` contiene 16 y un `/48` contiene 65.536. Se resta longitud de prefijos y se calcula una potencia de dos. No se resta dos por «red y broadcast» de IPv4.

**Problema F.** La cadena `2001:db8::56::10` es inválida porque comprime dos veces. La representación `2001:0db8:0000:0056:0000:0000:0000:0010` puede escribirse `2001:db8:0:56::10`. La compresión elimina grupos de ceros, no grupos arbitrarios.

## 9. Práctica avanzada: revisión de un plan ajeno

Trabaja primero sobre papel o una hoja de cálculo. Recibe cinco redes, dos pools, tres gateways y una previsión de crecimiento sintética. Introduce deliberadamente una máscara incompatible, un solapamiento y una reserva dentro del pool. No cambies las NIC del laboratorio base para demostrar errores de diseño que se pueden detectar estáticamente.

Entrega tabla normalizada, cálculo de rangos, inventario de necesidades, mapa de reservas y una decisión por cada defecto. Para contrastar utiliza la calculadora y una segunda técnica manual. Añade una prueba que distinga error de diseño de error de aplicación: si el plan es válido pero la interfaz tiene otra máscara, la corrección debe dirigirse a la configuración.

La aceptación exige ausencia de solapamientos, capacidad justificada, gateways que correspondan a equipos previstos y separación de estáticos y pools. La rúbrica didáctica asigna 30% a requisitos,30% a cálculos,20% a reservas/crecimiento y 20% a explicación de pruebas. Un plan con aritmética correcta y necesidades incompletas no obtiene la misma valoración que uno útil para operar.

## Referencias primarias

- [RFC 4632: CIDR](https://www.rfc-editor.org/rfc/rfc4632).
- [RFC 3021: enlaces IPv4 `/31`](https://www.rfc-editor.org/rfc/rfc3021).
- [RFC 4291: arquitectura de direccionamiento IPv6](https://www.rfc-editor.org/rfc/rfc4291).
- [RFC 5952: representación textual IPv6](https://www.rfc-editor.org/rfc/rfc5952).
- [RFC 6164: `/127` en enlaces interrouter](https://www.rfc-editor.org/rfc/rfc6164).
- [Python: ipaddress](https://docs.python.org/3/library/ipaddress.html).
