# Módulo profesional optativo · segundo

## Catálogo oficial aplicable a SMR

Ya puedes consultar el [catálogo completo de optativas aplicables a SMR en Madrid](../../optativas/README.md), con las16 variantes, RA, criterios, condiciones y actividades. La oferta real y matrícula se concretan en el centro. Los talleres propios que siguen debajo son material complementario y no se atribuyen a una optativa oficial.

La organización madrileña de SMR incluye en segundo una optativa de 90 horas de currículo y tres horas semanales de referencia. Su nombre concreto y programación deben obtenerse del centro: esta carpeta no atribuye una materia a una oferta que no se ha identificado. El catálogo de referencia es la [Orden 3536/2025](https://www.bocm.es/boletin/CM_Orden_BOCM/2025/08/27/BOCM-20250827-5.PDF), modificada por la [Orden 3822/2026](https://www.bocm.es/boletin/CM_Orden_BOCM/2026/09/25/BOCM-20260925-20.PDF).

## Propuesta propia: operación y soporte documentados

### Itinerario ampliado

1. [Operación y automatización controlada: planes, validación y fallo parcial](01-operacion-y-automatizacion-controlada.md).
2. [Casos, métricas y evaluación del soporte](02-casos-metricas-y-evaluacion.md).

Tras la introducción, profundiza en automatizaciones de lectura y planes sin ejecución. Los casos trabajan una alerta útil, conflictos de altas, media y mediana de respuesta y comunicación de una mitigación cuya causa aún no se conoce. Son actividades complementarias, sin atribución de currículo oficial.

Este material es una ampliación opcional para practicar capacidades de SMR; no es una denominación oficial, una convalidación ni un sustituto de la optativa del centro. El objetivo es pasar de “resolver algo en mi equipo” a prestar un soporte que otra persona pueda revisar y continuar.

### Ciclo de una incidencia

1. **Recepción:** identifica servicio, alcance, impacto, hora y persona responsable de la validación sin recoger datos innecesarios.
2. **Clasificación:** distingue incidencia, solicitud y cambio. Prioriza por impacto y urgencia con una escala definida por el ejercicio.
3. **Diagnóstico:** formula hipótesis y selecciona pruebas que las distingan. Conserva resultados antes de modificar.
4. **Intervención:** describe el cambio, la autorización operativa que exige el entorno y la forma de volver atrás.
5. **Validación:** prueba desde el contexto de la persona afectada, con sus permisos, y verifica efectos secundarios.
6. **Cierre:** registra causa confirmada o límites de la investigación, solución, evidencias y trabajo pendiente.

Una solicitud para instalar una aplicación no implica que exista una avería. Un cambio puede necesitar ventana, copia y pruebas diferentes. Una mitigación que permite trabajar no confirma la causa raíz: documenta ambos estados por separado.

### Recogida inicial de información

En una VM Debian con systemd, las siguientes consultas son de observación:

```bash
cat /etc/os-release
systemctl --failed
df -h
```

Indican versión declarada del sistema, unidades con fallo y ocupación de sistemas de archivos. Ninguna demuestra por sí sola integridad de disco o disponibilidad completa de una aplicación. No ejecutes limpieza automática porque un porcentaje te parezca alto sin identificar qué ocupa espacio y cuál es la política de conservación.

En Windows, una consulta de información del sistema es:

```powershell
Get-CimInstance Win32_OperatingSystem |
    Select-Object Caption, Version, BuildNumber
```

La salida debe revisarse antes de compartirla. Otros comandos y registros pueden incluir nombres, rutas personales, direcciones o información sensible. Conserva sólo lo necesario y utiliza datos de prácticas. No conviertas la recopilación inicial en un escaneo de redes ajenas ni en una exportación completa de registros de empresa.

### Práctica: incidente con espacio de trabajo

Prepara en una VM una carpeta de datos sintéticos. Una segunda persona redacta un ticket indicando que no puede guardar un documento, sin proporcionar la causa. Investiga permisos, ruta, espacio disponible y estado de la aplicación sin borrar contenido real. Si se simula una falta de espacio, utiliza una imagen o volumen de pruebas controlado y no llenes el sistema del host.

La resolución debe incluir una prueba permitida y una denegada cuando haya permisos, registro del cambio y validación de guardado desde la cuenta adecuada. Si no puedes distinguir entre dos causas, explica qué prueba falta; no elijas una al azar para cerrar el ticket.

**Entregables:** ticket inicial, árbol de hipótesis, resultados, plan de cambio, validación, reversión y artículo breve de conocimiento. La evaluación propuesta asigna igual importancia a diagnóstico, intervención, pruebas y documentación; la calificación oficial corresponde a la programación del centro.

### Métricas que ayudan a decidir

Tiempo de primera respuesta y tiempo de resolución son diferentes. Define inicio, fin, pausas y horario antes de comparar. La media puede ocultar casos extremos; presenta también mediana y número de tickets. No premies cerrar pronto sin validar: puede aumentar reaperturas y degradar el servicio.

Un artículo de conocimiento útil indica síntoma, entorno, causa confirmada, comprobación, solución y límites. No contiene cuentas reales ni contraseñas. Pide a otra persona que lo siga en una VM nueva: las dudas que surjan revelan información implícita que debe documentarse.

## Fuentes y enlaces

- [INCIBE: empresas](https://www.incibe.es/empresas).
- [Debian Reference](https://www.debian.org/doc/manuals/debian-reference/).
- [Microsoft Learn: PowerShell](https://learn.microsoft.com/en-us/powershell/).
- [Laboratorio común](../../docs/laboratorio.md).

[Índice de segundo](../README.md) · [Índice general](../../README.md)
