# CMO-313 · Fundamentos de programación

[Catálogo de optativas](../README.md) · [Índice general](../../README.md)

## Aplicabilidad y forma de estudio

La tabla del catálogo fija 50 horas para este módulo específico de Informática y Comunicaciones. Su ubicación en primero se deduce del encaje con las optativas de SMR (50/90 horas); no se presenta como una columna de curso expresamente asignada a IFC en el catálogo. Deben confirmarse la oferta y las condiciones del centro.

El currículo de referencia es la [Orden 3536/2025](https://www.bocm.es/boletin/CM_Orden_BOCM/2025/08/27/BOCM-20250827-5.PDF), Anexo II, CMO-313; BOCM página 191 y siguientes; PDF páginas 174–175. La relación aplicable se contrasta con la [Orden 3822/2026](https://www.bocm.es/boletin/CM_Orden_BOCM/2026/09/25/BOCM-20260925-20.PDF). El catálogo permite una oferta; no demuestra que un centro imparta todas estas materias ni que un alumno deba cursarlas simultáneamente.

Los enunciados de RA y los CE de las tablas se transcriben del referente normativo. Las explicaciones, retos, soluciones y condiciones de aceptación son propuestas didácticas propias. La evidencia esperada se diferencia de lo observado: completa resultados reales en una copia de la plantilla de seguimiento.

## Preparación

Revisa el [laboratorio común](../../docs/laboratorio.md) y trabaja con datos sintéticos y un entorno identificado. Antes de modificar, registra versión, estado inicial y recuperación. Las tareas que necesitan hardware, motor de juego o plataforma administrada deben ejecutarse en esos medios para aportar evidencia completa; la preparación escrita conserva su valor y se marca como pendiente de esa ejecución.

## Ruta por resultados de aprendizaje

<a id="ra1"></a>
## RA1 · Leer la estructura de una aplicación de inventario

**Enunciado oficial:** Reconoce la estructura de un programa informático, identificando y relacionando los elementos propios del lenguaje de programación utilizado.

Un programa tiene entradas, transformaciones, salidas y tratamiento de errores. Reconocer tipos, operadores y conversiones permite anticipar resultados, mientras el IDE ayuda a navegar y depurar sin sustituir la comprensión del código.

### Actividad CMO-313-RA1-A1

1. Crea un proyecto local con archivo principal y una breve descripción de entradas/salidas.
2. Declara un código de activo, una cantidad entera y un precio; distingue variable, literal y constante por convenio.
3. Evalúa expresiones y conversiones de texto a número, incluyendo una entrada inválida.
4. Usa el depurador para observar valores y añade comentarios que expliquen decisiones.

**Solución razonada y errores que debes interpretar:** La cadena "12" no es automáticamente el entero 12 en todas las operaciones. Una conversión explícita necesita validar la entrada y tratar el error. Los comentarios aclaran propósito y supuestos, sin repetir cada línea con palabras.

**Entregable:** Proyecto, tabla de tipos y traza del depurador.

**Aceptación del reto:** La persona explica estructura, valor y tipo de cada expresión y reproduce el caso de conversión inválida.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han identificado los bloques que componen la estructura de un programa informático. | Proyecto, tabla de tipos y traza del depurador; apartado a con datos, explicación o salida referida expresamente a ese criterio. La persona explica estructura, valor y tipo de cada expresión y reproduce el caso de conversión inválida. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han creado proyectos de desarrollo de aplicaciones. | Proyecto, tabla de tipos y traza del depurador; apartado b con datos, explicación o salida referida expresamente a ese criterio. La persona explica estructura, valor y tipo de cada expresión y reproduce el caso de conversión inválida. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han utilizado entornos integrados de desarrollo. | Proyecto, tabla de tipos y traza del depurador; apartado c con datos, explicación o salida referida expresamente a ese criterio. La persona explica estructura, valor y tipo de cada expresión y reproduce el caso de conversión inválida. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han identificado los distintos tipos de variables y la utilidad específica de cada uno. | Código y caso de entrada/salida identificado para el criterio d, incorporados a «Proyecto, tabla de tipos y traza del depurador». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| e | Se ha modificado el código de un programa para crear y utilizar variables. | Código y caso de entrada/salida identificado para el criterio e, incorporados a «Proyecto, tabla de tipos y traza del depurador». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| f | Se han creado y utilizado constantes y literales. | Proyecto, tabla de tipos y traza del depurador; apartado f con datos, explicación o salida referida expresamente a ese criterio. La persona explica estructura, valor y tipo de cada expresión y reproduce el caso de conversión inválida. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| g | Se han clasificado, reconocido y utilizado en expresiones los operadores del lenguaje. | Proyecto, tabla de tipos y traza del depurador; apartado g con datos, explicación o salida referida expresamente a ese criterio. La persona explica estructura, valor y tipo de cada expresión y reproduce el caso de conversión inválida. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| h | Se ha comprobado el funcionamiento de las conversiones de tipo explícitas e implícitas. | Proyecto, tabla de tipos y traza del depurador; apartado h con datos, explicación o salida referida expresamente a ese criterio. La persona explica estructura, valor y tipo de cada expresión y reproduce el caso de conversión inválida. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| i | Se han introducido comentarios en el código. | Código y caso de entrada/salida identificado para el criterio i, incorporados a «Proyecto, tabla de tipos y traza del depurador». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |

<a id="ra2"></a>
## RA2 · Descomponer una solución en funciones

**Enunciado oficial:** Escribe y prueba programas sencillos, reconociendo y aplicando los fundamentos de la programación.

Una función recibe datos, realiza una tarea acotada y devuelve un resultado. Separar cálculo y presentación permite probar sin pedir entrada interactiva en cada caso. Importar una biblioteca requiere conocer su contrato y la versión usada.

### Actividad CMO-313-RA2-A1

1. Escribe una función que calcule el coste de un lote a partir de cantidad y precio.
2. Valida cantidad no negativa y documenta el resultado para lote vacío.
3. Llama a la función con distintos parámetros y compara resultados calculados a mano.
4. Utiliza una biblioteca estándar para formatos o fechas, explicando qué evita reimplementar.

**Solución razonada y errores que debes interpretar:** El caso de cantidad cero debe devolver cero o la respuesta definida por el contrato, no fallar por una suposición oculta. Una función que imprime pero no devuelve el dato puede servir para presentación, pero complica su reutilización en otra operación.

**Entregable:** Código de funciones, contrato y casos de entrada/salida.

**Aceptación del reto:** Se diferencian parámetros, argumentos y retorno, y los casos válidos e inválidos tienen resultado previsto.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han identificado los fundamentos de la programación. | Código de funciones, contrato y casos de entrada/salida; apartado a con datos, explicación o salida referida expresamente a ese criterio. Se diferencian parámetros, argumentos y retorno, y los casos válidos e inválidos tienen resultado previsto. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han escrito programas simples. | Código y caso de entrada/salida identificado para el criterio b, incorporados a «Código de funciones, contrato y casos de entrada/salida». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| c | Se han utilizado métodos/ funciones. | Código y caso de entrada/salida identificado para el criterio c, incorporados a «Código de funciones, contrato y casos de entrada/salida». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| d | Se han utilizado parámetros en la llamada métodos. | Código de funciones, contrato y casos de entrada/salida; apartado d con datos, explicación o salida referida expresamente a ese criterio. Se diferencian parámetros, argumentos y retorno, y los casos válidos e inválidos tienen resultado previsto. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se han incorporado y utilizado librerías. | Código de funciones, contrato y casos de entrada/salida; apartado e con datos, explicación o salida referida expresamente a ese criterio. Se diferencian parámetros, argumentos y retorno, y los casos válidos e inválidos tienen resultado previsto. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra3"></a>
## RA3 · Controlar flujo y depurar decisiones

**Enunciado oficial:** Escribe y depura código, analizando y utilizando las estructuras de control del lenguaje.

Condicionales, bucles y excepciones expresan caminos distintos del programa. Una ejecución correcta con un dato favorable no prueba los límites ni las ramas de error. Las pruebas se eligen para cubrir decisiones y terminación.

### Actividad CMO-313-RA3-A1

1. Procesa una lista de cantidades y clasifica valores válidos, cero y negativos.
2. Compara un bucle contado y otro condicionado, justificando cuándo termina.
3. Añade manejo de conversión inválida y un mensaje que identifique el registro.
4. Introduce un fallo de límite en una copia, localízalo con el depurador y conserva el cambio corrector.

**Solución razonada y errores que debes interpretar:** La captura de cualquier excepción sin informar puede ocultar errores de programación. Trata los errores previstos y deja evidencia del caso. Un continue omite una iteración y un break termina el bucle: elige según el requisito y explica su efecto.

**Entregable:** Tabla de ramas, programa y registro de corrección.

**Aceptación del reto:** Todas las ramas relevantes se ejercitan y el bucle finaliza con listas vacías y entradas de frontera.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha escrito y probado código que haga uso de estructuras de selección. | Código y caso de entrada/salida identificado para el criterio a, incorporados a «Tabla de ramas, programa y registro de corrección». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| b | Se han utilizado estructuras de repetición. | Tabla de ramas, programa y registro de corrección; apartado b con datos, explicación o salida referida expresamente a ese criterio. Todas las ramas relevantes se ejercitan y el bucle finaliza con listas vacías y entradas de frontera. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han reconocido las posibilidades de las sentencias de salto. | Tabla de ramas, programa y registro de corrección; apartado c con datos, explicación o salida referida expresamente a ese criterio. Todas las ramas relevantes se ejercitan y el bucle finaliza con listas vacías y entradas de frontera. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se ha escrito código utilizando control de excepciones. | Código y caso de entrada/salida identificado para el criterio d, incorporados a «Tabla de ramas, programa y registro de corrección». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| e | Se han creado programas ejecutables utilizando diferentes estructuras de control. | Código y caso de entrada/salida identificado para el criterio e, incorporados a «Tabla de ramas, programa y registro de corrección». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| f | Se han probado y depurado los programas. | Código y caso de entrada/salida identificado para el criterio f, incorporados a «Tabla de ramas, programa y registro de corrección». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| g | Se ha comentado y documentado el código. | Código y caso de entrada/salida identificado para el criterio g, incorporados a «Tabla de ramas, programa y registro de corrección». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |

<a id="ra4"></a>
## RA4 · Modelar activos con clases

**Enunciado oficial:** Conoce los fundamentos de la programación orientada a objetos.

Una clase agrupa estado y operaciones relacionadas; no hace falta convertir todo en una jerarquía. La herencia se justifica si existe una relación que conserve el contrato; la composición puede resultar más sencilla para asociar componentes.

### Actividad CMO-313-RA4-A1

1. Define Activo con código y estado, validando los valores en su construcción.
2. Añade una operación de retirada que respete una regla de negocio sencilla.
3. Crea una especialización sólo si añade una conducta coherente, y compárala con composición.
4. Explica la política de acceso a atributos del lenguaje utilizado y sus límites reales.

**Solución razonada y errores que debes interpretar:** En Python un prefijo de guion bajo expresa una convención y no constituye una barrera de seguridad del sistema. El ejemplo debe proteger invariantes mediante su diseño y pruebas, sin presentar convenciones como permisos de usuario.

**Entregable:** Clases, diagrama breve y casos de invariantes.

**Aceptación del reto:** Los objetos válidos se crean, los estados imposibles se rechazan y la herencia no rompe el comportamiento esperado.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han definido y utilizado clases adecuadamente. | Código y caso de entrada/salida identificado para el criterio a, incorporados a «Clases, diagrama breve y casos de invariantes». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| b | Se ha conocido el concepto de herencia y su utilización | Clases, diagrama breve y casos de invariantes; apartado b con datos, explicación o salida referida expresamente a ese criterio. Los objetos válidos se crean, los estados imposibles se rechazan y la herencia no rompe el comportamiento esperado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han diferenciado las condiciones de acceso a los atributos y métodos que definen una clase. | Clases, diagrama breve y casos de invariantes; apartado c con datos, explicación o salida referida expresamente a ese criterio. Los objetos válidos se crean, los estados imposibles se rechazan y la herencia no rompe el comportamiento esperado. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra5"></a>
## RA5 · Intercambiar datos sin perder su significado

**Enunciado oficial:** Realiza operaciones de entrada y salida de información utilizando ficheros usando las librerías o clases que ofrece el lenguaje de programación.

Texto, CSV y JSON tienen convenciones de codificación y estructura. Leer un archivo también implica decidir qué hacer con campos ausentes, tipos incorrectos y filas duplicadas. La ruta de salida se elige sin sobrescribir datos ajenos.

### Actividad CMO-313-RA5-A1

1. Crea un CSV sintético con código y cantidad y un JSON equivalente.
2. Lee ambos con la biblioteca adecuada, especificando UTF-8 y separador.
3. Valida estructura y muestra un informe por consola sin modificar los originales.
4. Ensaya archivo inexistente, dato mal formado y número inválido; conserva mensajes claros.

**Solución razonada y errores que debes interpretar:** Separar por comas mediante una operación de cadena no sustituye siempre al parser CSV, porque puede haber campos citados y separadores dentro del texto. El programa debe conservar identificadores con ceros iniciales y no tratarlos como cantidades.

**Entregable:** Archivos de intercambio, lector y reporte de errores.

**Aceptación del reto:** Se conservan tipos y códigos, y los errores de entrada no producen un informe aparentemente válido.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha utilizado la consola para realizar operaciones de entrada y salida de información. | Archivos de intercambio, lector y reporte de errores; apartado a con datos, explicación o salida referida expresamente a ese criterio. Se conservan tipos y códigos, y los errores de entrada no producen un informe aparentemente válido. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han aplicado formatos en la visualización de la información. | Archivos de intercambio, lector y reporte de errores; apartado b con datos, explicación o salida referida expresamente a ese criterio. Se conservan tipos y códigos, y los errores de entrada no producen un informe aparentemente válido. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han reconocido las posibilidades de entrada / salida del lenguaje y las librerías asociadas. | Archivos de intercambio, lector y reporte de errores; apartado c con datos, explicación o salida referida expresamente a ese criterio. Se conservan tipos y códigos, y los errores de entrada no producen un informe aparentemente válido. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han utilizado ficheros para almacenar y recuperar información. | Código y caso de entrada/salida identificado para el criterio d, incorporados a «Archivos de intercambio, lector y reporte de errores». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| e | Se han creado programas que utilicen ficheros distintos formatos. | Código y caso de entrada/salida identificado para el criterio e, incorporados a «Archivos de intercambio, lector y reporte de errores». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |

<a id="ra6"></a>
## RA6 · Conectar código y base relacional con integridad

**Enunciado oficial:** Gestiona información almacenada en bases de datos relacionales manteniendo la integridad y la consistencia de los datos.

El programa debe separar sentencias y datos mediante parámetros. La base conserva restricciones, y las transacciones mantienen consistencia entre operaciones relacionadas. La prueba en memoria permite estudiar el contrato sin alterar una base de trabajo.

### Actividad CMO-313-RA6-A1

1. Conecta una base nueva o en memoria y crea la tabla de activos con clave única.
2. Implementa alta, consulta y actualización usando parámetros.
3. Prueba código duplicado y una modificación que deba deshacerse.
4. Cierra recursos y documenta qué estado queda después de cada operación.

**Solución razonada y errores que debes interpretar:** Concatenar texto recibido en una sentencia confunde código SQL y datos. Una consulta parametrizada evita esa construcción y simplifica valores con caracteres especiales. La validación de negocio y las restricciones de la base siguen siendo necesarias.

**Entregable:** Aplicación de gestión mínima, consultas y ensayo de rollback.

**Aceptación del reto:** Las operaciones válidas funcionan, las violaciones se rechazan y una transacción fallida no deja cambios parciales.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han identificado las características y métodos de acceso a sistemas gestores de bases de datos relacionales. | Aplicación de gestión mínima, consultas y ensayo de rollback; apartado a con datos, explicación o salida referida expresamente a ese criterio. Las operaciones válidas funcionan, las violaciones se rechazan y una transacción fallida no deja cambios parciales. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han programado conexiones con bases de datos. | Código y caso de entrada/salida identificado para el criterio b, incorporados a «Aplicación de gestión mínima, consultas y ensayo de rollback». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| c | Se ha escrito código para almacenar información en bases de datos. | Código y caso de entrada/salida identificado para el criterio c, incorporados a «Aplicación de gestión mínima, consultas y ensayo de rollback». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| d | Se han creado programas para recuperar y mostrar información almacenada en bases de datos. | Código y caso de entrada/salida identificado para el criterio d, incorporados a «Aplicación de gestión mínima, consultas y ensayo de rollback». La operación de programación indicada se explica y se reproduce con un caso normal y uno de límite o error, según el contrato del programa. |
| e | Se han efectuado borrados y modificaciones sobre la información almacenada. | Aplicación de gestión mínima, consultas y ensayo de rollback; apartado e con datos, explicación o salida referida expresamente a ese criterio. Las operaciones válidas funcionan, las violaciones se rechazan y una transacción fallida no deja cambios parciales. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| f | Se han creado aplicaciones que ejecuten consultas sobre bases de datos. | Aplicación de gestión mínima, consultas y ensayo de rollback; apartado f con datos, explicación o salida referida expresamente a ese criterio. Las operaciones válidas funcionan, las violaciones se rechazan y una transacción fallida no deja cambios parciales. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| g | Se han creado aplicaciones para posibilitar la gestión de información presente en bases de datos relacionales. | Aplicación de gestión mínima, consultas y ensayo de rollback; apartado g con datos, explicación o salida referida expresamente a ese criterio. Las operaciones válidas funcionan, las violaciones se rechazan y una transacción fallida no deja cambios parciales. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

## Dossier final y autoevaluación

Reúne las actividades por RA y enlaza cada CE con el artefacto concreto que lo demuestra. Una memoria extensa sin resultados identificables no sustituye las pruebas; una configuración que funciona por casualidad debe revisarse con casos de límite y recuperación. Explica las dependencias y qué haría falta para repetir el trabajo en otro equipo.

Como rúbrica de práctica se propone valorar corrección técnica (40 %), evidencia y pruebas (30 %), explicación de decisiones (20 %) y documentación/revisión (10 %). Es una propuesta propia: los instrumentos, ponderaciones y calificaciones oficiales corresponden al centro. Los CE no ejecutados o sin medios disponibles se anotan pendientes, sin inventar una adquisición del RA.

## Referencias y datos de trazabilidad

- [Matriz completa de este módulo](alineacion-ra.json).
- [Referentes normativos del repositorio](../../recursos/ra/referentes-oficiales.json).
- [Tutorial de Python](https://docs.python.org/3/tutorial/).
- [SQLite: transacciones](https://www.sqlite.org/lang_transaction.html).
