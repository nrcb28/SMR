# Retos prácticos por resultado de aprendizaje · 0222

[Mapa de RA y criterios](09-alineacion-ra.md) · [Índice](README.md) · [Trazabilidad JSON](alineacion-ra.json)

## Preparación y reglas de evidencia

Los cinco retos organizan el trabajo por resultados de aprendizaje oficiales. Cada uno desarrolla la actividad A1 de su RA y permite reunir evidencias de todas sus letras. El [mapa](09-alineacion-ra.md) indica exactamente qué criterio se vincula a cada artefacto y comprobación. Las propuestas son didácticas; el centro establece las condiciones e instrumentos de evaluación.

Se utiliza Debian 13 y Windows 11 Pro con soporte y licencia adecuados. Las acciones de instalación, recuperación, cuentas, servicios y almacenamiento se realizan en una VM nueva o copia autorizada, con datos sintéticos y consola disponible. Una condición que no se puede ejecutar por falta de recursos se deja pendiente. Las salidas descritas son resultados esperados para contrastar, no pruebas realizadas por el autor.

Antes de cada cambio conserva configuración y objetivo de retorno. No se reutilizan cuentas o rutas de una actividad anterior sin comprobar su finalidad. La memoria incluye contexto de la identidad y versión: una acción como administrador y una acción ordinaria no demuestran el mismo comportamiento.

<a id="ra1"></a>
## RA1 · 0222-RA1-A1: de la información al archivo

### Caso y procedimiento

Un puesto conserva documentos en español, un conjunto de archivos de trabajo y una aplicación que puede cerrarse inesperadamente. Debes explicar cómo representa información, cómo se ejecuta la aplicación y qué ofrece el sistema de archivos. Entrega un mapa que relacione hardware, SO, proceso, memoria, archivo y almacenamiento, sin confundir representación lógica con ubicación física.

Empieza con un cuaderno de conversiones. El valor decimal 56 es `00111000` en ocho bits y `0x38` en hexadecimal. El carácter «ñ» tiene punto de código U+00F1 y se codifica en UTF‑8 mediante dos bytes, `C3 B1`. El número de caracteres, puntos de código o bytes puede diferir según texto y codificación; no se deduce el tamaño de un documento multiplicando siempre por uno.

En una terminal con Python 3 comprueba el ejemplo sobre un dato literal:

```python
texto = "ñ"
print(hex(ord(texto)))
print(texto.encode("utf-8").hex())
print(len(texto), len(texto.encode("utf-8")))
```

Se espera `0xf1`, `c3b1` y `1 2`. Después estudia un proceso propio con herramienta gráfica o `ps`: identifica PID, usuario y estado, y explica por qué un proceso dormido no está necesariamente averiado.

Prepara un directorio temporal de archivos sintéticos en la VM Linux:

```bash
lab_ra1=$(mktemp -d -t smr-ra1.XXXXXX)
printf 'Contenido de prueba\n' > "$lab_ra1/dato.txt"
ln "$lab_ra1/dato.txt" "$lab_ra1/enlace-duro.txt"
ln -s dato.txt "$lab_ra1/enlace-simbolico.txt"
ls -li "$lab_ra1"
```

Interpreta entradas, inodos, contenido y enlaces. Un enlace duro no es una segunda copia independiente; un enlace simbólico contiene una referencia a una ruta. Las propiedades se observan en el sistema de archivos que ejecuta la prueba, no se extrapolan sin matices a todos los productos.

### Elección transaccional y solución

Compara ext4 y NTFS en el contexto real del puesto: compatibilidad, permisos, tamaños, herramientas, recuperación y mantenimiento. Un journal ayuda a consistencia según su implementación y modo; no es una copia histórica de todos los documentos ni convierte varias escrituras de una aplicación en una transacción de base de datos. La caída de un proceso y el fallo de alimentación tampoco son el mismo escenario.

No provoques cortes eléctricos para observar recuperación. Explica qué protege el mecanismo y qué debe proteger una copia de seguridad. Concluye con una prueba de permisos sobre datos sintéticos y una tabla de atributos de archivo/directorio en ambos sistemas. Un nombre que «termina en .txt» no determina su codificación ni garantiza su contenido.

**Aceptación:** conversiones comprobadas, proceso contextualizado, árbol/metadatos interpretados y elección del FS justificada. Una tabla copiada sin relacionar sus propiedades con el uso no completa el criterio de selección. La retirada conserva únicamente los archivos de la actividad que hayas identificado.

