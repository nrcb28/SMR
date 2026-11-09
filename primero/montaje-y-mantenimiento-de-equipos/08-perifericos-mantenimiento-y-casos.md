# 08 · Periféricos, impresión y mantenimiento organizado

[Índice](README.md) · [Casos de diagnóstico](06-diagnostico-por-subsistemas.md)

## 1. El periférico como sistema completo

Un periférico combina alimentación, conexión, protocolo, controlador, firmware, configuración y aplicación. Que aparezca un dispositivo conectado no demuestra que estén disponibles todas sus funciones. Una pantalla puede mostrar imagen y no ofrecer la resolución esperada; una impresora puede aceptar un trabajo y no producir papel; una cámara puede funcionar en una aplicación y estar bloqueada por permisos en otra.

El inventario debe recoger la función requerida y el trayecto. Para una cámara: puerto, cable, modo admitido, aplicación, resolución y permisos. Para una impresora: tecnología, conexión, dirección o cola, lenguaje/controlador, tamaño de papel y política de acceso. Estos datos reducen la tentación de reinstalar controladores sin saber qué parte está fallando.

Antes de una sustitución verifica especificaciones y compatibilidad. La forma del conector no garantiza transporte de vídeo, potencia suficiente o velocidad máxima. Un adaptador puede cambiar el protocolo y añadir límites. Documenta cada elemento del trayecto para localizar dónde se negocia una característica inferior.

## 2. USB: conector, protocolo y alimentación

USB-C describe un conector; no basta para deducir todas las capacidades del puerto o cable. Un mismo formato puede ofrecer combinaciones diferentes de datos, carga y modos alternativos. Consulta las marcas y especificaciones de equipo, dock, cable y periférico. Una cadena queda limitada por las capacidades compatibles del conjunto, no por el componente con la cifra mayor en su caja.

Los concentradores comparten un enlace ascendente y, según diseño, una fuente de alimentación. Varias capturadoras o unidades de almacenamiento pueden competir por ancho de banda; un concentrador sin alimentación suficiente puede sufrir desconexiones al aumentar carga. El diagnóstico separa falta de energía, saturación y fallos de enumeración mediante pruebas controladas con un solo dispositivo y un puerto conocido adecuado.

En Linux, `lsusb` y `lsusb -t` permiten observar dispositivos y topología que ve el sistema. Pertenecen a `usbutils`; si faltan, instala el paquete en la VM autorizada. Los logs del kernel pueden registrar conexión y desconexión. En una VM con passthrough, identifica además si el dispositivo lo posee el anfitrión o el invitado: una desconexión aparente puede ser un cambio de asignación del hipervisor.

No cambies políticas de ahorro de energía globales como primer paso. Comprueba si el síntoma coincide con suspensión, conector, movimiento o demanda. Si se ensaya una opción energética, registra su ámbito, valor anterior y efecto. Una mejora en un modelo no convierte el ajuste en recomendación universal para todos los puestos.

## 3. Pantallas, docks y resolución

Analiza resolución, frecuencia, formato de color y transporte como una combinación. Una conexión puede admitir una resolución a una frecuencia y no otra superior. El escalado del escritorio modifica tamaño aparente de elementos y no es lo mismo que cambiar el número de píxeles transmitidos. Un usuario que ve texto pequeño puede necesitar escalado accesible, no una reducción arbitraria de resolución.

Con varios monitores, documenta qué puerto sirve a cada pantalla y qué recursos comparte el dock. Algunos equipos admiten un número limitado de salidas simultáneas o requieren un modo concreto. Si una pantalla pierde señal sólo al conectar otra, prueba combinaciones admitidas y consulta la matriz del fabricante. No atribuyas el fallo automáticamente al cable recién instalado.

Comprueba con contenido de prueba conocido: texto, patrones y vídeo local sintético. Diferencia imagen desenfocada por escala o resolución no nativa, parpadeo por frecuencia/transporte y problemas de aplicación. En proyectos de accesibilidad, además de resolución se valora legibilidad, contraste, tamaño y facilidad de uso, con la persona usuaria implicada en la aceptación.

## 4. La cadena de impresión

Un trabajo pasa por aplicación, representación de página, cola, controlador/filtro, transporte y motor físico. Cada etapa puede aceptar el trabajo y dejar que falle después. El diagnóstico empieza preguntando dónde existe evidencia: vista previa correcta, trabajo en cola, envío confirmado, página de autoprueba del equipo y resultado físico.

