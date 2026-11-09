# 5. Riesgos, impacto de negocio y diseño de controles

[Índice del módulo](README.md) · [Fundamentos](01-fundamentos.md) · [Continuidad](07-criptografia-copias-y-continuidad.md)

## 5.1 Comenzar por el servicio que necesita la organización

Un análisis de seguridad empieza con las actividades que se quieren proteger. «Tenemos un servidor» describe un componente; «doce personas deben consultar y actualizar órdenes durante la jornada» describe una necesidad. La disponibilidad del servidor puede ser importante porque soporta esa actividad, y la confidencialidad puede ser relevante porque contiene información de clientes. El control se justifica por el daño que reduce, no por su nombre comercial.

El caso de este capítulo es una pequeña oficina ficticia con doce puestos, un servicio de archivos, una aplicación web interna y soporte técnico compartido. Todos los nombres, cantidades y valoraciones son hipótesis didácticas. No se pretende presentar una estimación real de pérdidas de una organización concreta. El objetivo es construir un razonamiento que permita discutir prioridades y recoger los datos que faltarían.

Un inventario de activos incluye datos, personas, procesos, software, hardware y proveedores. Si sólo se enumeran equipos, desaparecen dependencias como la contraseña de recuperación, la persona que conoce la aplicación o el canal utilizado para avisar de un incidente. Asigna propietario funcional a la información y responsable operativo al sistema. La misma persona puede ocupar ambos papeles, pero debe distinguir qué decisiones adopta en cada uno.

## 5.2 Dependencias y puntos únicos de fallo

Dibuja la actividad desde la persona usuaria hasta los datos. Para abrir una carpeta mediante nombre de dominio pueden intervenir red, DNS, directorio, hora, identidad del cliente, servidor de archivos, almacenamiento y permisos. Para restaurarla, además se necesitan copia, clave, herramienta y capacidad de destino. Un control aislado en un componente puede dejar intacto un fallo en otra dependencia.

| Servicio del caso | Dependencias principales | Consecuencia de pérdida |
| --- | --- | --- |
| Archivos operativos | LAN, identidad, SMB, disco y permisos | Se detiene edición y consulta normal |
| Aplicación interna | DNS, HTTPS, aplicación y base de datos | Se retrasa el registro de tareas |
| Identidad central | DNS, hora, DC y claves | Nuevas autenticaciones y administración afectadas |
| Restauración | Copia separada, clave y procedimiento | Se prolonga o impide la recuperación |
| Comunicación | Contactos y canal alternativo | Decisiones descoordinadas o tardías |

Un único DC es un punto de dependencia importante en este laboratorio, pero añadir otro no elimina todas las causas comunes. Dos controladores en el mismo anfitrión, el mismo almacenamiento y la misma fuente eléctrica comparten riesgos. Lo mismo ocurre con dos copias en directorios distintos del mismo disco. La redundancia se evalúa en relación con la causa que se pretende soportar.

Para cada dependencia pregunta cómo se detecta su fallo y qué alternativa existe. Una alternativa manual puede mantener temporalmente parte de la actividad, pero necesita instrucciones y control de integridad para reintroducir los datos después. «Se apuntará en papel» no es una estrategia completa si nadie define campos, custodia, numeración y conciliación.

## 5.3 BIA: medir consecuencias según tiempo y datos

El análisis de impacto de negocio estudia qué ocurre cuando una actividad pierde disponibilidad o datos. No asigna automáticamente probabilidad de un ataque. En el caso, se plantea que una indisponibilidad de archivos de 15 minutos provoca molestias, de dos horas retrasa operaciones y de un día afecta a compromisos. Esas categorías se validan con quien conoce el proceso; el administrador no puede inventarlas como si fueran requisitos confirmados.

Define objetivos de recuperación con alcance. Un RTO de dos horas significa un objetivo temporal para recuperar una función concreta bajo las condiciones del plan; no asegura que toda la infraestructura vuelva al estado previo en dos horas. Un RPO de cuatro horas limita la pérdida temporal admitida de datos para un conjunto definido. Si la copia se realiza una vez al día, no suele satisfacer por sí sola un RPO de cuatro horas frente a pérdida completa del origen.

También distingue integridad y confidencialidad. Recuperar rápidamente una base cuyos datos fueron alterados puede restaurar el servicio equivocado. Una copia muy reciente puede contener la modificación maliciosa o accidental, de modo que el plan necesita varios puntos de recuperación y pruebas para elegir uno confiable. La disponibilidad no se da por satisfecha si el servicio responde con datos incoherentes.

