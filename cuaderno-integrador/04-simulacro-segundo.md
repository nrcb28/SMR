# Simulacro práctico de segundo: servicio, identidad y recuperación

[Cuaderno](README.md) · [Segundo](../segundo/README.md) · [Proyecto](../segundo/proyecto-intermodular/README.md)

## 1. Escenario y restricciones

Una organización ficticia necesita un servicio de documentación, acceso administrativo protegido, archivos por grupos y un procedimiento de recuperación. La actividad integra Servicios en red, Sistemas en red, Seguridad, Aplicaciones web, Inglés e IPE II. Se propone realizarla en cuatro sesiones, con instalación de paquetes preparada si el objetivo es evaluar configuración y operación.

Es un simulacro didáctico propio. El centro determina la evaluación oficial y qué herramientas se utilizan. No se pide abrir servicios a Internet ni contratar nube. Trabaja en un clon aislado con las funciones y direcciones del [laboratorio](../docs/laboratorio.md): servidor Debian `srv01` `.56.10/24`, cliente `.56.20/24`, dominio de servicios `aula.test`, NIC LAB identificada y NAT separada cuando se necesite.

El escenario base usa DNS BIND y Samba independiente. La variante AD se ejecuta por separado con `dc01` `.56.11`, DNS del directorio y `ad.aula.test`; no se sustituye inadvertidamente BIND por el DNS de un controlador en la misma dirección. El servidor web se limita a la interfaz LAB y se inspeccionan los otros sitios activos de Nginx.

## 2. Requisitos verificables

| ID | Requisito | Evidencia mínima |
| --- | --- | --- |
| R01 | Resolver nombres del laboratorio mediante su DNS | Consulta dirigida y resolución normal desde cliente |
| R02 | Distinguir nombre inexistente y tipo de registro ausente | Dos consultas con explicación de estado y respuesta |
| R03 | Administrar por SSH verificando identidad del servidor | Fingerprint contrastada y autenticación válida |
| R04 | Ofrecer web HTTPS con nombre y confianza correctos | Respuesta desde cliente sin omitir validación TLS |
| R05 | Autorizar archivos por grupos | Lectura, escritura y denegación probadas con identidades distintas |
| R06 | Restaurar un conjunto de datos y comprobarlo | Recuperación a otra ruta, integridad y permisos |
| R07 | Medir RPO y recuperación frente al objetivo | Línea temporal, punto recuperable y tiempos comparados |
| R08 | Entregar documentación de operación y cambio | Configuración sanitizada, runbook y matriz de pruebas |
| R09 | Comunicar un incidente en inglés | Mensaje claro con impacto, estado y siguiente actualización |

La tabla contiene objetivos, no resultados ejecutados. Completa [la matriz de ejemplo](datos/matriz-aceptacion-segundo.csv) con tus observaciones; sus columnas de resultado y evidencia están vacías deliberadamente.

## 3. Parte A: DNS y alcance de la resolución

Prepara una zona directa de `aula.test` y su inversa para las direcciones realmente utilizadas. Deben existir nombres para el servidor y la web, con dirección `.10`. Puedes usar un alias para la web si lo justificas y respetas las reglas de DNS. No publiques registros de equipos que no existan en tu topología.

Antes de cargar la zona valida la configuración y el archivo con las herramientas de BIND de la guía. Documenta número de serie y qué cambio lo actualiza. Comprueba desde el cliente un A conocido, un PTR y un nombre deliberadamente inexistente. Para un nombre existente que sólo tenga A, consulta AAAA y explica su diferencia con el nombre inexistente.

Si BIND actúa sólo como autoritativo sin recursión, no lo evalúes como si debiera resolver cualquier dominio externo. La resolución de paquetes por NAT y la resolución de la zona LAB deben estar diseñadas. Documenta qué resolutor recibe cada consulta; no «arregles» el escenario añadiendo servidores públicos sin explicar su selección.

## 4. Parte B: acceso remoto y HTTPS

Prepara SSH con una cuenta de administración de laboratorio y una política compatible con el ejercicio. Contrasta la clave pública de host desde la consola de la VM con la huella que ve el cliente. No aceptes una clave nueva a ciegas ni desactives la comprobación para eliminar un mensaje.

