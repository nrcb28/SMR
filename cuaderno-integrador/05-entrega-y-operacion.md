# Entrega técnica, cambios y operación de un servicio

[Cuaderno](README.md) · [Proyecto intermodular](../segundo/proyecto-intermodular/README.md)

## 1. Qué significa entregar una infraestructura

Una infraestructura no se entrega únicamente porque un instalador termina o una página abre una vez. La persona que la recibe necesita conocer qué servicio ofrece, quién puede utilizarlo, de qué depende, cómo se comprueba y qué hacer cuando falla. La documentación permite conservar el resultado después de que cambie quien hizo la práctica.

En SMR conviene distinguir tres productos relacionados: diseño previsto, configuración aplicada y evidencia observada. Un diagrama expresa intención; un archivo configura una parte del sistema; una prueba muestra un comportamiento bajo condiciones concretas. Las diferencias entre los tres deben registrarse, porque una configuración puede no estar cargada y un diagrama puede haber quedado desactualizado.

Este capítulo propone un método de entrega para el laboratorio y el proyecto. Sus roles, plantillas y criterios son didácticos. En empresa se adaptan a sus procedimientos, supervisión y confidencialidad, como se explica en [formación en empresa](../docs/formacion-en-empresa.md).

## 2. Pasar de una petición vaga a requisitos comprobables

Petición inicial: «queremos que los archivos estén seguros y sean fáciles de usar». Es necesario concretar población, operaciones, datos, periodo y límites. Por ejemplo: «el grupo lector puede leer documentos del recurso; el editor puede crearlos y modificarlos; una identidad ajena no puede listar su contenido». Cada frase permite preparar una prueba.

Un requisito debe tener un identificador estable. Es útil mantener la relación entre origen, decisión, componente y prueba. No utilices una captura como sustituto del requisito: antes de probar hay que definir qué se espera observar.

| ID | Requisito didáctico | Decisión asociada | Prueba de aceptación |
| --- | --- | --- | --- |
| DOC-01 | Lectores sin modificación | Autorización mediante grupos y ACL | Leer y después intentar modificar con cuenta lectora |
| DOC-02 | Recuperar datos y permisos | Copia compatible y procedimiento ensayado | Restauración en otra ruta y matriz de identidades |
| DOC-03 | Web interna con identidad validable | Nombre controlado y CA de laboratorio | URL normal con confianza y nombre correctos |
| DOC-04 | Operación por una segunda persona | Runbook con precondiciones y retorno | Revisión o ejecución supervisada desde estado conocido |

Evita palabras que no tienen una prueba definida: «rápido», «intuitivo», «robusto» o «seguro» necesitan contexto. Un objetivo de velocidad debe indicar operación, tamaño de datos, carga y umbral. Una exigencia de seguridad debe identificar amenaza o acceso que se quiere controlar.

## 3. Inventario y propiedad operativa

Un inventario útil relaciona servicio y activo. Incluye identificador, rol, versión, ubicación lógica, dependencias, responsable funcional, procedimiento y ciclo de mantenimiento. La información sensible se conserva en el sistema autorizado de la organización; el repositorio público sólo debe contener datos sintéticos o saneados.

La propiedad operativa responde quién decide, quién ejecuta y quién recibe avisos. Una cuenta técnica de servicio no es una persona responsable. Si nadie recibe y revisa fallos del backup, tener una tarea programada no garantiza continuidad.

Para el laboratorio, registra `srv01` como rol de servicios y las funciones activas en cada escenario. Si BIND y Samba AD son laboratorios alternativos, deja constancia de ello. No dibujes todas las funciones estudiadas como si estuvieran activas simultáneamente en una sola VM.

## 4. Documentar una decisión técnica

Una decisión debe conservar problema, alternativas, criterios, elección, consecuencias y fecha o versión. La [plantilla de decisión](../recursos/plantillas/decision-tecnica.md) evita que la memoria se reduzca a «elegimos X porque es mejor».

Ejemplo sintético: un recurso para seis personas necesita lectura/escritura por grupos, sin políticas centralizadas del puesto. Se comparan Samba independiente y un directorio centralizado. El primero puede reducir componentes del ejercicio, pero mantiene administración de identidades específica del servidor; el segundo permite ampliar centralización y políticas a costa de dependencias de DNS, tiempo y operación.

Si el requisito no exige dominio, puede justificarse Samba independiente con límites explícitos. Si se añaden políticas de equipo centralizadas o integración con una identidad ya existente, la decisión debe revisarse. No se concluye que una opción sea universalmente adecuada: se conserva para qué requisitos y contexto fue elegida.

La decisión debe incluir condiciones que la invalidan. Por ejemplo, aumento de identidades, necesidad de SSO, cambios de soporte o requerimientos de recuperación. Esto permite explicar una evolución sin fingir que el diseño inicial resolvía necesidades que todavía no existían.

## 5. Configuración prevista, efectiva y persistente

