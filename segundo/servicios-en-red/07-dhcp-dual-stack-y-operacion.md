# DHCP, doble pila y operación de direcciones

[Índice de Servicios en red](README.md) · [DHCP inicial](02-guia-tecnica.md) · [Direcciones y VLSM](../../primero/redes-locales/05-direccionamiento-y-ejercicios-avanzados.md)

## 1. Qué significa recibir una concesión correcta

Una concesión útil debe cumplir más condiciones que tener una dirección. El cliente debe estar en el segmento previsto, usar un prefijo coherente, recibir opciones adecuadas y conservar identidad y temporizadores interpretables. La dirección no debe estar duplicada, reservada para otra función o incluida en un rango que pertenece a otra red.

La asignación dinámica deja un estado distribuido: cliente, base de concesiones del servidor, posibles reservas, DNS y cachés. Reiniciar un daemon no borra necesariamente ese estado. Cuando aparece una anomalía, recoge el estado antes de renovar compulsivamente. Una renovación puede ocultar la evidencia que distingue un segundo servidor de una reserva mal definida.

El escenario sigue utilizando Kea en `.10`, interfaz LAB verificada y pool `.100–.150`. El cliente fijo `.20` conserva un camino de administración. Para observar DHCP se utiliza un clon temporal con una MAC/identidad propia, inicialmente sin IP estática LAB. No cambies la NIC NAT para seguir el ejercicio y no anuncies una puerta de enlace inexistente.

## 2. Estado del cliente y lectura de DORA

DISCOVER busca servidores disponibles; OFFER propone parámetros; REQUEST expresa una solicitud y selección según estado; ACK confirma la concesión aceptada. El esquema DORA enseña un caso inicial, pero no toda operación DHCP consiste en cuatro paquetes. Un cliente que conserva estado puede intentar reutilizarlo o renovar sin repetir el descubrimiento completo.

En una captura identifica transacción, identificadores, dirección ofertada, servidor elegido y opciones. No correlaciones mensajes sólo por proximidad temporal si hay varios clientes. Una MAC visible puede no ser el único identificador utilizado por el servidor; las opciones de identificador de cliente influyen en cómo se reconoce el estado.

La distinción broadcast/unicast cambia según fase y capacidades. Un REQUEST inicial puede informar qué servidor eligió el cliente; una renovación suele dirigirse al servidor que otorgó la concesión. Si ese servidor no responde y se alcanza la fase de rebind, el alcance cambia. Examina el estado concreto antes de declarar que un paquete «se envió mal» por no coincidir con un diagrama simplificado.

Un NAK indica rechazo a la configuración que se intenta usar en ese contexto y desencadena acciones del cliente. No es equivalente a que el servidor esté caído. Un DECLINE puede informar de un conflicto detectado; antes de limpiar estados verifica qué equipo utiliza la dirección y por qué entró en el rango.

## 3. Temporizadores T1, T2 y expiración

T1 marca cuándo el cliente intenta renovar y T2 cuándo pasa a la fase de rebind si no lo logró. La duración válida limita hasta cuándo puede utilizar la concesión bajo las reglas del protocolo. Debe cumplirse una relación coherente entre temporizadores y vida de concesión; no uses T1 posterior al vencimiento como si fuera un intervalo de sondeo.

Ejemplo didáctico con concesión de 3600 s: T1=1800 y T2=3150. El cliente intenta renovación aproximadamente a los 30 minutos; si no obtiene respuesta, alcanza rebind a los 52 minutos 30 segundos; el vencimiento ocurre a los 60 minutos desde el momento pertinente del estado. No sumes T1+T2 como si fueran dos duraciones consecutivas: ambos se expresan respecto al origen temporal de la concesión.

Si no se proporcionan valores explícitos, el comportamiento predeterminado se interpreta según protocolo y cliente. Kea permite especificar `renew-timer`, `rebind-timer` o calcular porcentajes con `calculate-tee-times` y parámetros relacionados. Elige un método y explica sus valores efectivos; no mantengas dos conjuntos contradictorios esperando que el lector adivine cuál prevalece.

Fragmento para **integrar dentro del objeto `Dhcp4` existente**, después de copia previa y revisión del manual de la versión:

```json
{
  "valid-lifetime": 3600,
  "renew-timer": 1800,
  "rebind-timer": 3150,
  "calculate-tee-times": false
}
```

Este fragmento no es una configuración completa ni se pega como segundo objeto raíz. Valida la configuración final con `kea-dhcp4 -t` y el archivo real antes de recargar o reiniciar según el procedimiento del paquete. La prueba debe registrar las opciones efectivas y el tiempo observado; no basta con mostrar el texto del archivo.

## 4. Reservas, estáticos y nombres

