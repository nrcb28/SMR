# Retos completos por RA · Seguridad informática

[Índice del módulo](README.md) · [Matriz oficial y evidencias](09-alineacion-ra.md) · [Datos de trazabilidad](alineacion-ra.json)

Estos cinco retos desarrollan las actividades `0226-RA1-A1` a `0226-RA5-A1` y sus 39 criterios. Los RA y las letras proceden del anexo I del [RD 1691/2007](https://www.boe.es/eli/es/rd/2007/12/14/1691); los escenarios, procedimientos y condiciones de aceptación son propuestas educativas. La documentación de un plan no acredita por sí sola su ejecución o la adquisición individual de un resultado.

## Preparación, alcance y evidencia

Utiliza datos sintéticos, cuentas de laboratorio y una VM o equipo expresamente destinado al ensayo. `srv01` usa `192.168.56.10/24`, `cli01` `.20` y LAB no tiene gateway; NAT proporciona, cuando hace falta, acceso separado a fuentes oficiales. Una actividad con firewall, imagen o recuperación puede necesitar un clon específico. No apliques una política de sólo SSH/HTTPS al servidor que otra práctica utiliza para DNS, DHCP o SMB.

Guarda estado inicial, versiones, diagrama, copia previa y procedimiento de retorno. Cada evidencia identifica máquina, identidad, momento, acción y resultado real. Las capturas de claves, tokens, datos personales o configuraciones sin sanear no se incorporan al repositorio. Las pruebas se realizan sólo dentro del alcance autorizado y no utilizan malware real.

El portfolio separa `sin realizar`, `ensayado`, `evidencia disponible` y `revisión pendiente`. Esos estados organizan el trabajo, sin fijar notas oficiales. Si una condición requiere SAI, soporte extraíble u otro recurso físico que no existe, registra lo preparado y la ejecución pendiente. Un dibujo o una VM no representan automáticamente esa evidencia física.

<a id="ra1"></a>
## RA1 · 0226-RA1-A1: seguridad pasiva y comprobación del SAI

**Encargo:** justificar y verificar la protección de una pequeña sala con servidor, switch y puestos. Debes identificar información que merece protección, diferenciar medidas físicas/lógicas, seleccionar cargas para SAI y elaborar políticas de acceso y credenciales. La verificación eléctrica se limita a las operaciones permitidas por el fabricante y la supervisión del centro.

### Inspección y diseño

1. Inventa tres conjuntos de datos —manuales públicos, configuración técnica y un expediente personal ficticio— y explica consecuencias de pérdida, alteración y exposición. No recopiles expedientes reales para hacer más convincente el caso.
2. Dibuja ubicación, accesos, ventilación, canalización y recorrido de alimentación/red. Relaciona cada peligro con una medida: cerradura o control de entrada, anclaje autorizado, orden de cableado, protección ambiental y procedimiento de mantenimiento. Comprueba que las medidas no bloquean evacuación o refrigeración.
3. Distingue seguridad física y lógica con un ejemplo por amenaza. Una contraseña no evita sustraer un equipo y un armario cerrado no restringe por sí solo una cuenta remota. Relaciona las medidas con personas responsables y una forma de revisar su funcionamiento.
4. Consulta fichas de SAI y equipo. Identifica potencia activa admitida en W, capacidad aparente en VA, curva de autonomía, compatibilidad de carga y mecanismo de comunicación. No conviertas VA en W mediante un factor inventado ni deduzcas autonomía por una simple división de energía nominal de batería.

Ejemplo sintético de cargas medidas: servidor 180 W, switch 25 W y almacenamiento externo 35 W. El conjunto suma 240 W. Un SAI anunciado como 900 VA/540 W no queda dimensionado sólo porque 240 sea menor que 540: todavía hay que revisar margen, picos, batería, curva y tiempo necesario para apagar. Si el objetivo requiere siete minutos, utiliza la curva correspondiente a esa carga y estado de batería, y registra su fuente.

Protege las dependencias necesarias. Mantener encendido el servidor sin el switch que transporta la comunicación de cierre puede incumplir el diseño. Una impresora u otro dispositivo con demandas particulares sólo se conecta al SAI si el fabricante lo admite y el cálculo lo justifica.

### Verificación supervisada

Identifica modelo, baterías, alarmas y estado. Utiliza el autotest o procedimiento de prueba admitido por el fabricante, con la supervisión prevista y un plan de recuperación. No abras la fuente/SAI, manipules circuitos o improvises cortes de red eléctrica. Registra qué comprueba el ensayo: un autotest correcto aporta evidencia de funcionamiento, pero no equivale a una medida completa de autonomía a cualquier carga.

Si el SAI ofrece comunicación USB o red, configura su agente conforme al manual y prueba una señal de estado o un evento de prueba permitido. Para ensayar apagado utiliza el procedimiento supervisado sobre el equipo de prácticas, después de guardar datos. La sola instalación del agente no demuestra que detecte una condición y ejecute el cierre esperado.

Completa una matriz de ACL con lector, editor y cuenta ajena, usando el procedimiento de permisos de [Sistemas en red](../sistemas-operativos-en-red/README.md). Prueba una operación permitida y otra denegada. Redacta una política de contraseñas y recuperación con MFA cuando el sistema lo permita, credenciales únicas y custodia; explica cómo se revisa sin pedir a nadie su contraseña. Compara biometría y alternativas según necesidad, falsos rechazos/aceptaciones, revocación y datos tratados, sin captar biometría de compañeros.

**Entregables:** inventario/impacto, plano, amenazas/controles, ficha de SAI, cargas, ensayo supervisado, ACL y políticas. La aceptación de a)–i) requiere distinguir cálculo, inspección y prueba real. Si no se dispone de SAI, la selección puede estar documentada y su funcionamiento permanece pendiente.

