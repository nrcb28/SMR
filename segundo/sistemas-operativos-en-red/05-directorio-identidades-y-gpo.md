# 5. Directorio, identidad y directivas en profundidad

[Índice del módulo](README.md) · [Fundamentos](01-fundamentos.md) · [Laboratorio común](../../docs/laboratorio.md)

## 5.1 Qué almacena un directorio y qué debe resolver el administrador

Un directorio relaciona objetos e identificadores: personas usuarias, equipos, grupos, servicios y unidades organizativas. La información permite localizar un objeto y tomar decisiones, pero no convierte todas las operaciones en una única función. Consultar un atributo por LDAP, autenticar una sesión mediante Kerberos y autorizar escritura en un directorio son operaciones diferentes. Un fallo en una de ellas puede coexistir con éxito en las demás.

En el laboratorio Windows, el dominio `ad.aula.test` contiene objetos y políticas y `dc01` presta las funciones de controlador y DNS. El nombre de inicio de sesión, el nombre visible y el SID no son equivalentes. Renombrar una cuenta conserva normalmente su identidad de seguridad; borrarla y crear otra con el mismo nombre genera un SID distinto. Por ello un recurso puede mostrar una entrada de SID sin resolver y una cuenta nueva homónima seguir sin acceso. La solución se basa en reconstruir la asignación autorizada, no en asumir continuidad por semejanza del texto.

Antes de crear objetos, responde cuatro preguntas: qué función desempeñan, quién los mantiene, qué acceso necesitan y cómo se retiran. Una cuenta personal atribuible a su titular no se administra como una identidad de aplicación; una identidad de aplicación no necesita normalmente sesión interactiva; una cuenta de emergencia exige controles y seguimiento específicos. Mantén un propietario funcional de cada grupo y una finalidad escrita para que las revisiones no dependan de recordar quién solicitó su alta.

El dominio es una frontera de administración y autenticación, pero la estructura de OU se diseña principalmente para delegación y aplicación de políticas. Una OU no concede por sí misma permiso sobre una carpeta compartida. Tampoco es necesario copiar exactamente el organigrama empresarial: un árbol basado en departamentos que cambian continuamente puede multiplicar movimientos y efectos de GPO. Para un aula, separar `Usuarios-LAB`, `Equipos-LAB`, `Grupos-LAB` y `Pruebas-GPO` permite acotar ensayos sin modificar contenedores de producción.

## 5.2 Dependencias: DNS, tiempo y conectividad

Para encontrar un controlador, un cliente necesita más que resolver `dc01.ad.aula.test` como dirección A. Los registros SRV anuncian servicios y permiten selección por dominio y sitio. Una entrada en el archivo `hosts` puede resolver un nombre concreto, pero no reemplaza el conjunto de registros que requiere el localizador de dominio. La siguiente investigación se realiza en PowerShell de `cli01`, con el DNS LAB apuntando a `192.168.56.11`:

```powershell
Get-DnsClientServerAddress -AddressFamily IPv4
Resolve-DnsName dc01.ad.aula.test -Server 192.168.56.11
Resolve-DnsName _ldap._tcp.dc._msdcs.ad.aula.test -Type SRV -Server 192.168.56.11
Resolve-DnsName _kerberos._tcp.ad.aula.test -Type SRV -Server 192.168.56.11
Test-NetConnection 192.168.56.11 -Port 389
```

Cada resultado demuestra algo distinto. Una respuesta SRV identifica el nombre y puerto anunciado, pero no demuestra que ese puerto acepte tráfico. Una conexión TCP a LDAP demuestra transporte, no que una búsqueda esté autorizada. Una resolución de un servidor público no puede demostrar que existe la zona privada del dominio. Registra servidor consultado, tipo, nombre, respuesta y tiempo de la prueba.

Kerberos utiliza información temporal para reducir repetición de mensajes. La zona horaria visible afecta a la presentación, mientras que la comparación de tiempos utiliza una referencia temporal común. Dos pantallas con horas locales distintas pueden corresponder al mismo instante si las zonas son diferentes. Consulta `Get-Date`, `w32tm /query /status` y `w32tm /query /source` antes de decidir que hay desfase. No fuerces una hora arbitraria ni añadas varios servicios de sincronización que compitan.

El DC del ejercicio debe tener la NIC LAB preparada y no publicar en DNS una dirección NAT que el cliente no pueda alcanzar. Para las actualizaciones se puede utilizar una fase temporal con NAT; después se vuelve al diseño de una NIC del escenario. Tener varias direcciones registradas puede producir un fallo intermitente: algunas consultas seleccionan una dirección válida y otras una inaccesible. Revisa los datos del DNS, no únicamente la configuración aparente del adaptador.

