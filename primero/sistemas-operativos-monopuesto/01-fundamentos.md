# 01 · Fundamentos de sistemas operativos

[Volver al módulo](README.md) · [Continuar con la guía técnica](02-guia-tecnica.md)

## 1. Qué hace un sistema operativo

Un sistema operativo administra CPU, memoria, dispositivos y almacenamiento, y proporciona interfaces para ejecutar programas. El kernel se ejecuta con privilegios y controla operaciones sensibles. Las aplicaciones solicitan servicios mediante interfaces y llamadas al sistema, como abrir un archivo, crear un proceso o reservar memoria. La separación de privilegios reduce la posibilidad de que una aplicación altere directamente la memoria de otra o el hardware.

No confundas kernel con distribución. Linux es un kernel; Debian incorpora además instalador, bibliotecas, utilidades, gestor de paquetes y políticas de integración. En Windows el sistema combina kernel, servicios, bibliotecas, interfaz y herramientas. Una interfaz gráfica es una forma de administrar el sistema, no su definición.

Un controlador traduce operaciones del sistema a un dispositivo o clase de dispositivos. Si una tarjeta aparece en el bus pero no tiene un controlador adecuado, el hardware puede estar presente y no resultar utilizable. Instalar varios controladores al azar aumenta la incertidumbre: identifica primero dispositivo, versión y procedencia.

## 2. Procesos, hilos y planificación

Un programa es un conjunto de instrucciones almacenado; un proceso es una instancia en ejecución con identificador, espacio de direcciones, credenciales y recursos. Un hilo es una secuencia de ejecución dentro del proceso. Los hilos de un mismo proceso comparten memoria y otros recursos, lo que facilita comunicar datos pero requiere sincronización.

El planificador distribuye tiempo de CPU entre tareas ejecutables. Que existan cien procesos no significa que todos consuman CPU: muchos esperan entrada/salida o eventos. Un estado de espera de disco no se corrige necesariamente aumentando prioridad. La prioridad cambia la preferencia de planificación; no crea potencia de cómputo ni elimina dependencias.

En Linux son útiles estos estados conceptuales:

| Estado | Interpretación práctica |
| --- | --- |
| Ejecutable | La tarea puede usar CPU y espera o está usando un procesador |
| Espera interrumpible | Espera un evento, como entrada de usuario |
| Espera no interrumpible | Frecuentemente espera ciertas operaciones del kernel o I/O |
| Detenido | La tarea ha sido suspendida por control de trabajos o señal |
| Zombi | Terminó, pero su proceso padre no ha recogido todavía su estado |

Un zombi no es un programa consumiendo CPU activamente. Acumular muchos puede indicar un problema del padre. La carga media de Linux incluye tareas ejecutables y determinadas esperas no interrumpibles; no equivale al porcentaje de CPU. Una carga de cuatro se interpreta de forma distinta en dos y en dieciséis CPU lógicas, y puede aumentar por almacenamiento bloqueado.

Las señales comunican eventos. `SIGTERM` solicita terminación y permite limpieza; `SIGKILL` fuerza la terminación sin que el proceso pueda manejarla. Forzar el cierre puede dejar archivos incompletos o trabajo sin guardar. En administración se empieza por cierre normal, luego terminación dirigida y solo finalmente fuerza sobre un proceso de prueba identificado.

## 3. Memoria física y virtual

Cada proceso trabaja con direcciones virtuales traducidas mediante tablas de páginas. Esto facilita aislamiento, carga flexible y compartición controlada. Una dirección virtual no es directamente una posición fija de RAM. La unidad de traducción habitual es la página y su tamaño depende de arquitectura y configuración.

La RAM se utiliza para código, datos, kernel y cachés. Linux emplea memoria que no necesita inmediatamente para acelerar acceso a archivos y puede recuperarla cuando otro trabajo la requiere. Por eso `available` es una referencia más útil que `free` para estimar margen. En Windows existen conceptos como conjunto de trabajo y memoria comprometida que no son intercambiables con memoria física usada.

