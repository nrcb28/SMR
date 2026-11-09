# Magnitudes, capacidad y rendimiento: problemas resueltos

[Cuaderno integrador](README.md) · [Redes locales](../primero/redes-locales/README.md) · [Seguridad](../segundo/seguridad-informatica/README.md)

## 1. Método para que una cifra tenga significado

Un resultado numérico necesita magnitud, unidad, intervalo y método. «El servidor va a 100» no permite saber si se habla de Mbit/s, MB/s, IOPS, porcentaje de CPU o milisegundos. Escribe siempre qué se mide y en qué punto del sistema: bytes de aplicación, tráfico del enlace, tiempo de respuesta del cliente o tiempo de ejecución interno del servidor.

Separa los datos de entrada de los supuestos. Un enlace anuncia una velocidad física; la eficiencia útil depende de los protocolos, del tamaño de petición, de las pérdidas y de los extremos. Si introduces una eficiencia de 0,80, estás planteando una hipótesis didáctica que debe sustituirse por mediciones al dimensionar una instalación real.

Resuelve primero de forma simbólica y comprueba dimensiones. Para transferir datos, tiempo = volumen / tasa. Si el volumen está en bytes y la tasa en bits por segundo, convierte una de las dos magnitudes. Después comprueba si el orden de magnitud tiene sentido y si el resultado cambia mucho con hipótesis razonables.

## 2. Problema 1: GB, GiB y espacio visible

Un dispositivo se vende con una capacidad nominal de 512 GB. ¿Cuántos GiB representan exactamente esos bytes antes de particiones, metadatos y reservas?

```text
512 GB = 512 × 10^9 bytes
1 GiB = 2^30 bytes = 1.073.741.824 bytes
Capacidad en GiB = 512.000.000.000 / 1.073.741.824
                 ≈ 476,837 GiB
```

La diferencia entre 512 y 476,837 no demuestra que haya fallado el dispositivo ni que se haya consumido todo ese espacio. Primero cambia la base de la unidad; después hay que considerar particiones, reservas y sistema de archivos. Si el programa etiqueta como «GB» una magnitud calculada en base dos, la presentación puede añadir confusión.

**Comprobación:** compara tamaños en bytes cuando las herramientas lo permitan. En Linux, `lsblk -b -o NAME,TYPE,SIZE` permite leer capacidad en bytes; en Windows puedes consultar las propiedades `Size` de los objetos de disco. No sumes capacidades de particiones y disco como si fueran almacenamiento independiente.

## 3. Problema 2: tiempo mínimo de transferencia

Se transfieren 12 GiB por un enlace de 100 Mbit/s, con eficiencia útil supuesta del 80 %. Calcula el tiempo y explica sus límites.

```text
Volumen = 12 × 2^30 × 8 = 103.079.215.104 bits
Tasa útil = 100 × 10^6 × 0,80 = 80.000.000 bit/s
Tiempo = 103.079.215.104 / 80.000.000
       = 1.288,4901888 s ≈ 21 min 28,49 s
```

El tiempo es una estimación bajo una tasa útil constante. Un conjunto de muchos archivos pequeños puede tardar más por aperturas, metadatos y latencia. Un archivo almacenado en un disco lento puede no alcanzar la tasa prevista aunque el enlace esté disponible.

**Error habitual:** dividir 12 entre 100 y presentar segundos. Esas cifras describen unidades incompatibles. Otro error es añadir de nuevo un 20 % de tiempo después de haber reducido la tasa al 80 %: para esta hipótesis el efecto ya está incorporado en el denominador.

**Sensibilidad:** si la eficiencia es 60 %, el tiempo pasa a unos 1.717,987 s, aproximadamente 28 min 38 s. Para aceptar una ventana de mantenimiento de 25 minutos, la hipótesis del 80 % podría cumplir y la del 60 % no; hace falta medir y dejar margen.

## 4. Problema 3: localizar el cuello de botella

Un cliente, una red y un servidor presentan estas capacidades útiles bajo una prueba concreta: lectura de origen 150 MB/s, red 110 MB/s y escritura de destino 70 MB/s. Se copian 10.000 MB. ¿Cuál es el límite teórico del flujo secuencial sin compresión?

