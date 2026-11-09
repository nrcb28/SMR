# 8. Laboratorios avanzados y casos resueltos de administración

[Índice del módulo](README.md) · [Directorio y GPO](05-directorio-identidades-y-gpo.md) · [Linux y capacidad](06-linux-permisos-y-capacidad.md) · [Operación y recuperación](07-operacion-automatizacion-y-recuperacion.md)

Las actividades amplían las prácticas iniciales mediante requisitos más precisos, errores reversibles y decisiones justificadas. Las duraciones son orientaciones de estudio y las rúbricas son propias del repositorio. Usa datos sintéticos y registra resultados realmente observados. Antes de empezar confirma la consola, el estado del laboratorio y el punto de recuperación; ninguna prueba requiere una infraestructura ajena.

## L4. Ciclo completo de identidades y permisos

### Enunciado y estado inicial

Una oficina ficticia necesita mantener manuales de soporte. Hay dos personas editoras, una lectora y una incorporación pendiente. La persona lectora pasará temporalmente a edición y después deberá volver a su función. Se exige poder explicar el acceso mediante grupos, sin permisos directos sobre los archivos para cada persona.

Elige uno de los escenarios ya construidos: recurso Samba independiente con identidades locales o servidor de archivos Windows del laboratorio. No mezcles ambos modelos dentro de una única prueba sin documentar cómo se mapean las identidades. El dominio, si se utiliza, es `ad.aula.test`, y los clientes consultan DNS del DC. Prepara un árbol nuevo con dos archivos de texto y una subcarpeta, sin reutilizar datos de ejercicios anteriores.

### Diseño y ejecución

1. Escribe la matriz persona–función–permiso. Separa grupo funcional y grupo de recurso cuando el escenario AD lo permita.
2. Guarda identidad estable, grupos iniciales y ACL. En Linux conserva rutas absolutas al exportar ACL; en Windows registra SID y pertenencias relevantes.
3. Crea el recurso con lectura y edición definidas. Explica la herencia elegida para los archivos nuevos.
4. Desde sesiones nuevas, realiza lectura por ambos roles, edición por editores y denegación de escritura por lector.
5. Simula el cambio de función añadiendo a la persona lectora al grupo previsto, sin otorgar permisos directos.
6. Compara una sesión existente y una nueva. Registra si el cambio se refleja y qué token o conexión se utiliza.
7. Retira la pertenencia temporal y verifica de nuevo el acceso desde una sesión controlada.
8. Deshabilita la incorporación pendiente sin borrar datos ni otros objetos. Documenta qué acceso tenía antes de deshabilitarse y qué queda pendiente de revisar.

### Solución razonada y criterios

El diseño correcto permite modificar pertenencias sin tocar cada archivo. Si la persona lectora conserva acceso después de retirarla del grupo, investiga sesiones y permisos alternativos antes de repetir la baja. Puede existir otro grupo anidado, una entrada explícita, una conexión autenticada con otra cuenta o una sesión cuyo contexto no se ha renovado. La explicación debe indicar cuál de esas posibilidades se comprobó.

La denegación de escritura debe incluir creación de un archivo nuevo y modificación del existente. Una aplicación puede necesitar renombrar o borrar un temporal; si sólo se prueba `echo` sobre un archivo se puede pasar por alto ese comportamiento. Utiliza una operación de cliente comparable a la que exige el enunciado y documenta las diferencias.

**Entregables:** matriz inicial/final, exportación sanitizada de grupos y ACL, cuatro pruebas positivas/negativas, cambio temporal, retirada y explicación de sesiones. **Rúbrica didáctica:** diseño de grupos 25 %, permisos efectivos 30 %, ciclo de cambio/baja 25 % y evidencia reproducible 20 %. Una captura de una lista de grupos no sustituye a una prueba de operación.

## L5. GPO de aula y resolución de un fallo de ámbito

### Enunciado

Un aula ficticia necesita una configuración visible de usuario sólo en un equipo compartido. La misma persona debe conservar su configuración normal al utilizar otro equipo. Se quiere estudiar la diferencia entre ámbito de usuario, ámbito de equipo y procesamiento loopback. No se bloquearán herramientas administrativas ni se modificará la GPO predeterminada del dominio.

Si no dispones de memoria para un segundo cliente, usa dos estados documentados de un cliente y deja claro que no se ha probado concurrencia. Prepara OU de laboratorio separadas y una cuenta sintética. Conserva el vínculo y ajuste iniciales de cualquier GPO implicada. Selecciona un ajuste cosmético reversible cuya disponibilidad esté documentada para la edición del cliente.

### Procedimiento

