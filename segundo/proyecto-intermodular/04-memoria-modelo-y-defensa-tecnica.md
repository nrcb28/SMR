# Memoria modelo, aceptación, recuperación y defensa

[Índice](README.md) · [Requisitos y planificación](03-cuaderno-de-requisitos-y-planificacion.md)

Este documento es un ejemplo extendido de estructura y razonamiento, no la memoria de una implantación realizada. Las tablas de resultados deben completarse con evidencias propias. Cuando se utiliza un tiempo o un resultado hipotético, se identifica como escenario de ensayo para evitar presentarlo como medición.

## 1. Resumen de la memoria modelo

“Se diseña una infraestructura de laboratorio para una oficina de doce puestos, cuatro de administración y ocho de soporte. El mínimo incluye resolución interna, configuración de cliente, archivos con acceso por función, intranet HTTPS y procedimiento de recuperación. El diseño permite validar una muestra con servidor y cliente, sin afirmar que existan doce equipos virtuales desplegados. La segmentación y el directorio centralizado se tratan como opciones con dependencias propias.”

El resumen debe indicar problema, alcance, solución propuesta y estado. Sustituye “se diseña” por “se implantó y probó” sólo cuando puedas identificar qué pruebas se ejecutaron, en qué versión y con qué resultado. Si una extensión queda pendiente, inclúyela en el resumen para que el lector no descubra la limitación al final.

## 2. Contexto y decisiones

La memoria explica funciones, datos y permisos antes de listar productos. Administración necesita modificar su área; soporte modifica la suya y consulta documentación común. Una cuenta ajena no accede a carpetas restringidas. La matriz de permisos se convierte en configuración y casos de prueba, con identidades ficticias distintas de la cuenta administradora.

El mínimo selecciona Debian 13 para servicios y Windows 11 Pro o Linux como cliente según la práctica. La red LAB usa srv01 en 192.168.56.10/24 y cli01 en .20; .11 queda reservada al controlador dc01 cuando se utilice el escenario de directorio. La red NAT adicional se documenta por separado y no se anuncia una puerta LAB inexistente.

Una decisión técnica registra alternativas y criterio. Por ejemplo, Samba independiente reduce complejidad para la muestra; AD añade identidades y políticas centralizadas, pero exige DNS de directorio, hora y recuperación específicas. No se afirma que una alternativa sea universalmente mejor. Se elige según requisitos, medios y pruebas disponibles.

## 3. Registro de configuración

Cada servicio necesita una ficha con máquina, versión, rol, puertos, interfaces, archivos editados, usuario de ejecución, dependencia, validación sintáctica y prueba funcional. Añade sólo extractos saneados que sean necesarios para entender el cambio. Los valores sensibles se obtienen por canal separado.

No copies una salida de otro ejemplo como si fuera de tu equipo. La evidencia incluye fecha, máquina y comando o acción. Si una herramienta localiza una ruta distinta según la versión, documenta la ruta real y su relación con el manual. El propósito es que otra persona pueda mantener el estado entregado, no reproducir literalmente una captura.

Una tabla de estado puede distinguir “configuración preparada”, “sintaxis validada”, “servicio activo”, “cliente probado” y “aceptación completada”. Una unidad activa sin prueba desde cliente no se marca aceptada. La columna de pendiente permite localizar qué falta y evita deducir cumplimiento a partir de silencio.

## 4. Matriz de doce pruebas

Cada prueba comienza con un estado conocido y conserva resultado esperado y obtenido por separado. Las siguientes son especificaciones para ejecutar, no resultados ya observados.

| ID | Preparación y estímulo | Resultado esperado | Evidencia mínima |
| --- | --- | --- | --- |
| T01 | Cliente de ensayo solicita concesión en LAB con DHCP previsto. | IP del rango documentado, prefijo y DNS correctos; sin gateway ficticio. | Concesión y configuración cliente. |
| T02 | Revisar emisores DHCP durante una solicitud. | Sólo el servicio autorizado del escenario responde en LAB. | Captura acotada o registro equivalente. |
| T03 | Consultar nombre conocido y uno inexistente al DNS previsto. | Registro conocido correcto y respuesta negativa coherente para el otro. | Consultas con servidor identificado. |
| T04 | Editor crea y lector abre un archivo sintético. | Escritura y lectura coinciden con matriz. | Identidad, acción y resultado. |
| T05 | Cuenta ajena intenta acceder al área restringida. | Denegación sin conceder permisos amplios. | Prueba desde cliente con sesión identificada. |
| T06 | Abrir URL HTTPS canónica con confianza correcta. | Nombre, cadena y vigencia válidos; contenido esperado. | Información TLS y operación cliente. |
| T07 | Comparar un nombre no incluido en certificado, sin desactivar validación. | Error TLS interpretable, no aceptación silenciosa. | Salida y explicación de nombre/SAN. |
| T08 | Restaurar muestra en destino separado. | Contenido y permisos equivalentes a la copia elegida. | Identificador de copia, integridad y acceso. |
| T09 | Ensayar orden de recuperación de configuración y dependencias. | Servicio funcional desde cliente al final del guion. | Cronología y lista de comprobaciones. |
| T10 | Revisor sigue un procedimiento sin explicación oral. | Puede ejecutarlo y localizar precondiciones/recuperación. | Dudas, correcciones y repetición. |
| T11 | Revisar hoja energética y ficha de retirada. | Unidades, límites y trazabilidad coherentes. | Fórmulas y conciliación sintética. |
| T12 | Exportar inventario y registrar alta/baja de una identidad ficticia. | Datos interpretables y acceso coherente con el estado. | Exportación saneada y prueba posterior. |

