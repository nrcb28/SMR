# Casos de IPE II

## Práctica 1. Candidatura a soporte de primer nivel

**Oferta ficticia:** soporte a puestos Windows, conceptos de redes TCP/IP, inventario, atención a usuarios y documentación. Se valora Linux. El trabajo exige seguir procedimientos y escalar cambios de servidor.

### Secuencia

1. Extrae cinco requisitos y clasifica cuáles son imprescindibles o valorables según el texto.
2. Relaciona cada uno con una práctica propia verificable.
3. Redacta un CV orientado a ese puesto, sin nombre, teléfono ni otros datos reales para la entrega pública.
4. Elige dos evidencias para el portfolio y revisa que no contengan datos de terceros.
5. Simula una entrevista de diez minutos y revisa después qué respuestas tuvieron evidencia y cuáles fueron vagas.

### Solución orientativa de correspondencia

| Requisito | Evidencia adecuada | Límite que debe declararse |
| --- | --- | --- |
| TCP/IP | Diagnóstico documentado de dirección, máscara y DNS | Red virtual de formación |
| Inventario | Tabla de activos sintéticos con historial | No incluye inventario real de clientes |
| Atención | Ticket simulado con preguntas y aceptación | Simulación entre compañeros |
| Windows | Alta de usuarios y permisos en VM | Sin experiencia de administración de producción si no existe |
| Linux | Práctica de permisos y servicio | Nivel y versión practicados |

**Criterio de aceptación:** cada afirmación importante tiene evidencia o se presenta como aprendizaje en curso. El CV exportado conserva texto seleccionable y orden lógico. Un documento visualmente atractivo con enlaces rotos no supera la revisión.

## Práctica 2. Diseñar y valorar un servicio mensual

Un servicio ficticio resuelve intervenciones homogéneas de soporte. Cada intervención se vende por 60 € sin IVA, genera un coste variable de 18 € y consume 1,5 horas de ejecución. Se prevén costes fijos mensuales de 2.100 €, que incluyen 50 € de amortización didáctica. Ese coste fijo incorpora la hipótesis de recursos y remuneración del proyecto; no equivale a una estructura de nómina legal. La capacidad máxima de ejecución facturable se fija en 105 horas mensuales.

### Cálculo base

```text
Contribución por intervención = 60 − 18 = 42 €
Equilibrio = 2.100 / 42 = 50 intervenciones
Capacidad = 105 / 1,5 = 70 intervenciones
Ventas con 70 = 70 × 60 = 4.200 €
Variables con 70 = 70 × 18 = 1.260 €
Resultado con 70 = 4.200 − 1.260 − 2.100 = 840 €
```

Hay 20 intervenciones de diferencia entre equilibrio y capacidad. Esa holgura no garantiza demanda ni cubre cualquier incidente. Si los 105 h ya fueran todo el tiempo laboral disponible, faltaría justificar administración y ventas; por eso aquí se definen expresamente como horas de ejecución facturable después de reservar otras tareas.

### Sensibilidad

| Escenario | Precio | Variable | Fijo | Equilibrio entero | Resultado con 70 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Base | 60 € | 18 € | 2.100 € | 50 | 840 € |
| Menor precio | 54 € | 18 € | 2.100 € | 59 | 420 € |
| Más coste variable | 60 € | 24 € | 2.100 € | 59 | 420 € |
| Ambos cambios | 54 € | 24 € | 2.100 € | 70 | 0 € |
| Mayor fijo con ambos cambios | 54 € | 24 € | 2.250 € | 75 | −150 € |

En el último caso se necesitan 75 intervenciones, por encima de la capacidad de 70. La conclusión debe proponer cambios y comprobarlos, no limitarse a poner un número rojo. Subir precio solo será viable si el cliente percibe valor y existe demanda. Reducir tiempo requiere medir calidad y repetición de incidencias.

### Tareas y entregables

Reproduce el modelo en una hoja de cálculo con entradas separadas de resultados. Importa el [CSV del caso](modelo-economico.csv), configurado con `;` y coma decimal. Añade validación para no permitir precio menor o igual que variable cuando se calcule equilibrio. Entrega hoja editable, resumen de alcance y recomendación de una página. Identifica al menos tres supuestos que requieren validación comercial u operativa.

