# Incidencias encadenadas: investigar dependencias y causas

[Cuaderno](README.md) · [Método de diagnóstico](../docs/metodo-de-diagnostico.md) · [Servicios](../segundo/servicios-en-red/README.md)

## 1. Cómo utilizar estos casos

Los siguientes relatos son escenarios sintéticos de investigación. Las salidas y tiempos descritos forman parte del enunciado; no son mediciones ejecutadas durante la elaboración del repositorio. Puedes reproducir las condiciones que sean apropiadas en una VM aislada, siempre con copia y recuperación. No provoques deliberadamente fallos en equipos de trabajo o redes ajenas.

En cada caso separa síntoma, observación, hipótesis y causa. Una observación puede ser compatible con varias causas. La hipótesis debe predecir una diferencia que puedas comprobar; la causa se considera confirmada cuando una prueba y una corrección controlada explican el comportamiento. Distingue causa inicial, dependencias y errores añadidos durante la investigación.

Antes de leer la solución, redacta tres pruebas ordenadas por coste y capacidad para descartar alternativas. Después compara con el razonamiento propuesto. Otras secuencias pueden ser válidas si preservan el estado, evitan cambios indiscriminados y producen evidencia suficiente.

## 2. Caso A: una web vuelve por IP, pero falla por nombre

### Enunciado y estado conocido

`cli01`, con dirección `.56.20/24`, puede abrir un servicio HTTP de `.56.10` y establecer TCP 443. El navegador falla al abrir `https://wp.aula.test`. Otro cliente abre la misma URL. La persona que investiga propone desactivar el firewall del servidor y reinstalar WordPress.

La primera pregunta es qué significa «falla»: resolución inexistente, conexión, certificado, redirección o código HTTP. Se facilita como dato sintético que `Resolve-DnsName wp.aula.test` en el cliente afectado devuelve una dirección antigua `.56.40`; una consulta explícita al DNS correcto devuelve `.56.10`.

### Investigación razonada

El hecho de que TCP 443 responda en `.10` demuestra transporte hacia ese destino, sin probar el nombre ni la confianza TLS. Que otro cliente funcione reduce la probabilidad de un fallo general del servidor, pero no lo excluye por completo: pueden usar otro resolutor, dirección o ruta.

Compara resolutores configurados, sufijos, archivo hosts, caché y consultas dirigidas. Si una consulta explícita funciona y la resolución normal no, el problema puede estar en la selección de DNS o en una sobrescritura local. Vaciar una caché sin identificar el origen puede resolver un síntoma temporal sin corregir la configuración que lo recrea.

Para aislar nombre y destino, desde un cliente con `curl` y confianza preparada puede usarse `--resolve` como explica la guía de web. El resultado no sustituye una prueba de resolución normal. Si se accede por IP, el certificado puede fallar legítimamente por nombre, aunque el servidor sea el correcto.

### Corrección y aceptación

En este escenario se descubre una entrada antigua en hosts del cliente. Se registra y corrige únicamente esa entrada de laboratorio. Después se comprueba la resolución habitual, TLS sin omitir validación y contenido esperado. No se modifica el firewall ni se reinstala el CMS porque las observaciones no justifican esas acciones.

**Cierre mínimo:** causa confirmada, entrada antigua, motivo de su existencia, cambio y tres pruebas: nombre a `.10`, certificado correcto y página correcta. Una segunda resolución tras nueva sesión comprueba persistencia. La prevención puede ser documentar y retirar las sobrescrituras temporales cuando termine su uso.

## 3. Caso B: la copia funciona, pero no satisface recuperación

### Enunciado

Una tarea termina cada noche con código de salida cero y el informe muestra archivos en el destino. Después de borrar accidentalmente una carpeta de prácticas, la restauración recupera datos, pero algunos usuarios no pueden acceder. El responsable afirma que el backup estaba bien porque «todos los ficheros han vuelto».

El requisito aprobado incluía datos y permisos para grupos lectores y editores. Los archivos se copiaban a un sistema de archivos que no conservaba del mismo modo propietarios y ACL. La tarea no comprobaba esas propiedades ni ejecutaba una restauración con identidades independientes.

### Investigación

Identifica el conjunto protegido: contenido, metadatos, ACL, propietarios, nombres de recurso, cuentas y grupos, configuración de aplicación y claves. Una copia de archivos puede ser correcta para un objetivo y no para otro. El resultado de una herramienta debe interpretarse contra los requisitos que esa herramienta y sus opciones implementan.