Para T02 no introduces un servidor DHCP ajeno en una red compartida. El ejercicio observa el laboratorio y puede simular un conflicto en otra copia aislada. Para T07 utiliza únicamente nombres y certificados del escenario; no enseñes al navegador a ignorar errores como criterio de éxito.

## 5. Pruebas negativas y persistencia

Una prueba negativa valida una condición que debe rechazarse, no busca romper indiscriminadamente el sistema. Define entrada, motivo del rechazo y conservación del estado válido. Acceso sin permiso, nombre no existente, certificado no confiado y dato inválido aportan evidencias diferentes.

La persistencia se prueba tras el evento pertinente: renovar una concesión, abrir una sesión nueva, reiniciar un servicio o reiniciar la VM cuando proceda. La elección debe relacionarse con el riesgo. Si un cambio sólo funciona hasta reiniciar, documenta por qué no se guardó o qué gestor reescribe la configuración.

No ejecutes todas las pruebas desde la misma sesión privilegiada. Las credenciales almacenadas, cachés y conexiones SMB abiertas pueden hacer que una prueba parezca corresponder a otra identidad. Registra contexto y prepara nuevas sesiones de forma controlada, sin cerrar conexiones ajenas al laboratorio.

## 6. Guion de recuperación con RPO y RTO

El objetivo propuesto es RPO de veinticuatro horas y RTO de cuatro. Define inicio del reloj de recuperación y punto de datos. Una copia que terminó hoy puede contener una instantánea de datos tomada antes; registra ambos momentos si difieren. El tiempo de transferencia no es el tiempo total de recuperación.

Escenario hipotético: incidente declarado a las 09:00 UTC y punto recuperable de datos de las 08:00 del mismo día. La ventana temporal hasta el incidente es una hora. Aun así debes comprobar qué operaciones incluía exactamente la copia y si existían datos posteriores en otras fuentes; el cálculo temporal no demuestra integridad.

| Fase del ensayo simulado | Duración supuesta | Momento acumulado |
| --- | ---: | --- |
| Delimitación y elección del punto | 20 min | 09:20 |
| Preparación del destino aislado | 15 min | 09:35 |
| Transferencia de 30 GB a 20 MB/s efectivos | 25 min | 10:00 |
| Configuración, identidades y permisos | 20 min | 10:20 |
| Validación de datos y cliente | 30 min | 10:50 |
| Aceptación y comunicación | 10 min | 11:00 |
| **Total supuesto** | **120 min** | **Dos horas desde declaración** |

Treinta GB decimales son treinta mil MB; dividido entre veinte MB/s son mil quinientos segundos, veinticinco minutos. Si utilizas GiB o MiB, cambia el cálculo de forma coherente. La tasa efectiva debe proceder de una medida si se utiliza como evidencia real; aquí es una hipótesis.

El escenario cumpliría los objetivos numéricos sólo si las fases se ejecutaran con éxito y los resultados fueran correctos. No se marca RTO cumplido leyendo esta tabla. En tu ensayo registra tiempos reales, fallos, intervención humana y repetición necesaria. Si la primera restauración falla, ese tiempo forma parte de la recuperación y no desaparece del informe.

## 7. Verificar integridad, permisos y funcionamiento

Comparar hashes de los archivos comprueba identidad de contenido para el conjunto comparado, no por sí solo funcionalidad de la aplicación ni corrección de autorización. Mantén un manifiesto de archivos esperados y comprueba también faltantes y extras. Un hash igual en un archivo no dice si el directorio completo se recuperó.

La restauración de permisos necesita preservar identidades y rutas. Documenta UID/GID o SID y sus relaciones, según escenario. No reasignes propietarios a una cuenta cualquiera sólo para conseguir acceso durante la demostración. Una aplicación con base de datos puede necesitar copia coherente, configuración y secretos coordinados; copiar sus archivos mientras cambia no garantiza una restauración válida.

