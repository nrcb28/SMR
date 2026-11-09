# 6. Calc avanzado: modelos trazables y calidad de datos

[Índice](README.md) · [Datos del caso](ejemplos/modelo-costes.csv)

## 1. Separar entradas, reglas y resultados

Una hoja útil debe poder responder qué se ha supuesto, cómo se ha calculado y qué cambia al modificar una entrada. Si escribes importes finales directamente sobre fórmulas anteriores, el archivo puede parecer correcto y dejar de ser reproducible. Separa una hoja de datos importados, otra de parámetros y otra de resultados; reserva una zona de controles que detecte incoherencias.

En el caso de renovación del aula se comparan ocho partidas. Los precios son **supuestos didácticos**, sin pretensión de describir una oferta de mercado o una obligación fiscal. La columna de tasa también es una hipótesis para practicar cálculo. No reutilices estos porcentajes como criterio legal de facturación.

Importa [modelo-costes.csv](ejemplos/modelo-costes.csv) con UTF-8, separador `;` y coma decimal. Fija `codigo` como texto y verifica que cantidad, precio, descuento y tasa sean numéricos. Guarda como ODS antes de añadir fórmulas. El CSV conserva datos, pero no estilos, protección, hojas adicionales ni fórmulas que crees después.

| Columna | Campo | Interpretación |
| --- | --- | --- |
| A | codigo | Identificador de partida |
| B | categoria | Clasificación para agrupar |
| C | concepto | Descripción visible |
| D | cantidad | Número de unidades o paquetes |
| E | precio_unitario | Importe antes de descuento |
| F | descuento | Fracción entre 0 y 1 |
| G | tasa_supuesta | Fracción usada exclusivamente en el caso |
| H | escenario | Etiqueta inicial de la oferta |

Un identificador no es una cantidad: `0012` debe conservar ceros iniciales si forman parte de la clave. Darle formato «0000» a un número sólo cambia su representación; no recupera necesariamente el dato original al exportar. Decide el tipo antes de importar y contrasta primera y última fila.

## 2. Fórmulas y política de redondeo

Añade I `bruto`, J `descuento_importe`, K `neto`, L `tasa_importe` y M `total`. En la primera fila:

```text
I2: =REDONDEAR(D2*E2;2)
J2: =REDONDEAR(I2*F2;2)
K2: =I2-J2
L2: =REDONDEAR(K2*G2;2)
M2: =K2+L2
```

Copia hasta la fila nueve. Esta política redondea cada partida y suma sus resultados. Otra política podría calcular sobre un agregado y redondear al final; ambas pueden diferir en céntimos. Explica cuál aplicas y por qué corresponde al ejercicio. Mostrar dos decimales en pantalla no equivale a redondear el valor que participa en cálculos posteriores.

Los datos incluidos producen un bruto de **5.459,00**, descuento total de **191,90**, neto de **5.267,10**, tasa calculada de **1.106,09** y total de **6.373,19** con esa política. Contrasta por separado bruto menos descuento igual a neto y neto más tasa igual a total. Esos controles detectan omisiones y errores de signo, aunque no prueban que cada precio sea correcto.

Evita usar decimales binarios como si siempre fueran fracciones exactas. Las hojas trabajan con una representación numérica finita, por lo que valores aparentemente sencillos pueden tener una aproximación interna. Aplica redondeo cuando lo define la regla del modelo y no añadas `REDONDEAR` a todos los pasos sin motivo, porque también puedes acumular desviaciones.

## 3. Referencias absolutas, mixtas y nombres

Una celda con tasa común debe tener referencia fija, por ejemplo `Parametros.$B$2`, mientras la base de cada fila se desplaza. Si el porcentaje pertenece a cada partida, debe proceder de su fila. La diferencia es de modelo, no de sintaxis: fijar una referencia incorrecta produce un cálculo consistente pero conceptualmente equivocado.

Para una matriz de sensibilidad, coloca multiplicadores de precio en la fila dos y cantidades en la columna A. La celda B3 puede multiplicar `$A3*B$2`: la columna de cantidad queda fija y la fila de factor también. Copia en ambas direcciones y examina la fórmula de una celda interior. Si sólo compruebas la primera, podrías no detectar que las referencias se desplazan mal.

Los rangos con nombre facilitan lectura, pero necesitan gobernanza. Un nombre `TipoTasa` resulta más expresivo que una referencia aislada; debe apuntar al parámetro correcto y tener un ámbito claro. Al copiar hojas entre archivos, comprueba posibles conflictos de nombres. Una etiqueta comprensible no sustituye el diccionario que explica unidad, límite y origen de cada parámetro.

## 4. Validación y controles de integridad