<a id="ra2"></a>
## RA2 · 0226-RA2-A1: almacenamiento e imagen de un sistema en funcionamiento

**Encargo:** proteger documentos y configuración de un puesto de laboratorio. Se necesita comparar almacenamiento, aplicar dos estrategias de copia, usar destinos remoto y extraíble y recuperar una imagen que produzca un sistema arrancable. El objetivo didáctico es perder como máximo dos horas de datos y recuperar el servicio en una hora; son hipótesis de la actividad.

### Política y dos estrategias

Clasifica almacenamiento local, extraíble y de red por capacidad útil, latencia, disponibilidad, accesibilidad y custodia. Distingue dispositivo, volumen, protocolo y servicio. Describe redundancia y almacenamiento distribuido con sus modos de fallo; RAID y replicación no sustituyen una copia independiente que conserve un estado anterior.

Define los datos, responsables funcionales, frecuencia, rotación, retención y claves necesarias. Una tarea cada dos horas sólo cumple el intervalo nominal si termina y produce un punto utilizable. Si falla una ejecución, calcula la edad del último punto realmente recuperable. Conserva ese dato junto al registro de éxito o error.

Primera estrategia: una copia completa y versiones incrementales de archivos sintéticos con una herramienta compatible. Segunda: una imagen de sistema o copia de bloques mediante un mecanismo que asegure coherencia. Registra qué incluye cada una y qué necesita para restaurarse. Ensaya un archivo recuperado de un punto anterior y compara contenido y permisos.

Utiliza un destino remoto de laboratorio y un medio extraíble autorizado, con identidades, cifrado y permisos apropiados. En una VM, un disco virtual adicional simula parte de la operación de almacenamiento, pero no acredita por sí solo conexión, custodia y retirada segura de un soporte físico. Para esa letra se requiere la actividad con el medio real o la adaptación que determine el centro.

Antes de escribir, verifica el destino. Una carpeta `/mnt/copias` puede pertenecer al sistema raíz si el disco no está montado. Comprueba el sistema de archivos que la contiene con `findmnt -T` y contrasta su identidad. No elimines copias antiguas para liberar espacio sin revisar retención y recuperabilidad.

### Imagen coherente con el sistema activo