<a id="ra2"></a>
## RA2 · 0222-RA2-A1: instalación que responde a un plan

### Preparación del proyecto

Configura dos invitados legítimos, uno libre y otro propietario, si los recursos lo permiten. Antes del instalador entrega una ficha de funciones del SO y arquitectura: kernel, servicios, controladores, espacio de usuario e interfaces. Relaciona esa arquitectura con una operación, por ejemplo abrir y guardar un documento; no se limita a dibujar cajas sin flujo.

Comprueba requisitos oficiales de hardware y edición, aplicaciones necesarias, espacio físico disponible en el anfitrión y recursos de VM. Para Windows 11 la plataforma virtual debe cumplir requisitos admitidos, incluidos los de seguridad que correspondan. No se eluden para terminar el reto. Una imagen que arranca en otra CPU o arquitectura no asegura compatibilidad con este equipo.

El plan identifica medio y procedencia, particiones, sistema de archivos, modo UEFI, cuentas, idioma/zona, red, actualizaciones y recuperación. El disco destino es nuevo y se reconoce por su configuración en el hipervisor y capacidad; no se selecciona sólo porque se llame `sda` o «Disco 0».

### Ejecución y control

Instala mediante el asistente oficial, registrando las decisiones significativas y mensajes. No es necesario capturar cada pantalla: sí las que permiten justificar arquitectura, almacenamiento, cuenta y resultado. Conserva una bitácora de incidencias con síntoma, hipótesis, acción y comprobación, incluso si la instalación termina sin errores relevantes.

Comprueba el gestor de arranque y el acceso al mecanismo de rescate sin modificar a ciegas una ESP o BCD. Identifica qué configuración es de firmware, qué pertenece al disco y qué aplica el SO. Una captura de «instalación completada» no muestra que el modo de arranque y la recuperación sean los previstos.

Configura actualizaciones por canal oficial, registra versión antes/después y programa el reinicio cuando corresponda. En LAB conserva `.56.20/24` para el cliente y ningún gateway ficticio; Internet puede ir por la NIC NAT separada. Registra el medio, las aplicaciones y su licencia en el inventario, sin publicar claves o imágenes redistribuidas sin permiso.

### Solución y recuperación

La elección correcta es la que satisface aplicaciones, soporte y requisitos documentados, no una preferencia por marca o interfaz. Si una aplicación sólo admite una plataforma, la alternativa puede requerir cambiar requisito, herramienta o entorno; no se afirma compatibilidad por tener procesadores de potencia parecida.

Ante un error, vuelve al último paso comprobado y valida su dependencia. Si el disco no aparece, estudia controlador y configuración del almacenamiento antes de crear particiones nuevas. Si no hay licencia o hardware adecuado, entrega diseño y deja la instalación concreta pendiente.

**Entregables:** matriz de elección, plan, inventario, bitácora, prueba de arranque y rescate, versión actualizada y registro de condiciones del software. La recuperación consiste en el procedimiento previsto sobre la VM de prueba, preservando medios y datos originales.

<a id="ra3"></a>
## RA3 · 0222-RA3-A1: puesto personalizable, actualizado y recuperable

### Requerimientos de usuario

Prepara un perfil ordinario que necesite interfaz legible, acceso a una red de pruebas, una utilidad de trabajo y una tarea periódica de comprobación. Explica qué resolverías mediante GUI y qué mediante CLI, incluyendo accesibilidad y posibilidad de documentar o repetir. La mejor interfaz depende del usuario y de la operación.

Aplica preferencias sólo a la cuenta de prueba: idioma, presentación, tamaño o contraste conforme a necesidades acordadas. Anota cómo regresar al estado anterior. No desactives bloqueo, protección o actualizaciones como una supuesta mejora universal de usabilidad. Una preferencia de perfil es distinta de una política para toda la máquina.

Trabaja con un volumen o árbol sintético identificado y realiza operaciones que permitan observar organización, atributos, compresión o gestión admitida por su sistema. La administración de un volumen no se sustituye por renombrar una carpeta; la memoria distingue el objeto que realmente se ha usado.

### Utilidad, dispositivos y automatización

