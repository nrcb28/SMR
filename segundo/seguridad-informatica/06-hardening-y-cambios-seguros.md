# 6. Endurecimiento y cambios de seguridad verificables

[Índice del módulo](README.md) · [Guía técnica inicial](02-guia-tecnica.md) · [Riesgos y controles](05-riesgos-bia-y-diseno-de-controles.md)

## 6.1 Una línea base es un contrato observable

El endurecimiento reduce posibilidades de uso innecesario o no autorizado, conservando la función requerida. Para decidir qué sobra, debes conocer primero la función. Una VM dedicada a SSH y HTTPS necesita una política distinta de un servidor DNS/DHCP, de Samba o de un controlador de dominio. Copiar el mismo firewall a todos puede interrumpir dependencias legítimas y producir una falsa sensación de protección.

La línea base del ejercicio registra versión de SO, paquetes, cuentas administrativas, servicios, puertos, interfaces, reglas, almacenamiento, hora y mecanismos de copia. Define qué debe poder hacer cada identidad y desde dónde. Una vez aplicada una medida, se compara el comportamiento con ese contrato; no se acepta únicamente porque un comando termine sin error.

Trabaja con un clon de Debian 13 dedicado a este capítulo. Conserva una consola del hipervisor operativa y una copia de la configuración. La NIC LAB utiliza `192.168.56.10/24`, el cliente autorizado `.20` y la NIC NAT, si existe, permanece separada. Confirma nombres reales: los ejemplos usan `ens19` para LAB y `ens18` para NAT, pero no debes asumirlos. No conectes este escenario con una red física compartida.

## 6.2 Inventario antes de reducir superficie

Recoge información local con privilegios adecuados:

```bash
cat /etc/os-release
ip -br address
ip route
sudo ss -lntup
systemctl --type=service --state=running --no-pager
systemctl list-unit-files --state=enabled --no-pager
sudo nft list ruleset
```

Un servicio ejecutándose no siempre tiene un puerto de red y un puerto puede pertenecer a una activación por socket. Examina `systemctl list-sockets` cuando corresponda. Distingue escucha en loopback, IP LAB, wildcard IPv4 e IPv6. Un listener `0.0.0.0` acepta en todas las direcciones IPv4 disponibles, sujeto a otras políticas; un listener sólo LAB reduce la exposición a esa dirección, pero no reemplaza autenticación y permisos.

Revisa paquetes y necesidad antes de desinstalar. Una dependencia puede utilizarse por una aplicación que todavía no has observado. Para una práctica, deshabilitar un servicio innecesario y comprobar su ausencia puede ser más fácil de revertir que eliminar paquetes y datos. No detengas servicios del anfitrión ni de otras asignaturas. Documenta nombre, motivo, dependencias y prueba de que la función necesaria sigue disponible.

No borres registros para conseguir una «base limpia». Sirven para comparar y diagnosticar. Puedes delimitar la sesión mediante fechas o marcadores controlados y conservar los datos sintéticos que genera la práctica. Las medidas de privacidad se basan en minimizar y controlar acceso, no en destruir evidencia de una incidencia activa.

## 6.3 Acceso administrativo y cuentas

Una cuenta administrativa de uso cotidiano aumenta el alcance de un error. Utiliza una cuenta ordinaria para tareas que no requieren privilegios y eleva sólo la operación necesaria. El acceso con `sudo` debe atribuirse a una identidad individual de laboratorio. Compartir una cuenta entre todo el grupo dificulta explicar quién realizó un cambio.

La pertenencia a un grupo administrativo no equivale a que todas las sesiones actuales tengan el mismo token o grupos efectivos. Después de modificar pertenencias, abre una sesión nueva y comprueba `id`. Para retirar acceso, distingue la cuenta, sus grupos, claves autorizadas, sesiones, tareas y servicios. Una clave que permanece en otra identidad o un servicio con credenciales propias puede conservar acceso aunque se cambie una contraseña.

Mantén un mecanismo de emergencia desde consola. Debe estar documentado y protegido, no oculto en una contraseña publicada junto a la guía. Prueba que funciona antes de restringir SSH. Una medida de seguridad que elimina el único canal de recuperación sin conocer cómo restaurarlo añade riesgo operacional.

## 6.4 SSH: configuración efectiva y prueba de identidad

