# 03 · Prácticas de administración y recuperación

[Volver al módulo](README.md) · [Consultar diagnóstico](04-diagnostico-y-evaluacion.md)

Todas las modificaciones se realizan en VM de laboratorio con datos ficticios. Las duraciones y ponderaciones son propuestas didácticas. Documenta resultados reales: si no dispones de un recurso o licencia, declara la parte pendiente y no fabriques capturas.

## Práctica 1 · Instalación comparada Debian y Windows

**Nivel inicial · 4–6 horas.** Prepara dos puestos virtuales para tareas de oficina y administración básica. El objetivo no es avanzar rápidamente por los asistentes: hay que justificar recursos, arranque, almacenamiento, cuentas y recuperación.

### Preparación y procedimiento

1. Comprueba recursos del anfitrión, virtualización disponible, espacio físico libre y medios oficiales. Registra versión del hipervisor y nombre de las imágenes. Verifica la imagen por el procedimiento publicado por cada proveedor.
2. Crea las VM por separado con un único disco virtual vacío en cada una. Define firmware UEFI y requisitos de cada SO. Elabora un esquema antes de instalar.
3. Instala Debian 13 con usuario ordinario y un conjunto de paquetes coherente. Revisa cada confirmación de escritura en disco. Anota el modelo de administración elegido para root y sudo.
4. Instala Windows 11 Pro con edición y canal legítimos, cumpliendo requisitos. Registra las particiones creadas por el instalador sin borrar ninguna después para simplificar una captura.
5. Instala herramientas oficiales del hipervisor cuando proceda. Actualiza, reinicia y confirma dispositivos, hora y conectividad. No expongas servicios entrantes en la red del centro.
6. Obtén inventarios con los comandos de la guía. Relaciona disco, particiones, sistemas de archivos y punto de montaje o letra.
7. Crea un archivo ficticio, realiza una copia externa al disco de la VM por el mecanismo del laboratorio y prueba su restauración. Conserva un punto de recuperación de configuración.
8. Ejecuta una aplicación de prueba y documenta apagado, arranque y recuperación del entorno.

### Resultado esperado y pruebas

Ambos sistemas arrancan desde sus discos, detectan recursos asignados, pueden actualizarse y permiten usar una cuenta ordinaria. El alumno explica qué partición participa en el arranque, cuál contiene datos y por qué el snapshot no sustituye la copia.

Si un instalador no ve el disco, revisa controlador virtual y medio antes de eliminar particiones. Si Windows no cumple requisitos, corrige la configuración admitida o marca la instalación pendiente; no conviertas la práctica en una elusión de restricciones.

### Entregables y rúbrica

Entrega diagrama de VM, tabla comparativa, comandos de inventario con interpretación, comprobación de actualizaciones y evidencia de restauración. Ponderación: planificación 20 %, instalación justificada 30 %, verificación 30 % y documentación 20 %. Es obligatorio identificar el disco de destino antes de escribir.

## Práctica 2 · Acceso mínimo con usuarios y grupos

**Nivel intermedio · 3–4 horas.** Una oficina ficticia tiene dos funciones: edición y consulta. Los editores deben crear y modificar documentos; los visitantes deben leer los documentos autorizados sin cambiarlos. Otros usuarios no deben acceder.

### Diseño previo

Construye una matriz con identidad, grupo, recurso y operaciones `listar`, `leer`, `crear`, `modificar` y `eliminar`. Distingue los requisitos del modelo técnico disponible. En POSIX básico, crear o eliminar nombres en un directorio depende de permisos de ese directorio; no se consigue cualquier combinación por cambiar solo el archivo.

### Procedimiento Linux

1. Usa cuentas ficticias y un grupo de taller inexistentes al iniciar. Crea el directorio dedicado siguiendo la guía técnica.
2. Aplica permisos de grupo y setgid para el espacio colaborativo. Establece una umask apropiada al crear archivos.
3. Prueba lectura, escritura y eliminación con `sudo -u` para cada identidad. Registra también `id` y permisos del camino.
4. Introduce intencionalmente un permiso demasiado restrictivo sobre un archivo de prueba. Reproduce el error, localiza la capa y corrígelo con el menor cambio.
5. Como ampliación, usa ACL para conceder lectura a un visitante sin incorporarlo al grupo editor. Revisa la máscara efectiva y compara resultado esperado y observado. No uses `chmod 777`.