Define cantidades enteras positivas, descuentos entre cero y uno, códigos únicos y categorías de una lista controlada. La validación de entrada ayuda al usuario, pero la importación, el pegado o una edición con otras herramientas pueden introducir valores que no han pasado por el diálogo de validación. Añade comprobaciones sobre el conjunto ya existente.

Ejemplos en español, con separador `;`:

```text
=CONTAR.SI($A$2:$A$9;A2)>1
=Y(ESNUMERO(D2);D2>0;D2=ENTERO(D2))
=Y(ESNUMERO(F2);F2>=0;F2<=1)
=SI(ESBLANCO(C2);"Falta descripción";"Completa")
```

El primer control detecta duplicidad de código, pero no decide automáticamente qué fila conservar. Un duplicado puede representar un error o una necesidad de cambiar la estructura, como separar un mismo producto por ubicación. Investiga antes de eliminar. Un campo vacío, una cadena vacía producida por fórmula y un cero tienen comportamientos y significados distintos.

Usa formato condicional para destacar incumplimientos y una columna textual con el motivo. El color aislado no explica el error ni es accesible para todas las personas. Añade un recuento general de incidencias de calidad; si es mayor que cero, el resumen debe indicar que los datos requieren revisión antes de usarse para decidir.

## 5. Fechas, horas y duraciones

La mayoría de las hojas representan fechas mediante un número de días respecto a una base configurada, y horas como fracciones de día. El formato determina cómo se muestran esos valores. Una cadena `03/04/2026` es ambigua entre convenciones; para intercambios usa una representación acordada como `2026-04-03` y selecciona explícitamente el patrón al importar.

Para construir una fecha evita concatenar textos regionales: `=FECHA(2026;4;3)` expresa año, mes y día. Para un seguimiento de tareas, resta fecha/hora final menos inicial y multiplica por 24 si quieres horas decimales. Si una tarea va de las 22:30 a las 01:15 del día siguiente, registrar sólo horas sin fecha puede producir un valor negativo. El dato completo elimina esa ambigüedad.

Una duración de 27 horas no debe mostrarse como si fuera la hora del día 03:00. Selecciona un formato de duración que permita superar 24 horas, de acuerdo con las opciones de la suite. Si utilizas `[HH]:MM`, comprueba su resultado en la versión receptora. Al exportar a CSV, incluye la unidad o conserva minutos enteros para facilitar el intercambio.

No calcules antigüedad exacta dividiendo días por 365 sin explicar la aproximación: años bisiestos y reglas de negocio pueden cambiar el resultado. Para una fecha de mantenimiento, normalmente es más claro determinar una próxima fecha según la política pactada y compararla con una fecha de corte fija. `HOY()` es útil para un panel vivo, pero altera la clasificación de un informe histórico al abrirlo otro día.

## 6. Agregación, tablas dinámicas y búsquedas

Para sumar neto por categoría utiliza `SUMAR.SI`; para combinar categoría y escenario, `SUMAR.SI.CONJUNTO`:

```text
=SUMAR.SI($B$2:$B$9;"Equipos";$K$2:$K$9)
=SUMAR.SI.CONJUNTO($K$2:$K$9;$B$2:$B$9;"Equipos";$H$2:$H$9;"Base")
```

Todos los intervalos deben tener dimensiones coherentes. Si una condición se almacena en una celda, referencia esa celda en lugar de duplicar el literal en muchas fórmulas. En criterios con operadores, forma la expresión de manera explícita, por ejemplo `">="&Parametros.$B$5` para una fecha o umbral. Revisa configuración de comodines y expresiones regulares cuando las claves contengan caracteres especiales.

Una tabla dinámica puede agrupar por categoría y sumar neto, descuento y total. Añade un total general y contrástalo con las fórmulas originales. Tras añadir filas al CSV y reimportar, comprueba que el origen de la tabla incluya las filas nuevas; actualizar la tabla no amplía necesariamente un rango definido de forma fija. Mantén la fuente en un rango controlado y documenta el procedimiento de ampliación.

Para buscar por código en versiones compatibles se puede usar BUSCARX. La guía inicial incluye alternativa `INDICE`/`COINCIDIR` para versiones que no reconocen esa función. No conviertas un «no encontrado» en cero si después vas a sumar precios: hacerlo podría infravalorar el presupuesto sin advertencia. Devuelve un texto de diagnóstico y bloquea conceptualmente la aceptación del resultado hasta corregirlo.

## 7. Escenarios y sensibilidad

Un escenario es un conjunto coherente de supuestos, no una copia del archivo a la que se cambian cifras sin registro. Define base, aumento de precios y reducción de alcance. Para cada uno identifica qué partidas cambian y cuáles permanecen fijas. Un aumento del 10 % en equipos no implica un aumento del 10 % en instalación, porque son componentes distintos.

