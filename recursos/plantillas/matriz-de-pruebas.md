# Matriz de pruebas de aceptación

[Recursos](../README.md)

Define cada criterio antes de ejecutar la prueba. Conserva resultado real y evidencia; no copies el resultado esperado a la columna de resultado obtenido.

| ID | Requisito | Preparación/identidad | Estímulo | Resultado esperado | Resultado obtenido | Evidencia | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [P01] | [Comportamiento] | [Máquina, versión y permisos] | [Consulta/acción] | [Dato verificable] | [Dato observado] | [Referencia] | [Pendiente/cumple/falla] |

## Casos que conviene cubrir

- Funcionamiento correcto desde un cliente independiente.
- Acceso denegado a una identidad que carece de permisos.
- Persistencia después del evento pertinente: reinicio, renovación o nueva sesión.
- Respuesta ante entrada inválida o recurso inexistente.
- Recuperación desde copia en un destino distinto.
- Integridad de datos y tiempo de recuperación cuando formen parte del requisito.

## Resumen de aceptación

[Requisitos cumplidos, defectos abiertos, impacto real, decisión justificada y fecha. Una prueba que no se ha ejecutado permanece pendiente.]