El criterio j) menciona imágenes de respaldo de sistemas en funcionamiento. Para ensayar una captura con el sistema activo, una variante es Windows Backup con VSS en una VM compatible, conforme a [Microsoft Learn](https://learn.microsoft.com/windows-server/administration/windows-commands/wbadmin-start-backup). Identifica edición, herramienta disponible y soporte actual. No copies el disco virtual mientras el huésped escribe y lo presentes como una imagen coherente de aplicación.

Prepara una VM de puesto independiente del directorio AD y un disco de destino nuevo de prácticas. Registra identificadores y tamaños; la letra `E:` siguiente es sólo un ejemplo que debes sustituir después de comprobar volúmenes. La copia puede gestionar versiones y espacio del destino; no la apliques a un disco que contenga la única copia de otro trabajo.

En una consola elevada, la observación inicial puede incluir:

```powershell
Get-Volume | Select-Object DriveLetter, FileSystemLabel, FileSystem, SizeRemaining, Size
vssadmin list writers
wbadmin get versions
```

Crea un documento sintético y registra su hash. Guarda y cierra aplicaciones según el método de consistencia previsto. En el escenario compatible, un ejemplo de inicio de copia de volúmenes críticos es:

```powershell
wbadmin start backup -backupTarget:E: -allCritical -vssCopy
```

Lee y confirma los objetos que proponga la herramienta sólo después de verificar el destino. `-vssCopy` no reemplaza el análisis de los escritores de la aplicación ni establece una política de rotación. Guarda el estado final, identificador de versión y mensajes. Un escritor ausente o con error exige revisar qué coherencia se ha obtenido; no deduzcas que cualquier base de datos quedó protegida.

Para restaurar, prepara otra VM con disco virtual vacío, firmware/controladores compatibles y medio de recuperación legítimo. Mantén la original apagada o desconectada de LAB durante la prueba de clonación. En el entorno de recuperación selecciona la imagen y comprueba explícitamente el disco vacío que se va a sobrescribir antes de aceptar. Nunca utilices un comando genérico de restauración contra un disco de trabajo.

Arranca el sistema recuperado, registra versión, aplicaciones y documento de prueba, compara el hash y verifica una operación real. La imagen no se acepta sólo porque su contenedor exista. Mide preparación, restauración y validación por separado y el intervalo total, comparándolos con el objetivo. Explica cómo evitar duplicar identidades o direcciones cuando se reincorpore el equipo; un controlador de dominio requiere un procedimiento específico distinto.

**Entregables:** política, clasificación, dos estrategias ejecutadas, destinos, puntos/versiones, medio remoto/extraíble y sistema recuperado. La solución debe indicar pérdida potencial, tiempo real y límites de coherencia, no únicamente capacidad ocupada por el backup.

<a id="ra3"></a>
## RA3 · 0226-RA3-A1: protección activa, procedencia y recuperación de datos

**Encargo:** preparar un puesto de prácticas frente a un fallo de seguridad, demostrar actualización y autenticidad, ensayar antimalware de forma inocua y recuperar archivos de una imagen de datos sintética. No se utilizan muestras de malware ni se prueba sobre información de terceros.

### Contingencia y mantenimiento

Redacta una secuencia de detección, contención, preservación, decisión, recuperación y validación. Clasifica al menos seis comportamientos —cifrado extorsivo, robo de credenciales, persistencia, propagación, publicidad no deseada y control remoto no autorizado— indicando vía y efecto. Las categorías pueden solaparse; una etiqueta comercial no sustituye el comportamiento observado.

Selecciona una actualización legítima del SO o aplicación. Registra versión anterior, aviso o motivo, dependencias, copia y pruebas previstas. Instálala mediante el mecanismo oficial del escenario y verifica versión, funcionamiento y regresiones. Una tarea programada que no termina no demuestra actualización periódica; conserva fechas y resultados.

Para autenticidad contrasta la firma del repositorio o distribuidor y la cadena de confianza que realmente se utiliza. Un hash recibido por el mismo canal no autenticado del paquete no identifica por sí solo a su autor. Documenta por qué la fuente de la clave o huella es confiable y qué error impediría instalar. No ejecutes un archivo desconocido para averiguar si «parece legítimo».

### Ensayo antimalware controlado

En Debian puede utilizarse ClamAV, con versión y firmas actualizadas mediante el mecanismo oficial. En Windows puede usarse la protección mantenida del sistema. Evita ejecutar simultáneamente dos procesos de actualización que bloqueen la misma base de firmas. En ClamAV consulta primero versión/estado y el servicio de actualización configurado.

Escanea un archivo benigno preparado por ti y después el archivo de prueba inocuo que el proveedor o [EICAR](https://www.eicar.org/download-anti-malware-testfile/) distribuye para verificar detectores, sólo dentro del laboratorio autorizado. No uses un ejecutable malicioso. La secuencia debe identificar dónde se produjo el bloqueo: navegador, protección del anfitrión, pasarela o motor de la VM. Un bloqueo anterior a la descarga no prueba que el motor del huésped haya analizado el archivo.

Para un archivo que ya está en la carpeta sintética de la VM, un ejemplo de observación es:

```bash
clamscan -V
clamscan --infected --no-summary /ruta/verificada/al/archivo-de-prueba
estado_analisis=$?
printf 'Código de salida: %s\n' "$estado_analisis"
```

Sustituye la ruta por el archivo autorizado; no la ejecutes literalmente. En `clamscan`, 0 indica ausencia de detecciones, 1 detección y 2 error según su manual. Conserva informe, versión de firmas y acción aplicada. Ensaya cuarentena o retirada mediante el procedimiento del producto y confirma qué desapareció y qué permanece. Una detección de prueba valida una ruta de funcionamiento, no demuestra inmunidad frente a cualquier amenaza.

### Recuperación sobre copia

El docente puede proporcionar una imagen de volumen con archivos sintéticos, un manifiesto de hashes y un borrado controlado. Conserva la imagen de origen y calcula su hash. Trabaja sobre copia, sin montar con escritura el original; guarda lo recuperado en otro destino. Utiliza una herramienta de recuperación admitida —por ejemplo TestDisk/PhotoRec en el escenario apropiado— y comprueba en la interfaz que seleccionas el archivo de imagen, no un disco físico del equipo.

Contrasta resultados con el manifiesto. Puede recuperarse contenido sin nombres ni estructura originales; distingue recuperación por metadatos y por firmas. No presentes una suma de ficheros como prueba de integridad. Explica qué no se recuperó y por qué la experiencia sobre una imagen sintética no garantiza recuperar un SSD que ya ha ejecutado TRIM o un medio sobrescrito.

**Entregables:** contingencia, clasificación, actualización, verificación de origen, ensayo antimalware y recuperación con hashes. La aceptación de a)–f) requiere resultados de acciones observables y conservación de los originales; los pasos que no hayas ejecutado quedan pendientes.

