# 5. Frontend progresivo: DOM, eventos, formularios y accesibilidad

[Índice del módulo](README.md) · [Demostración local](ejemplos/registro-local/index.html) · [JavaScript](ejemplos/registro-local/app.js)

## 1. Un frontend que se puede explicar

El navegador transforma el HTML en una estructura de objetos denominada DOM. CSS participa en la presentación y JavaScript puede leer o modificar esa estructura y responder a eventos. No son tres archivos independientes que se ejecuten sin relación: el orden de carga, los selectores y el estado de la página determinan qué ocurre.

La finalidad de este capítulo es construir una interacción pequeña que permita razonar sobre cada paso. La [demostración de registro local](ejemplos/registro-local/index.html) presenta información útil sin JavaScript y ofrece una simulación adicional cuando se carga el script. No tiene backend, no guarda datos y no envía solicitudes con el formulario. Utiliza exclusivamente códigos y síntomas ficticios.

La mejora progresiva empieza con una base que conserva sentido por sí misma. En este caso, estructura, tabla de referencia e instrucciones son HTML ordinario. La zona interactiva se muestra cuando se han encontrado sus elementos y preparado los controladores. No se considera equivalente a un sistema de tickets real: persistencia, autenticación y autorización pertenecerían al servidor.

## 2. Identificar objetos y mantener separadas las responsabilidades

Un selector como `document.querySelector('#codigo')` devuelve un elemento o `null`. Si el código usa inmediatamente `.value` sin comprobar existencia, un cambio en el HTML puede producir una excepción que impida el resto de la interacción. Selecciona el conjunto de elementos que necesita una función y verifica precondiciones antes de activarla.

Los identificadores deben ser únicos en el documento. Reutilizar `id="error"` en varios campos hace ambiguas las referencias y puede provocar que el navegador o una tecnología de apoyo encuentre un elemento distinto del previsto. Usa identificadores específicos y conecta cada campo con su etiqueta y mensajes mediante relaciones explícitas.

Separa la validación de la manipulación visual. Una función pura recibe datos y devuelve errores y valores normalizados, sin leer directamente el DOM. El controlador de envío recoge las entradas, llama a esa función y representa su resultado. Así puedes probar reglas sin simular todo el navegador y reduces acoplamiento entre texto de interfaz y modelo.

En el ejemplo, `validarDatos` comprueba código, categoría y descripción. El normalizado recorta espacios y convierte el código a mayúsculas; no modifica arbitrariamente el síntoma ni intenta «corregir» palabras técnicas. Un normalizado útil tiene un alcance definido. Eliminar todos los signos para evitar problemas puede destruir información de un mensaje de error.

## 3. Eventos y comportamiento de los controles

Un evento comunica que ha ocurrido algo: activación, escritura, envío o cambio de foco. `addEventListener` permite asociar un controlador sin mezclar código dentro de los atributos HTML. La función recibe el evento y decide si debe conservar o cancelar su comportamiento predeterminado.

En un formulario real, enviar puede iniciar una petición o navegación. La demostración utiliza `preventDefault()` en el evento `submit` porque su propósito es trabajar sólo en memoria. Esta cancelación debe ser explícita y estar documentada. Un botón sin `type` dentro de un formulario suele actuar como envío; para acciones secundarias, como limpiar la lista, especifica `type="button"`.

El botón de reinicio nativo devuelve valores iniciales, pero no conoce tus mensajes, estados ARIA o filas creadas por JavaScript. Si necesitas reiniciar la interfaz, restablece también esos elementos de manera controlada. En el ejemplo hay una acción separada para vaciar únicamente las filas generadas durante la sesión y conservar la tabla de referencia estática.

No ejecutes validación agresiva en cada pulsación si la persona todavía está escribiendo un dato. Un código incompleto puede ser normal durante la entrada. Define cuándo mostrar errores: al intentar registrar, al abandonar un campo o después de corregir un error previo. Mantén los mensajes estables y evita mover el foco de forma inesperada mientras se escribe.

## 4. Formularios semánticos y mensajes comprensibles

Un `label` asociado mediante `for` e `id` identifica el campo y permite activarlo desde el texto. Un placeholder es una pista temporal, no reemplaza la etiqueta. Utiliza un texto de ayuda estable para el formato, por ejemplo «PC-001: PC, guion y tres cifras». Indicar «formato incorrecto» después del error resulta menos útil que explicar cómo corregirlo.

