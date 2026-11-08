# Glosario técnico de SMR

[Índice](../README.md) · [Laboratorio](laboratorio.md)

Las definiciones siguientes resaltan diferencias útiles para configurar y diagnosticar. Consulta la guía de la asignatura para el procedimiento y las fuentes específicas.

## Arquitectura, almacenamiento y sistemas

| Término | Significado y distinción práctica |
| --- | --- |
| Bit y byte | Un byte contiene ocho bits. Las velocidades de enlace suelen expresarse en bit/s; las transferencias y capacidades pueden usar bytes. |
| GB y GiB | GB es 10⁹ bytes; GiB es 2³⁰ bytes. La diferencia de unidades explica parte de la capacidad que muestra un SO, antes de particiones y reservas. |
| ISA | Conjunto de instrucciones y contrato visible de una arquitectura de CPU; no equivale al socket de la placa. |
| Núcleo e hilo | Un núcleo es una unidad física de ejecución; un hilo lógico presentado por SMT comparte recursos. Duplicar hilos no garantiza duplicar rendimiento. |
| Caché | Almacenamiento que reduce el coste de recuperar datos. Su efecto obliga a distinguir pruebas con caché fría y caliente. |
| ECC | Mecanismo de detección/corrección de errores de memoria que requiere compatibilidad de CPU, placa y módulo. |
| UEFI | Interfaz de firmware que inicializa la plataforma y participa en el arranque. GPT es una estructura de particiones, no otro firmware. |
| Secure Boot | Comprobación de componentes de arranque según claves y políticas. No equivale a cifrado del disco. |
| TPM | Componente de seguridad que protege operaciones y material criptográfico bajo políticas; no es una copia de recuperación de tus claves. |
| GPT | Tabla de particiones con identificadores y metadatos redundantes. Hay que distinguir disco, partición, volumen y sistema de archivos. |
| SATA, PCIe y NVMe | SATA y PCIe describen interfaces/enlaces; NVMe es un protocolo de acceso a almacenamiento que normalmente utiliza PCIe. M.2 describe un formato/conector con distintas capacidades. |
| IOPS y latencia | IOPS cuenta operaciones por segundo; latencia mide cuánto tarda una. Su relación depende de tamaño de petición, concurrencia y carga. |
| SMART | Telemetría del dispositivo de almacenamiento; ayuda a detectar problemas, pero un estado saludable no garantiza ausencia de fallos futuros. |
| RAID | Organización de discos para rendimiento o disponibilidad según nivel. No protege por sí sola frente a borrado, ransomware o pérdida del conjunto. |
| Sistema de archivos | Estructura que organiza nombres, datos y metadatos: por ejemplo NTFS o ext4. Un volumen montado no tiene por qué corresponder a un disco completo. |
| Proceso y servicio | Un proceso es una instancia de ejecución; un servicio es una función administrada por el sistema que puede involucrar uno o varios procesos. |
| Memoria virtual | Espacio y mecanismos de traducción de direcciones que utiliza un proceso. No significa que toda la memoria virtual esté almacenada en swap. |
| Paginación | Gestión de memoria por páginas; puede incluir movimiento entre RAM y respaldo. Un fallo de página no implica necesariamente lectura de disco. |
| UID, GID y SID | Identificadores de principales: usuarios y grupos UNIX mediante UID/GID; principales de seguridad Windows mediante SID. Un nombre coincidente no crea identidad compartida. |
| ACL | Lista de control de acceso. El permiso efectivo depende de identidad, grupos, herencia, reglas aplicables y capa de acceso. |
| Hipervisor | Software que ejecuta y aísla máquinas virtuales. Las VMs comparten recursos físicos y requieren dimensionamiento. |
| Instantánea | Estado de una VM o almacenamiento que depende de la tecnología y de archivos base. Se diferencia de una copia independiente y de un backup coherente de aplicación. |

## Redes y servicios