Un BIA didáctico debe indicar actividad, responsable, ventanas críticas, efectos por duración, conjunto de datos, RTO/RPO propuestos y dependencia de validación. Cuando falte información, se marca «pendiente de confirmar». La transparencia sobre supuestos permite mejorar el análisis; una tabla completa de números inventados no proporciona esa garantía.

## 5.4 Amenaza, vulnerabilidad, escenario y riesgo

Una amenaza es una causa potencial de daño. Una vulnerabilidad es una debilidad que puede facilitarlo. Un escenario relaciona ambas con un activo y una consecuencia: una cuenta con privilegios excesivos modifica archivos compartidos tras un acceso no autorizado, y la copia conectada con las mismas credenciales también resulta alterada. Esa descripción permite identificar varios controles y sus límites.

No expreses riesgos como «tener virus» o «el servidor es inseguro». Describe origen, condición, acción, activo y efecto. También hay errores, averías y causas ambientales: una actualización incorrecta o una eliminación accidental puede detener una actividad sin intención maliciosa. La seguridad operacional necesita considerar esos escenarios junto con las amenazas deliberadas.

Para la oficina se propone una escala ordinal de probabilidad de 1 a 5 y de impacto de 1 a 5. Sus números representan categorías, no mediciones de frecuencia exacta. Multiplicarlos produce una ayuda de priorización definida por el ejercicio, pero una puntuación 20 no implica que el riesgo sea el doble de otro puntuado 10. No conviertas resultados ordinales en pérdidas monetarias esperadas.

| Escenario | Probabilidad supuesta | Impacto supuesto | Producto didáctico | Fundamento a contrastar |
| --- | ---: | ---: | ---: | --- |
| Borrado accidental de documentos | 4 | 3 | 12 | Muchas operaciones y restauración no ensayada |
| Cuenta de soporte comprometida | 3 | 5 | 15 | Privilegios amplios y acceso a varias funciones |
| Fallo del disco principal | 3 | 4 | 12 | Equipo sin redundancia y copia externa disponible |
| Pérdida del único equipo de backup | 2 | 5 | 10 | Sin segunda copia independiente |
| Error de cambio en DNS | 3 | 3 | 9 | Sin validación ni revisión previa |

Estas puntuaciones son supuestos para discutir el método. El análisis real utilizaría evidencia de exposición, historial, controles y consecuencias del contexto. Un escenario de puntuación inferior puede necesitar atención urgente si afecta a una obligación o a una dependencia crítica que no refleja bien la escala.

## 5.5 Tratamiento y riesgo residual

Las decisiones habituales incluyen evitar una actividad, reducir el riesgo mediante controles, transferir parte de sus consecuencias contractuales o aceptar el riesgo bajo autoridad apropiada. Contratar un seguro no evita que el servicio se interrumpa ni transfiere todas las responsabilidades. Del mismo modo, un proveedor de nube cambia la distribución de tareas, pero exige revisar identidad, datos, exportación y recuperación.

Un control preventivo intenta disminuir la ocurrencia o facilitar su bloqueo; uno detectivo reduce el tiempo hasta advertir el problema; uno correctivo o de recuperación limita consecuencias posteriores. En el escenario de cuenta comprometida, mínimo privilegio, MFA donde esté disponible, segmentación y separación de credenciales reducen exposición; registros ayudan a detectar; copias protegidas y procedimientos permiten recuperar. Ninguna etiqueta garantiza eficacia sin prueba.

El riesgo residual se evalúa después del tratamiento con supuestos actualizados. No reduzcas automáticamente todos los valores a uno porque has instalado una herramienta. Si el backup comparte credenciales de escritura con el servidor protegido, la amenaza que afecta a ambos permanece. Si la MFA sólo protege un portal pero existen accesos alternativos no cubiertos, debe reflejarse esa limitación.

La aceptación del riesgo tiene responsable, alcance y revisión. Un estudiante puede proponerla en el caso, pero no atribuirse la decisión de una organización real. Mantén un registro con riesgo, decisión, justificación, propietario, control previsto, fecha objetivo, evidencia y estado. Un control pendiente de instalación no cuenta como riesgo ya reducido.

## 5.6 Relacionar controles con pruebas y costes

Un control debe tener una condición verificable. «Usar contraseñas seguras» es demasiado vago para aceptar una configuración. Una formulación operativa identifica métodos de autenticación admitidos, cuentas, política aplicada, canal de recuperación y prueba de acceso. «Hacer backup» se convierte en frecuencia, conjuntos, destinos, retención, protección de claves y restauración medida.