Para HTTPS utiliza una CA exclusiva de prácticas con el certificado público instalado en el cliente apropiado. El certificado del servidor debe incluir el nombre que realmente se utiliza. Conserva claves privadas fuera del repositorio y limita su lectura según el servicio. Registra emisor, nombre, vigencia y forma de retirar confianza al terminar.

Una prueba con `curl --cacert` debe validar TLS y obtener respuesta HTTP. Si utilizas `--resolve` para aislar un fallo, repite después la consulta normal sin esa opción. Una respuesta 404 puede mostrar que el servidor y TLS funcionan pero que la ruta no existe; no satisface por sí sola el requisito de contenido correcto.

En un clon dedicado comprueba que el sitio predeterminado de Nginx no conserve listeners wildcard fuera de LAB. `nginx -t` no sustituye comprobar puertos efectivos ni realizar una petición desde cliente. Para un CMS con peticiones internas revisa además resolución del servidor y confianza de su propia biblioteca HTTP, como se explica en [Aplicaciones web](../segundo/aplicaciones-web/README.md).

## 5. Parte C: archivos y autorización

Diseña una matriz con un grupo lector, un grupo editor y una cuenta ajena. Relaciona cuenta, pertenencia, operación y resultado esperado. La autenticación correcta de una cuenta ajena no implica que deba recibir permiso sobre el recurso.

En Samba independiente documenta cómo se relacionan cuentas Samba e identidades UNIX, permisos del recurso y sistema de archivos. En la variante Windows/AD utiliza el esquema de grupos del módulo y muestra cómo los permisos del recurso y NTFS afectan al resultado. Una variante no tiene por qué usar exactamente los mismos comandos para satisfacer el requisito.

Prueba con archivos nuevos de contenido ficticio: listar, leer, crear, modificar y, si lo exige tu diseño, borrar. El permiso de borrar puede depender del directorio o de mecanismos distintos a la escritura del contenido; explica la operación que estás comprobando. No agrupes todas las acciones bajo la frase «tiene acceso».

Si cambias grupos, considera sesiones y tokens. Una prueba con credenciales almacenadas puede utilizar una identidad distinta de la que creías. Cierra únicamente la conexión de laboratorio necesaria y establece una sesión nueva según el sistema, preservando otras conexiones del usuario.

## 6. Parte D: recuperación y cronología

Define un conjunto pequeño de archivos y, en una variante CMS, datos y configuración consistentes. Crea una copia mediante el mecanismo documentado y restaura en un destino distinto. Un backup no se acepta únicamente por tener un archivo de tamaño distinto de cero.

Usa estos objetivos didácticos para analizar la cronología: RPO máximo de 30 minutos y recuperación del servicio en 30 minutos desde la detección. Se facilitan los siguientes **datos sintéticos de un incidente**, independientes del tiempo que tarde tu práctica:

| Evento | Hora UTC del escenario |
| --- | --- |
| Último punto de datos recuperable | 09:15 |
| Detección del incidente y servicio no disponible | 10:00 |
| Inicio de investigación | 10:04 |
| Inicio de restauración | 10:12 |
| Datos restaurados en destino | 10:23 |
| Validación y servicio aceptado | 10:29 |

Calcula pérdida potencial, tiempo de copia de datos, intervalo de restauración y recuperación total. Determina qué objetivo se cumple y cuál no. Después plantea una medida que mejore el objetivo incumplido sin confundir frecuencia nominal de tarea con punto realmente recuperable.

En tu ensayo real registra tus propios tiempos y mantenlos separados de la tabla. Si no existe una aplicación o equipo para ejecutar una parte, márcala pendiente y explica su prueba; no rellenes esa ausencia copiando los datos del escenario.

## 7. Solución razonada: pruebas de nombres

Un A conocido debe devolver el destino configurado. Un PTR correcto relaciona la IP con el nombre previsto en la zona inversa; no se crea automáticamente por existir el A. La respuesta se interpreta con estado, secciones y autoridad. Puedes consultar con `dig @192.168.56.10 srv01.aula.test A` desde el cliente preparado.

