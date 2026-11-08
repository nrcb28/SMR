# 4. Diagnóstico y evaluación razonada

## 4.1 Orden de diagnóstico

Empieza por el síntoma reproducible: quién falla, desde dónde, a qué recurso, a qué hora y con qué mensaje exacto. «La red no funciona» mezcla demasiadas capas. Conserva el estado antes de modificarlo y cambia una variable por vez. Un fallo de credenciales no se arregla desactivando el firewall ni un fallo DNS concediendo permisos de administrador.

1. **Alcance:** confirma si afecta a una cuenta, equipo, recurso o a todos. Prueba un segundo caso autorizado que permita comparar.
2. **Red:** IP, máscara, interfaz activa y rutas. En LAB no inventes un gateway porque aparezca en otra guía.
3. **Nombres y tiempo:** consulta el resolver realmente configurado, A/AAAA/SRV y fuente de hora. Anota la diferencia entre resolver un nombre y localizar AD.
4. **Servicio:** estado, escucha, configuración efectiva y registro. Un proceso activo puede escuchar en la interfaz incorrecta.
5. **Identidad:** cuenta habilitada, ámbito local/dominio, autenticación válida y pertenencias vigentes en el token.
6. **Autorización:** permiso del recurso, ACL de archivos, directorios padre, herencia y máscaras efectivas.
7. **Integridad y capacidad:** espacio, sistema de archivos de sólo lectura, bloqueo del archivo, cuota y dependencias caídas.

No ejecutes todos los comandos de todas las capas sin criterio: plantea una hipótesis, selecciona una prueba que pueda refutarla y decide el siguiente paso a partir de lo observado.

## 4.2 Incidencias frecuentes

| Síntoma | Hipótesis que debes comprobar | Prueba útil | Corrección controlada |
| --- | --- | --- | --- |
| SMB acepta contraseña pero deniega el recurso | Falta grupo o ACL | `id`, `getfacl`, `testparm` y sesión nueva | Corregir el grupo o entrada concreta; repetir caso negativo. |
| Ana escribe localmente pero no por SMB | Restricción del recurso o sesión almacenada | `valid users`, cuenta Samba, registros y sesión | Ajustar sólo el control que niega el acceso previsto. |
| Nuevos archivos pierden escritura de grupo | Herencia o máscara inadecuada | `getfacl` de carpeta y archivo nuevo | Revisar ACL por defecto y máscara; no `777`. |
| Cliente no encuentra el dominio | DNS ajeno a AD | Consulta SRV y DNS efectivo | DNS del dominio; revisar NAT y métricas si hay varias NIC. |
| Unión correcta, inicio con cuenta inesperada | Se usa identidad local | `whoami /user` y pantalla de inicio | UPN o prefijo de dominio explícito. |
| GPO no aparece en resultados | Equipo fuera de OU o filtrado | `Get-ADComputer`, `gpresult`, vínculo y permisos | Mover el objeto o corregir el ámbito de la GPO de prueba. |
| Grupos correctos en AD, permiso no cambia | Token antiguo o sesión SMB persistente | Hora del inicio de sesión y grupos del token | Cerrar la sesión de prueba y volver a iniciar. |
| Error Kerberos y reloj desviado | Jerarquía temporal incorrecta | `w32tm /query /status` | Corregir la fuente y sincronizar con procedimiento soportado. |
| Servicio falla tras editar configuración | Sintaxis o parámetro no admitido | Validador y registros desde el momento del cambio | Recuperar copia o corregir línea; validar antes de recargar. |

## 4.3 Herramientas y significado

En Debian:

```bash
systemctl status smbd --no-pager
journalctl -u smbd --since '-15 min' --no-pager
sudo testparm -s
sudo smbstatus
namei -l /srv/samba/manuales/prueba.txt
getfacl /srv/samba/manuales/prueba.txt
df -hT /srv/samba/manuales
```

`smbstatus` requiere privilegios para mostrar toda la información y sus opciones varían con la versión. No publiques usuarios y equipos reales si examinas un servicio compartido. El diario puede no contener cada intento SMB: revisa también la ruta de registro definida en la configuración.

En Windows:

```powershell
Get-DnsClientServerAddress
Resolve-DnsName '_ldap._tcp.dc._msdcs.ad.aula.test' -Type SRV
Test-ComputerSecureChannel -Verbose
whoami /groups
Get-SmbConnection
gpresult /r
Get-WinEvent -LogName System -MaxEvents 30
```

`Test-ComputerSecureChannel` se utiliza en el cliente o servidor miembro y no como diagnóstico universal del controlador. No invoques su reparación automáticamente: primero demuestra la avería y confirma credenciales y conectividad. El registro System es sólo un punto de partida; AD DS, DNS, seguridad y GroupPolicy tienen registros específicos. Los eventos de auditoría dependen de que la política pertinente esté habilitada y de que existan SACL cuando son necesarias.

