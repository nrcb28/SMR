# SMR · Sistemas Microinformáticos y Redes

Documentación técnica y práctica del ciclo de **Técnico en Sistemas Microinformáticos y Redes**, organizada por asignaturas de **primero y segundo de la Comunidad de Madrid**. Incluye fundamentos, procedimientos, comandos comentados, ejercicios resueltos, prácticas, diagnóstico y criterios para evaluar las evidencias.

**Referencia curricular:** plan madrileño adaptado a la nueva FP; Decreto 34/2009 modificado por el Decreto 102/2024, junto con el desarrollo de módulos transversales de 2025. Consulta y revisión de fuentes: **8 de noviembre de 2026**. La [guía del currículo](docs/curriculo-madrid.md) contiene los enlaces al BOCM, la distribución horaria y las particularidades del proyecto y la optatividad. Las guías y rúbricas de este repositorio son material didáctico propio.

## Empieza aquí

1. Consulta el [mapa de asignaturas y horas](docs/curriculo-madrid.md).
2. Prepara el [laboratorio común](docs/laboratorio.md) antes de ejecutar prácticas de administración.
3. Sigue la [ruta de aprendizaje](docs/ruta-de-estudio.md) y el índice de tu asignatura.
4. Documenta cada práctica con la [plantilla de memoria](recursos/plantillas/memoria-practica.md) y la [ficha de incidencia](recursos/plantillas/incidencia.md).
5. Integra lo aprendido en el [proyecto intermodular](segundo/proyecto-intermodular/README.md).

Las explicaciones se pueden leer sin instalar software. Los ejercicios de instalación, permisos, redes y servicios se realizan en máquinas virtuales de laboratorio. Cada guía distingue el contexto y la finalidad de los comandos; los resultados mostrados como ejemplos son expectativas didácticas que debes contrastar en tu equipo.

## Primer curso

| Código | Asignatura | Contenidos principales |
| --- | --- | --- |
| 0221 | [Montaje y mantenimiento de equipos](primero/montaje-y-mantenimiento-de-equipos/README.md) | Arquitectura, compatibilidad, montaje, firmware, almacenamiento, averías y periféricos |
| 0222 | [Sistemas operativos monopuesto](primero/sistemas-operativos-monopuesto/README.md) | Instalación de Windows/Linux, procesos, memoria, archivos, usuarios, automatización y recuperación |
| 0223 | [Aplicaciones ofimáticas](primero/aplicaciones-ofimaticas/README.md) | Documentos, hojas de cálculo, bases de datos, presentaciones, formatos y accesibilidad |
| 0225 | [Redes locales](primero/redes-locales/README.md) | Ethernet, cableado, TCP/IP, subnetting, IPv6, VLAN, conmutación y Wi-Fi |
| 1709 | [Itinerario personal para la empleabilidad I](primero/itinerario-personal-para-la-empleabilidad-i/README.md) | Prevención de riesgos, relaciones laborales, sector informático y desarrollo profesional |
| CMO | [Módulo optativo de primero](primero/modulo-optativo/README.md) | Orientación para adaptar la guía a la oferta del centro; propuesta complementaria identificada |

Accede al [índice completo de primero](primero/README.md).

## Segundo curso

| Código | Asignatura | Contenidos principales |
| --- | --- | --- |
| 0224 | [Sistemas operativos en red](segundo/sistemas-operativos-en-red/README.md) | Servidores, directorios, dominios, Samba, AD DS, permisos y administración |
| 0226 | [Seguridad informática](segundo/seguridad-informatica/README.md) | Riesgo, endurecimiento, cifrado, cortafuegos, copias, restauración e incidentes |
| 0227 | [Servicios en red](segundo/servicios-en-red/README.md) | DNS, DHCP, SSH, transferencia segura, HTTP/TLS y arquitectura de correo |
| 0228 | [Aplicaciones web](segundo/aplicaciones-web/README.md) | HTML/CSS, HTTP, accesibilidad, CMS, bases de datos, mantenimiento y aplicaciones colaborativas |
| 0156 | [Inglés profesional](segundo/ingles-profesional/README.md) | Manuales, tickets, conversación de soporte, correos y vocabulario técnico |
| 1710 | [Itinerario personal para la empleabilidad II](segundo/itinerario-personal-para-la-empleabilidad-ii/README.md) | Búsqueda de empleo, colaboración, iniciativa y proyecto empresarial |
| 1664 | [Digitalización aplicada a los sectores productivos](segundo/digitalizacion-aplicada-a-los-sectores-productivos/README.md) | IT/OT, nube, datos, IoT, automatización e IA aplicada |
| 1708 | [Sostenibilidad aplicada al sistema productivo](segundo/sostenibilidad-aplicada-al-sistema-productivo/README.md) | Energía, vida útil, reparación, economía circular, RAEE y medición |
| CMO | [Módulo optativo de segundo](segundo/modulo-optativo/README.md) | Orientación sobre la oferta del centro y propuesta complementaria |
| 1713 | [Proyecto intermodular](segundo/proyecto-intermodular/README.md) | Diseño, implantación, documentación y defensa de una infraestructura de pequeña empresa |

Accede al [índice completo de segundo](segundo/README.md). La carpeta del proyecto se ubica aquí para facilitar su entrega final; **el proyecto tiene carácter transversal** y el centro determina su inicio, que en presencial no puede ser posterior al comienzo de segundo según las instrucciones de 2026/2027. La [formación en empresa](docs/formacion-en-empresa.md) se explica por separado porque forma parte de la nueva organización de la FP.

## Material de apoyo

| Recurso | Uso |
| --- | --- |
| [Laboratorio común](docs/laboratorio.md) | Máquinas, direccionamiento, nombres, aislamiento, instantáneas y verificación inicial |
| [Ruta de estudio](docs/ruta-de-estudio.md) | Dependencias entre asignaturas y progresión por hitos |
| [Método de diagnóstico](docs/metodo-de-diagnostico.md) | Hipótesis, pruebas, causas y comprobación de la recuperación |
| [Glosario técnico](docs/glosario.md) | Términos esenciales y distinciones que evitan errores |
| [Recursos y plantillas](recursos/README.md) | Memorias, inventario, incidencias, pruebas de aceptación y scripts |
| [Fuentes y mantenimiento](docs/fuentes-y-mantenimiento.md) | Normativa, documentación primaria, versiones y alcance de la revisión |
| [Revisión de la entrega](docs/validacion.md) | Comprobaciones realizadas, correcciones y alcance de las pruebas |
| [Plan anterior](plan-anterior/README.md) | FOL, Empresa e iniciativa emprendedora y FCT, expresamente marcadas como históricas |

## Consultar y trabajar con el repositorio

GitHub permite leer todas las guías y descargar los archivos desde **Code → Download ZIP**. Para trabajar con Git:

```bash
git clone https://github.com/nrcb28/smr.git
cd smr
python3 scripts/validar_documentacion.py
```

El validador comprueba estructura, archivos, enlaces locales y bloques de código; requiere Python 3.9 o posterior y utiliza únicamente su biblioteca estándar. No instala servicios ni cambia la configuración de tu equipo. Las comprobaciones de documentación no sustituyen las pruebas funcionales de las prácticas.

Para proponer una corrección, identifica asignatura, archivo, versión del sistema, comportamiento esperado y evidencia obtenida. Sigue [CONTRIBUTING.md](CONTRIBUTING.md). Nunca publiques contraseñas, claves privadas, datos de clientes ni capturas sin revisar.
