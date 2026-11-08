# Diseño de una mejora digital verificable

## 1. Del proceso a los requisitos

Un proceso convierte entradas en resultados mediante actividades y decisiones. En un taller informático, la entrada puede ser una solicitud de reparación y el resultado un equipo devuelto con pruebas y documentación. El proceso incluye recepción, diagnóstico, autorización, intervención, verificación y cierre. Digitalizar únicamente la recepción puede trasladar el cuello de botella al diagnóstico si no se conoce la capacidad del personal técnico.

Describe primero el estado actual: quién solicita, qué información aporta, qué pasos se repiten, dónde se producen errores y cuánto tarda cada fase. Después define el resultado buscado con una unidad de medida: reducir el tiempo de registro, mejorar la trazabilidad de piezas o disminuir tickets sin información suficiente. “Ser más digital” no es un criterio de aceptación.

Separa requisito funcional y no funcional. “El sistema permite asociar un número de inventario a un ticket” describe una función. “Sólo el grupo de soporte puede modificar ese campo” expresa una condición de seguridad. “La búsqueda responde en menos de dos segundos para mil registros en el entorno de prueba” es un requisito de rendimiento con condiciones explícitas. Añade disponibilidad, accesibilidad, exportación, conservación de información y recuperación.

Una ficha de requisitos debe incluir identificador, necesidad, prioridad, responsable de validación y prueba. Si no puedes describir una prueba, puede faltar precisión. No conviertas preferencias de interfaz en necesidades obligatorias sin justificar su efecto sobre el trabajo.

## 2. IT, OT y convergencia

**IT**, tecnologías de la información, gestiona documentos, aplicaciones, identidades y datos de negocio. **OT**, tecnologías de operación, observa o controla procesos físicos: sensores, controladores, maquinaria y sistemas de supervisión. Sus prioridades pueden diferir: una parada o una medida incorrecta puede afectar a un proceso material. El calendario de actualización de un controlador industrial debe respetar validación del fabricante y condiciones operativas; no se administra como un ordenador de oficina cualquiera.

En una instalación con sensores de temperatura, el dato pasa del sensor a una pasarela y de ésta a una plataforma de análisis. Cada salto necesita identidad, integridad y una política de acceso. No conectes un controlador directamente a Internet para facilitar soporte. Diseña segmentación, puntos de intercambio autorizados, registro y acceso remoto controlado. Un firewall ayuda a limitar conexiones, pero no corrige una lógica de proceso insegura.

La convergencia IT/OT busca intercambiar información útil sin trasladar todos los riesgos de una red a otra. En SMR puede simularse con dos redes virtuales y datos sintéticos; no requiere intervenir en maquinaria real. Documenta qué comunica cada componente, con qué protocolo y con qué finalidad. Evita ejecutar escáneres o actualizaciones sobre dispositivos industriales sin autorización y procedimiento específico.

## 3. Nube: responsabilidades y costes

