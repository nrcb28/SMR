# Diagnóstico de aplicaciones web y evaluación

## 1. Seguir la petición y reunir evidencias

Empieza por URL, hora, cliente y alcance: ¿falla una persona, un navegador, una ruta o todo el servicio? Conserva la configuración previa y ejecuta primero consultas. Reiniciar todos los servicios puede ocultar una causa temporal y destruir la evidencia de un fallo que volverá a ocurrir.

```bash
getent hosts wp.aula.test
ip -br address
ss -lntp
systemctl status nginx php8.4-fpm mariadb --no-pager
sudo nginx -t
sudo journalctl -u nginx -u php8.4-fpm -u mariadb --since '15 minutes ago'
```

Estos comandos consultan nombre, interfaz, listeners, estado, configuración y eventos recientes. Las versiones de servicio pueden diferir: ajusta el nombre FPM identificado en tu instalación. `nginx -t` no aplica cambios. Los registros pueden contener información sensible: recorta las líneas necesarias y elimina tokens, cookies y datos personales antes de compartirlos.

Inspecciona después el registro del sitio, no sólo el general. Si la respuesta sale de un servidor virtual distinto, comprueba `Host`, SNI, `server_name` y listeners. Una petición a la IP no reproduce exactamente una petición al nombre HTTPS. Para fijar IP conservando nombre utiliza `curl --resolve`, con el certificado de confianza correcto; compara después con una petición **sin** ese argumento desde srv01 para comprobar su resolución real.

## 2. Matriz de incidencias

| Síntoma | Causa probable | Comprobación | Resolución que conserva el diseño |
| --- | --- | --- | --- |
| Nombre inexistente | DNS o hosts incorrectos | `getent hosts` en servidor y cliente | Corregir resolución, no cambiar URLs al azar |
| Conexión rechazada | Sin listener o IP/puerto incorrectos | `ss`, estado y dirección local | Arrancar/configurar el servicio previsto |
| Tiempo agotado | Ruta o filtrado | Ruta y reglas del gestor de firewall | Permitir sólo el tráfico necesario |
| Certificado no válido | Confianza, SAN o fecha | Emisor, SAN, reloj y cadena | Corregir certificado/confianza; no omitir validación |
| Navegador funciona pero WordPress falla en loopback TLS | HTTP API usa otro bundle CA | Probar HTTP API y revisar mu-plugin/almacén Debian | Aplicar la CA al host LAB con `sslcertificates`, manteniendo `sslverify=true` |
| Siguen listeners wildcard tras activar el CMS | Sitio predeterminado u otro bloque activo | `nginx -T`, `sites-enabled` y `ss` | Retirar sólo el enlace estándar del clon con copia; revisar los demás bloques |
| 403 en archivos estáticos | Permiso o regla | Logs y permisos de toda la ruta | Dar lectura/traversal al usuario previsto |
| 404 en entradas | Reescritura o ruta | `try_files`, configuración y enlaces | Ajustar el servidor virtual y URL correcta |
| 502 al ejecutar PHP | FPM caído o socket equivocado | Servicio, socket y permisos | Restaurar backend y ruta correcta |
| Error de conexión SQL | Identidad, host o base | Conexión local con usuario de aplicación | Corregir credencial/host sin privilegios globales |
| Pantalla de error tras cambio | Núcleo/tema/plugin incompatible | Versión y log PHP de pruebas | Revertir conjunto compatible o corregir extensión |
| No se pueden subir imágenes | Permisos o límite | Carpeta, PHP y tamaño de petición | Ajustar sólo subidas y límites coherentes |
| Actualizar desde panel no funciona | Política de despliegue | Constantes y propietario del código | Usar el mantenimiento controlado documentado |
| Redirección infinita | URL o esquema incoherente | Cadena de Location y configuración | Unificar URL/esquema y proxy confiado |
| Tras restaurar faltan medios | Copia incompleta | Archivos de uploads y referencias SQL | Recuperar archivos del mismo punto de copia |

No modifiques simultáneamente permisos, URL y configuración de PHP. Realiza un cambio que corresponda a una hipótesis, repite la prueba y documenta resultado. Si no mejora, revierte antes de probar otra causa salvo que el cambio sea necesario y esté justificado.

## 3. Espacio, registros y recursos

Un disco lleno puede impedir sesiones, subidas, temporales y escrituras SQL. Comprueba `df -h` y, si hay espacio aparente pero siguen fallando creaciones, revisa inodos con `df -i`. No borres registros ni bases a ciegas. Identifica qué ocupa espacio, conserva evidencia necesaria y aplica retención coherente.

Un límite de subida puede existir en Nginx, PHP y la propia aplicación. Aumentar sólo `client_max_body_size` no modifica `upload_max_filesize` ni `post_max_size`. El tamaño del cuerpo puede incluir más que el archivo; establece límites relacionados y comprueba el FPM efectivo, no únicamente la CLI. No incrementes todos los límites a valores enormes para evitar diagnosticar la petición.

