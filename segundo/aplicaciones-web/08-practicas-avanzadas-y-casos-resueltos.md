# 8. Laboratorio avanzado y casos resueltos de aplicaciones web

[Índice del módulo](README.md) · [Frontend](05-frontend-progresivo-y-accesibilidad.md) · [HTTP y controles](06-http-caches-sesiones-y-seguridad.md) · [Operación del CMS](07-operacion-migracion-y-recuperacion-cms.md)

## 1. Método de una práctica completa

Una práctica avanzada conecta requisito, diseño, cambio y evidencia. El número de comandos ejecutados no demuestra dominio si no puedes explicar qué objeto modifican. Empieza con un estado conocido, declara los comportamientos esperados y conserva una vía de recuperación antes de producir un fallo deliberado.

Las prácticas de este capítulo utilizan la LAB aislada, datos ficticios y clones cuando se cambian configuraciones del CMS. El servidor original es `srv01`, `192.168.56.10`; el cliente, `.20`; no se añade una puerta de enlace imaginaria al segmento. Una NIC NAT independiente permite descargas según necesidad. Los experimentos que conservan las mismas direcciones en un clon se hacen en otra red interna.

Para cada prueba indica resultado esperado y real, versión, momento y conclusión. Si una acción no se ha ejecutado, permanece pendiente. Una captura de la portada no demuestra accesibilidad completa, seguridad de todos los endpoints ni capacidad de recuperación. El alcance debe expresarse con precisión en la memoria.

## 2. Práctica avanzada A: frontend accesible y validación

**Objetivo:** comprender la relación entre HTML, reglas de entrada y cambios del DOM utilizando [registro-local](ejemplos/registro-local/index.html). El ejemplo no utiliza backend ni almacenamiento persistente, y la interfaz advierte que el contenido se pierde al recargar.

### Preparación

Copia la carpeta del ejemplo a un espacio de trabajo, conserva el original y revisa sus tres archivos. Sirve la carpeta sólo en loopback con el mecanismo explicado en el capítulo de frontend, o usa el entorno estático autorizado del centro. Abre Consola y Red para comprobar que no se cargan dependencias externas.

### Desarrollo

1. Desactiva JavaScript y registra qué información sigue disponible.
2. Actívalo, recarga y comprueba que la zona interactiva aparece sólo tras preparar los controles.
3. Envía campos vacíos y recorre el resumen de errores con teclado.
4. Introduce un código con espacios y minúsculas y observa su normalización.
5. Añade dos incidencias del mismo activo; deben ser registros distintos.
6. Introduce una descripción sintética con signos `<` y `>` y confirma su representación literal.
7. Vacía la lista generada y recarga; explica la diferencia entre memoria de la página y persistencia.

### Ampliación

Añade prioridad mediante una lista cerrada y un filtro de filas. Especifica si el filtro oculta o elimina información; la aceptación exige que una fila vuelva a mostrarse al quitar el filtro. Actualiza validación y pruebas cuando amplíes categorías, sin confiar únicamente en las opciones visibles del HTML.

### Aceptación y recuperación

La página debe conservar base informativa, etiquetas, foco visible y mensajes vinculados. Un error de script debe poder investigarse sin tocar reglas de Nginx o base de datos que no participan en el caso. Para recuperar vuelve a la copia original y compara los cambios que introdujiste; no sustituyas indiscriminadamente todo el proyecto si necesitas entender la causa.

**Entregables:** tres archivos, diccionario de entradas, explicación de funciones puras, doce pruebas y memoria de teclado/reflujo. **Rúbrica didáctica:** interacción 30 %, accesibilidad evaluada 25 %, representación de datos 20 %, pruebas 15 %, razonamiento y límites 10 %.

## 3. Práctica avanzada B: caché y recursos desactualizados

**Objetivo:** distinguir carga, frescura y revalidación en un sitio estático de laboratorio. Utiliza un recurso que puedas modificar sin afectar el CMS, en un clon o servidor virtual ya definido para esa actividad. No publiques un listener adicional en todas las interfaces para simplificar la prueba.

Define versión A y B de una hoja CSS con un cambio visible y sencillo. Obtén cabeceras, tamaño y respuesta inicial. Repite con caché normal y después con las herramientas de desarrollo configuradas para no reutilizar caché durante la sesión de prueba. Registra cuál de esas condiciones se usó: comparar dos ensayos diferentes sin anotarlo produce conclusiones falsas.

Si el servidor emite ETag, envía el valor en una petición condicional y observa 304 o la respuesta correspondiente. Modifica el contenido, repite y explica cómo cambia la representación. Si no se emite ese validador, documenta su ausencia y observa otro mecanismo disponible; no escribas un resultado esperado como si fuera observado.

Prepara una política para el HTML y otra para CSS versionado, justificando diferencias. Una prueba negativa debe demostrar que no se ha aplicado caché pública a una página privada. El caso de autenticación requiere sesiones distintas y contenido sintético; no uses cuentas reales para generar evidencias compartidas.

