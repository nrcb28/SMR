# Simulacro práctico de primero: puesto, red y documentación

[Cuaderno](README.md) · [Primero](../primero/README.md) · [Memoria](../recursos/plantillas/memoria-practica.md)

## 1. Contexto y forma de realizarlo

Este simulacro es una actividad didáctica original que combina Montaje, Sistemas monopuesto, Redes locales, Ofimática e IPE I. No es un examen oficial ni reproduce la programación de un centro. Se propone realizarlo en tres sesiones de 60 minutos, adaptando tiempos a los equipos y conocimientos disponibles.

Una pequeña aula ficticia necesita cuatro puestos para ofimática, navegación y prácticas de administración con una VM ligera. Debes justificar la selección del equipo, preparar una VM, organizar archivos con permisos, comprobar conectividad y entregar una memoria con presupuesto y prevención. El caso no exige comprar componentes ni usar datos personales.

Para las tareas de sistema utiliza una VM nueva o una copia destinada al examen. Conserva el laboratorio base con `srv01` en `.56.10/24` y `cli01` en `.56.20/24`. La interfaz LAB no tiene gateway. Una NIC NAT distinta puede proporcionar acceso a repositorios oficiales. El ejercicio de diseño de subredes usa otra topología y se resuelve como cálculo, sin modificar esa LAB.

Oculta las secciones de solución durante el primer intento. Antes de ejecutar, redacta el estado inicial, la copia o instantánea y las acciones que requieren administración. Los comandos son propuestas para una VM Linux de laboratorio; si se realiza una variante en Windows, hay que demostrar las mismas condiciones con sus mecanismos de permisos y evidencia.

## 2. Enunciado: requisitos y entregables

### Bloque A: selección e inventario

Los componentes del presupuesto son categorías ficticias, con compatibilidad ya documentada en las fichas que debe aportar el estudiante. Los importes son supuestos para practicar cálculos, no precios de mercado. Cada puesto necesita placa, CPU, memoria, almacenamiento, fuente, caja y periféricos.

1. Describe la compatibilidad que comprobarías para CPU/placa, memoria, almacenamiento y fuente. Identifica dónde consultarías cada dato.
2. Justifica una configuración con 16 GiB de RAM y almacenamiento de 512 GB nominales, indicando límites de la comparación GB/GiB.
3. Entrega inventario de la VM o equipo observado sin números de serie, contraseñas ni información personal.
4. Explica dos comprobaciones de salud o funcionamiento y qué no permiten concluir.

### Bloque B: sistema y permisos

En una VM Debian del laboratorio crea un directorio exclusivo de la actividad. Una cuenta editora debe crear y modificar archivos; otra lectora debe leerlos sin modificarlos; una identidad ajena debe recibir denegación. No uses acceso universal como solución.

Debes explicar usuarios, grupos, propietario, permisos del directorio y herencia para entradas nuevas. El directorio no debe contener datos anteriores. Comprueba con sesiones o identidades diferentes y guarda el estado de permisos. Crea una copia de tres archivos sintéticos y restaura al menos uno en una ruta distinta, comprobando contenido.

### Bloque C: red y diseño

1. Identifica NIC LAB y NAT, dirección, prefijo y ruta por defecto. Comprueba comunicación hacia el otro equipo y distingue ICMP de una prueba de servicio.
2. Diseña, sobre `10.50.0.0/24`, tres subredes que admitan 90, 30 y 10 puestos respectivamente, más una dirección de router por subred. Reserva una región sin asignar para crecimiento.
3. Calcula red, prefijo, broadcast y rango utilizable de cada segmento. Explica por qué un `/27` no basta para el segmento de treinta puestos con router.
4. Dibuja la diferencia entre plano físico y lógico. No atribuyas routing o VLAN a un switch virtual que no los implementa.

### Bloque D: ofimática y presupuesto

Importa [presupuesto-primero.csv](datos/presupuesto-primero.csv), cuyo delimitador es punto y coma y cuyos precios usan punto decimal en el archivo de intercambio. Si tu aplicación usa coma decimal, configura la importación; no conviertas importes en texto inadvertidamente.

Calcula subtotal por línea y total, separa las entradas de las fórmulas e incluye una comprobación manual. Añade un escenario donde el precio de memoria suba un 10 % y una reserva presupuestaria que represente exactamente un 10 % del subtotal de cada escenario. No se calcula IVA: es una comparación didáctica de costes antes de impuestos.

