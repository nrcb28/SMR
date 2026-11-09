# Revisión de las entregas

[Índice general](../README.md) · Primera edición: 08/11/2026 · Ampliación: 09/11/2026

## Comprobaciones realizadas

| Área | Comprobación y resultado |
| --- | --- |
| Organización curricular | Tabla de Madrid contrastada con BOCM de 15/11/2024 y tablas horarias del portal autonómico. Total de 2.000 horas; 30 semanales por curso en las casillas de la tabla. |
| Actualización normativa | Incorporadas Orden 3537/2025, catálogo de optativas y modificación 3822/2026, corrección del Decreto 27/2025 e instrucciones de 2026/2027. |
| Estructura | Índices de los 16 módulos/entradas del plan actual y de los tres históricos, con carpetas separadas por curso. |
| Navegación | Validador local de rutas, anclas, bloques cercados y documentos accesibles desde el README. Sin errores en la revisión de entrega. |
| Python | Compilación de scripts y ejecución de la calculadora con IPv4, IPv6, `/31`, `/32`, prefijos extremos y entrada inválida. Resultados coherentes con `ipaddress`. |
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

## Revisión de la ampliación del 09/11/2026

Se mantienen las guías iniciales y se revisan las nuevas monografías, los ejemplos de código/datos, los casos profesionales y el cuaderno integrador. Las comprobaciones se ajustan al tipo de material: una salida sintética permite verificar un cálculo, mientras una instalación administrativa necesita ejecutarse en su laboratorio de destino para aportar evidencia funcional.

### Datos, cálculo y scripts locales

La muestra del analizador de transferencias produce ocho observaciones, media de 1.250 ms, mediana de 1.010 ms, p95 por rango más próximo de 3.000 ms y caudal agregado de 51,2 MiB/s. Se han comprobado cabeceras duplicadas y valores numéricos extremos: el CLI informa de error con código 2, sin presentar una traza como resultado válido.

Los presupuestos, VLSM y cronología de los simulacros se han contrastado por separado. En IPE se han revisado mezcla de servicios, tres meses de tesorería, conciliación, nómina con hipótesis didácticas y equilibrio entero mediante Decimal; las rúbricas nuevas revisadas suman 100 %.

El manifiesto Bash del módulo de Sistemas monopuesto se ha comprobado con datos temporales y nombres especiales, verificación SHA, bloqueo concurrente, rechazo de salida anidada y conservación del informe anterior ante origen vacío. El generador PowerShell de planes se ha revisado estáticamente; no crea cuentas automáticamente ni se ha ejecutado PowerShell en este entorno.

El ejemplo frontend de registro local pasa comprobación de sintaxis y nueve casos de reglas de validación en Node, además de revisión estática de IDs, asociaciones ARIA, anclas y recursos HTML. Se intentó la prueba en Chromium: el sandbox bloqueó una operación de socket y el intento fuera del sandbox no devolvió el DOM. No se presenta como una prueba visual, funcional de navegador o auditoría WCAG completada. Los modelos Calc incluyen los totales de sus escenarios y se ha contrastado su aritmética con Decimal.

### Coherencia entre módulos y referencias

Se ha resuelto una colisión de direccionamiento: `.56.30` queda para la secundaria DNS opcional y `.56.50` para la reserva DHCP de prácticas. Se ha precisado la semántica de `allow-notify`, la diferencia entre filtrado y denegación de una transferencia DNS, y el alcance de un usuario SFTP restringido. Estas configuraciones se describen para su ejecución en VMs, sin afirmar que se hayan desplegado durante la revisión editorial.

Las referencias de protocolos se han contrastado con RFC Editor, incluyendo las especificaciones de 2026 para DHCPv6 y DMARC y su relación con documentos anteriores. La ampliación laboral distingue las plantillas antiguas usadas para nuevas contrataciones y el régimen transitorio de contratos previos al RD 1065/2025. Cada capítulo conserva su fuente y fecha cuando corresponde.

### Navegación y alcance

Se añade un índice completo regenerable y se actualizan las rutas de estudio de los módulos. Las pruebas de estructura comprueban los enlaces locales, anclas, cercas, inventario curricular y acceso a documentos desde el README. Los archivos de configuración y las explicaciones administrativas requieren sus pruebas de servicio en el entorno indicado; una validación editorial no equivale a desplegar todas las combinaciones de versiones y topologías.

En el cierre de la ampliación, el inventario contiene 189 archivos y 156 documentos Markdown; el validador comprueba 809 enlaces locales sin errores. El [mapa de ampliación](novedades-ampliacion.md) compara la primera edición con la actual y el [índice completo](../INDICE.md) permite localizar los nuevos capítulos.
