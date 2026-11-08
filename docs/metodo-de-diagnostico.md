# Método técnico de diagnóstico

[Índice](../README.md) · [Laboratorio](laboratorio.md) · [Ficha de incidencia](../recursos/plantillas/incidencia.md)

## 1. Convertir un síntoma en un problema comprobable

«No funciona Internet» no identifica una causa ni una prueba. Una descripción útil sería: «En cli01, a las 10:15 UTC, el navegador no abre `https://srv01.aula.test`; el acceso por IP al puerto 443 responde y el mismo nombre se resuelve desde otro cliente». Esta información delimita el alcance y permite investigar resolución, configuración del cliente o caché.

Recoge cuándo empezó, a quién afecta, qué cambió y cómo se reproduce. Distingue el error del usuario, el mensaje de aplicación, el código de protocolo y el registro del servidor. Un estado `active` de systemd demuestra que el proceso está activo según su unidad; no demuestra que el cliente reciba una respuesta válida.

## 2. Secuencia de trabajo

1. **Delimita el alcance.** Equipo, usuario, red, servicio, momento y consecuencias.
2. **Protege el estado.** Guarda configuración y registros relevantes; identifica cómo volver atrás antes de modificar.
3. **Obtén una línea base.** Versiones, recursos, rutas, listeners y último estado conocido.
4. **Formula una hipótesis.** Debe predecir un resultado observable: si DNS es la causa, una consulta directa al servidor correcto diferirá de la resolución que usa la aplicación.
5. **Ejecuta una prueba discriminante.** Elige la que separa causas, no la que únicamente repite el síntoma.
6. **Modifica una variable controlada.** Cambiar dirección, DNS, firewall y servicio a la vez impide atribuir el resultado.
7. **Valida el servicio desde el cliente.** Incluye funcionamiento, autorización, persistencia y un caso negativo.
8. **Documenta la causa y la prevención.** Guarda evidencia antes/después y pasos de recuperación.

Reiniciar puede ser una medida de recuperación, pero elimina contexto y no identifica necesariamente la causa. Si el incidente reaparece, busca registros, espacio, recursos, dependencias y cambios recientes en lugar de repetir reinicios sin medir.

## 3. Diagnóstico por capas

| Capa de investigación | Pregunta | Evidencia típica |
| --- | --- | --- |
| Física o virtual | ¿Existe enlace y está conectada la NIC correcta? | LEDs, estado del switch, adaptador virtual, `ip -br link` |
| Enlace | ¿Coinciden VLAN y dominio de difusión? | Tabla MAC, configuración de puerto, vecinos ARP/ND |
| Red | ¿La dirección/prefijo es correcto y hay ruta? | `ip route get`, `Get-NetIPConfiguration`, trazas |
| Transporte | ¿Se puede completar la conexión al puerto? | `ss`, `Test-NetConnection`, captura TCP |
| Nombre y tiempo | ¿Se resuelve al servicio correcto y el reloj es válido? | `dig`, `Resolve-DnsName`, registros SRV y sincronización |
| Aplicación | ¿Responde con el protocolo, datos y código esperados? | HTTP, logs de servicio, validadores de configuración |
| Identidad/autorización | ¿Es el principal correcto y tiene el permiso efectivo? | Grupos, ACL, tickets, auditoría |
| Datos y continuidad | ¿Los datos son coherentes y se pueden recuperar? | Checksums, consultas, restauración y tiempos |

Esta división guía la investigación; un fallo puede atravesar varias capas. Si se abre TCP pero TLS falla, no has demostrado un problema de cableado. Si HTTP responde 403, existe comunicación con un servidor y debes analizar identidad, permisos y configuración de acceso.

## 4. Caso resuelto: no se abre una web por nombre

Estado esperado: `srv01.aula.test` resuelve a `192.168.56.10` y sirve HTTPS. Desde el cliente falla la URL, pero no se conoce todavía la causa.

