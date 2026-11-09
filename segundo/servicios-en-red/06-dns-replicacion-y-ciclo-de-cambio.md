# DNS avanzado: réplicas, delegación y cambios verificables

[Índice de Servicios en red](README.md) · [Despliegue inicial](02-guia-tecnica.md) · [Laboratorio común](../../docs/laboratorio.md)

## 1. Qué añade una segunda autoridad

Una segunda instancia autoritativa conserva una copia de una zona y puede contestar aunque la primera no esté disponible. No convierte automáticamente el sistema en un resolver de Internet, no elimina errores de datos y no sustituye una copia histórica. Si el administrador publica una dirección incorrecta y aumenta el serial, la réplica puede distribuir fielmente ese error.

Este capítulo extiende el escenario BIND del módulo mediante una VM nueva, `ns2`, en `192.168.56.30/24`. No utiliza `.11`, reservada al escenario de directorio. Mantén LAB aislada y sin gateway; NAT, si existe, sirve sólo para instalar paquetes. La VM de `srv01/.10` actúa como primaria; `.30`, como secundaria. No mezcles este ejercicio con un controlador AD que ya ocupe DNS.

Dibuja tres caminos: consultas de clientes, notificaciones y transferencias. Las consultas ordinarias pueden usar UDP o TCP; las transferencias tradicionales de zona requieren TCP. Una regla que permite sólo UDP53 puede dejar consultas pequeñas funcionando y romper réplica o respuestas que requieren TCP. La política debe autorizar exactamente los participantes del laboratorio.

## 2. Serial, SOA y conservación de coherencia

El serial identifica una versión lógica de zona dentro de la aritmética definida por el protocolo. El convenio `AAAAMMDDnn` facilita operación humana, pero no es obligatorio. Aumenta el serial al cambiar datos y registra qué modificación representa. Editar un A sin cambiar el serial puede mantener al secundario con datos anteriores aunque la primaria haya recargado el archivo.

Los temporizadores SOA tienen funciones distintas. `refresh` orienta cada cuánto se comprueba la versión; `retry` trata intentos posteriores a un fallo; `expire` limita cuánto tiempo puede conservarse la zona secundaria sin poder refrescarla; el último campo participa en el almacenamiento negativo conforme a las reglas correspondientes. No llames «TTL de toda la zona» a cualquier número del SOA.

Un ejemplo de fallo: la primaria deja de estar disponible y la secundaria sigue sirviendo la última versión. Esa continuidad es esperable hasta las condiciones de expiración. Aumentar `expire` permite sobrevivir más tiempo sin primaria y también conservar más tiempo datos que podrían quedar obsoletos. La decisión debe relacionar continuidad, frecuencia de cambios y procedimiento de recuperación.

RFC 1982 define comparación de seriales con límites que no son una comparación ilimitada de enteros decimales. Para el aprendizaje ordinario basta incrementar de forma controlada; si se ha publicado un valor equivocado, no reduzcas después el número de forma improvisada esperando que todos acepten la zona. Sigue el procedimiento documentado del servidor y verifica ambas autoridades.

## 3. TSIG: autenticar el intercambio entre servidores

TSIG añade autenticación e integridad a mensajes DNS mediante una clave compartida. No cifra automáticamente el contenido de una transferencia. Un observador del enlace podría ver datos aunque no pueda producir una firma válida. Para requisitos de confidencialidad se debe diseñar además un transporte protegido o una red confiable con controles apropiados.

Genera una clave exclusiva para esta pareja y su propósito. No reutilices una clave de actualizaciones dinámicas como si todas las autorizaciones fueran iguales. En la primaria, con BIND y sus herramientas ya instalados, prepara un directorio accesible por el daemon y restringido para otros usuarios:

```bash
sudo install -d -o root -g bind -m 0750 /etc/bind/keys
sudo sh -c 'umask 027; set -C; tsig-keygen -a hmac-sha256 smr-transfer > /etc/bind/keys/smr-transfer.key'
sudo chown root:bind /etc/bind/keys/smr-transfer.key
sudo chmod 0640 /etc/bind/keys/smr-transfer.key
```

Comprueba antes que el archivo no exista; si existe, inspecciona su función sin publicarlo y no sobrescribas una clave activa. `set -C` evita reemplazar un archivo existente mediante esa redirección. La salida contiene un secreto. Transfiere ese archivo a la secundaria por un canal autenticado cuyo host hayas verificado; conserva el mismo propietario/grupo/permisos adecuados allí. No lo subas a Git ni lo pegues en la memoria pública.

La política propuesta autoriza transferencias mediante la clave y limita adicionalmente por firewall el origen a `.30` en la primaria. No interpretes `allow-transfer { 192.168.56.30; key "smr-transfer"; };` como un AND obligatorio: las listas de coincidencia tienen una semántica que debe entenderse. Una regla mal construida podría permitir por IP sin exigir la clave. Aquí se exige la clave en la aplicación y se controla IP por separado.

