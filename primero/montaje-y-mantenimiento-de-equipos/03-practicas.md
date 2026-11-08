# 03 · Prácticas de taller

[Volver al módulo](README.md) · [Consultar diagnóstico y evaluación](04-diagnostico-y-evaluacion.md)

Las duraciones son orientativas. No sustituyas una pieza real ni alteres firmware sin autorización del responsable del puesto. Una VM permite la parte de inventario; las verificaciones físicas requieren hardware real.

## Práctica 1 · Inventario y propuesta de ampliación

**Nivel inicial · 2–3 horas.** El escenario es un puesto de oficina ficticio que abre documentos, participa en videollamadas y mantiene numerosas pestañas. Se describe una ralentización al cambiar de aplicación. Dispones de un equipo de laboratorio o de una VM con sus limitaciones indicadas.

### Objetivos

Identificar componentes, distinguir capacidad nominal y configuración efectiva, relacionar un síntoma con métricas y proponer una ampliación compatible sin modificar el equipo.

### Procedimiento

1. Redacta tres preguntas para la persona usuaria: qué tarea se ralentiza, desde cuándo y si ocurre también tras reiniciar. Anota respuestas ficticias coherentes.
2. Obtén CPU, RAM, almacenamiento, sistema, firmware y periféricos mediante las consultas de la guía. Anonimiza identificadores antes de guardar evidencias.
3. Observa el puesto en reposo y con una carga de oficina reproducible. Registra RAM disponible, uso de CPU, actividad de disco y duración de una tarea definida. No captures contenido personal.
4. Consulta el manual del modelo o placa. Localiza máximo de memoria, ranuras ocupadas, generación admitida y almacenamiento compatible. Si estás en VM, explica qué datos físicos faltan y qué debe consultar el administrador del anfitrión.
5. Formula dos hipótesis; por ejemplo, presión de memoria frente a almacenamiento lento. Para cada una indica qué observación la apoyaría y cuál la debilitaría.
6. Propón una intervención, una alternativa y mantener el equipo sin cambio. Justifica coste, beneficio, riesgos y prueba de aceptación. Si usas precios, indica fecha y fuente.

### Resultado esperado

La conclusión debe ser condicional a la evidencia. Si CPU está poco ocupada y existe paginación sostenida junto con demoras, una ampliación de memoria puede estar justificada. Si el síntoma aparece solo en una aplicación que espera una respuesta remota, comprar RAM no está demostrado.

### Entregables y criterios

Entrega inventario de una página, matriz de compatibilidad, tabla de mediciones y recomendación de 300–500 palabras. Se valora identificación correcta (25 %), trazabilidad de la evidencia (30 %), compatibilidad de la propuesta (30 %) y claridad de la entrega (15 %). Una propuesta incompatible debe corregirse aunque el resto del informe esté bien presentado.

## Práctica 2 · Montaje y aceptación de un equipo

**Nivel intermedio · 4–6 horas.** Monta un equipo de piezas del centro o desmonta y vuelve a montar un equipo preparado para formación. No se utiliza el equipo personal del alumno ni un dispositivo con datos sin copia.

### Preparación

El responsable facilita manuales, piezas comprobadas, herramienta, control ESD y un almacenamiento vacío identificado. El alumnado entrega una lista previa de compatibilidad y un esquema de conexiones. Para practicar exclusivamente en VM, sustituye el montaje por configuración documentada de hardware virtual; declara que no se han demostrado competencias manuales.

### Procedimiento

1. Fotografía o dibuja el estado inicial sin identificadores sensibles. Comprueba alimentación retirada y registra el número de piezas y tornillos.
2. Monta CPU, disipación, RAM, almacenamiento, placa, fuente y periféricos siguiendo el procedimiento técnico y los manuales.
3. Antes de conectar corriente, otro compañero inspecciona separadores, cableado y refrigeración. Marca cada control; la firma no transfiere la responsabilidad del montaje.
4. Realiza primer arranque y registra lo detectado por UEFI. Compara memoria instalada y reconocida. No actives perfiles de rendimiento todavía.
5. Arranca un entorno de diagnóstico autorizado. Obtén inventario, consulta registros y ejecuta las comprobaciones de aceptación acordadas.
6. Instala un SO únicamente sobre el disco vacío identificado o reutiliza una imagen de laboratorio aprobada. Anota qué queda pendiente si no hay licencia o medios adecuados.
7. Realiza carga representativa, reinicio, apagado, arranque en frío y prueba de puertos. Registra límites de temperatura del modelo y valores observados.
8. Entrega el equipo con cables ordenados, inventario actualizado y piezas sobrantes justificadas.

