# Seguridad informática · 0226

La seguridad se demuestra relacionando necesidades, riesgos, controles y pruebas. Este módulo explica cómo reducir superficie expuesta, proteger identidades y datos, recuperar un servicio y responder a un incidente con evidencias suficientes para decidir.

**Curso:** segundo de SMR en Madrid. El itinerario, las prácticas y las ponderaciones siguientes son propuestas didácticas del repositorio; la programación del centro establece la evaluación oficial.

## Documentación del módulo

| Guía | Qué aprenderás a justificar y comprobar |
| --- | --- |
| [01 · Fundamentos](01-fundamentos.md) | Activos, amenazas, riesgo, criptografía, identidades y continuidad. |
| [02 · Guía técnica](02-guia-tecnica.md) | Inventario, actualización, SSH, nftables, TLS, registros, copias y respuesta. |
| [03 · Prácticas](03-practicas.md) | Cuatro ejercicios de endurecimiento, filtrado, recuperación y gestión de incidentes. |
| [04 · Diagnóstico y evaluación](04-diagnostico-y-evaluacion.md) | Casos razonados, pruebas, rúbrica y lista de cierre. |

## Prerrequisitos y entorno

Debes manejar usuarios, permisos, servicios, direcciones IP, DNS y comandos básicos de Linux y Windows. Utiliza el [laboratorio común](../../docs/laboratorio.md) con Debian 13 en `srv01` (`192.168.56.10/24`) y un cliente autorizado, normalmente `cli01` (`192.168.56.20/24`). Confirma el nombre real de la interfaz LAB, que en los ejemplos es `ens19`; la interfaz NAT es una conexión distinta y no convierte LAB en una red con router.

La práctica de firewall usa una VM dedicada o una instantánea preparada exclusivamente para ese ejercicio. Su matriz permite SSH y HTTPS; no sirve sin adaptar para el servidor DNS, DHCP, Samba o AD de otras asignaturas. Trabaja desde la consola del hipervisor y conserva un mecanismo de recuperación probado antes de modificar el acceso remoto.

## Productos de aprendizaje

- Inventario de activos y una matriz de riesgos cuyos supuestos puedas defender.
- Registro de un cambio con estado previo, objetivo, validación y reversión.
- Autenticación SSH con clave y pruebas de acceso permitido y denegado.
- Política de firewall que coincida con los servicios necesarios y no elimine ICMPv6 esencial.
- Explicación verificable de la diferencia entre hash, cifrado, firma y certificado.
- Copia independiente restaurada, con RPO y RTO medidos o declarados como objetivos pendientes.
- Cronología de un incidente simulado y decisiones sobre contención, comunicación y recuperación.

## Forma de estudiar

Empieza por un servicio pequeño y documenta una línea base. Aplica un único cambio, valida el resultado y comprueba también qué acceso deja de funcionar. No aumentes privilegios o desactives controles como solución permanente a una incidencia. La explicación del fallo es parte del resultado técnico.

Los ejemplos utilizan archivos ficticios y cuentas propias del laboratorio. Las pruebas se limitan a esos equipos. No necesitas malware, ataques a terceros ni datos personales reales para aprender estas competencias. Ningún bloque se presenta como ejecutado en tu instalación: deberás conservar las observaciones que obtengas.

[Volver al repositorio](../../README.md)