Una reserva vincula un identificador y parámetros en el servidor. Una IP estática se configura en el cliente. Son estrategias distintas y pueden coexistir si el plan evita colisiones. La reserva no garantiza ausencia de duplicados si otro equipo tiene la misma IP escrita a mano o si el identificador elegido no es el que presenta el cliente.

En el diseño inicial, la reserva `.50` queda fuera del pool dinámico y dentro de la subred. No se afirma que toda implementación o política impida reservas dentro de pools; se escoge esta organización para facilitar revisión. Documenta capacidades de la versión Kea, mecanismos de reserva y comprobación de identificadores antes de modificar su comportamiento.

Un nombre configurado en una reserva no crea automáticamente un registro en BIND. DDNS requiere un flujo de actualizaciones, permisos y tratamiento de errores expresos. En un laboratorio con zonas estáticas, registra manualmente los nombres que deban existir y no prometas sincronización que no has configurado. Un cliente puede obtener IP y seguir sin resolver su propio nombre.

La aleatorización de MAC en redes inalámbricas puede cambiar la identidad percibida de un dispositivo. No la desactives globalmente sólo para facilitar un inventario sin analizar privacidad y política. Elige identificadores y procedimientos compatibles con los dispositivos y el objetivo del servicio, y explica las limitaciones de reservas basadas en una característica mutable.

## 5. Pools, ocupación y capacidad operativa

El rango `.100–.150` contiene 51 direcciones, incluyendo ambos extremos. Si hay 46 concesiones activas y cinco direcciones libres, la ocupación respecto al pool es 46/51≈90,2%. No uses el tamaño de todo `/24` para presentar esa cifra: el servicio sólo distribuye el rango configurado. Tampoco sumes automáticamente concesiones antiguas expiradas como si siguieran ocupando capacidad válida.

Relaciona duración de concesiones con movilidad. Periodos largos reducen ciertos intercambios y pueden mantener capacidad ocupada por clientes que ya se marcharon; periodos cortos aumentan trabajo y dependencia de disponibilidad del servidor. La opción correcta depende de tasas de llegada/salida, parque y tolerancia a fallos. No se decide sólo por el deseo de ver un ACK más a menudo.

Una alerta de capacidad debe incluir umbral, ventana, tendencia y acción. «Pool al 90%» sin contexto no indica si falta ampliar una red o depurar un diseño erróneo. Si la red está llena de equipos esperados, añadir direcciones fuera de la subred no es una solución; revisa direccionamiento, rangos y capacidad del segmento. Si hay muchas identidades inesperadas, estudia su origen antes de borrar concesiones.

Kea puede conservar concesiones en un backend memfile o en otros backends compatibles según edición/configuración. Copiar un archivo mientras cambia puede no representar el estado que esperas. Para la práctica de recuperación sigue el procedimiento consistente de la versión y evita editar a mano archivos activos para forzar una dirección. Conservar una copia de configuración sin concesiones puede provocar problemas al restaurar si no se analiza el estado de clientes.

## 6. Segundo servidor y relay: dos causas diferentes

Si un cliente recibe ofertas de dos servidores no previstos, la selección puede producir DNS o parámetros distintos entre sesiones. Observa la opción de identificador del servidor y la interfaz por la que llegan ofertas. En host-only, el servicio incorporado del hipervisor es una causa frecuente que debe descartarse. Apaga sólo el DHCP de LAB, sin desactivar el de NAT que da acceso a repositorios.

Un relay permite transportar intercambios entre clientes de una subred y un servidor en otra, aportando contexto para seleccionar el ámbito. No es necesario en el segmento base donde cliente y Kea están en el mismo enlace. Añadir un relay para «arreglar» ese escenario sin diagnosticar introduce complejidad y puede duplicar respuestas.

Para aprender relay crea un diseño enrutado separado, con subredes, interfaces, servidor y políticas documentadas. El servidor debe conocer qué subred atiende y el camino de vuelta. No añadas la opción `routers` a todos los clientes apuntando a `.1` si ese router no existe. La prueba de aceptación debe observar el relay, el ámbito seleccionado y la comunicación posterior del cliente.

DHCP snooping, cuando el switch lo soporte, puede restringir por dónde se aceptan respuestas del servidor. Sus puertos de confianza y base de vinculaciones deben ajustarse al mapa real. Marcar todos los puertos como confiables para que «deje de fallar» anula la protección; marcar el uplink erróneo puede impedir la asignación a todo un segmento.

## 7. Doble pila: separar funciones IPv6

DHCPv6 no es DHCPv4 con direcciones más largas. Los mecanismos de descubrimiento de router y autoconfiguración se distribuyen de otra forma. El host aprende normalmente routers mediante RA; SLAAC puede construir direcciones con los prefijos anunciados; DHCPv6 puede asignar direcciones o proporcionar parámetros según modo y soporte.

