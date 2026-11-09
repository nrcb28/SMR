# 7. Operación, automatización y recuperación de sistemas en red

[Índice del módulo](README.md) · [Permisos y capacidad](06-linux-permisos-y-capacidad.md) · [Prácticas avanzadas](08-laboratorios-y-casos-resueltos.md)

## 7.1 Administrar un servicio durante todo su ciclo de vida

Instalar un servidor es una fase breve de su vida. Después hay que saber quién lo administra, qué datos mantiene, cómo cambia, qué versiones ejecuta y cómo se recupera. Una operación repetible parte de un catálogo de servicios con propietario, consumidores, dependencias, estado esperado, ventana de mantenimiento y procedimiento de escalado. En una pequeña empresa una misma persona puede desempeñar varios papeles, pero las decisiones siguen necesitando responsables identificados.

Para `srv01`, diferencia el servicio de archivos del acceso administrativo. Que Samba esté disponible no significa que SSH deba aceptar cualquier usuario; que un administrador pueda entrar no demuestra que una cuenta lectora tenga los permisos previstos. El inventario debe registrar protocolos de cliente, nombres, puertos, identidades y rutas de datos. Relaciona cada monitor con la función que representa: proceso activo, listener correcto, consulta de prueba, lectura autorizada y restauración son niveles distintos de evidencia.

Una ficha útil permite que otra persona localice el archivo efectivo de configuración y el mecanismo de arranque. En Debian, `systemctl cat smbd` muestra la unidad y sus cambios locales; `testparm -s` ayuda a examinar la configuración Samba interpretada. En Windows, los roles instalados, servicios, objetos de AD y vínculos GPO se documentan por separado. No conviertas un exportado masivo del directorio en sustituto de una explicación de diseño.

## 7.2 Cambios controlados y evidencia mínima

Cada cambio tiene un estado previo, un objetivo y un criterio de retorno. Antes de modificar una ACL, guarda sus metadatos; antes de cambiar configuración de un servicio, conserva la versión anterior y conoce cómo validar sintaxis; antes de actualizar una aplicación dependiente de directorio, comprueba su compatibilidad y la recuperación. La copia debe poder localizarse y leerse cuando el servicio que estás cambiando falle.

Una solicitud de cambio de laboratorio puede expresarse así: «Permitir que el grupo lector consulte Manuales sin modificar documentos». El alcance incluye grupo, recurso Samba, directorio y pruebas desde cliente. El cambio queda aceptado si un lector abre un archivo, no puede guardarlo ni crear otro y el grupo editor sigue trabajando. El retorno consiste en reponer las ACL y configuración guardadas, no en otorgar permisos a todos.

Una prueba debe distinguir resultado esperado y observado. Si el estudiante no ha ejecutado todavía la comprobación, la columna real permanece pendiente. No se genera evidencia por copiar una salida de esta guía. Registra comando, máquina, identidad, momento y conclusión. Un mensaje de éxito sin identificar el contexto puede corresponder a la sesión administrativa que invalida la prueba de autorización.

## 7.3 Automatizar no equivale a repetir órdenes sin revisión

La automatización útil valida entradas, restringe ámbito, calcula una propuesta, aplica cambios cuando corresponde y comprueba el resultado. Un archivo CSV no se considera confiable sólo por estar en el repositorio; puede tener delimitador incorrecto, campos vacíos, duplicados o un grupo distinto del previsto. Si un script interpreta texto como código, además de errores de datos aparecen riesgos de ejecución. Usa parámetros estructurados de cmdlets y valida las cadenas que forman identificadores.

Distingue tres niveles de ensayo. El primero valida archivos sin conectarse a ningún sistema. El segundo consulta el directorio y compara estado deseado y existente. El tercero modifica objetos bajo una autorización, con alcance acotado y reversión. El ejemplo incluido se limita a los dos primeros; no contiene órdenes de creación ni un interruptor que convierta una revisión en ejecución masiva.

El [CSV de altas sintéticas](ejemplos/altas-lab.csv) contiene tres personas ficticias. El [generador de plan](ejemplos/plan-altas-lab.ps1) comprueba columnas, alias, nombres, prefijo de grupo y duplicados. Su ejecución sin consultas no requiere el módulo ActiveDirectory. Desde la raíz del repositorio:

```powershell
& '.\segundo\sistemas-operativos-en-red\ejemplos\plan-altas-lab.ps1' `
    -Csv '.\segundo\sistemas-operativos-en-red\ejemplos\altas-lab.csv' | Format-Table