La tasa máxima de un flujo que necesita atravesar las tres etapas no supera la menor capacidad sostenible: 70 MB/s. El tiempo ideal es `10.000 / 70 ≈ 142,857 s`. Cambiar únicamente el enlace para que admita 250 MB/s no elimina el límite de escritura de 70 MB/s.

Sin embargo, una copia pequeña puede terminar antes o después de lo que sugeriría esa tasa por cachés y confirmaciones diferidas. Si el objetivo exige persistencia, la prueba debe considerar cuándo los datos quedan almacenados de forma duradera. «La barra de progreso terminó» y «los datos sobrevivirán a un fallo» son condiciones distintas.

**Prueba discriminante:** mide lectura, red y escritura con carga controlada, volumen suficiente y un método que describa el tratamiento de caché. No ejecutes pruebas de escritura destructivas contra dispositivos con datos. Las guías de hardware y sistemas desarrollan herramientas y limitaciones para ese entorno.

## 5. Problema 4: IOPS y tamaño de operación

Un dispositivo sostiene hipotéticamente 5.000 operaciones de 4 KiB por segundo en una carga definida. ¿A qué caudal de datos equivale?

```text
5.000 × 4 × 1.024 = 20.480.000 bytes/s
20.480.000 / 10^6 = 20,48 MB/s
20.480.000 / 2^20 = 19,53125 MiB/s
```

Este cálculo no significa que el dispositivo sólo pueda transferir 20,48 MB/s de forma secuencial. Una operación grande mueve más datos por petición y tiene un patrón de acceso distinto. Hay que conservar tamaño de bloque, distribución de lectura/escritura, aleatoriedad, profundidad de cola y latencia para comparar resultados.

Si cada operación de un flujo estrictamente serial tarda 2 ms, el límite de ese flujo es aproximadamente `1 / 0,002 = 500 operaciones/s`, antes de otros costes. Introducir concurrencia puede elevar las operaciones completadas, pero también la latencia y la cola. No deduzcas el rendimiento real de multiplicar indiscriminadamente una latencia por un número comercial de IOPS obtenido en otra prueba.

## 6. Problema 5: media, mediana y percentil

Las ocho duraciones sintéticas de [mediciones-transferencia.csv](datos/mediciones-transferencia.csv), en milisegundos, son:

```text
900, 950, 980, 1.000, 1.020, 1.050, 1.100, 3.000
```

La suma es 10.000 ms y la media 1.250 ms. La mediana es la media de los valores cuarto y quinto ordenados: `(1.000 + 1.020) / 2 = 1.010 ms`. El valor de 3.000 ms desplaza la media sin cambiar mucho el centro de la serie.

Para este cuaderno se define p95 mediante **rango más próximo**: posición `ceil(0,95 × n)`, contando desde uno. Con ocho muestras, `ceil(7,6) = 8`; p95 es 3.000 ms. Otras implementaciones interpolan y pueden devolver otro número. Informa del método y del tamaño de muestra; ocho observaciones no describen con precisión una cola de latencia de producción.

Si cada transferencia mueve 64 MiB, el caudal agregado del conjunto secuencial es `8 × 64 / 10 = 51,2 MiB/s`. La media aritmética de los ocho cocientes individuales no coincide necesariamente con este valor. Para estimar capacidad de un lote secuencial, divide volumen total entre tiempo total; para estudiar variación, conserva las observaciones individuales.

**Comprobación reproducible:** ejecuta [la herramienta](../scripts/analizar_mediciones.py). Debe informar 1.250 ms de media, 1.010 ms de mediana, 3.000 ms de p95 y 51,2 MiB/s de caudal agregado. El programa valida datos; no ejecuta una transferencia real.

## 7. Problema 6: crecimiento compuesto y reserva

Un servicio almacena inicialmente 400 GiB y se estima un crecimiento anual del 25 % durante tres años. ¿Qué capacidad lógica sería necesaria al final, antes de backups y redundancia, si se quiere mantener un 20 % libre del volumen provisionado?

```text
Datos al final = 400 × 1,25^3 = 781,25 GiB
Datos = 0,80 × capacidad provisionada
Capacidad provisionada = 781,25 / 0,80 = 976,5625 GiB
```

Multiplicar 781,25 por 1,20 daría 937,5 GiB, donde lo libre sería un 16,67 % del total, no un 20 %. Hay que identificar si un porcentaje se refiere al consumo o a la capacidad final.