Los indicadores de RA orientan ciertos comportamientos, pero el resultado depende del sistema cliente. No prometas que todos los teléfonos utilizarán DHCPv6 con estado porque un router tenga una casilla activada. Incluye una matriz de clientes y observa dirección, ruta por defecto y DNS efectivos. Las direcciones temporales pueden coexistir con otras; su aparición no significa necesariamente un fallo de concesión.

Las identidades DHCPv6 se basan en DUID y otros campos relevantes; no sustituyas mecánicamente una reserva MAC por el mismo texto dentro de una configuración DHCPv6. Una imagen clonada puede conservar identificadores y provocar colisiones operativas. La preparación de clones incluye identidad de SO y cliente, además de MAC virtual.

Si se amplía Kea a IPv6, identifica paquete/unidad correspondiente y prepara un archivo independiente con su sintaxis de versión. Un demonio DHCPv4 activo no demuestra que exista DHCPv6. La escucha, reglas, prefijos y pruebas deben incluir IPv6 expresamente. Este capítulo desarrolla diseño y observación; no habilita RA/DHCPv6 en la red física.

## 8. Diagnóstico comparado de tres clientes

**Cliente A:** no tiene dirección esperada y aparece enlace local IPv4. Comprueba enlace, NIC correcta, estado DHCP, ofertas y alcance del pool. No empieces por reiniciar DNS: todavía no se ha completado la asignación prevista.

**Cliente B:** tiene `.120/24`, no resuelve nombres y llega a `.10`. Consulta opciones DNS y realiza una consulta directa a BIND. Si el BIND del escenario sólo es autoritativo y no recursivo, esperar resolución de Internet por él es un error de diseño, no necesariamente una avería.

**Cliente C:** conserva IP durante un fallo del servidor y sigue comunicándose localmente. Eso puede ser correcto mientras la concesión siga válida y el enlace funcione. Registra T1/T2/vencimiento antes de concluir que el servidor «sigue respondiendo» sin capturar ningún ACK.

En los tres casos conserva eventos, configuración efectiva y datos de transacción. Los nombres de opciones en interfaces gráficas cambian; el protocolo y la evidencia ayudan a comparar sistemas sin depender de una captura de menú concreto.

## 9. Práctica avanzada: cronología y agotamiento simulado

Usa un clon desechable y un pool pequeño separado de una práctica, dentro de la misma subred y fuera de estáticos/reservas. No realices agotamiento mediante clientes masivos ni tráfico contra redes ajenas. La capacidad se estudia con dos o tres VM propias o mediante un conjunto sintético de concesiones interpretado sobre papel.

Primero registra una asignación limpia con temporizadores moderados adecuados al tiempo de clase, coherentes entre sí. Después detén Kea en una ventana prevista y observa qué hace el cliente al renovar, sin esperar pérdida instantánea. Restaura el servidor y comprueba renovación y permanencia de parámetros. No reduzcas temporizadores en el servicio de una organización para terminar antes la sesión.

Entrega línea temporal, identificadores, opciones, estado de concesiones, prueba de ausencia de segundo servidor y tabla de capacidad. Añade recuperación del cliente a su estado anterior y de Kea al pool base. La rúbrica propia valora 25% aislamiento/plan,25% lectura del protocolo,25% evidencia temporal y 25% diagnóstico/cierre.

## Vigencia del protocolo y referencias primarias

En la revisión de noviembre de 2026, [RFC 9915](https://www.rfc-editor.org/rfc/rfc9915) es la especificación DHCPv6 que sustituye a RFC 8415. Entre sus cambios retira la asignación temporal mediante IA_TA y la capacidad Server Unicast del protocolo anterior. Esto no equivale a retirar las direcciones temporales creadas por otros mecanismos IPv6. Los manuales o implementaciones que todavía citan RFC 8415 se interpretan según su versión y soporte; no se habilitan opciones antiguas sólo por encontrarlas en una receta.

- [Kea ARM: servidor DHCPv4](https://kea.readthedocs.io/en/stable/arm/dhcp4-srv.html).
- [Kea ARM: servidor DHCPv6](https://kea.readthedocs.io/en/stable/arm/dhcp6-srv.html).
- [RFC 2131:DHCPv4](https://www.rfc-editor.org/rfc/rfc2131).
- [RFC 2132:opciones DHCP](https://www.rfc-editor.org/rfc/rfc2132).
- [RFC 9915: DHCPv6, especificación vigente de referencia](https://www.rfc-editor.org/rfc/rfc9915).
- [RFC 8415: especificación anterior, para contraste de implementaciones](https://www.rfc-editor.org/rfc/rfc8415).
- [RFC 4861:RA ydescubrimiento de vecinos](https://www.rfc-editor.org/rfc/rfc4861).
- [RFC 4862:SLAAC](https://www.rfc-editor.org/rfc/rfc4862).