## 4. Configuración de la primaria

Conserva copia de los archivos anteriores. Añade una inclusión del archivo secreto en el contexto superior de configuración, por ejemplo en `named.conf.local`, antes de utilizar su nombre:

```text
include "/etc/bind/keys/smr-transfer.key";

zone "aula.test" {
    type primary;
    file "/etc/bind/db.aula.test";
    allow-transfer { key "smr-transfer"; };
    also-notify { 192.168.56.30 key "smr-transfer"; };
};
```

Sustituye la definición previa de esa zona; no declares dos veces `aula.test`. La zona inversa puede replicarse con el mismo patrón y una decisión documentada de alcance de clave. Para centrar el primer ejercicio, replica sólo la directa y deja la inversa en la arquitectura original hasta completar aceptación.

Añade a los datos de zona un NS para `ns2.aula.test.` y un A `ns2` hacia `.30`, aumenta serial y valida. El segundo NS describe otra autoridad para la misma zona; no es una delegación de subdominio. La política global original `allow-transfer { none; };` puede mantenerse como denegación por defecto para zonas que no se amplíen; la regla de la zona controla ésta específicamente.

Comprueba `named-checkconf`, `named-checkzone` y carga de zonas antes de recargar. Mantén la escucha y las ACL de consultas limitadas a LAB/loopback como en la guía inicial. El intercambio entre autoridades no requiere abrir recursión a todo el mundo. Después revisa registros y consulta el SOA directamente a `.10`.

## 5. Configuración de la secundaria

Instala BIND y herramientas en `ns2` con la misma preparación de red aislada. Configura escucha en loopback y `.30`, consultas limitadas a LAB, recursión desactivada y transferencias descendentes denegadas. El servicio necesita escribir el archivo secundario; se utiliza una ubicación prevista para ello en el paquete Debian:

```text
include "/etc/bind/keys/smr-transfer.key";

zone "aula.test" {
    type secondary;
    primaries { 192.168.56.10 key "smr-transfer"; };
    file "/var/cache/bind/sec.aula.test";
    allow-notify { key "smr-transfer"; };
    allow-transfer { none; };
};
```

No crees manualmente una zona primaria vacía en la secundaria. Su copia procede de la transferencia. No edites el archivo recibido como mecanismo ordinario de mantenimiento: puede regenerarse y representa datos administrados por la primaria. Los permisos y AppArmor del paquete deben permitir al proceso escribir en la ubicación elegida; si se usa otro directorio hay que revisar ambos mecanismos.