Cuando no hay memoria suficiente, el sistema puede recuperar páginas limpias, escribir determinadas páginas al área de intercambio y, en última instancia, terminar procesos o rechazar reservas. La paginación sostenida puede convertir un SSD rápido en un cuello de botella por latencia. Aumentar swap puede evitar un fallo inmediato, pero no convierte almacenamiento en RAM equivalente.

Para diagnosticar observa evolución temporal: memoria disponible, entradas y salidas de swap, tareas afectadas y registros. Un pico momentáneo y una falta sostenida de capacidad tienen soluciones diferentes. Un proceso que aumenta continuamente su consumo con una carga estable puede tener una fuga, pero hay que distinguirla de una caché deliberada.

## 4. Almacenamiento por capas

```text
Dispositivo físico o virtual
  → tabla de particiones, si se utiliza
    → partición o volumen lógico
      → sistema de archivos
        → directorios y archivos
```

Puede haber capas adicionales: RAID, cifrado o LVM. Un problema de una capa no implica que deban recrearse todas. Si la unidad se detecta, la partición existe y el sistema de archivos no monta, borrar la tabla de particiones no es una reparación razonada.

GPT almacena descripciones de particiones con identificadores y redundancia. MBR es un esquema anterior con límites dependientes del tamaño de sector; el límite clásico cercano a 2 TiB se refiere a sectores lógicos de 512 bytes. No reduzcas el diagnóstico a una regla de capacidad sin revisar el formato real. En instalaciones modernas UEFI se utiliza normalmente GPT.

Un sistema de archivos organiza nombres, datos, metadatos, permisos y asignación de espacio. El diario de un sistema con *journaling* ayuda a mantener coherencia de metadatos tras ciertos fallos; no garantiza recuperar el contenido de todos los archivos ni sustituye una copia de seguridad.

En Linux, una ruta se resuelve desde `/` o desde el directorio actual. Los puntos de montaje integran distintos sistemas de archivos en el mismo árbol. En Windows son habituales letras de unidad, rutas UNC y puntos de montaje. Un volumen puede existir sin letra y un directorio Linux puede mostrar contenido diferente al montar otra unidad encima.

### Inodos y enlaces

En sistemas Linux habituales, un inodo conserva metadatos y referencias a datos; el nombre pertenece a una entrada de directorio. Un enlace duro añade otra referencia al mismo objeto y normalmente no cruza sistemas de archivos. Un enlace simbólico guarda una ruta que puede apuntar a otro sistema de archivos y quedar rota si desaparece el destino.

Eliminar un nombre no libera necesariamente los datos si existe otro enlace duro o un proceso mantiene el archivo abierto. Esto explica por qué borrar un registro grande no siempre recupera espacio hasta que el servicio cierre su descriptor. Reiniciar o rotar de forma controlada el servicio puede resolverlo; truncar datos indiscriminadamente elimina evidencia.

## 5. Permisos POSIX y ACL de Windows

En Linux cada archivo tiene propietario, grupo y permisos de lectura, escritura y ejecución. Para directorios, `r` permite listar nombres; `x` permite atravesar y acceder por nombre; `w`, junto con los permisos necesarios, permite crear o eliminar entradas. Poder modificar un archivo y poder eliminar su nombre son capacidades distintas.

La forma octal resume bits: lectura vale cuatro, escritura dos y ejecución uno. `640` significa propietario con lectura/escritura, grupo con lectura y resto sin permisos. No uses `777` como remedio universal: concede escritura y ejecución innecesarias y oculta qué identidad necesita acceso.

`umask` restringe los permisos iniciales solicitados al crear objetos; no modifica retroactivamente archivos existentes. Los permisos finales también dependen del programa y de ACL por defecto si existen. El bit setgid en un directorio ayuda a que nuevos objetos hereden el grupo, mientras que el bit sticky limita determinadas eliminaciones en directorios compartidos. Ambos deben explicarse en su contexto.