La protección del acceso remoto combina verificación del servidor, autenticación del cliente, cuentas admitidas y alcance de red. Una clave pública de usuario en el servidor autoriza un método de acceso para esa cuenta; no prueba al cliente que el servidor sea el correcto. Las claves de host y su huella se verifican mediante un canal de confianza, especialmente después de reinstalar una VM.

Antes de cambiar, consulta configuración efectiva y valida el archivo:

```bash
sudo sshd -t
sudo sshd -T
systemctl status ssh --no-pager
```

`sshd -T` interpreta configuración, pero algunas condiciones `Match` dependen de usuario, host y dirección. Consulta el manual para utilizar un contexto de prueba apropiado cuando las reglas sean condicionales. Un fichero de un directorio de configuración adicional puede modificar expectativas según orden y coincidencias; identifica siempre qué archivo se aplica.

En una VM con claves ya comprobadas, una política puede limitar inicios interactivos y cuentas admitidas. No se deshabilitan métodos hasta demostrar que el alternativo funciona desde una nueva sesión. Conserva la consola y la sesión existente, valida sintaxis, recarga y abre otra sesión de prueba antes de cerrar la anterior. Si sólo compruebas una sesión que ya estaba abierta, no has validado una autenticación nueva.

El caso negativo también debe ser controlado. Utiliza una cuenta sintética no autorizada o un puerto que la política de este ejercicio no permita. No realices intentos masivos ni ataques de contraseñas. La finalidad es verificar el criterio de acceso, no generar una carga o un bloqueo involuntario de cuentas.

## 6.5 Cortafuegos: política, contexto y recuperación

El siguiente ensayo crea una tabla separada `smr_guardia` en una VM dedicada. No contiene `flush ruleset`, no reemplaza automáticamente la política persistente y no debe ejecutarse si otro gestor administra las reglas. Las cadenas de distintos gestores pueden interactuar; aceptar en una no garantiza que otra no deniegue después. Inventaría primero y elige un único responsable de la política.

Precondiciones: consola comprobada, copia de configuración, SSH/HTTPS funcionando en LAB, nombres de NIC confirmados y ninguna tabla llamada `smr_guardia`. `sudo nft list table inet smr_guardia` debe indicar que no existe; si existe, examínala y no la sobrescribas. El archivo siguiente es una plantilla para el clon y necesita adaptar ambas interfaces. El permiso de DHCP se incluye sólo si la NIC NAT realmente utiliza DHCPv4.

```nft
table inet smr_guardia {
    chain entrada {
        type filter hook input priority 0; policy drop;
        iifname "lo" accept
        ct state invalid drop
        ct state established,related accept
        ip protocol icmp accept
        meta l4proto ipv6-icmp accept
        iifname "ens18" udp sport 67 udp dport 68 accept
        iifname "ens19" ip saddr 192.168.56.20 tcp dport { 22, 443 } ct state new accept
    }
}
```

La tabla afecta a entrada local; no define política de forwarding ni una arquitectura de segmentación completa. Permite mensajes ICMP/ICMPv6 para no romper funciones de control y diagnóstico del ejercicio. Un diseño real puede limitar clases o tasas cuando corresponda, conservando funciones necesarias. Si la VM requiere DNS entrante, SMB, DHCP servidor, AD u otro servicio, esta matriz no sirve sin un rediseño explícito.

Guarda el contenido como `smr-guardia.nft` en tu usuario de laboratorio. Una validación de sintaxis no aplica reglas; la aplicación sí modifica la red:

```bash
sudo nft -c -f ./smr-guardia.nft
sudo nft -f ./smr-guardia.nft
sudo nft list table inet smr_guardia
```

Si el primer paso falla, no ejecutes el segundo. Si la política produce un efecto no previsto, desde consola retira únicamente la tabla creada por este ensayo:

```bash
sudo nft delete table inet smr_guardia
```

Ese retorno no se utiliza si la tabla ya contenía cambios ajenos al ejercicio. En ese caso se necesita restaurar de forma coordinada la política administrada. No reinicies esperando que desaparezca el problema: una configuración persistente puede volver a aplicarse y un reinicio puede interrumpir otros servicios.

## 6.6 Matriz de pruebas del firewall

