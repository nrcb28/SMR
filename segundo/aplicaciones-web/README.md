# 0228 · Aplicaciones web

Curso: **segundo de SMR en la Comunidad de Madrid**. El objetivo es instalar, configurar, mantener y utilizar aplicaciones web con criterios de disponibilidad, accesibilidad y seguridad. Comprender HTML y HTTP permite diagnosticar problemas que un asistente de instalación oculta; conocer bases de datos, permisos y copias permite recuperar el servicio cuando deja de funcionar.

La guía recorre dos casos complementarios: un sitio estático que se puede inspeccionar por completo y un CMS WordPress con Nginx, PHP-FPM y MariaDB. Incluye también aplicaciones colaborativas y criterios para elegir entre servicio alojado y mantenimiento propio. Los procedimientos se destinan al laboratorio aislado, no constituyen una autorización para exponer servidores sin revisión.

## Documentación y ejemplos

1. [Fundamentos: arquitectura, HTTP, sesiones y accesibilidad](01-fundamentos.md).
2. [Guía técnica: sitio estático, WordPress, permisos y recuperación](02-guia-tecnica.md).
3. [Cuatro prácticas con pruebas de aceptación](03-practicas.md).
4. [Diagnóstico y evaluación con respuestas razonadas](04-diagnostico-y-evaluacion.md).
5. [Frontend progresivo: DOM, eventos, formularios y accesibilidad](05-frontend-progresivo-y-accesibilidad.md).
6. [HTTP en operación: cachés, sesiones y controles](06-http-caches-sesiones-y-seguridad.md).
7. [Operación del CMS: migración, copias y recuperación](07-operacion-migracion-y-recuperacion-cms.md).
8. [Cuatro prácticas avanzadas y dieciséis casos resueltos](08-practicas-avanzadas-y-casos-resueltos.md).
9. [Alineación de los cinco RA y sus criterios oficiales](09-alineacion-ra.md).
10. [Retos completos por RA: CMS, LMS, archivos, ofimática y escritorio web](10-retos-por-ra.md).
11. [Complementos de despliegue: Moodle, Nextcloud, Office, webmail y CalDAV](11-complementos-curriculares.md).

## Ejemplos inspeccionables

- [Sitio estático inicial](ejemplos/sitio-estatico/index.html) y [hoja de estilos](ejemplos/sitio-estatico/estilos.css).
- [Registro local con mejora progresiva](ejemplos/registro-local/index.html), [CSS](ejemplos/registro-local/estilos.css) y [JavaScript](ejemplos/registro-local/app.js): simulación en memoria, sin backend ni persistencia.
- [Servidor virtual de Nginx para el CMS](ejemplos/wp-aula.nginx.conf).
- [Mu-plugin de confianza CA exclusivo del laboratorio](ejemplos/smr-lab-ca.php), con instalación, pruebas y retirada explicadas en la guía técnica.

## Prerrequisitos y entorno

Debes comprender permisos Linux, servicios, paquetes, direcciones IP, resolución de nombres y consultas SQL básicas. Revisa los módulos [Servicios en red](../servicios-en-red/README.md), [Sistemas operativos en red](../sistemas-operativos-en-red/README.md) y el [laboratorio común](../../docs/laboratorio.md).

La referencia es una VM Debian 13 `srv01`, IP de laboratorio `192.168.56.10/24`, una interfaz host-only y una NIC NAT independiente para descargas. El cliente `cli01` usa `192.168.56.20/24`; la interfaz de laboratorio no necesita una puerta de enlace ficticia. El sitio CMS se llama `wp.aula.test`. Utiliza una instantánea o un clon específico para estas prácticas si otras asignaturas ya han configurado servicios que utilicen los mismos puertos.

Los paquetes de Debian 13 proporcionan como referencia PHP 8.4 y MariaDB 11.8; comprueba siempre los candidatos reales y las actualizaciones. En la consulta oficial realizada para esta documentación, WordPress recomienda PHP 8.3 o posterior, MariaDB 10.11 o posterior o MySQL 8.0 o posterior, y HTTPS. La compatibilidad del núcleo no garantiza la de cada tema o complemento. Verifica la matriz oficial para la versión estable que elijas. [Requisitos](https://wordpress.org/about/requirements/) y [compatibilidad PHP](https://make.wordpress.org/core/handbook/references/php-compatibility-and-wordpress-versions/).

## Resultados demostrables

| Trabajo | Evidencia |
| --- | --- |
| Publicar contenido estático | Estructura semántica, recursos locales y comprobación con teclado |
| Explicar una petición | Método, estado, cabeceras y cuerpo identificados |
| Instalar un CMS | Inventario de versiones, configuración, roles y servicio funcional |
| Mantenerlo | Actualización ensayada, copia consistente y restauración comprobada |
| Elegir una aplicación colaborativa | Permisos, exportación, costes y salida del servicio documentados |

Estas evidencias y las rúbricas de las prácticas son propuestas educativas propias. No sustituyen la programación didáctica oficial. Vuelve al [índice general](../../README.md) para seguir el itinerario completo.

## Ruta de profundización

Tras completar el sitio estático y las prácticas base, estudia el capítulo 5 para relacionar HTML, reglas de entrada y DOM. Continúa con el 6 para interpretar HTTP y controles de aplicación, y utiliza el 7 sólo sobre un clon identificado del CMS. El capítulo 8 integra pruebas de frontend, caché, restauración y comunicación. Las comprobaciones de código y datos no sustituyen ensayar foco, anuncios, accesibilidad o continuidad en tu laboratorio; registra navegador, versiones y resultados realmente observados.

## Itinerario por resultados de aprendizaje

El [mapa de RA y criterios oficiales](09-alineacion-ra.md) identifica los 5 RA y sus 40 criterios, con paráfrasis didácticas, materiales, actividades y evidencias. Los [retos por RA](10-retos-por-ra.md) desarrollan las operaciones que debe poder demostrar el estudiante. Los [datos JSON](alineacion-ra.json) permiten revisar su trazabilidad. Una cobertura documental no acredita por sí sola la adquisición del RA.