Al final realiza una operación desde cliente con cuenta ordinaria y otra negativa. Comprueba también dependencias de nombre y tiempo. La aceptación incluye lo que una persona usuaria puede hacer, no sólo que el servidor tenga procesos escuchando.

## 8. Registro de defectos y cambios

Un defecto se identifica con requisito, pasos, resultado esperado, obtenido, severidad del ejercicio y estado. “No funciona” no permite reproducir. No uses el mismo estado para “sin investigar”, “mitigado” y “corregido y probado”. Cada transición debe tener motivo y evidencia.

Ejemplo documental: T05 revela que el área común permite escritura a lectores. El equipo conserva evidencia, revisa capas de permiso y prepara un cambio acotado. Tras corregir repite T04 y T05, además de una comprobación de persistencia relevante. El ejemplo describe el método; no afirma que ese defecto exista en la configuración entregada.

Si el defecto obliga a cambiar arquitectura o requisito, actualiza trazabilidad, riesgo y presupuesto. Una corrección pequeña puede tener consecuencias amplias cuando toca DNS, identidades o rutas compartidas. El registro de decisiones permite explicar por qué la versión final difiere del primer diseño sin convertir la memoria en una narración desordenada de intentos.

## 9. Manual de operación y relevo

El manual describe comprobación diaria o periódica, revisión de copias, alta/baja, certificados, actualizaciones y recuperación. Cada tarea indica responsable por rol, frecuencia propuesta, precondición, acción, evidencia y criterio de escalado. “Revisar copias” debe concretar antigüedad, resultado y ensayo, no sólo abrir una carpeta.

Incluye ubicación lógica de documentos y forma de obtener secretos por un canal autorizado, sin incorporar sus valores. El relevo enumera estado final, cambios pendientes, limitaciones conocidas y siguiente revisión. Si una función es sólo diseño, debe quedar identificada para que nadie la opere suponiendo que está desplegada.

## 10. Defensa con preguntas y respuestas razonadas

**¿Por qué no anunciáis una puerta .1 en LAB?** Porque el segmento base no incluye un router configurado. Dentro de la subred los equipos se comunican directamente. La NIC NAT tiene su propio entorno y no convierte automáticamente a .1 de LAB en siguiente salto válido.

**¿Por qué separar el controlador de dominio?** Porque DNS de directorio, identidades y recuperación necesitan un rol coherente. Instalar dos servicios DNS en la misma IP y puerto no implementa separación. dc01 permite explicar dependencias y evitar presentar una combinación conflictiva.

**¿Qué prueba demuestra seguridad de archivos?** Una matriz materializada con operaciones permitidas y denegadas desde identidades diferentes. Abrir el recurso con administrador no demuestra mínimo privilegio. Además se revisan permisos de recurso y sistema de archivos.

**¿Por qué HTTPS interno necesita confianza?** Porque cifrar sin validar nombre y emisor no cumple el criterio del proyecto. La CA de prácticas se instala sólo en entornos previstos y se retira cuando corresponde; una advertencia ignorada no es una aceptación válida.

**¿Una instantánea prueba continuidad?** No. Puede depender de los discos originales y no representar una copia consistente de aplicación. La continuidad exige elegir punto recuperable, preparar destino, restaurar y validar con tiempo y pérdida de datos documentados.

**¿Por qué el presupuesto es parcial?** Porque los importes son hipótesis y quedan conceptos como licencias o conectividad por verificar. Se conserva subtotal y contingencia por separado y no se presenta una propuesta de compra como aprobada con datos pendientes.

**¿Cómo sabéis que se puede mantener?** Un revisor sigue una tarea con la documentación y registra dificultades. El resultado debe conducir a correcciones concretas. Un manual que sólo entiende quien lo escribió no satisface reproducibilidad.

**¿Qué no habéis comprobado?** La respuesta depende del trabajo real. Debe identificar extensiones diseñadas pero no desplegadas, versiones no ensayadas y limitaciones del laboratorio. Reconocerlo permite evaluar la conclusión y planear el siguiente paso.

## 11. Autoevaluación de entrega

Rúbrica propuesta: requisitos/trazabilidad 20 %, coherencia de arquitectura 20 %, pruebas positivas y negativas 25 %, recuperación 15 %, documentación y relevo 10 %, defensa y límites 10 %. Evalúa el valor de las evidencias y la relación entre decisiones, no cantidad de capturas o tecnologías.

Antes de defender, intenta explicar el proyecto sin mostrar terminal durante dos minutos: necesidad, diseño, dependencia principal, prueba más importante y limitación. Después muestra una evidencia que sostenga cada afirmación. El proyecto integra las [guías del ciclo](../../README.md); no se sustituye por memorizar una presentación.
