# Proyecto: infraestructura para una oficina de doce puestos

## 1. Necesidad, alcance y entregables

Una pequeña empresa ficticia dispone de cuatro puestos de administración y ocho de soporte. Necesita acceso a documentos compartidos, intranet, resolución de nombres, asignación IP y un procedimiento verificable de copia y recuperación. Se propone una infraestructura proporcionada a ese tamaño, con grupos de acceso separados, inventario y documentación de mantenimiento. No se utilizarán datos, credenciales ni contratos reales.

El alcance mínimo es un laboratorio funcional con servidor, cliente, servicios y restauración de una muestra. La extensión de segmentación mediante VLAN requiere un switch y un router compatibles o un simulador adecuado; debe identificarse como una fase adicional si no se implementa. No se considera desplegada una arquitectura porque aparezca en un dibujo.

Entregables mínimos: memoria de requisitos, diagramas lógico y físico, inventario, plan de direccionamiento, lista de componentes y versiones, configuración sin secretos, plan de copias, procedimiento de recuperación, registro de cambios, matriz de pruebas y manual de operación. El repositorio contiene instrucciones y evidencias saneadas; el almacenamiento de copias y secretos permanece fuera de él.

## 2. Requisitos con pruebas

| ID | Requisito propuesto | Comprobación |
| --- | --- | --- |
| R01 | Los equipos autorizados obtienen configuración IP válida. | Renovar concesión en un cliente de prueba y registrar IP, prefijo, DNS y servidor DHCP. |
| R02 | La intranet se resuelve por su nombre interno. | Consultar registro DNS y abrir el servicio desde el cliente. |
| R03 | Administración y soporte tienen permisos definidos. | Probar acceso permitido y denegado con cuentas diferentes. |
| R04 | La intranet usa HTTPS con confianza configurada en el laboratorio. | Comprobar nombre, cadena y vigencia del certificado. |
| R05 | Los datos de prueba pueden restaurarse. | Restaurar en ubicación separada y comparar contenido y permisos. |
| R06 | Los cambios quedan documentados. | Repetir un procedimiento usando sólo la documentación. |
| R07 | La retirada de un equipo conserva trazabilidad. | Completar una ficha sintética con decisión y destino. |

Las pruebas deben registrar también condiciones de error. Un recurso compartido accesible para todo el mundo no cumple R03 aunque se pueda abrir desde la cuenta administradora. Un navegador que muestra una página después de ignorar una advertencia no demuestra que la confianza HTTPS esté bien configurada.

## 3. Arquitectura base y ampliación

### Laboratorio base común

Empieza por la [topología compartida](../../docs/laboratorio.md): `srv01` con Debian 13 en `192.168.56.10/24`, `cli01` en `.20`, red LAB aislada/host-only y dominio de prácticas `aula.test`. La interfaz LAB debe identificarse; `ens19` es sólo un nombre de ejemplo. Una NIC NAT adicional puede facilitar actualizaciones, pero DHCP y servicios internos deben escuchar únicamente donde esté previsto. No se presupone que `.1` sea un router de la red LAB.

Despliega DNS, DHCP en un ámbito que no incluya las IP estáticas, archivos y web según las guías de los módulos. Si el hipervisor ejecuta su propio DHCP en LAB, desactívalo para esa red antes de probar otro servidor. Registra la configuración previa y las interfaces para no tocar la red doméstica o del centro.

El directorio de usuarios puede empezar con cuentas locales y Samba independiente. Si se utiliza AD, despliega `dc01` en otra VM y documenta DNS y dominio `ad.aula.test`; no conviertas sin planificación el servidor BIND independiente en controlador de dominio. Dos servicios que intentan ocupar el mismo puerto no pueden presentarse como una configuración válida.

### Extensión segmentada

La siguiente tabla es un **diseño nuevo**, distinto del laboratorio plano anterior. Sólo se ejecuta si se han desplegado router virtual o físico y switch con VLAN; una red host-only sencilla no implementa automáticamente esa segmentación.

| VLAN | Finalidad | Subred propuesta | Interfaz del router que se debe crear |
| --- | --- | --- | --- |
| 10 | Cuatro puestos de administración | `10.40.10.0/24` | `10.40.10.1` |
| 20 | Ocho puestos de soporte | `10.40.20.0/24` | `10.40.20.1` |
| 30 | Servidores | `10.40.30.0/24` | `10.40.30.1` |
| 99 | Gestión de infraestructura | `10.40.99.0/24` | `10.40.99.1` |

En esta extensión, `srv01` pasa a `10.40.30.10`; un `dc01` opcional, a `.11` de la misma subred. Esa migración exige actualizar registros DNS, enlaces, ámbitos DHCP y configuraciones que contengan direcciones anteriores. Mantén un listado de cambios y una forma de volver al laboratorio base.

Los puertos de usuario son de acceso en su VLAN; el enlace switch-router transporta las VLAN necesarias mediante trunk etiquetado, con configuración compatible en ambos extremos. Cada subred utiliza un ámbito DHCP propio, por ejemplo `.100` a `.149`. Para llegar al servidor DHCP de VLAN 30 desde otra VLAN hace falta un relay en el router o servidores locales; las difusiones DHCP no atraviesan un router por sí solas.

