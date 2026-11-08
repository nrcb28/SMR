# Plan de copias y restauración

[Recursos](../README.md) · [Seguridad informática](../../segundo/seguridad-informatica/README.md)

## Datos y objetivos

| Conjunto | Responsable/rol | Tamaño y crecimiento | RPO objetivo | RTO objetivo | Dependencias |
| --- | --- | --- | --- | --- | --- |
| [Archivos, base de datos, configuración] | [Rol] | [GiB/periodo] | [Tiempo] | [Tiempo] | [Claves, DNS, aplicación] |

## Política propuesta

| Tipo de copia | Frecuencia | Destino separado | Retención | Cifrado y custodia de clave | Verificación |
| --- | --- | --- | --- | --- | --- |
| [Completa/incremental/lógica] | [Calendario] | [Medio] | [Periodos] | [Procedimiento sin claves] | [Resultado de integridad y restauración] |

Justifica coherencia de aplicaciones: copiar archivos de una base de datos en ejecución no garantiza una copia consistente. Describe el mecanismo de exportación o backup compatible y cómo se recuperan configuración, datos y secretos de forma coordinada.

## Ensayo de restauración

1. Identificar el incidente y el punto de recuperación.
2. Preparar un destino aislado sin sobrescribir la única copia de los datos.
3. Recuperar claves por el canal previsto.
4. Restaurar dependencias, configuración y datos en orden.
5. Comprobar integridad, identidad, permisos y funcionamiento desde cliente.
6. Medir tiempo real y pérdida real de datos.
7. Comparar con RTO/RPO y documentar desviaciones.

| Fecha | Copia utilizada | Destino de ensayo | Tiempo real | Pérdida de datos | Prueba funcional | Mejora |
| --- | --- | --- | --- | --- | --- | --- |
| [Dato] | [Identificador] | [Laboratorio] | [Duración] | [Intervalo] | [Evidencia] | [Acción] |
