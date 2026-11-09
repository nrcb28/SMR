# Viabilidad avanzada: mezcla de servicios, capacidad y tesorería

[Índice del módulo](README.md) · [Casos profesionales](06-casos-profesionales-resueltos.md) · [Modelo inicial](02-casos-practicos.md)

## 1. Del margen unitario al servicio completo

Este capítulo utiliza una empresa ficticia de soporte para analizar decisiones, sin contratar, invertir o presentar declaraciones. Todos los precios, tiempos y costes son hipótesis didácticas. Los importes del modelo de explotación y caja se expresan sin IVA para aislar relaciones; un presupuesto de caja real debe incorporar impuestos y sus fechas según régimen y operaciones.

Un servicio informático combina trabajo, desplazamiento, consumibles, herramientas, licencias, coordinación y riesgo de repetir tareas. Un precio aparentemente alto puede ser insuficiente si exige muchas horas o cobertura que no se puede prestar. La rentabilidad no se evalúa únicamente por porcentaje de margen: importa el recurso escaso, la demanda y la liquidez.

El modelo admite dos líneas homogéneas dentro del supuesto: diagnóstico `D` y mantenimiento `M`. No se comparan con servicios reales de mercado ni se asume que un diagnóstico siempre se resuelva en el mismo tiempo. Se mantienen cantidades para poder estudiar sensibilidad sin cambiar todas las variables simultáneamente.

## 2. Catálogo, unidad y costes trazables

| Variable | Diagnóstico D | Mantenimiento M |
| --- | ---: | ---: |
| Precio por unidad sin IVA | 45 € | 120 € |
| Coste variable por unidad | 9 € | 30 € |
| Contribución por unidad | 36 € | 90 € |
| Tiempo de ejecución por unidad | 0,75 h | 2,5 h |
| Contribución por hora de ejecución | 48 €/h | 36 €/h |

Los variables incluyen partidas directamente asociadas al servicio del caso; el trabajo y recursos fijos se contemplan en el coste del periodo. Si cambias la forma de remuneración del profesional, revisa dónde está imputado para no contarlo dos veces o dejarlo fuera. Coste variable no significa cualquier compra del mes: la clasificación depende de cómo cambia con el volumen y del horizonte.

Los costes fijos mensuales suman 2.400 €, incluidos 80 € de amortización de gestión. El pago corriente de esos fijos es 2.320 €. La amortización supone una inversión previa de 3.840 €, sin valor residual, distribuida linealmente en 48 meses. Es una hipótesis económica, no una tabla fiscal. El desembolso de inversión se sitúa antes del periodo de caja analizado.

Define también alcance: qué entrega un diagnóstico, qué activos cubre un mantenimiento y qué requiere presupuesto adicional. Si «mantenimiento» incluye atención ilimitada sin datos de uso, la unidad pierde significado. Las exclusiones no sirven para abandonar una obligación; aclaran qué se ha modelado y qué debe negociarse y comprobarse.

## 3. Resultado con una mezcla de ventas

La previsión base fija cuarenta diagnósticos y veinte mantenimientos al mes. Los ingresos son `40×45 + 20×120 = 4.200 €`. Los variables son `40×9 + 20×30 = 960 €`. La contribución total es 3.240 €, y el resultado de explotación reducido es `3.240 − 2.400 = 840 €`.

El consumo de ejecución es `40×0,75 + 20×2,5 = 80 h`. Se dispone de cien horas de ejecución facturable después de reservar otras tareas. No se interpreta que esas cien horas sean toda la jornada de trabajo. Quedan veinte para variabilidad dentro del diseño; el plan debe contemplar qué ocurre si se emplean en repetición, atención urgente o desplazamientos no incluidos.

Para modelar equilibrio con mezcla constante definimos un paquete matemático de dos D y un M. No implica que se venda obligatoriamente como paquete comercial. Sus ingresos son 210 €, variables 48 €, contribución 162 € y tiempo cuatro horas.

```text
Equilibrio continuo = 2.400 / 162 = 14,814814... paquetes
Equilibrio entero con mezcla fija = 15 paquetes
Volúmenes = 30 D y 15 M
Tiempo = 15 × 4 = 60 h
Resultado = 15 × 162 − 2.400 = 30 €
```

Con catorce paquetes el resultado es `2.268 − 2.400 = −132 €`. El redondeo se hace sobre el conjunto cuando el supuesto exige mantener la mezcla entera. No redondees independientemente un D y un M procedentes de un promedio sin revisar la combinación final.

## 4. Capacidad y recurso limitante

Con cien horas y cuatro horas por paquete caben veinticinco paquetes: cincuenta D y veinticinco M. La contribución sería 4.050 € y el resultado 1.650 €, si se vendiera y ejecutara esa mezcla sin otros cambios. Que la capacidad lo permita no demuestra demanda. El caso base vende veinte paquetes, no veinticinco.

El diagnóstico aporta más contribución por hora que mantenimiento en este supuesto. Si la única restricción fuera tiempo y hubiera demanda ilimitada, merecería estudiarse esa diferencia. Pero demanda, compromisos recurrentes, horarios, aprendizaje y calidad pueden cambiar la decisión. No se abandona a un cliente con contrato para sustituirlo por una cuenta de margen horario.