Primero comprueba dirección y ruta. En Linux, `ip route get 192.168.56.10` debe seleccionar la NIC LAB. En Windows, `Test-NetConnection 192.168.56.10 -Port 443` prueba transporte. Un timeout no basta para elegir entre filtrado y ruta; combina con listener del servidor (`sudo ss -lntp`) y logs.

Consulta al servidor DNS previsto:

```bash
dig @192.168.56.10 srv01.aula.test A
```

El resultado esperado es una respuesta autoritativa o válida según configuración, con A `.10`. Si la consulta directa funciona y la aplicación usa otro resolutor, comprueba la configuración DNS y la caché del cliente. No añadas un registro arbitrario a `/etc/hosts` sin registrar que estás evitando temporalmente DNS.

Para probar HTTP/TLS con nombre y dirección controlados:

```bash
curl --resolve srv01.aula.test:443:192.168.56.10 https://srv01.aula.test/
```

`--resolve` mantiene el nombre de la URL y el SNI, pero fija el destino para esa ejecución. El cliente debe confiar en la CA de laboratorio y el certificado debe incluir el nombre. Un fallo de confianza exige revisar cadena, nombre y fechas; no se considera resuelto añadiendo `-k` como configuración permanente.

Si la web responde con 502, el frontal está respondiendo y debes comprobar su backend, socket o conexión FastCGI. Si responde 200 con contenido incorrecto, revisa host virtual, raíz del sitio y caché. Acepta el cierre cuando el nombre resuelva normalmente, TLS valide y el contenido sea el correcto desde un cliente.

## 5. Caso resuelto: acceso denegado a archivos

Una usuaria puede listar un recurso SMB pero no crear archivos. Separa identidad usada, permiso del recurso compartido y permisos del sistema de archivos. La autenticación correcta no concede automáticamente autorización de escritura.

En Windows consulta grupos efectivos y ACL; en Samba revisa usuario/grupos UNIX, configuración del recurso y permisos del directorio. Un permiso de escritura en la definición de Samba no evita que el sistema de archivos deniegue acceso. Un usuario que cambió de grupo puede necesitar nueva sesión o token.

Prepara tres pruebas con archivos sintéticos: lectura por un grupo lector, escritura por un grupo editor y denegación a un usuario ajeno. Comprueba las pruebas desde el cliente con identidades distintas y elimina credenciales de sesión almacenadas si interfieren. No uses `chmod 777` ni permisos para todos como diagnóstico final: harían desaparecer el síntoma a costa de incumplir el requisito.

## 6. Rendimiento y capacidad

Define antes una carga y un objetivo: abrir un documento de 20 MiB desde un cliente cableado en menos de un umbral didáctico, con tres repeticiones y mismo estado de caché. Un resultado aislado no distingue saturación de disco, memoria, CPU o red.

Observa correlación temporal: latencia de almacenamiento, uso de CPU, memoria disponible, paginación y transferencia. El porcentaje de ocupación de un disco no mide su salud; disponer de espacio no demuestra baja latencia. La velocidad nominal del enlace no equivale al caudal útil de una transferencia y la compresión puede falsear algunas mediciones.

Expresa unidades y método: MB/s y Mb/s difieren por un factor de ocho antes de considerar sobrecarga; GiB y GB usan bases distintas. Registra si los datos están en caché, si hay otros procesos activos y cómo se obtuvo la medida. Justifica una ampliación por la evidencia del cuello de botella.

## 7. Cierre y prevención

Una incidencia cerrada indica causa confirmada o, cuando no se ha podido confirmar, hipótesis pendiente y medida de contención aplicada. Añade impacto, cambio exacto, prueba positiva, prueba negativa, persistencia tras reinicio cuando proceda y riesgo residual observado.

Relaciona prevención y causa. Si el problema era disco lleno por logs, un reinicio no evita repetición; revisa rotación, retención, capacidad y alertas. Si fue un cambio sin revisión, documenta validación de sintaxis, copia previa y ventana de cambio. Las evidencias se entregan con datos mínimos y con la [matriz de pruebas](../recursos/plantillas/matriz-de-pruebas.md).