<a id="ra4"></a>
## RA4 · 0226-RA4-A1: privacidad de las comunicaciones e identidad

**Encargo:** revisar los servicios de un puesto, reducir comunicaciones no necesarias, proteger un intercambio, demostrar firma digital y configurar un firewall con retorno. Se utilizará una VM dedicada y sólo tráfico sintético de sus equipos.

### Inventario y comunicaciones

Lista procesos, listeners, dirección de enlace y finalidad. En Linux `sudo ss -lntup` permite observar sockets y procesos con los permisos adecuados; relaciona cada entrada con una necesidad. Desinstalar o detener un servicio sin conocer su dependencia no constituye una mejora justificada. Conserva la comparación antes/después y la prueba del servicio que debe seguir disponible.

Analiza un mensaje de fraude inventado: urgencia, cambio de cuenta de pago y petición de credenciales. Propón verificación independiente mediante un contacto ya conocido, sin responder al remitente ni abrir su enlace. Diferencia indicios y causa confirmada; un error ortográfico no es un criterio suficiente para clasificar todos los fraudes.

Prepara reglas de correo o controles de contenido con mensajes sintéticos permitidos y no deseados. Registra qué se filtra, qué falso positivo puede aparecer y cómo recuperarlo. Minimizar publicidad o spam no equivale a bloquear arbitrariamente todos los puertos de correo. Relaciona el control con el componente que realmente procesa los mensajes.

