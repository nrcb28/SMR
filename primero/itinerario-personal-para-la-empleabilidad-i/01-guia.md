# Guía técnica y profesional de IPE I

## 1. Entender el puesto antes de elegir formación

SMR prepara para tareas de montaje, mantenimiento y soporte de equipos, redes locales y servicios. En un puesto de primer nivel no basta con saber reinstalar: se necesita identificar el impacto de una incidencia, proteger los datos, registrar lo realizado y reconocer cuándo debe intervenir otra persona. Resolver una avería sin autorización o sin una copia recuperable puede causar un daño mayor que el fallo inicial.

Describe el trabajo mediante **tareas observables**, no mediante adjetivos. «Soy resolutivo» no permite evaluar una competencia; «identifico una IP duplicada, documento la prueba y verifico la solución desde un cliente» sí. Una ficha de puesto útil tiene cuatro partes:

1. Servicios atendidos: puestos, periféricos, conectividad, cuentas y aplicaciones.
2. Acciones permitidas: consultar registros, reiniciar bajo procedimiento o sustituir un componente autorizado.
3. Límites: datos sensibles, cambios en producción, electricidad, recuperación avanzada y decisiones de seguridad.
4. Evidencias: ticket, inventario, resultado de verificación y aceptación de la persona usuaria.

Relaciona el inventario de competencias con ofertas reales, separando requisitos obligatorios de preferencias. Una oferta que pide Windows Server no equivale a una que pide únicamente manejo de Windows de escritorio. Anota tecnologías, tareas y nivel esperado; después decide qué práctica demostrará cada requisito. El resultado es un itinerario, no una colección indiscriminada de cursos.

## 2. Prevención: peligro, riesgo y daño

Un **peligro** es una condición con capacidad de causar daño: un cable deteriorado, una batería hinchada o una carga pesada. El **riesgo** expresa la posibilidad de que el daño ocurra en las condiciones de trabajo. El **daño** puede ser una lesión, una alteración de salud o una exposición perjudicial. No confundas el riesgo para el equipo con el de la persona: una descarga electrostática puede destruir memoria sin ser el principal peligro eléctrico del taller.

