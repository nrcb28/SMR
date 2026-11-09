# 06 · Procesos, memoria y observabilidad del puesto

[Índice](README.md) · [Medición del hardware](../montaje-y-mantenimiento-de-equipos/05-medicion-y-rendimiento.md)

## 1. Del programa al proceso y al trabajo útil

Un archivo ejecutable no consume CPU por existir; un proceso es una instancia en ejecución con recursos y contexto. Una aplicación puede abrir varios procesos y cada proceso puede contener varios hilos. Para explicar un bloqueo interesa saber qué trabajo realiza cada uno y de qué recurso espera respuesta. El proceso con más tiempo acumulado de CPU no es necesariamente el responsable de una pausa que ocurre ahora.

El tiempo de pared mide la duración percibida entre inicio y fin. El tiempo de CPU suma ejecución sobre procesadores según la herramienta. Una tarea puede durar diez segundos y consumir dos de CPU porque pasó el resto esperando disco, red, una cerradura o interacción. Una tarea paralela puede acumular más segundos de CPU que de pared. Registra cuál estás midiendo y cómo se agrega.

Un hilo en espera de entrada/salida no se arregla automáticamente aumentando prioridad. La prioridad afecta a decisiones de planificación dentro de un conjunto de condiciones; no acelera un dispositivo ni resuelve una dependencia circular. Elevar procesos indiscriminadamente puede perjudicar la respuesta del resto del sistema y ocultar el diseño del problema.

## 2. Estados y señales de planificación en Linux

Consulta procesos con `ps` y actividad con `top`; no necesitas instalar herramientas adicionales para empezar. Una selección de observación es:

```bash
ps -eo pid,ppid,stat,etimes,time,%cpu,%mem,comm --sort=-%cpu | head -20
uptime
vmstat 1 5
```

`etimes` expresa segundos transcurridos desde el inicio; `time` es tiempo de CPU acumulado. Los porcentajes dependen de cómo calcula la herramienta su ventana. La primera muestra de `vmstat` puede representar promedios desde el arranque; compara las muestras siguientes como intervalos. En una VM, el anfitrión también puede limitar la ejecución aunque el invitado no muestre una causa local evidente.

La carga media de Linux no equivale a porcentaje de CPU: incluye tareas ejecutables y ciertas esperas no interrumpibles. Interprétala junto a número de CPU disponibles, estados y actividad de E/S. Una carga alta con CPU poco utilizada puede apuntar a espera de almacenamiento; una captura aislada no permite concluirlo sin otras evidencias.

Para un proceso concreto, registra PID, comando y hora. Los PID se reutilizan: detener más tarde el mismo número sin comprobar identidad puede afectar otro proceso. Antes de enviar una señal, identifica el objeto y utiliza primero el mecanismo de cierre ordenado de la aplicación. `SIGKILL` impide limpieza normal y no es una respuesta rutinaria a cualquier ventana que tarda.

## 3. Memoria virtual, residencia y compromiso

El espacio virtual describe direcciones que un proceso puede utilizar; no representa directamente RAM ocupada. Las páginas pueden estar respaldadas por archivos, memoria anónima, cero compartido u otros mecanismos. Parte del contenido puede ser compartido por varios procesos, por lo que sumar sin más todos los conjuntos residentes puede contar páginas repetidas.

En Linux, RSS representa páginas residentes según el contador y PSS reparte páginas compartidas entre procesos cuando la herramienta lo ofrece. Una aplicación puede reservar un espacio virtual grande y tocar sólo una parte. Por eso una cifra alta de tamaño virtual no basta para diagnosticar falta de RAM. Relaciona residencia, memoria disponible, reclamación, swap y respuesta percibida.

En Windows, el conjunto de trabajo describe páginas residentes asociadas al proceso, mientras el compromiso de memoria tiene un significado diferente vinculado a recursos de respaldo. El límite de compromiso depende de la configuración y no debe confundirse con RAM instalada. Una aplicación puede fallar al comprometer memoria aunque la interpretación de una única gráfica parezca sugerir espacio libre.