1. Dibuja la ubicación del usuario y de cada equipo. Identifica qué sección de GPO contiene el ajuste.
2. Crea una GPO exclusiva y vincúlala al ámbito de usuario. Actualiza según corresponda y recoge `gpresult`.
3. Conserva el informe, retira sólo el vínculo de prueba y vincula la GPO a la OU del equipo sin habilitar loopback.
4. Formula el resultado esperado antes de iniciar sesión: un ajuste de usuario no se aplica automáticamente por la ubicación del objeto de equipo.
5. Configura un escenario de loopback de laboratorio de acuerdo con la documentación. Prueba el modo elegido, registra qué conjunto de directivas resulta y explica por qué.
6. Introduce un fallo reversible de ámbito, como mover la cuenta de equipo de prueba a una OU distinta prevista para este ensayo. No alteres objetos ajenos.
7. Diagnostica utilizando informe y ubicación; corrige una variable, repite la prueba y guarda evidencia.
8. Restituye objetos y vínculos, dejando las GPO del centro sin cambios.

### Discusión de resultados

Si el informe indica que la GPO no está dentro del ámbito, un `gpupdate /force` no repara la ubicación. Si la GPO aparece pero el ajuste no cambia, examina precedencia, extensión, necesidad de sesión nueva y compatibilidad del ajuste. Si el resultado difiere entre clientes, compara su ubicación y procesamiento antes de atribuirlo al usuario.

Una solución completa explica también cuándo **no** se necesita loopback. Para imponer una configuración a una persona en cualquier equipo, el ámbito de usuario adecuado puede ser suficiente. Añadir loopback a todo el dominio para corregir una práctica pequeña ampliaría el efecto sin justificación.

**Entregables:** diagrama, hipótesis de cada etapa, informes sanitizados, vínculo inicial/final y tabla de precedencia. **Rúbrica:** comprensión de ámbito 30 %, aplicación y diagnóstico 35 %, reversión 20 % y claridad 15 %. Se evalúa el razonamiento, no la cantidad de GPO creadas.

## L6. Recuperación de un servicio con metadatos

### Enunciado

Se dispone de un recurso de archivos con 24 documentos sintéticos distribuidos en tres carpetas. Dos roles tienen accesos distintos. Debes producir una copia independiente, restaurarla a otra ruta y demostrar que el servicio conserva contenido y autorización. El objetivo de recuperación será de 40 minutos y la pérdida admisible de datos, 24 horas; ambos son supuestos didácticos.

No se borrará el original para demostrar que la copia existe. Prepara un destino separado y comprueba su montaje y espacio. Si trabajas con un solo volumen virtual, declara que la prueba muestra el procedimiento de restauración pero no protege frente a la pérdida del volumen. Una instantánea no convierte ese destino en independiente.

### Desarrollo

1. Genera los documentos con nombres y contenidos conocidos. Registra tamaño, hash y permisos de un conjunto representativo.
2. Identifica la herramienta de copia y las opciones que conservan ACL, propietarios y atributos pertinentes.
3. Crea la copia, registra fecha y verifica su catálogo o contenido.
4. Introduce después dos modificaciones sintéticas en el origen y anota sus horas. No las incluyas en la copia anterior.
5. Restaura a una ruta nueva. Explica por qué esos dos cambios quedan fuera del punto recuperado y calcula el intervalo de pérdida.
6. Publica temporalmente el árbol restaurado como un recurso de laboratorio distinto, con configuración mínima y autorizada.
7. Comprueba archivos, metadatos, lectura por lector, escritura por editor y rechazo de otras cuentas.
8. Mide por fases identificación, preparación, transferencia, validación y habilitación. No confundas duración de copia con RTO completo.
9. Retira el recurso temporal sin borrar la única copia conservada y registra qué información se mantendrá para revisión.

### Solución y valoración

Si los hashes coinciden pero cualquier persona puede editar, la restauración no cumple el requisito. Si se conservan ACL numéricas pero los UID/GID se resuelven a otras cuentas, tampoco. La aceptación exige coherencia entre identidad, metadatos y operación del cliente.

Un tiempo real de 28 minutos cumple el objetivo de 40 bajo la carga del ensayo, pero no demuestra que se cumpla con un volumen diez veces mayor. Si la transferencia tarda 16 minutos y la preparación/validación otros 12, duplicar el caudal sólo mejora la parte transferible. Conserva el desglose para justificar inversiones.

**Entregables:** plan, inventario, catálogo de copia, comparación de contenido y autorización, línea temporal y evaluación RPO/RTO. **Rúbrica:** coherencia de copia 25 %, restauración 30 %, pruebas funcionales 25 % y medición/explicación 20 %.

