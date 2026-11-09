# 06 · Diagnóstico por subsistemas y casos de taller

[Índice](README.md) · [Método general](../../docs/metodo-de-diagnostico.md)

## 1. Separar ausencia de energía, POST y arranque

Un equipo que «no arranca» puede no recibir energía, detenerse durante la inicialización de hardware, no encontrar un cargador o iniciar un SO que falla después. Cada situación tiene observaciones diferentes. Antes de abrir la caja, registra qué ocurre al pulsar el botón: indicadores, ventilación, imagen, mensajes, sonidos y secuencia temporal. No conviertas la ausencia de pitidos en prueba de placa averiada: puede no existir altavoz o el modelo usar otro mecanismo.

La fuente de información prioritaria es el manual de servicio del equipo o placa exactos. Un LED de memoria o una secuencia de códigos orienta una etapa, pero no identifica siempre la pieza culpable. CPU, zócalo, alimentación o firmware pueden impedir entrenar la memoria. El diagnóstico requiere pruebas que separen esas causas, no una sustitución inmediata del componente nombrado por el indicador.

Define el límite de intervención. Un puesto autorizado de SMR permite inspección, sustitución modular y pruebas previstas por el fabricante; no implica abrir una fuente, reparar baterías o intervenir circuitos energizados. Un olor anómalo, líquido o batería deformada detiene el procedimiento y activa el protocolo de retirada y supervisión.

## 2. Orden de pruebas y coste de la información

Empieza por pruebas de bajo riesgo y alto poder discriminante. Comprobar una toma mediante un procedimiento autorizado o un cable conocido puede separar el entorno del equipo. Fotografiar conexiones antes de desmontar conserva el estado. Recolocar todos los módulos a la vez puede recuperar funcionamiento, pero impide saber qué conexión fallaba y complica la prevención.

La «configuración mínima» no es una receta universal de quitar piezas. Debe respetar los requisitos de la plataforma: algunos procesadores no ofrecen gráficos integrados, ciertas placas necesitan conectores adicionales y los equipos de fabricante pueden incluir sensores o interbloqueos. Determina la configuración admitida con el manual y registra cada elemento retirado. El hecho de que una pieza no sea necesaria para una prueba no permite desconectarla en caliente.

Una pieza conocida buena ayuda si es compatible y su instalación no genera otro problema. Una fuente con potencia nominal similar puede tener conectores, pinout modular o límites diferentes. Nunca intercambies cables modulares entre modelos suponiendo compatibilidad por su forma. El diagnóstico debe reducir incertidumbre, no introducir riesgos ocultos.

## 3. Matriz de síntomas e hipótesis

| Síntoma observado | Hipótesis alternativas | Prueba que aporta información | Conclusión que todavía no puedes afirmar |
| --- | --- | --- | --- |
| Ninguna señal al pulsar | Alimentación externa, interruptor, cableado del botón, fuente, placa | Secuencia externa y conexiones según manual | «La placa está muerta» |
| Ventiladores activos sin imagen | Entrada/pantalla, salida incorrecta, POST, RAM, GPU | Pantalla/cable conocidos y salida soportada | «La CPU funciona porque gira el ventilador» |
| Reinicio bajo carga | Temperatura, alimentación, RAM, controlador | Correlación temporal y carga controlada | «Hace falta más potencia» |
| Arranque intermitente | Contacto, entrenamiento, batería/firmware, periférico | Línea base y cambio único con varios ciclos | «Ya se arregló porque arrancó una vez» |
| Disco desaparece | Cable, puerto, alimentación, dispositivo, firmware | Detección en firmware y consulta de logs | «El sistema de archivos está corrupto» |
| Errores tras ampliación RAM | Compatibilidad, ranura, perfil, módulo, controlador | Configuración admitida y pruebas aisladas | «El módulo nuevo es defectuoso» |
| USB se desconecta | Puerto/cable, potencia, controlador, dispositivo | Otro puerto adecuado y registro de eventos | «Todos los USB son equivalentes» |

La matriz organiza hipótesis; no sustituye instrucciones del fabricante ni confirma fallos por coincidencia. Cada prueba se anota con estado inicial, intervención, observación y siguiente decisión.