En España la prevención se organiza en torno a una evaluación, la planificación de medidas y su seguimiento. Los deberes concretos y la participación se consultan en la [Ley de Prevención de Riesgos Laborales](https://www.boe.es/eli/es/l/1995/11/08/31/con). La inspección del alumno es un ejercicio de identificación; la evaluación real corresponde a la organización preventiva y al personal con competencia para ello.

### Inspección sistemática del taller

Recorre primero las zonas de paso y evacuación. Después revisa mesas, tomas eléctricas, almacenamiento, herramientas, iluminación, ventilación y trabajos con pantallas. Observa también cómo se organiza el trabajo: interrupciones, presión por cerrar tickets, falta de instrucciones y jornadas de intervención pueden influir en el riesgo. Registrar solo objetos visibles deja fuera los factores de organización.

Para cada hallazgo identifica la tarea, la persona expuesta, la condición peligrosa, las medidas actuales, la propuesta y el responsable de revisar. Una foto sin localización ni explicación no es una evaluación. En documentación pública usa planos ficticios y evita mostrar accesos, alarmas o detalles de seguridad del centro.

### Jerarquía de medidas

La prioridad didáctica es eliminar el peligro cuando sea posible, sustituir el elemento o proceso problemático, aplicar protecciones colectivas y organizar el trabajo. Los equipos de protección individual se seleccionan en función del riesgo y del procedimiento, no como respuesta automática a cualquier problema.

Ejemplo: ante un cable de alimentación con aislamiento roto, la solución no es usar guantes para seguir trabajando. Se retira el equipo de servicio, se identifica para impedir su uso y se comunica la sustitución conforme al procedimiento. Una cinta añadida por el alumno no constituye una reparación homologada.

## 3. Riesgos específicos en microinformática

### Electricidad y energía almacenada

Antes de una intervención interna se realiza el apagado previsto, se desconecta la alimentación externa y se impide una reconexión accidental según el procedimiento del taller. Los equipos con baterías internas requieren instrucciones del fabricante y herramientas adecuadas. No se asume que apagar el sistema operativo elimina toda fuente de energía.

Las fuentes de alimentación, UPS/SAI, monitores y otros equipos pueden contener partes peligrosas incluso desconectados. En prácticas de SMR se sustituyen como unidades cuando corresponda: **no se abren para reparar su electrónica de potencia**. Un alumno no realiza mediciones de red eléctrica ni verifica ausencia de tensión sin la formación y autorización aplicables.

Las pulseras y superficies ESD protegen componentes frente a electricidad estática. Se emplean únicamente en el entorno y condiciones indicados por el fabricante y el procedimiento, nunca como protección personal ante tensión eléctrica. La toma de tierra improvisada a una tubería o un elemento metálico desconocido no es aceptable.

### Manipulación y almacenamiento

Una caja de ordenadores puede ser difícil de manejar por volumen, agarre o centro de gravedad aunque parezca ligera. Planifica el recorrido, despeja obstáculos, consulta el procedimiento de manipulación y solicita ayuda o medios mecánicos cuando corresponda. Los racks no se trasladan, estabilizan o cargan sin instrucciones; un equipo extraído puede provocar vuelco. Etiqueta estanterías y evita almacenar objetos pesados en posiciones que exijan alcances forzados.

### Baterías, tóner, polvo y residuos

No perfores, comprimas ni intentes recuperar una batería hinchada. Detén el uso del dispositivo y sigue el protocolo de retirada y almacenamiento del centro. El manejo de consumibles se ajusta a su ficha de seguridad y a las instrucciones del fabricante; no se emplean aspiradores domésticos o aire comprimido indiscriminadamente para dispersar polvo de tóner. Los residuos eléctricos, baterías y consumibles tienen canales de gestión diferenciados.

### Puesto con pantalla y organización

Evalúa el conjunto: silla, mesa, pantalla, teclado, ratón, iluminación, ruido, distribución de tareas y necesidades de la persona. La pantalla debe permitir lectura cómoda sin reflejos molestos; los elementos usados con frecuencia deben estar accesibles sin torsión mantenida. Las pausas y cambios de tarea se concretan en la evaluación y la organización del puesto, no en una regla universal de minutos inventada. Consulta la [guía técnica del INSST para pantallas de visualización](https://www.insst.es/documentacion/catalogo-de-publicaciones/guia-tecnica-para-la-evaluacion-y-prevencion-de-los-riesgos-relativos-a-la-utilizacion-de-equipos-con-pantallas-de-visualizacion).

Si alguien refiere molestias, el registro técnico debe permitir comunicar el problema sin diagnosticarlo ni difundir datos de salud. Aumentar el tamaño de letra puede mejorar legibilidad, pero no reemplaza revisar mobiliario, iluminación y carga de trabajo. Una persona distinta puede necesitar un ajuste diferente en el mismo puesto.

## 4. Emergencias y comunicación

Antes de trabajar, localiza las salidas, los puntos de aviso y el procedimiento del centro. Si aparece humo, olor intenso, una batería alterada o una persona afectada, detén la actividad y avisa. No manipules el equipo peligroso ni te expongas para salvar datos. En una emergencia real sigue las indicaciones del servicio de emergencias y del personal designado; en España el teléfono general es el 112.

En clase se puede simular la comunicación: lugar exacto, situación observada, personas afectadas, riesgos conocidos y forma de contacto. No se llama al servicio real para un ejercicio. No se improvisan maniobras sanitarias ni se enseñan técnicas invasivas mediante una guía de informática. La formación práctica correspondiente debe estar dirigida por personal competente.

Tras un incidente o un «casi accidente», registra hechos y preserva la información útil. No ocultes el suceso porque no haya lesión. La ausencia de consecuencias en una ocasión no demuestra que el procedimiento fuese correcto.

## 5. Fuentes de la relación laboral

Para interpretar condiciones de trabajo identifica el régimen de la relación y las normas que le resultan aplicables. No todas las personas que trabajan en un centro tienen el mismo convenio o vínculo. Una actividad formativa en empresa, un contrato de trabajo y una prestación de servicios autónoma tienen encuadres distintos.

La búsqueda documental comienza por el contrato y la descripción real de la actividad. Localiza el convenio aplicable por ámbitos funcional, territorial, personal y temporal; comprueba su publicación oficial y las revisiones posteriores. Después contrasta la norma de referencia, las condiciones pactadas y las dudas con el profesional adecuado. El [Estatuto de los Trabajadores](https://www.boe.es/eli/es/rdlg/2015/10/23/2/con) es una referencia básica para la relación laboral común, pero no resuelve por sí solo cada caso.

Un método de lectura evita errores frecuentes:

| Pregunta | Dato que debes buscar |
| --- | --- |
| ¿Quién contrata y qué trabajo se realiza? | Identificación, centro, funciones y grupo profesional |
| ¿Con qué modalidad? | Modalidad, causa cuando proceda y documentación asociada |
| ¿Durante cuánto tiempo? | Inicio, duración o condición de finalización |
| ¿Con qué jornada? | Distribución, calendario y registro correspondiente |
| ¿Qué retribución corresponde? | Conceptos, periodicidad y referencia al convenio |
| ¿Qué condiciones adicionales existen? | Prueba, movilidad, confidencialidad y pactos |

No completes automáticamente una casilla desconocida. Anota «pendiente de comprobar» y el documento que falta. Una condición contractual no se acepta como válida solo por aparecer firmada: su encaje debe comprobarse en el marco aplicable.

## 6. Contratos, derechos y protección social

Para comenzar, distingue contrato indefinido, temporal y modalidades formativas. La denominación no es una explicación suficiente: importa la causa y el objeto reales. Los requisitos, límites, incentivos y formularios pueden cambiar; trabaja con los [modelos y explicaciones del SEPE](https://sepe.es/HomeSepe/empresas/Contratos-de-trabajo/modelos-contrato.html) y guarda fecha de consulta. No reutilices una plantilla antigua de «contrato en prácticas» sin comprobar la regulación actual del contrato formativo para la obtención de práctica profesional.

Estudia los derechos y deberes a través de situaciones: confidencialidad en un soporte remoto, respeto en una comunicación de incidencia, igualdad en selección y necesidad de instrucciones claras. Documenta una orden dudosa y usa el canal interno adecuado; no publiques datos del cliente para justificar una disputa. Aprende también dónde consultar representación, orientación y procedimientos administrativos.

La Seguridad Social tiene sus propias bases, tipos y reglas de cálculo. El hecho de recibir un importe neto no permite deducir todas las cotizaciones ni las prestaciones futuras. Consulta la [explicación oficial de bases, tipos y cuotas](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/10721/10957/583?changeLanguage=es); en casos reales intervienen conceptos y topes que un ejercicio reducido puede omitir.

## 7. Anatomía de una nómina

El recibo permite separar identificación y periodo, devengos, bases de cálculo, deducciones, líquido a percibir y aportaciones empresariales informadas. La relación matemática de partida es:

```text
total devengado − total deducciones = líquido a percibir
coste empresarial simplificado = devengado + aportaciones empresariales
```

La segunda igualdad es una aproximación de gestión: otros costes de la relación laboral pueden existir. Las cotizaciones de la empresa no se descuentan íntegramente del salario del trabajador. La retención de IRPF es un pago a cuenta y no equivale a la cuota final del impuesto.

Las bases de cotización y de retención no son necesariamente iguales al devengado. Puede haber conceptos con tratamiento diferente, pagas extraordinarias no prorrateadas y reglas específicas. En el caso de ejercicio se explicitan las bases precisamente para no presentar una simplificación como una liquidación válida.

En la hoja de cálculo guarda los tipos como parámetros con fecha y fuente. Usa referencias absolutas cuando varias filas apliquen el mismo parámetro; redondea con una política explícita y conserva suficiente precisión intermedia. Una fórmula correcta con un tipo de otro año sigue produciendo un resultado inaplicable.

## 8. Aprender a aprender con evidencias

El autoconocimiento profesional requiere comparar expectativa y desempeño. Después de una práctica escribe qué pudiste realizar sin ayuda, qué parte requirió instrucciones y qué fallo no supiste diagnosticar. «Me falta Linux» es demasiado amplio; «no distingo propietario, grupo y máscara ACL en una carpeta compartida» permite diseñar una actividad concreta.

Formula un objetivo con acción, plazo y criterio: «en tres semanas, restaurar una carpeta desde una copia en una VM nueva, documentando integridad y permisos». Divide el objetivo en sesiones de preparación, ejecución y explicación. Mantén una fuente principal, registra versiones y evita cambiar de tutorial cuando aparece el primer error: analiza primero la diferencia entre el entorno del tutorial y el tuyo.

Un entorno personal de aprendizaje puede combinar documentación oficial, cuaderno de errores, repositorio de prácticas y revisión entre compañeros. Valida la información generada por asistentes automáticos mediante documentación y pruebas en laboratorio. No pegues datos de empresa o secretos en herramientas externas. La autonomía consiste también en saber pedir ayuda con un contexto reproducible.