La proyección no considera cambios de negocio, compresión, deduplicación, versiones ni bases de datos temporales. Incluye esas cargas cuando sean relevantes y evalúa varios escenarios. Si el crecimiento real es irregular, utiliza observaciones y eventos previstos además de una tasa anual media.

**Entregable:** tabla por año con datos, reserva, capacidad y supuesto de crecimiento. Una adquisición de discos debe distinguir capacidad bruta, útil del esquema de redundancia, volumen lógico y espacio realmente disponible.

## 8. Problema 7: capacidad de una política de copias

Modelo simplificado: una copia completa de 300 GiB y seis incrementales de 12 GiB cada una. No se comprime, no se deduplica y se conserva una sola cadena. ¿Cuánto ocupa la cadena y cuánto se provisiona para que ocupe como máximo un 80 % del repositorio?

```text
Cadena = 300 + 6 × 12 = 372 GiB
Capacidad con 20 % libre = 372 / 0,80 = 465 GiB
```

Si se conservan cuatro cadenas completas independientes con el mismo tamaño, el modelo suma 1.488 GiB antes del margen. Si el producto comparte bloques entre puntos de restauración, esa multiplicación puede sobrestimar o subestimar el almacenamiento según cambios, retención y recolector. El ejercicio es un modelo declarado, no una predicción de todos los programas de backup.

La restauración desde una cadena puede necesitar la completa y los incrementales correspondientes. Perder una pieza puede impedir recuperar puntos posteriores. Un producto con una cadena distinta o snapshots de bloques exige seguir su procedimiento, no aplicar mecánicamente un esquema de archivos.

**Prueba de aceptación:** restaurar un conjunto representativo en destino separado, comprobar integridad y permisos, y medir tiempo. Comprobar sólo el tamaño del repositorio no verifica recuperabilidad.

## 9. Problema 8: RPO real y una copia fallida

Se hacen copias a las 00:00 y a las 12:00. La copia de las 12:00 falla y el incidente ocurre a las 17:20. La última copia utilizable es la de las 00:00. ¿Cuál es la pérdida temporal máxima respecto a ese punto?

La ventana potencial es 17 horas y 20 minutos. Decir «tenemos un RPO de doce horas» describe quizá un objetivo o frecuencia nominal, pero no el estado observado después de un fallo de copia. Se necesita supervisar que las copias terminen y se puedan usar.

Supón que el objetivo aprobado es perder como máximo cuatro horas de trabajo. La política nominal de dos copias diarias ya resulta insuficiente en el peor momento, incluso sin fallos, si no hay otro mecanismo de recuperación. La solución puede implicar más frecuencia, registros de transacciones u otra arquitectura compatible; depende de aplicación y presupuesto.

Documenta también qué transacciones pueden reconstruirse desde fuentes externas y con qué coste. No reduzcas el RPO medido sólo porque una persona cree recordar los datos perdidos; esa reconstrucción necesita evidencia y procedimiento.

## 10. Problema 9: ventana de restauración

Hay que restaurar 200 GiB a una tasa útil sostenida supuesta de 80 MiB/s. Además se necesitan 15 minutos para preparar infraestructura y 10 minutos para verificar aplicación y permisos.

```text
Tiempo de datos = 200 × 1.024 / 80 = 2.560 s
Preparación + validación = 25 × 60 = 1.500 s
Tiempo total estimado = 4.060 s = 67 min 40 s
```

Si el RTO objetivo es una hora, la estimación no cumple. Acelerar la transferencia a 160 MiB/s reduciría datos a 1.280 s y total a 2.780 s, unos 46 min 20 s, manteniendo las demás hipótesis. También puede reducirse preparación mediante procedimientos ensayados, pero no eliminando sin más las pruebas de integridad.

El cronómetro debe empezar y terminar en eventos definidos. Medir desde que alguien pulsa «restaurar» excluye detección, decisión y preparación; ese intervalo puede ser útil como métrica técnica, pero no representa necesariamente la recuperación completa del servicio.

## 11. Problema 10: presupuesto de indisponibilidad

En un periodo didáctico de 30 días de 24 horas, un SLO de disponibilidad del 99,9 % permite como presupuesto aritmético:

