# CMO-312 · Fundamentos de computación en la nube

[Catálogo de optativas](../README.md) · [Índice general](../../README.md)

## Aplicabilidad y forma de estudio

La tabla del catálogo fija 50 horas para este módulo específico de Informática y Comunicaciones. Su ubicación en primero se deduce del encaje con las optativas de SMR (50/90 horas); no se presenta como una columna de curso expresamente asignada a IFC en el catálogo. Deben confirmarse la oferta y las condiciones del centro.

El currículo de referencia es la [Orden 3536/2025](https://www.bocm.es/boletin/CM_Orden_BOCM/2025/08/27/BOCM-20250827-5.PDF), Anexo II, CMO-312; BOCM página 187 y siguientes; PDF páginas 170–172. La relación aplicable se contrasta con la [Orden 3822/2026](https://www.bocm.es/boletin/CM_Orden_BOCM/2026/09/25/BOCM-20260925-20.PDF). El catálogo permite una oferta; no demuestra que un centro imparta todas estas materias ni que un alumno deba cursarlas simultáneamente.

Los enunciados de RA y los CE de las tablas se transcriben del referente normativo. Las explicaciones, retos, soluciones y condiciones de aceptación son propuestas didácticas propias. La evidencia esperada se diferencia de lo observado: completa resultados reales en una copia de la plantilla de seguimiento.

## Preparación

Revisa el [laboratorio común](../../docs/laboratorio.md) y trabaja con datos sintéticos y un entorno identificado. Antes de modificar, registra versión, estado inicial y recuperación. Las tareas que necesitan hardware, motor de juego o plataforma administrada deben ejecutarse en esos medios para aportar evidencia completa; la preparación escrita conserva su valor y se marca como pendiente de esa ejecución.

## Ruta por resultados de aprendizaje

**Entorno de nube:** no se pide contratar servicios ni abrir una cuenta de pago. Utiliza, si existe, el sandbox del centro ya autorizado con límites, presupuesto y plan de retirada. Un simulador o una VM local permite preparar conceptos, pero no demuestra los CE que exigen crear, desplegar o utilizar recursos administrados de un proveedor. Esos criterios quedan pendientes cuando no se dispone de plataforma; no se rellenan con capturas de ejemplo.

<a id="ra1"></a>
## RA1 · Comparar servicio en nube y servicio local

**Enunciado oficial:** Define qué es la computación en la nube.

La nube combina provisión bajo demanda, servicios y responsabilidades distribuidas. IaaS, PaaS y SaaS cambian lo que administra el cliente, pero no eliminan la necesidad de decidir identidades, datos, recuperación y salida del proveedor.

### Actividad CMO-312-RA1-A1

1. Describe una pequeña aplicación de tickets y sus requisitos.
2. Clasifica sus componentes en un diseño local, IaaS, PaaS y SaaS.
3. Compara elasticidad, dependencia de red, mantenimiento y control de datos.
4. Propón fases de adopción con requisitos medibles y una condición de retorno.

**Solución razonada y errores que debes interpretar:** Migrar una VM sin revisar licencias, copias o identidad sólo cambia parte de la infraestructura. La alternativa elegida se justifica por necesidad y capacidad operativa; no se supone que nube sea siempre más económica.

**Entregable:** Matriz de modelos y plan básico de adopción.

**Aceptación del reto:** Cada alternativa asigna tareas a cliente/proveedor y conserva requisitos de datos y continuidad.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han definido los diferentes modelos de computación en la nube. | Matriz de modelos y plan básico de adopción; apartado a con datos, explicación o salida referida expresamente a ese criterio. Cada alternativa asigna tareas a cliente/proveedor y conserva requisitos de datos y continuidad. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han descrito las ventajas de la computación en la nube frente a la computación en las instalaciones. | Matriz de modelos y plan básico de adopción; apartado b con datos, explicación o salida referida expresamente a ese criterio. Cada alternativa asigna tareas a cliente/proveedor y conserva requisitos de datos y continuidad. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han reconocido los servicios esenciales de la computación en la nube. | Matriz de modelos y plan básico de adopción; apartado c con datos, explicación o salida referida expresamente a ese criterio. Cada alternativa asigna tareas a cliente/proveedor y conserva requisitos de datos y continuidad. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se ha revisado el marco de adopción de la nube. | Matriz de modelos y plan básico de adopción; apartado d con datos, explicación o salida referida expresamente a ese criterio. Cada alternativa asigna tareas a cliente/proveedor y conserva requisitos de datos y continuidad. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra2"></a>
## RA2 · Construir un presupuesto con hipótesis visibles

**Enunciado oficial:** Describe la filosofía de precios en la nube.

El coste depende de capacidad, tiempo, almacenamiento, peticiones, transferencia y soporte. Una estimación debe indicar región, moneda, fecha, carga y exclusiones. Los precios del ejercicio son hipotéticos y se sustituyen por la calculadora oficial al preparar una práctica real.

### Actividad CMO-312-RA2-A1

1. Supón dos VM a 0,04 euros/hora durante 100 horas y 50 GB a 0,02 euros/GB-mes.
2. Calcula cómputo y almacenamiento por separado y añade una línea de transferencia aún sin estimar.
3. Repite con 200 horas y compara reserva de capacidad, apagado y soporte.
4. Con una cuenta educativa existente, revisa presupuestos y alertas sin contratar servicios nuevos.

**Solución razonada y errores que debes interpretar:** El supuesto inicial suma 8 euros de cómputo y 1 euro de almacenamiento del mes, antes de transferencia, impuestos o soporte. Duplicar horas duplica cómputo, no necesariamente almacenamiento. Una alerta informa de consumo: no siempre impide que siga facturándose.

**Entregable:** Hoja TCO, escenarios y captura saneada de estimación oficial si se usa.

**Aceptación del reto:** Las partidas y unidades son reproducibles y los límites de la estimación aparecen expresamente.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han reconocido las características fundamentales de los precios. | Hoja TCO, escenarios y captura saneada de estimación oficial si se usa; apartado a con datos, explicación o salida referida expresamente a ese criterio. Las partidas y unidades son reproducibles y los límites de la estimación aparecen expresamente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han indicado los factores que intervienen en el coste total de la propiedad (TCO). | Hoja TCO, escenarios y captura saneada de estimación oficial si se usa; apartado b con datos, explicación o salida referida expresamente a ese criterio. Las partidas y unidades son reproducibles y los límites de la estimación aparecen expresamente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han utilizado servicios para estimar el coste del despliegue de una infraestructura en la nube. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Hoja TCO, escenarios y captura saneada de estimación oficial si se usa»; criterio c. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| d | Se han utilizado los servicios para presupuestar y analizar costes de una infraestructura en la nube. | Hoja TCO, escenarios y captura saneada de estimación oficial si se usa; apartado d con datos, explicación o salida referida expresamente a ese criterio. Las partidas y unidades son reproducibles y los límites de la estimación aparecen expresamente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se han descrito los diferentes planes de soporte de los proveedores de servicios en la nube. | Hoja TCO, escenarios y captura saneada de estimación oficial si se usa; apartado e con datos, explicación o salida referida expresamente a ese criterio. Las partidas y unidades son reproducibles y los límites de la estimación aparecen expresamente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| f | Se han identificado los elementos de optimización de costes de las máquinas virtuales en la nube. | Hoja TCO, escenarios y captura saneada de estimación oficial si se usa; apartado f con datos, explicación o salida referida expresamente a ese criterio. Las partidas y unidades son reproducibles y los límites de la estimación aparecen expresamente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra3"></a>
## RA3 · Situar regiones, zonas y borde

**Enunciado oficial:** Identifica los componentes de la infraestructura en la nube.

Región, zona de disponibilidad y punto de presencia de borde representan ámbitos distintos. Repartir recursos entre zonas no equivale a tener recuperación entre regiones. El nombre comercial y la estructura exacta dependen del proveedor y deben comprobarse en su documentación.

### Actividad CMO-312-RA3-A1

1. Dibuja región, dos zonas y clientes distribuidos.
2. Clasifica cómputo, almacenamiento, red, datos y servicios de borde.
3. Relaciona cada ubicación con latencia, disponibilidad y residencia de datos.
4. Señala qué dependencia común seguiría afectando a ambas zonas.

**Solución razonada y errores que debes interpretar:** Dos instancias en la misma zona no toleran necesariamente un fallo de esa zona. Una CDN puede acercar contenido estático, pero no sustituye por sí sola la base de datos ni la autenticación de la aplicación.

**Entregable:** Mapa de infraestructura y clasificación de servicios.

**Aceptación del reto:** El diagrama distingue los tres ámbitos y no atribuye independencia a componentes compartidos.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han identificado las diferencias entre regiones, zonas de disponibilidad y zonas de borde. | Mapa de infraestructura y clasificación de servicios; apartado a con datos, explicación o salida referida expresamente a ese criterio. El diagrama distingue los tres ámbitos y no atribuye independencia a componentes compartidos. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han identificado las diferentes categorías y servicios en la nube. | Mapa de infraestructura y clasificación de servicios; apartado b con datos, explicación o salida referida expresamente a ese criterio. El diagrama distingue los tres ámbitos y no atribuye independencia a componentes compartidos. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra4"></a>
## RA4 · Preparar identidad y responsabilidad compartida

**Enunciado oficial:** Describe las medidas de seguridad y conformidad de la nube.

Antes de desplegar se define quién autentica, qué rol usa la aplicación y qué operaciones se permiten. Las claves de una persona no deben incrustarse en un programa. El reparto de seguridad cambia entre VM, plataforma administrada y aplicación contratada.

### Actividad CMO-312-RA4-A1

1. Construye una matriz de responsabilidades para VM y base administrada.
2. En el sandbox autorizado crea identidades de prueba, grupos y un rol con permiso de lectura acotado.
3. Contrasta una acción permitida y otra denegada y registra cómo se revoca el acceso.
4. Clasifica datos, cifrado, custodia de claves y evidencias de conformidad sin afirmar una certificación propia.

**Solución razonada y errores que debes interpretar:** El mínimo privilegio se demuestra con operaciones, no con el nombre del rol. Si no hay sandbox, la matriz y las políticas propuestas son preparación; el criterio de crear identidades y comprobarlas queda pendiente de ejecución.

**Entregable:** Matriz de responsabilidades, política y registro de acceso permitido/denegado.

**Aceptación del reto:** Las identidades reales del ejercicio tienen permisos limitados y se distingue diseño de ejecución.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha reconocido el modelo de responsabilidad compartida. | Matriz de responsabilidades, política y registro de acceso permitido/denegado; apartado a con datos, explicación o salida referida expresamente a ese criterio. Las identidades reales del ejercicio tienen permisos limitados y se distingue diseño de ejecución. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han identificado las responsabilidades del cliente y del proveedor de servicios en la nube. | Matriz de responsabilidades, política y registro de acceso permitido/denegado; apartado b con datos, explicación o salida referida expresamente a ese criterio. Las identidades reales del ejercicio tienen permisos limitados y se distingue diseño de ejecución. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han reconocido las entidades que intervienen en el proceso de autenticación. | Matriz de responsabilidades, política y registro de acceso permitido/denegado; apartado c con datos, explicación o salida referida expresamente a ese criterio. Las identidades reales del ejercicio tienen permisos limitados y se distingue diseño de ejecución. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han descrito los diferentes tipos de credenciales de seguridad en la nube. | Matriz de responsabilidades, política y registro de acceso permitido/denegado; apartado d con datos, explicación o salida referida expresamente a ese criterio. Las identidades reales del ejercicio tienen permisos limitados y se distingue diseño de ejecución. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se han creado usuarios, grupos y roles. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Matriz de responsabilidades, política y registro de acceso permitido/denegado»; criterio e. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| f | Se ha reconocido cómo proteger los datos en la nube. | Matriz de responsabilidades, política y registro de acceso permitido/denegado; apartado f con datos, explicación o salida referida expresamente a ese criterio. Las identidades reales del ejercicio tienen permisos limitados y se distingue diseño de ejecución. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| g | Se han reconocido los diferentes programas de conformidad. | Matriz de responsabilidades, política y registro de acceso permitido/denegado; apartado g con datos, explicación o salida referida expresamente a ese criterio. Las identidades reales del ejercicio tienen permisos limitados y se distingue diseño de ejecución. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra5"></a>
## RA5 · Diseñar y crear una red privada virtual

**Enunciado oficial:** Crea una nube privada virtual.

Una VPC agrupa redes y controles del proveedor. Definir CIDR, subredes y rutas es distinto de publicar un servicio. Una subred no es pública sólo por su nombre: cuentan rutas, direcciones y políticas efectivas.

### Actividad CMO-312-RA5-A1

1. Diseña una red 10.60.0.0/16 con subredes 10.60.1.0/24 y 10.60.2.0/24 sin solaparlas con el laboratorio.
2. En una cuenta docente ya habilitada crea la red y subredes; registra IDs y rutas.
3. Añade únicamente los componentes de acceso que el diseño justifique y limita orígenes.
4. Comprueba DNS y explica qué contenido podría distribuir una CDN; elimina recursos según el plan del centro.

**Solución razonada y errores que debes interpretar:** Un dibujo o dos NIC locales no acreditan la creación de una VPC de proveedor. La guía no obliga a abrir una cuenta de pago: si no existe plataforma autorizada, conserva el diseño y marca el despliegue pendiente. La evidencia válida incluye inventario y configuración efectiva del recurso creado.

**Entregable:** Plan CIDR, inventario del sandbox y pruebas de rutas/controles.

**Aceptación del reto:** La red real coincide con el diseño, no tiene solapamientos y sólo permite los trayectos previstos.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han reconocido los conceptos básicos de redes. | Plan CIDR, inventario del sandbox y pruebas de rutas/controles; apartado a con datos, explicación o salida referida expresamente a ese criterio. La red real coincide con el diseño, no tiene solapamientos y sólo permite los trayectos previstos. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han descrito las redes virtuales en la nube. | Plan CIDR, inventario del sandbox y pruebas de rutas/controles; apartado b con datos, explicación o salida referida expresamente a ese criterio. La red real coincide con el diseño, no tiene solapamientos y sólo permite los trayectos previstos. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han diseñado arquitecturas básicas de redes privadas en la nube. | Plan CIDR, inventario del sandbox y pruebas de rutas/controles; apartado c con datos, explicación o salida referida expresamente a ese criterio. La red real coincide con el diseño, no tiene solapamientos y sólo permite los trayectos previstos. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han indicado los pasos para desplegar una red privada en la nube. | Plan CIDR, inventario del sandbox y pruebas de rutas/controles; apartado d con datos, explicación o salida referida expresamente a ese criterio. La red real coincide con el diseño, no tiene solapamientos y sólo permite los trayectos previstos. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se ha creado una red privada en la nube y se han agregado los componentes necesarios para personalizarla. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Plan CIDR, inventario del sandbox y pruebas de rutas/controles»; criterio e. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| f | Se han identificado los aspectos fundamentales de los servicios de nombres de dominio en la nube. | Plan CIDR, inventario del sandbox y pruebas de rutas/controles; apartado f con datos, explicación o salida referida expresamente a ese criterio. La red real coincide con el diseño, no tiene solapamientos y sólo permite los trayectos previstos. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| g | Se han reconocido los beneficios de utilizar redes de entrega de contenidos en la nube. | Plan CIDR, inventario del sandbox y pruebas de rutas/controles; apartado g con datos, explicación o salida referida expresamente a ese criterio. La red real coincide con el diseño, no tiene solapamientos y sólo permite los trayectos previstos. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra6"></a>
## RA6 · Elegir cómputo para una carga concreta

**Enunciado oficial:** Describe los casos de uso de los diferentes servicios de computación en nube.

VM, plataforma web, funciones y contenedores administrados ofrecen distintos grados de control y operación. Serverless no significa ausencia de servidores ni coste nulo. La duración, estado, concurrencia, arranque y dependencias influyen en la elección.

### Actividad CMO-312-RA6-A1

1. Compara un proceso continuo, una web y una tarea por evento.
2. En el sandbox autorizado lanza una VM mínima desde imagen oficial y prueba acceso por el mecanismo previsto.
3. Documenta qué cambiaría al usar plataforma web, función o clúster de contenedores.
4. Detén y retira los recursos del ensayo incluyendo discos que se mantengan aparte.

**Solución razonada y errores que debes interpretar:** La VM requiere administrar su SO; una función necesita controlar permisos, evento y límites aunque no se administre el anfitrión. La selección debe relacionar carga y responsabilidad, y el lanzamiento se demuestra mediante estado y operación del recurso.

**Entregable:** Comparación de cómputo y acta de lanzamiento/retirada de VM.

**Aceptación del reto:** Se justifica cada caso de uso y la VM del sandbox responde sin accesos públicos innecesarios.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han descrito los diferentes servicios de cómputo en la nube. | Comparación de cómputo y acta de lanzamiento/retirada de VM; apartado a con datos, explicación o salida referida expresamente a ese criterio. Se justifica cada caso de uso y la VM del sandbox responde sin accesos públicos innecesarios. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han identificado los casos de uso de las máquinas virtuales en la nube. | Comparación de cómputo y acta de lanzamiento/retirada de VM; apartado b con datos, explicación o salida referida expresamente a ese criterio. Se justifica cada caso de uso y la VM del sandbox responde sin accesos públicos innecesarios. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han lanzado máquinas virtuales en la nube. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Comparación de cómputo y acta de lanzamiento/retirada de VM»; criterio c. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |
| d | Se han identificado los casos de uso de los servicios administrados de despliegue de aplicaciones web. | Comparación de cómputo y acta de lanzamiento/retirada de VM; apartado d con datos, explicación o salida referida expresamente a ese criterio. Se justifica cada caso de uso y la VM del sandbox responde sin accesos públicos innecesarios. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se han identificado los casos de uso de los servicios de funciones sin servidor. | Comparación de cómputo y acta de lanzamiento/retirada de VM; apartado e con datos, explicación o salida referida expresamente a ese criterio. Se justifica cada caso de uso y la VM del sandbox responde sin accesos públicos innecesarios. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| f | Se han identificado los casos de uso de los servicios de contenedorización en un clúster de servidores administrados. | Comparación de cómputo y acta de lanzamiento/retirada de VM; apartado f con datos, explicación o salida referida expresamente a ese criterio. Se justifica cada caso de uso y la VM del sandbox responde sin accesos públicos innecesarios. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra7"></a>
## RA7 · Relacionar almacenamiento y patrón de acceso

**Enunciado oficial:** Describe y diferencia los servicios de almacenamiento en la nube.

Objetos, bloques, archivos compartidos y archivo a largo plazo tienen interfaces y costes distintos. Un contenedor de objetos no se comporta automáticamente como un disco local; restaurar un archivo archivado puede tener latencia y coste adicionales.

### Actividad CMO-312-RA7-A1

1. Asigna almacenamiento a discos de VM, documentos compartidos, imágenes web y copias históricas.
2. Compara acceso, consistencia, durabilidad, permisos, retención y recuperación.
3. Diseña una política de ciclo de vida con requisitos de recuperación.
4. Ensaya con datos sintéticos en sandbox si está disponible y documenta retirada.

**Solución razonada y errores que debes interpretar:** Un disco de bloques sirve a una VM; un recurso de archivos permite protocolos compartidos; objetos se consumen mediante su API. Elegir archivo frío para datos que deben recuperarse de inmediato puede incumplir el requisito aunque el precio por capacidad sea menor.

**Entregable:** Matriz de almacenamiento y política de recuperación/ciclo de vida.

**Aceptación del reto:** Cada carga tiene interfaz y recuperación compatibles, con permisos y costes considerados.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han diferenciado los tipos de servicios de almacenamiento en la nube. | Matriz de almacenamiento y política de recuperación/ciclo de vida; apartado a con datos, explicación o salida referida expresamente a ese criterio. Cada carga tiene interfaz y recuperación compatibles, con permisos y costes considerados. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han descrito los servicios de almacenamiento de objetos en la nube y se ha identificado sus funcionalidades. | Matriz de almacenamiento y política de recuperación/ciclo de vida; apartado b con datos, explicación o salida referida expresamente a ese criterio. Cada carga tiene interfaz y recuperación compatibles, con permisos y costes considerados. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han descrito los servicios de almacenamiento de bloques en la nube y se ha identificado sus funcionalidades. | Matriz de almacenamiento y política de recuperación/ciclo de vida; apartado c con datos, explicación o salida referida expresamente a ese criterio. Cada carga tiene interfaz y recuperación compatibles, con permisos y costes considerados. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han descrito los servicios de almacenamiento de ficheros en la nube y se ha identificado sus funcionalidades. | Matriz de almacenamiento y política de recuperación/ciclo de vida; apartado d con datos, explicación o salida referida expresamente a ese criterio. Cada carga tiene interfaz y recuperación compatibles, con permisos y costes considerados. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se han identificado los servicios de archivado de datos en la nube y se han identificado sus funcionalidades. | Matriz de almacenamiento y política de recuperación/ciclo de vida; apartado e con datos, explicación o salida referida expresamente a ese criterio. Cada carga tiene interfaz y recuperación compatibles, con permisos y costes considerados. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra8"></a>
## RA8 · Desplegar una base de datos administrada

**Enunciado oficial:** Describe, diferencia y despliega bases de datos administradas en la nube.

Relacional, NoSQL y analítica responden a modelos de acceso distintos. Administrada no significa que el proveedor diseñe el esquema, conceda permisos correctos a la aplicación o pruebe la restauración por el cliente.

### Actividad CMO-312-RA8-A1

1. Compara inventario transaccional, documentos variables y análisis agregado.
2. En sandbox ya autorizado crea una base relacional privada y una cuenta de aplicación acotada.
3. Desde un cliente autorizado crea datos sintéticos, consulta y prueba una denegación.
4. Revisa backup, punto recuperable y retirada; una SQLite local sólo prepara SQL y no acredita servicio administrado.

**Solución razonada y errores que debes interpretar:** La evidencia del despliegue incluye recurso, acceso privado y una consulta de aplicación. Si la consola muestra creado pero la aplicación no conecta, todavía falta una dependencia. Las credenciales se custodian fuera del repositorio y se revocan al terminar.

**Entregable:** Ficha de selección, inventario de base y transacción sintética verificada.

**Aceptación del reto:** El servicio administrado se usa realmente desde el cliente previsto y respeta controles de acceso.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han descrito e identificado las funcionalidades de los servicios administrados de bases de datos relacionales. | Ficha de selección, inventario de base y transacción sintética verificada; apartado a con datos, explicación o salida referida expresamente a ese criterio. El servicio administrado se usa realmente desde el cliente previsto y respeta controles de acceso. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han descrito e identificado las funcionalidades de los servicios administrados de bases de datos NoSQL. | Ficha de selección, inventario de base y transacción sintética verificada; apartado b con datos, explicación o salida referida expresamente a ese criterio. El servicio administrado se usa realmente desde el cliente previsto y respeta controles de acceso. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han descrito e identificado las funcionalidades de los servicios administrados de bases de datos analíticas. | Ficha de selección, inventario de base y transacción sintética verificada; apartado c con datos, explicación o salida referida expresamente a ese criterio. El servicio administrado se usa realmente desde el cliente previsto y respeta controles de acceso. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han desplegado bases de datos relacionales administradas en la nube. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Ficha de selección, inventario de base y transacción sintética verificada»; criterio d. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |

<a id="ra9"></a>
## RA9 · Revisar una arquitectura con criterios explícitos

**Enunciado oficial:** Describe los principios arquitectónicos en la nube.

Los marcos de buena arquitectura agrupan preguntas de operación, seguridad, fiabilidad, rendimiento, coste y sostenibilidad. Debe comprobarse el marco y versión del proveedor; una lista de pilares no demuestra que una instalación los cumpla.

### Actividad CMO-312-RA9-A1

1. Relaciona cada pilar con un requisito y una evidencia del caso de tickets.
2. Identifica punto único de fallo, dependencia de identidad y estrategia de recuperación.
3. Obtén recomendaciones del servicio de revisión del proveedor cuando exista acceso docente.
4. Prioriza dos mejoras indicando efecto esperado, esfuerzo y prueba.

**Solución razonada y errores que debes interpretar:** Una recomendación automática es una entrada para el análisis. Puede no conocer todos los requisitos de negocio ni autorizar un cambio. La entrega explica qué se acepta, qué se pospone y con qué evidencia se comprobará la mejora.

**Entregable:** Informe de revisión arquitectónica y plan priorizado.

**Aceptación del reto:** Cada decisión enlaza requisito, evidencia y consecuencia; se distingue disponibilidad de recuperación.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha descrito el marco de la buena arquitectura en la nube. | Informe de revisión arquitectónica y plan priorizado; apartado a con datos, explicación o salida referida expresamente a ese criterio. Cada decisión enlaza requisito, evidencia y consecuencia; se distingue disponibilidad de recuperación. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han identificado los seis pilares de la buena arquitectura y se han identificado los principios de diseño. | Informe de revisión arquitectónica y plan priorizado; apartado b con datos, explicación o salida referida expresamente a ese criterio. Cada decisión enlaza requisito, evidencia y consecuencia; se distingue disponibilidad de recuperación. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se ha explicado la importancia de la fiabilidad y de la alta disponibilidad. | Informe de revisión arquitectónica y plan priorizado; apartado c con datos, explicación o salida referida expresamente a ese criterio. Cada decisión enlaza requisito, evidencia y consecuencia; se distingue disponibilidad de recuperación. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han utilizado los servicios administrados para obtener recomendaciones arquitectónicas. | Informe de revisión arquitectónica y plan priorizado; apartado d con datos, explicación o salida referida expresamente a ese criterio. Cada decisión enlaza requisito, evidencia y consecuencia; se distingue disponibilidad de recuperación. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra10"></a>
## RA10 · Comprobar elasticidad, balanceo y señales

**Enunciado oficial:** Entiende los conceptos de balanceado de carga, autoescalado y monitorización para el diseño de arquitecturas elásticas.

El balanceador distribuye peticiones entre destinos sanos; el autoescalado modifica capacidad ante una política y métricas. Añadir instancias no corrige por sí solo una base saturada o sesiones guardadas únicamente en un servidor.

### Actividad CMO-312-RA10-A1

1. Define salud, latencia y tasa de error con población e intervalo.
2. En sandbox prepara dos destinos con identificación visible y un balanceador.
3. Ensaya la retirada de un destino de prácticas y registra distribución y continuidad.
4. Configura o simula una política de escalado; distingue el ensayo real de una tabla de cálculo y retira recursos.

**Solución razonada y errores que debes interpretar:** La prueba debe mostrar qué destino atendió y cómo se comporta el balanceador ante un fallo. Una política que se dispara después de una carga breve puede llegar tarde; registra tiempos de arranque, umbrales y recuperación, sin generar carga contra sistemas externos.

**Entregable:** Matriz de peticiones, métricas y política de escalado.

**Aceptación del reto:** Se demuestra balanceo, estado de destinos y reacción medida; el autoescalado real pendiente no se declara ejecutado.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha indicado cómo distribuir el tráfico entre diferentes máquinas virtuales utilizando balanceadores de carga. | Matriz de peticiones, métricas y política de escalado; apartado a con datos, explicación o salida referida expresamente a ese criterio. Se demuestra balanceo, estado de destinos y reacción medida; el autoescalado real pendiente no se declara ejecutado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han identificado los servicios de monitorización de recursos y aplicaciones en tiempo real. | Matriz de peticiones, métricas y política de escalado; apartado b con datos, explicación o salida referida expresamente a ese criterio. Se demuestra balanceo, estado de destinos y reacción medida; el autoescalado real pendiente no se declara ejecutado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se ha indicado el funcionamiento de los servicios de escalado automático en respuesta a cambios en las cargas de trabajo. | Matriz de peticiones, métricas y política de escalado; apartado c con datos, explicación o salida referida expresamente a ese criterio. Se demuestra balanceo, estado de destinos y reacción medida; el autoescalado real pendiente no se declara ejecutado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han realizado tareas de escalado y balanceo de carga para aumentar la elasticidad de una infraestructura. | Inventario y registro de la operación en el sandbox autorizado, dentro de «Matriz de peticiones, métricas y política de escalado»; criterio d. El recurso o servicio exigido se ha creado o utilizado realmente y se verifica su estado y función. Si sólo existe diseño o simulación local, se registra pendiente. |

## Dossier final y autoevaluación

Reúne las actividades por RA y enlaza cada CE con el artefacto concreto que lo demuestra. Una memoria extensa sin resultados identificables no sustituye las pruebas; una configuración que funciona por casualidad debe revisarse con casos de límite y recuperación. Explica las dependencias y qué haría falta para repetir el trabajo en otro equipo.

Como rúbrica de práctica se propone valorar corrección técnica (40 %), evidencia y pruebas (30 %), explicación de decisiones (20 %) y documentación/revisión (10 %). Es una propuesta propia: los instrumentos, ponderaciones y calificaciones oficiales corresponden al centro. Los CE no ejecutados o sin medios disponibles se anotan pendientes, sin inventar una adquisición del RA.

## Referencias y datos de trazabilidad

- [Matriz completa de este módulo](alineacion-ra.json).
- [Referentes normativos del repositorio](../../recursos/ra/referentes-oficiales.json).
- [AWS: responsabilidad compartida](https://aws.amazon.com/compliance/shared-responsibility-model/).
- [AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).