La página de autoprueba generada desde el propio dispositivo separa en parte motor físico y trayecto informático. Si sale correctamente y el trabajo del PC no, investiga cola, formato, controlador y transporte. Si también falla la autoprueba, revisa consumibles, papel, sensores y mantenimiento previsto. No abras el fusor ni manipules zonas calientes o de alta tensión para una práctica básica.

No confundas calidad de impresión, atasco y escalado. Líneas o manchas repetidas pueden relacionarse con consumible o elemento mecánico según su patrón; un documento cortado puede deberse al tamaño de papel configurado; páginas desordenadas pueden ser opciones de dúplex, orientación o aplicación. Conserva una muestra de prueba sin datos personales y relaciona el patrón con el manual del modelo.

## 5. Colas y consulta en Windows

En Windows 11, utiliza las herramientas del sistema y del controlador admitido. PowerShell permite consultas como:

```powershell
Get-Printer | Select-Object Name, DriverName, PortName, PrinterStatus
Get-PrintJob -PrinterName 'Impresora-LAB'
Get-Service Spooler
```

Sustituye el nombre después de identificar la cola real. `Get-PrintJob` puede devolver cero elementos si no hay trabajos; eso no significa que se haya impreso el documento correcto. Un servicio Spooler activo tampoco demuestra que el motor físico esté disponible o que el controlador genere un lenguaje comprendido por el equipo.

Una intervención que reinicia Spooler puede afectar a todas las colas de ese puesto y a trabajos pendientes. Antes de hacerla, registra el impacto y conserva la evidencia necesaria. No publiques una instrucción de borrar todo el directorio de spool como solución automática: puede eliminar trabajos de otras personas y ocultar el problema. En un laboratorio con cola sintética, cancela únicamente el trabajo que has creado y comprueba el resultado.

Si se cambia controlador, documenta procedencia, arquitectura y compatibilidad del sistema. Un controlador universal puede ofrecer menos funciones que uno específico o ser una opción admitida por el fabricante; la decisión depende del requisito. No descargues controladores de repositorios no oficiales porque una búsqueda los presenta primero.

## 6. Consulta en CUPS y separación de escenarios

En Linux con CUPS instalado y configurado, `lpstat -t` resume colas y estado y `lpq -P nombre` consulta trabajos de una cola. Estas herramientas pertenecen al entorno de impresión; una Debian mínima puede no tenerlo instalado. Consulta primero qué paquetes y servicio usa tu instalación antes de aplicar un tutorial de escritorio completo.

Una práctica sencilla usa una impresora virtual o salida a archivo con datos sintéticos, si el entorno del centro la ofrece. El objetivo es distinguir envío, cola y salida; no se instala un servidor de impresión abierto en todas las interfaces de la red. Si se realiza impresión física compartida, delimita clientes, autorización y administración según el diseño del laboratorio.

Para comparar, imprime un documento corto con una sola página, papel y orientación explícitos. Comprueba después si el archivo de salida o la página contiene lo esperado. Los trabajos de pruebas deben identificarse como tales y retirarse por el procedimiento de la cola, sin borrar documentos de terceros. Registra tanto un caso correcto como uno deliberadamente inválido, por ejemplo un nombre de cola inexistente, para interpretar el mensaje.

## 7. Mantenimiento preventivo basado en evidencia

Un calendario útil relaciona tarea, condición, responsable, herramienta, evidencia y criterio de aceptación. «Limpiar cada mes» no define cómo ni por qué. Un equipo de oficina limpia y otro en un taller con polvo necesitan evaluación distinta. El objetivo es mantener refrigeración, conexiones, disponibilidad y vida útil sin desmontar innecesariamente.

| Tarea | Desencadenante orientativo | Evidencia | Condición de cierre |
| --- | --- | --- | --- |
| Revisar refrigeración | Inspección programada o tendencia térmica | Fotos, temperaturas contextualizadas | Ventilación y montaje según fabricante |
| Revisar almacenamiento | Alertas, tendencia o planificación | Copia verificada y telemetría privada | Decisión y recuperación comprobables |
| Revisar consumibles | Calidad o contador del dispositivo | Página de prueba sintética | Impresión legible y sin errores relevantes |
| Revisar cables y docks | Cambios de puesto o desconexiones | Mapa de conexiones | Características requeridas verificadas |
| Revisar firmware | Necesidad documentada o aviso oficial | Modelo, versión, motivo y plan | Cambio admitido y prueba posterior |

El mantenimiento físico se hace con equipo apagado y desconectado conforme a su manual. No se emplean líquidos o aspiradores sin comprobar adecuación a componentes, ni se fuerza el giro de ventiladores con métodos que puedan dañarlos. Las medidas ESD siguen el procedimiento del puesto. Si no se dispone del material o autorización adecuados, se documenta la limitación y se escala.