```text
Periodo = 30 × 24 × 60 = 43.200 min
Fracción no disponible = 1 − 0,999 = 0,001
Presupuesto = 43.200 × 0,001 = 43,2 min
```

El resultado depende del denominador. Un servicio que sólo se compromete durante horario de apertura tiene otro periodo. También hay que definir cómo se cuentan degradaciones, mantenimiento, peticiones fallidas y tiempos sin datos. Excluir un evento exige una regla acordada, no una decisión tomada después del incidente.

Si un incidente consume 35 minutos y otro 20, la suma es 55 minutos cuando no se solapan; excede el presupuesto de 43,2. Si se solapan en diez minutos para la misma población y criterio, el tiempo conjunto sería 45 minutos. No sumes sin revisar intervalos y alcance.

## 12. Problema 11: dependencias en serie y redundancia

Modelo simplificado: una aplicación requiere simultáneamente dos componentes independientes, cada uno con disponibilidad 0,999. La disponibilidad conjunta aproximada es `0,999 × 0,999 = 0,998001`, es decir, 99,8001 %. Añadir dependencias indispensables puede reducir la disponibilidad global si no se mejora su diseño.

Para dos componentes redundantes e independientes con disponibilidad 0,99, si basta uno y la conmutación funciona perfectamente, la disponibilidad modelada es `1 − (1 − 0,99)^2 = 0,9999`, 99,99 %. El beneficio desaparece parcialmente ante causas comunes: alimentación compartida, mismo software defectuoso, error de configuración replicado o un único switch.

Estos cálculos no prueban que una arquitectura real tenga esos porcentajes. La independencia y la conmutación perfecta son supuestos fuertes. Documenta modos de fallo y ensaya la recuperación. Un segundo servidor que nadie sabe promover puede aportar capacidad sin aportar la continuidad esperada.

## 13. Problema 12: colas y concurrencia

En un sistema estable, para una población y un límite de observación coherentes, la relación de Little expresa `L = λ × W`: número medio dentro del sistema, tasa media de entrada y tiempo medio de permanencia. Supón 12 solicitudes por segundo y un tiempo medio de 0,25 segundos; el número medio en el sistema sería tres solicitudes.

El valor tres no significa que una configuración de tres trabajadores garantice ausencia de colas. La media oculta ráfagas, variación de servicio y solicitudes que esperan o bloquean. Tampoco permite aplicar sin condiciones la relación a un intervalo con una cola que crece indefinidamente.

**Ejercicio de diseño:** si la tasa se duplica y el tiempo medio se mantiene, la media de solicitudes en el sistema se duplica. Si el tiempo aumenta al saturarse un recurso, la concurrencia observada puede crecer todavía más. Mide tasa, latencia y cola conjuntamente antes de aumentar hilos.

## 14. Problema 13: ahorro de energía y periodo de uso

Doce equipos reducen potencia media de 90 W a 65 W durante seis horas al día, 180 días al año. No se cuenta otra franja de actividad ni consumo fuera de ese periodo.

```text
Reducción por equipo = 25 W = 0,025 kW
Energía evitada = 12 × 0,025 × 6 × 180 = 324 kWh/año
Con precio hipotético 0,20 €/kWh: 324 × 0,20 = 64,80 €/año
Con factor hipotético 0,15 kgCO2eq/kWh: 324 × 0,15 = 48,6 kgCO2eq/año
```

El factor de emisiones no se presenta como el vigente de una comercializadora o territorio. Cambiarlo cambia la estimación. Una comparación de ciclo de vida debe incluir además fabricación, uso, reparación, transporte y fin de vida dentro de límites definidos; este cálculo cubre únicamente la energía de una franja de uso.

Si el cambio de equipos cuesta 2.400 €, dividir sólo por ese ahorro da un periodo de retorno simple de unos 37 años. Eso no determina por sí solo la decisión: pueden existir necesidades de soporte, rendimiento o seguridad, pero no se debe justificar una sustitución como ahorro energético rápido cuando los números del supuesto no lo sostienen.

## 15. Problema 14: coste total y capacidad de mantenimiento

Alternativa A: inversión de 900 €, mantenimiento de 25 €/mes y 18 horas anuales de administración valoradas hipotéticamente a 20 €/h. Alternativa B: cuota de 55 €/mes y ocho horas anuales. Horizonte: tres años, sin impuestos, actualización de precios, financiación ni valor residual.

