# 7. Operación de un CMS: cambios, migración y recuperación comprobada

[Índice](README.md) · [Instalación de laboratorio](02-guia-tecnica.md)

## 1. De una instalación a un servicio mantenible

Un asistente que termina correctamente demuestra una parte de la instalación. Operar el servicio exige conocer versiones, dependencias, permisos, datos, copias, certificados y responsables. El CMS puede seguir mostrando la portada mientras la API REST, tareas programadas, subidas o edición fallan. Define qué operaciones constituyen el servicio antes de aceptar su estado.

Para el caso de este repositorio, la aceptación mínima incluye portada, autenticación, creación de borrador, publicación por el rol autorizado, subida de imagen sintética, lectura anónima y restauración de una entrada anterior. Añade pruebas de denegación para un rol sin capacidades. Si sólo se comprueba HTTP 200, una página de error personalizada podría pasar la prueba.

La base mantiene Debian 13, PHP 8.4-FPM, MariaDB y WordPress compatible, con `wp.aula.test` en `192.168.56.10`. Conserva el modelo de código propiedad de root, contenido subido escribible por el servicio, Nginx limitado a LAB y el mu-plugin de confianza de la CA descrito en la guía. La ampliación no habilita actualizaciones desde el panel ni elimina esas restricciones.

## 2. Inventario y registro de cambio

Registra SO, paquetes, versión del núcleo WordPress, temas, plugins, idioma, zona horaria, esquema de base, prefijo de tablas y extensiones PHP relevantes. Añade versión y hash de artefactos usados cuando sea útil para reproducir una actualización. La palabra «actualizado» pierde significado si no identifica respecto de qué fecha y versión se comparó.

Un cambio necesita motivo, alcance, precondiciones, ventana, pruebas y reversión. La compatibilidad del núcleo con PHP no garantiza la de todos los plugins. Tampoco una extensión con versión reciente es automáticamente necesaria o apropiada. Conserva sólo las que aporten una función justificada y revisa las dependencias entre ellas antes de retirar una.

### Ficha de cambio didáctica

| Campo | Ejemplo sintético |
| --- | --- |
| Motivo | Ensayar una actualización compatible del tema |
| Estado inicial | Versiones e inventario de plugins registrados |
| Riesgo concreto | Cambios de plantilla que afecten menú y formulario |
| Copia | Base, contenido, configuración e inventario consistentes |
| Aceptación | Portada, roles, edición, imagen y pruebas de accesibilidad acordadas |
| Reversión | Restaurar conjunto previo y repetir la matriz |
| Decisión | Aceptar o revertir según resultados observados |

No conviertas «se puede volver a la versión anterior» en una promesa sin prueba. Una actualización puede migrar tablas o datos; restaurar sólo archivos del núcleo anterior puede dejar un conjunto incompatible. El punto de recuperación debe contemplar los componentes que cambiaron juntos.

## 3. Preparar un entorno de ensayo sin duplicar identidades en la misma red

La alternativa más sencilla para repetir el sitio es un clon **en una red interna diferente**, por ejemplo `LAB-CMS-ENSAYO`, separado de la LAB original. Puede conservar `.10` y `wp.aula.test` si el cliente de ensayo también está aislado y resuelve hacia ese clon. No conectes dos VMs con la misma dirección al mismo segmento por confiar en que «una es de pruebas».

Desactiva correo saliente, integraciones, analítica y tareas que puedan contactar sistemas reales. Una copia del sitio puede seguir conteniendo claves y direcciones de integración aunque no tenga visitantes. Para el ejercicio utiliza contenido sintético y revisa configuración antes de proporcionar acceso a otros estudiantes.

La NIC NAT sirve para descargas y actualizaciones, pero no debe publicar puertos del clon ni sustituir el aislamiento de LAB. Si necesitas cambiar de hostname para una práctica de migración, prepara resolución, `server_name`, certificado con SAN correspondiente y confianza del cliente y del servidor. El mu-plugin incluido acepta exactamente `wp.aula.test`: una copia con otro nombre requiere adaptar deliberadamente su condición **sólo en ese clon**, sin convertirla en un comodín.

Documenta cuál de los dos escenarios utilizas: reproducción del mismo nombre en red separada o migración a un nombre distinto. Mezclar ambos hace que algunas pruebas funcionen por una entrada antigua de hosts y otras alcancen un servidor equivocado. Identifica el destino mediante contenido o registro controlado, además de la IP.

## 4. Copia consistente: qué debe formar el conjunto

El estado recuperable incluye base, `wp-content`, configuración, artefactos de código necesarios, Nginx, política relevante de PHP y referencia a certificados/claves por su canal protegido. La exportación de entradas del panel no contiene todo ese conjunto. Una imagen de una VM ayuda, pero su coherencia y dependencia del almacenamiento deben analizarse igual que el resto del backup.

Antes de exportar, identifica motores de tablas y escrituras previstas. En una consola autenticada, selecciona primero el esquema de laboratorio correcto —en este ejemplo, `USE wp_aula;`— y comprueba `SELECT DATABASE();`. Si `DATABASE()` devuelve `NULL`, la consulta siguiente no está identificando un esquema. Después consulta sus motores:

```sql
SELECT ENGINE, COUNT(*) AS TABLAS
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = DATABASE()
GROUP BY ENGINE;
```

Una exportación con `--single-transaction` permite una vista consistente para tablas transaccionales bajo sus condiciones, pero no congela automáticamente cambios de archivos ni garantiza coherencia de motores no transaccionales o DDL concurrente. Para el laboratorio pequeño, acuerda una ventana sin edición ni cambios de estructura y realiza el conjunto de manera coordinada. La política de una aplicación con carga real puede necesitar herramientas y diseño adicionales.

La guía inicial contiene un ejemplo de backup con privilegios administrativos locales. Otra opción didáctica para la base, si el usuario tiene los permisos requeridos, es una exportación con solicitud interactiva de contraseña, dentro de una carpeta privada nueva:

```bash
umask 077
destino_cms="$HOME/respaldo-cms-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$destino_cms"
mariadb-dump --user=wp_aula --password --single-transaction --quick \
  wp_aula > "$destino_cms/base.sql"
```

Comprueba el código de salida antes de considerar válida la exportación y protege el fichero: puede contener usuarios, hashes y contenido sensible. No incluyas la contraseña después de `--password=`. El comando anterior no copia archivos, permisos ni configuración y no pretende ser un backup completo por sí solo.

Registra identificador del conjunto, hora de comienzo/fin, versiones, componentes y hashes de los ficheros terminados. Un hash permite comprobar si esos bytes cambiaron; no demuestra que la base se pueda importar o que los archivos correspondan al mismo estado lógico. La restauración es la prueba funcional que falta.

## 5. Restaurar antes de dar por válido el backup

El destino de recuperación debe estar identificado y separado del original. Restaura en una base nueva con credenciales propias y un árbol de archivos de ensayo; no importes un dump sobre la única base vigente para comprobar si funciona. Una ruta con nombre «restore» no garantiza aislamiento si la configuración continúa apuntando al esquema original.

Después de restaurar, revisa `DB_NAME`, `DB_USER`, `DB_HOST`, URL del sitio, permisos y archivos que requieran escritura. No reutilices a ciegas un `wp-config.php` con credenciales de otro entorno. Configura la confianza HTTPS y resolución desde el cliente y desde el servidor; las peticiones internas pueden fallar aunque el navegador abra la portada.

Ejecuta la misma matriz que antes del backup y comprueba una entrada y una imagen cuyo contenido conoces. Añade una publicación creada **después** del punto de copia en el original sintético: que no aparezca en el destino recuperado ayuda a demostrar qué punto has restaurado. No es un defecto del backup; representa su pérdida de datos real respecto del estado posterior.

Mide desde el comienzo operativo de recuperación hasta la aceptación del servicio, sin excluir silenciosamente preparación o descarga si el objetivo requiere incluirlas. Distingue tiempo de transferencia, importación, configuración y prueba. Compara con RTO y RPO declarados y explica qué paso domina; una estimación teórica de transferencia no sustituye medir el proceso completo.

## 6. WP-CLI como herramienta controlada