Compara una comunicación protegida mediante HTTPS o SSH con su configuración. Verifica nombre, confianza y resultado desde cliente. Si analizas paquetes, captura sólo el enlace propio autorizado y explica qué metadatos siguen visibles. El cifrado de transporte no oculta necesariamente direcciones, tamaños o tiempos ni protege un endpoint ya comprometido.

Para Wi-Fi compara autenticación, cifrado, compatibilidad y gestión de claves de los mecanismos disponibles. No habilites WEP o una red abierta de aula para «probar» seguridad antigua. Los mecanismos obsoletos pueden analizarse con documentación o una simulación expresamente aislada; el resultado de esa comparación no es una recomendación de despliegue.

### Firma y certificado con datos sintéticos

En una carpeta nueva de prácticas, protegida y sin archivos previos homónimos, prepara un documento sin datos personales. El ejemplo siguiente crea una clave privada cifrada y demuestra firma criptográfica; las contraseñas se introducen interactivamente y no se escriben en el comando:

```bash
umask 077
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -aes-256-cbc -out privada-lab.pem
openssl pkey -in privada-lab.pem -pubout -out publica-lab.pem
openssl dgst -sha256 -sign privada-lab.pem -out informe-lab.sig informe-lab.txt
openssl dgst -sha256 -verify publica-lab.pem -signature informe-lab.sig informe-lab.txt
```

El archivo `informe-lab.txt` se crea antes del ejemplo y las salidas no deben existir. Verifica el original; después modifica una copia y comprueba que la misma firma no valida esa copia. No publiques la clave privada. Explica la diferencia entre hash, firma y cifrado: firmar el documento no oculta su contenido.

Inspecciona también un certificado público de laboratorio: sujeto, emisor, vigencia, clave pública y huella. Relaciona identidad y cadena de confianza. Una clave que tú has creado o un certificado autofirmado no acredita automáticamente la identidad de una persona ni equivale a una firma electrónica cualificada. El ensayo demuestra un mecanismo; su uso jurídico requiere un contexto y requisitos distintos.

### Firewall y cierre

Ejecuta la práctica recuperable de [hardening](06-hardening-y-cambios-seguros.md) en una VM dedicada, con consola, copia del estado y política única. Antes de aplicar valida sintaxis y reglas; después prueba un flujo permitido y uno denegado desde el cliente. Guarda reglas efectivas y procedimiento de retorno. No mantengas dos gestores modificando la misma política sin una arquitectura documentada.

**Entregables:** inventario, fraude sintético, filtrado, transporte protegido, comparación Wi-Fi, firma/verificación y firewall. La aceptación requiere que los accesos y denegaciones correspondan al diseño. Un puerto abierto no demuestra identidad y una firma válida no demuestra confidencialidad; cada prueba responde a su objetivo.

<a id="ra5"></a>
## RA5 · 0226-RA5-A1: expediente normativo de un servicio

**Encargo:** analizar una academia ficticia que publica un portal, mantiene cuentas de estudiantes y encarga soporte técnico a otra entidad. El caso usa datos inventados. Debes identificar normas, acceso a información personal, intervinientes, atención de derechos y alcance de marcos de seguridad, relacionándolo con decisiones técnicas.

### Investigación y expediente