Un archivo editado puede no corresponder al servicio activo. Revisa ruta, inclusiones, entorno y unidad que lo carga. Una opción introducida en una consola puede ser temporal, mientras un gestor restaura su estado al reiniciar. La entrega debe indicar cómo se conserva la configuración.

Para cada cambio registra objeto y prueba. En DNS: zona, serial, validación y consulta. En Nginx: virtual host habilitado, sintaxis, listeners y petición por nombre. En permisos: ACL y operación con identidad. En backup: configuración, destino verificado, ejecución y restauración.

Una copia del archivo anterior facilita retorno, pero hay que protegerla si contiene secretos. No basta con añadir `.bak` dentro del directorio web: podría convertirse en una copia descargable de credenciales. Utiliza una ubicación y permisos adecuados, y conserva únicamente material saneado en Git.

## 6. Planificar un cambio

El [plan de cambio](../recursos/plantillas/plan-de-cambio.md) relaciona motivo, alcance, precondiciones, impacto, ejecución, validación y vuelta atrás. Se adapta al tamaño del cambio: una corrección de texto no requiere el mismo procedimiento que una migración de datos.

Antes de ejecutar, identifica qué dependencias pueden romperse. Cambiar una IP puede exigir revisar DNS, firewall, cliente, certificado y monitorización. Cambiar una versión de PHP puede afectar extensiones y sockets. Cambiar una estructura de grupos puede requerir nuevas sesiones y revisión de permisos heredados.

Una ventana de mantenimiento debe incluir preparación y aceptación. Si reservaras veinte minutos para una copia que dura dieciocho, sólo quedarían dos para interpretar errores y recuperar. Utiliza tiempos medidos y margen justificado. La prisa no convierte en comprobado un paso que se ha omitido.

## 7. Vuelta atrás y recuperación hacia delante

La vuelta atrás no siempre consiste en restaurar un archivo. Una actualización que cambia esquema de base de datos puede no ser compatible con el código anterior. Una copia de VM puede tener implicaciones distintas para un controlador de dominio que para una web de prácticas.

Define qué estado restaura cada mecanismo y qué datos posteriores podrían perderse. Una reversión del código puede conservar datos nuevos; una restauración completa puede retrocederlos. Si no existe retorno viable, la estrategia puede ser una corrección hacia delante con soporte y preparación adecuados, pero debe reconocerse antes del cambio.

En el laboratorio evita utilizar una instantánea como explicación universal de recuperación. Consulta procedimientos de la aplicación o directorio. Mantén una copia independiente cuando el objetivo exige sobrevivir a la pérdida del almacenamiento de la VM.

## 8. Crear un runbook que se pueda seguir

Un runbook es un procedimiento operativo con un objetivo acotado: renovar un certificado, restaurar un recurso, comprobar una copia o diagnosticar un fallo concreto. La [plantilla](../recursos/plantillas/procedimiento-operacion.md) contiene estado inicial, pasos, resultados y condiciones de parada.

Cada paso debe responder dónde, con qué identidad, qué hace y qué prueba que terminó. Un comando sin máquina o ruta puede ejecutarse en el lugar equivocado. Una captura antigua sin versión ni fecha puede mostrar una interfaz diferente de la actual.

Incluye condiciones de parada. Si el destino de backup no está montado, se detiene la escritura; si una validación de sintaxis falla, no se recarga; si el certificado corresponde a otro nombre, no se acepta una excepción permanente. Estas condiciones forman parte del procedimiento, no son obstáculos que haya que saltar para terminar.

## 9. Ejemplo de runbook: revisar una copia diaria

**Objetivo:** comprobar que el conjunto de datos del laboratorio dispone de un punto recuperable conforme al objetivo acordado. **Entradas:** identificador de tarea, destino, política, última ejecución y un conjunto sintético de prueba.

Primero confirma fecha y estado de la ejecución y que el destino es el almacenamiento previsto. Después identifica el punto recuperable más reciente, no sólo la fecha del archivo contenedor. Revisa alertas y cambios de tamaño que puedan requerir interpretación. Un crecimiento nulo podría significar deduplicación correcta o una tarea que no incluye datos nuevos; el contexto decide.

Ejecuta un ensayo pequeño en un destino distinto según el procedimiento del producto. Compara contenido y permisos de la muestra, registra tiempo y resultado. Si el backup requiere claves, verifica que la recuperación tiene acceso por el canal previsto sin copiarlas a la memoria.

Si falta una copia o el ensayo falla, registra incidencia y decide con la supervisión correspondiente. No borres automáticamente copias antiguas para «hacer espacio» antes de entender retención e integridad. La salida del runbook debe ser evidencia y una acción clara, no únicamente un mensaje «todo correcto».

## 10. Diseñar pruebas que detecten fallos reales