`allow-notify` amplía los remitentes de NOTIFY aceptables; no restringe los que ya admite `primaries`. Por tanto, la línea con la clave no significa «IP de la primaria Y TSIG» para todos los mensajes de notificación. El NOTIFY firmado de `also-notify`, la transferencia autenticada y las reglas de red son controles distintos que deben comprobarse. Una notificación recibida no autoriza por sí sola a sustituir datos de zona: la secundaria consulta las primarias configuradas para obtenerlos. Consulta la [semántica de `allow-notify` en BIND](https://bind9.readthedocs.io/en/stable/reference.html#namedconf-statement-allow-notify) antes de adaptar la política.

Valida configuración y reinicia sólo después de que pase. La primera transferencia puede tardar y se diagnostica con journal y consultas. Comprueba que el reloj no esté desviado de forma anormal; TSIG tiene controles temporales y un secreto correcto no compensa un problema de tiempo. Confronta errores concretos antes de regenerar claves.

## 6. Pruebas positivas y negativas

```bash
dig @192.168.56.10 aula.test SOA +norecurse
dig @192.168.56.30 aula.test SOA +norecurse
dig @192.168.56.30 srv01.aula.test A +norecurse
dig @192.168.56.10 aula.test AXFR
```

Las tres primeras consultas deben mostrar datos coherentes y autoridad según su contexto. Ejecuta la última desde `ns2`, cuyo origen `.30` admite la política de red, pero sin proporcionar clave: BIND debe denegar la transferencia. Así distingues rechazo de autorización en la aplicación de un timeout por firewall desde otro origen. Para probar autorización con clave utiliza `dig -k` sobre el archivo secreto local protegido, no `-y` con el secreto incrustado en la línea de comandos. Esta prueba sólo se ejecuta desde el participante autorizado y se conserva fuera de una salida pública.

Publica un registro sintético `revision.aula.test` hacia una dirección de laboratorio que tenga sentido para el ejercicio, aumenta serial, valida y recarga primaria. Consulta SOA y registro en ambas. Registra instante del cambio, notificación, transferencia y primera respuesta nueva. Si los seriales difieren, no copies archivos manualmente como primer arreglo: revisa conectividad TCP 53, clave, serial y permisos.

Para continuidad detén temporalmente `named` únicamente en `.10` desde consola, después de verificar `.30`. Consulta directamente a la secundaria. No afirmes que todos los clientes han cambiado automáticamente de DNS: el comportamiento depende de su configuración de resolutores, caché y aplicación. Restaura la primaria y comprueba que las autoridades vuelvan a estar coherentes.

## 7. TTL, caché negativa y planificación de cambios

TTL no es un temporizador de propagación universal. Cada caché tiene un tiempo restante desde que obtuvo el dato; los clientes pueden consultar resolutores distintos y las aplicaciones mantener su propia caché. Reducir hoy un TTL no modifica retroactivamente una copia que ayer se almacenó con un valor mayor.

Ejemplo: un registro tenía TTL 3600 y un resolver lo guardó a las 09:00. A las 09:20 publicas TTL 300 junto al mismo dato. El resolver todavía puede conservar la copia anterior hasta las 10:00 conforme al valor que recibió. Una estrategia consiste en reducir con antelación suficiente, esperar el vencimiento anterior y hacer después el cambio, con un plan de retorno que tenga en cuenta el mismo efecto.

La respuesta negativa también puede almacenarse. Si se consulta antes de crear un nombre, la caché puede seguir respondiendo inexistencia durante su tiempo permitido aunque la autoridad ya contenga el A. Por eso conviene crear previamente nombres o planificar la prueba, y distinguir consulta directa a autoridad de consulta al resolver usado por la aplicación.

Un cambio de web con TTL 300 no garantiza recuperación en cinco minutos si la base de datos o certificados no están preparados. DNS es una dependencia del cambio completo. Relaciona registros, certificados, contenido, accesos y pruebas desde cliente, y conserva el servicio anterior el tiempo que requiera la transición planificada.

## 8. Delegación y separación de responsabilidades

Delegar `taller.aula.test` significa que la zona padre publica qué servidores son autoridades de esa zona hija. El padre y la hija mantienen datos distintos alrededor del corte. Un nombre como `ns.taller.aula.test` puede requerir glue en el padre para romper la dependencia de resolución cuando corresponde. Los registros necesarios deben planificarse, no copiarse por intuición.

Un CNAME crea un alias y no delega una zona. Un NS en el ápice de `aula.test` enumera autoridades de esa misma zona. Una configuración de forwarding de un resolver tampoco equivale a una delegación pública. Estos mecanismos pueden coexistir, pero responden a problemas de administración y resolución diferentes.

Para practicar delegación utiliza otra VM o instancia separada, con nombre y dirección documentados y sin ocupar los roles del escenario anterior. Si no hay recursos, resuelve la secuencia con un diagrama de consultas y zonas sintéticas. No declares ejecutada una delegación porque el nombre respondió mediante una entrada de `hosts` o una zona local añadida al cliente.

DNSSEC valida el origen de datos mediante firmas y una cadena de confianza; TSIG autentica intercambios entre participantes que comparten una clave. Activar uno no activa el otro. Una firma válida tampoco indica que una dirección sea la correcta para el negocio: puede autenticar un dato publicado por error por el administrador autorizado.

## 9. Práctica avanzada y diagnóstico

Entrega diseño de las dos autoridades, mapa de archivos públicos/secretos, versiones, ACL de consultas, política de transferencia, pruebas de seriales y secuencia de un cambio. Añade rechazo sin clave y continuidad con primaria detenida, así como recuperación. La rúbrica propia reparte 25% diseño/control de acceso,25% configuración,30% pruebas y 20% operación/cierre.

**REFUSED en AXFR sin clave:** resultado esperado. **BADSIG:** revisar identidad de clave, algoritmo y secreto sin publicarlo. **BADTIME:** contrastar reloj y sincronización. **Serial igual con datos distintos:** investigar modificación sin incremento, servidor consultado y carga real. **Permiso denegado en archivo secundario:** revisar usuario del servicio, ruta, permisos y AppArmor, sin convertir el directorio en escritura global.

Si debes volver atrás, conserva versiones y seriales publicados, restaura datos mediante un nuevo cambio controlado y verifica ambas autoridades. Retirar la secundaria exige revisar NS, clientes y cualquier referencia de operación; no apagues simplemente la VM dejando una autoridad anunciada que nadie mantiene.

## Referencias primarias

- [BIND ARM: configuración](https://bind9.readthedocs.io/en/stable/reference.html).
- [BIND ARM: configuraciones de seguridad](https://bind9.readthedocs.io/en/stable/chapter7.html).
- [RFC 1982: seriales DNS](https://www.rfc-editor.org/rfc/rfc1982).
- [RFC 2308: caché negativa](https://www.rfc-editor.org/rfc/rfc2308).
- [RFC 8945: TSIG](https://www.rfc-editor.org/rfc/rfc8945).
- [RFC 5936: AXFR](https://www.rfc-editor.org/rfc/rfc5936).
- [Debian: manuales BIND](https://manpages.debian.org/trixie/bind9/).
