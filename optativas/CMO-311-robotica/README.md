# CMO-311 · Informática aplicada a sistemas electrónicos (Robótica)

[Catálogo de optativas](../README.md) · [Índice general](../../README.md)

## Aplicabilidad y forma de estudio

La tabla del catálogo fija 50 horas para este módulo específico de Informática y Comunicaciones. Su ubicación en primero se deduce del encaje con las optativas de SMR (50/90 horas); no se presenta como una columna de curso expresamente asignada a IFC en el catálogo. Deben confirmarse la oferta y las condiciones del centro.

El currículo de referencia es la [Orden 3536/2025](https://www.bocm.es/boletin/CM_Orden_BOCM/2025/08/27/BOCM-20250827-5.PDF), Anexo II, CMO-311; BOCM página 185 y siguientes; PDF páginas 168–170. La relación aplicable se contrasta con la [Orden 3822/2026](https://www.bocm.es/boletin/CM_Orden_BOCM/2026/09/25/BOCM-20260925-20.PDF). El catálogo permite una oferta; no demuestra que un centro imparta todas estas materias ni que un alumno deba cursarlas simultáneamente.

Los enunciados de RA y los CE de las tablas se transcriben del referente normativo. Las explicaciones, retos, soluciones y condiciones de aceptación son propuestas didácticas propias. La evidencia esperada se diferencia de lo observado: completa resultados reales en una copia de la plantilla de seguimiento.

## Preparación

Revisa el [laboratorio común](../../docs/laboratorio.md) y trabaja con datos sintéticos y un entorno identificado. Antes de modificar, registra versión, estado inicial y recuperación. Las tareas que necesitan hardware, motor de juego o plataforma administrada deben ejecutarse en esos medios para aportar evidencia completa; la preparación escrita conserva su valor y se marca como pendiente de esa ejecución.

## Ruta por resultados de aprendizaje

<a id="ra1"></a>
## RA1 · Interpretar una señal antes de medirla

**Enunciado oficial:** Describe los fundamentos básicos de las señales eléctricas.

Tensión, corriente, resistencia, potencia y energía no son intercambiables. Una señal periódica tiene periodo y frecuencia relacionados por f=1/T; una secuencia muestreada añade frecuencia de muestreo y resolución. El valor de una lectura depende del instrumento, rango y referencia.

### Actividad CMO-311-RA1-A1

1. Dibuja una señal continua y una periódica de 50 Hz e indica unidades y amplitud.
2. Calcula su periodo y compara una adquisición de 100 y de 1.000 muestras por segundo.
3. Para un ADC ideal de 10 bits y 5 V de referencia calcula el escalón de cuantificación.
4. Describe qué información del sensor se perdería por saturación o muestreo insuficiente.

**Solución razonada y errores que debes interpretar:** A 50 Hz el periodo es 20 ms. El escalón ideal 5/1024 es aproximadamente 4,88 mV. Tomar exactamente dos muestras por periodo es un límite teórico insuficiente como criterio práctico de calidad; se necesita margen, filtrado y conocer el contenido de frecuencia de la señal.

**Entregable:** Ficha de magnitudes, gráfica y cálculo de muestreo.

**Aceptación del reto:** Todas las cifras tienen unidad y se distingue señal continua, discreta, rango y resolución.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha descrito el significado de corriente, tensión, resistencia, potencia y energía. | Ficha de magnitudes, gráfica y cálculo de muestreo; apartado a con datos, explicación o salida referida expresamente a ese criterio. Todas las cifras tienen unidad y se distingue señal continua, discreta, rango y resolución. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han identificado señales continuas y alternas. | Ficha de magnitudes, gráfica y cálculo de muestreo; apartado b con datos, explicación o salida referida expresamente a ese criterio. Todas las cifras tienen unidad y se distingue señal continua, discreta, rango y resolución. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han identificado señales periódicas y aleatorias. | Ficha de magnitudes, gráfica y cálculo de muestreo; apartado c con datos, explicación o salida referida expresamente a ese criterio. Todas las cifras tienen unidad y se distingue señal continua, discreta, rango y resolución. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han descrito la amplitud, frecuencia y el periodo de una señal periódica. | Ficha de magnitudes, gráfica y cálculo de muestreo; apartado d con datos, explicación o salida referida expresamente a ese criterio. Todas las cifras tienen unidad y se distingue señal continua, discreta, rango y resolución. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se han identificado señales en tiempo continuo y discreto. | Ficha de magnitudes, gráfica y cálculo de muestreo; apartado e con datos, explicación o salida referida expresamente a ese criterio. Todas las cifras tienen unidad y se distingue señal continua, discreta, rango y resolución. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| f | Se ha descrito la conversión analógico-digital (muestreo, cuantificación y codificación) examinando los conceptos básicos (frecuencia de muestreo y resolución). | Ficha de magnitudes, gráfica y cálculo de muestreo; apartado f con datos, explicación o salida referida expresamente a ese criterio. Todas las cifras tienen unidad y se distingue señal continua, discreta, rango y resolución. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra2"></a>
## RA2 · Diseñar y verificar un circuito de baja tensión

**Enunciado oficial:** Analiza, diseña, simula y mide circuitos electrónicos en continua.

La simulación permite comparar hipótesis con un modelo; el montaje físico añade tolerancias, conexiones e instrumentación. Limita esta actividad a baja tensión de laboratorio y supervisión. Nunca se emplea la red eléctrica ni se abre una fuente de alimentación.

### Actividad CMO-311-RA2-A1

1. Diseña un circuito LED con fuente de 5 V, caída supuesta de 2 V y resistencia de 220 ohmios.
2. Calcula corriente y potencia en la resistencia; contrasta con un simulador.
3. Con el circuito desenergizado revisa conexiones y rango del instrumento; monta bajo supervisión.
4. Mide según el procedimiento del laboratorio y explica circuito abierto y cortocircuito sin provocarlos en la fuente.

**Solución razonada y errores que debes interpretar:** El modelo da I=(5−2)/220≈13,6 mA y P=I²R≈0,041 W. Una resistencia de 0,25 W ofrece margen en este supuesto, pero se comprueban LED y fuente concretos. Una captura del simulador no acredita destreza de montaje o medición física.

**Entregable:** Esquema, cálculo, simulación y hoja de medición supervisada.

**Aceptación del reto:** El montaje respeta límites del componente y separa cálculo, simulación y medición real; lo no ejecutado queda pendiente.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han identificado los distintos componentes discretos que forman parte de un circuito electrónico. | Esquema, cálculo, simulación y hoja de medición supervisada; apartado a con datos, explicación o salida referida expresamente a ese criterio. El montaje respeta límites del componente y separa cálculo, simulación y medición real; lo no ejecutado queda pendiente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han descrito las características básicas y principios de los distintos componentes discretos. | Esquema, cálculo, simulación y hoja de medición supervisada; apartado b con datos, explicación o salida referida expresamente a ese criterio. El montaje respeta límites del componente y separa cálculo, simulación y medición real; lo no ejecutado queda pendiente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han analizado y explicado circuitos electrónicos con componentes discretos. | Esquema, cálculo, simulación y hoja de medición supervisada; apartado c con datos, explicación o salida referida expresamente a ese criterio. El montaje respeta límites del componente y separa cálculo, simulación y medición real; lo no ejecutado queda pendiente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han diseñado circuitos electrónicos con componentes discretos. | Esquema, cálculo, simulación y hoja de medición supervisada; apartado d con datos, explicación o salida referida expresamente a ese criterio. El montaje respeta límites del componente y separa cálculo, simulación y medición real; lo no ejecutado queda pendiente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se han empleado programas de simulación para comprobar cálculos y verificar el diseño de los circuitos electrónicos. | Esquema, cálculo, simulación y hoja de medición supervisada; apartado e con datos, explicación o salida referida expresamente a ese criterio. El montaje respeta límites del componente y separa cálculo, simulación y medición real; lo no ejecutado queda pendiente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| f | Se han realizado montajes y pruebas de funcionamiento de circuitos con componentes discretos con las herramientas e instrumentación adecuada. | Acta de observación física supervisada y datos de medida o funcionamiento; Esquema, cálculo, simulación y hoja de medición supervisada. La operación física del criterio es observada con seguridad y se relaciona con el diseño; una captura del simulador no la sustituye. |
| g | Se han identificado circuitos abiertos y cortocircuitos. | Esquema, cálculo, simulación y hoja de medición supervisada; apartado g con datos, explicación o salida referida expresamente a ese criterio. El montaje respeta límites del componente y separa cálculo, simulación y medición real; lo no ejecutado queda pendiente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra3"></a>
## RA3 · Programar un controlador con estados

**Enunciado oficial:** Utiliza con destreza un entorno de programación de sistemas electrónicos digitales.

Un controlador lee entradas, actualiza estado y actúa sobre salidas. Bloquear el programa con pausas largas puede impedir atender un botón o sensor. Define frecuencia de lectura, umbral y comportamiento de error antes de conectar una carga.

### Actividad CMO-311-RA3-A1

1. En el entorno educativo elegido crea constantes, variables y una lista de lecturas sintéticas.
2. Programa estados reposo/alerta y un cambio de estado al superar el umbral.
3. Añade un botón de reconocimiento y una condición de lectura inválida.
4. Traza el programa y comprueba ramas, bucles y reinicio sin conectar actuadores peligrosos.

**Solución razonada y errores que debes interpretar:** Para evitar oscilaciones cerca del umbral puede usarse histéresis: entrar en alerta por encima de 30 y volver a reposo por debajo de 28, con unidades declaradas. El fallo de sensor requiere un estado definido; no debe tratarse silenciosamente como una lectura de cero.

**Entregable:** Código del controlador, diagrama de estados y traza de entradas/salidas.

**Aceptación del reto:** Cada transición prevista se reproduce y una entrada inválida lleva al estado de seguridad definido.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha utilizado con precisión el entorno de programación de un sistema electrónico. | Código del controlador, diagrama de estados y traza de entradas/salidas; apartado a con datos, explicación o salida referida expresamente a ese criterio. Cada transición prevista se reproduce y una entrada inválida lleva al estado de seguridad definido. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han desarrollado programas para controlar el funcionamiento de un sistema electrónico. | Código del controlador, diagrama de estados y traza de entradas/salidas; apartado b con datos, explicación o salida referida expresamente a ese criterio. Cada transición prevista se reproduce y una entrada inválida lleva al estado de seguridad definido. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han usado de manera adecuada comandos de control de ejecución (condicionales y bucles). | Código del controlador, diagrama de estados y traza de entradas/salidas; apartado c con datos, explicación o salida referida expresamente a ese criterio. Cada transición prevista se reproduce y una entrada inválida lleva al estado de seguridad definido. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han usado de manera adecuada constantes, variables y listas. | Código del controlador, diagrama de estados y traza de entradas/salidas; apartado d con datos, explicación o salida referida expresamente a ese criterio. Cada transición prevista se reproduce y una entrada inválida lleva al estado de seguridad definido. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se ha analizado el funcionamiento de un programa de un sistema electrónico. | Código del controlador, diagrama de estados y traza de entradas/salidas; apartado e con datos, explicación o salida referida expresamente a ese criterio. Cada transición prevista se reproduce y una entrada inválida lleva al estado de seguridad definido. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra4"></a>
## RA4 · Diseñar una carcasa que se pueda fabricar

**Enunciado oficial:** Utiliza software de diseño 3D e impresión 3D para la creación de objetos y prototipos.

El modelo 3D necesita unidades, tolerancias, acceso a conectores y ventilación. La selección de material depende de temperatura, esfuerzo y proceso; una apariencia correcta en pantalla no garantiza ajuste físico o estabilidad de la pieza.

### Actividad CMO-311-RA4-A1

1. Diseña una caja para la placa didáctica con dimensiones documentadas y acceso a USB.
2. Compara dos materiales y selecciona uno para las condiciones del prototipo.
3. Exporta el formato admitido por el laminador y configura orientación, capas, relleno y soportes.
4. Imprime una probeta de ajuste antes de la pieza completa y registra la revisión del diseño.

**Solución razonada y errores que debes interpretar:** Un hueco del tamaño nominal exacto del conector puede no ajustar por tolerancias. Ensayar una probeta reduce material y tiempo. La impresión exige seguir el procedimiento del centro para superficies calientes, partes móviles y ventilación; el laminado sin impresión queda como evidencia parcial.

**Entregable:** Modelo editable, archivo de fabricación y ficha de parámetros/ajuste.

**Aceptación del reto:** El diseño mantiene unidades, permite conectar y fijar la placa y justifica material y parámetros.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha descrito el funcionamiento de un sistema de impresión 3D. | Modelo editable, archivo de fabricación y ficha de parámetros/ajuste; apartado a con datos, explicación o salida referida expresamente a ese criterio. El diseño mantiene unidades, permite conectar y fijar la placa y justifica material y parámetros. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han enumerado los distintos tipos de materiales usados en impresión 3D, así como las características de cada uno de ellos. | Modelo editable, archivo de fabricación y ficha de parámetros/ajuste; apartado b con datos, explicación o salida referida expresamente a ese criterio. El diseño mantiene unidades, permite conectar y fijar la placa y justifica material y parámetros. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se ha seleccionado el material adecuado de impresión 3D. | Modelo editable, archivo de fabricación y ficha de parámetros/ajuste; apartado c con datos, explicación o salida referida expresamente a ese criterio. El diseño mantiene unidades, permite conectar y fijar la placa y justifica material y parámetros. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se ha usado software de diseño adecuado para la creación de objetos y prototipos 3D. | Modelo editable, archivo de fabricación y ficha de parámetros/ajuste; apartado d con datos, explicación o salida referida expresamente a ese criterio. El diseño mantiene unidades, permite conectar y fijar la placa y justifica material y parámetros. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se ha usado software de impresión 3D y se han configurado sus parámetros para la impresión adecuada de objetos y prototipos 3D. | Modelo editable, archivo de fabricación y ficha de parámetros/ajuste; apartado e con datos, explicación o salida referida expresamente a ese criterio. El diseño mantiene unidades, permite conectar y fijar la placa y justifica material y parámetros. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra5"></a>
## RA5 · Integrar un prototipo robótico demostrable

**Enunciado oficial:** Desarrolla un proyecto para la creación de un prototipo de un sistema robótico funcional, respetando las fases de diseño, elaborando documentación técnica y presentando dicho proyecto.

El proyecto une electrónica, programa, mecánica y comunicación. Acota una función sencilla, como detectar un obstáculo y detener un movimiento de muy baja energía. Un objetivo acotado permite demostrar entradas, decisión y salida sin convertir el montaje en un ensayo de riesgo.

### Actividad CMO-311-RA5-A1

1. Redacta requisitos, diagrama de bloques, lista de materiales y presupuesto sintético.
2. Distribuye tareas y versiones de circuito, código y carcasa.
3. Prueba primero módulos y después integra con desconexión de emergencia accesible.
4. Presenta la función, un fallo previsto, las correcciones y la documentación suficiente para repetir el ensayo.

**Solución razonada y errores que debes interpretar:** Una demostración válida relaciona cada requisito con una prueba y muestra qué se hizo realmente. El prototipo no se declara apto para uso industrial por funcionar en el aula. Si falta un componente, documenta el simulador y la prueba física pendiente.

**Entregable:** Expediente del prototipo con planificación, versiones y vídeo o acta de demostración.

**Aceptación del reto:** Se verifica la función acotada, el comportamiento ante fallo y la correspondencia entre documentación y prototipo.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han descrito las fases del proceso de un proyecto tecnológico. | Expediente del prototipo con planificación, versiones y vídeo o acta de demostración; apartado a con datos, explicación o salida referida expresamente a ese criterio. Se verifica la función acotada, el comportamiento ante fallo y la correspondencia entre documentación y prototipo. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han usado herramientas de gestión de proyectos. | Expediente del prototipo con planificación, versiones y vídeo o acta de demostración; apartado b con datos, explicación o salida referida expresamente a ese criterio. Se verifica la función acotada, el comportamiento ante fallo y la correspondencia entre documentación y prototipo. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se ha empleado el software adecuado para la generación de la documentación asociada al proceso tecnológico (elaboración de exposiciones, presupuestos...). | Expediente del prototipo con planificación, versiones y vídeo o acta de demostración; apartado c con datos, explicación o salida referida expresamente a ese criterio. Se verifica la función acotada, el comportamiento ante fallo y la correspondencia entre documentación y prototipo. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se ha elaborado documentación técnica asociada a un proyecto tecnológico. | Expediente del prototipo con planificación, versiones y vídeo o acta de demostración; apartado d con datos, explicación o salida referida expresamente a ese criterio. Se verifica la función acotada, el comportamiento ante fallo y la correspondencia entre documentación y prototipo. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se ha desarrollado y seguido una planificación del proyecto. | Expediente del prototipo con planificación, versiones y vídeo o acta de demostración; apartado e con datos, explicación o salida referida expresamente a ese criterio. Se verifica la función acotada, el comportamiento ante fallo y la correspondencia entre documentación y prototipo. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| f | Se ha diseñado y creado un sistema robótico. | Acta de observación física supervisada y datos de medida o funcionamiento; Expediente del prototipo con planificación, versiones y vídeo o acta de demostración. La operación física del criterio es observada con seguridad y se relaciona con el diseño; una captura del simulador no la sustituye. |
| g | Se ha presentado adecuadamente el proyecto de un sistema robótico. | Expediente del prototipo con planificación, versiones y vídeo o acta de demostración; apartado g con datos, explicación o salida referida expresamente a ese criterio. Se verifica la función acotada, el comportamiento ante fallo y la correspondencia entre documentación y prototipo. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

## Dossier final y autoevaluación

Reúne las actividades por RA y enlaza cada CE con el artefacto concreto que lo demuestra. Una memoria extensa sin resultados identificables no sustituye las pruebas; una configuración que funciona por casualidad debe revisarse con casos de límite y recuperación. Explica las dependencias y qué haría falta para repetir el trabajo en otro equipo.

Como rúbrica de práctica se propone valorar corrección técnica (40 %), evidencia y pruebas (30 %), explicación de decisiones (20 %) y documentación/revisión (10 %). Es una propuesta propia: los instrumentos, ponderaciones y calificaciones oficiales corresponden al centro. Los CE no ejecutados o sin medios disponibles se anotan pendientes, sin inventar una adquisición del RA.

## Referencias y datos de trazabilidad

- [Matriz completa de este módulo](alineacion-ra.json).
- [Referentes normativos del repositorio](../../recursos/ra/referentes-oficiales.json).
- [Arduino: documentación](https://docs.arduino.cc/).
- [FreeCAD: documentación](https://www.freecad.org/documentation.php).
