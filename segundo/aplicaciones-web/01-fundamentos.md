# Fundamentos de las aplicaciones web

## 1. De una URL a una página

Una URL describe un recurso mediante esquema, nombre de host, puerto opcional, ruta, consulta y fragmento. En `https://wp.aula.test/manuales/?tema=copias#restaurar`, el esquema indica HTTPS, el nombre requiere resolución, la ruta identifica el recurso, la consulta envía parámetros y el fragmento señala una parte del documento. El fragmento normalmente lo procesa el navegador y no se envía al servidor como parte de la petición HTTP.

El cliente resuelve el nombre, establece conexión y negocia TLS cuando corresponde. Después envía una petición y recibe una respuesta. La página HTML puede referenciar CSS, imágenes, fuentes y JavaScript, lo que genera nuevas peticiones. Por eso recibir un HTML con estado 200 no demuestra que el sitio esté completo: pueden fallar recursos, API o controles de autenticación.

Un sitio **estático** entrega archivos ya existentes. Un sitio **dinámico** produce respuestas utilizando lógica, plantillas, usuarios y datos. Un CMS combina un núcleo, una base de datos, temas y extensiones para gestionar contenido. Un servicio SaaS añade operación a cargo del proveedor, pero la organización sigue decidiendo usuarios, permisos, retención y exportación.

## 2. Capas y responsabilidades

| Componente | Responsabilidad | Fallo representativo |
| --- | --- | --- |
| Navegador | Interpretar HTML/CSS y ejecutar JS | Error de script o caché local |
| DNS | Resolver nombres | Dirección antigua o nombre inexistente |
| TLS | Proteger y autenticar el canal | Certificado no confiable o nombre incorrecto |
| Servidor HTTP | Seleccionar sitio y entregar/proxyar recursos | 404, permisos, servidor virtual incorrecto |
| Intérprete/backend | Ejecutar reglas de aplicación | Error PHP o dependencia incompatible |
| Base de datos | Persistir datos y consultas | Credencial incorrecta o servicio inaccesible |
| Almacenamiento | Conservar archivos y subidas | Espacio agotado o permisos insuficientes |

El frontend es la parte que se presenta y ejecuta en el cliente. El backend valida peticiones y aplica reglas en el servidor. Una validación de formulario en JavaScript mejora la experiencia, pero no protege por sí sola una base de datos: un cliente puede enviar peticiones sin utilizar esa interfaz. El servidor debe validar entradas y autorizar cada operación.

Diferencia desarrollo, pruebas y producción. Desarrollo permite experimentar; pruebas reproduce las condiciones necesarias para aceptar cambios; producción contiene el servicio real. No pruebes una actualización arriesgada directamente sobre la única copia. Una copia de producción con datos reales sigue necesitando protección aunque se denomine «pruebas».

## 3. HTTP: semántica útil para diagnosticar

Una petición contiene método, destino, cabeceras y, a veces, cuerpo. La respuesta incluye estado, cabeceras y cuerpo opcional. HTTP/2 y HTTP/3 cambian transporte y representación, pero conservan conceptos de métodos y estados. Una herramienta que muestra líneas de HTTP/1.1 ayuda a enseñar la semántica sin describir literalmente todos los detalles del protocolo moderno.

`GET` obtiene una representación; `HEAD` solicita cabeceras sin el cuerpo; `POST` envía datos para procesar una operación; `PUT` representa una sustitución según la API y `DELETE` una solicitud de eliminación. No uses GET para una acción que cambia estado, como borrar una cuenta, porque navegadores, previsualizadores y cachés pueden solicitar enlaces automáticamente.