## 4. Caché y memoria disponible

Los sistemas aprovechan RAM para caché de datos y metadatos. Una cifra baja de memoria estrictamente libre puede ser normal si existe memoria recuperable y el trabajo responde bien. En Linux, `MemAvailable` estima memoria que podría ofrecerse a nuevas aplicaciones sin un intercambio perjudicial en las condiciones consideradas. No es una reserva garantizada para cualquier carga futura.

Consulta:

```bash
free -h
grep -E 'MemTotal|MemFree|MemAvailable|Cached|SwapTotal|SwapFree' /proc/meminfo
```

`Cached` no resume por sí solo toda la memoria recuperable ni debe restarse dos veces de otras categorías. Usa las definiciones del kernel y herramienta. La comparación útil combina tendencia y experiencia: si al abrir otra aplicación aumenta la actividad de swap, se elevan latencias y la respuesta cae, existe evidencia de presión; una caché grande sin pausas no prueba un problema.

Vaciar cachés para obtener una cifra de RAM «limpia» cambia el experimento y puede degradar rendimiento. Para estudiar primera apertura y reapertura, documenta explícitamente que son condiciones distintas. En un laboratorio no es necesario modificar parámetros globales de memoria para entender el efecto; observar con un conjunto sintético suele aportar información suficiente.

## 5. Fallos de página y paginación

Un fallo de página significa que el acceso necesita intervención del gestor de memoria; no todos implican ir al disco. Algunos se resuelven con páginas ya residentes o asignación inicial, otros requieren lectura de almacenamiento. Confundir todos los fallos con «RAM defectuosa» o «swap» lleva a diagnósticos equivocados.

El uso de swap no demuestra por sí solo falta de capacidad actual. Puede quedar contenido poco activo que no se necesita recuperar. Lo relevante es la actividad durante el problema: entradas/salidas, tiempos y conjunto activo. Deshabilitar swap como supuesto remedio universal puede reducir el margen del sistema y provocar terminación de procesos o fallos de asignación.

En Windows, el archivo de paginación también se relaciona con el compromiso y con ciertas configuraciones de volcados. Su tamaño no se fija con una regla universal basada únicamente en multiplicar RAM. Aprende a observar requisitos de carga, picos y configuración admitida. En estas prácticas no se cambia la política global del archivo de paginación de un equipo real.

## 6. Observación en Windows sin contadores localizados frágiles

Administrador de tareas y Monitor de recursos permiten empezar sin instalar software. Cambia a una vista por procesador lógico y observa memoria, disco y procesos durante la tarea. Las rutas y etiquetas de contadores pueden estar localizadas; un comando que usa nombres ingleses de Performance Monitor puede fallar en otra instalación. Primero enumera los disponibles o utiliza objetos con propiedades estables cuando sea apropiado.