Agrupa controles relacionados con `fieldset` y `legend` cuando su significado lo requiera. Usa tipos de entrada apropiados y no conviertas todos los valores en números: un código `PC-001` o un identificador con ceros iniciales es texto. Los límites como longitud máxima deben corresponder a una regla del caso y aparecer en las instrucciones.

La validación HTML nativa puede ayudar con obligatoriedad y formato. En una validación personalizada, decide de manera consciente si mantienes el mecanismo nativo o si el script desactiva su presentación para gestionar mensajes coherentes. No mezcles ambos sin probar: una validación nativa puede impedir que se dispare `submit`, y tu resumen de errores no llegará a mostrarse.

El ejemplo activa su validación propia sólo cuando el script se ha preparado y establece entonces `noValidate`. Cada error se relaciona con su control mediante `aria-describedby`, y se actualiza `aria-invalid`. Un resumen enfocable enumera problemas y ofrece enlaces a los campos. La aceptación exige poder entender y corregir errores con teclado, no únicamente observar texto rojo.

## 5. Foco, anuncios y orden de navegación

El orden normal de tabulación sigue el documento y los controles interactivos. Evita números positivos de `tabindex` para reconstruir manualmente un orden que después deja de corresponder con la presentación. Reorganiza el HTML cuando su secuencia sea incorrecta y utiliza CSS para presentación sin romper el sentido de lectura.

Si el envío tiene errores, mover el foco al resumen permite conocer el conjunto antes de corregir. Ese resumen utiliza `tabindex="-1"` para recibir foco programático sin añadir una parada habitual. Sus enlaces dirigen a cada campo. Si el envío es válido, un mensaje de estado anuncia el registro local y el formulario conserva una siguiente acción previsible.

Un área con `role="status"` comunica cambios no urgentes de forma compatible con tecnologías de apoyo. No conviertas todos los cambios en alertas: una aplicación que anuncia cada carácter o cada filtro puede saturar la navegación. Prueba el momento y el contenido del anuncio en el entorno real; asignar un atributo ARIA no garantiza que la experiencia completa sea adecuada.

El foco debe ser visible y conservar contraste. No uses `outline: none` por motivos estéticos sin sustituto equivalente. En pantallas pequeñas o con cabeceras fijas, comprueba que un elemento enfocado no quede cubierto. La conformidad con WCAG 2.2 requiere evaluar los criterios aplicables; este ejercicio practica un subconjunto y no presenta una certificación completa.

## 6. Insertar datos como texto

Cuando un síntoma se muestra en la tabla, crea nodos y asigna `textContent`. Si el usuario introduce caracteres como `<` y `>`, deben verse como texto. No se interpreta esa descripción como HTML ni se construye una plantilla mezclando entrada con `innerHTML`. La regla reduce una clase de errores de inyección en este punto concreto.

No deduzcas de ello que el sistema está «asegurado contra XSS» en todos sus componentes. Los contextos HTML, atributos, URL, CSS y JavaScript tienen reglas distintas, y una aplicación real necesita defensas del framework y del servidor. La demostración evita deliberadamente un contexto complejo para que puedas observar el dato y su representación sin introducir ejecución de contenido.

Los identificadores de ticket que genera el ejemplo pertenecen sólo a la sesión. Dos páginas abiertas pueden producir la misma secuencia y al recargar se pierde. Una aplicación con persistencia debería generar identidad e integridad en su modelo, tratar concurrencia y comprobar permisos. No lleves el contador del navegador a un servicio multiusuario esperando unicidad global.

## 7. Persistencia y límites del almacenamiento del navegador

No todo dato introducido debe guardarse. El ejemplo mantiene la información en memoria y explica que se pierde al recargar. Esto permite estudiar validación sin almacenar descripciones potencialmente sensibles. Antes de añadir persistencia, decide finalidad, duración, acceso y procedimiento de eliminación.

`localStorage` es accesible al JavaScript del mismo origen y no sustituye un almacén de secretos. Un token de sesión con privilegios no debe introducirse allí sólo por comodidad. Las cookies con `HttpOnly` tienen un modelo de acceso distinto, y un servicio real debe diseñar autenticación y caducidad según su arquitectura. La elección requiere comprender el riesgo y no copiar un fragmento aislado.