**Entregables:** tabla de peticiones, cabeceras relevantes, política propuesta, pruebas de cambio de versión y diagrama de capas. **Aceptación:** explicar una actualización visible y otra aparentemente desactualizada con la evidencia de cada capa. La corrección consiste en resolver la política o versión correspondiente, no en enseñar al usuario a vaciar siempre todo.

## 4. Práctica avanzada C: restauración y migración controlada

**Objetivo:** comprobar que la copia del CMS representa un punto recuperable y trasladar su nombre de manera coherente. Sigue el capítulo de operación, manteniendo redes separadas y bases distintas cuando corresponda.

Antes de copiar, genera contenido sintético conocido y guarda un inventario verificable. Coordina una ventana sin edición y construye el conjunto de datos, archivos y configuración. Restaura en un destino aislado y confirma que el archivo de configuración apunta al esquema de ese destino. Registra tiempo de preparación, transferencia, importación, ajuste y pruebas.

Añade una publicación al original después del punto de copia y verifica que la restauración mantiene el estado anterior. Explica la pérdida real en términos del requisito de recuperación y no como un recuento de ficheros. Un backup puede ser técnicamente legible y no cumplir el RPO que exige la organización.

Para migrar a otro nombre, prepara resolución, certificado, Nginx, configuración y condición exacta del mu-plugin local. Ejecuta primero `search-replace` en simulación y revisa alcance. La aplicación sólo se realiza sobre el clon identificado. Comprueba portada, editor, medios, enlaces, roles, peticiones internas y URL canónica al terminar.

**Entregables:** conjunto protegido fuera de Git, inventario sin secretos, registro de recuperación, informe de simulación sanitizado y matriz de aceptación. **Rúbrica propia:** copia y coherencia 30 %, aislamiento y preparación 20 %, migración 20 %, medición y pruebas 20 %, documentación 10 %.

## 5. Práctica avanzada D: incidente de servicio y comunicación

**Objetivo:** localizar un fallo deliberado reversible sin ampliar permisos ni desactivar TLS. En un clon limpio, el tutor o compañero prepara un único defecto: socket FPM incorrecto, nombre de certificado distinto, dirección hosts equivocada o permiso de lectura insuficiente de un archivo de prueba. No se modifica una instalación real para provocar una avería.

El investigador recibe síntoma, momento y alcance, no la solución. Debe comprobar red, nombre, TLS, frontal, backend y datos en un orden que discrimine hipótesis. Si la respuesta es 502, una prueba de cableado puede ser útil como base, pero no explica por sí sola la dependencia FPM. Si el navegador denuncia certificado, no se acepta «continuar de todos modos» como reparación.

La comunicación final incluye qué falló, qué impacto tuvo, qué cambió y qué se comprobó. Redacta también una explicación comprensible para una persona usuaria: disponibilidad restaurada, datos conservados o incertidumbre pendiente y siguiente paso. No compartas logs con credenciales para aparentar mayor detalle técnico.

**Aceptación:** causa demostrada con evidencia, cambio limitado al objeto correcto, prueba positiva y negativa, recuperación y registro del estado final. **Rúbrica propia:** investigación 30 %, corrección 25 %, validación 25 %, comunicación 20 %.

## 6. Dieciséis casos con respuesta razonada

### Caso 1. El HTML llega, pero la página no tiene estilos

Comprueba la petición CSS en Red: ruta, estado y `Content-Type`. Un 404 del CSS no exige reinstalar PHP. Si hay 200 con HTML en lugar de CSS, puede estar respondiendo una regla de fallback. Verifica URL y configuración del sitio que atendió la petición antes de cambiar el archivo de estilos.

### Caso 2. El script se descarga y el botón no responde

Descargar el recurso no demuestra ejecución correcta. Revisa errores de sintaxis, orden de carga, selector y asociación del controlador. Un ID renombrado puede devolver `null`. Pon un punto de interrupción en la preparación de la interfaz y otro en el evento para localizar dónde se interrumpe el flujo.

### Caso 3. El navegador valida, pero otro cliente acepta datos inválidos

La validación del frontend sólo controla esa experiencia de entrada. El servidor debe validar tipo, dominio, longitud y permisos antes de escribir. No se corrige imponiendo una expresión más compleja en JavaScript si el endpoint sigue confiando en cualquier petición recibida.

### Caso 4. Un error sólo se muestra en rojo

El color no identifica de manera suficiente la causa ni garantiza percepción. Añade mensaje textual, asociación con el campo y un resumen cuando haya varios errores. Comprueba teclado y foco. Cambiar rojo por otro color no resuelve la relación semántica ausente.

### Caso 5. `no-cache` parece seguir guardando el recurso

Ese comportamiento puede ser correcto: la directiva permite almacenamiento, pero exige validación antes de reutilizar. Comprueba petición condicional y respuesta 304/200. Si el requisito es evitar almacenar, analiza `no-store` y las demás capas según el tipo de datos, sin confundir los dos objetivos.

### Caso 6. La portada muestra el nombre de otro usuario

Trata el síntoma como posible fallo de aislamiento de contenido. Reproduce con cuentas sintéticas y sesiones separadas, revisa caché del CMS/proxy y política de respuestas personalizadas. No aceptes la corrección hasta comprobar que las identidades no comparten representaciones privadas.