En PowerShell, consultas iniciales son:

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Id, ProcessName, CPU, WorkingSet64
Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory
```

`CPU` es tiempo acumulado, no porcentaje instantáneo. `WorkingSet64` utiliza bytes; las propiedades de memoria de `Win32_OperatingSystem` tienen unidades documentadas y no se comparan directamente sin convertir. Una muestra tomada antes y otra después permite calcular diferencias, pero debes comprobar que se trata del mismo proceso y contemplar procesos que terminaron o comenzaron entre ambas.

No recojas líneas de comandos o listados completos de procesos de una organización sin necesidad: pueden contener rutas, documentos o parámetros sensibles. Para una memoria de prácticas basta el proceso sintético y los campos que sustentan tu hipótesis.

## 7. Evidencia de presión y correlación temporal

Una investigación de rendimiento necesita un eje temporal. Registra inicio y fin de la acción, intervalos de muestreo y cambios. Si una pausa aparece a las 10:03:15, una media de toda la mañana puede ocultarla. Por otro lado, muestrear demasiado frecuentemente añade carga y genera información difícil de interpretar. Elige una ventana proporcional al fenómeno.

En Linux, Pressure Stall Information puede aportar datos sobre tiempo en que tareas se retrasan por recursos, si el kernel y el entorno lo ofrecen. Consultar `/proc/pressure/memory`, `/proc/pressure/cpu` y `/proc/pressure/io` permite estudiar tendencias. No todas las VMs o contenedores presentan el mismo alcance y no hay un umbral universal que identifique avería. Relaciona el dato con el servicio y otros contadores.

Un registro de actividad de disco y presión de memoria que coincide con lentitud apoya una hipótesis de paginación, pero también puede haber otra tarea intensiva. La prueba siguiente debe separar consumidores, por ejemplo repetir con la aplicación de fondo detenida de forma ordenada en una VM. Mantén el resto de condiciones, conserva ambas mediciones y evita afirmar causalidad sólo por coincidencia.

## 8. Caso resuelto: navegador y máquina virtual

Un puesto con varias pestañas y una VM responde lentamente. Hipótesis: la carga activa supera memoria cómoda del anfitrión, la VM compite por CPU o el almacenamiento presenta latencia. Primero observa el anfitrión: recursos asignados a la VM, actividad total, presión de memoria y disco. Después observa el invitado. Medir sólo desde la VM puede ocultar la presión del anfitrión.

Si el invitado dispone de RAM aparentemente suficiente, pero el anfitrión pagina intensamente, asignarle todavía más puede empeorar el conjunto. La respuesta apropiada puede ser reducir carga concurrente o ajustar la asignación dentro de requisitos, antes de una ampliación física. Si una tarea satura un hilo y no hay presión de memoria, cerrar aplicaciones que apenas ocupan CPU podría no reducir el tiempo de esa tarea.

La conclusión debe relacionar cambio y resultado. «Al reducir una VM inactiva de forma controlada bajó la presión del anfitrión y mejoró la respuesta de la tarea medida» es más defendible que «Windows usa demasiada RAM». Registra también que la nueva configuración sigue siendo suficiente para las prácticas del invitado.

## 9. Práctica ampliada: línea temporal de una carga inocua

Usa dos aplicaciones habituales con datos sintéticos: editor y compresión de una carpeta de prueba pequeña. No generes procesos infinitos ni consumos de RAM deliberadamente capaces de agotar el equipo. Define una acción de 20–60 segundos, registra actividad antes/durante/después y repite tres veces. Conserva al menos una captura temporal o tabla de muestras con unidades.

Debes explicar dos contadores que aumentan, uno que no cambia de manera relevante y una limitación de la herramienta. Si la carga resulta demasiado breve, amplía moderadamente el conjunto de datos, no la agresividad del proceso. Deja el sistema en su estado inicial, cierra aplicaciones y conserva los archivos de prueba identificados.

Entrega una hipótesis, mediciones, interpretación y recomendación proporcionada. Rúbrica propia: diseño 25 %, unidades y medidas 25 %, correlación 25 %, límites y decisión 15 % y documentación/recuperación 10 %. Una recomendación de no ampliar hardware es válida cuando la evidencia no justifica la inversión.

## Fuentes primarias

- [Linux: conceptos de memoria](https://docs.kernel.org/admin-guide/mm/concepts.html).
- [Linux: PSI](https://docs.kernel.org/accounting/psi.html).
- [Debian: vmstat](https://manpages.debian.org/trixie/procps/vmstat.8.en.html).
- [Microsoft: métricas de memoria](https://learn.microsoft.com/windows/win32/memory/memory-performance-information).
- [Microsoft: conjunto de trabajo](https://learn.microsoft.com/windows/win32/memory/working-set).
- [Microsoft: introducción al archivo de paginación](https://learn.microsoft.com/troubleshoot/windows-client/performance/introduction-to-the-page-file).