| Riesgo | Control propuesto | Prueba de eficacia | Limitación que permanece |
| --- | --- | --- | --- |
| Error de cambio DNS | Copia y validación antes de recarga | Zona inválida de ensayo rechazada sin sustituir servicio válido | Puede haber error lógico con sintaxis válida |
| Escritura excesiva | Grupos por función y matriz de permisos | Lector no crea ni modifica; editor sí | Cuenta editora comprometida conserva capacidad de editar |
| Pérdida del origen | Copia separada y puntos históricos | Restauración aislada de archivo y servicio | Recuperación depende de clave y capacidad de destino |
| Fallo administrativo remoto | Consola y procedimiento de retorno | Cambio reversible con acceso comprobado | Pérdida del anfitrión requiere otro nivel de recuperación |

El coste incluye operación y complejidad, no sólo adquisición. Una solución que exige seis horas semanales de mantenimiento puede ser inviable para un equipo que dispone de dos. Una política demasiado compleja que nadie entiende produce errores y dificulta diagnóstico. Compara alternativas con el mismo requisito y reconoce qué se deja fuera del presupuesto.

Ejemplo hipotético: un ensayo mensual de recuperación consume 1,5 horas de preparación, 1 de ejecución y 0,5 de documentación, tres horas mensuales. A un coste interno supuesto de 22 €/hora son 66 € de capacidad de trabajo al mes. No es necesariamente un pago adicional, pero sí recurso que debe planificarse. No se afirma que ese importe sea un precio de mercado ni un coste legal.

## 5.7 Priorización con dependencias

Si el servicio crítico depende de DNS y autenticación, puede convenir asegurar primero su recuperación antes de añadir una medida de presentación sobre la web interna. Una lista ordenada exclusivamente por puntuación puede pasar por alto esa dependencia. Agrupa trabajos que comparten causa o precondición: inventario, separación de identidades, copias, configuración y monitorización.

Distingue medida inmediata y mejora estructural. Si falta una copia independiente, realizar una copia protegida y comprobar un archivo puede ser una acción inicial, mientras se diseña la política completa de retención y restauración. Esa acción no autoriza a marcar toda la continuidad como terminada. Registra el avance por evidencias y mantén visibles los aspectos pendientes.

La priorización también incluye cambios reversibles de bajo impacto que aclaran el estado. Inventariar puertos, comprobar actualizaciones y documentar propietarios puede proporcionar información antes de imponer políticas generales. Un endurecimiento sin conocer servicios puede interrumpir una función legítima y crear un nuevo incidente.

## 5.8 Taller: construir un plan de tratamiento

### Procedimiento

1. Elabora un inventario de diez activos del caso y relaciona al menos cinco dependencias.
2. Elige tres actividades y define consecuencias de interrupción en tres intervalos temporales.
3. Propón RTO/RPO con sus supuestos y marca la aprobación como pendiente del propietario funcional.
4. Redacta seis escenarios, incluyendo error humano, avería y compromiso de cuenta.
5. Asigna categorías justificadas y registra qué evidencia necesitarías para mejorarlas.
6. Diseña un control preventivo, uno detectivo y uno de recuperación para el escenario prioritario.
7. Define una prueba positiva, una negativa y una recuperación para cada control operativo.
8. Estima coste de implantación y mantenimiento con unidades y periodos coherentes.
9. Describe riesgo residual y responsable de su revisión.

### Solución orientativa

Una propuesta defendible puede priorizar separación de credenciales administrativas, política de permisos y copia independiente. La justificación conecta esos controles con acceso a muchos datos y falta de recuperación demostrada. No se aceptaría sustituir el razonamiento por «es la mejor práctica». Debes explicar qué amenaza o efecto cambia, qué no cubre la medida y cómo comprobarás la mejora.

**Entregables:** diagrama, BIA, registro de riesgos, plan de tratamiento y matriz de pruebas. **Rúbrica propia:** claridad de escenarios 25 %, dependencias e impacto 25 %, controles y evidencia 30 %, costes/riesgo residual 20 %. No existe una única puntuación correcta porque el caso contiene supuestos; sí existen justificaciones incoherentes que deben corregirse.

## Referencias primarias

- [INCIBE: guía de gestión de riesgos](https://www.incibe.es/empresas/guias/gestion-de-riesgos-una-guia-de-aproximacion-para-el-empresario-actualizacion).
- [INCIBE: plan de contingencia y continuidad de negocio](https://www.incibe.es/sites/default/files/contenidos/dosieres/metad_plan_de_contingencia_y_continuidad_de_negocio.pdf).
- [BOE: Real Decreto 311/2022, Esquema Nacional de Seguridad](https://www.boe.es/eli/es/rd/2022/05/03/311/con).
- [AEPD: gestión del riesgo y evaluación de impacto](https://www.aepd.es/guias/gestion-riesgo-y-evaluacion-impacto-en-tratamientos-datos-personales.pdf).