La lentitud puede pertenecer a DNS, TLS, backend, SQL, contenido externo o cliente. Registra tiempos y compara una página estática con una dinámica. Si la estática responde rápido y la dinámica tarda, enfoca aplicación y dependencias; no concluyas automáticamente que la red está bien en todos sus aspectos. Una prueba aislada no representa la carga de muchas personas.

## 4. Preguntas resueltas

**1. ¿Recibir 200 significa que la aplicación funciona?** Significa que esa petición se atendió con éxito según la semántica del servidor. Pueden fallar imágenes, llamadas de API o acciones posteriores; también puede devolverse una página de error con estado incorrectamente 200. Comprueba contenido y recorrido funcional.

**2. ¿Por qué HTTPS no sustituye la seguridad de WordPress?** Protege el canal y autentica el extremo según el certificado. Un complemento vulnerable o un administrador con contraseña comprometida sigue pudiendo permitir cambios indebidos. Se necesitan controles en cada capa.

**3. ¿Por qué no se publica la clave privada de la CA?** Permitiría emitir certificados que los clientes confiados podrían aceptar. Para distribuir confianza sólo hace falta el certificado público. La clave del servidor también debe permanecer privada y con acceso mínimo.

**4. ¿Por qué el CMS no necesita MariaDB abierta a toda la red?** En este diseño PHP y MariaDB comparten servidor y se comunican localmente. Exponer 3306 añade acceso innecesario. Una arquitectura distribuida requeriría otras reglas y autenticación explícita, no una apertura general.

**5. ¿Por qué `nginx -t` puede pasar aunque el sitio devuelva 502?** Comprueba sintaxis y recursos que Nginx necesita al cargar configuración, pero no garantiza que el backend atienda peticiones. El socket FPM puede no existir al acceder o el servicio puede estar caído.

**6. ¿Es suficiente copiar `wp-content`?** No. Allí residen temas, extensiones y medios, pero entradas, usuarios y opciones se guardan principalmente en la base. Además necesitas configuración e inventario compatibles. La estrategia debe recuperar el servicio completo.

**7. ¿Se puede cambiar de dominio reemplazando todas las cadenas del SQL con un editor?** Puede corromper datos serializados cuyo formato incluye longitudes. Utiliza procedimientos y herramientas conscientes del formato y conserva copia antes de modificar. Prueba la migración en entorno separado.

**8. ¿Ocultar «Administración» en el menú evita que un editor administre el sitio?** No. El servidor debe comprobar capacidades en cada operación. Un enlace oculto no impide solicitar su URL o endpoint directamente.

**9. ¿La opción de disuadir buscadores protege un sitio?** No. Es una preferencia para indexadores cooperativos. La confidencialidad depende de autenticación, permisos y controles de red según el caso.

**10. ¿Una herramienta automática puede certificar por sí sola accesibilidad?** No. Detecta determinadas condiciones, pero muchas decisiones necesitan revisión humana: sentido del texto alternativo, orden de lectura, instrucciones y funcionamiento por teclado. Documenta alcance y limitaciones de cada comprobación.

**11. ¿Por qué se actualiza primero en pruebas?** Porque un cambio puede alterar esquema, permisos o compatibilidad. Un entorno separado permite ensayar aceptación y reversión antes de comprometer disponibilidad. Debe parecerse lo suficiente al principal para que la prueba aporte evidencia.

**12. ¿Qué demuestra una restauración?** Que un conjunto concreto de artefactos, herramientas y pasos permitió recuperar funciones verificadas en condiciones definidas. No demuestra que cualquier copia histórica sea válida ni que el tiempo sea igual bajo otra carga o hardware.

**13. ¿Por qué confiar en la CA en el navegador no basta para WordPress?** El navegador, el almacén del sistema y la HTTP API pueden utilizar almacenes distintos. La guía instala la CA pública en Debian y selecciona ese bundle únicamente para el host HTTPS del clon mediante un mu-plugin. Así conserva validación de certificado y nombre sin editar el bundle del núcleo ni desactivar TLS.

## 5. Evidencia final de autonomía

Prepara un expediente sin secretos: arquitectura, inventario, configuración depurada, matriz de roles, pruebas de HTTP/TLS, registro de cambio y restauración. Otra persona debería poder repetir la instalación con sus propias credenciales y reconocer los puntos dependientes de versión.

Distingue siempre «esperado», «observado» y «pendiente». La documentación deja de ser fiable cuando una prueba prevista se presenta como si ya hubiera ocurrido. Un resultado limitado y bien registrado aporta más valor que una declaración general de funcionamiento sin recorrido reproducible.