Para un nombre existente con A y sin AAAA, una zona normal puede responder `NOERROR` sin respuesta AAAA, conocida como ausencia de datos para ese tipo. Para un nombre que no existe en la zona y no está cubierto por otras reglas, se espera `NXDOMAIN`. Debes controlar los datos de tu zona y la existencia de comodines para que la expectativa sea válida.

Una consulta dirigida a `.10` correcta no demuestra que el sistema la use de forma habitual. Consulta el nombre mediante el resolutor normal y revisa su configuración. Si hay un archivo hosts, no lo uses como evidencia de que BIND está funcionando: es otro mecanismo que puede resolver el mismo nombre.

La resolución de un servicio del directorio usa registros y DNS del dominio. En la variante AD, una consulta a un DNS público no sustituye descubrimiento de controladores. Se documenta el escenario elegido para que el evaluador no atribuya a BIND la función de DNS interno del directorio.

## 8. Solución razonada: transporte, confianza y aplicación

La secuencia útil es observar ruta, conexión al puerto, negociación TLS, respuesta HTTP y contenido. Si TCP falla, un cambio en el tema de WordPress no aborda la evidencia. Si TLS falla por nombre, revisa SAN y URL; si falla por confianza, revisa emisor, cadena y almacén utilizado. No se acepta `-k` como sustituto de una solución de confianza.

La identidad SSH se contrasta por un canal independiente, por ejemplo consola de la VM. Cuando una VM se reinstala puede cambiar legítimamente la clave, pero primero hay que comprobar que ésa es la explicación. El procedimiento debe preservar la protección contra un destino equivocado, no enseñar a borrar todo el archivo de hosts conocidos ante cualquier aviso.

Para aceptar web, el cliente abre el nombre correcto, valida certificado y recibe la página esperada. Para aceptar edición CMS se necesita además una cuenta de rol adecuado y una operación editorial. Un lector anónimo no debe poder ejercer funciones de administración.

Los listeners en `.56.10` y un firewall coherente son evidencias de alcance, pero la red virtual también importa. Una VM en modo puente puede tener exposición distinta de una host-only. Comprueba hipervisor, NIC y servicio; el nombre del modo en una captura antigua no demuestra su estado actual.

## 9. Solución razonada: autorización efectiva

La matriz se valida desde el cliente y con identidades separadas. Una cuenta editora escribe, la lectora sólo lee y la ajena recibe denegación. Registra qué archivo, qué operación, qué sesión y qué resultado. Si se añade un permiso directo de emergencia, se documenta y se retira después de restablecer el diseño por grupos.

Para explicar un fallo, separa localización del recurso, autenticación y autorización. Un usuario puede autenticarse y no estar en un grupo autorizado; el recurso puede permitir escritura y el directorio denegarla; un archivo heredado puede conservar permisos distintos de otros nuevos. Las pruebas deben abarcar ese tipo de diferencia cuando sea relevante.

Una salida de `id`, `whoami` o una herramienta equivalente muestra un contexto concreto; no todos los servicios comparten automáticamente el mismo token o sesiones. En Windows, considera la identidad de la conexión SMB y las políticas del dominio. En Linux, considera NSS, grupos y la cuenta bajo la que corre la operación.

La recuperación debe conservar o reconstruir también el esquema de permisos. Un archivo recuperado con el propietario equivocado puede pasar una comparación de hash y fallar confidencialidad o trabajo del usuario. El caso de copias del [capítulo de incidencias](02-incidencias-encadenadas.md) desarrolla esa distinción.

## 10. Solución numérica de recuperación

Desde 09:15 a 10:00 hay 45 minutos. Ésa es la ventana de pérdida potencial del escenario si no hay otro mecanismo de recuperación. Excede el objetivo de 30 minutos. No se sabe cuántas operaciones concretas se perdieron sin más datos; se conoce la distancia al punto recuperable.

La fase desde inicio de restauración a datos restaurados tarda once minutos, de 10:12 a 10:23. La validación añade seis minutos. Desde la detección al servicio aceptado pasan 29 minutos, por lo que se cumple el objetivo de recuperación de 30 minutos tal como se definió para este caso.

Si alguien presenta sólo once minutos como RTO observado, está excluyendo preparación y validación del límite declarado. Puede informar ese tiempo como duración de la fase de datos, pero debe conservar también el intervalo extremo a extremo. Si la definición del servicio incluye otras fases, hay que incorporarlas y revisar el resultado.

