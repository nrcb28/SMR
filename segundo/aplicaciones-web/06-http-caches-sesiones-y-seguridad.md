# 6. HTTP en operación: cachés, sesiones y controles de aplicación

[Índice](README.md) · [Guía base HTTP](01-fundamentos.md)

## 1. Representaciones y capas de caché

Un recurso puede tener varias representaciones según idioma, compresión, identidad o formato. La URL no basta siempre para decidir si dos respuestas pueden compartirse. La caché del navegador, una caché intermediaria y la caché de página del CMS actúan en puntos diferentes y tienen reglas distintas. Vaciar una no garantiza eliminar las otras.

El objetivo de caché es reutilizar una respuesta cuando lo permite su política y sus validadores. La frescura responde durante cuánto tiempo puede reutilizarse sin consultar de nuevo; la validación comprueba si una copia almacenada sigue vigente. Un 304 ahorra transferir el cuerpo, pero no elimina la petición y la comparación asociada.

Para un archivo CSS con un nombre que cambia al modificar su contenido, puede ser adecuado un periodo largo de caché. Para una página personal con datos de una sesión, una caché pública puede causar exposición. La política se elige según significado y arquitectura, no aplicando una cabecera idéntica a todo el sitio porque mejora una puntuación de rendimiento.

## 2. Cache-Control sin confundir las directivas

`no-store` pide no almacenar la respuesta en las cachés a las que se aplica. `no-cache` permite almacenarla, pero exige validarla antes de reutilizarla. `private` restringe el almacenamiento a cachés privadas. `max-age` expresa un periodo de frescura. Estas directivas no son sinónimos y combinarlas indiscriminadamente dificulta explicar la política.

Ejemplos conceptuales:

| Recurso | Política ilustrativa | Razón |
| --- | --- | --- |
| CSS versionado de un sitio estático | `public, max-age=3600` en el ejercicio | Reutilizar una representación idéntica durante una hora |
| HTML informativo que cambia con frecuencia | `no-cache` con validadores | Conservar una copia, pero consultar vigencia |
| Página con información personal | `private, no-store` según requisitos | Evitar almacenamiento compartido y conservación no prevista |

Las cabeceras son parte del diseño; la aplicación y el proxy deben mantener coherencia. No añadas caché pública a una respuesta con contenido de usuario sin revisar cómo se diferencia la identidad. Tampoco interpretes que `no-store` elimina automáticamente copias previamente obtenidas, capturas o datos almacenados por código de aplicación.

## 3. ETag y peticiones condicionales

`ETag` identifica una versión de una representación según el servidor. No tiene por qué ser un hash criptográfico del archivo y no debe usarse como prueba de integridad de una descarga salvo que el proveedor defina expresamente ese contrato. Los validadores débiles y fuertes tienen semántica distinta; observa qué emite realmente la aplicación.

En el laboratorio estático, obtén primero cabeceras y cuerpo con `curl`. El servidor local puede no generar todos los validadores; documenta el caso en lugar de inventar una cabecera. En Nginx configurado para archivos estáticos puedes inspeccionar un recurso conocido:

```bash
curl --head --cacert /etc/ssl/certs/ca-certificates.crt \
  https://wp.aula.test/recurso-estatico-conocido.css
```

Sustituye la ruta por una que exista y cuyo comportamiento esté controlado. Copia el valor exacto de `ETag`, con sus comillas y prefijo si lo hay, y úsalo en `If-None-Match`. Si la representación no cambia y la política es compatible, una respuesta 304 demuestra revalidación. Un 200 no implica necesariamente error: puede haber cambiado contenido, variar la representación o no atender ese validador.

Cuando pruebes con `curl -I`, recuerda que estás enviando HEAD, no descargando cuerpo. Para comparar contenido usa GET y guarda una copia sintética en una ruta de trabajo. No midas bytes transferidos únicamente por el tamaño del archivo si hay compresión o recursos adicionales. Registra método, estado, cabeceras relevantes y condición de la prueba.

## 4. Vary, compresión y contenido personalizado

