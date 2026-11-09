# Manual de documentación técnica versionada

[Índice de la propuesta](README.md) · [Casos de revisión](02-casos-y-evaluacion.md)

## 1. Alcance de esta ampliación

Este manual desarrolla la propuesta complementaria de documentar prácticas con Git. No identifica la optativa oficial del centro ni le atribuye un currículo. Se realiza en un repositorio local nuevo con datos sintéticos. Sus ejercicios permiten practicar claridad, trazabilidad y revisión antes de utilizar esos hábitos en otras asignaturas.

Una guía técnica tiene dos estados que deben concordar: el comportamiento que describe y la versión del entorno para la que fue comprobada. Un historial permite saber qué cambió, pero no demuestra que cada instrucción sea correcta. Por eso se combina control de versiones con lectura, fuentes y pruebas pertinentes.

## 2. Unidad mínima de una guía reproducible

Una instrucción útil identifica máquina, sistema, privilegio, finalidad y objeto. “Reinicia el servicio” deja preguntas abiertas: cuál, dónde, con qué permisos y por qué. En una memoria de DNS, distingue editar el archivo de zona, validar sintaxis, cargar el cambio y consultar desde cliente. Cada paso aporta una evidencia diferente.

Separa resultados esperados y observados. Una salida de manual enseña qué interpretar; la ejecución real registra lo ocurrido en tu VM. Si una práctica aún no se ha ejecutado, conserva el procedimiento como propuesta y marca la prueba pendiente. No cambies su estado sólo para que la memoria parezca terminada.

Una estructura pequeña puede contener `README.md`, `guia.md`, `datos/` y `configuracion-saneada/`. La información privada pertenece a otro espacio autorizado. No publiques discos virtuales para demostrar que instalaste un SO: una ficha de versión, configuración y evidencia adecuada es más revisable.

## 3. Diseñar cambios que se puedan revisar

Un commit debe responder a una finalidad reconocible: corregir una dirección, aclarar una precondición o añadir una prueba. Si se mezclan cambios de formato, nombres y procedimiento en un bloque enorme, resulta más difícil saber qué modificación explica un problema posterior.

Antes de registrar, revisa el directorio de trabajo y el índice. `git diff` muestra cambios no preparados respecto al índice; `git diff --cached` muestra lo preparado para el siguiente commit. Que un archivo aparezca modificado no significa que toda su versión actual esté incluida: el índice puede contener una versión intermedia.

En la carpeta de la práctica, los siguientes comandos consultan estado y diferencias:

```bash
git status --short
git diff -- guia.md
git diff --cached -- guia.md
```

Lee la diferencia por su significado. Un signo menos y otro más pueden representar corregir un dato, pero también eliminar una comprobación importante. El número de líneas no mide la importancia técnica. Comprueba nombres, rutas, unidades y dependencias antes de aceptar.

## 4. Ramas para una revisión acotada

Una rama permite trabajar sobre una línea identificada sin crear carpetas “final”, “final2” y “definitiva”. En un repositorio limpio de prácticas puedes crear `revision-guia` con `git switch -c revision-guia`. Antes consulta `git status`: los cambios sin registrar requieren entender qué se conserva al cambiar de rama.

Haz una corrección, revisa y registra su commit. Compara con `main` usando `git diff main...revision-guia -- guia.md`; esta forma compara el punto común con la rama revisada. Para un ejercicio lineal sencillo permite localizar lo aportado, pero no debes describir toda comparación de Git como si usara siempre el mismo punto inicial.

El revisor explica problema, evidencia y propuesta. “No me gusta” no fundamenta una revisión técnica. “La ruta apunta al archivo anterior; el servicio carga este otro archivo según la unidad y la configuración efectiva” aporta una razón comprobable. La decisión debe quedar en una corrección o una nota que resuelva la duda.

## 5. Conflictos y recuperación de una edición

Un conflicto de texto significa que Git necesita una decisión para integrar ciertos cambios. No demuestra que una de las personas haya trabajado mal. Si dos ramas cambiaron el mismo parámetro con necesidades distintas, quitar los marcadores sin entender el requisito puede dejar una guía sintácticamente limpia y técnicamente incoherente.

En una práctica de conflicto, conserva el objetivo de ambas modificaciones, consulta el estado y elige una versión coherente con el laboratorio. Después revisa el archivo completo, prepara el resultado y termina la integración según el estado que muestre Git. Si decides abandonar, utiliza el procedimiento de aborto apropiado a la operación en curso, después de comprender qué trabajo conservarás.

Para recuperar una versión antigua de un archivo, identifica primero el commit mediante el historial y compara su contenido. `git restore` puede sobrescribir cambios del directorio de trabajo; no se presenta como una consulta inocua. Guarda o registra las ediciones que necesites conservar antes de aplicar una restauración deliberada. Recuperar un archivo y borrar una rama no son operaciones equivalentes.

## 6. Formatos y revisión de datos

Declara UTF-8, separador CSV, formato decimal y fechas. Un cambio de finales de línea puede hacer que parezca modificado todo un archivo; no lo confundas con una revisión sustancial. Acuerda convenciones y comprueba que las herramientas de tu entorno mantienen el contenido.

Una tabla Markdown debe identificar unidades. Un CSV puede transportar texto que la hoja interprete como fecha o fórmula; usa datos sintéticos y revisa la importación. Git conserva bytes y versiones, pero no decide si una columna tiene el significado correcto. Incluye diccionario de datos y una muestra comprobada cuando la guía dependa de un archivo.

La documentación oficial de [Git](https://git-scm.com/docs), [Pro Git](https://git-scm.com/book/es/v2) y los manuales del servicio descrito son las fuentes para resolver opciones y compatibilidad. No copies una orden sólo porque se repite en varios tutoriales: identifica producto, versión y efecto.

## 7. Entrega y revisión

Entrega guía, historial y una nota de revisión con una duda resuelta y una prueba pendiente o completada según corresponda. Una segunda persona debe localizar precondiciones, ejecución, interpretación y retorno sin necesitar la explicación oral del autor. Las dudas que encuentre son información para mejorar la guía, no un motivo para ocultar los pasos difíciles.