## 5.3 Recorrido de una autenticación Kerberos

Una explicación operativa ayuda a elegir pruebas. Al iniciar sesión, el cliente obtiene material de autenticación y solicita un ticket inicial al servicio correspondiente. Con un ticket de concesión de tickets puede solicitar después un ticket para un servicio concreto, identificado por su principal de servicio. El servicio valida el ticket con sus claves y se construye el contexto de seguridad necesario para la operación. El intercambio evita enviar una contraseña en cada acceso, pero no elimina la necesidad de proteger claves, equipos y sesiones.

No todos los tickets caducan simultáneamente ni todos los cambios de grupo alteran instantáneamente un token ya creado. Si acabas de añadir a una persona a un grupo y conserva una sesión antigua, una consulta al directorio puede mostrar la pertenencia mientras que el proceso que accede al recurso aún utiliza un contexto anterior. Primero documenta quién es la identidad efectiva y qué sesión se está probando. Una nueva sesión controlada permite distinguir caché o token de un problema de pertenencia.

En una consola del cliente puedes observar, sin purgar nada de forma indiscriminada:

```powershell
whoami /user
whoami /groups
klist
Get-SmbConnection
```

`klist` muestra tickets de la sesión correspondiente; `Get-SmbConnection` ayuda a identificar conexiones SMB y usuarios empleados. Ejecutar una consola elevada puede cambiar el contexto que observas. Usa la sesión del usuario que debe cumplir el requisito y documenta cuándo elevas. No compartas capturas que contengan nombres reales o información innecesaria de un dominio ajeno.

Un acceso a `\\192.168.56.11\recurso` y otro a `\\dc01.ad.aula.test\recurso` no tienen necesariamente el mismo recorrido de autenticación. Los nombres de servicio y sus SPN importan. Acceder por IP puede impedir utilizar el principal esperado; el resultado no justifica habilitar protocolos antiguos o debilitar políticas. Prueba por el nombre canónico diseñado y estudia los registros de autenticación antes de atribuir el problema a una contraseña.

NTLM aparece en diagnósticos y compatibilidad, pero conocerlo no obliga a seleccionarlo como solución. El administrador identifica por qué se está utilizando y qué aplicación o configuración necesita corregirse. No desactives protecciones ni habilites mecanismos obsoletos por comodidad de un único cliente. La compatibilidad se resuelve con una decisión documentada sobre versiones, nombres y métodos admitidos.

## 5.4 Grupos: separar personas, función y permiso

AGDLP expresa una estrategia de asignación en un dominio: cuentas a grupos globales de función, esos grupos a grupos locales de dominio que representan permisos, y estos últimos a las ACL del recurso. La utilidad no reside en las siglas, sino en separar el motivo de pertenencia del permiso que necesita un recurso. Para un laboratorio:

| Objeto | Significado | Ejemplo de relación |
| --- | --- | --- |
| Cuenta `alba.lab` | Identidad sintética individual | Miembro de `GG_LAB_Soporte` |
| `GG_LAB_Soporte` | Función de soporte | Miembro de `DL_LAB_Manuales_Modificar` |
| `DL_LAB_Manuales_Modificar` | Autorización sobre Manuales | Concedida modificación en el recurso |
| `DL_LAB_Manuales_Leer` | Autorización de consulta | Concedida lectura a otro grupo funcional |

Una cuenta no necesita pertenecer a veinte grupos de recurso si su función se expresa mediante unos pocos grupos mantenibles. El anidamiento excesivo, sin embargo, dificulta entender el acceso y puede producir tokens grandes o relaciones circulares. Documenta cada relación y comprueba pertenencia efectiva; no deduzcas el resultado de un único listado de miembros directos.

La creación de grupos no debe depender de nombres que puedan confundirse. Incluye ámbito, función y permiso de forma consistente. La descripción debe indicar propietario y solicitud que la justifica. Evita nombres como `GrupoNuevo2`, cuyo significado desaparece al terminar la práctica. Mantén un registro de altas, cambios y bajas con aprobaciones didácticas del tutor o del responsable del caso.

Las listas ACL no se corrigen añadiendo permisos directos a una cuenta cada vez que alguien no puede trabajar. Esa práctica crea excepciones difíciles de retirar. Primero comprueba función, grupo, token y herencia. Si existe una excepción justificada, registra alcance y fecha de revisión. Al dar de baja una persona, deshabilitar la cuenta, retirar sesiones y revisar datos y titularidades son tareas diferentes.