`Vary` indica qué cabeceras de la petición participaron en la selección de la representación y deben tenerse en cuenta para reutilizarla. Es habitual que la compresión se relacione con `Accept-Encoding`, pero las capas concretas pueden transformar la respuesta. Si un proxy mezcla respuestas comprimidas y no comprimidas bajo una clave incompleta, el resultado puede ser incorrecto aunque el origen funcione.

La personalización requiere especial cuidado. Una página con saludo y permisos de un usuario no se convierte en pública por tener una URL que parece un documento. Decide dónde se mantiene sesión y qué condiciones impiden caché compartida. Una prueba negativa útil abre el recurso con dos identidades en sesiones independientes y verifica que no se reutiliza contenido privado.

En CMS, varias extensiones pueden gestionar caché, minificación y cabeceras. Antes de añadir otra, inventaría las existentes y define la responsabilidad de cada capa. Un fallo intermitente después de actualizar CSS puede provenir de nombres no versionados, CDN, plugin, navegador o service worker. Vaciar todo a la vez puede recuperar el sitio sin identificar la causa.

## 5. Cookies: alcance y atributos

Una cookie es un dato que el navegador guarda y envía según dominio, ruta y otras condiciones. La cookie no «sabe» si representa una sesión, preferencia o seguimiento; ese significado lo asigna la aplicación. No coloques una contraseña en una cookie como sustituto de un identificador de sesión adecuado.

`Secure` limita su envío a contextos de transporte apropiados; `HttpOnly` evita el acceso ordinario mediante JavaScript del documento; `SameSite` modifica envíos en determinados contextos entre sitios. `Path` organiza alcance de envío, pero no constituye una frontera robusta de aislamiento entre aplicaciones del mismo origen. Una política segura necesita comprender también dominio, caducidad y regeneración.

Origen y sitio no son idénticos. Un origen incluye esquema, host y puerto; el concepto de sitio utilizado por ciertas reglas del navegador se basa en otros criterios. Dos subdominios pueden pertenecer al mismo sitio y ser orígenes distintos. Por eso una defensa que depende sólo de `SameSite` no cubre automáticamente toda relación entre aplicaciones de una organización.

Observa cookies en las herramientas del navegador, pero no publiques sus valores. Para una memoria basta identificar nombre ficticio, atributos y comportamiento. Una captura con una cookie válida puede equivaler a compartir una credencial temporal. Cerrar una ventana no demuestra invalidar la sesión en el servidor.

## 6. Sesión y autorización comprobadas por separado

La autenticación establece una identidad y la sesión permite relacionar peticiones con ese estado. La autorización decide si esa identidad puede ejecutar una operación sobre un objeto. Una pantalla de inicio de sesión correcta no garantiza que todos los endpoints comprueben permisos.

Construye una matriz de operaciones: leer página pública, crear borrador, publicar, modificar contenido ajeno, instalar extensión y administrar usuarios. Asigna cuentas de laboratorio con roles distintos y prueba cada operación mediante la interfaz permitida. Si falta un botón, no concluyas todavía que el servidor deniega la operación: la interfaz es una evidencia parcial del control.

Un servicio real necesita caducidad, invalidación, recuperación de cuenta y protección del identificador de sesión. Utiliza mecanismos mantenidos de la aplicación o framework; no diseñes un token predecible con hora y nombre. En WordPress mantén roles y capacidades según necesidad y revisa cómo los plugins pueden ampliarlas.

## 7. CSRF, XSS e inyección SQL: problemas diferentes

CSRF intenta provocar que un navegador autenticado envíe una operación que la persona no pretendía realizar. La defensa puede incluir tokens adecuados, comprobación de origen, métodos coherentes y atributos de cookie, según arquitectura. Usar POST por sí solo no demuestra protección, y `SameSite` forma parte de una defensa, no de una garantía universal.

XSS aparece cuando datos no confiables se interpretan como código en un contexto de la aplicación. La respuesta consiste en controlar cómo se produce la salida y utilizar APIs/plantillas adecuadas al contexto, además de otras defensas. En la demostración local se usa `textContent` para un síntoma; eso evita interpretar ese dato como HTML en ese punto. No justifica insertar el mismo valor sin tratarlo dentro de una URL o un script.