## 8. Gestión de repuestos y trazabilidad

Un repuesto debe identificarse por compatibilidad, estado y procedencia. Un módulo sin etiqueta o una fuente retirada por un fallo intermitente no se guarda como «conocida buena». Separa material operativo, pendiente de diagnóstico y residuo. Mantén historial de intervención para no reinstalar un componente sospechoso en otro puesto y transferir la avería.

Registra garantía, soporte y documentación de cada activo sin publicar identificadores sensibles. Una sustitución incluye traslado o protección de datos cuando corresponde, verificación de función, actualización del inventario y destino de la pieza retirada. En consumibles y almacenamiento, confidencialidad y RAEE son procesos complementarios: entregar un disco al reciclaje no prueba que sus datos hayan sido tratados adecuadamente.

El stock se decide por criticidad y tiempo de reposición. Mantener muchas piezas incompatibles inmoviliza recursos sin mejorar continuidad. Un conjunto pequeño de cables y adaptadores admitidos puede resolver incidencias más frecuentes que una placa de repuesto que no sirve a la flota. Justifica la propuesta con casos observados y supuestos, no con probabilidades inventadas.

## 9. Tres prácticas adicionales

### P4 · Diagnóstico USB por trayecto

Utiliza un periférico propio no crítico, dos cables admitidos si están disponibles y un puerto directo más un concentrador. Antes de conectar, documenta qué capacidades necesitas. Registra enumeración, topología y funcionamiento con una tarea corta idéntica. Cambia un elemento cada vez y conserva el resto. No uses un dispositivo con datos únicos ni desconectes almacenamiento mientras escribe.

La entrega contiene mapa del trayecto, hipótesis, cuatro observaciones y conclusión. Si todos los casos funcionan, explica qué comprobaste y qué no; no es obligatorio fabricar un fallo. La recuperación consiste en devolver el cableado original y expulsar almacenamiento según procedimiento. Criterios propios: diseño 25 %, control de variables 25 %, evidencia 30 % y conclusión/recuperación 20 %.

### P5 · Incidencia de impresión sin datos personales

Prepara una cola de laboratorio física o virtual acordada con el docente. Crea un documento sintético con una página, título y número de prueba. Registra cola, controlador, puerto y estado inicial. Envía el trabajo y compara aplicación, cola y salida. Introduce un error reversible de configuración de papel en la copia del documento o utiliza una cola de prueba pausada, según lo que permita el entorno.

Debes distinguir el error de contenido/configuración del error de transporte. Antes de cancelar identifica el trabajo concreto y su alcance. Entrega una secuencia de diagnóstico y una prueba final correcta; no reinicies servicios de una infraestructura compartida sin autorización. Criterios: identificación de capas 30 %, pruebas discriminantes 30 %, resolución 20 % y comunicación 20 %.

### P6 · Plan anual de mantenimiento de un aula

Usa una flota ficticia de doce puestos, dos impresoras y cuatro docks. Define criticidad, calendario orientativo, desencadenantes por alertas, responsables, repuestos, tiempo de parada y documentación. Incluye una medida de consumo y una decisión de reparación o sustitución apoyada en supuestos económicos explícitos. No afirmes que una tarea reduce fallos un porcentaje concreto sin datos.

Entrega inventario, matriz de tareas y una orden completa de trabajo de ejemplo. La aceptación exige que otra persona pueda ejecutar la tarea con seguridad, saber cuándo detenerse y comprobar el resultado. Rúbrica: cobertura de funciones 25 %, procedimientos 25 %, criterios verificables 25 %, coste/continuidad 15 % y trazabilidad 10 %.

## Fuentes primarias

- [USB-IF: documentos](https://www.usb.org/documents): terminología y especificaciones de interfaces; consultar además el manual del equipo y cable.
- [lsusb en Debian](https://manpages.debian.org/trixie/usbutils/lsusb.8.en.html): inspección de dispositivos y topología.
- [Microsoft PrintManagement](https://learn.microsoft.com/powershell/module/printmanagement/): consultas y administración de impresoras y trabajos.
- [OpenPrinting CUPS](https://openprinting.github.io/cups/): arquitectura y herramientas del sistema de impresión.
- [MITECO: aparatos eléctricos y electrónicos](https://www.miteco.gob.es/es/calidad-y-evaluacion-ambiental/temas/prevencion-y-gestion-residuos/flujos/aparatos-electr.html): gestión del flujo de residuos.