## Ocho problemas adicionales con respuesta explicada

### 1. Permiso del recurso y NTFS

Un grupo tiene cambio en el recurso SMB y sólo lectura en NTFS. ¿Puede guardar un documento? La operación necesita superar ambos controles; el permiso más amplio de una capa no elimina una denegación de la otra. Revisa el permiso efectivo del usuario en su contexto y las entradas heredadas/expresas. La respuesta se demuestra desde cliente; una prueba local como administrador no reproduce la situación.

### 2. Directorio padre sin recorrido

Un archivo Linux permite lectura al grupo soporte, pero `/srv/privado` no permite atravesarlo. ¿Por qué `cat` falla? La resolución de la ruta requiere permisos en los directorios padre, independientemente del archivo final. `namei -l` ayuda a localizar el bloqueo. Conceder lectura al archivo otra vez no cambia la imposibilidad de atravesar el padre.

### 3. Espacio libre aparente

`df -h` muestra capacidad disponible y una aplicación informa de que no puede crear archivos. Propón tres comprobaciones. Consulta inodos, cuotas del principal y permisos/límites de la ruta real. Comprueba también que la aplicación escribe en el montaje que supones. No concluyas que el disco físico está averiado por un único mensaje traducido por la aplicación.

### 4. UID en una migración

El origen atribuye un directorio a UID 1205 y el destino asigna ese número a otra persona. ¿Qué riesgo tiene copiar conservando números? El destino interpretará la propiedad según su propio catálogo de identidades. Se necesita coherencia o un mapeo controlado antes de habilitar el servicio. Cambiar recursivamente propietario sin inventario puede asignar datos de otros usuarios de forma incorrecta.

### 5. Baja y credenciales en caché

Una cuenta deshabilitada en AD sigue permitiendo abrir un escritorio sin conexión. ¿Demuestra que el DC ignora la baja? No necesariamente: el cliente puede utilizar información de inicio de sesión en caché y no contactar al dominio. Distingue acceso local, ticket, conexión existente y nueva autenticación en línea. Las políticas de continuidad y revocación deben contemplar cada caso.

### 6. Cuenta con nombre repetido

Se borra `alba.lab`, se crea otra cuenta igual y una ACL antigua deja de resolver el nombre. ¿Debe el servidor reutilizar el permiso por el texto? No: la identidad estable cambió. Reconstruye la autorización usando grupos y SIDs correctos, revisando la propiedad de los datos. El nombre no es una prueba de identidad.

### 7. Automatización con error parcial

Un lote crea cuatro objetos y falla en el quinto. ¿Es correcto volver a ejecutarlo entero? Sólo si el diseño contempla estado previo y repetición segura. Primero enumera objetos creados, causas del fallo y resultados de validación. Una segunda ejecución sin controles puede duplicar grupos o aplicar atributos a cuentas equivocadas. Un plan con entradas verificadas reduce errores antes de la fase de cambios.

### 8. Restauración de dominio

Un estudiante conserva únicamente la instantánea de una VM DC y cree que ya tiene recuperación del bosque. ¿Qué falta? Identificar un procedimiento compatible con AD, copia coherente, estado y claves de recuperación, dependencias y prueba aislada. Con varios controladores hay además decisiones de replicación y autoridad de datos. La existencia de una instantánea no responde por sí sola a ese conjunto de requisitos.

## Lista de preparación para una evaluación práctica

Antes de empezar, localiza consola, versiones, identidades, DNS y copia previa. Durante la prueba registra una hipótesis antes de cambiar algo y evita ampliar permisos para ocultar un fallo. Reserva tiempo para el cliente y un caso negativo. Al entregar, separa hechos observados, supuestos y decisiones pendientes.

Un informe avanzado permite a otra persona reconstruir el servicio, repetir la prueba y reconocer qué no se ha validado. Si no has ejecutado una operación, explica el procedimiento previsto sin presentarlo como resultado conseguido. Esa precisión forma parte del trabajo técnico.

## Referencias primarias

- [Microsoft: documentación de Active Directory Domain Services](https://learn.microsoft.com/windows-server/identity/ad-ds/).
- [Microsoft: procesamiento de directiva de grupo](https://learn.microsoft.com/windows-server/identity/ad-ds/manage/group-policy/group-policy-processing).
- [Microsoft: guía de recuperación del bosque](https://learn.microsoft.com/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-procedures).
- [Samba: documentación oficial](https://www.samba.org/samba/docs/).
- [Debian Reference](https://www.debian.org/doc/manuals/debian-reference/).