Selecciona una utilidad pequeña y legítima de los repositorios o canal oficial. Comprueba si ya está instalada y qué otras aplicaciones dependen de ella. Instálala sólo en la VM y verifica la función concreta; después ensaya su retirada sin ordenar una limpieza general de paquetes ajenos. En Windows revisa editor, firma/canal y alcance de instalación; en Linux diferencia actualizar índices de instalar paquetes.

Utiliza el asistente pertinente para conectar un dispositivo o configurar la NIC LAB y prueba su función. Un icono de adaptador presente no demuestra una dirección correcta ni un servicio. La topología base no requiere una puerta de enlace en LAB.

Programa una tarea que ejecute un manifiesto sobre archivos sintéticos según el [capítulo de automatización](08-automatizacion-y-taller-resuelto.md). Define horario, cuenta, ruta absoluta, directorio de trabajo, salida y código de error. Cambia de forma controlada una entrada de prueba para comprobar que el fallo aparece y no se registra falsamente éxito.

### Recuperación del puesto

Ensaya una recuperación con el mecanismo correspondiente a tu instalación: archivo propio, configuración de prueba o VM completa según el objetivo. Un punto de restauración, una instantánea y una copia de datos no recuperan necesariamente los mismos objetos. Describe qué se restauró y qué cambios posteriores podrían perderse.

**Aceptación:** preferencias verificadas, actualización configurada, utilidad instalada/retirada con registro, dispositivo o red funcional y tarea con caso de éxito y fallo. Si la tarea se ejecutó manualmente pero no según calendario, deja pendiente la parte programada. Conserva captura o registro del horario y resultado real, sin fabricar una fecha de ejecución.

<a id="ra4"></a>
## RA4 · 0222-RA4-A1: administrar observando antes y después

### Usuarios, archivos y procesos

Parte de una matriz de identidades locales: editor, lector y cuenta ajena sobre un recurso sintético. Utiliza los procedimientos de [permisos efectivos](07-archivos-permisos-y-consistencia.md) para comprobar operaciones. Explora además la organización de archivos del sistema con herramienta gráfica en modo de consulta, sin modificar archivos protegidos para obtener evidencia.

Inicia un proceso propio de laboratorio, identifica su PID y estado y actúa sólo sobre él. En una shell Linux ordinaria un ejemplo es iniciar `sleep 120`, observarlo y finalizarlo con una señal apropiada. Si se ensaya `renice`, recuerda que un usuario puede disminuir prioridad de su proceso aumentando su valor nice, pero no obtiene por ello autorización para aumentar arbitrariamente prioridad. No mates procesos por un número copiado de otra sesión.

### Un servicio exclusivo y reversible

Para actuar sobre un servicio sin afectar componentes del puesto, crea una unidad de usuario en una sesión que disponga de systemd de usuario y bus. En la VM, el archivo `~/.config/systemd/user/ra4-demo.service` puede contener:

```ini
[Unit]
Description=Servicio de demostración del RA4 de SOM

[Service]
Type=simple
ExecStart=/usr/bin/sleep 120
```

Después de revisar el archivo, utiliza `systemctl --user daemon-reload`, `start ra4-demo`, `status ra4-demo`, `restart ra4-demo` y `stop ra4-demo`. Registra el cambio de PID y el estado, y consulta `journalctl --user -u ra4-demo`. No habilites arranque persistente si no forma parte de la actividad. Si no existe sesión de usuario apropiada, prepara ese entorno o deja la ejecución pendiente; no sustituyas el reto reiniciando servicios críticos al azar.

### Memoria, almacenamiento y configuración

Mide una carga de trabajo conocida con herramientas del [capítulo de observación](06-procesos-memoria-y-observabilidad.md). Separa memoria residente, disponible, caché, swap y actividad. Optimiza una causa demostrada: cerrar una aplicación innecesaria o ajustar recursos de la VM con parada y retorno, si el diseño lo admite. No vacíes cachés para que una captura muestre un número menor.

Para almacenamiento registra capacidad, inodos cuando proceda y actividad. Ensaya limpieza sólo de datos temporales generados por la actividad o una política compatible y justificada. SSD y HDD no necesitan exactamente las mismas operaciones; no uses desfragmentación como recomendación universal. Relaciona el mantenimiento con un objetivo, como margen de espacio o latencia bajo la carga.

### Evidencia y retirada

Entrega línea temporal, matriz de accesos, exploración gráfica, proceso, unidad de demostración, métricas y configuración efectiva. Un parámetro guardado pero no cargado se anota como tal. La retirada para la unidad es detenerla, quitar exclusivamente el archivo creado para ella y recargar el gestor de usuario; verifica que no queda activa.