## 5.5 Cómo se procesan las GPO

Las directivas de grupo combinan configuraciones de equipo y usuario. Su resultado depende del objeto que inicia el procesamiento, de los vínculos, de la herencia, del orden, del filtrado y de las extensiones que aplican cada ajuste. La regla de estudio local–sitio–dominio–OU ayuda a comenzar, pero no es una explicación completa cuando existen vínculos forzados, bloqueo de herencia o filtros. Examina el conjunto resultante, no únicamente el editor.

Si dos GPO definen un mismo ajuste, el orden y las reglas de precedencia deciden el resultado. Los valores no se suman aritméticamente. Algunas opciones se aplican al inicio o al inicio de sesión y otras en actualizaciones posteriores. Una actualización de directiva puede avisar de que necesita cerrar sesión o reiniciar: ese aviso forma parte del procedimiento, no es un error que deba ocultarse.

Diseña primero una GPO de prueba con un ajuste reversible y visible. Vincúlala a una OU exclusiva que contenga únicamente `cli01` o una cuenta sintética, según sea configuración de equipo o usuario. Conserva el valor anterior y registra el vínculo. Un bloqueo amplio de acceso a herramientas administrativas es un mal primer ensayo, porque puede impedir el propio diagnóstico.

En Windows 11 Pro, los siguientes comandos permiten recoger evidencia:

```powershell
gpresult /r
gpresult /h "$env:TEMP\informe-gpo-lab.html"
gpupdate /target:computer /force
```

El informe HTML puede contener información del dominio y se revisa antes de publicarlo. `gpupdate /force` no convierte una GPO mal vinculada en aplicable. Si no aparece, revisa dónde está el objeto de equipo, qué ámbito tiene el ajuste, qué permisos de lectura y aplicación existen y si un filtro excluye el caso. Usa el Visor de eventos de GroupPolicy para investigar errores del procesamiento, con fecha y equipo identificados.

## 5.6 Loopback: decidir según el equipo utilizado

En equipos compartidos puede interesar que la configuración de usuario dependa del equipo, por ejemplo un puesto de atención o un aula específica. El procesamiento loopback permite incorporar las configuraciones de usuario vinculadas al ámbito del equipo. Sus modos de combinación o sustitución cambian qué conjunto se utiliza. No se habilita para reparar una GPO que simplemente está en la OU equivocada.

Supón que la cuenta `alba.lab` está en `Usuarios-LAB` y `cli01` en `Equipos-LAB`. Una directiva de usuario vinculada sólo a la OU del equipo normalmente no se aplica al usuario por esa ubicación. Si el diseño exige una configuración de usuario específica de ese puesto, se estudia loopback y se verifica con el informe resultante. Si sólo se quería una política general para Alba, se vincula al ámbito de usuario adecuado.

En una prueba controlada prepara dos ajustes no destructivos y distintos, uno por ámbito, y registra qué debe ocurrir en modo normal, combinación y sustitución. No cambies los tres escenarios a la vez. Tras cada transición, realiza los cierres de sesión o actualizaciones que requiera el ajuste y guarda informes comparables. Al terminar, deshabilita el vínculo de prueba o restaura su configuración, sin borrar una GPO compartida con otras actividades.

## 5.7 Casos de diagnóstico razonado

**Caso A: el usuario ve el grupo en AD, pero no puede editar.** Consulta primero quién inicia la conexión SMB y con qué sesión. Si es una sesión anterior al cambio, vuelve a probar en un contexto nuevo. Si persiste, revisa que el grupo funcional esté anidado en el grupo de permiso correcto y que ese grupo figure en las ACL efectivas. No agregues al usuario a Administradores para resolver la escritura.

**Caso B: se encuentra el DC por nombre, pero la unión al dominio falla.** Una respuesta A no demuestra localización de servicios. Consulta SRV contra el DNS del directorio, revisa hora y conectividad necesaria, y recoge el mensaje de unión completo. La solución no consiste en añadir un servidor público como segundo DNS «por si acaso»: podría responder de forma distinta sin conocer la zona interna.

**Caso C: la GPO aparece como denegada.** El objeto puede estar dentro del ámbito jerárquico y aun carecer de permisos de lectura o aplicación. También puede excluirlo un filtro. Registra el motivo exacto del informe, consulta la configuración pertinente y corrige el alcance mínimo. No quites todos los filtros para conseguir una captura de éxito.

