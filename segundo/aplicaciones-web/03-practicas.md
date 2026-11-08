# Prácticas de Aplicaciones web

Trabaja en una VM aislada y usa datos ficticios. Las ventanas, tiempos y rúbricas siguientes son propuestas didácticas del repositorio. Antes de ejecutar una modificación, identifica el objetivo, conserva su configuración y decide cómo revertirla.

## Práctica 1 · Sitio estático explicable y accesible

**Duración orientativa:** 3–4 horas. **Objetivo:** publicar una página cuyos recursos, estructura y comportamiento puedas explicar. **Requisitos:** navegador, editor de texto y Python 3 o servidor HTTP de pruebas.

1. Copia el [sitio de ejemplo](ejemplos/sitio-estatico/index.html) y su CSS a una carpeta de trabajo. Abre el HTML y enumera sus regiones, títulos, enlaces y tabla.
2. Sustituye el tema por una guía de mantenimiento propia. Conserva HTML semántico, idioma, título significativo, enlaces internos y una tabla con encabezados. No incorpores datos reales.
3. Inicia el servidor local según la guía técnica. Revisa Red y Consola; anota método, estado y tipo de contenido de HTML y CSS.
4. Solicita una ruta inexistente. Documenta la diferencia entre recibir la página principal y un 404; no cambies el servidor para ocultar el error.
5. Recorre todo con teclado, observa foco y activa el enlace de salto. Amplía al 200% y reduce la ventana a 320 píxeles. Corrige desbordamientos del texto principal.
6. Comprueba HTML y CSS con herramientas de validación apropiadas. Una validación sintáctica no garantiza accesibilidad, por lo que debes conservar también las comprobaciones manuales.
7. Añade una imagen propia o de licencia identificada y el texto alternativo adecuado. Explica si es informativa o decorativa.
8. Entrega los archivos y un registro de prueba con resultado observado, esperado y cambios realizados.

**Aceptación:** los recursos deben ser locales, los enlaces internos alcanzar su destino y la página poder recorrerse sin ratón. La tabla puede tener desplazamiento propio cuando sea necesario, pero el resto del texto debe reorganizarse. **Rúbrica sobre 10:** estructura 3; adaptabilidad 2; teclado/alternativas 2; HTTP y diagnóstico 2; memoria 1.

**Recuperación:** si se rompe el estilo, comprueba ruta del CSS, estado HTTP y errores sintácticos antes de rediseñar todo. Si falla únicamente la versión publicada, revisa diferencias entre rutas relativas y absolutas, mayúsculas y permisos.

## Práctica 2 · Instalación de WordPress y roles

**Duración orientativa:** 5–7 horas. **Objetivo:** levantar un CMS HTTPS con dependencias y permisos documentados. **Requisitos:** instantánea, Debian 13 y cliente LAB; completa antes los fundamentos y el procedimiento de la guía técnica.

### Ejecución

1. Registra IP, nombres, rutas, listeners y versiones candidatas. Confirma que no alterarás un servidor de otra práctica. Configura la resolución de `wp.aula.test` en **srv01 y cli01**; verifica en srv01 con `getent ahostsv4` que apunta a `.10`.
2. Instala Nginx, MariaDB y PHP-FPM. Verifica el socket real y anota extensiones. Contrasta la versión de WordPress con la matriz de PHP y los complementos que piensas utilizar.
3. Crea el esquema y usuario SQL restringidos a la aplicación. Demuestra conexión sin publicar la contraseña ni capturas que la contengan.
4. Descarga WordPress desde el proyecto, registra versión y hash, y despliega con código no escribible por PHP. Configura secretos locales y permisos.
5. Prepara la CA de laboratorio o usa la existente. Emite un certificado cuyo SAN incluya `wp.aula.test`; instala únicamente su certificado público en el cliente y en el almacén Debian de srv01. Instala el mu-plugin LAB según la guía, conservando verificación TLS y sin modificar núcleo.
6. En el clon dedicado, respalda Nginx e inspecciona los sitios activos. Si existe el enlace estándar `sites-enabled/default`, retira sólo ese enlace según la comprobación de la guía; revisa otros listeners antes de activar el CMS. Configura el servidor virtual, valida con `nginx -t`, recarga y comprueba con `ss` que sólo escucha en `.10:80` y `.10:443`. Comprueba redirección HTTP a HTTPS y conexión TLS **desde srv01, sin `--resolve` y sin omitir verificación**.
7. Completa instalación. Crea una página «Taller», dos entradas, una categoría y una imagen. Configura enlaces permanentes y prueba cada URL.
8. Crea cuentas separadas de administrador y editor. En una sesión privada verifica qué puede hacer el editor y qué operaciones deben denegarse.
9. Revisa el acceso anónimo, cierra sesión y comprueba que la administración no queda disponible sin autenticación.
10. Ejecuta la prueba de la HTTP API como `www-data` y revisa bucle invertido, REST y tareas programadas en Salud del sitio. Documenta cómo retirarás el mu-plugin, los certificados de confianza de servidor/cliente y las entradas locales de nombre al terminar.

### Pruebas de aceptación

