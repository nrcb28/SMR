# Cómo contribuir

Gracias por ayudar a mantener guías reproducibles y claras. Propón correcciones con el archivo y la sección afectados, la versión del entorno y una explicación del problema.

## Cambios de documentación

1. Lee la guía completa y el [laboratorio común](docs/laboratorio.md).
2. Consulta una fuente primaria apropiada para la versión.
3. Explica el concepto y el propósito de cada procedimiento nuevo.
4. Incluye comprobación, errores previsibles y recuperación cuando el cambio administre un sistema.
5. Mantén enlaces relativos dentro del repositorio y una línea en blanco antes de listas y tablas.
6. Ejecuta `python3 scripts/validar_documentacion.py` desde la raíz.

Los resultados que no hayas ejecutado deben identificarse como ejemplos o resultados esperados. Si has realizado una prueba, registra versión, entorno, pasos y evidencia mínima sanitizada. No atribuyas una rúbrica propia a la normativa oficial.

## Incidencias técnicas

Indica síntoma, pasos de reproducción, resultado esperado y real. Añade extractos breves de logs sin secretos, información personal ni datos de clientes. Una captura sin contexto puede resultar insuficiente; identifica máquina, servicio y momento de la prueba.

Si se modifica una dirección, nombre DNS, rol de servidor o versión base, revisa los módulos que dependen de ello. Separa los escenarios de DNS de servicios y DNS del directorio. No propongas contraseñas incrustadas o un comando destructivo sin identificación previa del objeto, ámbito de laboratorio y procedimiento de recuperación.

## Cambios curriculares

Incluye norma, fecha, enlace oficial y tabla o apartado aplicable. Actualiza [currículo](docs/curriculo-madrid.md), [inventario JSON](recursos/plan-estudios-madrid.json), índices de curso y enlaces afectados. La oferta de optativas requiere conocer el centro; no asignes una optativa concreta a todo Madrid a partir de un único ejemplo.