## 4. Caso A: ventiladores, pero ninguna imagen

Primero separa imagen y ejecución. Comprueba encendido de pantalla, selección de entrada y cable. Si hay dos adaptadores gráficos, identifica qué salida admite la configuración actual. No conectes el monitor a una salida de placa cuyo procesador carece de gráficos integrados y concluyas que falla el equipo.

Después observa si el sistema llega a un punto verificable: indicador de POST documentado, acceso remoto previamente configurado o mensaje de firmware. No utilices «enciende el teclado» como prueba concluyente de carga del SO. Si existe un código de error, registra el texto y la secuencia exactos; búsquedas de un código de otra familia de placas pueden conducir a un procedimiento equivocado.

Si procede examinar memoria o GPU, apaga, desconecta y aplica medidas ESD. Conserva fotos y coloca los módulos en la posición recomendada. Comprueba que cierres y alimentación de GPU queden correctos. Tras cada cambio realiza un ciclo documentado y espera el tiempo de inicialización razonable del modelo, especialmente después de modificar memoria; interrumpir repetidamente puede impedir completar el entrenamiento.

Acepta la recuperación cuando haya imagen correcta, identificación del hardware, arranque del SO y varias pruebas básicas de estabilidad. La solución debe indicar causa confirmada o hipótesis más probable. Si sólo recolocar un módulo recuperó el equipo, informa de esa evidencia sin inventar que el chip estaba averiado.

## 5. Caso B: reinicio durante tareas exigentes

Recoge hora y tipo de carga: CPU, GPU, almacenamiento o combinación. Distingue apagado súbito, reinicio, pantalla de error y cierre de aplicación. Consulta registros del SO posteriores al evento, pero interpreta sus límites. Un evento que indica apagado inesperado confirma que no hubo cierre limpio; no identifica automáticamente la fuente como causa.

Inspecciona primero condiciones evidentes con el equipo apagado: obstrucción, disipador, ventiladores y conectores. Después observa una carga representativa controlada dentro de los límites del fabricante. No provoques repetidamente fallos térmicos ni ejecutes pruebas extremas para «estar seguro». Si hay signos de riesgo físico, se detiene la prueba.

Relaciona temperatura, frecuencia y momento del fallo. Un descenso sostenido de frecuencia puede ser una respuesta de protección, mientras un reinicio sin rastro puede requerir examinar alimentación y conexiones. Las utilidades de sensores no siempre representan todos los puntos calientes o transitorios. Un dato ausente o incoherente exige contrastar con herramientas y firmware del fabricante.

La prueba con fuente conocida compatible puede aportar evidencia en un taller autorizado, pero no sustituye una selección correcta ni permite abrir la fuente retirada. Si el fallo sólo ocurre con un controlador o después de una actualización, conserva la rama de software y ensaya una reversión soportada en copia de laboratorio.

## 6. Caso C: errores de memoria después de ampliar

Registra referencia completa de los módulos, capacidad, organización, voltaje y posiciones. Consulta límites de CPU y placa y la versión de firmware necesaria. Mezclar kits no garantiza que la combinación funcione con el perfil anunciado de cada kit por separado. La lista de compatibilidad del fabricante tampoco pretende demostrar que cualquier combinación no incluida sea imposible.

Vuelve a una configuración soportada y conocida, con los cambios anotados. Si los errores aparecen con un módulo en todas las ranuras admitidas, la hipótesis del módulo gana fuerza; si aparecen con distintos módulos sólo en una ranura o canal, investiga placa, zócalo, conexión o controlador de memoria. No intercambies piezas sin proteger los datos: errores de memoria pueden afectar a información procesada antes de que el SO detecte el problema.

Una prueba de memoria sin errores reduce algunas hipótesis, pero no certifica todos los patrones, temperaturas o condiciones futuras. Documenta versión de herramienta, duración, configuración y resultado. Un error reproducible es una evidencia fuerte de inestabilidad del conjunto; el componente exacto se confirma mediante aislamiento y procedimientos del fabricante.