## Práctica 3. Beneficio, caja e IVA

Este caso continúa el escenario base de 70 intervenciones. Se reconocen 4.200 € de ventas, pero durante el mes solo se cobran 3.000 €; quedan 1.200 € pendientes. Los pagos de variables son 1.260 € y los fijos que consumen caja son 2.050 €, ya que los otros 50 € son amortización. Se parte de 1.000 € de caja. Para aislar conceptos, este primer cálculo se realiza **antes de flujos de IVA, financiación e impuestos sobre resultado**.

```text
Beneficio del modelo = 4.200 − 1.260 − 2.100 = 840 €
Caja final del modelo = 1.000 + 3.000 − 1.260 − 2.050 = 690 €
Clientes pendientes = 4.200 − 3.000 = 1.200 €
```

La caja disminuye 310 € pese al beneficio de 840 €. La diferencia se explica por la amortización no pagada del mes y el cobro pendiente: `840 + 50 − 1.200 = −310`. Esta conciliación funciona porque el supuesto excluye otros movimientos y saldos. No es un estado completo de flujos de efectivo.

### Mini caso de IVA separado

Para una factura ficticia se fija una base de 200 € y un tipo del 21 % **asumido aplicable a esa operación del supuesto**. Cuota: 42 €. Total: 242 €. Si en el mismo ejercicio académico hay 15 € de IVA soportado y se cumplen todas las condiciones para deducirlo, el saldo simplificado sería 27 € a ingresar. No basta haber pagado una compra para afirmar que su IVA es deducible.

No añadas 42 € como ingreso del servicio ni restes 15 € del resultado empresarial sin analizar el tratamiento. El modelo de caja completo debe registrar cobros y pagos con IVA y después la liquidación correspondiente. Una factura no cobrada puede generar obligaciones conforme al régimen aplicable; el caso no determina su momento legal.

**Entrega:** conciliación de resultado y caja, factura ficticia y lista de exclusiones. **Aceptación:** explica por qué 242 € cobrados no equivalen a 242 € de ingreso neto del servicio y por qué el beneficio no es saldo bancario.

## Práctica 4. Mejorar un proceso en equipo

Un grupo registra incidencias sin criterio común. En una muestra ficticia de veinte tickets, ocho vuelven a abrirse porque faltaba verificar con el usuario. El equipo propone una plantilla con impacto, pruebas, acción, verificación y aceptación.

Asigna responsables de diseño, revisión técnica y medición; una persona puede ocupar más de un rol si se declara. Define el criterio antes de la nueva muestra: reapertura por la misma causa y dentro del periodo fijado. Simula otros veinte tickets; si se reabren tres, la tasa pasa de 40 % a 15 %, una diferencia de 25 puntos porcentuales y una reducción relativa del 62,5 %.

Es una comparación didáctica, no una prueba causal concluyente: cambian dificultad, usuarios y tamaño de muestra. La mejora de documentación puede coincidir con otros factores. Explica estas limitaciones y decide si conviene una prueba más larga.

**Entregables:** plantilla, acuerdo de responsabilidades, tabla antes/después y retrospectiva. **Aceptación:** se diferencian porcentajes y puntos porcentuales, se usa la misma definición de reapertura y no se ocultan tickets desfavorables.

## Práctica 5. Validación breve de una propuesta

Prepara una ficha de mantenimiento para una oficina ficticia de diez puestos. Indica alcance, horario, tiempos de respuesta, exclusiones, privacidad y precio de referencia. Simula entrevistas con tres roles: quien paga, quien usa los equipos y quien autoriza cambios. Cada rol puede tener una prioridad distinta.

La propuesta debe cambiar a partir de al menos un hallazgo. Si el usuario desea atención inmediata durante todo el día y solo hay una persona disponible, revisa recursos y promesa. Si las incidencias dependen de una aplicación de terceros, define el escalado en lugar de garantizar una solución que no controlas.

Entrega hipótesis inicial, guion, respuestas claramente rotuladas como simuladas, cambio introducido y cuestiones aún no verificadas. Una maqueta aceptada en clase no acredita un mercado real ni autoriza a firmar contratos.