Consulta permisos del origen y de la restauración. En Linux distingue permisos POSIX, ACL de acceso y ACL por defecto, así como capacidad del destino para conservarlas. En Windows distingue ACL del sistema de archivos y permisos del recurso SMB. Verifica si las identidades tienen los mismos identificadores o sólo el mismo nombre visible.

Una exportación de ACL debe conservar rutas e interpretarse en el destino adecuado. La guía de SOR usa rutas absolutas mediante `getfacl -Rp` y una simulación antes de aplicar `setfacl --restore`. No restaures ciegamente sobre un árbol distinto ni supongas que una ACL sustituye a los datos.

### Solución y pruebas

Se rediseña el procedimiento para conservar o reconstruir los metadatos necesarios mediante mecanismos compatibles y documentados. Se recupera primero en una ruta nueva y se prueba con tres identidades: lector, editor y usuario sin autorización. El editor crea y modifica un archivo sintético; el lector lo lee sin modificar; el tercero recibe denegación.

Se compara integridad de contenido y se mide tiempo. La tarea de copia se supervisa y se programa un ensayo de restauración. El código cero sigue siendo una evidencia de ejecución, pero se complementa con comprobación del objetivo real.

**Pregunta:** ¿puedes aceptar una restauración cuyo hash coincide pero cuyos permisos no cumplen? Si el requisito incluye confidencialidad y autorización, no. La integridad del contenido es una condición necesaria de ese objetivo, pero no suficiente.

## 4. Caso C: unirse al dominio falla después de «arreglar Internet»

### Enunciado

El cliente de una práctica AD navega por sitios externos, pero no encuentra `ad.aula.test`. El día anterior se cambió DNS del cliente a un servidor público para resolver una descarga. El controlador `dc01` mantiene `.56.11/24` y sus servicios están activos.

En la variante del caso, las consultas del dominio ya funcionan pero la autenticación falla y el reloj del cliente está desajustado. Hay dos problemas diferentes que pueden aparecer en secuencia.

### Razonamiento

La resolución pública de Internet no demuestra que un DNS externo conozca la zona privada del directorio ni sus registros SRV. Una dirección IP de controlador en hosts tampoco sustituye todos los mecanismos de descubrimiento. AD utiliza DNS para localizar servicios y necesita una política de tiempo coherente para autenticación.

Comprueba conectividad al controlador, DNS configurado en la NIC usada, resolución de la zona y registros de servicio. Observa la hora y sincronización. Evita alternar varios DNS de forma aleatoria: distintos sistemas pueden seleccionar servidores según reglas que no significan «pregunta siempre primero a éste y después al otro si el nombre no existe».

La NIC NAT añade otro contexto de resolución. Para el escenario de AD sigue la guía de SOR: controlador dedicado y diseño claro de conectividad y DNS. No conviertas el DNS público en un sustituto del del dominio para solucionar una descarga.

### Corrección

Se restaura el DNS del directorio en el cliente y se repiten consultas explícitas y normales. Se prepara resolución externa con el diseño apropiado cuando se necesite, sin cambiar la autoridad del dominio. Si persiste un fallo de autenticación, se investiga tiempo, credenciales, edición del cliente, permisos de unión y registros, sin declarar que todos los errores de AD son «de DNS».

**Aceptación:** localización del dominio, autenticación con una cuenta de laboratorio, aplicación de la política prevista y acceso a un recurso autorizado. **Caso negativo:** una cuenta no autorizada sigue sin obtener el recurso. El informe identifica qué fallo era DNS y cuál, si aparece en la variante, corresponde al reloj.

## 5. Caso D: dos servidores DHCP y una avería intermitente

### Enunciado

Tras reiniciar, algunos clientes reciben direcciones `.56.100–150` y DNS `.10`; otros reciben otro rango y un DNS distinto. El servidor Kea está bien configurado y sus logs muestran concesiones correctas. La práctica parecía funcionar la sesión anterior.

Se facilita como dato del escenario que la red host-only conserva un DHCP del hipervisor. El equipo mantiene además una NIC NAT legítima para Internet. Desactivar indiscriminadamente todos los DHCP podría romper la NIC NAT sin resolver el método de la práctica.

### Pruebas discriminantes

Identifica la NIC y el identificador del servidor que concedió cada configuración. En un cliente de prueba observa el ciclo de concesión y correlaciónalo con logs y una captura autorizada en LAB. No provoques renovaciones o desconexiones de equipos ajenos. Conserva una VM con IP estática para administrar.