La inyección SQL surge al mezclar datos con estructura de una consulta de forma que el dato altera su significado. Utiliza consultas parametrizadas en el backend y un usuario de base con permisos ajustados. Escapar manualmente una comilla no sustituye un mecanismo correcto ni resuelve el diseño de autorización. La validación de JavaScript no impide que otro cliente envíe una petición diferente.

No es necesario explotar un sitio externo para aprender estas diferencias. Revisa fragmentos didácticos, identifica la frontera de confianza y explica qué componente debe aplicar el control. En los ejercicios utiliza tu entorno aislado y datos sintéticos; las pruebas sobre servicios ajenos requieren su autorización y alcance explícito.

## 8. CSP, cabeceras y límites de una lista de comprobación

Una política de seguridad de contenido puede limitar fuentes de scripts y otros recursos y contribuir a reducir ciertos efectos de una inyección. Su diseño depende de cómo carga recursos la aplicación. Copiar una política muy restrictiva sin inventario puede romper el editor, fuentes o plugins del CMS; abrir todo con comodines para eliminar errores anula parte de su finalidad.

Empieza inventariando recursos y, cuando la plataforma lo permita, ensaya una política de reporte en el clon antes de imponerla. Revisa informes con datos mínimos y correlaciona con funcionalidades. Una cabecera presente no demuestra que la política sea efectiva ni que se evalúen todos los caminos de la aplicación.

`X-Content-Type-Options: nosniff` y una política de referencia ayudan a controlar comportamientos específicos. HSTS también tiene consecuencias: puede fijar el uso de HTTPS y propagarse a subdominios según directivas. No actives políticas persistentes de forma indiscriminada sobre nombres de laboratorio si después quieres ensayar HTTP; documenta alcance y retirada.

## 9. Accesibilidad y seguridad se encuentran en los flujos de error

Un formulario protegido debe comunicar errores sin revelar datos innecesarios. Un fallo de inicio de sesión no debería confirmar de forma indiscriminada qué cuentas existen, pero tampoco debe dejar a la persona sin una vía comprensible de recuperación. La solución combina mensajes, límites y un flujo adecuado a la aplicación, no simplemente volver todos los errores idénticos sin contexto.

Si caduca la sesión durante una edición, conserva o recupera el trabajo según el modelo autorizado y explica qué ha ocurrido. Un 403 mostrado como página vacía causa reintentos inútiles y puede hacer que el usuario copie datos en canales inseguros para pedir ayuda. El procedimiento de soporte debe recoger código, momento y referencia, sin solicitar contraseñas o cookies.

Prueba foco y mensajes tras error, navegación de vuelta y duplicidad de envío. Un doble clic no debe crear dos cobros o dos altas en un sistema real sin una política de idempotencia. En el laboratorio, identifica ese requisito en el diseño aunque no implementes un servicio transaccional completo.

## 10. Práctica de diagnóstico HTTP y sesión

Selecciona un recurso estático de laboratorio y una página editorial. Obtén cabeceras, clasifica qué contenido puede compartirse y explica los validadores observados. No modifiques globalmente el CMS para obtener un 304 si su respuesta no es cacheable: el objetivo es interpretar el comportamiento real.

Con dos roles de WordPress, construye una matriz de seis operaciones y registra permiso esperado y real. Usa perfiles de navegador separados o sesiones aisladas, evitando que cookies almacenadas mezclen identidades. Completa una prueba de cierre de sesión y revisa que una página privada no quede servida como contenido público desde una capa de caché.

Entrega tabla de cabeceras, explicación de cachés, matriz de permisos y tres casos de error. Añade propuestas de mejora vinculadas a evidencias, distinguiendo un defecto confirmado de una hipótesis. Rúbrica propia: interpretación HTTP 30 %, identidades y permisos 25 %, análisis de amenazas y controles 25 %, pruebas y comunicación 20 %.

## Referencias primarias

- [MDN: caché HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching), [Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) y [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/ETag).
- [MDN: cookies seguras](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/Cookies) y [gestión de sesiones](https://developer.mozilla.org/en-US/docs/Web/Security/Authentication/Session_management).
- [MDN: CSRF](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF) y [seguridad web](https://developer.mozilla.org/en-US/docs/Web/Security).
- [WordPress: seguridad](https://developer.wordpress.org/advanced-administration/security/): controles y mantenimiento en el CMS.