## 7. Caso D: disco visible en firmware, pero no en el explorador

La detección de dispositivo y el montaje de un volumen son capas distintas. Empieza por identificar disco, particiones y sistema de archivos mediante consultas. En Linux utiliza `lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS` y `findmnt`; en Windows, Administración de discos o `Get-Disk` y `Get-Volume`. No inicialices ni formatees una unidad con datos sólo para hacerla aparecer.

Un disco sin letra en Windows puede contener una partición que no corresponde montar como datos. Un volumen Linux puede no tener un punto de montaje activo, o usar un formato no admitido por el otro sistema. Si el volumen esperado aparece RAW o hay errores de lectura, detén cambios y prioriza copia o recuperación autorizada; no ejecutes reparaciones automáticamente sobre la única copia.

Si el disco desaparece también en firmware, vuelve a cableado, puerto, alimentación y salud del dispositivo. Un error lógico no explica normalmente que el controlador deje de enumerar físicamente el dispositivo. Conserva los registros antes de cambiar puertos para poder relacionar el problema con su trayecto.

## 8. Práctica ampliada: mesa de diagnóstico

Trabaja con un equipo de entrenamiento y tres incidencias reversibles preparadas por el docente: entrada de pantalla equivocada, dispositivo no esencial desconectado o configuración de arranque que apunta a otro medio. No se preparan cortocircuitos, daños físicos ni cambios de tensión. Si se usa una VM, indica qué fallos sólo representan una capa virtual.

Cada estudiante recibe únicamente el síntoma y debe elaborar una tabla de al menos cuatro hipótesis, elegir dos pruebas discriminantes y justificar su orden. El evaluador registra si la intervención introduce cambios innecesarios. La resolución debe terminar con el estado esperado, inventario actualizado y explicación a una persona usuaria.

Entrega fotografías o diagramas sanitizados, registro de cambios, resultados y una causa técnicamente proporcionada. Rúbrica propia: hipótesis y priorización 25 %, seguridad/procedimiento 20 %, pruebas 25 %, comprobación de recuperación 20 % y comunicación 10 %. No se premia cambiar más piezas ni acertar por casualidad sin evidencia.

## 9. Preguntas de contraste

**¿Una prueba buena elimina todas las causas de hardware?** No. Su alcance depende de carga, duración, sensores y combinación utilizada. Debes expresar qué hipótesis debilita y cuáles siguen abiertas.

**¿Una actualización de firmware es el primer paso ante cualquier fallo?** No. Es un cambio con requisitos de modelo, versión, alimentación y recuperación. Primero identifica el problema y contrasta si la actualización lo aborda; sigue el procedimiento del fabricante.

**¿Borrar la configuración del firmware conserva siempre todos los datos de acceso?** No debe suponerse. Puede cambiar modo de almacenamiento, arranque, TPM o ajustes relacionados. Registra configuración y claves de recuperación antes de cualquier operación autorizada; no se incluye una secuencia genérica para ejecutarla sobre equipos reales.

**¿Sustituir una pieza y ver que funciona confirma causalidad?** Aporta evidencia, pero puede haber cambiado conexión, configuración o estado térmico. Una conclusión firme requiere controlar esas variables y, cuando sea viable, repetir el comportamiento de forma segura.

## Referencias primarias

- [UEFI Forum](https://uefi.org/specifications): fases y servicios de la plataforma; el procedimiento concreto pertenece al fabricante del equipo.
- [Microsoft: resolución de errores de detención](https://learn.microsoft.com/troubleshoot/windows-client/performance/stop-error-or-blue-screen-error-troubleshooting): clasificación y recogida de información del fallo.
- [Linux: mensajes y registros del kernel](https://manpages.debian.org/trixie/util-linux/dmesg.1.en.html): consulta y límites de acceso.
- [Debian: lsblk](https://manpages.debian.org/trixie/util-linux/lsblk.8.en.html): identificación de capas del almacenamiento.
- [Microsoft: Get-Disk](https://learn.microsoft.com/powershell/module/storage/get-disk): consulta de objetos de disco sin inicialización ni formateo.