Para mejorar el RPO, estudia frecuencia y éxito de copias, registros de transacciones u otro mecanismo compatible. Una copia cada treinta minutos puede fallar y dejar un punto más antiguo; hacen falta supervisión y procedimientos. Para mejorar recuperación, ensaya preparación y verificación, no sólo ancho de banda.

**Prueba de continuidad completa:** copia coherente, identificación del punto, restauración en destino seguro, integridad, permisos, servicio desde cliente y registro temporal. Un ensayo que no llega al cliente deja pendiente una parte esencial del objetivo.

## 11. Comunicación en inglés: propuesta comentada

Escribe primero un aviso corto sin hipótesis presentadas como hechos. Un ejemplo sintético:

> The documentation service is currently unavailable in the lab. We detected the issue at 10:00 UTC and are checking the storage and application logs. Please avoid editing shared files until the service is confirmed as available. We will provide the next update at 10:15 UTC.

El texto identifica servicio, detección, acción y próxima actualización. No atribuye causa antes de comprobarla ni promete un tiempo de solución que no se conoce. La instrucción debe adecuarse al incidente real: en otro caso puede ser mejor conservar sesiones o registrar cambios en lugar de evitar toda edición.

Ejemplo de cierre del escenario:

> The service was restored and validated at 10:29 UTC. The latest recoverable data is from 09:15 UTC. Access permissions and a sample of restored files have been checked. Changes made after 09:15 may need to be recreated. We are reviewing the backup schedule and failure alerts to reduce the recovery gap.

El cierre diferencia recuperación del servicio y punto de datos. «May need» expresa la incertidumbre sobre cambios concretos sin ocultar la ventana potencial. No se comunica «no data loss» cuando los datos del caso no lo demuestran.

Añade después un ticket técnico con versión, alcance, pruebas y causa confirmada o pendiente. El mensaje a usuario no necesita todos los comandos; el ticket de operación sí debe permitir entender el cambio y el siguiente paso. Consulta [Inglés profesional](../segundo/ingles-profesional/README.md) para ampliar situaciones y vocabulario.

## 12. Evidencias de entrega y defensa

Entrega diagrama, tabla de roles/servicios, inventario de versiones, configuración sanitizada, matriz de permisos, matriz de aceptación y runbook de recuperación. Conserva las claves y contraseñas fuera del repositorio. Si debes demostrar que existe una clave, presenta su huella o la parte pública apropiada, no el material privado.

Durante la defensa, explica una prueba negativa y por qué es útil. Responde qué ocurriría si el DNS dejara de funcionar, si se cambiara un grupo o si la copia más reciente no fuera utilizable. Una respuesta sólida identifica dependencias y método de recuperación, sin inventar alta disponibilidad que no se haya diseñado.

Una mejora propuesta debe indicar problema, cambio, coste o esfuerzo, prueba y riesgo residual. «Añadir más seguridad» no es un plan. «Restringir el acceso administrativo a LAB y comprobar listeners y acceso desde orígenes previstos» sí identifica una medida y su validación.

## 13. Rúbrica propia y repetición

| Área | Peso orientativo | Para obtener una valoración alta |
| --- | ---: | --- |
| DNS y dependencias | 20 % | Consultas normales/dirigidas, negativos interpretados y roles separados |
| Identidades y permisos | 20 % | Grupos, sesiones y operaciones con resultados verificables |
| SSH y TLS | 15 % | Identidad y confianza comprobadas, alcance de escucha documentado |
| Recuperación | 20 % | Datos, permisos y servicio restaurados; RPO/RTO bien interpretados |
| Documentación y decisiones | 15 % | Otro operador puede seguir diseño, cambio y recuperación |
| Comunicación en inglés | 10 % | Impacto, estado, tiempos e incertidumbre expresados con claridad |

Para repetir, cambia el nombre del sitio o los grupos manteniendo coherencia, y modifica el punto recuperable para recalcular objetivos. No cambies direcciones, certificados y DNS por separado sin revisar dependencias. La finalidad es demostrar comprensión transferible, no reproducir una secuencia memorizada.