| Prueba | Resultado esperado |
| --- | --- |
| HTTP al nombre del CMS | Redirección al mismo recurso por HTTPS |
| HTTPS con CA confiada | Nombre y cadena válidos, contenido del CMS |
| Resolución y HTTPS desde srv01 sin `--resolve` | Nombre real `.10`, CA válida y respuesta de la aplicación |
| HTTP API y Salud del sitio | Petición interna verificada, sin error de CA; revisar por separado REST y tareas |
| Listeners efectivos Nginx | Sólo `.10:80` y `.10:443`, sin wildcard IPv4/IPv6 |
| URL de entrada publicada | Contenido correcto y recursos sin errores |
| Editor intenta gestionar complementos | Operación denegada por capacidad y política |
| Petición a `wp-config.php` | No se entrega el archivo ni su contenido |
| PHP en subidas | Configuración impide su ejecución; no es necesario subir código peligroso para comprobar la regla |
| Listener SQL | Acceso local según diseño, sin exposición a toda la red |

Entrega memoria de instalación, configuración **sin secretos**, inventario y resultados. No incluyas `wp-config.php`, claves TLS privadas ni volcados con credenciales en el repositorio. **Rúbrica:** arquitectura/versiones 2; instalación/permisos 3; TLS 2; roles/pruebas 2; documentación 1.

**Fallo provocado seguro:** en una copia de la configuración, escribe un socket FPM inexistente y ejecuta la prueba sintáctica. Explica por qué una sintaxis correcta puede seguir produciendo un 502 al atender peticiones. No recargues la configuración errónea en la VM principal; el objetivo es entender el límite de `nginx -t`.

## Práctica 3 · Copia, restauración y actualización ensayada

**Duración orientativa:** 4–6 horas. **Objetivo:** demostrar recuperación y controlar un cambio de versión. **Requisitos:** CMS operativo, dos VM o una restauración en una red separada y espacio de copia fuera del árbol web.

1. Define un objetivo de pérdida de datos y otro de recuperación. Para esta práctica puedes fijar, por ejemplo, una copia previa a cada cambio y recuperación en menos de una sesión; debes medir el resultado real.
2. Crea una entrada y sube una imagen identificables como «marcadores de recuperación». Registra fecha y URL.
3. Pausa escrituras de aplicación en una ventana, exporta base y copia archivos/configuración según la guía. Registra herramientas, hashes, permisos y versiones.
4. Transfiere el conjunto a un almacenamiento distinto o a la VM de restauración. No lo sirvas mediante HTTP para facilitar la descarga.
5. Restaura en una base vacía y directorio separados. Mantén la prueba aislada si utiliza el mismo nombre del sitio. Comprueba portada, marcadores, medios, roles y enlaces.
6. Mide el tiempo y anota cualquier paso manual que faltaba en la guía. Corrige el procedimiento de copia si descubriste una omisión.
7. En el entorno restaurado, ensaya una actualización oficial disponible o, si ya usas la última versión mantenida, prepara y documenta el procedimiento con verificación de que no hay cambios pendientes. No instales deliberadamente una versión vulnerable para simular una actualización.
8. Evalúa regresiones y prepara reversión compatible de archivos y base. Sólo considera aceptada la prueba cuando haya criterios verificables.

**Entregables:** procedimiento sin secretos, inventario, hashes, tiempos y registro de restauración. Las copias sensibles permanecen en almacenamiento privado de laboratorio, no en el repositorio público. **Rúbrica:** coherencia de copia 3; restauración demostrada 3; cambio/reversión 2; medición y documentación 2.

**Solución razonada:** si restauras la base pero faltan imágenes, conservaste referencias a medios sin sus archivos. Si las imágenes están pero los usuarios y entradas no existen, falta la base correcta. Una exportación editorial por sí sola no cubre ambos componentes.

## Práctica 4 · Selección de una aplicación colaborativa

**Duración orientativa:** 2–3 horas. **Objetivo:** elegir una herramienta por necesidades y demostrar una salida posible. No necesitas contratar servicios ni crear cuentas de pago.

El caso es un equipo ficticio de cinco técnicos que comparte procedimientos e incidencias. Compara una alternativa alojada y una autogestionada usando documentación primaria o cuentas educativas ya autorizadas. Define cinco necesidades: permisos por rol, historial, búsqueda, exportación y recuperación. Añade requisitos de dispositivos, accesibilidad e integración.

Construye una matriz con requisito, evidencia, limitación y decisión. No marques «sí» a exportación porque exista un botón: identifica formato, adjuntos, comentarios, historial y permisos que se incluyen. Si dispones de un entorno de pruebas autorizado, crea tres documentos sintéticos, exporta e intenta abrirlos en una alternativa. Si sólo puedes investigar, indica que la prueba práctica queda pendiente y no presentes la capacidad como verificada.

Entrega recomendación de 500–700 palabras, matriz y procedimiento de salida. Distingue precio publicado de coste total de operación. **Rúbrica:** necesidades 2; fuentes/evidencias 2; permisos/privacidad 2; exportación/salida 3; recomendación 1.
