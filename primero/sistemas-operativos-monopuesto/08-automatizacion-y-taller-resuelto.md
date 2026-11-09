# 08 · Automatización mantenible y taller resuelto

[Índice](README.md) · [Permisos y consistencia](07-archivos-permisos-y-consistencia.md)

## 1. Contrato de una tarea automatizada

Una automatización fiable define entradas, identidad, salidas, entorno, errores y verificación. «Ejecutar un script cada día» deja sin responder qué ocurre si la sesión está cerrada, falta el origen, se llena el destino o dos ejecuciones coinciden. Esos casos no son detalles posteriores: forman parte de la función de administración.

El ejemplo de este capítulo genera un **manifiesto de archivos sintéticos** con hashes. Lee el origen y publica un informe en otra carpeta; no copia datos y no constituye un backup. Sirve para aprender validación de rutas, tratamiento de nombres, publicación de resultados y programación. Ninguna ejecución debe tocar un árbol de datos de una empresa sin adaptar requisitos y autorización.

Se incluyen versiones [Bash](ejemplos/ampliacion/manifiesto.sh) y [PowerShell](ejemplos/ampliacion/manifiesto.ps1). Ambas requieren dos directorios existentes y rechazan que la salida esté dentro del origen. El árbol se controla desde una sola cuenta; no se promete resistir a actores que cambien enlaces o permisos mientras se ejecuta. Las lecturas sucesivas tampoco representan un snapshot consistente de una aplicación activa.

## 2. Preparar y ejecutar Bash

Dentro de tu VM Debian, crea un conjunto nuevo y revisa que no reutilizas archivos anteriores:

```bash
mkdir -p "$HOME/smr-som-automatizacion/entrada" "$HOME/smr-som-automatizacion/salida"
printf '%s\n' 'Dato sintético uno' > "$HOME/smr-som-automatizacion/entrada/uno.txt"
printf '%s\n' 'Dato sintético dos' > "$HOME/smr-som-automatizacion/entrada/dos con espacios.txt"
```

Desde la raíz del repositorio:

```bash
bash -n primero/sistemas-operativos-monopuesto/ejemplos/ampliacion/manifiesto.sh
bash primero/sistemas-operativos-monopuesto/ejemplos/ampliacion/manifiesto.sh \
  "$HOME/smr-som-automatizacion/entrada" \
  "$HOME/smr-som-automatizacion/salida"
```

La primera orden comprueba sintaxis, no comportamiento. La segunda genera `manifiesto.sha256` y una línea de resultado. Necesita Bash, utilidades GNU y `flock` de `util-linux`; no instala dependencias. El fichero `.manifiesto.lock` puede permanecer en la salida: el bloqueo lo mantiene un descriptor abierto, no la mera existencia del nombre.

Las rutas se validan y normalizan antes de comparar su relación. El script utiliza un temporal dentro del directorio de salida y lo publica al terminar correctamente. Si falla la lectura o no encuentra archivos regulares, conserva el informe anterior. El código de error y el mensaje deben quedar registrados; un fichero de ayer no demuestra que hoy haya habido éxito.

## 3. Nombres, enlaces y comprobación del resultado

Bash debe proteger argumentos mediante comillas. El ejemplo usa `find ... -exec ... +` para pasar nombres como argumentos sin dividirlos por espacios. La salida GNU de `sha256sum` utiliza sus convenciones de escape cuando es necesario. No construye comandos concatenando nombres ni usa `eval`.

El recorrido no sigue enlaces simbólicos por defecto y recoge archivos regulares. Esa elección evita incluir automáticamente objetos externos, pero significa que el manifiesto no representa enlaces, directorios vacíos, ACL o todos los metadatos. Si el requisito cambia, debes ampliar el formato; no presentar un inventario parcial como imagen completa del sistema.

Verifica desde el directorio de origen, porque los nombres del manifiesto son relativos a él:

```bash
cd "$HOME/smr-som-automatizacion/entrada"
sha256sum -c ../salida/manifiesto.sha256
```

Después modifica sólo un archivo sintético y repite: debe detectarse diferencia. No regeneres antes el manifiesto que usas como referencia, porque convertirías la modificación en la nueva referencia sin evaluar el cambio. Conserva original, informe y resultado de la prueba según el objetivo de la práctica.

## 4. Temporizador systemd de usuario

Primero ejecuta manualmente hasta comprender la salida. Después copia la versión revisada del script a una ruta controlada de tu cuenta, como `%h/.local/bin/smr-manifiesto.sh`, y hazla ejecutable. Crea `~/.config/systemd/user/` si falta. Los ejemplos siguientes sólo administran la instancia de usuario y sus datos de prueba; no necesitan un servicio root.

`smr-manifiesto.service`:

```ini
[Unit]
Description=Manifiesto de archivos sintéticos de SMR

[Service]
Type=oneshot
ExecStart="%h/.local/bin/smr-manifiesto.sh" "%h/smr-som-automatizacion/entrada" "%h/smr-som-automatizacion/salida"
NoNewPrivileges=true
UMask=0077
```

`smr-manifiesto.timer`:

```ini
[Unit]
Description=Programación del manifiesto SMR

[Timer]
OnCalendar=*-*-* 18:00:00
Persistent=true
Unit=smr-manifiesto.service

[Install]
WantedBy=timers.target
```

En estos archivos `%h` es un especificador de systemd, no una variable de shell. `ExecStart` no interpreta una línea como si fuera Bash; no se añaden redirecciones o tuberías esperando ese comportamiento. El script ya gestiona su informe y el journal recoge salida y error.

Tras revisar los archivos:

```bash
systemctl --user daemon-reload
systemctl --user start smr-manifiesto.service
systemctl --user status smr-manifiesto.service --no-pager
journalctl --user -u smr-manifiesto.service --no-pager -n 20
systemctl --user enable --now smr-manifiesto.timer
systemctl --user list-timers --all
```

Un servicio `oneshot` terminado correctamente puede quedar inactivo después de ejecutar; eso no equivale a fallo. Comprueba código de salida, journal, fecha y contenido. `Persistent=true` permite tratar un disparo de calendario perdido cuando el temporizador vuelve a activarse, con el alcance documentado; no ejecuta necesariamente una vez por cada día perdido ni garantiza funcionamiento mientras la instancia de usuario no exista.

La instancia de usuario suele depender del inicio de sesión salvo configuración adicional. No habilites permanencia de usuario como cambio automático en un equipo real; decide con el centro si el requisito exige ejecución sin sesión y qué mecanismo corresponde. Registra zona horaria y sincronización para interpretar la hora de calendario.

Para retirar esta programación utiliza `systemctl --user disable --now smr-manifiesto.timer`, confirma que ya no hay disparos y elimina sólo las unidades y script de esta práctica cuando no se necesiten. Ejecuta después `daemon-reload`. Conserva los resultados que formen parte de la entrega.

## 5. PowerShell y Programador de tareas

La versión PowerShell genera un CSV con ruta relativa, tamaño y SHA-256. Rechaza enlaces y puntos de análisis en el árbol de entrada, recorre directorios de forma controlada y mantiene un bloqueo exclusivo en la salida. Trabaja con rutas literales para no interpretar caracteres como patrones. Requiere un árbol sintético legible y un destino escribible por la identidad que la ejecute.

Prepara dos carpetas nuevas en tu perfil, revisa el script y ejecútalo según la política autorizada del equipo. No se cambia la política global de ejecución para evitar una restricción del centro. Ejemplo desde PowerShell y la raíz del repositorio:

```powershell
$basePrueba = Join-Path $env:USERPROFILE 'smr-som-automatizacion'
$entradaPrueba = Join-Path $basePrueba 'entrada'
$salidaPrueba = Join-Path $basePrueba 'salida'
New-Item -ItemType Directory -Path $entradaPrueba, $salidaPrueba -Force | Out-Null
Set-Content -LiteralPath (Join-Path $entradaPrueba 'uno.txt') -Value 'Dato sintético' -Encoding UTF8
& '.\primero\sistemas-operativos-monopuesto\ejemplos\ampliacion\manifiesto.ps1' `
  -Origen $entradaPrueba -Salida $salidaPrueba