### Resultados y recuperación

Se espera detección consistente del hardware y ausencia de fallos reproducibles en las pruebas definidas. Si no hay POST, retira alimentación, revisa conexiones y vuelve a la configuración mínima. No conectes RAM o cables internos en caliente. Si aparece un error de memoria, documenta ranura y módulo antes de permutarlos; cambiar simultáneamente varias piezas impide identificar la causa.

### Entregables y criterios

Entrega diagrama, lista de control, fotografías del montaje, ficha de firmware y matriz de aceptación con estados `correcto`, `fallo` o `no comprobado`. Seguridad y compatibilidad son requisitos de realización. Una vez cumplidos, la rúbrica didáctica reparte montaje (30 %), verificación (35 %), documentación (20 %) y explicación de entrega (15 %). No marques como realizada una prueba que el material del aula no permita ejecutar.

## Práctica 3 · Incidencia reproducible y mantenimiento

**Nivel avanzado · 3–5 horas.** El docente prepara una avería reversible, como un cable de datos desconectado con el equipo apagado, una cola de impresión detenida o un módulo de RAM mal ubicado respecto al plan de canales. No se provoca sobretemperatura, cortocircuito, daño físico o pérdida de datos.

### Método de diagnóstico

1. Abre una incidencia con síntoma, impacto, alcance y cambios recientes. Reproduce una vez y describe exactamente qué ocurre.
2. Separa las capas: ¿hay alimentación?, ¿hay POST?, ¿aparece el dispositivo en firmware?, ¿lo ve el SO?, ¿falla solo una aplicación?
3. Escribe al menos tres hipótesis y ordénalas por probabilidad, facilidad de prueba y coste de equivocarse.
4. Diseña una prueba por hipótesis. Una prueba útil puede descartar una causa: ver el disco en firmware pero no su partición en el SO dirige la investigación hacia capas lógicas o controladores.
5. Cambia una sola variable, registra resultado y decide el siguiente paso. No sustituyas componentes por intuición sin una observación justificativa.
6. Aplica la corrección aprobada y repite exactamente la prueba que reproducía el fallo. Añade dos pruebas de regresión relacionadas.
7. Propón una medida preventiva que ataque la causa: identificación de cables, actualización de inventario, filtro de polvo o control periódico de capacidad, según el caso.

### Rama de impresora

Primero imprime la página interna desde el dispositivo, si el modelo lo permite. Si falla, revisa consumibles y mecanismo siguiendo el manual. Si funciona, consulta estado de conexión, dirección configurada, cola y controlador. No publiques páginas con datos personales. Si reiniciar una cola recupera temporalmente el servicio pero el fallo reaparece con un documento específico, conserva un documento de prueba inocuo y analiza ese desencadenante.

### Rama de almacenamiento

Identifica unidad y copia disponible antes de consultar SMART. Compara errores y registros con el síntoma. Si aparecen fallos de lectura sobre datos importantes, documenta la necesidad de preservar o escalar; no conviertas el ejercicio en una batería de pruebas que degrade el medio. La práctica se considera bien resuelta si el alumno decide justificadamente no continuar una operación inadecuada.

### Entregables y criterios

Entrega cronología `hora → hipótesis → prueba → resultado → decisión`, informe de causa o de incertidumbre y plan preventivo trimestral. Se valora aislamiento de la causa (35 %), calidad de pruebas (30 %), recuperación verificada (20 %) y comunicación (15 %). Identificar explícitamente que no se ha podido confirmar una causa es más correcto que inventar una explicación.

## Plantilla de acta de aceptación

| Prueba | Condición inicial | Resultado esperado | Resultado observado | Evidencia | Decisión |
| --- | --- | --- | --- | --- | --- |
| Arranque en frío | Equipo apagado | POST y SO disponibles | Completar | Foto o registro anonimizado | Aceptar/revisar |
| Memoria | Configuración base | Capacidad correcta; sin errores en prueba definida | Completar | Registro de herramienta | Aceptar/revisar |
| Almacenamiento | Unidad identificada | Lectura de datos de prueba y registros sin incidencia investigable | Completar | Informe | Aceptar/revisar |
| Impresión | Consumibles presentes | Página interna y del SO correctas | Completar | Página ficticia | Aceptar/revisar |

Un acta describe el alcance realmente comprobado. No promete que el equipo nunca fallará ni certifica propiedades que la prueba no mide.