Un navegador puede limitar o borrar almacenamiento, y las pestañas pueden tener estados diferentes. Una interfaz que muestra «guardado» antes de confirmar la operación del servidor induce a error. En una aplicación real distingue validación local, envío pendiente, confirmación y fallo; en esta demostración el mensaje dice explícitamente «añadido a esta vista local».

## 8. Depuración sin modificar varias capas a la vez

Abre las herramientas de desarrollo y comprueba Consola y Red. Un archivo JavaScript con 404 no se corrige cambiando las reglas de validación; un error de sintaxis impide ejecutar el archivo; un selector incorrecto puede dejar inactiva una parte sin afectar la carga HTTP. Sigue la secuencia recurso, análisis, ejecución, selección de elementos y evento.

Coloca un punto de interrupción dentro del controlador de envío y observa los datos antes y después de normalizar. No añadas `console.log` con contraseñas o datos reales en una aplicación de producción. Para esta práctica utiliza exclusivamente valores sintéticos y elimina registros temporales de depuración que no aporten valor al ejemplo final.

El script se carga con `defer`, por lo que se ejecuta después del análisis del documento y antes del evento correspondiente de carga del DOM. Si cambias a una carga asíncrona o insertas el script dinámicamente, revisa esa dependencia. «Funciona en mi recarga» no demuestra que el orden sea estable bajo otras condiciones de carga.

## 9. Matriz de pruebas del ejemplo

| Caso | Entrada o condición | Resultado esperado |
| --- | --- | --- |
| Base sin script | JavaScript desactivado | Información estática e instrucciones siguen disponibles; zona interactiva oculta |
| Código normalizado | ` pc-007 ` | Se interpreta como `PC-007` |
| Código inválido | `equipo7` | Error de formato asociado al campo |
| Categoría no permitida | Valor que no pertenece a la lista del modelo | Error de categoría, aunque se altere el DOM |
| Síntoma corto | Menos de diez caracteres tras recortar | Error que explica el mínimo |
| Texto con signos | Descripción sintética que contiene `<dato>` | Se muestra literalmente, sin interpretarlo como marcado |
| Dos tickets del mismo activo | Mismo código con síntomas distintos | Dos registros locales: un activo puede tener varias incidencias |
| Recarga | Añadir y recargar | Se pierde la lista de la sesión, según lo advertido |
| Teclado | Tabular y activar botones | Foco visible, orden coherente y posibilidad de corregir errores |

Estas son expectativas para ejecutar, no un registro de una auditoría de navegador realizada en tu VM. Conserva resultado real, navegador y versión al probarlas. La comprobación de la función pura no sustituye probar foco, anuncios, reflujo y lectura de la tabla.

## 10. Práctica: ampliar sin romper la base

Ejecuta el ejemplo desde un servidor de archivos estáticos ligado a loopback si utilizas un entorno local. Por ejemplo, desde su carpeta, `python3 -m http.server 8000 --bind 127.0.0.1`; accede sólo desde el mismo equipo mediante `http://127.0.0.1:8000/`. Detén el proceso al terminar. No uses ese servidor de desarrollo para publicar un CMS ni para atender tráfico externo.

Añade una nueva categoría acordada y modifica tanto el HTML como la lista de reglas. Después agrega un filtro visual que no borre los registros. Define qué debe ocurrir si no hay coincidencias y proporciona un mensaje comprensible. Evita hacer la tabla inaccesible sustituyéndola por elementos sin relaciones semánticas.

Entrega HTML, CSS, JS, diccionario de entradas y matriz de pruebas con casos válidos e inválidos. Explica qué parte validaría nuevamente un backend y qué controles de autorización no existen en el ejemplo. Rúbrica propia: estructura y mejora progresiva 25 %, validación y mensajes 25 %, representación segura 20 %, pruebas de teclado y reflujo 20 %, explicación de límites 10 %.

## Referencias primarias

- [MDN: introducción al DOM](https://developer.mozilla.org/es/docs/Web/API/Document_Object_Model/Introduction).
- [MDN: eventos](https://developer.mozilla.org/es/docs/Learn_web_development/Core/Scripting/Events).
- [W3C WAI: formularios](https://www.w3.org/WAI/tutorials/forms/) y [notificación de errores](https://www.w3.org/WAI/tutorials/forms/notifications/).
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): criterios aplicables de interacción, contenido y presentación.