```text
A = 900 + 25 × 36 + 18 × 20 × 3 = 2.880 €
B = 55 × 36 + 8 × 20 × 3 = 2.460 €
Diferencia bajo estas hipótesis = 420 €
```

El valor del trabajo administrativo no es necesariamente un desembolso adicional si lo realiza personal con coste fijo, pero representa capacidad ocupada. Presenta ambas perspectivas sin sumarlas dos veces. Incluye migración, exportación y salida del proveedor si son relevantes; este ejemplo no es una cotización de mercado.

Para elegir, añade requisitos de recuperación, privacidad, dependencia de Internet, compatibilidad y soporte. Una opción más barata que incumple un requisito obligatorio no se acepta sólo por encabezar la tabla de costes.

## 16. Problema 15: porcentajes y puntos porcentuales

Un piloto pasa de 18 errores en 200 operaciones a nueve errores en otras 200. La tasa inicial es 9 % y la final 4,5 %. La reducción es de **4,5 puntos porcentuales** y del **50 % respecto a la tasa inicial**. Ambas expresiones son correctas si se nombra su base.

Si la carga cambia, comparar recuentos puede engañar: nueve errores en 50 operaciones sería un 18 %, aunque el recuento absoluto bajase. Conserva denominador, tipo de tarea, periodo y población. No atribuyas causalidad a un cambio sólo porque coincide con una mejora temporal; revisa entrenamiento, complejidad y otros factores.

**Entregable:** tabla con recuentos, denominadores, tasas y diferencia; explicación de al menos dos posibles factores de confusión. En una práctica escolar pequeña se presenta un piloto y sus límites, sin convertirlo en evidencia estadística definitiva de una empresa.

## 17. Problema 16: compresión y transferencia

Un conjunto de 8 GiB queda en 5 GiB al comprimirse. La razón respecto al original es `5 / 8 = 0,625`, y la reducción de tamaño es 37,5 %. Si el enlace útil es 40 MiB/s, la transferencia sin compresión tarda `8 × 1.024 / 40 = 204,8 s`; comprimido tarda 128 s.

La diferencia de transferencia es 76,8 s. Si comprimir y descomprimir añade 95 s que no pueden solaparse, el proceso completo tarda más. Si se puede canalizar y el cuello de botella es otro, el modelo cambia. Mide extremo a extremo y considera CPU, memoria y cifrado.

No extrapoles una razón obtenida con texto a vídeo ya comprimido o datos cifrados. Los mecanismos de deduplicación también dependen de patrones de datos, versiones y cifrado. El resultado debe conservar qué conjunto se utilizó y si era sintético.

## 18. Cómo entregar una solución numérica

Escribe datos, fórmula, sustitución con unidades, resultado, redondeo e interpretación. Añade un caso límite y una variación de una hipótesis. Si haces una hoja de cálculo, separa entradas de fórmulas y evita números incrustados sin etiqueta. Comprueba al menos un resultado con un cálculo independiente.

Una respuesta correcta en un supuesto puede ser inaplicable a otra infraestructura. La calidad técnica consiste también en decir qué no incluye el modelo y qué dato falta para usarlo en una decisión real. Consulta [Aplicaciones ofimáticas](../primero/aplicaciones-ofimaticas/README.md), [IPE II](../segundo/itinerario-personal-para-la-empleabilidad-ii/README.md) y [Sostenibilidad](../segundo/sostenibilidad-aplicada-al-sistema-productivo/README.md) para desarrollar los modelos y sus evidencias.

## Referencias para contrastar unidades y métodos

- [NIST: prefixes for binary multiples](https://physics.nist.gov/cuu/Units/binary.html): distinción de unidades decimales y binarias.
- [Python: statistics](https://docs.python.org/3/library/statistics.html): definiciones y comportamiento de funciones estadísticas.
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/): población y definición de objetivos de servicio.
- [Debian Reference](https://www.debian.org/doc/manuals/debian-reference/): observación y administración del sistema.
- [Microsoft Learn: performance tuning](https://learn.microsoft.com/windows-server/administration/performance-tuning/): dimensiones y contexto de análisis de rendimiento.