### Caso 7. Cambiar la cookie no modifica el rol mostrado

Puede haber estado de sesión en el servidor, cookies adicionales o caché de interfaz. No presupongas que un valor visible es la autoridad del permiso. La autorización debe depender del modelo del servidor; borrar una etiqueta del frontend no demuestra revocar capacidades. Usa mecanismos de la aplicación y repite una operación protegida.

### Caso 8. Una respuesta 403 se interpreta como fallo de red

El código demuestra que algún servidor HTTP respondió, aunque podría ser un intermediario. Identifica quién respondió y revisa autorización, reglas y permisos. Abrir todos los puertos o cambiar gateway no explica una denegación de aplicación. Correlaciona URL, identidad y registro relevante.

### Caso 9. Hay 502 después de actualizar PHP

Comprueba servicio FPM, versión, socket existente y destino configurado en Nginx. Una ruta a `php8.4-fpm.sock` debe corresponder al proceso preparado. Valida sintaxis y listeners antes de recargar. No cambies propietario de todo el sitio a modo mundial para resolver una dependencia de backend equivocada.

### Caso 10. El navegador confía en TLS, pero Salud del sitio falla

El navegador y la HTTP API de WordPress pueden usar almacenes de CA diferentes. Comprueba resolución desde srv01, certificado, CA del SO y configuración exacta del mu-plugin de laboratorio. La prueba desde el propio servidor sin `--resolve` y la prueba de la API ayudan a separar confianza de resolución.

### Caso 11. La migración redirige al nombre antiguo

Revisa `home`, `siteurl`, reglas de Nginx, datos de plugins y caché. Una entrada hosts nueva no reescribe URLs de la aplicación. Usa simulación de una herramienta compatible con datos serializados y limita alcance; un reemplazo SQL global puede añadir corrupción a la redirección inicial.

### Caso 12. El dump existe, pero la recuperación queda incompleta

Un archivo presente puede estar vacío, truncado o contener sólo la base sin archivos subidos. Comprueba salida de exportación, contenido, conjunto de componentes e importación en otro destino. La evidencia decisiva es recuperar funciones y datos conocidos, no mostrar el tamaño del ZIP.

### Caso 13. Volver al código anterior no recupera el CMS

La actualización pudo modificar esquema o datos. La reversión debe recuperar el conjunto compatible o seguir un mecanismo soportado de migración inversa. No todas las extensiones ofrecen downgrade seguro. Restaura en el clon el punto previo y compara versiones y configuración antes de tocar de nuevo el original.

### Caso 14. La copia de pruebas envía correos no deseados

El clon conserva configuración y tareas del sitio. Aísla integraciones antes de encenderlo con acceso necesario y utiliza contenido sintético. Cambiar el título del sitio a «pruebas» no elimina credenciales ni cron. Documenta qué se deshabilita y cómo se demuestra que no hay envío externo en ese escenario.

### Caso 15. Se propone habilitar escritura general para actualizar

El modelo base separa código y operación editorial. Dar escritura a todo el proceso web cambia esa frontera. Mantén un despliegue controlado con identidad y permisos apropiados, ensaya la actualización y vuelve a comprobar propietarios. Que un botón quede habilitado no justifica ampliar capacidad sin revisar el diseño.

### Caso 16. Una mejora reduce el tiempo medio y empeora algunas peticiones

El promedio puede ocultar variabilidad y fallos. Revisa conjunto de pruebas, tipos de operación, caché y distribución de duraciones. Con una muestra pequeña presenta observaciones sin prometer percentiles robustos. Una mejora se acepta respecto de requisitos concretos, no únicamente porque una cifra resumen disminuya.

## 7. Defensa técnica y preguntas de contraste

Prepara una demostración de diez minutos orientativa: arquitectura, requisito, prueba positiva, denegación y recuperación. Identifica qué ya estaba instalado y qué has realizado tú. Si una parte no se ha ensayado, explica el procedimiento pendiente sin presentarlo como éxito obtenido.

Para comprobar profundidad, responde por qué el sitio sigue necesitando controles del servidor aunque valide en JavaScript; qué diferencia `private` de `no-store`; por qué el mu-plugin restringe host y entorno; y cómo demostrarías que una restauración recuperó el punto previsto. Relaciona cada respuesta con una evidencia, no sólo con una definición.

La memoria final debe permitir que otra persona repita el laboratorio dentro del mismo alcance. Incluye versiones, dependencias, nombres, archivos modificados y pruebas. Omite secretos, dumps y datos personales del repositorio público. Conserva las copias y claves por el canal indicado en el plan del ejercicio.

## Referencias primarias

Los procedimientos se apoyan en [MDN Web Docs](https://developer.mozilla.org/), [WCAG 2.2 de W3C](https://www.w3.org/TR/WCAG22/), [la administración de WordPress](https://developer.wordpress.org/advanced-administration/) y [WP-CLI](https://developer.wordpress.org/cli/commands/). Consulta en cada capítulo las páginas concretas y la versión aplicable. Los casos, tiempos orientativos y rúbricas son material didáctico propio.