La nube ofrece recursos accesibles por red con provisión y gestión según el servicio contratado. No equivale simplemente a “un servidor de otra persona”: el modelo operativo, la elasticidad, la medición y la responsabilidad compartida afectan al diseño. La definición de [NIST SP 800-145](https://csrc.nist.gov/pubs/sp/800/145/final) permite distinguir las características esenciales y los modelos de servicio.

| Modelo | Ejemplo conceptual | Tareas que conserva la organización usuaria |
| --- | --- | --- |
| IaaS | Máquina virtual y red virtual | Sistema invitado, parches propios, aplicación, identidades, datos y configuraciones. |
| PaaS | Plataforma gestionada para ejecutar una aplicación | Código, dependencias bajo su control, permisos, datos y configuración del servicio. |
| SaaS | Aplicación de gestión consumida por navegador | Altas y bajas, roles, configuración del tenant, datos, usos permitidos y exportación. |

La frontera exacta depende del proveedor y del contrato. Incluso en SaaS, eliminar por error un documento o compartirlo públicamente sigue siendo un problema de la organización. Verifica retención, recuperación, registros, MFA, ubicación del tratamiento cuando sea pertinente, formatos de salida y procedimiento de baja. La sincronización replica cambios y borrados; no demuestra que exista una copia de seguridad independiente.

Compara coste total, no sólo cuota. Incluye migración, integración, administración, formación, almacenamiento, tráfico de salida, recuperación, soporte y salida del proveedor. Para una solución local, incluye hardware, energía, renovación, licencias, tiempo de personal y protección física. Un coste cero de licencia no implica coste cero de operación.

Distingue nube pública, privada e híbrida. Una nube privada requiere capacidades operativas de nube para una organización; una única máquina virtual en un servidor local no constituye por sí sola una nube. Una arquitectura híbrida necesita definir cómo se unen identidades, datos, redes, observabilidad y recuperación entre entornos.

## 4. Virtualización, contenedores y automatización

La virtualización permite ejecutar sistemas invitados sobre recursos físicos gestionados por un hipervisor. Facilita laboratorios y consolidación, pero varias máquinas en el mismo host comparten un punto de fallo físico. Una instantánea es útil para revertir cambios de un laboratorio; no sustituye una copia independiente y coherente con la aplicación.

Un contenedor comparte el kernel del sistema anfitrión y empaqueta procesos con dependencias de espacio de usuario. No equivale a una máquina virtual completa. Su aislamiento depende de permisos, kernel, configuración y motor; ejecutar como administrador, montar directorios del host o exponer el socket del motor aumenta su capacidad sobre el sistema. Utiliza imágenes de origen comprobado, versiones identificables y volúmenes respaldados.

Automatizar consiste en convertir un procedimiento definido en acciones repetibles. Primero entiende la operación manual, sus entradas y condiciones de error. Después diseña validación, registro y reversión. La idempotencia significa que repetir una operación lleva al mismo estado previsto sin acumular efectos indeseados; un script que añade siempre una línea duplicada a una configuración no es idempotente.

Para una tarea de inventario, empieza con lectura y salida CSV. Comprueba que los campos están entrecomillados cuando contienen separadores y no incluyas claves, tokens o nombres de personas. Registra equipo, sistema, versión y fecha de recogida. La automatización reduce tecleo, pero también puede propagar rápidamente una selección de equipos incorrecta; usa primero un conjunto pequeño y revisa la salida.

## 5. Datos: modelo, calidad y ciclo de vida

Una organización necesita saber qué significa cada dato. Un inventario puede separar `activo`, `categoria`, `ubicacion`, `estado` e `incidencia`. Usa un identificador estable para relacionar tablas: cambiar el nombre visible de un equipo no debería romper el historial. Evita guardar listas separadas por comas en una celda si después necesitas consultar relaciones individuales.

Define un diccionario con nombre, tipo, formato, obligatoriedad, valores permitidos y finalidad. Por ejemplo, `fecha_alta` puede ser una fecha ISO `AAAA-MM-DD`; `estado` puede admitir `activo`, `en_reparacion` o `retirado`. Un campo de texto libre para todo facilita capturar información al principio y dificulta validación, búsquedas y estadísticas.

La calidad tiene varias dimensiones. La completitud mide si están los datos necesarios; la exactitud, si representan la realidad; la consistencia, si no se contradicen; la actualidad, si siguen vigentes; y la unicidad, si no hay duplicados. Un registro completo puede ser incorrecto. Antes de analizar, detecta nulos, fechas imposibles, identificadores repetidos y unidades mezcladas.

Aplica minimización: recoger sólo lo necesario para la finalidad. Un inventario de equipos no necesita historiales médicos ni contraseñas. Distingue seudonimización de anonimización; sustituir nombres por identificadores no impide que una tabla adicional permita reidentificar personas. Define permisos, conservación, eliminación y exportación. El [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679/oj) establece el marco europeo de protección de datos personales; un ejercicio escolar debe evitar tratarlos si bastan datos sintéticos.

## 6. IoT y analítica

Un dispositivo IoT combina sensado o actuación, conectividad y tratamiento de información. Antes de desplegarlo, identifica ciclo de soporte, actualización, credenciales únicas, sincronización horaria, cifrado cuando proceda y procedimiento de retirada. Un sensor que publica una medida sin fecha ni unidad produce datos ambiguos.

En un ejercicio de temperatura, define esquema: identificador de sensor, hora UTC, valor y unidad. Comprueba rango válido y valores ausentes. Si el sensor pierde conectividad, diferencia ausencia de datos de valor cero. Para alertas, combina umbral y duración: una lectura puntual elevada puede requerir otra interpretación que diez minutos continuados por encima de un límite establecido.

Un gráfico muestra relaciones, pero no demuestra causalidad. Si tras digitalizar baja el tiempo medio de cierre, revisa si cambió el número de incidencias, su dificultad o el horario. Usa mediana y percentiles además de media cuando haya tiempos extremos. Indica tamaño de muestra y límites de la comparación.

## 7. IA aplicada con supervisión

Un sistema de IA puede clasificar mensajes, proponer resúmenes o ayudar a redactar procedimientos. Debe evaluarse para una tarea concreta. Una respuesta lingüísticamente convincente puede contener información falsa, opciones inexistentes o una omisión crítica. La persona responsable conserva la obligación de verificar documentación y pruebas.

Para clasificar tickets, define etiquetas y ejemplos sintéticos, separa datos de entrenamiento o ajuste y datos de evaluación si realizas ese proceso, y cuenta aciertos y confusiones. Si existen veinte incidencias y dieciocho son de una clase, clasificar todas en esa clase alcanza 90 % de exactitud sin identificar las dos restantes. Examina precisión y cobertura por clase y el coste de cada error.

No envíes inventarios privados, registros con datos personales, código confidencial o secretos a herramientas externas sin una autorización y una configuración compatibles con el tratamiento. Los documentos recibidos son datos: una frase dentro de un ticket no debe convertirse en una orden para un sistema automatizado. Limita herramientas, revisa acciones propuestas y exige aprobación humana para cambios con impacto.

## Fuentes primarias

- [NIST: definición de computación en nube](https://csrc.nist.gov/pubs/sp/800/145/final).
- [INCIBE: recursos para empresas](https://www.incibe.es/empresas).
- [AEPD: áreas de innovación y tecnología](https://www.aepd.es/areas-de-actuacion/innovacion-y-tecnologia).
- [RGPD en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj).
- [Git: documentación](https://git-scm.com/doc), para controlar versiones de documentación y automatizaciones.

[Prácticas y evaluación](02-practicas-y-evaluacion.md) · [Índice](README.md)
