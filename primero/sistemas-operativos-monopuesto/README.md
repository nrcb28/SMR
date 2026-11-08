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

## Fuentes primarias

- [Instalación de Debian 13](https://www.debian.org/releases/trixie/installmanual).
- [Referencia de Debian](https://www.debian.org/doc/manuals/debian-reference/).
- [Documentación del kernel Linux](https://docs.kernel.org/).
- [Microsoft Learn: Windows](https://learn.microsoft.com/windows/).
- [Microsoft Learn: PowerShell](https://learn.microsoft.com/powershell/).
- [Documentación de systemd](https://www.freedesktop.org/software/systemd/man/latest/).