Ejemplo: el neto de la categoría Equipos es 3.420,00. Si sube un 10 % manteniendo el resto, añade 342,00 al neto y calcula de nuevo la tasa con la política elegida. Si reduces doce monitores a diez, el ahorro depende del precio y descuento de esa partida; no apliques un porcentaje al total general. El análisis de sensibilidad debe seguir las relaciones causales del modelo.

Con la política de redondeo por partida ya definida, las comprobaciones de referencia son:

| Escenario sintético | Cambio de entrada respecto a la base | Neto | Tasa supuesta | Total |
| --- | --- | ---: | ---: | ---: |
| Base | Ocho partidas originales | 5.267,10 | 1.106,09 | 6.373,19 |
| Equipos +10 % | Precio unitario de P-001 de 600,00 a 660,00; conserva descuento y cantidad | 5.609,10 | 1.177,91 | 6.787,01 |
| Dos monitores menos | Cantidad de P-002 de doce a diez; conserva precio y demás partidas | 5.067,10 | 1.064,09 | 6.131,19 |

Los escenarios se calculan por separado sobre la base; no acumules el aumento de equipos y la reducción de monitores salvo que definas un cuarto escenario combinado. Esta tabla permite contrastar la hoja, pero debes conservar tus fórmulas y la explicación del cambio: copiar el total no demuestra que el modelo responda a otra entrada.

Para un coste anual de propiedad, distingue desembolso, gasto operativo y amortización didáctica. Si un activo supuesto de 3.420,00 se reparte linealmente en cuatro años, la asignación anual es 855,00 bajo esa hipótesis, con valor residual cero. Eso no significa que se paguen 855,00 cada año ni establece un tratamiento contable o fiscal real. Evita sumar la compra completa y su amortización anual como si fueran dos pagos distintos.

Añade consumo medido o estimado por separado: potencia en kW por horas genera kWh, que después se multiplica por un precio supuesto. Una potencia de catálogo no equivale a consumo constante. Presenta un intervalo o varios perfiles de carga cuando la incertidumbre sea relevante y no mezcles unidades entre W y kW.

## 8. Auditoría de una hoja y entrega

Oculta temporalmente los resultados almacenados de tu razonamiento: elige una fila y calcula a mano su importe. Después modifica cantidad, descuento y tasa por separado y predice qué celdas deben cambiar. Si aparece un cambio fuera de esas dependencias, investiga referencias incorrectas o una fórmula copiada de manera desigual.

Comprueba al menos una entrada límite y una inválida: cantidad uno, descuento cero, descuento completo si el modelo lo permite, código duplicado y precio como texto. No valides el archivo únicamente con datos «bonitos». Registra qué comportamiento esperas y qué se observa realmente, incluyendo advertencias y bloqueos de entrada.

Antes de entregar, muestra unidades y fecha de corte, identifica las celdas editables y conserva la hoja de datos original. La protección de celdas reduce cambios accidentales; para información confidencial se necesita una política de acceso y cifrado apropiada. Abre una copia en la suite receptora y fuerza recálculo: ver valores anteriores no demuestra compatibilidad de fórmulas.

## 9. Práctica avanzada de modelización

Entrega un ODS con hojas `Datos`, `Parametros`, `Calculo`, `Escenarios` y `Control`. Las denominaciones no son obligatorias, pero la separación de responsabilidades sí debe ser explicable. Incluye el CSV original y una memoria corta que detalle tipos, redondeo y referencias.

La aceptación exige reproducir los cinco totales de referencia, detectar un código duplicado añadido a una copia, actualizar un resumen al incorporar una partida y comparar dos escenarios sin sobrescribir la base. Añade una prueba de intercambio XLSX o PDF según la necesidad: el primero conserva un modelo editable con posibles diferencias; el segundo comunica una representación y no reemplaza el cálculo original.

Rúbrica propia: calidad y trazabilidad de entradas 25 %, fórmulas y controles 30 %, escenarios y unidades 20 %, compatibilidad y presentación 15 %, pruebas y memoria 10 %. Un total correcto con una fórmula que no se adapta a las entradas no recibe la misma valoración que un modelo reproducible.

## Referencias primarias

- [Ayuda de funciones Calc](https://help.libreoffice.org/latest/es/text/scalc/01/04060100.html): consulta el nombre y la sintaxis de la instalación.
- [SUMAR.SI.CONJUNTO](https://help.libreoffice.org/latest/es/text/scalc/01/func_sumifs.html): intervalos, criterios y configuración de coincidencia.
- [BUSCARX en LibreOffice](https://help.libreoffice.org/latest/es/text/scalc/01/func_xlookup.html): disponibilidad y compatibilidad.
- [Guías de Calc](https://books.libreoffice.org/): hojas, datos, fechas y escenarios.
- [Funciones de Excel en Microsoft Support](https://support.microsoft.com/es-es/excel): verifica equivalencias en el producto receptor.
