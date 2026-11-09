# CMO-310 · Fundamentos de bases de datos

[Catálogo de optativas](../README.md) · [Índice general](../../README.md)

## Aplicabilidad y forma de estudio

La tabla del catálogo fija 50 horas para este módulo específico de Informática y Comunicaciones. Su ubicación en primero se deduce del encaje con las optativas de SMR (50/90 horas); no se presenta como una columna de curso expresamente asignada a IFC en el catálogo. Deben confirmarse la oferta y las condiciones del centro.

El currículo de referencia es la [Orden 3536/2025](https://www.bocm.es/boletin/CM_Orden_BOCM/2025/08/27/BOCM-20250827-5.PDF), Anexo II, CMO-310; BOCM página 183 y siguientes; PDF páginas 166–167. La relación aplicable se contrasta con la [Orden 3822/2026](https://www.bocm.es/boletin/CM_Orden_BOCM/2026/09/25/BOCM-20260925-20.PDF). El catálogo permite una oferta; no demuestra que un centro imparta todas estas materias ni que un alumno deba cursarlas simultáneamente.

Los enunciados de RA y los CE de las tablas se transcriben del referente normativo. Las explicaciones, retos, soluciones y condiciones de aceptación son propuestas didácticas propias. La evidencia esperada se diferencia de lo observado: completa resultados reales en una copia de la plantilla de seguimiento.

## Preparación

Revisa el [laboratorio común](../../docs/laboratorio.md) y trabaja con datos sintéticos y un entorno identificado. Antes de modificar, registra versión, estado inicial y recuperación. Las tareas que necesitan hardware, motor de juego o plataforma administrada deben ejecutarse en esos medios para aportar evidencia completa; la preparación escrita conserva su valor y se marca como pendiente de esa ejecución.

## Ruta por resultados de aprendizaje

<a id="ra1"></a>
## RA1 · Elegir un gestor para el inventario del aula

**Enunciado oficial:** Reconoce los elementos de las bases de datos analizando sus funciones y valorando la utilidad de los sistemas gestores.

Un CSV facilita intercambio, pero no impone por sí solo claves, relaciones ni transacciones. Un gestor relacional coordina esas reglas y ofrece consultas; distinguir motor, esquema, cliente y archivo de datos evita atribuir al formulario la integridad de la base. Compara almacenamiento local, cliente-servidor y un servicio administrado sin suponer que todos tienen el mismo coste de operación.

### Actividad CMO-310-RA1-A1

1. Describe un aula ficticia con equipos e incidencias; identifica quién consulta y quién modifica.
2. Compara CSV, SQLite y un gestor cliente-servidor por concurrencia, tipos, recuperación y permisos.
3. Dibuja el recorrido de una consulta: cliente, motor, almacenamiento y resultado.

**Solución razonada y errores que debes interpretar:** Para una práctica individual SQLite reduce instalación y permite comprobar SQL; para varias personas con escrituras simultáneas hay que analizar el servidor, los accesos y la recuperación. La elección se justifica por requisitos, no por declarar que un producto es siempre mejor.

**Entregable:** Ficha comparativa y diagrama de componentes del SGBD.

**Aceptación del reto:** La comparación identifica al menos un límite operativo de cada opción y explica la función de motor, esquema y cliente.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han analizado los sistemas lógicos de almacenamiento y sus características. | Ficha comparativa y diagrama de componentes del SGBD; apartado a con datos, explicación o salida referida expresamente a ese criterio. La comparación identifica al menos un límite operativo de cada opción y explica la función de motor, esquema y cliente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se ha evaluado la utilidad de un sistema gestor de bases de datos. | Ficha comparativa y diagrama de componentes del SGBD; apartado b con datos, explicación o salida referida expresamente a ese criterio. La comparación identifica al menos un límite operativo de cada opción y explica la función de motor, esquema y cliente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se ha reconocido la función de cada uno de los elementos de un sistema gestor de bases de datos. | Ficha comparativa y diagrama de componentes del SGBD; apartado c con datos, explicación o salida referida expresamente a ese criterio. La comparación identifica al menos un límite operativo de cada opción y explica la función de motor, esquema y cliente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han clasificado los sistemas gestores de bases de datos. | Ficha comparativa y diagrama de componentes del SGBD; apartado d con datos, explicación o salida referida expresamente a ese criterio. La comparación identifica al menos un límite operativo de cada opción y explica la función de motor, esquema y cliente. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |

<a id="ra2"></a>
## RA2 · Crear tablas con reglas verificables

**Enunciado oficial:** Crea bases de datos definiendo su estructura y las características de sus elementos según el modelo relacional.

El diseño convierte reglas del negocio en restricciones. Un identificador no nulo y único, una referencia válida y un estado limitado son propiedades distintas. Elegir TEXT para todo permite cargar datos rápidamente, pero desplaza controles al programa y puede admitir estados imposibles.

### Actividad CMO-310-RA2-A1

1. Modela EQUIPO(id, codigo) e INCIDENCIA(id, equipo_id, estado), con datos inventados.
2. Crea las tablas en una base nueva; activa las claves foráneas si utilizas SQLite.
3. Inserta una fila válida y ensaya duplicado de código, referencia inexistente y estado no permitido.
4. Ejecuta la secuencia de asistente, editor gráfico, relaciones y DDL que sigue; guarda sus artefactos junto con los mensajes del gestor. La parte gráfica no es opcional para acreditar el CE2.f.

### Secuencia de asistente, editor de tablas y DDL (CE2.f)

Este procedimiento requiere una herramienta gráfica operativa. Una opción es LibreOffice Base con una base Firebird incrustada nueva, preparada por el centro; registra versión y motor. Si se utiliza otro gestor, ejecuta sus asistentes y editor equivalentes y adapta el dialecto. Los nombres de menús pueden variar según versión e idioma: documenta los usados. El script SQLite de esta guía comprueba SQL, pero no acredita esta actuación gráfica.

1. En una base nueva, abre **Tablas → Usar asistente para crear tabla**. Selecciona una plantilla disponible, conserva dos campos y renómbralos `ID` y `CODIGO`. Configura `ID` como entero y clave primaria; configura `CODIGO` como texto de longitud 20 y obligatorio. Guarda la tabla como `EQUIPO`. Registra las pantallas de selección de campos, tipos y clave, sin datos personales.
2. Abre `EQUIPO` en **vista Diseño** y revisa nombre, tipo, longitud, obligatoriedad y clave. Usa el editor de índices para definir unicidad en `CODIGO` cuando ese control no haya quedado configurado por el asistente. No interpretes la apariencia de un campo como una restricción efectiva: prueba después un duplicado.
3. Crea `INCIDENCIA` mediante **Crear tabla en vista Diseño** con `ID` entero y clave primaria, `EQUIPO_ID` entero obligatorio y `ESTADO` texto obligatorio. En **Herramientas → Relaciones**, añade ambas tablas y vincula `EQUIPO.ID` con `INCIDENCIA.EQUIPO_ID`. Conserva integridad referencial y una política de borrado que rechace eliminar un equipo con incidencias; registra la opción efectiva del motor.
4. Escribe el DDL equivalente de ambas tablas y compara columna por columna con el diseño gráfico. Comprueba también claves, unicidad, nulabilidad y relación; una línea dibujada no demuestra por sí sola que el motor imponga la clave foránea.
5. En **otra base nueva de ensayo**, usa **Herramientas → SQL** para ejecutar el DDL, una sentencia cada vez según el cliente. El ejemplo siguiente usa SQL compatible con Firebird. Actualiza la lista de tablas y compara su diseño con la base creada mediante asistentes/editor. No vuelvas a crear las mismas tablas sobre una base con datos anteriores.

```sql
CREATE TABLE EQUIPO (
    ID INTEGER NOT NULL PRIMARY KEY,
    CODIGO VARCHAR(20) NOT NULL UNIQUE
);
CREATE TABLE INCIDENCIA (
    ID INTEGER NOT NULL PRIMARY KEY,
    EQUIPO_ID INTEGER NOT NULL,
    ESTADO VARCHAR(16) NOT NULL,
    CONSTRAINT FK_INCIDENCIA_EQUIPO FOREIGN KEY (EQUIPO_ID) REFERENCES EQUIPO(ID),
    CONSTRAINT CK_ESTADO CHECK (ESTADO IN ('abierta', 'cerrada'))
);
```

Introduce un equipo y una incidencia válidos y repite las pruebas de código duplicado y referencia inexistente en ambas bases. El DDL añade el `CHECK` de estado: si no está presente en la primera base, documenta esa diferencia. En Firebird puedes añadirlo desde la ventana SQL mediante la sentencia siguiente, sólo después de comprobar que no existe ya y que los datos actuales cumplen la condición:

```sql
ALTER TABLE INCIDENCIA ADD CONSTRAINT CK_ESTADO
CHECK (ESTADO IN ('abierta', 'cerrada'));
```

Después ensaya un estado inválido y conserva el rechazo del motor antes de afirmar equivalencia. No basta con que el formulario limite los valores si una operación SQL directa sigue admitiéndolo.

**Evidencia exigida para CE2.f:** recorrido por asistente, revisión en editor gráfico, relación verificada, DDL ejecutado en la segunda base y tabla de equivalencias/diferencias con pruebas. Si no hay herramienta disponible o esa secuencia no se realiza, marca **CE2.f pendiente**; la ejecución del script en memoria no lo convierte en cumplido. Esta guía no afirma que LibreOffice Base se haya ejecutado durante su elaboración. Consulta la [documentación de Base](https://documentation.libreoffice.org/en/english-documentation/base/) de la versión del centro.

**Solución razonada y errores que debes interpretar:** Una clave foránea impide una incidencia para un equipo inexistente si está realmente activa. Un CHECK de estado limita valores, mientras NOT NULL impide ausencia. Las tres restricciones se prueban por separado; una captura de la tabla vacía no demuestra su funcionamiento.

**Entregable:** DDL, diagrama de tablas y registro de tres rechazos esperados.

**Aceptación del reto:** Las inserciones válidas funcionan y las tres violaciones se rechazan sin alterar el conjunto correcto.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se ha analizado el formato de almacenamiento de la información. | DDL, diagrama de tablas y registro de tres rechazos esperados; apartado a con datos, explicación o salida referida expresamente a ese criterio. Las inserciones válidas funcionan y las tres violaciones se rechazan sin alterar el conjunto correcto. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han creado las tablas y las relaciones entre ellas. | Sentencia o acción de la herramienta y su resultado real para el criterio b; DDL, diagrama de tablas y registro de tres rechazos esperados. La consulta o cambio produce las filas previstas y conserva las restricciones declaradas; la prueba de rechazo/rollback se registra cuando corresponde. |
| c | Se han seleccionado los tipos de datos adecuados. | DDL, diagrama de tablas y registro de tres rechazos esperados; apartado c con datos, explicación o salida referida expresamente a ese criterio. Las inserciones válidas funcionan y las tres violaciones se rechazan sin alterar el conjunto correcto. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han definido los campos clave en las tablas. | DDL, diagrama de tablas y registro de tres rechazos esperados; apartado d con datos, explicación o salida referida expresamente a ese criterio. Las inserciones válidas funcionan y las tres violaciones se rechazan sin alterar el conjunto correcto. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se han implantado las restricciones reflejadas en el diseño lógico. | Sentencia o acción de la herramienta y su resultado real para el criterio e; DDL, diagrama de tablas y registro de tres rechazos esperados. La consulta o cambio produce las filas previstas y conserva las restricciones declaradas; la prueba de rechazo/rollback se registra cuando corresponde. |
| f | Se han utilizado asistentes, herramientas gráficas y el lenguaje de definición de datos. | Recorrido real de asistente, editor gráfico de tablas y relaciones, más DDL ejecutado y comparación entre ambas bases de ensayo. Se comprueban las tres formas de trabajo (asistente, herramienta gráfica y DDL), tablas/relación y pruebas de integridad. Sin actuación gráfica, CE2.f queda pendiente. |

<a id="ra3"></a>
## RA3 · Consultar incluyendo equipos sin incidencias

**Enunciado oficial:** Consulta la información almacenada en una base de datos empleando asistentes, herramientas gráficas y el lenguaje de manipulación de datos.

JOIN interno devuelve coincidencias; LEFT JOIN conserva las filas de la izquierda sin coincidencia. Al contar incidencias tras una unión externa usa COUNT(incidencia.id): COUNT(*) cuenta también la fila extendida con NULL y podría asignar una incidencia inexistente.

### Actividad CMO-310-RA3-A1

1. Carga tres equipos y dos incidencias sólo para el primero.
2. Obtén los datos de una tabla y después combina equipos e incidencias mediante INNER JOIN.
3. Calcula el recuento de incidencias de todos los equipos con LEFT JOIN y agrupación.
4. Reproduce una consulta con la herramienta gráfica y compara resultados con SQL.

**Solución razonada y errores que debes interpretar:** La salida esperada para el recuento inicial es 2, 0 y 0. El JOIN interno puede omitir los dos equipos sin incidencias: eso no es pérdida de datos, sino consecuencia de la consulta. Explica NULL y evita convertirlo automáticamente en una cadena vacía.

**Entregable:** Consultas SQL y tabla de resultados esperados/obtenidos.

**Aceptación del reto:** Se mantienen los equipos sin incidencias y se distinguen los resultados de unión interna y externa.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han identificado las herramientas y sentencias para realizar consultas. | Sentencia o acción de la herramienta y su resultado real para el criterio a; Consultas SQL y tabla de resultados esperados/obtenidos. La consulta o cambio produce las filas previstas y conserva las restricciones declaradas; la prueba de rechazo/rollback se registra cuando corresponde. |
| b | Se han realizado consultas simples sobre una tabla. | Sentencia o acción de la herramienta y su resultado real para el criterio b; Consultas SQL y tabla de resultados esperados/obtenidos. La consulta o cambio produce las filas previstas y conserva las restricciones declaradas; la prueba de rechazo/rollback se registra cuando corresponde. |
| c | Se han realizado consultas sobre el contenido de varias tablas mediante composiciones internas. | Sentencia o acción de la herramienta y su resultado real para el criterio c; Consultas SQL y tabla de resultados esperados/obtenidos. La consulta o cambio produce las filas previstas y conserva las restricciones declaradas; la prueba de rechazo/rollback se registra cuando corresponde. |
| d | Se han realizado consultas sobre el contenido de varias tablas mediante composiciones externas | Sentencia o acción de la herramienta y su resultado real para el criterio d; Consultas SQL y tabla de resultados esperados/obtenidos. La consulta o cambio produce las filas previstas y conserva las restricciones declaradas; la prueba de rechazo/rollback se registra cuando corresponde. |

<a id="ra4"></a>
## RA4 · Actualizar con transacción y vuelta atrás

**Enunciado oficial:** Modifica la información almacenada en la base de datos utilizando asistentes, herramientas gráficas y el lenguaje de manipulación de datos.

Una modificación necesita condición, alcance y comprobación previa. Una transacción permite tratar varias operaciones como una unidad; no convierte una sentencia mal planteada en correcta. El respaldo sigue siendo necesario para recuperar estados que ya fueron confirmados.

### Actividad CMO-310-RA4-A1

1. Trabaja en una copia o base en memoria y consulta cuántas filas afecta la condición.
2. Inserta, actualiza y elimina sólo datos de ensayo; registra cambios de recuento.
3. Inicia una transacción de prueba, realiza una modificación y ejecuta ROLLBACK.
4. Crea una tabla de archivo a partir de una consulta y explica su diferencia con una vista.

**Solución razonada y errores que debes interpretar:** Tras ROLLBACK el estado previo debe conservarse. Si la herramienta confirma automáticamente cada sentencia, la prueba no demuestra una transacción compuesta: identifica el modo de conexión. La cláusula WHERE se revisa antes de ejecutar y los parámetros se usan para datos aportados al programa.

**Entregable:** Guion de operaciones, conteos y evidencia de rollback.

**Aceptación del reto:** El ensayo restaura el estado inicial y la modificación definitiva sólo afecta a las filas previstas.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han identificado las herramientas y sentencias para modificar el contenido de la base de datos. | Guion de operaciones, conteos y evidencia de rollback; apartado a con datos, explicación o salida referida expresamente a ese criterio. El ensayo restaura el estado inicial y la modificación definitiva sólo afecta a las filas previstas. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han insertado, borrado y actualizado datos en las tablas. | Sentencia o acción de la herramienta y su resultado real para el criterio b; Guion de operaciones, conteos y evidencia de rollback. La consulta o cambio produce las filas previstas y conserva las restricciones declaradas; la prueba de rechazo/rollback se registra cuando corresponde. |
| c | Se ha incluido en una tabla la información resultante de la ejecución de una consulta. | Guion de operaciones, conteos y evidencia de rollback; apartado c con datos, explicación o salida referida expresamente a ese criterio. El ensayo restaura el estado inicial y la modificación definitiva sólo afecta a las filas previstas. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han adoptado medidas para mantener la integridad y consistencia de la información. | Sentencia o acción de la herramienta y su resultado real para el criterio d; Guion de operaciones, conteos y evidencia de rollback. La consulta o cambio produce las filas previstas y conserva las restricciones declaradas; la prueba de rechazo/rollback se registra cuando corresponde. |

<a id="ra5"></a>
## RA5 · Transformar requisitos en modelo relacional

**Enunciado oficial:** Diseña modelos relacionales interpretando diagramas entidad/relación.

Un diagrama entidad/relación expresa entidades y cardinalidades; el esquema relacional concreta tablas, claves y restricciones. Una relación muchos-a-muchos no se resuelve duplicando columnas de texto: necesita una tabla de asociación y una regla para sus pares.

### Actividad CMO-310-RA5-A1

1. Añade técnicos y asignaciones a incidencias; decide si una incidencia puede tener varios técnicos.
2. Dibuja cardinalidades y opcionalidad antes de crear tablas.
3. Transforma el diagrama en claves primarias/foráneas y una tabla ASIGNACION si corresponde.
4. Prueba una asignación duplicada y una que refiera a un técnico inexistente.

**Solución razonada y errores que debes interpretar:** La tabla de asociación puede usar una clave compuesta por incidencia y técnico si cada pareja sólo debe existir una vez. Si se requiere historial, identifica además el evento o intervalo; esa necesidad cambia el modelo y debe documentarse.

**Entregable:** Diagrama ER, esquema relacional y dos pruebas de integridad.

**Aceptación del reto:** Cada relación del diagrama tiene una representación y las restricciones implementan las reglas declaradas.

### Criterios y evidencias

| CE | Criterio oficial | Evidencia esperada y comprobación |
| --- | --- | --- |
| a | Se han utilizado herramientas gráficas para representar el diseño lógico. | Diagrama ER, esquema relacional y dos pruebas de integridad; apartado a con datos, explicación o salida referida expresamente a ese criterio. Cada relación del diagrama tiene una representación y las restricciones implementan las reglas declaradas. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| b | Se han identificado las tablas del diseño lógico. | Diagrama ER, esquema relacional y dos pruebas de integridad; apartado b con datos, explicación o salida referida expresamente a ese criterio. Cada relación del diagrama tiene una representación y las restricciones implementan las reglas declaradas. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| c | Se han identificado los campos que forman parte de las tablas del diseño lógico. | Diagrama ER, esquema relacional y dos pruebas de integridad; apartado c con datos, explicación o salida referida expresamente a ese criterio. Cada relación del diagrama tiene una representación y las restricciones implementan las reglas declaradas. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| d | Se han analizado las relaciones entre las tablas del diseño lógico. | Diagrama ER, esquema relacional y dos pruebas de integridad; apartado d con datos, explicación o salida referida expresamente a ese criterio. Cada relación del diagrama tiene una representación y las restricciones implementan las reglas declaradas. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| e | Se han identificado los campos clave. | Diagrama ER, esquema relacional y dos pruebas de integridad; apartado e con datos, explicación o salida referida expresamente a ese criterio. Cada relación del diagrama tiene una representación y las restricciones implementan las reglas declaradas. Se comprueba la operación o explicación concreta del criterio, sin atribuir resultados que no se han observado. |
| f | Se han aplicado reglas de integridad. | Sentencia o acción de la herramienta y su resultado real para el criterio f; Diagrama ER, esquema relacional y dos pruebas de integridad. La consulta o cambio produce las filas previstas y conserva las restricciones declaradas; la prueba de rechazo/rollback se registra cuando corresponde. |

## Ejemplo local ejecutable

El archivo [inventario_en_memoria.py](ejemplos/inventario_en_memoria.py) utiliza sqlite3 de la biblioteca estándar de Python y una base en memoria. No crea archivos de datos. Desde la raíz del repositorio:

```bash
python3 optativas/CMO-310-fundamentos-bases-datos/ejemplos/inventario_en_memoria.py
```

El contrato del ejemplo exige recuentos 2,0,0, tres violaciones de integridad rechazadas y estado abierta antes/después de rollback. Relaciona cada sentencia con los RA2, RA3 y RA4 y explica por qué COUNT(i.id) conserva ceros en la unión externa. El script no sustituye los asistentes y herramientas gráficas que aparecen en los CE: ejecuta también esas operaciones en el gestor del centro; si no dispones de él, conserva esa evidencia como pendiente.

## Dossier final y autoevaluación

Reúne las actividades por RA y enlaza cada CE con el artefacto concreto que lo demuestra. Una memoria extensa sin resultados identificables no sustituye las pruebas; una configuración que funciona por casualidad debe revisarse con casos de límite y recuperación. Explica las dependencias y qué haría falta para repetir el trabajo en otro equipo.

Como rúbrica de práctica se propone valorar corrección técnica (40 %), evidencia y pruebas (30 %), explicación de decisiones (20 %) y documentación/revisión (10 %). Es una propuesta propia: los instrumentos, ponderaciones y calificaciones oficiales corresponden al centro. Los CE no ejecutados o sin medios disponibles se anotan pendientes, sin inventar una adquisición del RA.

## Referencias y datos de trazabilidad

- [Matriz completa de este módulo](alineacion-ra.json).
- [Referentes normativos del repositorio](../../recursos/ra/referentes-oficiales.json).
- [SQLite: lenguaje SQL](https://www.sqlite.org/lang.html).
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html).