La captura puede mostrar varias ofertas. Debes interpretar interfaz, servidor, rango y opciones. Una concesión correcta de Kea no demuestra que todos los clientes la hayan recibido. Tampoco se debe culpar a DNS por una dirección y parámetros que proceden de otro servidor.

### Corrección y cierre

Se desactiva sólo el DHCP incorporado en LAB, manteniendo el de NAT donde corresponde. Se verifica que LAB no esté en puente con la red física y que Kea escuche en la NIC prevista. Se ensaya con un cliente temporal y se registran dirección, prefijo, DNS e identificador del servidor.

La ausencia de gateway en LAB es correcta en la topología base. No se añade `.56.1` sólo porque aparecía como dirección del anfitrión. El acceso a Internet, si se necesita, sigue por la NIC NAT y su ruta por defecto.

**Causa:** coexistencia no planificada de DHCP en el mismo dominio de difusión. **Prevención:** checklist del hipervisor, inventario de servicios y prueba de servidor de concesión antes de comenzar cada laboratorio. Un DHCP mal conectado a la red física tiene un alcance distinto y exige detener el servicio y comunicar el incidente por el procedimiento del centro.

## 6. Caso E: el servidor «está activo» y la aplicación devuelve 502

### Enunciado

Nginx aparece activo, el cliente resuelve el nombre y TLS valida. Al pedir una página PHP se recibe HTTP 502; una página estática se sirve correctamente. La persona de soporte propone volver a crear el certificado.

El dato sintético del caso es una actualización de PHP que cambió el socket FPM disponible. El servidor virtual conserva una ruta al socket anterior. Existen otras causas posibles de 502, por lo que no se debe aplicar esa explicación sin evidencia.

### Análisis de dependencias

La respuesta 502 demuestra que un componente HTTP ha respondido y declara un problema con su upstream. Que una página estática funcione orienta hacia el trayecto dinámico. La confianza TLS ya comprobada reduce la pertinencia de volver a generar el certificado.

Revisa el error log de ese virtual host y el estado de FPM. Comprueba existencia del socket o destino de red, permisos, usuario/grupo y configuración efectiva. `nginx -t` valida sintaxis y algunos recursos, pero no garantiza que el backend funcione correctamente durante cada petición.

Si hay varios sitios o pools, identifica cuál está sirviendo el nombre. Cambiar un archivo que no está habilitado no modifica el servicio observado. `nginx -T` permite revisar la configuración efectiva; su salida puede incluir detalles que deben sanearse antes de compartir.

### Solución y pruebas

En el escenario se actualiza la referencia al socket del pool correcto después de comprobar la versión y su estado. Se valida y recarga sólo la configuración necesaria. Se pide una página estática, una dinámica y una operación de aplicación que consulte datos, evitando dejar un `phpinfo()` públicamente disponible.

**Recuperación:** si el cambio de aplicación exige una versión no compatible, la respuesta puede ser restaurar el conjunto ensayado de aplicación, PHP y datos. Una reversión del código no siempre revierte una migración de esquema. La memoria debe describir qué componente cambió y qué dependencia impidió el servicio.

## 7. Caso F: permisos, sesión antigua y una conclusión falsa

### Enunciado

Se añade una cuenta al grupo de editores. La consola del servidor muestra la pertenencia correcta, pero el cliente sigue sin poder escribir. Un administrador concede permisos directos al usuario y después declara que «los grupos no funcionan».

En el caso sintético, el cliente conserva una sesión SMB o token anterior al cambio. Además, existe una ACL que impide una operación concreta. El objetivo es reconocer que corregir una dependencia puede revelar otro problema.

### Investigación

Comprueba identidad efectiva y sesión realmente utilizada. El nombre escrito en un diálogo no prueba qué credencial se reutiliza. Identifica conexiones de laboratorio existentes y crea una sesión nueva mediante el procedimiento documentado, sin eliminar todas las conexiones de trabajo del usuario.

Después revisa autorización en cada capa: recurso compartido, sistema de archivos, herencia, ACL explícitas y permisos del directorio padre. Una membresía recién creada no convierte cualquier ACL en favorable. En Samba independiente intervienen además las identidades y grupos del servidor UNIX según el diseño elegido.

La concesión directa al usuario puede ocultar tanto el problema de sesión como el diseño de grupos y complicar futuras bajas. Si se añadió como medida temporal, debe registrarse y retirarse cuando el esquema previsto funcione.