La solución se acepta cuando cada actuación responde a un requerimiento y una observación. Una consola llena de comandos sin contexto no demuestra optimización ni administración razonada.

<a id="ra5"></a>
## RA5 · 0222-RA5-A1: dos tecnologías de virtualización y sus límites

### Plan de anfitriones e invitados

Diseña dos escenarios admitidos: uno con software libre, como KVM/libvirt en un anfitrión Linux compatible, y otro con software propietario legítimo, como Hyper‑V en un Windows Pro compatible. No se presupone que ambos puedan activarse dentro de una VM sin virtualización anidada ni que cualquier producto se comporte igual con otros hipervisores o mecanismos de seguridad activos.

El RA incluye instalar software libre y propietario y crear invitados libres y propietarios. Una revisión documental de dos productos no demuestra haber instalado ambos. Si sólo tienes un anfitrión válido o no dispones de licencia, conserva el plan y marca ese desempeño pendiente hasta una sesión del centro.

Comprueba capacidad física, CPU/virtualización, memoria reservada al anfitrión, almacenamiento libre, soporte y condiciones del software. Obtén medios oficiales de los invitados y sus requisitos. Planifica CPU, RAM, disco, firmware y dos NIC cuando corresponda al laboratorio, sin comprometer el anfitrión por sobreasignación injustificada.

### Instalación y configuración

En Debian amd64 compatible, consulta candidatos de `qemu-system-x86`, `libvirt-daemon-system` y `virt-manager` y utiliza el procedimiento oficial de la distribución para instalarlos. El conjunto y servicios reales pueden variar; documenta versión y arquitectura. En Windows comprueba compatibilidad de Hyper‑V y utiliza la activación de características que documenta Microsoft, con reinicio autorizado cuando se requiera. No desactives protecciones del anfitrión para seguir una receta de otra versión.

Crea invitados Linux y Windows legítimos, registra sus recursos y realiza arranque, parada limpia y acceso a consola. Relaciona dispositivos virtuales con el anfitrión: una NIC virtual no es el cable físico, y una carpeta compartida introduce un trayecto de datos que atraviesa el límite del invitado. Usa sólo datos sintéticos y habilita integraciones necesarias con su alcance documentado.

### Comparación y solución razonada

Define una prueba de rendimiento repetible: volumen de datos, operación, repeticiones, caché, estado del anfitrión y métrica. Conserva mediana y distribución, no sólo el mejor resultado. Si cambias a la vez SO invitado, aplicación e hipervisor, no puedes atribuir toda diferencia al hipervisor. Describe la comparación como dos escenarios distintos o controla las variables.

Una instantánea puede ayudar a repetir y volver al estado anterior, pero depende de archivos base y no equivale a una copia independiente. Un invitado aislado tampoco garantiza separación absoluta si se habilitan carpetas, portapapeles, USB o redes hacia el anfitrión.

**Entregables:** actas de instalación de virtualizadores, inventario de invitados, diagrama anfitrión/invitado, configuración, riesgos y prueba con resultados propios. La aceptación comprueba funcionamiento y explicación del límite. La retirada conserva sólo imágenes autorizadas y copias necesarias; no elimina discos ajenos para liberar espacio.

## Fuentes técnicas y cierre del dossier

- [Debian: manual de instalación](https://www.debian.org/releases/trixie/installmanual) y [Debian Reference](https://www.debian.org/doc/manuals/debian-reference/): plataforma y administración.
- [Documentación de ext4](https://docs.kernel.org/filesystems/ext4/): estructura y mecanismos de consistencia.
- [Python: Unicode HOWTO](https://docs.python.org/3/howto/unicode.html): texto, codificación y bytes.
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) y [systemctl](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html): unidades y operaciones.
- [Microsoft: habilitar Hyper‑V en Windows](https://learn.microsoft.com/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v): requisitos y procedimiento del anfitrión.
- [libvirt](https://libvirt.org/docs.html): administración e integración según su versión.

Antes de entregar, recorre las 41 letras del mapa. Para cada una localiza evidencia real o estado pendiente y una comprobación concreta. Una actividad integrada puede satisfacer varias letras, pero no hace desaparecer una prueba de instalación, programación o recuperación que todavía no se ha realizado.
