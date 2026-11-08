# Prácticas completas de Servicios en red

Cada práctica tiene diseño, implementación, pruebas positivas, pruebas negativas y recuperación. Utiliza exclusivamente el [laboratorio común](../../docs/laboratorio.md). No conectes servicios DHCP o SMTP de prácticas a redes reales. Las salidas esperadas son criterios que debes contrastar, no resultados ya obtenidos.

## Práctica 1. DNS directo e inverso con autoridad limitada

**Objetivo:** resolver nombres del laboratorio y explicar qué información se considera autoritativa.\
**Preparación:** srv01 con IP fija, cliente en `192.168.56.20/24`, sin DHCP de prácticas activo todavía.

### Trabajo

1. Redacta una tabla de nombres con A, CNAME, MX y PTR. Identifica qué registro responde a cada pregunta.
2. Configura las dos zonas siguiendo la guía técnica y conserva la configuración anterior.
3. Valida sintaxis y carga antes de reiniciar BIND.
4. Desde el cliente consulta explícitamente el A de srv01, el alias www, el MX del dominio y el PTR de `192.168.56.10`.
5. Prueba 53/TCP mediante `dig +tcp` y compara con la consulta habitual.
6. Consulta un nombre inexistente y diferencia `NXDOMAIN` de un nombre existente consultado por un tipo que no tiene, por ejemplo AAAA en esta versión IPv4.
7. Consulta un nombre externo a las zonas. Explica por qué un servidor autoritativo sin recursión no debe comportarse como resolver general de Internet.
8. Modifica sólo el TTL de un registro o añade un nombre de prueba, aumenta el serial, valida y recarga. Compara consulta directa al servidor con consulta mediante una caché que hayas identificado.

### Entrega y aceptación

Entrega zonas, comandos, respuestas completas saneadas y explicación de bandera `aa`, serial, TTL y código de estado. El nombre inexistente debe producir una respuesta coherente y TCP debe funcionar. No se considera éxito cambiar el DNS del navegador hasta que «abra una web» sin saber a qué servidor consultó.

**Solución orientativa:** www es alias de srv01; el A de srv01 ofrece `.10`; el PTR ofrece un nombre canónico; el MX contiene un nombre y preferencia. La resolución directa correcta no crea una concesión DHCP ni habilita el servicio al que apunta el nombre.

**Recuperación:** restaura las zonas previas si se rompe una consulta; incrementa el serial si el cambio se distribuye a secundarios. Para el laboratorio sin secundarios, aun así conserva una política coherente y revisa cachés del cliente.

## Práctica 2. DHCP aislado y sin gateway ficticio

**Objetivo:** demostrar una concesión correcta, detectar un segundo servidor y explicar renovación.\
**Preparación:** BIND funcionando, LAB aislada, DHCP del hipervisor desactivado y acceso de consola.

### Trabajo

1. Registra IP y MAC de las NIC NAT y LAB. Toma una instantánea del cliente.
2. Justifica el pool `.100–.150` y las exclusiones de `.10` y `.20`.
3. Configura Kea para escuchar sólo en LAB. No anuncies gateway en esa red.
4. Ejecuta la comprobación de configuración, inicia el servicio y revisa los logs.
5. Inicia una captura limitada de DHCP en LAB. Cambia sólo el adaptador LAB del cliente a DHCP.
6. Relaciona Discover, Offer, Request y ACK por los identificadores de transacción y cliente. No presupongas que todos los estados generan siempre exactamente cuatro paquetes: renovación y reutilización pueden producir otra secuencia.
7. Comprueba IP, prefijo, DNS, duración y rutas. Demuestra que NAT conserva su función y que LAB no ganó una puerta de enlace falsa.
8. Renueva la concesión y observa la diferencia respecto a la primera adquisición.
9. Añade una reserva fuera del pool, usando la MAC de prueba, y repite el proceso de obtención de dirección según el gestor del cliente.
10. Comprueba que el nombre de reserva no apareció mágicamente en BIND. Explica qué componente adicional haría falta para DDNS.

### Entrega y aceptación

Incluye JSON validado, topología, configuración del hipervisor, concesión y captura pequeña. Debe existir una sola oferta del servidor previsto durante el caso controlado. Si aparecen ofertas inesperadas, el procedimiento correcto es detener Kea y revisar aislamiento antes de seguir.

**Solución orientativa:** un cliente nuevo recibe una dirección dentro del pool y DNS `192.168.56.10`. La reserva puede proporcionar `.30` cuando su identificador coincide. La ausencia de opción routers es intencional porque no existe ese router en LAB.

**Recuperación:** detén Kea, devuelve LAB al estado guardado y confirma que el cliente fijo vuelve a funcionar. No alteres el DHCP del router doméstico ni el de ninguna red ajena.

## Práctica 3. Identidad SSH y transferencia íntegra

**Objetivo:** administrar con una identidad verificable y transferir sin publicar secretos.\
**Preparación:** cuenta alumno sin privilegios extra, consola de srv01 y cliente con OpenSSH.

### Trabajo