## 4.4 Preguntas con solución razonada

**1. ¿Basta con copiar `/etc/passwd` para migrar usuarios y archivos?** No. Hay identificadores, grupos, verificadores de contraseña, homes, ACL, atributos y bases de servicio. Copiar el archivo completo sobre otro sistema puede sobrescribir cuentas del propio sistema. La migración debe mapear identidades y preservar metadatos con un procedimiento planificado.

**2. ¿Por qué Bruno no accede aunque su contraseña Samba sea correcta?** La autenticación acredita identidad; `valid users` y el sistema de archivos aplican autorización. En la práctica Bruno no pertenece al grupo permitido. Hay que comprobar ambos controles antes de concluir cuál lo rechaza.

**3. ¿Una OU se puede utilizar directamente como grupo de una ACL?** No. Es un contenedor administrativo. Para permisos utiliza grupos de seguridad. Las OU son útiles para delegación y aplicación de políticas, pero no sustituyen las pertenencias de grupos.

**4. ¿Por qué un DNS público como alternativo puede romper AD?** No contiene los SRV privados que localizan controladores. Los clientes no lo interpretan como «sólo para Internet». La redundancia se obtiene con resolvers que conozcan el dominio, y éstos resuelven el resto mediante su diseño de reenvío o recursión.

**5. ¿Un grupo retirado deja de actuar al instante sobre todos los archivos abiertos?** No necesariamente. Existen tokens y sesiones ya autenticadas. Hay que considerar invalidación o cierre de sesiones conforme al procedimiento y probar una sesión nueva. Una baja urgente exige más que editar una lista de miembros.

**6. ¿La ACL del recurso SMB determina el acceso de una persona sentada en el servidor?** No. El acceso local usa los controles del sistema de archivos y del sistema. SMB añade sus controles al acceso remoto. Por eso se evalúan ambos caminos cuando existe esa posibilidad.

**7. ¿Dos controladores sustituyen las copias?** No. La replicación distribuye también borrados y cambios no deseados. Hace falta copia compatible con el directorio, custodia de credenciales y recuperación practicada en aislamiento.

**8. ¿Una GPO visible en el editor ya está aplicada?** No. Debe estar vinculada y dentro del ámbito, superar el filtrado y ser procesada por el destino. Se demuestra con resultados de directiva y comportamiento, no sólo con la existencia del objeto.

**9. ¿Reinstalar Ana con el mismo nombre recupera sus permisos Windows?** No por el nombre. La identidad nueva tiene otro SID. Se debe restaurar la identidad o reasignar permisos de forma deliberada, conservando trazabilidad y evitando apropiaciones indebidas.

**10. ¿Por qué se prueba también una denegación?** Una prueba positiva demuestra utilidad, pero no que el acceso esté limitado. El requisito de confidencialidad incluye que una identidad sin autorización no pueda operar. La matriz necesita ambos tipos de evidencia.

## 4.5 Rúbrica orientativa del repositorio

Esta ponderación es didáctica y puede adaptarse; no es la calificación oficial del centro.

| Criterio | Peso propuesto | Evidencia de logro |
| --- | --- | --- |
| Diseño y dependencias | 15 % | Roles, IP, DNS, hora y ámbitos de identidad explicados. |
| Configuración reproducible | 25 % | Procedimiento ordenado, validadores y supuestos de versión. |
| Autorización y mínimo privilegio | 25 % | Grupos, ACL y pruebas permitidas/denegadas sin permisos indiscriminados. |
| Diagnóstico y recuperación | 20 % | Hipótesis, prueba concluyente, corrección y restauración comprobada. |
| Documentación y custodia | 15 % | Evidencias legibles, secretos excluidos, estado final y limitaciones. |

Un servicio que expone datos fuera de LAB, guarda contraseñas en Git o sólo funciona concediendo privilegios generales debe corregirse antes de considerarlo terminado. Si una función no pudo comprobarse por recursos insuficientes, documéntala como pendiente; no presentes el resultado esperado como realizado.

## 4.6 Lista de cierre

- El inventario coincide con las interfaces y direcciones observadas.
- DNS y hora son coherentes con el dominio del escenario.
- Las cuentas de uso cotidiano no tienen privilegios de administración innecesarios.
- Hay una prueba de escritura autorizada, otra denegada y otra de autenticación inválida.
- La GPO de laboratorio tiene ámbito limitado y evidencia de aplicación.
- Existe copia independiente y al menos una restauración de datos verificada.
- El informe explica qué faltaría para producción: redundancia, gestión de secretos, monitorización y recuperación del directorio.

[Volver al índice del módulo](README.md)