| Estado | Interpretación inicial | Qué revisar |
| --- | --- | --- |
| 200 | Petición atendida correctamente | Contenido y recursos posteriores |
| 301/308 | Redirección permanente | Destino, caché y conservación del método |
| 302/303/307 | Redirección con semántica específica | Flujo de autenticación y método siguiente |
| 304 | Reutilizar representación en caché | Validadores y copia local |
| 400 | Petición no aceptable | Formato y cabeceras |
| 401 | Falta autenticación válida | Mecanismo de autenticación anunciado |
| 403 | Acceso denegado | Permisos y autorización |
| 404 | Recurso no encontrado | Ruta, sitio virtual y enlaces permanentes |
| 429 | Límite de peticiones | Política de límite y `Retry-After` |
| 500 | Error interno de aplicación | Registro del backend |
| 502/504 | Problema con un servicio intermedio | FPM, upstream y tiempos |
| 503 | Servicio temporalmente no disponible | Mantenimiento, capacidad y dependencias |

No deduzcas la causa únicamente por el código. Un 403 puede deberse a reglas del servidor, permisos del sistema de archivos o una decisión de la aplicación. Correlaciona URL, hora, cliente y registros. Evita publicar registros completos sin revisar datos personales, cookies o parámetros sensibles.

`Content-Type` describe cómo interpretar el cuerpo. `Cache-Control` expresa políticas de caché; `ETag` y `Last-Modified` ayudan a comprobar vigencia. Las cookies viajan mediante cabeceras y pueden incluir restricciones de alcance y uso. Una página con autenticación no debe cachearse públicamente por descuido.

## 4. HTTPS y confianza

TLS aporta confidencialidad e integridad en tránsito y permite comprobar la identidad del servidor mediante certificados y una cadena de confianza. No corrige vulnerabilidades de la aplicación ni cifra automáticamente las copias guardadas. El nombre utilizado debe figurar en el certificado, normalmente en `subjectAltName`.

En un dominio reservado como `aula.test` no se debe esperar un certificado público emitido como para un dominio real. Utiliza una autoridad interna gestionada o un certificado de laboratorio cuya confianza se instale únicamente en los clientes de la práctica. No conviertas «ignorar la advertencia» en procedimiento habitual y no desactives la verificación TLS de herramientas para que una prueba parezca correcta.

HTTPS protege el trayecto hasta donde termina TLS. Si existe un proxy inverso que termina el cifrado, también debes definir la protección y confianza del tramo hacia el backend. Las cabeceras reenviadas sobre esquema o IP sólo se deben confiar cuando proceden del proxy autorizado.

## 5. Sesiones, cookies y control de acceso

HTTP no exige mantener estado entre peticiones. Una sesión asocia solicitudes con un estado del servidor, normalmente utilizando un identificador impredecible que el navegador conserva en una cookie. La contraseña no debería viajar en cada URL. Una cookie de sesión robada puede permitir suplantación mientras siga siendo válida; por eso es un dato sensible.

`Secure` limita el envío a HTTPS, `HttpOnly` impide acceso mediante JavaScript del documento y `SameSite` ayuda a limitar ciertos envíos entre sitios. Ningún atributo sustituye todos los demás controles. La aplicación necesita caducidad, invalidación al cerrar sesión, renovación cuando cambia el privilegio y protección frente a peticiones falsificadas cuando corresponda.

Autenticación responde quién es la persona o proceso. Autorización decide qué operación puede realizar sobre qué recurso. Un usuario que conoce la URL de administración no adquiere permiso por conocerla. Prueba cada rol en una sesión distinta; ocultar un botón en el frontend no impide solicitar la operación al backend.

En WordPress, los roles habituales incluyen administrador, editor, autor, colaborador y suscriptor, con capacidades diferentes. Reserva administración para mantenimiento y usa una cuenta editorial para publicar. Un complemento puede añadir roles o capacidades; revisa sus efectos y no asumas que el nombre del rol describe todos sus permisos.

## 6. HTML semántico y CSS adaptable

HTML expresa estructura: `header`, `nav`, `main`, `section`, `article` y `footer` describen regiones y relaciones. Los encabezados ordenan contenido; `button` activa una acción y `a` navega hacia un recurso. Sustituir un botón por un `div` con un evento obliga a reconstruir interacción de teclado y semántica que el elemento correcto ya aporta.

