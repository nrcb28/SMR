# Fuentes, versiones y mantenimiento

[Índice](../README.md) · [Currículo de Madrid](curriculo-madrid.md)

## 1. Naturaleza del material

Este repositorio es una elaboración didáctica original para estudiar y practicar SMR. Sus explicaciones, ejemplos sintéticos, prácticas y rúbricas desarrollan competencias del ciclo, con enlaces a normativa y documentación técnica primaria. Los textos legales y manuales externos se consultan en su fuente; no se redistribuyen libros, cursos comerciales, licencias de software ni imágenes de sistemas operativos.

La organización por cursos sigue la tabla madrileña que se detalla en [currículo](curriculo-madrid.md). Una unidad puede profundizar en un tema que atraviesa varios módulos; esa elección no modifica el nombre oficial de una asignatura ni sus resultados de aprendizaje. Las ponderaciones y tiempos de las actividades del repositorio son propuestas de estudio.

## 2. Fuentes por área

| Área | Documentación primaria | Para qué contrastarla |
| --- | --- | --- |
| Currículo | [BOCM](https://www.bocm.es/), [BOE](https://www.boe.es/), [Comunidad de Madrid](https://www.comunidad.madrid/educacion/ensenanzas-formacion-profesional) | Módulos, horas, normativa e instrucciones vigentes |
| Debian/Linux | [Debian Reference](https://www.debian.org/doc/manuals/debian-reference/), [manuales Debian](https://manpages.debian.org/), [documentación del kernel](https://docs.kernel.org/) | Paquetes, comandos, servicios y comportamiento del sistema |
| Windows y AD | [Microsoft Learn: Windows Server](https://learn.microsoft.com/windows-server/), [PowerShell](https://learn.microsoft.com/powershell/) | Requisitos por versión, roles, cmdlets y recuperación |
| Samba | [Samba documentation](https://www.samba.org/samba/docs/) | Directorio, comparticiones y diferencias de roles |
| Protocolos | [RFC Editor](https://www.rfc-editor.org/) | Semántica de IP, DNS, DHCP, HTTP y TLS |
| DNS/DHCP | [BIND ARM](https://bind9.readthedocs.io/), [Kea ARM](https://kea.readthedocs.io/) | Sintaxis, opciones, validación y versiones de los servicios |
| Web y SSH | [Nginx](https://nginx.org/en/docs/), [OpenSSH](https://www.openssh.com/manual.html), [MDN](https://developer.mozilla.org/es/), [W3C](https://www.w3.org/TR/) | Configuración, protocolos y accesibilidad |
| CMS | [WordPress documentation](https://wordpress.org/documentation/), [requisitos WordPress](https://wordpress.org/about/requirements/) | Compatibilidad, actualizaciones, usuarios y copias |
| Ofimática | [LibreOffice Help](https://help.libreoffice.org/latest/es/), [guías LibreOffice](https://documentation.libreoffice.org/), [Microsoft Support](https://support.microsoft.com/) | Funciones, formatos, accesibilidad y diferencias de producto |
| Seguridad y privacidad | [INCIBE](https://www.incibe.es/), [AEPD](https://www.aepd.es/), [ENS en BOE](https://www.boe.es/eli/es/rd/2022/05/03/311/con) | Protección, incidentes, obligaciones y alcance de medidas |
| Prevención y empleo | [INSST](https://www.insst.es/), [SEPE](https://www.sepe.es/), [Seguridad Social](https://www.seg-social.es/) | Riesgos del trabajo, contratación y trámites |
| Emprendimiento | [AEAT](https://sede.agenciatributaria.gob.es/), [Plataforma PYME](https://plataformapyme.es/) | Obligaciones, facturación, fiscalidad e información empresarial |

Cada guía añade referencias relacionadas con sus procedimientos. Prioriza el manual de la versión instalada: un tutorial reciente puede describir otra distribución o un paquete con rutas distintas.

## 3. Decisiones de versión

La base común usa Debian 13, Windows 11 Pro y Windows Server 2025 para el escenario de AD de Microsoft. Se evita enseñar servicios sin mantenimiento como opción por defecto: DHCP se desarrolla con Kea; los protocolos antiguos que aparecen por razones curriculares se contextualizan frente a alternativas protegidas.

Consulta la compatibilidad del CMS, PHP, base de datos, extensiones y plugins antes de instalar. La versión de PHP del sistema no garantiza por sí sola que toda extensión de WordPress funcione. Mantén una relación de versiones y valida actualización y restauración en una copia del sitio.

Los nombres `ens19`, `.10`, `.20` y `aula.test` son convenciones del [laboratorio](laboratorio.md). Sustituir una IP exige revisar zona DNS, DHCP, rutas, cliente, certificados y reglas que dependan de ella. Un cambio local sin revisar dependencias puede dejar una práctica incoherente.

## 4. Qué se comprueba al mantener el repositorio

- Correspondencia entre índices, carpetas y módulos del inventario curricular.
- Existencia de destinos de enlaces internos y cierre de bloques de código.
- Legibilidad UTF-8 y ausencia de archivos de credenciales y discos virtuales.
- Sintaxis y comportamiento de ejemplos seleccionados que se puedan comprobar sin desplegar servicios externos.
- Consistencia del direccionamiento, funciones de VM y separación entre escenarios.
- Distinción entre ejemplos, resultados esperados y resultados realmente observados.

El [validador](../scripts/validar_documentacion.py) realiza las comprobaciones estáticas descritas en su salida. No valida todos los enlaces externos ni ejecuta automáticamente los comandos administrativos de las guías. Una comprobación estática no certifica compatibilidad de todas las versiones o cumplimiento normativo de una infraestructura.

## 5. Cómo revisar una guía después de un cambio

Registra versión anterior/nueva, fuente del cambio y procedimiento afectado. Parte de un laboratorio con estado conocido, valida sintaxis con la herramienta del servicio y realiza la prueba desde un cliente. Si cambia la salida, actualiza la explicación y conserva la evidencia que justifica la modificación.

Para normativa, revisa texto publicado, correcciones y modificaciones, además de instrucciones de curso. Para importes, tipos de cotización y fiscalidad, utiliza datos oficiales del periodo; los casos numéricos del repositorio indican sus supuestos y no pretenden fijar valores legales vigentes.

Una referencia inaccesible no demuestra que una norma haya sido derogada. Busca su publicación oficial, identificador y fecha. El enlace antiguo de la ficha IFCM01 devolvió 404 durante la preparación; la distribución se fundamenta en el BOCM y en las tablas horarias enlazadas por el portal oficial, evitando depender de esa ficha.