Import-Csv -LiteralPath (Join-Path $salidaPrueba 'manifiesto.csv')
```

Antes de usar `-Force` comprueba que esas carpetas y archivo no contienen trabajo previo; aquí sólo se preparan objetos exclusivos de laboratorio. El CSV requiere comprobar cada archivo contra su hash de referencia. No basta contar filas: también hay que relacionar rutas, tamaños y contenido, y explicar que el inventario no guarda una copia.

En Programador de tareas define ejecutable de PowerShell apropiado, `-NoProfile`, ruta del script y argumentos con comillas, usuario, condición de sesión y directorio de inicio. No incluyas credenciales en argumentos ni marques elevación sin necesidad. Una tarea que escribe sólo en su perfil debería ensayarse con esa misma cuenta y privilegios.

Primero ejecuta por demanda y consulta historial, última ejecución y resultado; después programa un disparo próximo y comprueba su efecto real. Los códigos de salida de PowerShell y herramientas externas necesitan interpretación. La presencia de un CSV anterior no valida el nuevo disparo. Para retirar, deshabilita la tarea concreta y elimina sólo su definición después de conservar evidencias.

## 6. Dieciséis problemas con solución razonada

**1. La tarea funciona manualmente y no programada.** Compara identidad, directorio de trabajo, argumentos y disponibilidad del origen. No amplíes permisos antes de identificar cuál de esos elementos difiere.

**2. El temporizador aparece, pero el servicio queda inactivo.** Un `oneshot` puede terminar y quedar inactivo correctamente. Revisa código de resultado, journal y salida reciente antes de declararlo fallido.

**3. Existe manifiesto después de una ejecución fallida.** Puede ser la última versión correcta que el script conservó. Fecha y código de salida distinguen preservación de éxito actual.

**4. Dos ejecuciones pisan su informe.** Falta exclusión o usan bloqueos distintos. El ejemplo utiliza el mismo bloqueo por destino; una ejecución concurrente debe terminar con error claro en vez de competir.

**5. Un archivo con espacios rompe el script del alumno.** Probablemente dividió texto en argumentos sin comillas o usó `for` sobre una salida. Debe conservar nombres como argumentos y evitar interpretar contenido como código.

**6. El informe crece cada vez que se ejecuta.** Si se escribe dentro del origen, puede inventariarse a sí mismo y sus temporales. Se rechaza esa relación de rutas y se separa salida.

**7. Un enlace apunta fuera del origen.** Hay que decidir si omitirlo, registrarlo o seguirlo con límites. El Bash incluido no lo sigue; el PowerShell lo rechaza. Ninguno promete incluir su destino.

**8. Todos los hashes coinciden, pero falta un archivo.** La verificación de entradas presentes no comprueba por sí sola que el conjunto de referencia estuviera completo. Revisa inventario y lista esperada.

**9. Se regeneró el manifiesto después de corromper la copia.** Se perdió la referencia anterior. Conserva referencias por versión o utiliza otra fuente de integridad conocida.

**10. ¿Un hash sustituye un backup?** No conserva el contenido. Permite comparar con una referencia; recuperar exige otra copia o mecanismo de reconstrucción.

**11. La memoria libre es baja, pero el puesto responde bien.** Estudia memoria disponible y caché recuperable antes de recomendar ampliación. La cifra libre aislada es insuficiente.

**12. Un proceso muestra mucha CPU acumulada, pero ahora está detenido.** El acumulado cuenta su historia, no actividad actual. Mide diferencias temporales y estado presente.

**13. El archivo tiene escritura, pero no puede borrarse.** El borrado de la entrada depende del directorio y reglas adicionales. Revisa permiso de recorrido, escritura y restricciones como sticky.

**14. `getfacl` muestra `rw-` con efectivo `r--`.** La máscara limita esa entrada. Evalúa el conjunto antes de ampliar máscara, pues puede afectar a otras identidades.

**15. Windows RE cambia la letra del volumen.** Identifica la instalación por contenido y estructura. Nunca ejecutes una reparación suponiendo que `C:` conserva su función en cualquier entorno.

**16. La máquina perdió varios disparos de calendario.** `Persistent` no debe interpretarse como una cola universal de todas las ejecuciones omitidas. Comprueba semántica, instancia activa y requisito de recuperación de tareas.

## 7. Tres prácticas integradoras nuevas

### P4 · Automatización con errores previstos

Genera un manifiesto de tres archivos sintéticos, uno con espacios. Comprueba contenido, cambia una copia y demuestra detección. Después ensaya origen inexistente, salida dentro del origen y ejecución concurrente mediante un bloqueo mantenido de forma controlada. No provoques falta de espacio real en el sistema para simular error.

La entrega incluye contrato, resultado de cada caso, códigos de salida y explicación del informe anterior conservado. Rúbrica propia: corrección 30 %, casos negativos 30 %, privilegio mínimo 20 % y documentación 20 %. La salida debe estar fuera del origen y no debe borrarse contenido para superar una prueba.

### P5 · Programación y recuperación de una tarea

Programa el manifiesto en la plataforma que tengas, primero por demanda y después mediante un disparo de prueba próximo. Registra identidad, horario, zona, directorio de trabajo y condición de sesión. Comprueba el contenido con hashes y una marca temporal de la ejecución esperada. Finalmente deshabilita la programación y verifica que no quedan disparos activos.

La aceptación requiere una ejecución real desde el programador y una prueba negativa interpretada. Una captura de la definición no es suficiente. Rúbrica propia: definición 25 %, ejecución y evidencia 30 %, diagnóstico 25 % y retirada 20 %.

### P6 · Incidencia transversal del puesto

El docente proporciona un escenario sintético con dos causas posibles: ruta relativa equivocada o permiso insuficiente para la cuenta de tarea. Antes de modificar redacta ambas hipótesis y una prueba que las separe. Resuelve sólo la causa confirmada, repite la tarea con mínimo privilegio y explica por qué no era necesario reinstalar el SO ni elevar toda la sesión.

Entrega registro de antes/después, prueba positiva, prueba fuera del alcance que debe seguir denegada y plan de reversión. Rúbrica: hipótesis 25 %, prueba discriminante 25 %, cambio mínimo 25 % y comunicación/evidencias 25 %. Las soluciones esperadas orientan el estudio; no afirman haber ejecutado el escenario en el equipo del lector.

## Referencias primarias

- [GNU Bash: manual](https://www.gnu.org/software/bash/manual/): expansión, comillas y estado de salida.
- [Debian: flock](https://manpages.debian.org/trixie/util-linux/flock.1.en.html): bloqueo asociado a descriptores y procesos.
- [systemd.timer en Debian 13](https://manpages.debian.org/trixie/systemd/systemd.timer.5.en.html): calendario, persistencia y alcance.
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html): semántica de servicios y ejecución.
- [Microsoft: about_Automatic_Variables](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_automatic_variables): estados y contexto de ejecución.
- [Microsoft: Task Scheduler](https://learn.microsoft.com/windows/win32/taskschd/task-scheduler-start-page): modelo de tareas, acciones y seguridad.
