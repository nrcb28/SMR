# Cuaderno de requisitos, trazabilidad y planificación

[Índice](README.md) · [Memoria, pruebas y defensa](04-memoria-modelo-y-defensa-tecnica.md)

Este cuaderno amplía el proyecto de la oficina ficticia de doce puestos. Sus matrices y horas de reparto son propuestas didácticas propias. No fijan la programación del centro ni sustituyen las instrucciones madrileñas: el inicio se concreta por el centro y, en presencial, no puede ser posterior al comienzo de segundo. La referencia de cincuenta horas no se convierte aquí en una carga semanal oficial.

## 1. Convertir una petición en alcance

La petición “necesitamos una red segura” no permite presupuestar ni aceptar una solución. Identifica personas usuarias, tareas, datos, disponibilidad, acceso y restricciones. En el caso base hay cuatro puestos de administración y ocho de soporte; necesitan archivos por función, documentación común, intranet y recuperación. El proyecto debe demostrar una muestra representativa sin confundir doce puestos previstos con doce VMs efectivamente desplegadas.

Registra cada necesidad con origen y persona que valida. Distingue requisito obligatorio, deseable y extensión. Un dominio AD puede ser una opción de diseño; no lo presentes como obligatorio si la necesidad se satisface con cuentas locales y Samba independiente. La defensa debe explicar qué se pierde y qué se gana al elegir una alternativa.

Define lo excluido: servicios de correo públicos, acceso de clientes externos, alta disponibilidad real, segunda sede y operación de equipos ajenos no forman parte del mínimo. Una exclusión no prohíbe estudiarlos, pero impide marcarlos como implantados o incluidos en un coste que no los contempla. Cualquier ampliación vuelve a revisar arquitectura, seguridad, pruebas y plazo.

La fotografía inicial utiliza inventario sintético, aplicaciones requeridas, tipos de documento, tamaño supuesto de datos y requisitos de acceso. No necesita nombres de clientes ni contenido de documentos reales. El diseño debe permitir que los datos de prueba se sustituyan por otro conjunto equivalente sin perder el sentido del procedimiento.

## 2. Especificación y criterios medibles

Un requisito bien formulado identifica sujeto, acción, condición y resultado. “El usuario editor puede crear un archivo en su carpeta desde cli01 con su cuenta ordinaria” es comprobable; “los permisos son correctos” todavía necesita definición. Añade una prueba negativa y qué evidencia se conservará.

| ID | Requisito ampliado | Criterio de aceptación propuesto | Responsable de validar |
| --- | --- | --- | --- |
| R01 | Configuración de cliente | Obtiene dirección del rango previsto, prefijo y DNS del laboratorio sin gateway LAB ficticio. | Revisor de red |
| R02 | Resolución de intranet | Nombre interno devuelve la dirección documentada y el cliente abre la URL prevista. | Revisor de servicios |
| R03 | Separación por función | Editor escribe; lector consulta; cuenta ajena no accede al área restringida. | Responsable funcional simulado |
| R04 | HTTPS verificable | Nombre, vigencia y cadena válidos con CA del laboratorio confiada. | Revisor de seguridad |
| R05 | Recuperación de datos | Restauración aislada mantiene contenido y permisos, con RPO/RTO comparados con objetivo. | Revisor de continuidad |
| R06 | Procedimiento reproducible | Otra persona realiza una operación usando la guía y registra dudas. | Revisor documental |
| R07 | Trazabilidad de retirada | Ficha identifica decisión, datos y destino del equipo sintético. | Revisor de inventario |
| R08 | Registro correlacionable | Eventos relevantes contienen instante y zona o referencia temporal común. | Revisor de operación |
| R09 | Recuperación de configuración | Se identifica copia, versión y orden de recuperación de dependencias. | Revisor de continuidad |
| R10 | Secretos fuera del repositorio | Archivos entregados no incluyen claves, contraseñas ni datos no autorizados. | Revisor documental |
| R11 | Energía y vida útil | Estimación declara estados, límites y supuestos; no afirma una huella total no calculada. | Revisor de sostenibilidad |
| R12 | Salida y mantenimiento | Se explica exportación, alta/baja y revisión de actualizaciones. | Revisor de operación |

R05 y R09 se relacionan: recuperar archivos no garantiza recuperar el servicio si faltan configuración, identidades o dependencias. Mantén esa relación en diseño y pruebas. Si un requisito cambia, incrementa su revisión y conserva motivo, impacto y decisión. No cambies una condición después de fallar sólo para obtener “cumple”.

