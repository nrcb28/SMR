# CMO-315 · Arquitecturas en la nube

[Catálogo de optativas](../README.md) · [Índice general](../../README.md)

## Aplicabilidad y forma de estudio

La tabla del catálogo fija 90 horas para este módulo específico de Informática y Comunicaciones. Su ubicación en segundo se deduce del encaje con las optativas de SMR (50/90 horas); no se presenta como una columna de curso expresamente asignada a IFC en el catálogo. Deben confirmarse la oferta y las condiciones del centro.

El currículo de referencia es la [Orden 3536/2025](https://www.bocm.es/boletin/CM_Orden_BOCM/2025/08/27/BOCM-20250827-5.PDF), Anexo II, CMO-315; BOCM página 197 y siguientes; PDF páginas 180–183. La relación aplicable se contrasta con la [Orden 3822/2026](https://www.bocm.es/boletin/CM_Orden_BOCM/2026/09/25/BOCM-20260925-20.PDF). El catálogo permite una oferta; no demuestra que un centro imparta todas estas materias ni que un alumno deba cursarlas simultáneamente.

Los enunciados de RA y los CE de las tablas se transcriben del referente normativo. Las explicaciones, retos, soluciones y condiciones de aceptación son propuestas didácticas propias. La evidencia esperada se diferencia de lo observado: completa resultados reales en una copia de la plantilla de seguimiento.

## Preparación

Revisa el [laboratorio común](../../docs/laboratorio.md) y trabaja con datos sintéticos y un entorno identificado. Antes de modificar, registra versión, estado inicial y recuperación. Las tareas que necesitan hardware, motor de juego o plataforma administrada deben ejecutarse en esos medios para aportar evidencia completa; la preparación escrita conserva su valor y se marca como pendiente de esa ejecución.

## Ruta por resultados de aprendizaje

**Entorno de nube:** no se pide contratar servicios ni abrir una cuenta de pago. Utiliza, si existe, el sandbox del centro ya autorizado con límites, presupuesto y plan de retirada. Un simulador o una VM local permite preparar conceptos, pero no demuestra los CE que exigen crear, desplegar o utilizar recursos administrados de un proveedor. Esos criterios quedan pendientes cuando no se dispone de plataforma; no se rellenan con capturas de ejemplo.

**Notas del referente:** el currículo de 2025 usa la cabecera «Arquitectura en la nube» y el catálogo vigente denomina «Arquitecturas en la nube». Se conservan los enunciados y criterios de la norma. RA3 y RA4 incluyen la letra **ñ** entre n y o: se han separado correctamente los dos criterios que una extracción automática había unido al párrafo n. Es una incidencia de extracción, no una errata de la norma. Algunos CE del RA3 repiten capacidades; se mantienen todos sus identificadores, pudiendo compartir una evidencia expresamente referenciada.

<a id="ra1"></a>
## RA1 · Defender una decisión arquitectónica

**Enunciado oficial:** Toma decisiones en materia de arquitectura a partir de los principios y buenas prácticas recomendadas.

Una arquitectura debe satisfacer requisitos y justificar compensaciones entre operación, seguridad, fiabilidad, rendimiento, coste y sostenibilidad. Región, servicio y patrón no se eligen por moda: se comparan con carga, datos y capacidad del equipo.

### Actividad CMO-315-RA1-A1

1. Define una aplicación de soporte con requisitos medibles y restricciones.
2. Compara dos diseños y registra hipótesis y dependencias comunes.
3. Selecciona ubicación y servicios con el marco de arquitectura vigente del proveedor.
4. Redacta una decisión técnica que incluya condiciones que obligarían a revisarla.

**Solución razonada y errores que debes interpretar:** Una VM grande puede simplificar el ensayo y limitar continuidad; varios servicios administrados pueden mejorar operación e introducir dependencia o coste. La respuesta correcta explica por qué el diseño elegido encaja en este caso y cómo se comprobará.

**Entregable:** Registro de decisión, diagrama y revisión por pilares.

**Aceptación del reto:** Las decisiones tienen requisito, evidencia y consecuencia; se explican límites y condiciones de revisión.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha definido la arquitectura en la nube. | Registro de decisión, diagrama y revisión por pilares; apartado a con datos, explicación o salida referida expresamente a ese criterio. Las decisiones tienen requisito, evidencia y consecuencia; se explican límites y condiciones de revisión. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se ha descrito cómo diseñar y evaluar arquitecturas utilizando marcos de la buena arquitectura. | Registro de decisión, diagrama y revisión por pilares; apartado b con datos, explicación o salida referida expresamente a ese criterio. Las decisiones tienen requisito, evidencia y consecuencia; se explican límites y condiciones de revisión. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han explicado las mejores prácticas para diseño de soluciones arquitectónicas en la nube. | Registro de decisión, diagrama y revisión por pilares; apartado c con datos, explicación o salida referida expresamente a ese criterio. Las decisiones tienen requisito, evidencia y consecuencia; se explican límites y condiciones de revisión. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han descrito cómo tomar decisiones sobre dónde desplegar recursos en la nube. | Registro de decisión, diagrama y revisión por pilares; apartado d con datos, explicación o salida referida expresamente a ese criterio. Las decisiones tienen requisito, evidencia y consecuencia; se explican límites y condiciones de revisión. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra2"></a>
## RA2 · Construir cómputo y almacenamiento recuperables

**Enunciado oficial:** Utiliza los servicios de computación en la nube para lograr una infraestructura escalable, fiable y altamente disponible.

La alta disponibilidad necesita distribuir fallos y comprobar conmutación. Discos de bloques, archivos compartidos y objetos tienen semánticas distintas. La persistencia debe sobrevivir al evento para el que se ha diseñado, no sólo al cierre de una consola.

### Actividad CMO-315-RA2-A1

1. En sandbox educativo preexistente despliega instancias y registra imagen, red e identidad.
2. Conecta un volumen EBS y un recurso EFS cuando se trabaje con AWS, tal como menciona el currículo; si se usa otro proveedor, identifica la equivalencia y su límite.
3. Comprueba montaje persistente, acceso con identidades y separación de datos del ciclo de vida de la instancia.
4. Publica un sitio estático de ensayo con el patrón de disponibilidad autorizado y retira todos los recursos al finalizar.

**Solución razonada y errores que debes interpretar:** Dos instancias que comparten un único componente frágil no prueban disponibilidad de todo el servicio. Los nombres EBS/EFS se conservan porque aparecen en los CE; una carpeta local sólo prepara conceptos y no acredita haber conectado esos recursos de nube.

**Entregable:** Inventario de instancias/almacenamiento y pruebas de persistencia/disponibilidad.

**Aceptación del reto:** Los recursos reales del sandbox funcionan conforme al diseño y sus datos/retirada se gestionan de forma controlada.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha identificado los diferentes servicios computacionales en la nube. | Inventario de instancias/almacenamiento y pruebas de persistencia/disponibilidad; apartado a con datos, explicación o salida referida expresamente a ese criterio. Los recursos reales del sandbox funcionan conforme al diseño y sus datos/retirada se gestionan de forma controlada. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han implementado y configurado máquinas virtuales. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Inventario de instancias/almacenamiento y pruebas de persistencia/disponibilidad»; criterio b. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| c | Se han creado soluciones de almacenamiento en la nube para máquinas virtuales. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Inventario de instancias/almacenamiento y pruebas de persistencia/disponibilidad»; criterio c. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| d | Se han lanzado máquinas virtuales en clústeres. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Inventario de instancias/almacenamiento y pruebas de persistencia/disponibilidad»; criterio d. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| e | Se han descrito los diferentes modelos de precios para las máquinas virtuales en la nube. | Inventario de instancias/almacenamiento y pruebas de persistencia/disponibilidad; apartado e con datos, explicación o salida referida expresamente a ese criterio. Los recursos reales del sandbox funcionan conforme al diseño y sus datos/retirada se gestionan de forma controlada. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| f | Se han reconocido los problemas que los servicios de almacenamiento en la nube pueden resolver. | Inventario de instancias/almacenamiento y pruebas de persistencia/disponibilidad; apartado f con datos, explicación o salida referida expresamente a ese criterio. Los recursos reales del sandbox funcionan conforme al diseño y sus datos/retirada se gestionan de forma controlada. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| g | Se ha descrito cómo utilizar eficientemente los servicios de almacenamiento en la nube y cómo migrar datos a la nube. | Inventario de instancias/almacenamiento y pruebas de persistencia/disponibilidad; apartado g con datos, explicación o salida referida expresamente a ese criterio. Los recursos reales del sandbox funcionan conforme al diseño y sus datos/retirada se gestionan de forma controlada. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| h | Se ha creado un sitio web estático altamente disponible en la nube. | Inventario de instancias/almacenamiento y pruebas de persistencia/disponibilidad; apartado h con datos, explicación o salida referida expresamente a ese criterio. Los recursos reales del sandbox funcionan conforme al diseño y sus datos/retirada se gestionan de forma controlada. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| i | Se han implementado y conectado discos EBS a instancias. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Inventario de instancias/almacenamiento y pruebas de persistencia/disponibilidad»; criterio i. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| j | Se han implementado y conectado de forma persistente unidades EFS a instancias. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Inventario de instancias/almacenamiento y pruebas de persistencia/disponibilidad»; criterio j. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |

<a id="ra3"></a>
## RA3 · Integrar servicios administrados sin acoplamiento innecesario

**Enunciado oficial:** Utiliza los servicios administrados para lograr una mayor flexibilidad y resiliencia de una infraestructura.

Una solución administrada conserva responsabilidades del cliente: esquema, autorización, secretos, continuidad y observabilidad. Colas desacoplan productores y consumidores; cachés aceleran lecturas bajo una política de caducidad; no sustituyen siempre al dato de autoridad.

### Actividad CMO-315-RA3-A1

1. Define despliegue automatizado y una aplicación sencilla en el sandbox; registra plantilla y cambios.
2. Despliega una base relacional privada y ensaya migración de datos sintéticos con recuento e integridad antes/después.
3. Compara NoSQL y añade, donde la plataforma docente lo permita, caché en memoria, cola y notificación con un mensaje de prueba.
4. Configura roles/federación y explica estado de sesión, invalidación de caché y distribución de contenidos de borde.

**Solución razonada y errores que debes interpretar:** Un mensaje debe poder identificarse y procesarse según su contrato, incluyendo duplicados o reintentos. La migración se valida con datos, permisos y aplicación, no únicamente porque la importación termine. Los CE repetidos del texto normativo se conservan y pueden referir a una evidencia compartida, identificada expresamente.

**Entregable:** Dossier de despliegue, migración, identidad y mensajería/caché.

**Aceptación del reto:** Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han utilizado servicios administrados para el despliegue automatizado de la infraestructura. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Dossier de despliegue, migración, identidad y mensajería/caché»; criterio a. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| b | Se han utilizado servicios administrados para el despliegue de aplicaciones sencillas. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Dossier de despliegue, migración, identidad y mensajería/caché»; criterio b. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| c | Se han comparado los diferentes tipos de bases de datos administradas. | Dossier de despliegue, migración, identidad y mensajería/caché; apartado c con datos, explicación o salida referida expresamente a ese criterio. Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han desplegado servicios administrados de bases de datos relacionales en la nube. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Dossier de despliegue, migración, identidad y mensajería/caché»; criterio d. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| e | Se ha explicado cómo utilizar bases de datos NoSQL administradas en la nube. | Dossier de despliegue, migración, identidad y mensajería/caché; apartado e con datos, explicación o salida referida expresamente a ese criterio. Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| f | Se han descrito los controles de seguridad de las bases de datos administradas. | Dossier de despliegue, migración, identidad y mensajería/caché; apartado f con datos, explicación o salida referida expresamente a ese criterio. Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| g | Se han realizado migraciones de bases de datos en las instalaciones a la nube. | Dossier de despliegue, migración, identidad y mensajería/caché; apartado g con datos, explicación o salida referida expresamente a ese criterio. Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| h | Se han comparado los diferentes tipos de bases de datos administradas. | Dossier de despliegue, migración, identidad y mensajería/caché; apartado h con datos, explicación o salida referida expresamente a ese criterio. Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| i | Se han desplegado servicios administrados de bases de datos relacionales en la nube. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Dossier de despliegue, migración, identidad y mensajería/caché»; criterio i. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| j | Se ha explicado cómo utilizar bases de datos NoSQL administradas en la nube. | Dossier de despliegue, migración, identidad y mensajería/caché; apartado j con datos, explicación o salida referida expresamente a ese criterio. Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| k | Se han descrito los controles de seguridad de las bases de datos administradas. | Dossier de despliegue, migración, identidad y mensajería/caché; apartado k con datos, explicación o salida referida expresamente a ese criterio. Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| l | Se han realizado migraciones de bases de datos en las instalaciones a la nube. | Dossier de despliegue, migración, identidad y mensajería/caché; apartado l con datos, explicación o salida referida expresamente a ese criterio. Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| m | Se ha explicado cómo gestionar la autenticación y autorización del acceso a los recursos de la nube. | Dossier de despliegue, migración, identidad y mensajería/caché; apartado m con datos, explicación o salida referida expresamente a ese criterio. Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| n | Se ha descrito cómo puede utilizarse la identidad federada para incrementar la seguridad de la infraestructura. | Dossier de despliegue, migración, identidad y mensajería/caché; apartado n con datos, explicación o salida referida expresamente a ese criterio. Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| ñ | Se han utilizado servicios administrados de bases de datos en memoria (Memchached, Redis, etc.) | Inventario y registro de la operación en el sandbox autorizado, dentro de «Dossier de despliegue, migración, identidad y mensajería/caché»; criterio ñ. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| o | Se han utilizado servicios administrados de colas de mensajes para el diseño de arquitecturas débilmente acopladas. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Dossier de despliegue, migración, identidad y mensajería/caché»; criterio o. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| p | Se han utilizado servicios administrados de notificaciones para el diseño de arquitecturas débilmente acopladas. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Dossier de despliegue, migración, identidad y mensajería/caché»; criterio p. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| q | Se ha identificado como las técnicas de caché pueden mejorar el rendimiento y reducir la latencia de una infraestructura. | Dossier de despliegue, migración, identidad y mensajería/caché; apartado q con datos, explicación o salida referida expresamente a ese criterio. Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| r | Se ha identificado cómo la computación en el borde (Edge Computing) puede utilizarse para la distribución de contenidos y como protección de ataques DDoS. | Dossier de despliegue, migración, identidad y mensajería/caché; apartado r con datos, explicación o salida referida expresamente a ese criterio. Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| s | Se ha reconocido cómo la administración de datos de sesión está relacionada con las técnicas de caché. | Dossier de despliegue, migración, identidad y mensajería/caché; apartado s con datos, explicación o salida referida expresamente a ese criterio. Cada servicio declarado tiene evidencia de uso en la plataforma autorizada; el diseño local pendiente no se presenta como despliegue administrado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra4"></a>
## RA4 · Medir resiliencia, elasticidad y coste

**Enunciado oficial:** Potencia el rendimiento y reduce los costes de una infraestructura creada en la nube.

El ajuste de rendimiento necesita una carga controlada y métricas comparables. Balanceo, autoescalado, DNS de conmutación y recuperación resuelven partes diferentes. Microservicios y funciones pueden aumentar flexibilidad y también complejidad operativa.

### Actividad CMO-315-RA4-A1

1. Modela red, subredes, rutas, gateway y controles con una plantilla IaC revisada antes de aplicar.
2. En sandbox ensaya balanceo, estado de salud y una política de escalado con carga limitada sólo a tus recursos.
3. Define RPO/RTO, estrategias ante desastres y un procedimiento de copia/restauración incluyendo almacenamiento híbrido si forma parte del escenario.
4. Compara una función con API Gateway y un flujo orquestado frente al servicio continuo, con costes hipotéticos y resultados medidos.
5. Documenta redes híbridas, peering, límites de caché y plan de retirada; conserva la lista de recursos y cargos esperados.

**Solución razonada y errores que debes interpretar:** Un RPO de treinta minutos no se demuestra por programar una tarea cada treinta minutos: hace falta un punto recuperable y supervisión. La plantilla es un artefacto de diseño hasta que se aplica y verifica. Los criterios de este RA incluyen muchas capacidades; una sola captura de un balanceador no acredita todas.

**Entregable:** Plantilla IaC, plan de recuperación y comparación de métricas/costes.

**Aceptación del reto:** La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han desplegado balanceadores de carga para crear entornos altamente disponibles. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Plantilla IaC, plan de recuperación y comparación de métricas/costes»; criterio a. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| b | Se ha utilizado los servicios de autoescalado para brindar elasticidad a un clúster de máquinas virtuales. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado b con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han utilizado servidores DNS administrados para conmutar por error automáticamente en caso de fallo en una infraestructura. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado c con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han diseñado arquitecturas con servicios de monitorización para dar respuestas reactivas a un evento o fallo en la infraestructura. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado d con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se ha explicado el rol de las redes virtuales en la nube. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado e con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| f | Se han identificado los servicios que permiten establecer una conexión de red híbrida entre las instalaciones y la nube. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado f con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| g | Se han implementado VPC y subredes. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Plantilla IaC, plan de recuperación y comparación de métricas/costes»; criterio g. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| h | Se han configurado grupos de seguridad y ALC de red. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Plantilla IaC, plan de recuperación y comparación de métricas/costes»; criterio h. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| i | Se ha descrito cómo conectar diferentes redes virtuales en la nube. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado i con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| j | Se ha descrito cómo escalar una infraestructura de red en la nube. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado j con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| k | Se han creado redes virtuales en la nube, gateways de Internet, tablas de encaminamiento y cortafuegos. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Plantilla IaC, plan de recuperación y comparación de métricas/costes»; criterio k. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| l | Se ha definido el despliegue de Infraestructura como Código (IaC). | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado l con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| m | Se ha modelado una infraestructura como código mediante una plantilla. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado m con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| n | Se ha explicado qué es el acoplamiento de infraestructuras en la nube y el por qué deben diseñarse arquitecturas débilmente acopladas. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado n con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| ñ | Se han identificado las diferentes estrategias de planificación ante desastres. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado ñ con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| o | Se han definido los conceptos de RPO (Recovery Point Objective) y RTO (Recovery Time Objective). | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado o con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| p | Se han descrito patrones comunes para el respaldo y recuperación de desastres y cómo implementarlos. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado p con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| q | Se han aplicado las buenas prácticas para lograr una infraestructura en la nube escalable, segura y altamente disponible. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado q con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| r | Se han utilizado servicios administrados de almacenamiento híbrido como soluciones de respaldo de datos. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Plantilla IaC, plan de recuperación y comparación de métricas/costes»; criterio r. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| s | Se han aplicado las buenas prácticas para lograr mayor flexibilidad y resiliencia de una infraestructura en la nube. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado s con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| t | Se han indicado las características de las arquitecturas basadas en microservicios y cómo éstas pueden reducir los costes de la infraestructura y potenciar el rendimiento. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado t con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| u | Se ha explicado qué es una arquitectura sin servidor (serverless). | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado u con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| v | Se ha desplegado una infraestructura sin servidor utilizando funciones serverless, API Gateway. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado v con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| w | Se ha explicado qué es la orquestación de flujos sin servidor y cómo puede reducir los costes. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado w con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| x | Se han aplicado las buenas prácticas para para potenciar el rendimiento y reducir los costes de la infraestructura en la nube. | Plantilla IaC, plan de recuperación y comparación de métricas/costes; apartado x con datos, explicación o salida referida expresamente a ese criterio. La entrega verifica cada capacidad que declara y distingue pruebas ejecutadas, simulaciones y acciones pendientes. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

## Dossier final y autoevaluación

Reúne las actividades por RA y enlaza cada CE con el artefacto concreto que lo demuestra. Una memoria extensa sin resultados identificables no sustituye las pruebas; una configuración que funciona por casualidad debe revisarse con casos de límite y recuperación. Explica las dependencias y qué haría falta para repetir el trabajo en otro equipo.

Como rúbrica de práctica se propone valorar corrección técnica (40 %), evidencia y pruebas (30 %), explicación de decisiones (20 %) y documentación/revisión (10 %). Es una propuesta propia: los instrumentos, ponderaciones y calificaciones oficiales corresponden al centro. Los CE no ejecutados o sin medios disponibles se anotan pendientes, sin inventar una adquisición del RA.

## Referencias y datos de trazabilidad

- [Matriz completa de este módulo](alineacion-ra.json).
- [Referentes normativos del repositorio](../../recursos/ra/referentes-oficiales.json).
- [AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).
- [Amazon EBS](https://docs.aws.amazon.com/ebs/).
- [Amazon EFS](https://docs.aws.amazon.com/efs/).