Define una matriz de comunicaciones. Los clientes pueden consultar DNS y acceder a los servicios necesarios; los puertos de gestión sólo se permiten desde el puesto autorizado de VLAN 99; el tráfico entre puestos y otras VLAN se deniega salvo necesidad demostrada. No uses “permitir todo entre VLAN” como estado final. Las reglas se aplican en el equipo que realmente enruta y se prueban desde origen y destino adecuados.

## 4. Identidades, datos y operación

Diseña grupos por función y concede permisos a grupos en vez de a cuentas individuales. Por ejemplo, administración puede modificar su carpeta y leer un área común; soporte mantiene su documentación y no accede a los documentos restringidos de administración. Distingue permiso de recurso SMB y permiso del sistema de archivos. Documenta herencia, propietario y acceso efectivo.

Crea usuarios ficticios y una política de altas, bajas y recuperación de acceso. Una baja debe revocar acceso, revisar propiedad de datos y conservar únicamente lo permitido por la política. No utilices la misma contraseña en todas las cuentas ni la publiques para que la demostración sea más fácil. Entrega credenciales de aula por el canal acordado con el centro.

Registra eventos necesarios para diagnóstico y seguridad: cambios de configuración, fallos de servicio y resultado de copias. Limita datos personales y retención. Configura hora coherente para correlacionar eventos; guarda hora y zona horaria en la documentación. Un gráfico de disponibilidad sin indicar de dónde procede el dato no es evidencia suficiente.

## 5. Copias, RPO y RTO

Define **RPO** como la pérdida de datos temporal máxima tolerada y **RTO** como el tiempo objetivo de recuperación del servicio. Para este caso se proponen RPO de 24 horas y RTO de cuatro horas; son requisitos didácticos que deben validarse con el procedimiento, no garantías ya cumplidas.

Una copia diaria que siempre termina correctamente podría aproximarse al RPO previsto, pero una copia fallida sin revisión aumenta la ventana de pérdida. Necesitas registros, alertas y verificación. Utiliza soportes independientes y una copia desconectada o con protección frente a modificaciones cuando sea viable. Un RAID mantiene disponibilidad frente a ciertos fallos de disco; no protege por sí solo de borrado, ransomware o incendio.

El plan incluye datos, configuración, inventario, dependencias y recuperación del sistema. Restaurar sólo los archivos puede no devolver identidades o permisos. En una muestra de 30 GB y rendimiento efectivo supuesto de 20 MB/s, la transferencia sería aproximadamente de 25 minutos usando unidades decimales; el RTO también incluye diagnóstico, preparación, restauración de configuraciones y pruebas. No extrapoles ese cálculo a cuatro horas de servicio recuperado sin medir el procedimiento completo.

## 6. Presupuesto y viabilidad

Ejemplo de estimación educativa sin IVA. Los importes no son ofertas ni precios de mercado; deben sustituirse por propuestas verificadas si se usa el proyecto para una compra.

| Concepto | Cantidad | Unitario | Subtotal |
| --- | ---: | ---: | ---: |
| Puesto completo de ejemplo | 12 | 400 € | 4 800 € |
| Switch gestionable | 1 | 250 € | 250 € |
| Router compatible | 1 | 180 € | 180 € |
| Servidor de ejemplo | 1 | 800 € | 800 € |
| Soporte independiente para copia | 2 | 100 € | 200 € |
| SAI | 1 | 200 € | 200 € |
| Punto de acceso | 1 | 120 € | 120 € |
| Latiguillos | 24 | 3 € | 72 € |
| Organización y accesorios | 1 lote | 150 € | 150 € |
| **Material** | | | **6 772 €** |
| Trabajo de implantación supuesto | 40 h | 25 €/h | 1 000 € |
| **Total parcial supuesto** | | | **7 772 €** |

Faltan, si son necesarios, licencias, soporte recurrente, formación, conectividad, energía, copias externas, renovación y contingencia. No presupongas que Windows o cualquier producto comercial dispone de licencia gratuita de producción. En el laboratorio utiliza licencias del centro o evaluaciones legítimas dentro de sus condiciones.

Para seleccionar hardware comprueba compatibilidad, rendimiento, ampliación, soporte y reparación. El SAI debe dimensionarse con carga y autonomía requeridas; su cifra en VA no equivale directamente a vatios útiles ni garantiza una duración concreta. La compra de un único servidor implica un punto de fallo y exige que la recuperación esté asumida.

## 7. Planificación y control de cambios

| Periodo orientativo | Actividad | Salida necesaria antes de continuar |
| --- | --- | --- |
| Semana 1 | Requisitos e inventario | Alcance y pruebas aprobados en el equipo. |
| Semana 2 | Diseño lógico, físico y presupuesto | Topología y dependencias consistentes. |
| Semana 3 | Laboratorio base e identidades | Comunicación y permisos comprobables. |
| Semana 4 | DNS, DHCP, web y copias | Pruebas de servicio registradas. |
| Semana 5 | Segmentación opcional y recuperación | Evidencia de aislamiento y restauración. |
| Semana 6 | Revisión, manuales y defensa | Otra persona puede operar lo desplegado. |

Esta distribución es una propuesta, no el horario oficial del módulo ni una asignación de horas lectivas. Divide tareas y dependencias; no asignes a una persona probar únicamente su propia configuración. Utiliza control de versiones para la documentación y un registro de decisiones con alternativas y motivo de elección.

[Pruebas y defensa](02-practicas-y-evaluacion.md) · [Índice](README.md)