## 3. Arquitectura y escenarios separados

El mínimo sigue el [laboratorio común](../../docs/laboratorio.md): srv01 Debian 13 en 192.168.56.10/24, cli01 en .20 y dominio aula.test. LAB es una red aislada; la NIC NAT, si existe, sólo proporciona acceso según el hipervisor y no convierte al servidor en router. Verifica interfaces antes de reutilizar nombres de ejemplos.

En la opción con directorio, dc01 ocupa .11 y administra ad.aula.test en un escenario dedicado. La documentación debe indicar cuál es el DNS utilizado por cada cliente y cómo se resuelve el nombre de la intranet. No instales BIND y otro DNS en la misma dirección/puerto esperando que ambos sirvan indistintamente. Un diagrama con dos roles necesita configuración que materialice su separación.

La extensión VLAN mantiene el diseño distinto del [capítulo inicial](01-guia.md): redes 10.40.10.0/24, 10.40.20.0/24, 10.40.30.0/24 y 10.40.99.0/24 con router y switch compatibles. Migrar exige revisar registros DNS, ámbitos DHCP, certificados por nombre/dirección, reglas, rutas y documentación. No se presenta como simple “activar VLAN” en una red host-only ordinaria.

Para decidir si implementar la extensión, comprueba recursos, herramienta y tiempo de prueba. Una propuesta de segmentación puede entregarse como diseño con matriz de comunicaciones, pero debe quedar marcada como no desplegada si no se han generado y validado los segmentos. El mismo criterio se aplica a redundancia, copias externas o automatización.

## 4. Matriz de trazabilidad

Relaciona cada requisito con diseño, artefacto y prueba. Si un archivo no responde a un requisito, puede ser apoyo útil o trabajo innecesario; explícalo. Si un requisito no tiene prueba, falta evidencia para aceptarlo.

| Requisito | Decisión de diseño | Artefacto previsto | Pruebas |
| --- | --- | --- | --- |
| R01 | DHCP sólo en LAB y rango sin estáticas | Configuración saneada de Kea y tabla IP | T01, T02 |
| R02 | Zona interna explícita | Zona DNS y esquema de nombres | T03 |
| R03 | Grupos lector/editor por función | Matriz de identidades y permisos | T04, T05 |
| R04 | CA interna y nombre coherente | Configuración TLS sin clave privada | T06, T07 |
| R05/R09 | Copias separadas y orden de recuperación | Plan de copia y guion de restauración | T08, T09 |
| R06/R10 | Memoria revisada y configuración sin secretos | Manual de operación y lista de entrega | T10 |
| R07/R11 | Inventario y decisión de ciclo de vida | Fichas sintéticas y hoja de energía | T11 |
| R08/R12 | Bitácora, exportación y mantenimiento | Registro de cambios y plan operativo | T12 |

Los identificadores T01–T12 se desarrollan en el [cuaderno de aceptación](04-memoria-modelo-y-defensa-tecnica.md). Una captura puede apoyar una prueba, pero no reemplaza preparación, estímulo, resultado esperado y real. Guarda salidas legibles y configura nombres de evidencia que permitan localizarlas sin contexto oral.

## 5. WBS y dependencias

Una estructura de desglose de trabajo identifica resultados y actividades. No es una lista de nombres de herramientas. “Instalar Nginx” es una actividad; “intranet accesible por HTTPS desde el cliente con validación TLS” es un resultado más completo que incluye configuración y prueba.

Reparto orientativo de cincuenta horas de trabajo autónomo para este caso:

| Paquete | Esfuerzo propuesto | Dependencia o condición de salida |
| --- | ---: | --- |
| P1 · Requisitos y línea base | 6 h | Necesidades y aceptación definidas. |
| P2 · Diseño y presupuesto | 7 h | P1; arquitectura y roles coherentes. |
| P3 · Preparación del laboratorio | 6 h | P2; inventario, red e instantánea identificados. |
| P4 · Servicios e identidades | 12 h | P3; comprobación incremental por servicio. |
| P5 · Copias y recuperación | 7 h | Datos y servicios de P4; destino separado. |
| P6 · Memoria y revisión | 8 h | Se trabaja durante todo el proyecto; revisión final tras P5. |
| P7 · Ensayo y defensa | 4 h | Evidencias y memoria revisadas. |
| **Total orientativo** | **50 h** | No representa facturación comercial ni horario oficial. |