Una matriz de aceptación debe incluir casos positivos, negativos y de recuperación. Para un recurso por grupos, comprobar sólo al editor deja sin evaluar confidencialidad. Para TLS, pedir una IP con verificación deshabilitada no evalúa nombre y confianza. Para una aplicación, un proceso activo no evalúa la transacción que utiliza la persona usuaria.

Elige evidencias proporcionales. Una consulta de texto con hora y contexto puede ser más útil que diez capturas sin título. Conserva entradas y condiciones para poder comparar otra ejecución. Si el dato se obtiene de una tabla sintética, decláralo; si se observa en tu VM, registra cómo se obtuvo.

No conviertas un procedimiento de prueba en una actividad invasiva. Un caso negativo de autorización puede realizarse con una cuenta de laboratorio. Para evaluar recuperación usa datos sintéticos y destino separado. En empresa, alcance y supervisión vienen dados por el procedimiento autorizado.

## 11. Observación, alerta y respuesta

Una métrica informa de una magnitud; una alerta expresa una condición que requiere atención; un procedimiento indica qué hacer. Alertar sobre cada evento sin priorización puede producir ruido, mientras una tarea crítica sin alerta deja fallos sin atender.

Relaciona señales con experiencia y dependencias: respuesta desde cliente, tasa de errores, espacio e inodos, edad del último punto recuperable y vencimiento de un certificado. Para el laboratorio puede bastar una comprobación manual programada en el plan de estudio; no es necesario desplegar una plataforma compleja para aprender el principio.

Una alerta necesita destinatario o rol, prioridad, información mínima y acción. Si la condición no puede verificarse por falta de datos, expresa «estado desconocido» en lugar de inventar disponibilidad. La ausencia de errores en un registro que dejó de escribirse tampoco demuestra salud.

## 12. Transferencia a otra persona

La transferencia comprueba que otra persona comprende servicio, dependencias y tareas comunes. Entrega diagrama, inventario, decisiones, runbooks, pruebas, defectos conocidos y ubicación autorizada de secretos. No incluyas esos secretos en el documento para hacerlo «autosuficiente».

Pide que la persona receptora explique cómo localizaría una avería y cómo recuperaría datos. En el aula puede realizar una comprobación con una copia del laboratorio. Las dificultades de interpretación son información útil para mejorar la guía, aunque el autor original pudiera ejecutar los pasos de memoria.

La entrega debe señalar pendientes y límites. Un servicio de prácticas sin prueba de restauración no se describe como «preparado para producción». Si una prueba depende de equipamiento no disponible, se registra qué falta y qué criterio se usaría. La precisión facilita la revisión y evita promesas que la evidencia no sostiene.

## 13. Mantener documentación con Git

Agrupa cambios relacionados y escribe mensajes que expliquen el comportamiento o contenido resultante. Para una guía, indica qué se corrigió o amplió. Evita incluir archivos generados que no forman parte de la entrega, capturas con datos sensibles o grandes discos de VM.

Una revisión compara intención y resultado. Si cambias un nombre de servicio, busca referencias en índices, comandos, diagramas y datos. Si cambias una ruta, revisa enlaces y scripts. El validador del repositorio ayuda con estructura y navegación; la revisión técnica comprueba significado y viabilidad.

El [índice completo](../INDICE.md) se genera mediante una herramienta local que recorre los documentos. Los índices de cada asignatura conservan la ruta pedagógica: una lista automática de archivos facilita encontrar material, pero no reemplaza una explicación de qué estudiar antes.

## 14. Revisión final de una memoria

Lee la memoria como alguien que no asistió a la práctica. ¿Sabe cuál era el problema? ¿Puede distinguir el diseño de la configuración aplicada? ¿Encuentra versiones, topología y dependencias? ¿Las pruebas indican resultado real y criterio de aceptación? ¿Sabe qué está pendiente y cómo recuperar?

Revisa tablas de unidades y cálculos, concordancia de nombres e IP, fuentes primarias y fecha cuando la información pueda cambiar. Comprueba que los comandos no ocultan un efecto distinto de la explicación. Una instrucción de restaurar, borrar o cambiar permisos necesita contexto y precondiciones explícitas.

La defensa final consiste en justificar decisiones y evidencias. Memorizar la secuencia de instalación no explica por qué el sistema funciona. Saber qué prueba falta, qué hipótesis permanece abierta y qué harías después también demuestra comprensión profesional.

## Fuentes y ampliación

- [Git documentation](https://git-scm.com/doc): control de cambios y revisión.
- [Debian Reference](https://www.debian.org/doc/manuals/debian-reference/): administración y operación.
- [Microsoft Learn: Windows Server](https://learn.microsoft.com/windows-server/): roles y recuperación según versión.
- [Samba documentation](https://www.samba.org/samba/docs/), [BIND ARM](https://bind9.readthedocs.io/) y [Nginx](https://nginx.org/en/docs/): procedimientos específicos de cada servicio.
- [INCIBE: empresas](https://www.incibe.es/empresas): continuidad, gestión e incidentes.