| Origen y operación | Resultado esperado en este clon | Qué demuestra |
| --- | --- | --- |
| `cli01` `.20` → SSH LAB | Autenticación nueva posible con identidad autorizada | Flujo y método permitido |
| `cli01` `.20` → HTTPS LAB | TLS y contenido correctos | Servicio permitido a nivel de aplicación |
| Cliente adicional `.21` → SSH | Conexión nueva denegada por la política | Restricción de origen |
| `cli01` → SMB en este clon | No se ofrece como función de esta VM | No se está usando la política como servidor de archivos |
| VM → repositorio de actualizaciones por NAT | Funciona si red y política de salida lo permiten | Dependencia operativa conservada |
| Renovación DHCP NAT, si se utiliza | Parámetros válidos | El ensayo no rompe renovación del adaptador NAT |

El cliente adicional debe ser una VM propia del mismo laboratorio, con dirección distinta y sin suplantar a terceros. Un puerto sin listener no permite distinguir de manera suficiente qué regla lo bloquearía: la matriz debe incluir un servicio conocido para probar el filtrado. Observa contadores o captura en la interfaz pertinente y registra si la conexión falla por rechazo, timeout, TLS o autenticación.

Las conexiones establecidas antes del cambio pueden continuar por la regla de estado. Para demostrar que una nueva conexión desde un origen no autorizado se bloquea, crea una nueva sesión y no reutilices la existente. Esta diferencia explica por qué una prueba aparentemente contradictoria no obliga a eliminar la regla de seguimiento de estado.

## 6.7 Actualizaciones y compatibilidad

Una actualización reduce problemas conocidos, pero también cambia el sistema y necesita validación. Documenta versión, origen, aviso relevante, dependencia y recuperación. En Debian consulta los paquetes candidatos y el alcance propuesto por el gestor; no aceptes una eliminación inesperada de componentes de un servidor compartido sin investigar.

Después de actualizar, comprueba servicio, listener, cliente, permisos y copia. Algunos cambios requieren reinicio de un servicio o del equipo para sustituir procesos que mantienen bibliotecas anteriores. Tener un paquete nuevo en disco no demuestra que todos los procesos utilicen ese código. El procedimiento del sistema y del paquete determina cómo identificarlo.

Evita bloquear indefinidamente versiones sólo porque una práctica funcionó con ellas. La estrategia de estudio distingue versión de referencia y revisión de compatibilidad. Un entorno de pruebas permite ensayar antes del servicio principal, pero debe representar sus dependencias. Una copia del software sin los permisos o datos necesarios puede pasar una prueba superficial y fallar en el cambio real.

## 6.8 Laboratorio avanzado de endurecimiento

### Objetivo y pasos

Elige tres controles con una relación explícita con riesgos: limitar escucha web a LAB, restringir identidades administrativas y filtrar flujos nuevos. Realiza cada cambio por separado en el clon. Para cada uno guarda estado previo, explica la intención, valida sintaxis, aplica, prueba desde cliente y registra una prueba negativa.

No se pide habilitar todos los controles posibles. Se exige justificar por qué los seleccionados cumplen el contrato y cómo se recupera el servicio si se falla. Introduce un error reversible de diseño, como un nombre de interfaz distinto en una copia de la plantilla que aún no se ha aplicado, y demuestra cómo el inventario lo detecta. No necesitas provocar deliberadamente un bloqueo real de la sesión para aprender a prevenirlo.

Al finalizar, retira la tabla de ensayo si no se ha decidido convertirla en política persistente. Si se decide persistencia, se documenta una actividad distinta con archivo de arranque, gestor único y prueba tras reinicio. La existencia de reglas activas ahora no demuestra persistencia, y persistencia incorrecta puede causar un bloqueo futuro.

**Entregables:** contrato del clon, inventario, configuración antes/después, matriz, logs mínimos y retorno. **Rúbrica propia:** justificación 20 %, cambio acotado 25 %, pruebas positivas/negativas 35 % y recuperación/documentación 20 %. Una caída del acceso no se interpreta como éxito de seguridad si también impide la función autorizada.

## Referencias primarias

- [OpenSSH: manuales oficiales](https://www.openssh.com/manual.html).
- [nftables: documentación del proyecto](https://wiki.nftables.org/).
- [Debian: manual de referencia, seguridad](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html).
- [Microsoft: conceptos de mínimo privilegio en Windows](https://learn.microsoft.com/windows/security/identity-protection/access-control/access-control).
