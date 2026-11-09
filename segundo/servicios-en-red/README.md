# Servicios en red · 0227 · Segundo

Un servicio de red combina un proceso, una dirección y puerto de escucha, una configuración, datos persistentes y una política de acceso. Esta asignatura enseña a desplegarlo y a demostrar que responde correctamente desde el cliente, que rechaza lo que debe rechazar y que se puede recuperar tras un error.

El itinerario utiliza Debian 13 como servidor y Linux o Windows 11 Pro como cliente. Las versiones de paquetes y sus valores predeterminados pueden cambiar: identifica la versión instalada y contrasta su manual antes de trasladar una configuración. Las guías no afirman haber ejecutado los servicios en tu infraestructura.

## Guías

1. [Fundamentos y arquitectura](01-fundamentos.md): transporte, resolución de nombres, configuración dinámica, acceso remoto, web y correo.
2. [Guía técnica de despliegue](02-guia-tecnica.md): DNS BIND9, DHCPv4 Kea, SSH/SFTP y HTTPS Nginx con pruebas.
3. [Prácticas completas](03-practicas.md): servicios aislados, integración, casos negativos y recuperación.
4. [Diagnóstico y evaluación](04-diagnostico-y-evaluacion.md): síntomas, evidencias, problemas resueltos y preguntas.
5. [Correo local: laboratorio de arquitectura](05-correo-local.md): SMTP y buzones dentro de una VM, sin retransmisión pública.
6. [DNS: replicación y ciclo de cambio](06-dns-replicacion-y-ciclo-de-cambio.md): primaria/secundaria, TSIG, seriales, caché negativa, delegación y continuidad.
7. [DHCP, doble pila y operación](07-dhcp-dual-stack-y-operacion.md): estados, T1/T2, reservas, capacidad, relay, RA y DHCPv6.
8. [SSH, PKI y publicación web](08-ssh-pki-y-publicacion-web.md): configuración efectiva, SFTP limitado, rotación de certificados, proxy y control de solicitudes.
9. [Correo, observabilidad y continuidad](09-correo-observabilidad-y-continuidad.md): SPF/DKIM/DMARC, indicadores, percentiles, alertas y restauración de dependencias.
10. [Alineación con los RA y criterios oficiales](10-alineacion-ra.md): los ocho resultados y sus 63 criterios, con materiales, evidencias y aceptación didáctica.
11. [Retos completos por RA](11-retos-por-ra.md): configuración dinámica, nombres, FTP, correo, web, acceso remoto, Wi-Fi y pasarela.
12. [Complementos curriculares de implantación](12-complementos-curriculares-ra.md): caché recursiva, FTP activo/pasivo/anónimo aislado, IMAPS, escritorio remoto y pasarela/proxy con exterior simulado.

El [JSON de alineación](alineacion-ra.json) conecta cada criterio con una actividad desarrollada y una evidencia concreta. El mapa describe material y actividades disponibles; no acredita adquisición del alumnado ni fija una ponderación oficial.

Antes de empezar, revisa [Redes locales](../../primero/redes-locales/README.md) y el [laboratorio común](../../docs/laboratorio.md). El [índice general](../../README.md) relaciona estos procedimientos con sistemas operativos y seguridad.

## Objetivos prácticos

- Diferenciar servidor autoritativo, resolver y caché DNS.
- Configurar zonas directas e inversas y validar datos antes de recargar.
- Desplegar DHCP exclusivamente en LAB, con pool, reservas y opciones coherentes.
- Administrar por SSH comprobando la identidad del servidor y utilizando claves.
- Publicar un sitio HTTPS local con validación explícita de nombre y confianza.
- Explicar el recorrido de un correo y mantener un laboratorio sin open relay.
- Supervisar proceso, escucha, logs y experiencia del cliente como evidencias distintas.
- Restaurar configuraciones y datos sin convertir la restauración en una nueva avería.

## Contrato de laboratorio

| Elemento | Valor |
| --- | --- |
| Servidor | `srv01`, `192.168.56.10/24` |
| Cliente fijo | `cli01`, `192.168.56.20/24` |
| Interfaz de servicio | `ens19` sólo como ejemplo; confirmar nombre real |
| Dominio de pruebas | `aula.test` |
| Pool DHCP | `192.168.56.100–192.168.56.150` |
| Gateway en LAB | Ninguno: no existe router en el diseño base |
| Internet | NIC NAT separada, sin DHCP servido hacia ella |

El hipervisor puede incorporar su propio servidor DHCP en host-only. Debe estar desactivado en esa red antes de habilitar Kea. Comprueba también que LAB no esté en modo puente hacia la red física. Un servidor DHCP de prácticas mal conectado puede cambiar la configuración de equipos ajenos.

## Secuencia y entregables

Empieza por DNS con IP fija. Añade después DHCP y conserva una máquina con IP fija para administrar. Continúa con SSH y HTTPS. Por último integra los servicios y realiza la práctica base de correo, que permanece local a una VM y no pretende entregar correo en Internet. La ampliación por RA añade recogida IMAPS desde un cliente de LAB y envío a través de un túnel SSH, sin publicar SMTP ni habilitar retransmisión externa.

Cada servicio requiere ficha de diseño, copia previa de configuración, validación de sintaxis, estado de proceso, puertos, prueba desde cliente, caso de rechazo y recuperación. Las rúbricas propuestas son didácticas; el centro define la evaluación oficial.

## Ruta de profundización

Los capítulos 6–9 incorporan operación y cambios controlados. Replica primero una zona con una segunda VM `.30`; estudia después el estado temporal de DHCP, la identidad y confianza de accesos, y finalmente indicadores y continuidad. Cada ampliación distingue datos sintéticos de pruebas reales y añade una práctica con aceptación y retorno. Conserva escenarios separados: DNS de servicios, dominio AD, CMS y correo loopback no se juntan sin revisar puertos, identidades y dependencias.

## Ruta por resultados de aprendizaje

Consulta el capítulo 10 antes de elegir una práctica: RA1 corresponde a DHCP; RA2 a autoridad, caché y réplica DNS; RA3 a transferencia de ficheros; RA4 a correo y recogida remota; RA5 a servidores web; RA6 a acceso remoto CLI/gráfico; RA7 a AP y router inalámbrico; RA8 a pasarela y acceso entre redes. Los capítulos 11 y 12 desarrollan las operaciones que faltaban en el itinerario inicial y permiten registrar cada criterio con evidencia verificable.

Una sesión SFTP no prueba los canales FTP activo/pasivo; un Maildir local no prueba recogida remota; un dibujo de router no demuestra radio ni una conexión real de operador. Los retos conservan esas diferencias y señalan qué es ejecución, observación, simulación o pendiente. Las pruebas de FTP se aíslan en `ftplab/.40`; la pasarela utiliza prefijos propios en otra topología y no introduce un gateway ficticio en la LAB base.
