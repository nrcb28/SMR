# 3. Prácticas de sistemas operativos en red

Estas prácticas desarrollan la [guía técnica](02-guia-tecnica.md). Los tiempos son orientativos y no sustituyen la programación del centro. Registra las salidas reales: los resultados indicados son criterios de aceptación, no una afirmación de que tu instalación los cumpla.

## P1. Recurso Samba con autorización demostrable

**Objetivo:** publicar un recurso de escritura para soporte sin conceder acceso a una cuenta ajena al grupo. **Duración orientativa:** dos sesiones de 90 minutos. **Requisitos:** `srv01` Debian 13 y un cliente LAB; cuentas de laboratorio, consola del hipervisor y espacio para una copia. No hace falta un dominio AD.

### Preparación y ejecución

1. Dibuja el flujo cliente → TCP 445 → autenticación Samba → identidad Unix → directorio. Anota dónde esperarías un rechazo por contraseña y dónde por permisos.
2. Confirma `192.168.56.10/24`, nombre de interfaz y ausencia de exposición a otra red. Guarda inventario con `ip -br address`, `ip route` y `ss -lntp`; no incluyas contraseñas.
3. Crea `soporte`, `ana` y `bruno` con los comandos de la guía. Ana pertenece a soporte; Bruno no. Comprueba con `id`. Las cuentas no tendrán shell interactiva.
4. Crea `/srv/samba/manuales`, grupo propietario, setgid y ACL de acceso y por defecto. Guarda `getfacl` y `namei -l`. Prueba desde Linux con `sudo -u` antes de instalar el recurso de red.
5. Haz copia de la configuración Samba. Introduce la configuración propuesta, adaptando la interfaz real. Crea las contraseñas Samba de forma interactiva. Ejecuta `testparm` y resuelve los errores antes de reiniciar `smbd`.
6. Comprueba que la escucha está restringida a LAB y loopback. Desde el cliente inicia una sesión como Ana, crea `informe.txt`, lee su contenido, modifica una línea y renómbralo. Registra cada resultado.
7. Cierra sólo la sesión SMB de ese recurso e inicia otra como Bruno. Prueba a listar y escribir. Debe denegarse. Conserva el mensaje exacto y el tramo de registro que ayude a distinguir autenticación de autorización.
8. Añade temporalmente Bruno a `soporte`, abre una sesión nueva y repite. Registra el cambio. Retíralo con `gpasswd -d bruno soporte`, vuelve a cerrar la conexión del recurso y comprueba que pierde acceso.

### Pruebas de aceptación

| Prueba | Resultado esperado | Evidencia mínima |
| --- | --- | --- |
| Cuenta Ana válida | Lectura y escritura | Archivo creado y propietario/grupo observados. |
| Bruno con contraseña válida pero sin grupo | Acceso denegado | Mensaje y pertenencia a grupos. |
| Contraseña errónea de Ana | Fallo de autenticación | Mensaje sin registrar la contraseña. |
| Anónimo | Acceso denegado | Prueba explícita sin credenciales guardadas. |
| Servicio reiniciado | Configuración conservada | `testparm`, estado y repetición de lectura. |
| Sesión SMB | Dialecto compatible y cifrado | Información de sesión del cliente cuando la herramienta lo permita. |

### Diagnóstico y recuperación

Si Ana tampoco puede escribir localmente, revisa ACL antes de Samba. Si la prueba local funciona pero la remota falla, revisa `valid users`, cuenta Samba, sesión guardada y configuración activa. Si no se abre la conexión TCP, empieza por enlace, IP, escucha y firewall. Un error de nombre no se resuelve alterando permisos.

Para deshacer el ejercicio, cierra conexiones, restaura el `smb.conf` guardado y valida con `testparm`; recarga o reinicia según corresponda. Conserva una copia de los datos antes de retirar el directorio. Las cuentas y grupos se eliminan sólo después de comprobar que no poseen otros archivos o servicios. Retirar una cuenta Samba no borra automáticamente la cuenta Unix.

### Entrega y valoración

