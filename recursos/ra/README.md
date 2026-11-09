# Datos y seguimiento de resultados de aprendizaje

[Índice general](../../README.md) · [Mapa curricular](../../docs/mapa-ra.md) · [Cómo trabajar por RA](../../docs/evaluacion-por-ra.md)

## Archivos

| Recurso | Contenido y uso |
| --- | --- |
| [Referentes oficiales](referentes-oficiales.json) | Enunciados RA, letras y textos de criterios, con referencias a BOE/BOCM |
| [Fuentes verificadas](fuentes-verificadas.json) | URL y huellas de los documentos originales consultados |
| [Inventario del mapa](mapa-ra.json) | Códigos, rutas de alineación y recuentos de RA/CE |
| [Plantilla de seguimiento](plantilla-seguimiento-ce.csv) | Una fila por criterio, con actividad, evidencia esperada y campos vacíos para observación real |

Cada módulo común y cada código optativo tiene su propio `alineacion-ra.json`. Ese archivo vincula el referente con la guía, los retos y las comprobaciones. Las rutas son relativas a la raíz del repositorio y pueden señalar un ancla dentro de un documento.

## Leer una alineación

`modulo` conserva el código oficial como texto, incluidos ceros y sufijos de idioma. `fuentes` identifica norma, URL, localizador y fecha. `resultados` mantiene el número y el enunciado del RA; `criterios` contiene la letra, un resumen didáctico y la relación con una actividad, evidencia y aceptación.

Las `actividades` declaran un identificador estable, título, guía desarrollada, criterios asociados, entregables y comprobaciones. El procedimiento se encuentra en el documento enlazado. Declarar una actividad en el JSON no sustituye su desarrollo ni la evidencia que el estudiante obtenga al realizarla.

Un criterio se identifica mediante su letra, salvo que la publicación repita una. Proyecto RA5 conserva dos criterios a), distinguidos con `clave` a.1 y a.2. Esa clave editorial permite trazabilidad sin cambiar las letras oficiales. Los criterios con ñ se mantienen como tales; no se fusionan con el anterior.

## Trabajar con la plantilla

Copia el CSV antes de usarlo como registro. Se distribuye en UTF-8 y con separador punto y coma. Las columnas de resultado real, fecha y observaciones están vacías, y el estado inicial es `sin_realizar`. Importa el archivo con esos parámetros y define la columna `modulo` como texto para conservar los ceros iniciales de códigos como `0221`.

En el registro personal identifica el ejercicio y el artefacto obtenido. Conserva datos mínimos y respeta las instrucciones de privacidad del centro. El repositorio no contiene calificaciones, identidades de estudiantes ni evidencias personales de ejecución.

La regeneración reemplaza únicamente la plantilla base publicada y los mapas generados. No utilices su ruta para conservar tu único registro personal. La [guía de trabajo por RA](../../docs/evaluacion-por-ra.md) propone estados de seguimiento y explica cómo interpretar pendientes y revisiones.

## Comprobación y regeneración

```bash
python3 scripts/validar_ra.py
python3 scripts/generar_mapa_ra.py
python3 scripts/generar_mapa_ra.py --check
python3 scripts/generar_indice.py
python3 scripts/validar_documentacion.py
```

El validador comprueba códigos, secuencias, enunciados, claves de criterios, relaciones con actividades y enlaces. No interpreta semánticamente una captura ni acredita una competencia del alumnado. Las cifras de variantes optativas cuentan cada código de lengua por separado aunque varias compartan currículo.