Redacta una memoria con estilos, índice automático si la longitud lo requiere, tablas con unidades y capturas explicadas. Exporta a PDF sin perder el archivo editable. La presentación final debe explicar decisiones y evidencias, no contener una captura por diapositiva sin interpretación.

### Bloque E: prevención y comunicación

Identifica al menos seis peligros relacionados con montaje y puesto: electricidad, baterías, manipulación de cargas, postura, pantallas y cableado, entre otros posibles. Propón medidas relacionadas con cada peligro y una forma de comprobar su implantación. Describe cuándo debes detener una tarea y pedir supervisión.

Escribe una comunicación breve a la persona usuaria: qué se ha preparado, qué puede hacer, cómo pedir soporte y qué prueba confirma que los archivos se recuperan. El lenguaje debe ser comprensible y conservar los límites de lo realmente ejecutado.

## 3. Organización del tiempo

En la primera sesión, lee requisitos, diseña y registra línea base. Dedica la segunda a configuración, pruebas y recuperación. Reserva la tercera para presupuesto, memoria y defensa. La instalación del SO puede prepararse de antemano si el centro decide evaluar administración y no instalación.

No ejecutes apresuradamente un comando cuyo destino no has identificado. Si una tarea queda pendiente, explica el estado y el siguiente paso verificable. Un sistema mal protegido pero aparentemente terminado no merece mejor valoración técnica que una configuración incompleta cuyo riesgo se ha reconocido y acotado.

## 4. Solución comentada: hardware y capacidad

La compatibilidad se justifica por documentación del fabricante: socket y revisión de firmware para CPU, tipo y capacidad de RAM admitidos, formato/conector/protocolo de almacenamiento, tamaño físico, conectores de alimentación y margen térmico. Que un conector encaje no garantiza todas las funciones: M.2 puede describir formatos con distintos protocolos.

Con 16 GiB, una VM de 4 GiB deja nominalmente 12 GiB para anfitrión y otras cargas, pero hay sobrecarga y consumo de aplicaciones. No se afirma que cualquier conjunto de aplicaciones funcione bien por esa resta: se debe observar presión de memoria y actividad. La decisión de ampliar se apoya en carga, capacidad y rendimiento sostenido.

Un dispositivo de 512 GB nominales representa aproximadamente 476,84 GiB antes de otras reservas. El tamaño del disco virtual puede mostrarse con otra unidad; registra bytes o la unidad exacta. Capacidad libre y salud son dimensiones distintas. SMART, cuando está disponible en hardware físico, aporta telemetría y no una garantía contra fallos; en una VM puede no exponer el dispositivo real.

Una memoria correcta relaciona cada comprobación con una conclusión limitada. Un arranque correcto demuestra que ese arranque funciona, pero no valida todos los módulos de RAM bajo cualquier carga. Un benchmark corto sin controlar caché tampoco representa la experiencia de toda una jornada.

## 5. Solución comentada: permisos Linux

Este ejemplo presupone que no existen las cuentas y grupos de examen ni `/srv/examen-smr1`. Comprueba con `getent` y consulta la ruta. Si existen, detente y revisa su finalidad; no reutilices objetos de otra actividad. Se necesita `sudo` y el paquete `acl` preparado según la guía de sistemas.

En la VM exclusiva se pueden crear grupos `ex1_editores` y `ex1_lectores` y cuentas `ex1_editor`, `ex1_lector` y `ex1_ajeno`, sin permisos administrativos. La creación de cuentas se realiza con el procedimiento ya explicado en [Sistemas monopuesto](../primero/sistemas-operativos-monopuesto/README.md). La asignación conceptual es:

| Cuenta | Grupo funcional | Operaciones esperadas |
| --- | --- | --- |
| `ex1_editor` | `ex1_editores` | Leer, crear y modificar archivos de la actividad |
| `ex1_lector` | `ex1_lectores` | Listar y leer, sin crear ni modificar |
| `ex1_ajeno` | Ninguno de esos grupos | Sin acceso al contenido |

Configuración del directorio nuevo, una vez creadas y verificadas las identidades:

```bash
sudo install -d -o root -g ex1_editores -m 2770 /srv/examen-smr1
sudo setfacl -m g:ex1_lectores:r-x,m::rwx,o::--- /srv/examen-smr1
sudo setfacl -m d:u::rwx,d:g::rwx,d:g:ex1_lectores:r-x,d:m::rwx,d:o::--- /srv/examen-smr1
getfacl /srv/examen-smr1
namei -l /srv/examen-smr1
```

`setgid` en el directorio favorece que nuevas entradas conserven su grupo. La ACL de acceso concede lectura y recorrido al grupo lector; la ACL por defecto define herencia para entradas nuevas. La máscara limita permisos efectivos de entradas de grupo y usuarios/grupos nombrados; debe interpretarse con la salida real, no sólo con un modo numérico.

Crear un archivo regular no lo convierte automáticamente en ejecutable porque una ACL por defecto permita `x`: el modo solicitado al crearlo limita los permisos resultantes. Comprueba entradas reales. Los directorios necesitan recorrido para llegar a archivos interiores, incluso si el archivo parece permitir lectura.

Prueba con identidades explícitas:

```bash
sudo -u ex1_editor sh -c 'printf "Dato sintético\n" > /srv/examen-smr1/ensayo.txt'
sudo -u ex1_lector cat /srv/examen-smr1/ensayo.txt
sudo -u ex1_lector sh -c 'printf "Cambio\n" >> /srv/examen-smr1/ensayo.txt'
sudo -u ex1_ajeno cat /srv/examen-smr1/ensayo.txt
```

Las dos últimas acciones deben ser denegadas. No ejecutes todas las operaciones como root y concluyas que los permisos están correctos: root no representa a esos usuarios. La memoria debe presentar el resultado real, no pegar literalmente la expectativa.

Para recuperación, utiliza el procedimiento de backup de la guía, registra qué metadatos conserva y restaura en otra ruta. Un hash igual comprueba contenido de ese archivo; repite además el acceso con identidades para evaluar autorización.

## 6. Solución comentada: direccionamiento

Para noventa puestos más router se necesitan 91 direcciones utilizables. `/25` ofrece 126 en una subred IPv4 ordinaria. Para treinta más router se necesitan 31; `/27` sólo ofrece treinta, así que se elige `/26`. Para diez más router se necesitan once; `/28` ofrece catorce.

Asignando de mayor a menor:

| Segmento | Red/prefijo | Hosts utilizables | Broadcast | Ejemplo de IP de router |
| --- | --- | --- | --- | --- |
| 90 puestos + router | `10.50.0.0/25` | `.1–.126` | `.127` | `.1` |
| 30 puestos + router | `10.50.0.128/26` | `.129–.190` | `.191` | `.129` |
| 10 puestos + router | `10.50.0.192/28` | `.193–.206` | `.207` | `.193` |

Queda sin asignar `.208–.255`, que puede representarse como `10.50.0.208/28` y `10.50.0.224/27` si se requieren prefijos alineados. No se representa ese intervalo irregular como un único `/27` que empiece en `.208`, porque no es una frontera válida para ese tamaño.

El router es un elemento del diseño calculado, no una función que haya aparecido en LAB. Al documentar la VM se mantiene su `/24` y ausencia de gateway en LAB. La existencia de una ruta por defecto vía NAT no implica que todo tráfico pase por NAT: destinos conectados tienen rutas más específicas.

Para comprobar dirección y ruta utiliza `ip -br address`, `ip route` y `ip route get 192.168.56.10` en el cliente Linux. Un ping exitoso demuestra respuesta ICMP, pero no prueba que un servidor web o DNS esté escuchando. La prueba de servicio debe realizarse sólo si ese servicio forma parte del ejercicio y está preparado.

## 7. Solución comentada: presupuesto y hoja de cálculo

Los costes sintéticos por puesto son: placa 90 €, CPU 110 €, memoria 45 €, almacenamiento 42 €, fuente 55 €, caja 35 € y periféricos 20 €. La suma es 397 €. Cuatro puestos suman 1.588 €. Se añaden repuestos por 70 € y switch por 110 €, de modo que el subtotal general es 1.768 €.

La reserva del 10 % del subtotal es 176,80 €; el presupuesto con esa reserva asciende a 1.944,80 €. Esa reserva equivale al 10 % del subtotal, no al 10 % del total final. Si el requisito pidiera que la reserva fuera el 10 % del total, la ecuación sería distinta: `total = subtotal / 0,90`.