Entrega diagrama, configuración sin secretos, ACL, matriz de acceso, cinco pruebas y un informe de una incidencia. Se considera logrado cuando puedes explicar tanto los accesos concedidos como los denegados. Una carpeta accesible a todos con `777` no cumple el objetivo aunque el archivo se transfiera.

## P2. Dominio Windows con DNS y GPO de laboratorio

**Objetivo:** unir un cliente al dominio y demostrar una política limitada a una OU. **Duración orientativa:** tres sesiones de 90 minutos. **Recursos:** `dc01` Windows Server 2025 y `cli01` Windows 11 Pro; consola, soporte de instalación legítimo y espacio de copia. Revisa la RAM requerida por ambas VM antes de arrancarlas simultáneamente.

### Preparación y ejecución

1. Crea un inventario de roles. `dc01` sólo tendrá AD DS y DNS para esta práctica. Desconecta su NIC NAT tras las actualizaciones. Documenta IP LAB `.11/24`, DNS propio y ausencia de gateway LAB.
2. Renombra el servidor, reinicia y valida conectividad local. Instala AD DS con herramientas y promueve `ad.aula.test`, NetBIOS `AULA`, mediante la guía. Guarda DSRM de forma privada y registra sólo que está custodiada.
3. Después del reinicio comprueba servicios, `Get-ADDomain`, `Get-ADForest`, consulta SRV y diagnóstico DNS. Anota advertencias con su interpretación en esta topología. No publiques registros completos con información ajena al laboratorio.
4. Crea `Laboratorio`, `Usuarios`, `Equipos` y `Grupos`, y una cuenta de alumno con cambio de contraseña en el primer inicio. No utilices esa cuenta para administrar el controlador.
5. Configura el cliente `.20/24` y DNS `.11`. Desde el cliente consulta el SRV del dominio, verifica hora y realiza la unión usando una cuenta autorizada. Reinicia y entra con el UPN del alumno.
6. Crea una GPO llamada `LAB_Desactivar_AutoPlay`, configúrala como directiva de equipo y vincúlala exclusivamente a la OU Equipos de Laboratorio. Confirma que el objeto de `cli01` está allí. No modifiques directivas del dominio completo.
7. Ejecuta `gpupdate` y genera `gpresult` de equipo con una consola elevada. Identifica la GPO y el ajuste. Si necesita reinicio o nuevo inicio de sesión, regístralo.
8. Desvincula temporalmente la GPO y analiza qué desaparece tras la actualización. Algunas configuraciones dejan valores persistentes: comprueba el comportamiento concreto y restaura la configuración mediante el método soportado, sin asumir que quitar un vínculo revierte todo.

### Comprobaciones y resultados

La conectividad por IP no demuestra que el dominio esté operativo. Deben funcionar la localización por SRV, la resolución del controlador, la unión, el inicio con identidad de dominio y la aplicación de la GPO. `whoami` debe mostrar el dominio esperado, no una cuenta local de igual nombre.

Como prueba negativa, deja de forma temporal el DNS del cliente apuntando a un servidor de laboratorio que no conozca AD; guarda el estado anterior y no cambies el controlador. Observa el fallo de consulta SRV y restablece `.11`. No hace falta forzar múltiples intentos de contraseña. Después repite la resolución y documenta que el problema era localización, no autorización.

### Reversión

Desvincula la GPO de prueba, conserva exportación o documentación y comprueba su efecto. Si se debe retirar el cliente del dominio, confirma antes una cuenta administradora local funcional y sus credenciales; usa la consola y no una sesión remota que pueda perderse. La despromoción de un controlador tiene un procedimiento específico: no borres su objeto como forma de apagar el dominio. En una práctica desechable puede eliminarse todo el conjunto de VM aisladas tras conservar entregables, sin reutilizar identidades en el dominio vivo.

### Entrega y valoración

Entrega diagrama, tabla IP/DNS, comprobación SRV desde el cliente, OU del equipo, identidad de inicio, informe GPO y causa/solución del fallo DNS. No incluyas contraseñas, volcados de credenciales o imágenes de discos completos en Git. La prueba está completa cuando otra persona puede seguir tu documentación sin necesitar tu memoria de los clics.