Una simulación útil separa capacidad nominal y efectiva. Si se reservan doce de las veinte horas libres para variabilidad y quedan ocho, sólo caben dos paquetes adicionales bajo la misma mezcla. La holgura no es desperdicio por definición: puede sostener tiempos de respuesta y evitar que un incidente provoque retraso de toda la agenda.

## 5. Sensibilidad: cambiar hipótesis con una pregunta

El [CSV de mezcla de servicios](mezcla-servicios.csv) conserva volúmenes para aislar cambios. Cada escenario indica precios y variables, con fijos de 2.400 €. Los tiempos se mantienen: una bajada de precio no convierte automáticamente una tarea en más rápida.

| Escenario | Precio D/M | Variable D/M | Contribución total | Resultado |
| --- | --- | --- | ---: | ---: |
| Base | 45 / 120 € | 9 / 30 € | 3.240 € | 840 € |
| Precio −10 % | 40,50 / 108 € | 9 / 30 € | 2.820 € | 420 € |
| Variable +20 % | 45 / 120 € | 10,80 / 36 € | 3.048 € | 648 € |
| Ambos cambios | 40,50 / 108 € | 10,80 / 36 € | 2.628 € | 228 € |
| Variable supera precio | 45 / 120 € | 48 / 130 € | −320 € | −2.720 € |

En el escenario de precios menores, el resultado baja un 50 %, aunque el precio sólo baja un 10 %. La estructura fija amplifica el efecto en beneficio. No se afirma una elasticidad de demanda; para analizar si venderías más necesitas otra hipótesis y capacidad suficiente.

En el último escenario no existe un punto de equilibrio positivo vendiendo la misma mezcla: cada paquete destruye contribución antes de fijos. Escribir un volumen negativo mediante la fórmula no resuelve el problema. Revisa servicio, coste, precio o viabilidad; vender más empeora el resultado bajo esas hipótesis.

## 6. Resultados contables reducidos y flujos de dinero

Partimos de 2.000 € de caja tras la inversión inicial y sin clientes pendientes. Todos los meses se reconocen 4.200 € de ventas. Se cobra el 60 % en el mismo mes y el 40 % en el siguiente. Los variables de 960 € y fijos que consumen caja de 2.320 € se pagan dentro del mes. No hay impagos, existencias nuevas, financiación ni otros flujos en esta tabla.

| Mes | Caja inicial | Cobro de ventas del mes | Cobro del mes anterior | Pagos de caja | Caja final |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 2.000 € | 2.520 € | 0 € | 3.280 € | 1.240 € |
| 2 | 1.240 € | 2.520 € | 1.680 € | 3.280 € | 2.160 € |
| 3 | 2.160 € | 2.520 € | 1.680 € | 3.280 € | 3.080 € |

El [CSV de tesorería](tesoreria-trimestral.csv) permite repetir los cálculos. El resultado de cada mes es 840 €, pero el cambio de caja del primero es −760 €. La conciliación explica: `840 de resultado + 80 de amortización − 1.680 de aumento de clientes = −760 €`.

Al cerrar tres meses el resultado acumulado es 2.520 €. La caja aumenta 1.080 €: `2.520 + 240 de amortización − 1.680 de clientes pendientes = 1.080`. Los saldos y exclusiones son esenciales para que la igualdad funcione. No extrapoles esta conciliación si hay inversión, préstamos o cambios de stock sin añadirlos.

## 7. Capital circulante y plazo de cobro

En una fotografía adicional del caso, caja es 1.240 €, clientes 1.680 € y existencias 300 €. Se suponen proveedores pendientes de 450 € y deuda a corto de 300 €. El activo corriente suma 3.220 € y el pasivo corriente 750 €; el fondo de maniobra reducido es 2.470 €. No equivale a todo el dinero inmediatamente disponible: incluye clientes y existencias.

La necesidad operativa simplificada, tomando sólo clientes más existencias menos proveedores, es `1.680 + 300 − 450 = 1.530 €`. Distingue esta magnitud del fondo de maniobra anterior. Los conceptos responden a preguntas diferentes: financiación de operaciones frente a una clasificación de recursos y obligaciones corrientes del modelo.

Si el periodo ficticio tiene treinta días y se mantienen ventas de 4.200 €, la venta media diaria es 140 €. Un saldo de clientes de 1.680 € equivale a doce días de esas ventas bajo esa simplificación. No significa que todos los recibos lleven doce días vencidos: hace falta un listado de antigüedad con fechas de factura, vencimiento y cobro.

## 8. Inversión, préstamo, amortización y caja

Una compra de herramienta de 3.840 € consume caja según fecha de pago, mientras el supuesto distribuye su gasto en 80 € mensuales. Si se financia, el préstamo aporta dinero y una obligación. No se registra su entrada como venta. La devolución de principal y el interés se separan porque afectan de modo distinto a resultado y caja.

