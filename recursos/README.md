# Recursos compartidos

[Índice general](../README.md) · [Laboratorio](../docs/laboratorio.md)

## Plantillas

| Archivo | Finalidad |
| --- | --- |
| [Memoria de práctica](plantillas/memoria-practica.md) | Explicar objetivo, entorno, procedimiento, resultados y recuperación |
| [Ficha de incidencia](plantillas/incidencia.md) | Registrar alcance, hipótesis, pruebas y causa confirmada |
| [Matriz de pruebas](plantillas/matriz-de-pruebas.md) | Comparar requisito, prueba positiva/negativa y evidencia real |
| [Plan de copias](plantillas/plan-de-copias.md) | Relacionar datos, RPO/RTO, retención y restauración |
| [Decisión técnica](plantillas/decision-tecnica.md) | Comparar alternativas y conservar criterios, consecuencias y condiciones de revisión |
| [Plan de cambio](plantillas/plan-de-cambio.md) | Preparar ejecución, aceptación y vuelta atrás de una intervención |
| [Procedimiento operativo](plantillas/procedimiento-operacion.md) | Redactar un runbook con precondiciones, resultados y condiciones de parada |
| [Inventario sintético CSV](inventario-ejemplo.csv) | Practicar importación y documentación sin usar datos de personas |

Copia la plantilla a tu espacio de trabajo y sustituye sus campos por datos observados. Los campos entre corchetes identifican lo que debes completar; no son respuestas a entregar. Conserva las evidencias sensibles fuera de Git.

## Herramientas sin dependencias externas

Los scripts Python requieren **Python 3.9 o posterior**. Utilizan únicamente su biblioteca estándar y no necesitan paquetes de `pip`. Los inventarios requieren Bash y utilidades GNU habituales en Debian o PowerShell con CIM en Windows, según corresponda.

| Herramienta | Ejecución desde la raíz | Efecto |
| --- | --- | --- |
| [Validador de documentación](../scripts/validar_documentacion.py) | `python3 scripts/validar_documentacion.py` | Lee Markdown e inventario curricular y presenta errores o resumen |
| [Calculadora de prefijos](../scripts/subredes.py) | `python3 scripts/subredes.py 192.168.56.20/27` | Calcula dirección de red, prefijo, rango y broadcast cuando corresponde |
| [Inventario Linux](../scripts/inventario-linux.sh) | `bash scripts/inventario-linux.sh` | Consulta SO, CPU, memoria y discos; no instala ni configura |
| [Inventario Windows](../scripts/inventario-windows.ps1) | `powershell -NoProfile -File scripts/inventario-windows.ps1` | Consulta versión, CPU, memoria y discos; sin requerir cambio de política global |
| [Inventario del plan](plan-estudios-madrid.json) | Lectura directa o desde el validador | Relaciona códigos, carga horaria y carpetas |
| [Generador del índice](../scripts/generar_indice.py) | `python3 scripts/generar_indice.py` | Actualiza únicamente el índice de navegación; `--check` compara sin escribir |
| [Analizador de mediciones](../scripts/analizar_mediciones.py) | `python3 scripts/analizar_mediciones.py cuaderno-integrador/datos/mediciones-transferencia.csv` | Valida un CSV y calcula estadísticas y caudal; no genera tráfico |

Los inventarios omiten deliberadamente números de serie, nombres de usuario, direcciones MAC y claves. Aun así revisa la salida antes de compartirla: el modelo del equipo, los volúmenes y su tamaño pueden revelar detalles de tu entorno. Si Windows bloquea la ejecución según la política de tu organización, revisa el archivo y utiliza el procedimiento autorizado de tu centro; no cambies la política global para una práctica.

La calculadora usa `ipaddress` de la biblioteca estándar. Para un prefijo IPv4 normal excluye dirección de red y broadcast al contar hosts; distingue `/31` y `/32`. En IPv6 presenta el intervalo matemático del prefijo y explica que no existe broadcast ni un conteo universal de hosts utilizables. Contrasta los resultados con el ejercicio resuelto de [Redes locales](../primero/redes-locales/README.md).

El [cuaderno integrador](../cuaderno-integrador/README.md) contiene datos sintéticos de mediciones, presupuesto y matriz de aceptación. El analizador expresa los decimales como cadenas JSON para conservar su representación y documenta el método de percentil empleado. No mide el rendimiento del equipo: calcula sobre los datos que se le proporcionan.
