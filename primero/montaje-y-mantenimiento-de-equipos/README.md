# Montaje y mantenimiento de equipos · 0221

Guía técnica de primer curso de SMR para la Comunidad de Madrid. El objetivo es aprender a justificar una configuración, montar un equipo y localizar averías con un procedimiento reproducible. Saber identificar una pieza es insuficiente: hay que explicar su función, comprobar compatibilidades y demostrar que la intervención ha resuelto el problema.

Esta documentación desarrolla contenidos de estudio y prácticas propias; las propuestas de evaluación no sustituyen los criterios del centro. Consulta el reparto oficial y el alcance general en el [inicio del repositorio](../../README.md).

## Itinerario de lectura

| Documento | Qué aprenderás | Evidencia que producirás |
| --- | --- | --- |
| [01 · Fundamentos](01-fundamentos.md) | CPU, memoria, buses, almacenamiento, energía, firmware y periféricos | Mapa de componentes y matriz de compatibilidad |
| [02 · Guía técnica](02-guia-tecnica.md) | Inventario, selección, montaje, primer arranque y mantenimiento | Orden de trabajo, inventario y acta de pruebas |
| [03 · Prácticas](03-practicas.md) | Tres intervenciones completas y graduadas | Presupuesto, montaje verificado e informe de avería |
| [04 · Diagnóstico y evaluación](04-diagnostico-y-evaluacion.md) | Árboles de decisión, métricas, preguntas y soluciones | Diagnóstico razonado y plan preventivo |
| [05 · Medición y rendimiento](05-medicion-y-rendimiento.md) | Latencia, IOPS, caudal, CPU, memoria, enlaces PCIe, potencia y temperatura | Comparación controlada y dimensionamiento justificado |
| [06 · Diagnóstico por subsistemas](06-diagnostico-por-subsistemas.md) | POST, ausencia de imagen, reinicios, memoria y detección de discos | Hipótesis separadas mediante pruebas y casos de taller |
| [07 · Almacenamiento e integridad](07-almacenamiento-integridad-y-vida-util.md) | HDD, SSD, resistencia, telemetría NVMe, hashes y preservación | Informe de estado y decisión de recuperación o sustitución |
| [08 · Periféricos y mantenimiento](08-perifericos-mantenimiento-y-casos.md) | USB, docks, pantallas, impresión, repuestos y planificación | Tres nuevas prácticas y plan documentado de mantenimiento |
| [09 · Alineación por RA](09-alineacion-ra.md) | Los 8 resultados y 60 criterios oficiales, con fuentes y correspondencias | Dossier con criterio, artefacto y comprobación |
| [10 · Retos por RA](10-retos-por-ra.md) | Selección, montaje, medición, mantenimiento, imágenes, tendencias, periféricos y prevención | Actuaciones y resultados reales separados de expectativas |

Los capítulos 05–08 amplían el itinerario con análisis de medidas, decisiones de taller y casos completos. Léelos después de dominar la instalación básica: su objetivo es explicar por qué una prueba aporta información y qué límites tiene, además de indicar el procedimiento. Incluyen ejercicios de cálculo, interpretación de telemetría y prácticas de USB, impresión y planificación de una flota.

## Antes de empezar

Necesitas manejar unidades de capacidad, tensión, corriente y potencia; distinguir software y hardware; y comprender qué es una copia de seguridad. Prepara el [laboratorio común](../../docs/laboratorio.md). Los ejercicios de inspección por software usan Debian 13 o Windows 11 Pro. Un hipervisor expone dispositivos virtuales: una VM sirve para aprender inventario y arranque, pero no permite validar el cableado, temperaturas o salud del disco físico del anfitrión.

Para desmontar equipos reales utiliza un puesto autorizado, herramientas adecuadas, manual del fabricante y medidas ESD. Una fuente de alimentación no se abre: puede mantener tensiones peligrosas aun desconectada. No se trabaja sobre equipos energizados, baterías hinchadas ni componentes quemados.

## Resultados de aprendizaje trabajados

| Capacidad orientativa | Demostración práctica |
| --- | --- |
| Seleccionar componentes compatibles | Relacionar CPU, placa, firmware, RAM, fuente, caja y almacenamiento con una necesidad concreta |
| Ensamblar y ampliar equipos | Montar, documentar conexiones y verificar funcionamiento sin piezas o tornillos sobrantes |
| Medir y diagnosticar | Elegir una prueba que distinga entre dos hipótesis y registrar resultados |
| Mantener y documentar | Crear una línea base, un plan preventivo y un informe de intervención |
| Gestionar periféricos y consumibles | Configurar una impresora, identificar fallos y tratar residuos por el canal correspondiente |

La tabla organiza el estudio; no asigna numeraciones oficiales a resultados curriculares.

La numeración normativa se desarrolla en el [mapa de alineación](09-alineacion-ra.md), con los ocho RA del módulo y las letras de sus 60 CE. Sigue después los [retos](10-retos-por-ra.md) y utiliza los [datos JSON](alineacion-ra.json) para localizar qué evidencia responde a cada criterio. Las mediciones eléctricas, el montaje físico o una actuación grupal requieren medios y supervisión adecuados; su diseño en una VM o una memoria no acredita por sí solo esas actuaciones.

## Método de trabajo

Lee fundamentos antes de ejecutar procedimientos. En cada práctica escribe la hipótesis antes de cambiar una pieza. Conserva datos de partida, fotografías sin información personal y resultados de las pruebas. Un equipo que arranca una vez todavía no está validado: hay que comprobar estabilidad, almacenamiento, conectividad, periféricos y reinicio. Toda intervención termina con inventario actualizado y una explicación comprensible para la persona usuaria.

## Fuentes principales

- [Guía de instalación de Debian 13](https://www.debian.org/releases/trixie/installmanual).
- [Microsoft Learn: Windows, UEFI y particionado GPT](https://learn.microsoft.com/windows-hardware/manufacture/desktop/windows-setup-installing-using-the-mbr-or-gpt-partition-style).
- [UEFI Forum: especificaciones](https://uefi.org/specifications).
- [Documentación de smartctl en Debian](https://manpages.debian.org/trixie/smartmontools/smartctl.8.en.html).
- [Documentación de administración del kernel Linux](https://docs.kernel.org/admin-guide/index.html).