| Término | Significado y distinción práctica |
| --- | --- |
| MAC | Identificador de capa de enlace de una interfaz. Puede cambiar o suplantarse y no prueba identidad de una persona. |
| Trama y paquete | La trama transporta datos en un enlace; el paquete IP permite comunicación entre redes. Cada capa añade sus propios campos. |
| MTU | Máximo tamaño de unidad transportada por una interfaz/enlace. Un problema de MTU puede permitir paquetes pequeños y romper otras comunicaciones. |
| CIDR | Notación de dirección/prefijo como `/24`; el prefijo indica los bits de red, no el número de equipos. |
| Subred | Conjunto de direcciones determinado por un prefijo. Las reglas de hosts de IPv4 ordinario no se trasladan sin matices a `/31`, `/32` o IPv6. |
| VLAN | Separación lógica de capa 2. Una VLAN no crea por sí sola reglas de firewall ni routing entre segmentos. |
| Puerto access y trunk | Access transporta habitualmente una VLAN de usuario sin etiqueta hacia un equipo; trunk transporta VLAN mediante etiquetado y una política definida. Los detalles dependen del fabricante. |
| STP | Familia de mecanismos para impedir bucles de capa 2 con topologías redundantes. No reemplaza el enrutamiento IP. |
| ARP y ND | ARP resuelve vecinos en IPv4. Neighbor Discovery en IPv6 incorpora descubrimiento de vecinos y otras funciones; IPv6 no usa ARP. |
| Gateway | Siguiente salto para destinos que requieren una ruta. Una dirección `.1` no es gateway sólo por acabar en uno. |
| NAT | Traducción de direcciones y, a menudo, puertos. El aislamiento y filtrado deben analizarse en la política real, no deducirse sólo de la palabra NAT. |
| TCP y UDP | TCP proporciona un flujo fiable y ordenado; UDP transporta datagramas. La aplicación determina su comportamiento y puede implementar controles adicionales. |
| Puerto | Número que ayuda a identificar extremos de transporte. Un puerto abierto no garantiza que el servicio sea correcto o esté autorizado. |
| DHCP | Asigna parámetros a clientes mediante concesiones. Un segundo servidor no previsto puede introducir direcciones, DNS y gateways incorrectos. |
| SLAAC | Configuración autónoma IPv6 basada en anuncios de router y reglas del protocolo. La puerta por defecto se aprende mediante RA, no de DHCPv6. |
| DNS autoritativo y recursivo | El autoritativo publica una zona; el recursivo busca respuestas para clientes. Mezclar funciones requiere controles explícitos. |
| TTL | Tiempo de vida; en DNS limita la reutilización en caché. En IPv4 el campo TTL limita saltos; no son el mismo mecanismo. |
| FQDN | Nombre completo de un recurso dentro de la jerarquía DNS. En archivos de zona el punto final distingue un nombre absoluto. |
| A, AAAA, PTR y SRV | Registros DNS para dirección IPv4, dirección IPv6, nombre inverso y localización de servicios respectivamente. |
| HTTP y HTTPS | HTTP define mensajes y semántica; HTTPS lo transporta sobre TLS. Cifrar el transporte no elimina errores de autorización o de aplicación. |
| TLS | Protocolo de protección del canal, autenticación y negociación criptográfica. La validación incluye confianza, nombre, fechas y política. |
| SNI | Información que permite al servidor TLS seleccionar un contexto por nombre. Cambiar una URL por una IP puede alterar la selección y validación del certificado. |
| SSH y SFTP | SSH protege sesiones y otros canales; SFTP es un protocolo de transferencia sobre SSH. SFTP no es FTP con TLS. |
| SMB | Protocolo de acceso compartido, entre otras funciones. Los permisos de recurso y del sistema de archivos deben evaluarse juntos. |
| LDAP y Kerberos | LDAP permite acceder a directorios; Kerberos permite autenticación mediante tickets. AD utiliza además DNS, tiempo y otros componentes. |
| GPO | Conjunto de políticas de grupo en Active Directory. Su aplicación depende de ámbito, vínculos, filtrado, herencia y momento de actualización. |

## Seguridad, aplicaciones y gestión

| Término | Significado y distinción práctica |
| --- | --- |
| Autenticación y autorización | Autenticación comprueba quién presenta una identidad; autorización decide qué acciones puede realizar. |
| MFA | Autenticación que combina factores de categorías distintas. Dos contraseñas no aportan dos categorías de factor. |
| Hash y cifrado | Un hash resume datos sin una operación ordinaria de descifrado; cifrado permite recuperar información con la clave apropiada. Las contraseñas necesitan esquemas de derivación adecuados. |
| RPO y RTO | RPO expresa pérdida de datos admisible en tiempo; RTO, tiempo objetivo de recuperación. Deben contrastarse con frecuencia de copias y restauraciones medidas. |
| Amenaza, vulnerabilidad y riesgo | Amenaza es una causa potencial; vulnerabilidad, una debilidad; riesgo relaciona probabilidad e impacto en un contexto concreto. |
| Hardening | Reducción y control de superficie expuesta: servicios, privilegios, configuración, actualizaciones y seguimiento. |
| Registro y auditoría | Un registro recoge eventos; una auditoría evalúa evidencias frente a requisitos. Tener muchos logs no asegura trazabilidad útil. |
| CSV y tipo de dato | CSV transporta campos de texto con convenciones de delimitación. Importar requiere decidir separador, codificación, fechas y decimales. |
| Clave primaria y foránea | La primaria identifica filas; la foránea mantiene una relación referencial. Relacionar tablas por texto libre dificulta integridad. |
| Sesión y cookie | La sesión mantiene contexto lógico; la cookie es un mecanismo del navegador para almacenar/enviar datos. No toda cookie es una sesión ni toda sesión depende de una única cookie. |
| CMS | Gestor de contenidos con usuarios, datos y extensiones; necesita actualizaciones, control de permisos y restauración. |
| SaaS, PaaS e IaaS | Modelos de servicio que distribuyen responsabilidades. Usar nube no traslada automáticamente todas las obligaciones al proveedor. |
| IT y OT | IT se centra en información y sistemas de negocio; OT controla procesos físicos. En OT la disponibilidad y seguridad física condicionan cambios. |
| RAEE | Residuos de aparatos eléctricos y electrónicos sujetos a gestión específica; borrar datos y gestionar el residuo son tareas diferentes. |
| kW y kWh | kW mide potencia; kWh energía acumulada. Un equipo de 0,1 kW durante 8 horas consume 0,8 kWh bajo esa hipótesis constante. |
| SLA y SLO | SLA recoge compromisos de servicio; SLO expresa un objetivo medible. Ninguno demuestra por sí solo que el servicio cumpla. |

## Fuentes para ampliar

[RFC Editor](https://www.rfc-editor.org/), [Debian Reference](https://www.debian.org/doc/manuals/debian-reference/), [Microsoft Learn](https://learn.microsoft.com/), [MDN Web Docs](https://developer.mozilla.org/es/), [INCIBE](https://www.incibe.es/) y [MITECO: RAEE](https://www.miteco.gob.es/es/calidad-y-evaluacion-ambiental/temas/prevencion-y-gestion-residuos/flujos/aparatos-electr.html).