```

El resultado es una lista de propuestas que se revisan; no crea cuentas. Si se copia a una estación con RSAT, conectada únicamente al dominio ficticio, se puede solicitar la consulta opcional:

```powershell
& '.\segundo\sistemas-operativos-en-red\ejemplos\plan-altas-lab.ps1' `
    -Csv '.\segundo\sistemas-operativos-en-red\ejemplos\altas-lab.csv' `
    -ConsultarDirectorio | Format-Table
```

El script utiliza explícitamente `dc01.ad.aula.test` y verifica el nombre del dominio antes de buscar usuarios. No debe adaptarse a un dominio real sin una revisión de diseño, permisos y tratamiento de datos. Las contraseñas no aparecen en el CSV. Si se implementa posteriormente una fase de aplicación, se preparan credenciales por un canal apropiado y se prueba primero una única cuenta deshabilitada.

## 7.4 Idempotencia, errores parciales y retirada

Una operación idempotente puede repetirse manteniendo el estado deseado, en lugar de duplicar objetos o acumular permisos. Para un alta, «si existe, continuar» no es suficiente: hay que comprobar que el objeto existente es el esperado y que sus atributos coinciden. Una cuenta homónima ajena al lote no se reutiliza sin investigación. Para un grupo, la pertenencia que se desea añadir no debe borrar otras pertenencias legítimas.

Un lote puede fallar en su quinta fila después de cuatro cambios. El informe debe indicar qué se hizo, qué falló y qué quedó pendiente. No se vuelve a ejecutar todo sin conocer el estado parcial. Un diseño de aplicación suele separar validación completa, plan, ejecución y comprobación; además guarda identificadores estables de los objetos creados, de modo que una retirada no dependa únicamente de nombres que puedan haber cambiado.

La baja de una cuenta requiere más que borrarla. Deshabilitar impide usos futuros según la aplicación de esa decisión y sus sesiones; la retirada de sesiones, permisos, datos, tareas programadas y titularidad de documentos requiere operaciones específicas. En un laboratorio, documenta el orden y la verificación. En una organización, la conservación o eliminación de datos depende de la política y obligaciones aplicables, no del deseo de dejar el directorio vacío.

Un plan de retirada seguro identifica sólo objetos del ejercicio. No uses un filtro amplio de OU para borrar todos sus usuarios como limpieza automática. Si la OU puede contener trabajo de otra persona o actividad, revisa uno por uno los identificadores y dependencias. El objetivo didáctico es demostrar control del ciclo de vida, no automatizar borrados de gran alcance.

## 7.5 Copias de un servidor de archivos

Una copia útil conserva contenido y los metadatos necesarios para recuperar el servicio: propietarios, ACL, atributos extendidos cuando se utilicen, configuración y relación con identidades. Guardar únicamente archivos puede restaurar documentos sin la autorización correcta; guardar sólo ACL no recupera los documentos. Diseña una prueba en la que una segunda ruta reciba la restauración y se compruebe tanto el hash como el acceso desde un cliente.

En un recurso POSIX nuevo, puedes archivar datos con una herramienta que soporte los metadatos del diseño. Antes de elegir opciones, lee el manual instalado y verifica el tipo de destino. Un archivo de backup almacenado dentro del árbol que se copia puede crecer recursivamente o quedar incluido accidentalmente. Un destino en el mismo volumen no protege frente a la pérdida completa de ese volumen.

Conserva hashes de archivos sintéticos antes de la copia, sin tratar ese listado como prueba de autenticidad si cualquiera puede modificarlo. El hash compara contenido contra una referencia; para una referencia de confianza se necesitan controles adicionales. Después de restaurar, compara tamaños y hashes, consulta propietarios numéricos y ACL y realiza lectura/escritura por roles. La prueba administrativa de `ls` no sustituye a la operación SMB que verá el usuario.

También deben existir copias de configuración y una descripción del orden de reconstrucción. Si el servicio depende de usuarios locales o de un mapeo de identidades, recuperarlos coherentemente forma parte del procedimiento. No copies `/etc/shadow` a un informe público ni incluyas secretos en un repositorio de documentación. La memoria puede explicar qué conjunto se protege sin adjuntar su contenido sensible.

## 7.6 AD: diferencias entre una copia y una recuperación válida

Un controlador de dominio mantiene datos y estado que se coordinan con otros componentes del directorio. La restauración debe utilizar herramientas y procedimientos compatibles con AD. La posibilidad técnica de volver a una instantánea de VM no convierte todas las instantáneas en un plan correcto de recuperación de dominio. Las protecciones de virtualización reducen determinados riesgos, pero no sustituyen una copia coherente ni las decisiones sobre replicas y autoridad de los datos.

En el laboratorio de un único DC, la pérdida del controlador afecta a localización, autenticación y administración del dominio. Los clientes pueden permitir ciertos inicios de sesión en caché, pero eso no equivale a disponer de los servicios de dominio. La práctica avanzada debe distinguir «el escritorio abre» de «el dominio está recuperado». Comprueba DNS, servicios de directorio, autenticación y acceso a un recurso mediante una sesión nueva.

En Windows Server, instala y utiliza la herramienta de copia que corresponda según la guía y su documentación. El estado del sistema incluye componentes relevantes para la recuperación de ese rol, pero el plan debe identificar volumen de destino, credenciales de recuperación, DSRM y compatibilidad. Antes de ensayar una restauración, aísla la red y evita que un controlador restaurado entre accidentalmente en contacto con una infraestructura real.

Una recuperación no autoritativa y una autoritativa tienen propósitos distintos en un directorio replicado. La elección depende de qué datos deben propagarse y del escenario. No se ejecutan órdenes de marcado autoritativo como receta general para «recuperar AD». La documentación oficial de recuperación del bosque organiza decisiones y secuencias que deben estudiarse antes de realizar una intervención de ese nivel.

## 7.7 Migración: mantener servicio y posibilidad de retorno

Una migración cambia el lugar, versión o arquitectura de un servicio manteniendo unas funciones y datos. Empieza con inventario y dependencias: clientes admitidos, nombres, credenciales, permisos, archivos abiertos, formatos y tareas automáticas. Un servidor nuevo con el mismo nombre no es necesariamente el mismo principal ni posee las claves o identificadores que esperan los clientes.

Prepara un piloto con datos sintéticos y un grupo reducido. Copia a un destino independiente, comprueba contenido y permisos, configura un nombre temporal y valida operaciones. Define un momento de corte y cómo evitar escrituras divergentes entre origen y destino. Una copia inicial seguida de cambios en ambos servidores produce dos historias que pueden requerir reconciliación; no se resuelve eligiendo arbitrariamente el archivo de fecha más reciente.

El criterio de retorno debe incluir datos escritos durante el piloto o el corte. Volver a encender el servidor anterior puede recuperar disponibilidad y perder trabajo reciente si no existe un plan de sincronización coherente. Registra puntos de control y aprobación antes de cada transición. Para un laboratorio pequeño puede bastar una ventana sin escrituras, verificada y comunicada, mientras que otros sistemas necesitan mecanismos de migración específicos.

La validación posterior incluye clientes distintos, lectores y editores, reinicio del servicio, resolución de nombres, tareas y backup. Una migración no termina al copiar el último byte; concluye cuando el usuario puede realizar las operaciones previstas y la nueva plataforma puede mantenerse y recuperarse. Retira el origen sólo cuando la política acordada y las pruebas lo permitan.

## 7.8 Caso completo de cambio y recuperación

Se solicita trasladar Manuales a un volumen virtual nuevo de laboratorio. El estudiante no debe modificar particiones del anfitrión. Primero identifica el disco virtual preparado y documenta capacidad, montaje y sistema de archivos. La preparación del volumen se realiza mediante el procedimiento de su plataforma, con identificación inequívoca y copia previa; este capítulo no proporciona una orden de formateo genérica que pueda aplicarse a cualquier dispositivo.

Mientras el recurso está en uso de lectura, prepara una copia inicial a una ruta temporal y contrasta datos. Acuerda una fase final sin escrituras, detén o restringe el servicio sólo en la VM dedicada y conserva el estado anterior. Completa la copia, cambia la ruta del recurso, valida `testparm`, inicia el servicio y ejecuta la matriz de permisos. Si falla una condición, vuelve a la ruta anterior conservando las nuevas escrituras para investigarlas.

La entrega incluye estado inicial/final, diferencia de configuración, catálogo de identidades, tabla de operaciones, hashes de los documentos ficticios y tiempos reales. El tiempo invertido en preparar evidencias antes del corte no se confunde con indisponibilidad. Explica qué habría ocurrido si el destino estuviera lleno, si se hubieran perdido ACL o si el cliente mantuviera una conexión anterior.

## Referencias primarias

- [Microsoft: módulo ActiveDirectory de PowerShell](https://learn.microsoft.com/powershell/module/activedirectory/).
- [Microsoft: Import-Csv](https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/import-csv).
- [Microsoft: guía de recuperación del bosque de AD](https://learn.microsoft.com/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-procedures).
- [Microsoft: recuperación inicial del bosque](https://learn.microsoft.com/windows-server/identity/ad-ds/manage/ad-forest-recovery-perform-initial-recovery).
- [GNU tar: manual](https://www.gnu.org/software/tar/manual/).
- [Samba: manuales oficiales](https://www.samba.org/samba/docs/).