1. Obtén la huella pública del servidor desde su consola.
2. Conecta por SSH y comprueba la huella antes de aceptarla.
3. Genera una clave de usuario en el cliente con frase de paso, sin sobrescribir otra clave.
4. Instala únicamente la clave pública en `authorized_keys` de alumno y revisa propiedad y permisos.
5. Abre una segunda sesión autenticada por clave. Mantén la primera mientras realizas cambios.
6. Limita acceso a las cuentas y direcciones planificadas. Valida configuración antes de recargar.
7. Crea un archivo de texto sintético, calcula su hash, súbelo y descárgalo por SFTP, y vuelve a calcular el hash.
8. Realiza una prueba con un usuario inexistente y otra con un archivo fuera del directorio autorizado del alumno. Explica la diferencia entre autenticación y autorización.
9. Documenta cómo actuarías si cambia la huella tras reinstalar el servidor. No simules el caso borrando todo `known_hosts`.

### Entrega y aceptación

Entrega huella pública, fragmentos saneados de configuración, prueba de conexión y hashes. No subas la clave privada, su frase de paso, capturas de contraseñas ni archivos `authorized_keys` reales de otras personas.

**Solución orientativa:** coincidencia de huella demuestra que se contacta con la identidad contrastada; autenticación por clave demuestra posesión de la privada correspondiente; permisos del sistema siguen limitando el acceso a archivos. Los tres controles son distintos.

**Recuperación:** desde consola retira el fichero de restricción creado para la práctica, valida y recarga. Retira sólo la clave pública de práctica si se quiere revocar ese acceso.

## Práctica 4. HTTPS integrado y casos de fallo

**Objetivo:** separar fallos de DNS, transporte y TLS utilizando pruebas independientes.\
**Preparación:** Nginx y nombre www del laboratorio, certificado autofirmado con SAN.

### Trabajo

1. Publica una página estática con título y texto propios del laboratorio. Conserva permisos de lectura y evita escritura global.
2. Genera el certificado con nombre `www.aula.test`, validez corta y clave protegida.
3. Configura el sitio para escuchar sólo en la IP LAB y verifica cualquier sitio predeterminado adicional.
4. Valida Nginx, recarga y comprueba escucha.
5. Copia al cliente el certificado público y contrasta su huella.
6. Ejecuta una petición con `curl --resolve` y `--cacert`. Guarda código de estado y contenido.
7. Repite sin `--resolve` para incorporar DNS al camino.
8. Prueba HTTP y comprueba destino de redirección. Prueba una ruta inexistente y registra 404.
9. Intenta acceder con un nombre diferente usando resolución forzada al mismo servidor y documenta el error de nombre del certificado.
10. Retira temporalmente la confianza explícita de la prueba y explica el error esperado. No lo «soluciones» usando `-k` como prueba final.
11. Introduce un único fallo reversible, como un nombre DNS de prueba incorrecto, y localízalo con consultas y petición forzada. Restaura después el valor correcto.

### Entrega y aceptación

Entrega configuración del sitio, certificado público sólo si contiene datos sintéticos, ficha de pruebas y relación de cada fallo con su capa. Se debe demostrar validación TLS con nombre correcto y confianza explícita, no sólo que el navegador muestra contenido después de ignorar una advertencia.

**Solución orientativa:** si `--resolve` funciona y la petición normal no, DNS o la selección del resolver merecen revisión. Si TCP falla en ambos casos, se investiga proceso, escucha, firewall y rutas. Si TCP funciona pero falla el certificado, se revisan SAN, reloj, cadena y confianza.

**Recuperación:** restaura configuración anterior, valida y recarga. Conserva la clave privada únicamente donde corresponde y elimina cualquier confianza global añadida sólo para la práctica.

## Práctica 5. Integración y recuperación

**Objetivo:** que otra persona reconstruya el laboratorio usando tu documentación.

Prepara una copia saneada de configuraciones, inventario de paquetes y versiones, tabla de nombres, direccionamiento, dependencias y lista de pruebas. No incluyas claves privadas ni bases con datos reales. Explica dónde se respalda cada secreto de forma separada.

En una instantánea o VM desechable recupera un único servicio. Primero comprueba su red, después instala la versión adecuada, restaura configuración y datos necesarios, valida y prueba desde cliente. Registra cualquier paso ausente de la documentación y corrígelo.

Una restauración correcta debe demostrar las funciones principales y las restricciones: DNS autoritativo responde, DHCP queda en LAB, SSH mantiene cuentas autorizadas y HTTPS verifica nombre. Mide tiempo de recuperación observado y compáralo con el objetivo que habías fijado; no inventes RTO cumplido por no haber realizado el ejercicio.

## Rúbrica didáctica

| Dimensión | Peso orientativo |
| --- | --- |
| Diseño, dependencias y alcance de escucha | 20 % |
| Configuración comprensible y validada | 25 % |
| Pruebas desde cliente, positivas y negativas | 30 % |
| Diagnóstico, logs y recuperación | 20 % |
| Higiene de evidencias y documentación | 5 % |

La puntuación no es oficial. Un servicio que responde exponiéndose fuera del laboratorio necesita corregir su alcance antes de considerarse terminado.
