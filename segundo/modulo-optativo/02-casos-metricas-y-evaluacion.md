# Casos de soporte, métricas y evaluación

[Índice](README.md) · [Manual operativo](01-operacion-y-automatizacion-controlada.md)

## Caso 1. Una alerta de disco que no indica qué hacer

Una comprobación envía “disco al 90 %” cada cinco minutos. Nadie sabe qué volumen es ni qué retención debe aplicarse. Se propone borrar automáticamente el archivo más grande.

**Resolución:** identifica sistema de archivos, capacidad, crecimiento, inodos y servicio afectado. Relaciona umbral con margen de operación y una acción revisada. El archivo más grande puede ser una base de datos o la única copia utilizable, por lo que el tamaño no autoriza eliminarlo. Se registra responsable, contexto y una prueba de retorno si se realiza un cambio.

**Entregable:** alerta reescrita con objeto, instante, condición, enlace al procedimiento y estado. En el ensayo se utilizan datos sintéticos, sin llenar el sistema del anfitrión. Si no existe política de retención, la acción es obtener esa decisión, no inventarla.

## Caso 2. Plan de altas con dos conflictos

Un CSV sintético contiene cinco solicitudes: tres identidades nuevas, una repetida y otra ya existente con grupo diferente. Un script que ejecuta cada línea sin revisar puede duplicar intentos y modificar una cuenta ajena al propósito del lote.

**Resolución:** valida cabeceras y tipos; detecta duplicados dentro del lote y contrasta estado existente. El informe concilia cinco filas: tres candidatas nuevas, una duplicada y un conflicto que requiere decisión. El plan no contiene secretos y no crea objetos por sí mismo. La fase de aplicación, si se autoriza en laboratorio, vuelve a comprobar condiciones y registra cambios reales.

El resultado de una simulación no se describe como “usuarios creados”. Los estados correctos son planificado, omitido por duplicado, en conflicto, aplicado o fallido, según lo observado. La precisión del lenguaje evita que otra persona asuma accesos que todavía no existen.

## Caso 3. Tiempo medio que oculta una espera

Seis tickets sintéticos tienen tiempos de primera respuesta de 2, 3, 4, 4, 5 y 30 minutos. La media es `48 / 6 = 8 minutos`; la mediana es `(4 + 4) / 2 = 4 minutos`. Un informe que sólo presenta mediana puede ocultar el caso de treinta minutos, mientras otro que sólo presenta media no describe el centro de la serie.

**Resolución:** informa tamaño de muestra, definición del intervalo, media, mediana y observación de extremos. Separa primera respuesta y resolución. Comprueba si los tiempos incluyen horario no operativo y cómo se registran pausas. No mezcles métricas calculadas con reglas distintas.

La mejora no consiste en cerrar tickets sin validar para reducir un contador. Conserva reaperturas, cumplimiento de requisitos y calidad de documentación. Una respuesta rápida que concede permisos indebidos empeora el servicio aunque mejore el tiempo registrado.

## Caso 4. Ejecución parcial sin causa confirmada

La automatización recupera conectividad después de reiniciar una interfaz y un servicio a la vez. El informe atribuye la causa al servicio, pero no hay prueba que distinga ambas acciones.

**Resolución:** registra la recuperación y la incertidumbre. Conserva cambios y evidencias disponibles; diseña una prueba controlada en copia del laboratorio para investigar. No inventes una causa retrospectiva ni repitas reinicios en equipos reales para completar la explicación. Una mitigación puede ser útil y tener la causa pendiente.

## Taller integrador

En parejas, una persona plantea un ticket con información incompleta y otra produce hipótesis, plan y validación. Se usan VM y cuentas de prueba. Después se intercambian papeles y una tercera persona revisa si el procedimiento puede continuarse sin explicación oral.

Entregan ticket, datos sintéticos, plan de acciones, resultados, artículo de conocimiento y una mejora de la herramienta de lectura. Si no se ejecutó un paso, queda pendiente con su prueba prevista. La entrega distingue ejecución manual, automatizada y simulación.

| Criterio | Peso didáctico | Evidencia |
| --- | ---: | --- |
| Delimitación e hipótesis | 25 % | Pruebas que separan causas |
| Plan y control de cambios | 25 % | Objetos identificados y fallo parcial previsto |
| Validación | 25 % | Caso positivo, negativo y contexto de usuario |
| Métricas y documentación | 25 % | Definiciones, cálculos y relevo comprensibles |

La rúbrica es propia de la propuesta. Una herramienta con más líneas o más funciones no obtiene mejor valoración si no conserva los requisitos o no informa de errores. El objetivo es una intervención trazable, proporcionada y comprensible.
