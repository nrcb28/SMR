# Casos de revisión y evaluación de documentación

[Índice](README.md) · [Manual](01-manual-de-documentacion-versionada.md)

## Caso 1. Una corrección de DNS que cambia demasiado

Una guía afirma que el servidor es `.56.10`, pero una captura antigua muestra `.56.40`. La propuesta de revisión sustituye todas las apariciones de `.10` por `.40`, incluyendo la configuración de otros servicios. El laboratorio actual conserva `.10`.

**Resolución razonada:** primero se determina qué representa la captura y qué configuración se ha adoptado. Una evidencia antigua no cambia por sí sola el diseño vigente. Se corrige la captura o su explicación y se verifica que los ejemplos actuales usan el valor documentado. Una sustitución global sin revisar contexto puede romper varios procedimientos a la vez.

**Entrega:** un diff pequeño, una fuente del dato y una prueba dirigida más otra normal desde el cliente. Si no se ejecuta el laboratorio, se entrega la propuesta y la prueba pendiente, sin escribir que la consulta funcionó.

## Caso 2. Exclusiones que no eliminan el historial

En el repositorio ficticio se registra por error un archivo `notas-privadas.txt` con información sintética que se ha marcado como material excluido. Después se añade su nombre a `.gitignore`, pero sigue apareciendo entre los archivos ya versionados.

**Resolución:** la exclusión orienta qué archivos no rastreados se añaden normalmente; no retira automáticamente contenido ya registrado. En el ejercicio se revisa el índice y se aplica el procedimiento de Git para dejar de rastrear ese archivo conservando o eliminando su copia local según el objetivo. Si fuese una credencial real expuesta, sanear un archivo no sustituiría revocarla y seguir el procedimiento de incidente.

No introduzcas un secreto real para demostrar este caso. Usa una cadena reconocible como dato sintético y explica la distinción entre copia actual, commits anteriores y publicación remota. La solución debe decir qué estado corrige y qué historia conserva.

## Caso 3. El mismo requisito con dos ediciones

Una rama aclara que la prueba de HTTPS debe usar nombre y CA. Otra añade una prueba por IP para diagnosticar transporte. La integración parece contradictoria porque ambas se llaman “prueba final”.

**Resolución:** conserva finalidades separadas. La prueba por destino controlado puede aislar un fallo, mientras la aceptación utiliza la URL canónica con resolución normal y validación. Se cambian títulos y explicación para que el lector sepa qué demuestra cada una. Resolver el conflicto exige comprender el protocolo, no elegir automáticamente el párrafo más reciente.

**Comprobación:** un revisor lee sólo la versión integrada e identifica qué acción diagnostica y cuál acepta el servicio. Si no puede hacerlo, la integración documental sigue incompleta.

## Caso 4. Una mejora que sólo existe en el mensaje de commit

El mensaje dice “añadir restauración”, pero el archivo únicamente incorpora una captura del backup creado. La revisión no encuentra destino, punto recuperable, contenido restaurado ni prueba de permisos.

**Resolución:** se corrige el alcance del mensaje o se completa el procedimiento. Una tarea de copia y una restauración son productos diferentes. El historial ayuda a localizar la intención, pero la evidencia está en el contenido y en las pruebas. Una captura no se interpreta como más de lo que muestra.

## Taller y rúbrica propia

Cada participante crea una modificación pequeña sobre una guía sintética y otra persona la revisa. Alternan autor y revisor. Entregan estado inicial, propuesta, comentario fundamentado, corrección y versión aceptada. No necesitan publicar ni enviar mensajes a cuentas externas.

| Criterio | Peso orientativo | Evidencia |
| --- | ---: | --- |
| Alcance y requisito | 20 % | Explica qué corrige y qué permanece pendiente |
| Calidad técnica | 30 % | Instrucciones, unidades y dependencias coherentes |
| Trazabilidad | 20 % | Diff e historial permiten seguir la decisión |
| Revisión entre personas | 20 % | Comentario fundamentado y respuesta verificable |
| Presentación y privacidad | 10 % | Navegación clara y datos sintéticos |

La rúbrica es una propuesta de autoevaluación. No mide calidad por cantidad de commits ni sustituye los criterios del centro. Al repetir, cambia el caso y comprueba si puedes justificar una decisión sin depender de una solución memorizada.