Esfuerzo y duración no son equivalentes. Dos personas pueden trabajar en paralelo, pero no dividir automáticamente por dos todo el calendario: existen dependencias, coordinación y revisión. Una prueba de recuperación necesita datos y copias; una defensa necesita resultados. La documentación se inicia al definir requisitos y se actualiza con cambios, no se escribe entera al final de memoria.

Establece hitos de salida: diseño revisado, base conectada, servicios verificados, restauración ensayada y entrega reproducible. Si un hito falla, identifica causa y replanifica. No sigas sumando funciones sobre una base que todavía no tiene dirección o resolución coherente.

## 6. Riesgos y respuestas

La escala siguiente usa probabilidad e impacto ordinales de uno a cinco. El producto sirve para ordenar atención dentro del ejercicio; no representa una pérdida financiera esperada ni una probabilidad estadística.

| Riesgo | P | I | P × I | Prevención y respuesta |
| --- | ---: | ---: | ---: | --- |
| Segundo DHCP en LAB | 3 | 4 | 12 | Inventariar hipervisor; capturar identidad del servidor y retirar sólo el servicio que no corresponde. |
| Copia no recuperable | 2 | 5 | 10 | Ensayo temprano, destino independiente y comprobación de integridad/permiso. |
| Confianza TLS incompleta | 3 | 3 | 9 | Comprobar nombre, CA y almacén del cliente y de la aplicación. |
| Aumento tardío de alcance | 3 | 4 | 12 | Registro de cambios y decisión explícita sobre tareas/plazo. |
| Dependencia de una persona | 3 | 3 | 9 | Revisión cruzada y procedimiento que otro integrante pueda seguir. |
| Licencia o soporte sin resolver | 2 | 4 | 8 | Identificar producto y condiciones antes de aceptar una compra o despliegue. |

Cada riesgo necesita responsable y señal de activación. “Tener cuidado” no es una respuesta operativa. Para la copia, la señal puede ser ensayo fallido o copia más antigua que la ventana prevista; la respuesta debe indicar quién revisa y qué tarea se pausa. Revisa riesgos después de cambios de arquitectura y durante hitos.

## 7. Presupuesto, reserva y coste de operación

El presupuesto inicial del [capítulo de diseño](01-guia.md) contiene 6 772 € de materiales y 1 000 € de implantación: 7 772 € parciales sin IVA. Mantén esa referencia en vez de introducir totales incompatibles. Los precios son sintéticos y las cuarenta horas comerciales supuestas no equivalen a las cincuenta horas didácticas del módulo.

Una ampliación documental puede incorporar ocho horas de formación a 25 €/h: 200 €. El subtotal inicial conocido pasa a 7 972 €. Una reserva educativa del 10 % aplicada a ese subtotal añade 797,20 € y produce 8 769,20 €. La reserva cubre incertidumbre presupuestaria del ejemplo; no es un gasto ya efectuado ni una tasa normativa.

Para veinticuatro meses, se suponen administración de dos horas mensuales a 25 €/h, copia externa o soporte de copia de 10 € y energía incremental de 12 €: 72 €/mes y 1 728 € en dos años. El conjunto parcial sería 8 769,20 + 1 728 = 10 497,20 €. La energía es un supuesto económico, no una medida ni una tarifa publicada.

Faltan licencias, conectividad u otros conceptos si resultan necesarios y no se han cuantificado. Por eso el resultado sigue siendo parcial y no autoriza una compra. Distingue decisión técnica, estimación y oferta verificada. Un requisito obligatorio de licencia o soporte no se da por resuelto porque una fila diga “pendiente”.

## 8. Control de cambios y entrega

Cada cambio incluye motivo, requisitos afectados, archivos, dependencias, prueba, reversión y decisión de incorporación. Una modificación de IP exige buscar referencias en DNS, DHCP, firewall y documentos. Una nueva regla de acceso debe acompañarse de matriz y prueba negativa. Guarda una revisión de la memoria que corresponda a la configuración final.

La entrega se prepara con un manifiesto: nombre de archivo, finalidad, versión, origen y clasificación. Los secretos se suministran por el canal acordado y no aparecen en Git, capturas o vídeo de defensa. Una guía saneada puede contener marcadores para valores secretos, pero debe explicar dónde se obtienen y qué permisos necesita quien opera el sistema.

Revisa que el estado declarado coincida con la evidencia: diseñado, configurado, probado, aceptado o pendiente son estados diferentes. La carpeta del proyecto permite estudiar todos, pero la defensa debe decir claramente cuál se alcanzó en cada requisito. Ese rigor aporta más valor que presentar una arquitectura ambiciosa sin comprobaciones.