1. Describe finalidad, población, datos, ubicaciones, destinatarios, conservación y operaciones del servicio. Distingue portal público, entorno interno y actividad comercial. La decisión legal no se deduce sólo de que una página utilice HTTPS.
2. Consulta el [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679/oj) y la [LOPDGDD](https://www.boe.es/eli/es/lo/2018/12/05/3/con). El módulo nació en 2007: los términos históricos de sus criterios se relacionan con el marco vigente, sin presentar una norma derogada como obligación actual. Anota fecha y artículo que fundamenta cada conclusión.
3. Identifica quién decide finalidades y medios y qué tercero trata datos por encargo. Determina los roles del caso por sus funciones, no sólo por llamarse «proveedor» o «administrador». Conserva una lista de cuestiones que requerirían revisión por la persona competente de la organización.
4. Diseña acceso por funciones con minimización: atención administrativa, docencia, soporte y consulta propia. Justifica qué información necesita cada rol y comprueba un permiso permitido y otro denegado con datos sintéticos. El soporte no recibe por defecto todo el expediente para resolver un problema de contraseña.
5. Simula una solicitud de acceso de una persona y el procedimiento de recepción, verificación proporcional, localización, revisión de terceros y respuesta por canal adecuado. Usa las condiciones y plazos que indique la norma aplicable al supuesto, citándolos. No reveles información de otras personas para responder a la petición.
6. Revisa la [LSSI](https://www.boe.es/eli/es/l/2002/07/11/34/con) según actividad y comunicaciones del servicio. Distingue obligaciones del supuesto de recomendaciones técnicas; no conviertas toda web interna en un comercio electrónico por su tecnología.
7. Compara gestión de seguridad y certificación. Consulta el [ENS](https://www.boe.es/eli/es/rd/2022/05/03/311/con) para analizar cuándo aplica y distingue ese alcance de un marco de gestión u obligaciones contractuales. Una checklist escolar no certifica ENS ni una norma de gestión.

### Solución razonada y evidencias

Construye una tabla `hecho del caso → cuestión → fuente/artículo → decisión → medida técnica → evidencia`. Por ejemplo, un rol de soporte necesita restablecer acceso, pero no consultar calificaciones: la decisión se refleja en permisos y una prueba negativa. Otra fila explica quién autoriza un cambio de finalidad y qué información no debe copiarse a los logs.

La respuesta debe reconocer incertidumbre. Si el supuesto no especifica si hay publicidad comercial o qué decisiones toma un proveedor, indica la información que falta y las alternativas condicionadas. No elijas una obligación o una exención para completar la tabla sin fundamento.

**Entregables:** ficha de normas, mapa de tratamiento y roles, matriz de acceso, procedimiento de derechos, análisis LSSI y alcance de marcos. Acepta cuando cada conclusión conserva fuente, condiciones y conexión con una medida verificable. El expediente es un ejercicio educativo y no una declaración de cumplimiento de una organización real.

## Revisión final de evidencias

Contrasta las 39 letras con la [matriz](09-alineacion-ra.md). Para cada una conserva evidencia, versión, resultado y límite. La lectura de una ficha no sustituye ensayo del SAI; tener un backup no sustituye restaurarlo; instalar un antivirus no demuestra que se actualice o detecte una prueba; escribir una política no demuestra sus permisos efectivos.

La revisión considera exactitud, conservación de datos, interpretación y autonomía. Si la actividad se realiza en grupo, identifica la participación individual y una operación que cada integrante pueda explicar. Las ponderaciones, adaptaciones y calificaciones oficiales corresponden al centro.

## Fuentes primarias de procedimiento

- [Microsoft Learn: wbadmin start backup](https://learn.microsoft.com/windows-server/administration/windows-commands/wbadmin-start-backup) y [Windows Server Backup](https://learn.microsoft.com/windows-server/storage/backup/): compatibilidad, VSS y recuperación del sistema.
- [ClamAV: análisis](https://docs.clamav.net/manual/Usage/Scanning.html), [actualización](https://docs.clamav.net/manual/Usage/SignatureManagement.html) y [EICAR](https://www.eicar.org/download-anti-malware-testfile/): herramientas y prueba inocua controlada.
- [CGSecurity: TestDisk y PhotoRec](https://www.cgsecurity.org/wiki/Main_Page): recuperación y preservación del medio de origen.
- [OpenSSL: dgst](https://docs.openssl.org/master/man1/openssl-dgst/) y [genpkey](https://docs.openssl.org/master/man1/openssl-genpkey/): firma, verificación y generación de claves.
- [AEPD](https://www.aepd.es/), BOE y EUR-Lex enlazados en el RA5: fuentes para el análisis normativo del caso.