**Caso D: una política de usuario funciona en un PC y no en otro.** Compara ubicación de cuentas de equipo, loopback, conectividad al DC y procesamiento de extensiones. No asumas que la pertenencia al mismo dominio hace idénticos los puestos. Los equipos pueden tener configuraciones y estados de aplicación diferentes.

**Caso E: tras recrear una cuenta con el mismo nombre aparecen permisos huérfanos.** Identifica los SID en la ACL y el SID de la nueva cuenta. Reconstruye el acceso mediante grupos definidos, documentando la retirada de entradas antiguas. El nombre visible no permite afirmar que se trata del mismo principal.

## 5.8 Entrega de una arquitectura de identidad

Una entrega avanzada incluye diagrama de dominio y OU, catálogo de grupos y propietarios, relación cuenta–función–permiso y matriz de recursos. Añade dependencia DNS y tiempo, informe GPO con datos mínimos, dos pruebas de acceso permitido y dos de denegación. Explica cómo se incorpora una persona, cambia de función y se retira.

La defensa debe responder por qué una OU no sustituye a un grupo de autorización, por qué un cliente necesita DNS de AD y cómo se distingue un cambio no aplicado de un permiso mal diseñado. El objetivo no es conseguir muchos objetos, sino una estructura que otra persona pueda administrar sin adivinar su intención.

## 5.9 Relaciones de confianza y límites de autoridad

Una relación de confianza permite que una infraestructura acepte determinadas autenticaciones procedentes de otra bajo reglas explícitas. No concede automáticamente autorización para todos los recursos. La persona todavía necesita un permiso efectivo sobre el servicio al que accede, y el servicio debe localizar e interpretar correctamente su identidad y grupos. Confundir confianza con acceso universal conduce a diseños demasiado amplios.

El sentido importa: si un entorno confía en identidades del otro, no se deduce necesariamente la relación inversa. También importan alcance y transitividad. Los mecanismos entre dominios de un bosque y las relaciones externas o entre bosques no se describen con una única regla simplificada. Antes de diseñarlas identifica quién administra cada entorno, qué identidades deben cruzar, qué servicios se publican y cómo se limita ese cruce.

En una pequeña organización, crear un segundo bosque para separar un departamento puede añadir complejidad sin resolver la necesidad original. Quizá basten grupos, OU, delegación y permisos dentro del diseño existente. En otros casos una frontera administrativa independiente sí es una necesidad, pero necesita analizar DNS, resolución de nombres, conectividad, métodos de autenticación, cuentas y supervisión. La decisión se fundamenta en requisitos y responsabilidades, no en que un diagrama con más dominios parezca más avanzado.

El laboratorio base de un dominio no crea relaciones con redes reales ni con la identidad del centro. Para estudiar el concepto sin ampliar recursos, prepara una tabla ficticia de dos organizaciones y marca sentido de autenticación, recurso, grupo autorizado y prueba negativa. Si en una práctica posterior se implementa una relación, se realiza entre entornos aislados propios y mediante la documentación de la versión, con una estrategia de retirada. No reutilices un DC de producción ni compartas credenciales administrativas entre entornos para acelerar la prueba.

Para estudiar loopback con mayor precisión en GPMC, localiza en la GPO del equipo el ajuste de **Configuración del equipo → Directivas → Plantillas administrativas → Sistema → Directiva de grupo → modo de procesamiento loopback de directiva de grupo de usuario**; el nombre traducido puede variar con las plantillas administrativas. Comprueba la descripción del ajuste, selecciona el modo previsto y registra el valor. Vincula sólo a la OU del equipo de prueba, conserva las configuraciones de usuario que se quieren comparar y valida con `gpresult` en una sesión nueva cuando corresponda. El procedimiento no requiere modificar directivas predeterminadas del dominio.

## Referencias primarias

- [Microsoft: procesamiento de Group Policy](https://learn.microsoft.com/windows-server/identity/ad-ds/manage/group-policy/group-policy-processing).
- [Microsoft: procesamiento loopback](https://learn.microsoft.com/troubleshoot/windows-server/group-policy/loopback-processing-of-group-policy).
- [Microsoft: Kerberos Authentication Overview](https://learn.microsoft.com/windows-server/security/kerberos/kerberos-authentication-overview).
- [Microsoft: grupos de seguridad de Active Directory](https://learn.microsoft.com/windows-server/identity/ad-ds/manage/understand-security-groups).
- [Microsoft: gpresult](https://learn.microsoft.com/windows-server/administration/windows-commands/gpresult).
