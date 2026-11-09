# 0223 · Aplicaciones ofimáticas

Curso: **primero de SMR en la Comunidad de Madrid**. Este módulo enseña a producir, intercambiar y mantener documentos de trabajo fiables: informes, hojas de cálculo, bases de datos de escritorio, presentaciones y material multimedia. Una entrega profesional debe conservar el significado de los datos, poder revisarse y resultar utilizable por otras personas.

Esta guía utiliza **LibreOffice** como entorno reproducible y explica equivalencias con Microsoft 365 cuando ayudan a entender la interoperabilidad. Comprueba la versión en `Ayuda → Acerca de LibreOffice`: nombres de menús, funciones recientes y opciones de exportación cambian entre versiones. Los ejemplos usan interfaz española, fórmulas con `;` como separador de argumentos y coma decimal. Si tu instalación usa nombres ingleses, consulta el asistente de funciones.

## Documentación

1. [Fundamentos: documentos, datos, formatos y accesibilidad](01-fundamentos.md).
2. [Guía técnica: Writer, Calc, Base, Impress y multimedia](02-guia-tecnica.md).
3. [Cuatro prácticas completas con entregables](03-practicas.md).
4. [Diagnóstico, evaluación y preguntas resueltas](04-diagnostico-y-evaluacion.md).
5. [Writer avanzado: documentos largos, revisión y publicación](05-documentos-largos-y-publicacion.md).
6. [Calc avanzado: modelos trazables y calidad de datos](06-modelos-calc-y-calidad-de-datos.md).
7. [Base avanzado: modelo relacional, consultas e integridad](07-base-modelado-consultas-y-transacciones.md).
8. [Taller integrado, multimedia y quince problemas resueltos](08-taller-integrado-y-ejercicios-resueltos.md).

## Archivos de ejemplo

- [Inventario sintético](ejemplos/inventario.csv) y [destinatarios ficticios](ejemplos/destinatarios.csv).
- [Esquema SQL del taller](ejemplos/taller.sql), [consultas iniciales](ejemplos/consultas.sql) y [consultas avanzadas de lectura](ejemplos/consultas-avanzadas.sql).
- [Modelo de costes con ocho partidas](ejemplos/modelo-costes.csv), utilizado en la ampliación de Calc y en el taller integrado.

## Objetivos y evidencias

| Capacidad que se trabaja | Evidencia observable |
| --- | --- |
| Instalar y mantener una suite | Versión, origen del instalador, configuración regional y prueba de apertura/exportación |
| Estructurar un documento | Estilos jerárquicos, índice automático, referencias y PDF accesible revisado |
| Modelar cálculos | Fórmulas trazables, validación, referencias correctas y resultados contrastados |
| Organizar datos relacionados | Claves, integridad referencial, consultas y formularios coherentes |
| Comunicar resultados | Presentación legible, material multimedia optimizado y fuentes identificadas |
| Dar soporte a usuarios | Incidencia reproducible, diagnóstico, solución y comprobación final |

La tabla es una organización didáctica de este repositorio, no la reproducción de los resultados de aprendizaje ni de los criterios oficiales de evaluación.

## Prerrequisitos y ruta de estudio

Necesitas manejar carpetas y extensiones, distinguir un archivo original de una copia, conocer permisos de lectura/escritura y disponer de una carpeta de trabajo con copia de seguridad. Para Base se utiliza una base **Firebird incrustada nueva**, destinada únicamente a ejercicios; el SQL de los ejemplos no se debe importar sobre datos reales.

Sigue primero los fundamentos y crea el informe de Writer. Continúa con el inventario de Calc, después con el taller relacional y termina con una presentación que explique tus resultados. Reserva una sesión final a abrir los archivos en otro perfil o equipo: la compatibilidad se comprueba, no se presume. Un PDF visualmente correcto puede haber perdido el orden de lectura y una hoja sin errores visibles puede contener importes almacenados como texto.

Para profundizar, utiliza el capítulo 5 para convertir el informe en una plantilla revisable; el 6 para separar entradas, fórmulas, controles y escenarios; y el 7 para razonar sobre integridad, consultas y límites de las transacciones. El capítulo 8 reúne los productos y añade tres prácticas integradas y quince problemas con solución. Conserva los resultados iniciales para comparar qué mejora aporta cada ampliación.

Consulta el [laboratorio común](../../docs/laboratorio.md) para preparar las máquinas y vuelve al [índice general](../../README.md) para relacionar este módulo con sistemas y aplicaciones web.

## Fuentes primarias

- [Guías oficiales de LibreOffice](https://books.libreoffice.org/).
- [Ayuda de LibreOffice en español](https://help.libreoffice.org/latest/es/).
- [Soporte oficial de Microsoft 365](https://support.microsoft.com/es-es/microsoft-365).
- [Introducción a la accesibilidad de W3C](https://www.w3.org/WAI/fundamentals/accessibility-intro/es).