CSS define presentación. El modelo de caja distingue contenido, relleno, borde y margen. Con `box-sizing: border-box`, el ancho declarado incluye relleno y borde, lo que facilita construir diseños previsibles. Flexbox y Grid permiten distribuir elementos sin tablas usadas como maquetación.

Un diseño adaptable no consiste únicamente en reducir tamaño. Debe reorganizar contenido, permitir zoom y evitar desbordamiento horizontal innecesario. Utiliza anchos relativos y máximos razonables; no fijes la página a una resolución de escritorio concreta. Una tabla de datos ancha puede tener desplazamiento propio, pero el texto principal debe seguir siendo legible en una ventana estrecha.

El JavaScript resulta útil para interacción, pero no es obligatorio para una página informativa. Si añades funcionalidades, considera qué ocurre cuando falla un script, tarda la red o la persona utiliza teclado. El sitio de ejemplo de este módulo funciona sin dependencias externas para que puedas inspeccionar todos sus recursos.

## 7. Accesibilidad y calidad

Las WCAG organizan requisitos alrededor de contenido perceptible, operable, comprensible y robusto. Para empezar, comprueba estructura, contraste, alternativas textuales, foco visible, teclado y formularios etiquetados. Los criterios y niveles concretos deben consultarse en la recomendación vigente; una comprobación automática parcial no certifica conformidad completa. [WCAG 2.2 del W3C](https://www.w3.org/TR/WCAG22/).

Incluye un enlace para saltar al contenido y un título de página significativo. No elimines el contorno de foco sin aportar un sustituto visible. Un `label` debe asociarse con su control, no ser solamente texto colocado al lado. Los errores deben explicar qué corregir y no depender únicamente del color rojo.

El texto alternativo depende del propósito. Si una imagen transmite el esquema de red, describe la relación que se necesita entender. Si el mismo contenido ya está explicado en el texto cercano y la imagen es decorativa, una alternativa vacía puede evitar repetición innecesaria. Prueba la navegación en un orden lógico y revisa el comportamiento al ampliar al 200%.

## 8. CMS, extensiones y mantenimiento

Un CMS reduce trabajo editorial, pero incorpora una superficie operativa. Cada extensión añade código, dependencias y mantenimiento. Evalúa procedencia, frecuencia de actualización, permisos, compatibilidad y procedimiento de retirada. Instalar varios complementos que modifican caché, autenticación o redirecciones puede crear interacciones difíciles de diagnosticar.

Una copia recuperable de WordPress debe contemplar base de datos, contenido subido, temas y extensiones necesarios, configuración e inventario de versiones. La exportación de entradas mediante el menú de herramientas no constituye una copia completa del sitio. Una instantánea de VM ayuda en el laboratorio, pero no sustituye una estrategia consistente si la base está escribiendo o si la única copia permanece en el mismo almacenamiento.

## 9. Aplicaciones colaborativas y salida del servicio

Para elegir entre una aplicación propia y una alojada compara finalidad, identidades, permisos, disponibilidad, residencia de datos, exportación, integración y costes. El coste propio incluye actualizaciones, copias, vigilancia y recuperación, no sólo alojamiento. El coste alojado incluye licencias, almacenamiento, límites y dependencia del proveedor.

Prueba la salida antes de introducir información importante. Exporta un documento, calendario o proyecto; impórtalo en una herramienta alternativa y anota pérdidas de comentarios, historial, permisos y adjuntos. Una API disponible no garantiza que exporte todas las funciones. En trabajo compartido define propietario institucional y plan para cuando una persona abandone la organización.

### Fuentes primarias

- [Guía de HTTP en MDN](https://developer.mozilla.org/es/docs/Web/HTTP).
- [Aprendizaje de desarrollo web en MDN](https://developer.mozilla.org/es/docs/Learn_web_development).
- [Tutoriales WAI del W3C](https://www.w3.org/WAI/tutorials/).
- [Documentación de WordPress](https://wordpress.org/documentation/).
- [Administración y seguridad de WordPress](https://developer.wordpress.org/advanced-administration/security/).