NTFS usa listas de control de acceso con entradas para identidades y grupos, herencia y derechos detallados. Un permiso puede provenir de varios grupos. Las denegaciones explícitas y el orden de evaluación complican las reglas simplificadas: utiliza Acceso efectivo y pruebas con la cuenta real. Convertirse en propietario no equivale por sí solo a tener todos los accesos de lectura; normalmente permite administrar permisos en determinados contextos.

Los permisos locales y los de un recurso compartido son capas diferentes, desarrolladas en segundo curso. En este módulo se trabaja primero acceso local. Si se prueba como administrador elevado, se puede medir una identidad o privilegios diferentes de los de la persona usuaria; realiza también pruebas sin elevación.

## 6. Usuarios, grupos y elevación

Una cuenta identifica a un sujeto y sus credenciales permiten autenticarse. Autorizar consiste en decidir qué puede hacer esa identidad. Autenticarse correctamente no da permiso para cualquier archivo. Los grupos facilitan asignar derechos a funciones en vez de repetir reglas para cada persona.

En Linux, `sudo` autoriza comandos según configuración y registra su uso. No todos los usuarios pertenecen al grupo que puede utilizarlo. En Windows, UAC separa normalmente operaciones corrientes de elevadas para cuentas administrativas. Trabajar permanentemente con privilegios máximos amplía las consecuencias de un error.

Bloquear pantalla, cerrar sesión, deshabilitar una cuenta y eliminarla son operaciones diferentes. Eliminar una cuenta no necesariamente elimina todos sus archivos y puede dejar ACL que referencien su identificador. Antes de retirar cuentas comprueba propiedad, tareas, servicios y retención autorizada.

## 7. Servicios, paquetes y tareas

Un servicio realiza trabajo en segundo plano. En Debian, systemd gestiona unidades como servicios, montajes y temporizadores. Que una unidad esté habilitada indica una relación con su activación prevista; no garantiza que esté ejecutándose ahora. Iniciar, detener, habilitar y deshabilitar resuelven preguntas distintas.

Un paquete agrupa archivos y metadatos de instalación, dependencias y configuración. `apt` resuelve operaciones sobre repositorios y `dpkg` gestiona paquetes a un nivel inferior. Actualizar índices no instala actualizaciones. La firma de repositorios verifica procedencia e integridad dentro de una cadena de confianza; no garantiza que todo paquete esté libre de errores.

Una tarea programada debe especificar identidad, directorio de trabajo, ruta de ejecutables, horario, registros y condición de éxito. Un comando que funciona en una terminal puede fallar en un programador por entorno distinto, falta de sesión gráfica o permisos. No guardes contraseñas en scripts para solucionar esa diferencia.

## 8. Virtualización, snapshots y copias

Un hipervisor proporciona hardware virtual y aísla máquinas con grados distintos de integración. La VM consume memoria y CPU del anfitrión; asignar más vCPU de forma indiscriminada puede empeorar competencia y latencia. La sobreasignación de almacenamiento fino también puede agotar el disco físico aunque el invitado vea espacio libre.

Un snapshot conserva un estado o una relación de diferencias según el hipervisor. No debe confundirse con una copia independiente: puede depender de archivos originales y compartir el mismo riesgo físico. Restaurarlo puede revertir cambios de identidad o tiempo; en servicios de red hay consideraciones adicionales.

Para este módulo utiliza red interna o NAT según el objetivo, datos ficticios y una copia o exportación independiente. Deshabilita integraciones innecesarias como carpetas del anfitrión cuando no se requieran. Registra nombres de VM, versión, recursos y puntos de recuperación para que otro alumno pueda repetir el laboratorio.

## Referencias de ampliación

- [Debian Reference: conceptos y administración](https://www.debian.org/doc/manuals/debian-reference/).
- [Kernel Linux: conceptos de memoria](https://docs.kernel.org/admin-guide/mm/concepts.html).
- [systemd: conceptos de unidades](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html).
- [Microsoft Learn: control de acceso](https://learn.microsoft.com/windows/security/identity-protection/access-control/access-control).
- [Microsoft Learn: memoria y espacios de direcciones](https://learn.microsoft.com/windows/win32/memory/virtual-address-spaces).