### Aceptación

La solución del escenario renueva la sesión, corrige el permiso que contradice el requisito y mantiene autorización mediante grupos. Se prueba crear, modificar, leer y denegar con las identidades previstas. Se conserva una matriz que muestra la diferencia entre pertenencia, permiso asignado y operación efectivamente permitida.

**Pregunta de defensa:** ¿qué prueba demostraría que la corrección se debe al grupo y no a una concesión directa residual? Retirar la concesión temporal en laboratorio, establecer una sesión nueva y repetir la matriz con una cuenta de prueba equivalente y su pertenencia documentada.

## 8. Caso G: disco lleno, logs y un backup que agrava el fallo

### Enunciado

La aplicación deja de guardar datos. Hay espacio en un disco secundario, pero el sistema raíz aparece lleno. Un script de copia escribe en `/mnt/copias`; el disco destinado a esa ruta no está montado y el script ha escrito en un directorio del sistema raíz. Los logs crecen además por errores repetidos del servicio.

El síntoma puede aparecer como fallo de base de datos, de sesión o de escritura temporal. La existencia física de un segundo disco no demuestra que una ruta pertenezca a él.

### Pruebas

Comprueba sistemas de archivos montados, espacio, inodos y ruta real. `findmnt -T /mnt/copias` identifica el sistema de archivos que contiene la ruta aunque no sea un punto de montaje separado. Usa herramientas de consulta y tamaños para localizar crecimiento, evitando búsquedas invasivas sobre árboles ajenos o servicios con carga crítica.

No borres archivos a ciegas ni elimines el único backup. Determina qué datos son recuperables, qué servicio mantiene archivos abiertos y qué retención debería aplicarse. Un fichero eliminado pero abierto puede seguir ocupando espacio hasta que el proceso cierre su descriptor; eso exige diagnóstico y un cambio controlado, no reinicios generales sin contexto.

### Corrección y prevención

En el laboratorio se recupera margen mediante el procedimiento autorizado y una copia verificada de datos prescindibles. Se monta y verifica el destino correcto. El script debe comprobar identidad y disponibilidad del almacenamiento antes de escribir, y fallar de forma visible si no cumple. No basta con comprobar que existe un directorio llamado `copias`.

Se corrige la causa de logs repetidos, se configura retención y se supervisan capacidad e inodos. La aplicación se prueba con un dato sintético nuevo y se ensaya backup/restauración. La prevención incluye alerta de tarea fallida y comprobación del destino, no sólo un correo genérico de «script finalizado».

## 9. Caso H: una ampliación de RAM no mejora una tarea

### Enunciado

Un equipo tarda en abrir un conjunto de imágenes. Se amplía RAM de 8 a 16 GiB, pero el tiempo casi no cambia. No se disponía de una medición previa de presión de memoria. El equipo tiene almacenamiento con latencia elevada y se calienta bajo carga.

### Investigación

Define una carga reproducible: mismos archivos sintéticos, aplicación, versión, caché y actividad concurrente. Mide tiempo de apertura, uso de memoria, paginación, latencia de disco y frecuencia/temperatura cuando el equipo permita observarlas de forma segura. No compares una primera apertura fría con otra posterior totalmente en caché como si fuesen condiciones equivalentes.

Si no había presión de memoria relevante, ampliar RAM puede aportar margen sin acelerar esa tarea. Si la CPU reduce frecuencia por límites térmicos, una cifra nominal de GHz tampoco describe el comportamiento sostenido. Si el origen es almacenamiento o una red remota, hay que medir ese trayecto.

### Decisión

Se identifica un cuello de botella con pruebas diferenciadas antes de proponer otra compra. El informe separa la mejora de capacidad de una mejora de rendimiento y evita atribuir todo cambio temporal al componente instalado. Se revisan compatibilidad y mantenimiento físico con procedimientos seguros; no se abren fuentes de alimentación ni se improvisan reparaciones eléctricas.

**Entregable:** tabla antes/después, condiciones de prueba, observaciones de recursos, hipótesis descartadas y una recomendación ligada al cuello de botella confirmado. Incluye la posibilidad de que el laboratorio virtual no permita observar el hardware físico de forma concluyente.

## 10. Caso I: piloto de automatización que parece excelente

### Enunciado

Un procedimiento manual tardaba diez minutos por ticket y una automatización tarda dos. El informe afirma un ahorro del 80 %. Sin embargo, el piloto automatizado sólo incluyó casos sencillos y excluyó revisión de errores y mantenimiento de la herramienta.