### Procedimiento Windows

1. Crea cuentas y grupos locales ficticios desde una consola autorizada. Utiliza la carpeta exclusiva indicada en la guía, sobre NTFS.
2. Conserva administración y SYSTEM, revisa herencia y asigna derechos por grupos.
3. Prueba cada operación desde sesiones ordinarias, no únicamente desde PowerShell elevado. Cierra sesión tras cambiar pertenencias.
4. Consulta Acceso efectivo y contrasta con una prueba real. Introduce y corrige una herencia no deseada únicamente en la carpeta de laboratorio.

### Resultado, reversión y entregables

La entrega debe mostrar que los accesos permitidos funcionan y los prohibidos son denegados. Si un resultado difiere, explica qué identidad, herencia o ACL intervenía. La reversión consiste en restaurar el punto de laboratorio después de exportar evidencias, evitando eliminar perfiles a ciegas.

Entrega matriz de accesos, decisiones POSIX/NTFS, resultados y explicación de diferencias. Rúbrica: diseño 25 %, implementación 25 %, pruebas positivas y negativas 35 %, documentación 15 %. Conceder derechos excesivos para hacer pasar la prueba invalida la solución hasta que se corrija.

## Práctica 3 · Incidencia, copia y restauración comprobada

**Nivel avanzado · 3–5 horas.** Un usuario ficticio informa de pérdida de un documento y de una tarea automática que parece completarse, pero no deja una copia utilizable. El docente prepara solo fallos reversibles sobre archivos de práctica.

### Procedimiento

1. Crea un pequeño conjunto de datos, incluida una subcarpeta y dos versiones de un documento. Guarda un manifiesto de nombres, tamaños y sumas SHA-256.
2. Realiza una copia usando una herramienta apropiada y registra código de salida. Coloca el artefacto en destino independiente mediante el mecanismo aprobado del laboratorio.
3. Restaura primero en una ubicación separada. Compara contenido, estructura y los metadatos que el plan exige conservar. Un archivo comprimido que puede listarse todavía no demuestra una restauración completa.
4. El docente altera o retira una copia de trabajo ficticia, conservando la copia válida. Recupera la versión solicitada sin reemplazar versiones posteriores que deban mantenerse.
5. Programa la operación de prueba con una identidad limitada. Registra rutas absolutas, directorio de inicio, horario y ubicación de logs.
6. Introduce una causa reversible de fallo: una ruta inexistente o un permiso insuficiente en el destino dedicado. Reproduce mediante el programador, investiga su historial y corrige la causa. No cambies privilegios de todo el sistema.
7. Comprueba una nueva ejecución programada y otra restauración. Mide tiempo real y compáralo con la necesidad de recuperación del escenario.

### Resultado y entregables

El informe diferencia recuperar un archivo, recuperar permisos y recuperar el equipo entero. Explica cuánto trabajo podría perderse entre copias y cuánto se tardó en restaurar. Incluye la versión pedida, evidencia de igualdad de contenido, registros de fallo y éxito y una propuesta de retención.

Rúbrica: diseño de copia 20 %, preservación y restauración 35 %, diagnóstico de tarea 30 % y documentación 15 %. No se acepta una captura de “tarea finalizada” sin comprobar datos. El ejercicio termina con la VM recuperable y los datos ficticios claramente identificados.

## Plantilla de registro de cambios

| Campo | Contenido esperado |
| --- | --- |
| Estado inicial | Versión, recurso afectado y síntoma reproducido |
| Hipótesis | Explicación que puede refutarse con una prueba |
| Cambio | Comando o acción exacta, identidad y alcance |
| Verificación | Prueba que confirma el resultado y una regresión relacionada |
| Reversión | Punto de recuperación o acción concreta comprobada |
| Limitaciones | Qué no se midió o no pudo verificarse |