## P3. Grupos, ciclo de vida y restauración de un recurso

**Objetivo:** implementar una matriz de permisos con grupos y demostrar recuperación de datos y metadatos. **Duración orientativa:** dos sesiones de 90 minutos. **Requisitos:** P1 completada; para el bloque de AD, P2 y un recurso Windows de datos aislado. La copia de archivos no sustituye a una copia del directorio.

### Diseño previo

Define tres identidades ficticias: soporte, auditoría y usuario ajeno. Soporte necesita modificar manuales; auditoría, leer; el tercero no debe acceder. Expresa esa necesidad antes de crear ACL. Decide si la práctica de datos se realizará en Linux o Windows. Para AGDLP utiliza el escenario de dominio; para Linux utiliza grupos POSIX con ACL equivalentes, explicando que no son grupos AD.

### Ejecución

1. En AD crea grupos globales por función y grupos locales de dominio por permiso. Añade personas a los primeros y éstos a los segundos. No añadas usuarios directamente a la ACL como atajo.
2. Crea un recurso de datos nuevo. Revisa herencia y permisos del padre. Asigna modificación al grupo RW, lectura al grupo RO y conserva administración y SYSTEM donde corresponda. Establece la ACL SMB de acuerdo con el objetivo.
3. Registra los derechos efectivos y prueba crear, editar, leer y eliminar con cada cuenta. Cierra sesión cuando cambien grupos. Documenta cualquier entrada heredada que amplíe acceso y corrígela con copia previa de ACL.
4. En el recurso Linux de P1, crea tres archivos de contenido ficticio, uno de ellos en un subdirectorio. Guarda hashes con `sha256sum` y ACL con `getfacl -Rp`, conservando rutas absolutas para la restauración. Utiliza un destino independiente montado y verificado, no una carpeta que sólo parece pertenecer a otro disco.
5. Copia contenido con una herramienta que preserve propietarios, ACL y atributos necesarios. Puede utilizarse `rsync -aHAX --numeric-ids` con privilegios adecuados sobre sistemas de archivos compatibles. La barra final de origen significa copiar el contenido; revisa origen y destino. No añadas `--delete` a esta práctica.
6. Restaura en una ruta nueva como `/srv/restauracion-lab/manuales`, después de verificar espacio y permisos de ese árbol. Compara contenido, propietarios y ACL. Las ACL guardadas contienen rutas: adapta la comparación; no apliques una restauración de ACL sobre el origen por confundir los nombres.
7. Simula la baja de una identidad: deshabilita cuenta, retira grupos de acceso y cierra las sesiones de prueba. Conserva propiedad y datos de trabajo según el procedimiento definido. Comprueba que una nueva sesión ya no accede.
8. Cronometra desde la decisión de recuperar hasta que un usuario puede abrir el recurso restaurado. Separa tiempo de restauración de tiempo de validación. Compara el resultado con el RTO propuesto.

### Entrega y pruebas finales

Incluye matriz antes/después, diagrama AGDLP, ACL, comandos de copia con rutas anonimizadas, hashes y tabla de verificaciones. Debe quedar claro qué recupera la copia de datos y qué necesitaría el servidor completo: configuración, identidades, secretos, bases coherentes y servicio. Describe también la custodia de las claves si la copia está cifrada; una copia sin su clave recuperable no cumple el objetivo.

## Plantilla de evidencia común

```text
Práctica y versión de la guía:
Fecha, VM, sistema y versión de paquetes:
Objetivo y supuestos:
Estado previo y copia disponible:
Acción realizada:
Resultado esperado:
Resultado observado y evidencia mínima:
Diagnóstico si difiere:
Reversión aplicada y resultado:
Riesgos o dudas pendientes:
```

El informe debe explicar decisiones. Veinte capturas sin contexto no sustituyen una matriz de acceso, una prueba negativa o una restauración verificable.
