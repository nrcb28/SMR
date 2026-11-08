# Revisión de la entrega

[Índice general](../README.md) · Fecha: 08/11/2026

## Comprobaciones realizadas

| Área | Comprobación y resultado |
| --- | --- |
| Organización curricular | Tabla de Madrid contrastada con BOCM de 15/11/2024 y tablas horarias del portal autonómico. Total de 2.000 horas; 30 semanales por curso en las casillas de la tabla. |
| Actualización normativa | Incorporadas Orden 3537/2025, catálogo de optativas y modificación 3822/2026, corrección del Decreto 27/2025 e instrucciones de 2026/2027. |
| Estructura | Índices de los 16 módulos/entradas del plan actual y de los tres históricos, con carpetas separadas por curso. |
| Navegación | Validador local de rutas, anclas, bloques cercados y documentos accesibles desde el README. Sin errores en la revisión de entrega. |
| Python | Compilación de los dos scripts y ejecución de la calculadora con IPv4, IPv6, `/31`, `/32`, prefijos extremos y entrada inválida. Resultados coherentes con `ipaddress`. |
| Inventario Linux | Sintaxis Bash revisada y ejecución de consultas locales sin instalación ni cambios de configuración. |
| Datos de ejemplo | Revisados importes y recuentos de CSV ofimáticos, cinco escenarios económicos, cálculos de energía y presupuesto del proyecto. |
| Ejemplo estático web | Revisados IDs, enlaces internos, anclas y referencia al CSS local. |
| Revisión cruzada | Lectura independiente de guías seleccionadas para detectar dependencias faltantes, recuperación de ACL, conflictos de servicios, aislamiento y coherencia de supuestos. |
| Publicación | Revisión de archivos vacíos y patrones de credenciales; sólo se incluyen texto, código de ejemplo y datos sintéticos. |

## Correcciones incorporadas durante la revisión

Se añadió `iperf3` y `tcpdump` a los procedimientos que los necesitan, se conservan rutas absolutas al exportar ACL y se utiliza `findmnt -T` para inspeccionar un directorio que puede pertenecer al sistema raíz. También se homogeneizó el periodo de cuatro semanas de un ejemplo económico y se precisó la temporalización del proyecto según las instrucciones del curso.

La revisión de web incluye el sitio predeterminado de Nginx y la resolución del nombre del CMS desde el propio servidor. La confianza TLS de las peticiones internas debe comprobarse con el mecanismo de CA de cada aplicación, además de la del navegador.

## Alcance de estas comprobaciones

Los comandos administrativos de las guías no se han ejecutado desplegando todas las VMs y servicios. Sus salidas se presentan como ejemplos o resultados esperados, con criterios para que el estudiante recoja la evidencia real. No se ha ejecutado WordPress, Firebird, LibreOffice ni PowerShell en este entorno; tampoco se dispone de PHP CLI para validar el ejemplo de mu-plugin. Las secciones correspondientes incluyen procedimientos y pruebas para su laboratorio de destino.

El validador de Markdown es una herramienta estática con el alcance documentado en su código. No comprueba disponibilidad de todos los enlaces externos, corrección semántica de todo el contenido, accesibilidad WCAG completa o compatibilidad con cualquier versión. Las referencias normativas principales y técnicas seleccionadas se consultaron en fuentes primarias durante la preparación.

Para repetir la comprobación de documentación, desde la raíz:

```bash
python3 scripts/validar_documentacion.py
python3 -m py_compile scripts/subredes.py scripts/validar_documentacion.py
bash -n scripts/inventario-linux.sh
```

Para validar una práctica administrativa utiliza la [matriz de aceptación](../recursos/plantillas/matriz-de-pruebas.md), identifica versiones y conserva sólo evidencias sanitizadas.