En el escenario de memoria, su precio sube de 45 a 49,50 € por puesto. La diferencia para cuatro es 18 €. El nuevo subtotal es 1.786 €, la reserva 178,60 € y el total 1.964,60 €. No aumentan los demás componentes porque el supuesto sólo cambia memoria.

En Calc, con cantidad en B y precio en C, una línea usa `=B2*C2`. Para una tasa de reserva situada en una celda de entrada, emplea referencia absoluta cuando copies la fórmula. Los separadores de argumentos y nombres de función dependen del idioma; comprueba el resultado con la aritmética manual de una línea y el total.

**Errores que deben detectarse:** precios importados como texto, suma que omite la última fila, referencia a una celda desplazada, porcentaje escrito como diez en lugar de 10 % y doble aplicación de la reserva. La hoja debe hacer visibles sus entradas y escenarios para que otra persona los revise.

## 8. Solución comentada: prevención

Una respuesta suficiente relaciona peligro, daño potencial, medida, responsable y comprobación. Para cableado de paso, la medida puede ser canalización y orden con inspección, no simplemente «tener cuidado». Para manipulación de equipos, se planifica el movimiento, peso y ayudas; una descripción escolar no sustituye formación preventiva.

Para electricidad, la intervención se limita a tareas autorizadas y equipos desconectados según procedimiento. No se abren fuentes de alimentación ni se asume que desenchufar elimina todos los peligros internos. Una batería hinchada o dañada exige detener la tarea, aislar el área según el protocolo del centro y solicitar intervención competente; no se prueba perforándola o forzando su carcasa.

Para PVD se revisan disposición de pantalla, mobiliario, reflejos, organización de tareas y ajustes a la persona. La prevención no se reduce a una única altura universal de silla. Consulta [IPE I](../primero/itinerario-personal-para-la-empleabilidad-i/README.md) y sus fuentes INSST para criterios técnicos.

## 9. Defensa oral y preguntas razonadas

**¿Por qué has reservado una dirección para router en el diseño y no has configurado gateway en LAB?** Porque son escenarios distintos: el cálculo incluye routing futuro; LAB es un segmento conectado sin router definido. Documentar esa diferencia evita parámetros ficticios.

**¿Cómo demuestras que tu lectura correcta no se debe a privilegios administrativos?** Ejecutando la prueba con la identidad lectora y mostrando grupos/sesión efectiva. El propietario de una captura no prueba por sí solo qué credencial utilizó una conexión.

**¿Por qué conservas el documento editable además del PDF?** El PDF facilita distribución, pero la fuente permite revisar estilos, fórmulas y cambios. Ambos deben conservar versión y correspondencia; modificar el editable exige regenerar la publicación.

**¿Qué harías si una operación no se puede probar por falta de equipo físico?** Documentaría el límite y distinguiría verificación de VM, revisión de ficha y prueba física pendiente. No presentaría una salida sintética como observación del hardware.

**¿Por qué no eliges un SSD sólo por velocidad anunciada?** Porque importan capacidad, interfaz, compatibilidad, carga, latencia, rendimiento sostenido, resistencia, soporte y recuperación. La necesidad del puesto determina qué diferencias son relevantes.

## 10. Rúbrica y criterios de aceptación

| Área | Peso didáctico | Evidencia principal |
| --- | ---: | --- |
| Compatibilidad e inventario | 15 % | Selección justificada y capacidades con unidades |
| Administración y permisos | 25 % | Matriz de identidades y resultados positivos/negativos |
| Red y direccionamiento | 20 % | Configuración observada y diseño sin solapamientos |
| Hoja y memoria | 20 % | Fórmulas trazables, escenarios correctos y documento legible |
| Recuperación | 10 % | Archivo restaurado y contenido contrastado |
| Prevención y defensa | 10 % | Medidas ligadas al riesgo y explicación de límites |

La entrega incluye memoria editable y PDF, hoja de cálculo, CSV fuente, diagrama, extractos sanitizados y archivos de configuración de la actividad si los hay. No incluye imágenes de VM, contraseñas ni claves privadas. Una rúbrica propia no sustituye las reglas de evaluación del centro.

Al repetir el simulacro, cambia cantidades y nombres de los datos sintéticos. Si sólo puedes reproducir los valores originales, vuelve al fundamento que permite obtener la solución. Evalúa especialmente si has explicado la evidencia y si otra persona puede repetir la comprobación con un estado inicial conocido.
