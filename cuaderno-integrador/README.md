# Cuaderno integrador de SMR

[Índice general](../README.md) · [Laboratorio común](../docs/laboratorio.md)

Este cuaderno reúne problemas que exigen combinar varias asignaturas. Su finalidad es pasar de saber ejecutar una instrucción a justificar un diseño, reconocer una avería y demostrar que una recuperación cumple el objetivo. Los casos, cifras, tiempos y resultados de ejemplo son sintéticos; no describen una empresa ni una implantación real.

## Itinerario

| Capítulo | Qué se trabaja | Producto de aprendizaje |
| --- | --- | --- |
| [Magnitudes, capacidad y rendimiento](01-magnitudes-y-calculos-resueltos.md) | Unidades, transferencias, colas, crecimiento, disponibilidad, energía y decisiones de capacidad | Cálculo reproducible con hipótesis y análisis de sensibilidad |
| [Incidencias encadenadas](02-incidencias-encadenadas.md) | Investigación de fallos que atraviesan hardware, SO, red, identidad y aplicación | Línea temporal, pruebas discriminantes y cierre con causa demostrada |
| [Simulacro práctico de primero](03-simulacro-primero.md) | Equipo, puesto, red, datos y prevención | Memoria completa con solución comentada y rúbrica didáctica |
| [Simulacro práctico de segundo](04-simulacro-segundo.md) | DNS, servicios, permisos, web, continuidad y comunicación | Dossier de aceptación desde cliente y recuperación medida |
| [Entrega técnica y operación](05-entrega-y-operacion.md) | Requisitos, decisiones, cambios, runbooks y transferencia del servicio | Documentación que otra persona pueda utilizar para operar el sistema |

Los simulacros permiten ocultar la solución y realizar primero el enunciado. Sus tiempos y ponderaciones sirven para entrenar; la programación del centro determina los instrumentos de evaluación oficiales. Las soluciones explican decisiones aceptables y sus límites, sin exigir que todas las instalaciones reproduzcan una captura concreta.

## Forma de trabajo

Antes de calcular, identifica unidad, población, intervalo y supuesto. Antes de configurar, identifica máquina, interfaz, archivo y privilegios. Antes de aceptar, define el estímulo que usarás y el resultado observable que demostraría el cumplimiento. Si el resultado no aparece, registra lo obtenido y modifica tu hipótesis.

Usa la [memoria de práctica](../recursos/plantillas/memoria-practica.md), la [matriz de pruebas](../recursos/plantillas/matriz-de-pruebas.md) y el [método de diagnóstico](../docs/metodo-de-diagnostico.md). Las pruebas de los servicios se realizan en el laboratorio aislado. Los ejemplos no autorizan intervenciones sobre equipos ajenos.

## Datos y herramienta de análisis

El archivo [mediciones-transferencia.csv](datos/mediciones-transferencia.csv) contiene ocho mediciones sintéticas de una transferencia de 64 MiB. La herramienta [analizar_mediciones.py](../scripts/analizar_mediciones.py) comprueba los datos y calcula media, mediana, percentil 95 por rango más próximo y tasas de transferencia, sin acceder a la red:

```bash
python3 scripts/analizar_mediciones.py cuaderno-integrador/datos/mediciones-transferencia.csv
```

Estos datos permiten reproducir los cálculos del primer capítulo. La herramienta informa de errores de formato y de valores inválidos; no convierte una serie de datos inventados en una medición de rendimiento del equipo donde se ejecute.
