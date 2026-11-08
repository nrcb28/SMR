# Sistemas operativos en red · 0224

Administrar un sistema en red exige coordinar identidad, nombres, hora, almacenamiento, permisos y continuidad. Este módulo pasa de un servidor independiente a un pequeño dominio de laboratorio y enseña a demostrar quién puede hacer qué, desde qué equipo y con qué evidencias.

**Curso:** segundo de SMR en la organización de Madrid. Las secuencias y rúbricas de estas guías son una propuesta de estudio, no criterios oficiales de calificación del centro.

## Itinerario y documentación

| Lectura | Contenido y resultado verificable |
| --- | --- |
| [01 · Fundamentos](01-fundamentos.md) | Modelos de administración, directorios, autenticación, permisos y diseño del laboratorio. |
| [02 · Guía técnica](02-guia-tecnica.md) | Linux, ACL, Samba independiente, Windows Server 2025, AD DS, DNS, OU, grupos, GPO y copias. |
| [03 · Prácticas](03-practicas.md) | Tres montajes completos con entregables, pruebas de acceso permitido y denegado y recuperación. |
| [04 · Diagnóstico y evaluación](04-diagnostico-y-evaluacion.md) | Árbol de diagnóstico, incidencias reproducibles, rúbrica orientativa y preguntas resueltas. |

Lee primero los [requisitos del laboratorio común](../../docs/laboratorio.md). Conviene dominar instalación de sistemas, IPv4, resolución DNS, servicios y permisos de primero. No hace falta un servidor físico: pueden utilizarse máquinas virtuales, siempre que el equipo anfitrión tenga memoria y almacenamiento suficientes.

## Qué debes ser capaz de entregar

- Inventario de servidores, interfaces, direcciones, roles y dependencias.
- Servidor Debian con cuentas sin acceso interactivo cuando sólo necesitan SMB, almacenamiento compartido y ACL documentadas.
- Dominio de laboratorio Windows con DNS funcional, cliente compatible unido, OU y grupos separados por función.
- Matriz de permisos que incluya al menos un caso permitido y otro denegado por cada recurso sensible.
- Directiva de equipo aplicada y demostrada con resultados de directiva, no sólo con una captura del editor.
- Copia restaurada en un destino alternativo y registro de los tiempos observados.

## Entornos y límites

`srv01`, Debian 13, utiliza `192.168.56.10/24` en la interfaz LAB. `dc01`, Windows Server 2025 con licencia o evaluación válida, utiliza `192.168.56.11/24`; `cli01`, Windows 11 Pro compatible, `192.168.56.20/24`. La edición Home no sirve para unir el cliente a un dominio AD tradicional. El dominio es `ad.aula.test` y el nombre NetBIOS propuesto es `AULA`. Los nombres son ficticios y `.test` está reservado para pruebas.

La red LAB es interna o de tipo host-only. No se publica SMB, LDAP, Kerberos ni RDP en Internet. La interfaz LAB no recibe puerta de enlace por defecto. El acceso de actualización mediante otra interfaz NAT se controla por separado; en el controlador de dominio se recomienda retirarla antes de promoverlo para evitar registros DNS y rutas ambiguos. `dc01` no debe ejecutar a la vez el BIND de la asignatura Servicios en red. Un Samba AD DC alternativo debe vivir en otra VM o sustituir el escenario Windows; no se instala encima del Samba independiente de estas prácticas.

Los bloques de código se ejecutan en las VM indicadas y con privilegios sólo cuando se señala. Ningún resultado se da por comprobado en tu equipo: cada práctica establece qué debes observar y cómo registrar el resultado real.

## Secuencia sugerida

1. Explica la diferencia entre identidad local y de dominio y dibuja las dependencias DNS–hora–Kerberos.
2. Construye un recurso Linux y comprueba permisos desde el sistema local antes de añadir Samba.
3. Instala el dominio, valida DNS y une un único cliente.
4. Organiza cuentas con grupos y OU; aplica una GPO limitada a una OU de prueba.
5. Simula una incidencia reversible, restablece el servicio y prepara el informe técnico.

[Volver al repositorio](../../README.md)
