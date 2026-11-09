# CMO-316 · Programación en Python

[Catálogo de optativas](../README.md) · [Índice general](../../README.md)

## Aplicabilidad y forma de estudio

La tabla del catálogo fija 90 horas para este módulo específico de Informática y Comunicaciones. Su ubicación en segundo se deduce del encaje con las optativas de SMR (50/90 horas); no se presenta como una columna de curso expresamente asignada a IFC en el catálogo. Deben confirmarse la oferta y las condiciones del centro.

El currículo de referencia es la [Orden 3536/2025](https://www.bocm.es/boletin/CM_Orden_BOCM/2025/08/27/BOCM-20250827-5.PDF), Anexo II, CMO-316; BOCM página 203 y siguientes; PDF páginas 186–187. La relación aplicable se contrasta con la [Orden 3822/2026](https://www.bocm.es/boletin/CM_Orden_BOCM/2026/09/25/BOCM-20260925-20.PDF). El catálogo permite una oferta; no demuestra que un centro imparta todas estas materias ni que un alumno deba cursarlas simultáneamente.

Los enunciados de RA y los CE de las tablas se transcriben del referente normativo. Las explicaciones, retos, soluciones y condiciones de aceptación son propuestas didácticas propias. La evidencia esperada se diferencia de lo observado: completa resultados reales en una copia de la plantilla de seguimiento.

## Preparación

Revisa el [laboratorio común](../../docs/laboratorio.md) y trabaja con datos sintéticos y un entorno identificado. Antes de modificar, registra versión, estado inicial y recuperación. Las tareas que necesitan hardware, motor de juego o plataforma administrada deben ejecutarse en esos medios para aportar evidencia completa; la preparación escrita conserva su valor y se marca como pendiente de esa ejecución.

## Ruta por resultados de aprendizaje

**Nota de denominación:** el anexo curricular de 2025 imprime «Phyton» en la cabecera; el catálogo de 2026 emplea «Python». Esta guía usa Python para la denominación del lenguaje y conserva literalmente los RA del referente.

<a id="ra1"></a>
## RA1 · Dominar nombres, valores y tipos en Python

**Enunciado oficial:** Reconoce la estructura de un programa informático, identificando y relacionando los elementos propios del lenguaje de programación utilizado.

Python asocia nombres con objetos. Comprender tipo, mutabilidad, operadores y conversiones permite explicar el programa sin confundir una anotación con validación automática. Se utiliza Python 3 y biblioteca estándar para reducir dependencias de la práctica.

### Actividad CMO-316-RA1-A1

1. Crea un proyecto con módulo principal y un entorno identificado.
2. Representa código de activo, cantidad, estado y precio con tipos adecuados.
3. Prueba operadores, conversión explícita y entrada no convertible.
4. Usa el depurador y comentarios para explicar valores y decisiones.

**Solución razonada y errores que debes interpretar:** Un código como 0012 se conserva como texto si los ceros forman parte de su identidad. La conversión de cantidad necesita capturar ValueError, mientras una anotación int no convierte una cadena por sí sola. Explica el contrato en lugar de confiar en el editor.

**Entregable:** Proyecto Python y tabla de expresiones/tipos.

**Aceptación del reto:** Se predicen resultados y tipos, y se detectan entradas que violan el contrato.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han identificado los bloques que componen la estructura de un programa informático. | Proyecto Python y tabla de expresiones/tipos; apartado a con datos, explicación o salida referida expresamente a ese criterio. Se predicen resultados y tipos, y se detectan entradas que violan el contrato. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han creado proyectos de desarrollo de aplicaciones. | Proyecto Python y tabla de expresiones/tipos; apartado b con datos, explicación o salida referida expresamente a ese criterio. Se predicen resultados y tipos, y se detectan entradas que violan el contrato. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han utilizado entornos integrados de desarrollo. | Proyecto Python y tabla de expresiones/tipos; apartado c con datos, explicación o salida referida expresamente a ese criterio. Se predicen resultados y tipos, y se detectan entradas que violan el contrato. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han identificado los distintos tipos de variables y la utilidad específica de cada uno. | Código y caso de entrada/salida identificado para el criterio d, incorporados a «Proyecto Python y tabla de expresiones/tipos». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| e | Se ha modificado el código de un programa para crear y utilizar variables. | Código y caso de entrada/salida identificado para el criterio e, incorporados a «Proyecto Python y tabla de expresiones/tipos». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| f | Se han creado y utilizado constantes y literales. Se han clasificado, reconocido y utilizado en expresiones los operadores del lenguaje. | Proyecto Python y tabla de expresiones/tipos; apartado f con datos, explicación o salida referida expresamente a ese criterio. Se predicen resultados y tipos, y se detectan entradas que violan el contrato. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| g | Se ha comprobado el funcionamiento de las conversiones de tipo explícitas e implícitas. | Proyecto Python y tabla de expresiones/tipos; apartado g con datos, explicación o salida referida expresamente a ese criterio. Se predicen resultados y tipos, y se detectan entradas que violan el contrato. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| h | Se han introducido comentarios en el código. | Código y caso de entrada/salida identificado para el criterio h, incorporados a «Proyecto Python y tabla de expresiones/tipos». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |

<a id="ra2"></a>
## RA2 · Elegir y depurar estructuras de control

**Enunciado oficial:** Escribe y depura código, analizando y utilizando las estructuras de control del lenguaje.

La corrección incluye casos vacíos, límites y errores, no sólo la ruta favorable. Un bucle debe tener un motivo para terminar y una excepción debe tratar un error previsto, sin ocultar defectos con un except general sin información.

### Actividad CMO-316-RA2-A1

1. Filtra cantidades válidas de una lista con valores cero, negativos y texto.
2. Usa selección y repetición, explicando cada rama.
3. Introduce un caso que provoque conversión inválida y conserva su tratamiento.
4. Depura una condición de frontera y documenta la corrección.

**Solución razonada y errores que debes interpretar:** La política puede rechazar toda la entrada o informar por fila; ambas requieren un contrato explícito. Saltar una fila errónea sin indicarlo puede producir un total aparentemente correcto y ocultar pérdida de información.

**Entregable:** Tabla de casos, código y registro de depuración.

**Aceptación del reto:** Los límites y errores tienen respuesta definida y la ejecución no queda bloqueada.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha escrito y probado código que haga uso de estructuras de selección. | Código y caso de entrada/salida identificado para el criterio a, incorporados a «Tabla de casos, código y registro de depuración». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| b | Se han utilizado estructuras de repetición. | Tabla de casos, código y registro de depuración; apartado b con datos, explicación o salida referida expresamente a ese criterio. Los límites y errores tienen respuesta definida y la ejecución no queda bloqueada. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han reconocido las posibilidades de las sentencias de salto. | Tabla de casos, código y registro de depuración; apartado c con datos, explicación o salida referida expresamente a ese criterio. Los límites y errores tienen respuesta definida y la ejecución no queda bloqueada. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se ha escrito código utilizando control de excepciones. | Código y caso de entrada/salida identificado para el criterio d, incorporados a «Tabla de casos, código y registro de depuración». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| e | Se han creado programas ejecutables utilizando diferentes estructuras de control. | Código y caso de entrada/salida identificado para el criterio e, incorporados a «Tabla de casos, código y registro de depuración». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| f | Se han probado y depurado los programas. Se ha comentado y documentado el código. | Código y caso de entrada/salida identificado para el criterio f, incorporados a «Tabla de casos, código y registro de depuración». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |

<a id="ra3"></a>
## RA3 · Modularizar y comprender los argumentos

**Enunciado oficial:** Escribe código utilizando programación modular. Conoce la diferencia entre el paso de parámetros por valor y por referencia.

Las funciones separan cálculo y entrada/salida. En Python los argumentos se asocian a objetos: reasignar un parámetro y mutar un objeto mutable tienen efectos distintos. Esta descripción evita atribuir sin matices el paso por referencia de otros lenguajes.

### Actividad CMO-316-RA3-A1

1. Escribe funciones para suma de cantidades y una operación matemática elemental.
2. Compara versión iterativa y recursiva con un límite pequeño y definido.
3. Pasa una lista y observa diferencia entre reasignar el parámetro y modificar su contenido.
4. Documenta precondiciones, retorno y efectos secundarios.

**Solución razonada y errores que debes interpretar:** Si una función hace datos=[] sólo cambia su nombre local; si hace datos.append(x) modifica la lista compartida. Una función pura puede devolver una nueva lista para evitar ese efecto. La recursividad necesita caso base y no es siempre la mejor elección en Python.

**Entregable:** Módulo de funciones y tabla de identidad/mutación.

**Aceptación del reto:** Se explica cada efecto con un ejemplo y el caso base evita recursión indefinida.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han codificado funciones para resolver problemas de matemática elemental. | Código y caso de entrada/salida identificado para el criterio a, incorporados a «Módulo de funciones y tabla de identidad/mutación». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| b | Se ha utilizado el concepto de iteración y recursividad. | Módulo de funciones y tabla de identidad/mutación; apartado b con datos, explicación o salida referida expresamente a ese criterio. Se explica cada efecto con un ejemplo y el caso base evita recursión indefinida. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra4"></a>
## RA4 · Elegir cadenas, listas y diccionarios

**Enunciado oficial:** Escribe programas que manipulen información, seleccionando y utilizando tipos avanzados de datos.

El tipo de estructura debe corresponder al acceso previsto. Un diccionario indexa por clave; una lista conserva secuencia; una cadena representa texto y es inmutable. Convertir todo a lista puede complicar búsqueda e integridad de identificadores.

### Actividad CMO-316-RA4-A1

1. Construye un inventario como diccionario por código y una lista de incidencias ordenadas.
2. Normaliza texto de entrada sin cambiar códigos sensibles a formato.
3. Detecta duplicados y campos ausentes antes de calcular.
4. Genera un resumen de cantidades y compara con un resultado manual.

**Solución razonada y errores que debes interpretar:** Dos registros con el mismo código requieren una regla de rechazo o combinación; asignar el segundo sobre el primero sin avisar puede perder información. La normalización se decide por campo y se prueba con espacios, acentos y entradas vacías.

**Entregable:** Modelo de datos y función de validación/resumen.

**Aceptación del reto:** Se conservan códigos y orden cuando corresponde, y los duplicados no se sobrescriben silenciosamente.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han escrito programas que utilizan cadenas, listas y diccionarios. | Código y caso de entrada/salida identificado para el criterio a, incorporados a «Modelo de datos y función de validación/resumen». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |

<a id="ra5"></a>
## RA5 · Leer y escribir archivos con contrato

**Enunciado oficial:** Realiza operaciones de entrada y salida de información, utilizando procedimientos específicos del lenguaje y librerías de clases.

La E/S define codificación, formato, ruta y respuesta ante errores. Usar bibliotecas CSV o JSON preserva estructuras que una separación ingenua de cadenas puede romper. Un informe no debe sobrescribir su fuente ni datos de trabajo ajenos.

### Actividad CMO-316-RA5-A1

1. Lee un CSV UTF-8 sintético y valida cabeceras y cantidades.
2. Genera un resumen por consola y otro JSON en una ruta nueva de ensayo.
3. Ejecuta una lectura secuencial del CSV y un segundo programa de acceso directo con `seek` sobre registros binarios de longitud fija, según el ejemplo siguiente. Conserva los resultados y explica la diferencia de métodos.
4. Ensaya falta de permisos o archivo mal formado sin alterar el sistema real.

### Dos métodos implementados: secuencial y directo (CE5.e)

El ejemplo [acceso_registros_fijos.py](ejemplos/acceso_registros_fijos.py) crea un archivo **real de ensayo** en un directorio temporal, realiza ambos métodos de lectura y elimina ese directorio al terminar. No modifica archivos del usuario. Cada registro ocupa 16 bytes: identificador de 4 bytes y código ASCII de 12 bytes. La convención de bytes y longitud es parte del formato, no una propiedad universal de todos los archivos.

Desde la raíz del repositorio:

```bash
python3 optativas/CMO-316-programacion-python/ejemplos/acceso_registros_fijos.py
```

1. Sigue el bucle que lee bloques consecutivos hasta fin de archivo y comprueba los tres registros `PC-001`, `PC-002`, `PC-003`.
2. Sigue `leer_directo`: obtiene el tamaño, valida que sea múltiplo de 16, comprueba el índice y ejecuta `seek(indice * 16)` antes de leer un bloque. Para índice 1, contando desde cero, el desplazamiento es 16 bytes y se obtiene `(2, 'PC-002')`.
3. Compara la segunda lectura con el segundo elemento de la lectura secuencial. El archivo inicial ocupa 48 bytes. El índice 3 queda fuera de los tres registros y debe producir el rechazo previsto, no datos vacíos presentados como un registro válido.
4. En una copia del ejercicio, añade un cuarto registro y repite ambos métodos. Ensaya además un bloque incompleto en otro archivo temporal: debe rechazarse como formato inválido. Conserva el código modificado y las salidas reales.

No apliques el desplazamiento de este formato a un CSV UTF-8 de registros variables. Un carácter puede ocupar varios bytes y cada fila puede tener longitud distinta; para acceso directo haría falta otra estrategia, como un índice de posiciones válido para el archivo concreto. Aquí se demuestra acceso secuencial **y** acceso directo con un contrato binario explícito.

**Evidencia de CE5.e:** los dos métodos implementados, resultado equivalente, control de índice fuera de rango y caso de formato incompleto. La comparación verbal de métodos sin crear o ejecutar programas deja el criterio pendiente. El ejemplo temporal se ha comprobado como código local; la evidencia del estudiante debe registrar su propia ejecución y las ampliaciones realizadas.

**Solución razonada y errores que debes interpretar:** El gestor de contexto with cierra el archivo incluso si se produce una excepción. El programa distingue error de lectura, estructura inválida y dato fuera de rango. Una salida parcial se identifica o se evita según el contrato; no se presenta como un informe completo.

**Entregable:** Lector, exportador y tabla de errores de E/S.

**Aceptación del reto:** La exportación conserva datos válidos y los errores producen una salida clara y un estado coherente.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha utilizado la consola para realizar operaciones de entrada y salida de información. | Lector, exportador y tabla de errores de E/S; apartado a con datos, explicación o salida referida expresamente a ese criterio. La exportación conserva datos válidos y los errores producen una salida clara y un estado coherente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han aplicado formatos en la visualización de la información. | Lector, exportador y tabla de errores de E/S; apartado b con datos, explicación o salida referida expresamente a ese criterio. La exportación conserva datos válidos y los errores producen una salida clara y un estado coherente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han reconocido las posibilidades de entrada / salida del lenguaje y las librerías asociadas. | Lector, exportador y tabla de errores de E/S; apartado c con datos, explicación o salida referida expresamente a ese criterio. La exportación conserva datos válidos y los errores producen una salida clara y un estado coherente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han utilizado ficheros para almacenar y recuperar información. | Código y caso de entrada/salida identificado para el criterio d, incorporados a «Lector, exportador y tabla de errores de E/S». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| e | Se han creado programas que utilicen diversos métodos de acceso al contenido de los ficheros. | Código de lectura secuencial y acceso directo con seek sobre archivo temporal de registros fijos, salidas equivalentes y ensayos de índice/formato inválido. Se ejecutan ambos métodos, el índice 1 devuelve el segundo registro y se rechazan índice fuera de rango y bloque incompleto. Una explicación sin programas ejecutados deja CE5.e pendiente. |

<a id="ra6"></a>
## RA6 · Crear objetos que mantengan invariantes

**Enunciado oficial:** Desarrolla programas organizados en clases analizando y aplicando los principios de la programación orientada a objetos.

Clases, propiedades, métodos y constructores organizan comportamiento alrededor de datos. La herencia debe conservar el contrato esperado y no sustituye a una decisión de modelo. Los mecanismos de visibilidad de Python tienen alcance de lenguaje, no permisos del SO.

### Actividad CMO-316-RA6-A1

1. Define Activo con código obligatorio y estado limitado.
2. Añade un método de cambio de estado y comprueba una transición no admitida.
3. Instancia varios objetos y verifica que no comparten accidentalmente una lista mutable de clase.
4. Crea una subclase sencilla y justifica qué hereda y qué especializa.

**Solución razonada y errores que debes interpretar:** Una lista definida como atributo de clase puede compartirse entre instancias; para estado individual se inicializa en cada objeto. Las pruebas deben mostrar esa diferencia y que una especialización respeta las operaciones previstas por el tipo base.

**Entregable:** Clases, instancias y ensayos de invariantes/herencia.

**Aceptación del reto:** El estado es consistente y los objetos independientes no se contaminan por atributos compartidos involuntariamente.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha reconocido la sintaxis, estructura y componentes típicos de una clase. | Clases, instancias y ensayos de invariantes/herencia; apartado a con datos, explicación o salida referida expresamente a ese criterio. El estado es consistente y los objetos independientes no se contaminan por atributos compartidos involuntariamente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han definido clases. | Código y caso de entrada/salida identificado para el criterio b, incorporados a «Clases, instancias y ensayos de invariantes/herencia». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| c | Se han definido propiedades y métodos. Se han creado constructores. | Clases, instancias y ensayos de invariantes/herencia; apartado c con datos, explicación o salida referida expresamente a ese criterio. El estado es consistente y los objetos independientes no se contaminan por atributos compartidos involuntariamente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han desarrollado programas que instancien y utilicen objetos de las clases creadas anteriormente. Se han utilizado mecanismos para controlar la visibilidad de las clases y de sus miembros. | Código y caso de entrada/salida identificado para el criterio d, incorporados a «Clases, instancias y ensayos de invariantes/herencia». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| e | Se han definido y utilizado clases heredadas. | Código y caso de entrada/salida identificado para el criterio e, incorporados a «Clases, instancias y ensayos de invariantes/herencia». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |

## Ejemplo local ejecutable

El archivo [funciones_inventario.py](ejemplos/funciones_inventario.py) contiene funciones sin E/S de archivos. Desde la raíz del repositorio:

```bash
python3 optativas/CMO-316-programacion-python/ejemplos/funciones_inventario.py
```

La salida conserva los códigos 0012/0040 como texto, muestra una lista sin cambios después de reasignar el parámetro y con un segundo elemento después de mutarla. Importa las funciones en tu entorno y añade casos de código duplicado, cantidad negativa y booleano usado como cantidad. Explica por qué el contrato usa type(cantidad) is int para excluir bool, aunque en Python bool sea una subclase de int. La demostración no sustituye los programas de archivos o clases de otros RA; éstos requieren sus propios artefactos.

## Dossier final y autoevaluación

Reúne las actividades por RA y enlaza cada CE con el artefacto concreto que lo demuestra. Una memoria extensa sin resultados identificables no sustituye las pruebas; una configuración que funciona por casualidad debe revisarse con casos de límite y recuperación. Explica las dependencias y qué haría falta para repetir el trabajo en otro equipo.

Como rúbrica de práctica se propone valorar corrección técnica (40 %), evidencia y pruebas (30 %), explicación de decisiones (20 %) y documentación/revisión (10 %). Es una propuesta propia: los instrumentos, ponderaciones y calificaciones oficiales corresponden al centro. Los CE no ejecutados o sin medios disponibles se anotan pendientes, sin inventar una adquisición del RA.

## Referencias y datos de trazabilidad

- [Matriz completa de este módulo](alineacion-ra.json).
- [Referentes normativos del repositorio](../../recursos/ra/referentes-oficiales.json).
- [Tutorial de Python](https://docs.python.org/3/tutorial/).
- [Python: paso de argumentos](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).