### Análisis

La reducción de diez a dos minutos es 80 % para esas tareas y ese intervalo, pero no demuestra un ahorro equivalente de todo el proceso. Define inicio y fin, mezcla de complejidades, tasa de error, retrabajo, formación y mantenimiento. Cuenta también los casos que fallan o se derivan al procedimiento manual.

Utiliza una muestra sintética con clases conocidas y un criterio de calidad. Alterna orden y personas cuando sea viable para reducir efectos de aprendizaje. Conserva resultados por categoría además de una media global. Si la automatización genera decisiones de acceso, el criterio debe incluir errores de autorización y supervisión, no sólo velocidad.

### Resolución

Se repite el piloto con una mezcla comparable y se calcula capacidad liberada con supuestos explícitos. El ahorro de tiempo no se convierte automáticamente en una reducción salarial ni en efectivo disponible. La propuesta incluye coste de operación, recuperación y salida si la herramienta deja de mantenerse.

**Conexiones:** [Digitalización](../segundo/digitalizacion-aplicada-a-los-sectores-productivos/README.md), [IPE II](../segundo/itinerario-personal-para-la-empleabilidad-ii/README.md) y [cálculos del cuaderno](01-magnitudes-y-calculos-resueltos.md).

## 11. Caso J: un incidente resuelto que no se puede transferir

### Enunciado

El servicio vuelve a funcionar después de varias modificaciones. La memoria contiene únicamente «se arregló DNS y permisos». Otra persona no puede repetir la solución ni saber qué valores quedaron activos. Al reiniciar una VM vuelve parte del fallo porque una modificación era temporal.

### Investigación del propio proceso

Recoge configuración efectiva, cambios realizados, persistencia y pruebas. Distingue comandos temporales de archivos o gestores que conservan estado. Un cambio con `ip` puede ser útil para diagnosticar, pero no equivale a una configuración persistente en el gestor activo.

Cuando varias variables cambiaron a la vez, no inventes una causa retrospectiva. Indica qué se conoce, qué permanece sin confirmar y qué prueba controlada podría resolverlo en un laboratorio. Puede aceptarse una medida de contención con causa pendiente si la decisión y su alcance quedan claros; no debe presentarse como una causa demostrada.

### Cierre profesional

Se elabora un runbook con estado inicial, cambio, validación y recuperación. Se identifica propietario y dependencia. Otra persona reproduce el procedimiento en una copia o revisa la evidencia. La prueba tras reinicio se reserva para cuando sea apropiada y esté autorizada; no se reinicia un servicio de producción sólo para completar una casilla escolar.

Este caso conecta con [entrega y operación](05-entrega-y-operacion.md): la recuperación técnica necesita una documentación suficiente para mantener el resultado y atender la siguiente incidencia.

## 12. Rúbrica de autoevaluación

| Criterio | Peso orientativo | Evidencia que aporta calidad |
| --- | ---: | --- |
| Alcance y síntoma | 15 % | Describe qué falla, desde dónde, cuándo y para quién |
| Hipótesis y pruebas | 25 % | Pruebas que separan causas y conservan el estado |
| Interpretación técnica | 25 % | Relaciona observaciones con dependencias y límites |
| Corrección y recuperación | 20 % | Cambio mínimo justificado y vuelta atrás definida |
| Validación y comunicación | 15 % | Caso positivo, negativo, persistencia y cierre claro |

La rúbrica es propia del cuaderno. No premia acumular comandos ni obtener casualmente un resultado. Si no has ejecutado una prueba, escribe «pendiente» y explica qué observarías; una salida de ejemplo no se transforma en evidencia real por pegarla en la memoria.

## Fuentes de contraste

- [Debian Reference](https://www.debian.org/doc/manuals/debian-reference/) y [manuales Debian](https://manpages.debian.org/): red, sistemas de archivos, procesos y herramientas.
- [Microsoft Learn: Active Directory Domain Services](https://learn.microsoft.com/windows-server/identity/ad-ds/): dependencias y administración del directorio.
- [Samba documentation](https://www.samba.org/samba/docs/): identidades, permisos y recursos.
- [Nginx documentation](https://nginx.org/en/docs/) y [PHP-FPM](https://www.php.net/manual/en/install.fpm.php): funcionamiento del frontal y backend.
- [Kea ARM](https://kea.readthedocs.io/): concesiones, configuración y operación DHCP.
- [WordPress: debugging](https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/): observación de problemas del CMS.