WP-CLI no forma parte automática de toda instalación WordPress ni de los paquetes elegidos para PHP. Si lo utilizas, obtén la herramienta mediante su [procedimiento oficial de instalación](https://make.wordpress.org/cli/handbook/guides/installing/), registra versión y origen y comprueba `wp --info`. No ejecutes como root un script descargado sin inspección ni añadas `--allow-root` para evitar entender permisos.

Las consultas deben ejecutarse con una identidad que pueda leer la instalación y acceder al esquema. En el clon de este laboratorio, `www-data` dispone de esas capacidades. Antes de una consulta confirma la ruta real y los datos que carga; los plugins pueden ejecutar lógica al arrancar WordPress. Ejemplos de inspección:

```bash
sudo -u www-data wp --path=/srv/www/wp-aula core version
sudo -u www-data wp --path=/srv/www/wp-aula plugin list
sudo -u www-data wp --path=/srv/www/wp-aula theme list
sudo -u www-data wp --path=/srv/www/wp-aula option get home
sudo -u www-data wp --path=/srv/www/wp-aula option get siteurl
```

Los comandos de actualización modifican archivos o base y no deben copiarse sin adaptar la identidad de despliegue y el modelo de permisos. El código sigue perteneciendo a root en la práctica base; ampliar escritura a todo `www-data` para que una herramienta deje de fallar cambia el diseño de seguridad. Utiliza un proceso de despliegue administrado y ensayado, manteniendo separada la operación editorial.

## 7. Migrar nombres sin dañar datos serializados

WordPress y sus extensiones pueden guardar estructuras serializadas que incluyen longitudes de cadenas. Un `REPLACE()` SQL indiscriminado sobre todos los valores puede dejar longitudes incorrectas y dañar esas estructuras. La operación requiere una herramienta consciente del formato y un alcance que corresponda a las tablas de ese sitio.

Para el ejercicio de un único sitio, prepara antes `wp-ensayo.aula.test`, con resolución, certificado y Nginx correctos. Confirma que el clon usa la base restaurada y no la original. Con WP-CLI instalado y permisos revisados, realiza primero la simulación:

```bash
sudo -u www-data wp --path=/srv/www/wp-aula search-replace \
  'https://wp.aula.test' 'https://wp-ensayo.aula.test' \
  --skip-columns=guid --precise --dry-run
```

La simulación informa cambios propuestos de esa sustitución; no es una autorización para aplicarlos a otra instalación. Revisa tablas, número de coincidencias, URL antiguas con otras variantes y significado de los resultados. La opción que omite `guid` evita tratar ese identificador como una URL de presentación ordinaria. No añadas `--all-tables` para «asegurarte» si la base contiene tablas ajenas.

Sólo en el clon identificado, con backup y plan de recuperación, se aplica la operación revisada retirando `--dry-run`. Después comprueba `home`, `siteurl`, enlaces, medios, menú, acceso editorial y datos de plugins. Actualiza el mu-plugin local para el nombre exacto elegido y mantén verificación TLS. Si aparece una redirección al sitio anterior, investiga configuración y caché antes de repetir reemplazos cada vez más amplios.

## 8. Actualización por etapas y reversión

Consulta requisitos del núcleo, PHP, base, tema y plugins para la versión prevista. Prepara una matriz de compatibilidad que distinga declarado por el proveedor y comprobado en el clon. Un componente sin información suficiente puede requerir sustitución o una prueba adicional; no inventes compatibilidad porque el instalador no proteste.

Aplica un conjunto pequeño de cambios y repite las funciones críticas. Cambiar simultáneamente PHP, núcleo, tema, plugins y estructura de Nginx dificulta atribuir un fallo. En ocasiones existen dependencias que obligan a coordinar versiones; documenta ese orden y el punto de recuperación del conjunto completo.

La reversión requiere decidir qué hacer con datos creados tras el cambio. Restaurar una base anterior puede perder edición legítima; volver sólo al código puede no ser compatible con una migración de esquema. En el laboratorio detén edición y utiliza contenido sintético para ensayar esa decisión. En operación real se necesita una estrategia que contemple continuidad y conservación de cambios, según el servicio.

## 9. Observabilidad desde el usuario hasta el backend

Relaciona una operación con hora, URL, estado, duración y referencia de registro. Nginx informa del frontal; PHP-FPM y WordPress aportan otros errores; MariaDB puede revelar problemas de conexión o consultas. No confíes en una única pantalla que diga «todo correcto». Las herramientas de Salud del sitio ayudan, pero tampoco representan todas las rutas funcionales.

No publiques logs completos con cookies, credenciales, parámetros privados o rutas internas innecesarias. Para una incidencia escolar basta un extracto sintético o sanitizado que conserve la información relevante. Evita habilitar visualización pública de errores para depurar un fallo de producción: utiliza registros con acceso adecuado y configura el nivel según el entorno.

Mide una operación con carga y condiciones definidas: primera carga, repetición con caché, tamaño de imagen o número de usuarios simulados. La mediana de varias pruebas puede describir el caso mejor que un único valor; percentiles requieren muestra y método suficientes. No conviertas un benchmark de dos peticiones en una capacidad garantizada del servidor.

## 10. Práctica de continuidad del CMS

Prepara tres entradas y dos imágenes sintéticas antes del punto de copia. Registra inventario, genera el conjunto y restaura en la red de ensayo. Después crea una entrada posterior sólo en el original y compara ambos estados. Ejecuta pruebas de portada, roles, edición, subida, API y HTTPS interno.

En una copia adicional, ensaya la migración de nombre mediante simulación y sustitución controlada. Predice qué debe cambiar en DNS, TLS, Nginx, configuración y datos; verifica cada capa por separado. Entrega cronograma real, prueba del punto de recuperación, defectos detectados y propuesta para reducir tiempo sin eliminar controles.

Rúbrica propia: consistencia y recuperación 30 %, aislamiento e identidades 20 %, migración y compatibilidad 20 %, medición y aceptación 20 %, documentación y fuentes 10 %. No se afirma que estas tareas hayan sido ejecutadas en tu entorno: conserva la evidencia obtenida durante tu práctica.

## Referencias primarias

- [WordPress: copias de seguridad](https://developer.wordpress.org/advanced-administration/security/backup/), [actualización](https://developer.wordpress.org/advanced-administration/upgrade/upgrading/) y [migración](https://developer.wordpress.org/advanced-administration/upgrade/migrating/).
- [WP-CLI: search-replace](https://developer.wordpress.org/cli/commands/search-replace/) y [comandos](https://developer.wordpress.org/cli/commands/).
- [MariaDB: documentación](https://mariadb.com/docs/): verifica las opciones de `mariadb-dump` y las condiciones de consistencia de la versión instalada.
- [WordPress: requisitos](https://wordpress.org/about/requirements/): el núcleo y cada extensión requieren comprobación de compatibilidad.
