# CMO-318 · Programación de videojuegos

[Catálogo de optativas](../README.md) · [Índice general](../../README.md)

## Aplicabilidad y forma de estudio

La tabla del catálogo fija 90 horas para este módulo específico de Informática y Comunicaciones. Su ubicación en segundo se deduce del encaje con las optativas de SMR (50/90 horas); no se presenta como una columna de curso expresamente asignada a IFC en el catálogo. Deben confirmarse la oferta y las condiciones del centro.

El currículo de referencia es la [Orden 3536/2025](https://www.bocm.es/boletin/CM_Orden_BOCM/2025/08/27/BOCM-20250827-5.PDF), Anexo II, CMO-318; BOCM página 206 y siguientes; PDF páginas 189–190. La relación aplicable se contrasta con la [Orden 3822/2026](https://www.bocm.es/boletin/CM_Orden_BOCM/2026/09/25/BOCM-20260925-20.PDF). El catálogo permite una oferta; no demuestra que un centro imparta todas estas materias ni que un alumno deba cursarlas simultáneamente.

Los enunciados de RA y los CE de las tablas se transcriben del referente normativo. Las explicaciones, retos, soluciones y condiciones de aceptación son propuestas didácticas propias. La evidencia esperada se diferencia de lo observado: completa resultados reales en una copia de la plantilla de seguimiento.

## Preparación

Revisa el [laboratorio común](../../docs/laboratorio.md) y trabaja con datos sintéticos y un entorno identificado. Antes de modificar, registra versión, estado inicial y recuperación. Las tareas que necesitan hardware, motor de juego o plataforma administrada deben ejecutarse en esos medios para aportar evidencia completa; la preparación escrita conserva su valor y se marca como pendiente de esa ejecución.

## Ruta por resultados de aprendizaje

<a id="ra1"></a>
## RA1 · Situar un prototipo en su contexto

**Enunciado oficial:** Identifica los principales referentes de la historia y la cultura del videojuego valorando su incidencia en la sociedad actual y las tendencias de desarrollo.

La historia del videojuego relaciona diseño, tecnología, distribución y públicos. Identificar referentes permite justificar decisiones sin copiar recursos protegidos. Las tendencias se contrastan con fuentes y fecha, no sólo con opiniones o cifras sin origen.

### Actividad CMO-318-RA1-A1

1. Compara tres juegos o etapas por mecánica, plataforma, interacción y modelo de distribución.
2. Relaciona una limitación tecnológica con una decisión de diseño.
3. Selecciona una tendencia para analizar posibilidades y barreras de un pequeño equipo.
4. Define un prototipo de aula y registra licencias de motores, arte y sonido.

**Solución razonada y errores que debes interpretar:** La comparación debe explicar una relación entre tecnología y experiencia, además de enumerar títulos. El prototipo escolar puede usar formas geométricas propias para no depender de recursos con licencias inciertas; su calidad se evalúa por la función que pretende mostrar.

**Entregable:** Informe de referentes y propuesta de prototipo.

**Aceptación del reto:** Cada referencia tiene contexto y la propuesta justifica alcance, recursos y licencias.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha situado el videojuego en el contexto de la creación audiovisual, reconociendo su importancia y potencial. | Informe de referentes y propuesta de prototipo; apartado a con datos, explicación o salida referida expresamente a ese criterio. Cada referencia tiene contexto y la propuesta justifica alcance, recursos y licencias. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han conocido las características del mercado de videojuegos. | Informe de referentes y propuesta de prototipo; apartado b con datos, explicación o salida referida expresamente a ese criterio. Cada referencia tiene contexto y la propuesta justifica alcance, recursos y licencias. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han reconocido los principales elementos de desarrollo de videojuegos y el state of the art de las tecnologías implicadas. | Informe de referentes y propuesta de prototipo; apartado c con datos, explicación o salida referida expresamente a ese criterio. Cada referencia tiene contexto y la propuesta justifica alcance, recursos y licencias. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han valorado las principales tendencias en el mundo de los videojuegos en relación con las tecnologías emergentes. | Informe de referentes y propuesta de prototipo; apartado d con datos, explicación o salida referida expresamente a ese criterio. Cada referencia tiene contexto y la propuesta justifica alcance, recursos y licencias. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra2"></a>
## RA2 · Preparar un proyecto en un motor

**Enunciado oficial:** Configura entornos de desarrollo, herramientas y motores de desarrollo de videojuegos, aplicando las técnicas necesarias y teniendo en cuenta los avances tecnológicos en el sector.

Un motor organiza escenas, objetos, recursos, entrada y renderizado. Registrar versión y estructura evita que una guía de otra edición produzca comportamientos distintos. Empieza con una escena pequeña que se pueda ejecutar y comprender.

### Actividad CMO-318-RA2-A1

1. Instala el motor elegido desde su fuente oficial según el procedimiento del centro.
2. Crea una escena con jugador, obstáculo, objetivo y cámara o vista 2D.
3. Asigna recursos propios, colisión, entrada y configuración visual apropiada al prototipo.
4. Ejecuta la prueba de iluminación ON/OFF descrita abajo y después comprueba las interacciones; guarda estructura, recursos y versión del proyecto.

### Escena mínima de iluminación e interacción (CE2.e)

Para una variante en **Godot 4**, crea una escena 2D independiente de ensayo. Usa recursos propios y conserva el proyecto editable; esta secuencia necesita el motor instalado y no se presenta como ejecutada durante la elaboración de la guía.

1. Crea una raíz `Node2D`, un `Polygon2D` con un cuadrado blanco, un `CanvasModulate` y un `PointLight2D`. Para un ensayo reproducible en una ventana de 800×600, define los puntos locales del cuadrado `(0,0)`, `(100,0)`, `(100,100)`, `(0,100)`, sitúa el polígono en `(200,150)` y la luz en `(250,200)`. Usa `CanvasModulate` con el tono gris oscuro `(0.15, 0.15, 0.15, 1)` para disponer de una condición ambiental controlada. No añadas una cámara que altere ese encuadre durante la comparación.
2. Asigna a `PointLight2D.texture` una textura radial propia. Una opción es `GradientTexture2D` con relleno radial y gradiente de blanco opaco en el centro a blanco transparente en el borde. La textura es necesaria para definir el alcance de la luz; registra su tamaño y los parámetros elegidos.
3. Comprueba que la máscara de luz del objeto y **Item Cull Mask** de la luz comparten el primer bit. Para la textura radial de 128×128 propuesta, fija **Texture Scale** en 2 y **Energy** en 1, manteniendo esos valores durante la comparación. Un objeto fuera de alcance o excluido por máscara puede no cambiar aunque la luz esté habilitada.
4. Añade en **Project Settings → Input Map** una acción `alternar_luz` asociada a una tecla, y conecta esa entrada mediante el script siguiente en la raíz. Ejecuta la escena: alternar debe cambiar únicamente `enabled`, manteniendo posición, textura, color y encuadre.

```gdscript
extends Node2D

@onready var luz: PointLight2D = $PointLight2D

func _unhandled_input(event: InputEvent) -> void:
    if event.is_action_pressed("alternar_luz"):
        luz.enabled = not luz.enabled
```

5. Captura o registra dos estados de la escena **en ejecución**: luz deshabilitada y luz habilitada. En el primero el cuadrado queda afectado por la modulación ambiental; en el segundo debe apreciarse el aporte de iluminación dentro del alcance. Repite tras mover la luz fuera de alcance y explica el cambio.
6. Si no se observa diferencia, revisa textura asignada, alcance, máscaras, modulación ambiental y nodo que recibe la entrada. No cambies todos a la vez: conserva una prueba discriminante por hipótesis y registra la corrección.

**Evidencia de CE2.e:** escena `.tscn`, textura/recurso utilizado, script e Input Map, parámetros de luz y objeto y comparación ON/OFF desde una ejecución real. La respuesta a la tecla demuestra una interacción entre entrada, script y luz; las capturas y parámetros permiten explicar los conceptos básicos de iluminación. Una escena dibujada o este código sin ejecutar no acredita la actuación: si no hay motor, marca esa evidencia **pendiente**. Consulta [luces y sombras 2D de Godot](https://docs.godotengine.org/en/stable/tutorials/2d/2d_lights_and_shadows.html) para la versión utilizada.

**Solución razonada y errores que debes interpretar:** En Godot 4 una escena 2D puede organizarse con CharacterBody2D y formas de colisión; en otro motor hay que documentar su equivalente. Instalar el editor no demuestra que los recursos estén conectados ni que el jugador responda: hay que ejecutar el proyecto.

**Entregable:** Proyecto mínimo del motor y registro de escenas/recursos/entrada.

**Aceptación del reto:** El proyecto abre en la versión indicada, ejecuta la escena y responde a la interacción diseñada.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha instalado y configurado el motor de desarrollo de videojuegos. | Escena, recurso o script del proyecto y demostración de la acción del criterio a; Proyecto mínimo del motor y registro de escenas/recursos/entrada. El comportamiento se comprueba ejecutando el proyecto del motor en la versión indicada; una descripción sin ejecución queda como preparación. |
| b | Se han identificado y conectado todos los tipos de recursos disponibles y necesarios para la elaboración del videojuego. | Proyecto mínimo del motor y registro de escenas/recursos/entrada; apartado b con datos, explicación o salida referida expresamente a ese criterio. El proyecto abre en la versión indicada, ejecuta la escena y responde a la interacción diseñada. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se ha definido la estructura de un proyecto de videojuego. | Proyecto mínimo del motor y registro de escenas/recursos/entrada; apartado c con datos, explicación o salida referida expresamente a ese criterio. El proyecto abre en la versión indicada, ejecuta la escena y responde a la interacción diseñada. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han creado diferentes objetos del videojuego y componentes. | Escena, recurso o script del proyecto y demostración de la acción del criterio d; Proyecto mínimo del motor y registro de escenas/recursos/entrada. El comportamiento se comprueba ejecutando el proyecto del motor en la versión indicada; una descripción sin ejecución queda como preparación. |
| e | Se han configurado las interacciones entre los diferentes elementos y los conceptos básicos de iluminación. | Proyecto Godot ejecutado con interacción de entrada que alterna PointLight2D, textura/máscaras/ambiente documentados y comparación ON/OFF. En la misma escena se observa el cambio de iluminación al alternar la luz y se explica textura, alcance y máscaras. Sin motor o ejecución, CE2.e queda pendiente. |
| f | Se han analizado y creado las diferentes interacciones del usuario con el videojuego. | Escena, recurso o script del proyecto y demostración de la acción del criterio f; Proyecto mínimo del motor y registro de escenas/recursos/entrada. El comportamiento se comprueba ejecutando el proyecto del motor en la versión indicada; una descripción sin ejecución queda como preparación. |

<a id="ra3"></a>
## RA3 · Programar estados, eventos y tiempo

**Enunciado oficial:** Establece la arquitectura interna de videojuegos determinando la programación de scripts del motor de desarrollo.

La lógica del juego relaciona entrada, estado, actualización y señales entre objetos. Multiplicar desplazamiento por el tiempo adecuado o utilizar el mecanismo físico del motor evita depender indebidamente de la tasa de fotogramas.

### Actividad CMO-318-RA3-A1

1. Define estados inicio, jugando, pausa y final, con transiciones explícitas.
2. Programa movimiento, recogida de un objeto y un evento de fin.
3. Conecta señales o eventos y registra orden de ejecución.
4. Depura un caso de evento duplicado y prueba dos condiciones de tasa de ejecución en el entorno de aula.

**Solución razonada y errores que debes interpretar:** Una señal conectada dos veces puede sumar dos puntos por una sola acción. El registro debe demostrar la causa y la corrección. En un cuerpo físico se respeta la API de la versión del motor: no se añade delta indiscriminadamente si el método ya trabaja con velocidad y paso físico.

**Entregable:** Scripts, diagrama de estados y traza de eventos.

**Aceptación del reto:** Una entrada produce el evento esperado una sola vez y la lógica conserva coherencia en pausa y reinicio.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han manejado conceptos esenciales del lenguaje de programación, utilizado en el motor de desarrollo de videojuegos. | Escena, recurso o script del proyecto y demostración de la acción del criterio a; Scripts, diagrama de estados y traza de eventos. El comportamiento se comprueba ejecutando el proyecto del motor en la versión indicada; una descripción sin ejecución queda como preparación. |
| b | Se han analizado los diferentes elementos que intervienen en la mecánica del videojuego. | Scripts, diagrama de estados y traza de eventos; apartado b con datos, explicación o salida referida expresamente a ese criterio. Una entrada produce el evento esperado una sola vez y la lógica conserva coherencia en pausa y reinicio. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han creado y usado scripts para la programación de los objetos del videojuego. | Escena, recurso o script del proyecto y demostración de la acción del criterio c; Scripts, diagrama de estados y traza de eventos. El comportamiento se comprueba ejecutando el proyecto del motor en la versión indicada; una descripción sin ejecución queda como preparación. |
| d | Se han creado funciones de eventos que ocurren durante el juego. | Escena, recurso o script del proyecto y demostración de la acción del criterio d; Scripts, diagrama de estados y traza de eventos. El comportamiento se comprueba ejecutando el proyecto del motor en la versión indicada; una descripción sin ejecución queda como preparación. |
| e | Se han administrado el tiempo de los eventos y acciones y el orden de ejecución. | Escena, recurso o script del proyecto y demostración de la acción del criterio e; Scripts, diagrama de estados y traza de eventos. El comportamiento se comprueba ejecutando el proyecto del motor en la versión indicada; una descripción sin ejecución queda como preparación. |
| f | Se han verificado las herramientas de ayuda a la programación de scripts que permiten la depuración, testeo y desarrollo de los mismos. | Escena, recurso o script del proyecto y demostración de la acción del criterio f; Scripts, diagrama de estados y traza de eventos. El comportamiento se comprueba ejecutando el proyecto del motor en la versión indicada; una descripción sin ejecución queda como preparación. |
| g | Se ha supervisado el sistema de eventos para comunicación entre los objetos de la aplicación basados en la entrada. | Escena, recurso o script del proyecto y demostración de la acción del criterio g; Scripts, diagrama de estados y traza de eventos. El comportamiento se comprueba ejecutando el proyecto del motor en la versión indicada; una descripción sin ejecución queda como preparación. |

<a id="ra4"></a>
## RA4 · Construir una interfaz legible y operable

**Enunciado oficial:** Define el interfaz de usuario del videojuego teniendo en cuenta su rapidez y la facilidad de utilización.

La interfaz muestra estado y permite acciones. Orden de dibujo, anclajes, tamaños, foco y contraste influyen en su uso. Una animación debe informar o ayudar a comprender, sin ocultar estados ni impedir operar con teclado.

### Actividad CMO-318-RA4-A1

1. Crea menú de inicio, marcador, pausa y pantalla final.
2. Ajusta capas u orden de visualización y prueba dos tamaños de ventana.
3. Asocia botones con acciones reales y comprueba foco, activación y retorno.
4. Añade una animación breve y una alternativa o reducción cuando proceda; documenta límites de accesibilidad.

**Solución razonada y errores que debes interpretar:** Un botón visible que no activa ninguna acción no cumple la interacción. El marcador debe reflejar el estado real y mantenerse legible. La revisión escolar comprueba aspectos concretos; no equivale a certificar accesibilidad completa del juego.

**Entregable:** Interfaz del proyecto y matriz de interacción/ventanas.

**Aceptación del reto:** Las acciones son operables, el estado es legible y la interfaz conserva disposición y foco en los tamaños probados.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha determinado el orden de visualización de todos los objetos que contiene el juego. | Interfaz del proyecto y matriz de interacción/ventanas; apartado a con datos, explicación o salida referida expresamente a ese criterio. Las acciones son operables, el estado es legible y la interfaz conserva disposición y foco en los tamaños probados. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han ajustado los modos de renderizado de los objetos en la pantalla o contenedor del juego. | Interfaz del proyecto y matriz de interacción/ventanas; apartado b con datos, explicación o salida referida expresamente a ese criterio. Las acciones son operables, el estado es legible y la interfaz conserva disposición y foco en los tamaños probados. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han posicionado y establecido los tamaños y rotaciones de los elementos de la interfaz de usuario en la pantalla. | Escena, recurso o script del proyecto y demostración de la acción del criterio c; Interfaz del proyecto y matriz de interacción/ventanas. El comportamiento se comprueba ejecutando el proyecto del motor en la versión indicada; una descripción sin ejecución queda como preparación. |
| d | Se ha proporcionado a los elementos del interfaz la interacción asociada a las acciones del videojuego. | Escena, recurso o script del proyecto y demostración de la acción del criterio d; Interfaz del proyecto y matriz de interacción/ventanas. El comportamiento se comprueba ejecutando el proyecto del motor en la versión indicada; una descripción sin ejecución queda como preparación. |
| e | Se han configurado las animaciones del interfaz de usuario. | Escena, recurso o script del proyecto y demostración de la acción del criterio e; Interfaz del proyecto y matriz de interacción/ventanas. El comportamiento se comprueba ejecutando el proyecto del motor en la versión indicada; una descripción sin ejecución queda como preparación. |

## Dossier final y autoevaluación

Reúne las actividades por RA y enlaza cada CE con el artefacto concreto que lo demuestra. Una memoria extensa sin resultados identificables no sustituye las pruebas; una configuración que funciona por casualidad debe revisarse con casos de límite y recuperación. Explica las dependencias y qué haría falta para repetir el trabajo en otro equipo.

Como rúbrica de práctica se propone valorar corrección técnica (40 %), evidencia y pruebas (30 %), explicación de decisiones (20 %) y documentación/revisión (10 %). Es una propuesta propia: los instrumentos, ponderaciones y calificaciones oficiales corresponden al centro. Los CE no ejecutados o sin medios disponibles se anotan pendientes, sin inventar una adquisición del RA.

## Referencias y datos de trazabilidad

- [Matriz completa de este módulo](alineacion-ra.json).
- [Referentes normativos del repositorio](../../recursos/ra/referentes-oficiales.json).
- [Godot: primeros pasos](https://docs.godotengine.org/en/stable/getting_started/introduction/index.html).
- [Godot: guía paso a paso](https://docs.godotengine.org/en/stable/getting_started/step_by_step/index.html).
