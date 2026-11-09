# Redes locales · 0225 · Primero

Esta asignatura explica cómo viajan los datos desde una aplicación hasta otro equipo y cómo convertir esa explicación en una instalación que se pueda medir, documentar y mantener. El objetivo práctico es montar una LAN pequeña, calcular su direccionamiento, separar sus segmentos y localizar una avería con evidencias.

**Ámbito:** documentación de estudio de SMR en Madrid. Los objetivos y las rúbricas de estas guías son una propuesta didáctica; la programación del centro establece la evaluación oficial. Las configuraciones están planteadas para máquinas virtuales y equipos propios de laboratorio.

## Guías

1. [Fundamentos y diseño de una LAN](01-fundamentos.md): modelos, medios, Ethernet, switching, direccionamiento IPv4 e IPv6.
2. [Configuración, observación y análisis](02-guia-tecnica.md): Linux, Windows, Wi-Fi, VLAN, routing y captura de paquetes.
3. [Prácticas completas](03-practicas.md): cableado, VLSM, capturas y segmentación.
4. [Diagnóstico, ejercicios y evaluación](04-diagnostico-y-evaluacion.md): método de trabajo, fallos frecuentes, preguntas y soluciones.
5. [Direccionamiento y ejercicios avanzados](05-direccionamiento-y-ejercicios-avanzados.md): VLSM completo, revisión de solapamientos, sumarización, /31, /32 e IPv6 /56, /64 y /127.
6. [Conmutación y diseño segmentado](06-conmutacion-y-diseno-segmentado.md): puertos, trunks, STP/RSTP, LACP, QoS y prueba de fallo controlado.
7. [Ingeniería Wi-Fi y capacidad](07-ingenieria-wifi-y-capacidad.md): radiofrecuencia, dBm/SNR, tiempo de aire, canales, movilidad y estudio reproducible.
8. [Análisis de protocolos y laboratorios](08-analisis-de-protocolos-y-laboratorios.md): secuencias sintéticas explicadas, TCP, ARP/ND, MTU, DNS/TLS e investigación por hipótesis.
9. [Alineación con los RA y criterios oficiales](09-alineacion-ra.md): los seis resultados y sus 51 criterios, con materiales, evidencias y condiciones de aceptación propuestas.
10. [Retos completos por RA](10-retos-por-ra.md): reconocimiento, despliegue físico, conectores de cobre/fibra, Wi-Fi/VLAN, mantenimiento y prevención.

Los [datos de alineación](alineacion-ra.json) conservan el enunciado de cada RA y vinculan cada letra de criterio con una actividad desarrollada. Los resúmenes de criterios y las condiciones de aceptación son propuestas didácticas; la programación del centro determina la evaluación oficial.

Consulta antes el [laboratorio común](../../docs/laboratorio.md). Continúa después con [Servicios en red](../../segundo/servicios-en-red/README.md) y vuelve al [índice general](../../README.md) para relacionar las asignaturas.

## Qué debes poder hacer al terminar

- Explicar una comunicación utilizando direcciones MAC, direcciones IP, puertos y protocolos, sin confundir sus funciones.
- Elaborar un plano físico, un esquema lógico y un inventario de puertos coherentes entre sí.
- Calcular red, broadcast, rango utilizable y prefijos sin depender de una calculadora.
- Configurar direcciones y rutas en el sistema que realmente administra cada interfaz.
- Identificar en una captura ARP, ICMP, DNS, TCP y TLS, y explicar sus límites de visibilidad.
- Diseñar VLAN y encaminamiento entre ellas con una política explícita de acceso.
- Distinguir pérdida, latencia, fluctuación y rendimiento; probar una hipótesis antes de cambiar la configuración.

## Conocimientos previos y material

Necesitas manejo básico de archivos, terminal, privilegios administrativos y virtualización. Para las primeras prácticas bastan dos VMs conectadas a la misma red aislada. Para VLAN se requiere un switch administrable o un simulador que implemente IEEE 802.1Q y, si se desea comunicación entre VLAN, un router o switch de capa 3.

En el laboratorio común, `srv01` utiliza `192.168.56.10/24` y `cli01` utiliza `192.168.56.20/24`. No hay puerta de enlace en esta interfaz LAB. Una interfaz NAT distinta proporciona acceso a Internet, si se necesita. Nunca supongas que `192.168.56.1` es un router: puede ser el adaptador del hipervisor y no reenviar paquetes.

## Ruta de estudio sugerida

| Etapa | Producto que debes elaborar | Condición para continuar |
| --- | --- | --- |
| 1. Medios y topología | Plano, etiquetado y ficha de cableado | Puedes localizar ambos extremos de cada enlace |
| 2. Ethernet | Explicación de ARP y tabla MAC | Distingues broadcast, unicast y flooding |
| 3. Direccionamiento | Plan IPv4 y esquema IPv6 | No hay rangos solapados ni direcciones reservadas usadas como hosts |
| 4. Configuración | Estado antes/después y pruebas | Justificas cada dirección y ruta |
| 5. Segmentación | Matriz de VLAN, puertos y acceso | Los permisos coinciden con el diseño |
| 6. Operación | Incidencia reproducible y resolución | Una segunda persona puede repetir tus comprobaciones |

No memorices únicamente salidas de comandos. Una captura y una tabla sólo sirven si puedes explicar qué hipótesis confirman, qué no demuestran y qué comprobarías después.

## Profundización de la edición ampliada

Los capítulos 5–8 desarrollan decisiones de diseño y operación que requieren relacionar varias capas. Realiza primero los cálculos sin configurar equipos, después el diseño de conmutación en una topología expresamente compatible, luego el estudio de radio y por último el análisis de evidencias. Cada bloque incluye una práctica adicional, problemas razonados y criterios propios de aceptación. Las secuencias de paquetes rotuladas sintéticas enseñan el mecanismo; no se presentan como capturas ejecutadas.

## Ruta de trabajo por resultados de aprendizaje

Utiliza la matriz del capítulo 9 para decidir qué evidencia necesitas, y el reto del capítulo 10 para prepararla y ejecutarla. RA1 construye el dossier de reconocimiento; RA2 despliega la maqueta de cableado; RA3 añade adaptadores y terminaciones de cobre y fibra; RA4 instala la red mixta y las VLAN; RA5 mantiene y repara; RA6 prepara y observa prevención y gestión ambiental durante las operaciones.

La VM permite practicar una parte lógica, pero no evidencia canalizaciones, armarios, conectores o cobertura de radio. Si falta equipo, conserva el diseño y registra la ejecución física como pendiente. Las fotografías y pruebas deben corresponder a tu bancada y a su identificación, y las operaciones se realizan bajo las condiciones de supervisión del centro.