Ejemplo independiente: se recibe un préstamo ficticio de 2.400 €, con un pago de principal de 200 € e interés de 20 € en un periodo posterior. La entrada inicial aumenta caja 2.400 €; el pago posterior la reduce 220 €. En un modelo de resultado que no incluía financiación, se añade el gasto financiero de 20 €, sin restar otros 200 € como si fueran un segundo gasto por el mismo recurso. Las condiciones reales, comisiones e impuestos quedan fuera del ejemplo.

La decisión de financiación compara coste, calendario, garantías, riesgo y flexibilidad, con información actual y asesoramiento cuando corresponda. Un saldo de caja positivo creado por deuda no demuestra que el servicio sea rentable. Una proyección completa separa explotación, inversión, financiación y los flujos fiscales aplicables.

## 9. IVA: separar base, cuota y dinero reservado

Para explicar mecánica se supone una operación a la que corresponde 21 % de IVA. Una base de 450 € genera cuota de 94,50 € y total de 544,50 €. La cuota cobrada no es margen del servicio. Su tratamiento y el de cuotas soportadas dependen de requisitos, régimen, localización y operación; se consultan en AEAT.

Si el ejercicio incorpora una compra con base de 100 € y cuota deducible de 21 € bajo sus hipótesis, el saldo simplificado entre ambas cuotas sería 73,50 €. Eso no convierte una factura aislada en liquidación completa ni determina el momento en que debe ingresarse. Hay que examinar el conjunto del periodo y las reglas aplicables.

No combines esta mini tabla con la caja trimestral anterior sin rehacer flujos brutos y liquidaciones. El modelo trimestral excluye IVA de forma expresa; añadir únicamente «el IVA a pagar» y mantener cobros netos restaría dinero que nunca registraste como cobrado. La coherencia de alcance precede a cualquier fórmula.

## 10. Calidad, repetición y coste de una promesa

Una intervención repetida sin cobro puede consumir tiempo y variable aunque el volumen facturado no cambie. Si de los veinte M se repiten dos con una hora adicional cada uno y coste de 8 € por repetición, se añaden dos horas y 16 € de variable. El resultado baja a 824 € y la ejecución sube a 82 h. El ejercicio obliga a registrar repetición, no a ocultarla como formación.

Un compromiso de atención rápida exige cobertura. Una sola persona no puede prometer disponibilidad simultánea ilimitada porque su Excel tenga beneficio positivo. Estudia picos, ausencias, desplazamientos, terceros y tiempo de recuperación. Un servicio sostenible tiene capacidad para cumplir su alcance y rechazar o escalar lo que excede sus medios.

No reduzcáis pruebas, copia o documentación para fabricar margen. Si esas tareas forman parte de la entrega necesaria, sus tiempos deben aparecer. Mejorar un procedimiento puede reducir errores y tiempo, pero se mide con una muestra comparable y criterios de calidad constantes.

## 11. Forma jurídica y puesta en marcha: expediente de preguntas

La elección de forma jurídica compara responsabilidad, participantes, gobierno, financiación, obligaciones y continuidad. No se resuelve con un único umbral de facturación ni copiando capitales mínimos de una guía antigua. Los requisitos pueden cambiar; utiliza las fichas vigentes de Plataforma PYME y contrasta trámites en sedes competentes.

Para el ejercicio elabora una tabla de dos alternativas, con pregunta, fuente, fecha y respuesta pendiente. Incluye separación entre constitución y puesta en marcha, encuadre fiscal/social, protección de datos, licencias cuando procedan y autorizaciones para tratar sistemas de clientes. No se realiza ningún alta ni declaración: el producto es un análisis documental.

## 12. Práctica completa y rúbrica

Reproduce mezcla, sensibilidad y tesorería con celdas de entrada separadas. Comprueba sumas, unidades y periodos. Añade un escenario con porcentaje de cobro inicial menor y calcula la necesidad de caja sin alterar beneficio por esa sola razón. Diseña una respuesta que no sea únicamente «pedir un préstamo»: revisar condiciones de cobro, capital inicial, alcance o calendario puede modificar el problema.

Entrega archivo editable, CSV importados, informe breve de decisiones y lista de supuestos pendientes de validación. Otra persona debe poder cambiar precio o cobro y reconstruir la conclusión. Rúbrica propia: estructura económica 25 %, capacidad/demanda 20 %, tesorería/conciliación 25 %, sensibilidad y decisiones 20 %, fuentes y claridad 10 %.

## Fuentes primarias

- [Plataforma PYME: formas jurídicas](https://plataformapyme.es/es-es/AppWeb/Paginas/FormasJuridicas-Descripcion.aspx).
- [DGEIPYME: plan de empresa](https://planempresa.ipyme.org/).
- [AEAT: información de IVA](https://sede.agenciatributaria.gob.es/Sede/iva.html).
- [AEAT: deducción de IVA soportado](https://sede.agenciatributaria.gob.es/Sede/iva/que-iva-soportado-puedo-deducir.html).

Las fórmulas y cifras son una elaboración de gestión para aprendizaje, sin atribuirles valor de contabilidad legal completa o asesoramiento fiscal.
