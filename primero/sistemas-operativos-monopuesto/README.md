# Sistemas operativos monopuesto · 0222

Guía técnica de primer curso de SMR para la Comunidad de Madrid. Estudia cómo un sistema operativo convierte el hardware en un entorno utilizable, aísla procesos, gestiona almacenamiento y permite administrar un puesto con Linux y Windows.

El trabajo se plantea como administración reproducible: observar el estado, planificar un cambio, ejecutarlo con el privilegio mínimo, comprobar su efecto y conservar una vía de recuperación. Se proponen actividades originales y criterios didácticos; la programación y evaluación oficiales corresponden al centro.

## Documentos y recorrido

| Documento | Contenido | Resultado práctico |
| --- | --- | --- |
| [01 · Fundamentos](01-fundamentos.md) | Kernel, procesos, memoria, archivos, permisos y virtualización | Explicar un fallo por capas |
| [02 · Guía técnica](02-guia-tecnica.md) | Instalación, administración Linux/Windows, paquetes, servicios y copias | Puesto instalado y mantenible |
| [03 · Prácticas](03-practicas.md) | Instalación comparada, permisos y recuperación | Evidencias de configuración y restauración |
| [04 · Diagnóstico y evaluación](04-diagnostico-y-evaluacion.md) | Casos, preguntas resueltas y comprobación final | Informe de incidencia verificable |
| [05 · Arranque y recuperación](05-arranque-y-recuperacion.md) | UEFI/ESP, cargadores, kernel/initramfs, BCD, cifrado y entornos de rescate | Identificar etapa de fallo y preservar datos antes de reparar |
| [06 · Procesos y memoria](06-procesos-memoria-y-observabilidad.md) | Tiempo de CPU/pared, estados, memoria virtual/residente, caché, swap y PSI | Línea temporal con métricas y diagnóstico proporcional |
| [07 · Archivos y permisos efectivos](07-archivos-permisos-y-consistencia.md) | Inodos, enlaces, ACL/máscara, NTFS, espacio y consistencia | Explicar accesos permitidos/denegados y diferencias de contadores |
| [08 · Automatización y taller resuelto](08-automatizacion-y-taller-resuelto.md) | Bash/PowerShell, manifiestos, bloqueo, tareas programadas y dieciséis problemas | Automatización comprobable con errores previstos y retirada |
| [09 · Alineación por RA](09-alineacion-ra.md) | Los 5 resultados y 41 criterios oficiales, vinculados a materiales y actividades | Identificar qué debe observarse en cada criterio |
| [10 · Retos por RA](10-retos-por-ra.md) | Representación, archivos, instalación, configuración, administración y virtualización | Dossier ejecutado con comprobaciones y recuperación |

La ampliación 05–08 desarrolla administración por capas y añade prácticas de recuperación, observación temporal, ACL y programación. Los [ejemplos Bash](ejemplos/ampliacion/manifiesto.sh) y [PowerShell](ejemplos/ampliacion/manifiesto.ps1) son herramientas educativas de manifiestos para árboles sintéticos: no son un sistema de backup. Su contrato, alcance, ejecución y casos negativos se explican en el capítulo 08.

Lee antes [Montaje y mantenimiento de equipos](../montaje-y-mantenimiento-de-equipos/README.md), especialmente firmware y almacenamiento. Utiliza el [laboratorio común](../../docs/laboratorio.md). Las prácticas de modificación se realizan en máquinas virtuales desechables, con datos ficticios, consola disponible y punto de recuperación.

## Sistemas de referencia

- **Debian 13 amd64:** instalación desde medios oficiales, shell Bash y servicios gestionados con systemd. Algunos comandos requieren paquetes opcionales.
- **Windows 11 Pro:** versión con soporte, recursos y hardware virtual admitidos, licencia o evaluación legítima. Se utiliza PowerShell y administración local; las características dependen de edición y compilación.

Las rutas de menús cambian entre versiones. Aprende también el objeto que estás administrando —servicio, partición, cuenta o ACL— para poder localizarlo si cambia la interfaz. Windows Home no ofrece exactamente las mismas herramientas de administración que Pro.

## Capacidades que se trabajan

| Capacidad orientativa | Evidencia de dominio |
| --- | --- |
| Identificar la función del SO | Relacionar proceso, memoria, sistema de archivos y controlador con un síntoma |
| Instalar y parametrizar | Justificar firmware, particionado, cuentas, actualizaciones y recuperación |
| Administrar usuarios y recursos | Aplicar permisos mínimos y demostrar accesos permitidos y denegados |
| Mantener y automatizar | Gestionar paquetes, servicios y tareas con registro de cambios |
| Recuperar y documentar | Restaurar datos de prueba y resolver una incidencia sin cambios indiscriminados |

Esta organización no inventa numeraciones de resultados de aprendizaje oficiales. Consulta el contexto curricular en el [inicio del repositorio](../../README.md).

El [mapa de RA](09-alineacion-ra.md) conserva la numeración del referente oficial y diferencia los resúmenes didácticos de criterios de sus enunciados normativos. Los [retos](10-retos-por-ra.md) amplían representación y codificación, sistemas transaccionales y comparación práctica de virtualizadores. Consulta la [trazabilidad JSON](alineacion-ra.json) para relacionar los cinco RA y 41 CE con entregables y aceptación, dejando pendientes las pruebas que no hayas realizado.

## Fuentes primarias

- [Instalación de Debian 13](https://www.debian.org/releases/trixie/installmanual).
- [Referencia de Debian](https://www.debian.org/doc/manuals/debian-reference/).
- [Documentación del kernel Linux](https://docs.kernel.org/).
- [Microsoft Learn: Windows](https://learn.microsoft.com/windows/).
- [Microsoft Learn: PowerShell](https://learn.microsoft.com/powershell/).
- [Documentación de systemd](https://www.freedesktop.org/software/systemd/man/latest/).
