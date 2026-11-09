# 07 · Almacenamiento, integridad y vida útil

[Índice](README.md) · [Copias y recuperación del puesto](../sistemas-operativos-monopuesto/03-practicas.md)

## 1. Cuatro preguntas diferentes sobre un disco

Un dispositivo puede estar conectado, ser accesible, devolver datos y aun así no ser fiable. Distingue **detección**, **disponibilidad**, **integridad** y **salud estimada**. Detección significa que el controlador lo enumera; disponibilidad, que el sistema puede usarlo cuando se necesita; integridad, que los datos conservan el contenido esperado; salud, que sus indicadores y comportamiento permiten estimar un estado. Ninguna de esas observaciones sustituye por sí sola a las otras.

Un hash correcto de un archivo demuestra coincidencia con el valor de referencia, siempre que esa referencia sea fiable y no haya cambiado. No certifica la salud futura del disco ni explica dónde se produjo una corrupción. Un informe SMART sin alertas tampoco demuestra que el archivo esté intacto: la aplicación pudo sobrescribirlo correctamente desde el punto de vista del dispositivo.

La intervención empieza por valorar los datos. Si hay información única, errores de lectura o sonidos anómalos, se prioriza preservación y recuperación autorizada. Una batería de benchmarks, una prueba extensa o una reparación del sistema de archivos puede aumentar la carga sobre un dispositivo degradado. No conviertas un ejercicio de mantenimiento en un experimento sobre la única copia de datos reales.

## 2. HDD: acceso mecánico y síntomas

En un HDD, localizar datos implica movimiento y espera de rotación. Las peticiones pequeñas dispersas son muy distintas de una lectura secuencial larga. Fragmentación, concurrencia y patrones de acceso influyen en tiempo de respuesta; por eso una tasa secuencial razonable no descarta problemas interactivos. El sistema puede estar esperando muchas operaciones pequeñas aunque el contador de MB/s parezca bajo.

Los sectores pendientes, reasignados o errores no corregibles se interpretan con el significado del fabricante y con su tendencia. Un incremento durante un periodo corto aporta una evidencia distinta de un contador histórico estable. Conserva fecha, horas de encendido, contexto y resultados previos. No compares valores brutos de atributos propietarios como si fueran una escala universal entre marcas.

Un aumento de errores de interfaz puede apuntar al trayecto —cableado, puerto, alimentación o controlador— y no necesariamente a la superficie magnética. Si la conectividad es intermitente, guarda registros y prueba un trayecto conocido compatible siguiendo el procedimiento físico de apagado. Cuando el dispositivo contiene datos importantes, la elección de pruebas se condiciona por la preservación, no por la curiosidad diagnóstica.

## 3. SSD: NAND, controlador y resistencia

Un SSD no necesita movimientos mecánicos para acceder a una dirección, pero tampoco ofrece un rendimiento constante bajo cualquier carga. Su controlador traduce direcciones lógicas, distribuye escrituras, corrige errores y recupera bloques para reutilizarlos. La memoria de caché, la capacidad disponible, la temperatura y el patrón de escritura pueden cambiar el comportamiento observado.

Las escrituras de la aplicación y las escrituras internas no son necesariamente iguales. La amplificación de escritura relaciona datos escritos físicamente con datos solicitados por el anfitrión; su valor depende de diseño y carga. No se calcula con precisión a partir de una sola tasa de copia. El espacio libre y las políticas del dispositivo forman parte del contexto, pero no justifican una receta universal de «dejar siempre exactamente el mismo porcentaje» para cualquier modelo.

La resistencia anunciada mediante TBW o DWPD expresa una condición de especificación y, a menudo, de garantía. No predice una fecha exacta de muerte ni reemplaza copias. Un indicador de porcentaje utilizado es una estimación del fabricante relacionada con desgaste; puede superar un valor nominal sin implicar un apagado inmediato, y un dispositivo con poco desgaste puede fallar por otra causa electrónica.

Ejercicio: un modelo didáctico especifica 600 TBW y recibe 80 GB diarios de escrituras del anfitrión. Una división simplificada da `600000/80 = 7500 días`, unos 20,5 años usando 365 días/año. Esa cuenta **no es una previsión de duración real**: ignora variación de carga, definición de unidades, garantía temporal, retención, fallos de controlador, temperatura y otros límites. Sirve para comprobar que no se confunden GB/día y TB totales.

## 4. NVMe y telemetría contextual

NVMe define registros de salud, errores y estado que las herramientas pueden presentar con nombres normalizados. Entre los datos habituales aparecen temperatura, porcentaje utilizado, unidades escritas, errores de integridad y apagados no seguros. Registra qué herramienta y versión interpretan la información, y confirma que accedes al dispositivo físico previsto.

Un apagado no seguro cuenta una condición de cierre que el dispositivo no recibió como esperaba. No demuestra por sí solo corrupción de archivos; se relaciona con cortes de alimentación, cuelgues o desconexiones y se contrasta con el SO y las aplicaciones. Un incremento de errores de integridad requiere una respuesta de preservación y diagnóstico distinta de una mera cifra histórica sin nuevos eventos.

Las VMs pueden exponer un disco virtual sin telemetría del dispositivo anfitrión. Un resultado «SMART no soportado» en ese contexto no equivale a disco averiado. Algunos puentes USB o controladoras requieren acceso y opciones específicas; no pruebes combinaciones de parámetros a ciegas sobre varios dispositivos. Identifica modelo, interfaz y compatibilidad en el manual de la herramienta.

## 5. Consulta de inventario y conservación de evidencias

En Debian 13, `smartctl` pertenece a `smartmontools`. Instálalo sólo dentro del entorno autorizado si falta. Primero consulta las rutas y capas:

```bash
lsblk -o NAME,TYPE,SIZE,MODEL,TRAN,FSTYPE,MOUNTPOINTS
findmnt -T "$HOME"
```

Después identifica expresamente la ruta del disco de laboratorio. Los siguientes comandos son **consultas**, con una ruta de ejemplo que no debes copiar sin comprobar el objeto:

```bash
sudo smartctl --scan-open
sudo smartctl -x /dev/nvme0
```

La salida puede incluir identificadores y números de serie. Guárdala en evidencias privadas y publica únicamente los campos necesarios sanitizados. No muestres la salida completa de un dispositivo de una empresa sin autorización. El código de salida de `smartctl` utiliza una máscara de bits; un valor distinto de cero exige interpretar el manual, no etiquetar cualquier caso como «comando roto».

En Windows, consultas iniciales posibles son:

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, OperationalStatus, Size
Get-Disk | Select-Object Number, FriendlyName, BusType, PartitionStyle, Size, OperationalStatus
```

Los datos que expone cada proveedor o controlador pueden ser limitados. No conviertas el campo `Healthy` en una garantía universal. Si utilizas herramientas del fabricante, registra procedencia, versión, modelo admitido y si la acción solicitada es consulta, autotest, actualización o borrado. Este capítulo no propone ejecutar borrado seguro ni firmware sobre un disco con datos únicos.

## 6. Integridad de archivos mediante un conjunto sintético

En tu cuenta de una VM, crea una carpeta nueva de prueba con dos documentos pequeños. Si ya existe una carpeta homónima con material ajeno, elige otro nombre. Es una práctica de archivos, no una prueba de desgaste del disco:

```bash
mkdir -p "$HOME/smr-integridad/origen" "$HOME/smr-integridad/copia"
printf '%s\n' 'Documento sintético A' > "$HOME/smr-integridad/origen/a.txt"
printf '%s\n' 'Documento sintético B' > "$HOME/smr-integridad/origen/b.txt"
cd "$HOME/smr-integridad/origen"
sha256sum a.txt b.txt > ../referencia.sha256
cp -- a.txt b.txt ../copia/
cd ../copia
sha256sum -c ../referencia.sha256
```

La comprobación debe indicar coincidencia para ambos archivos antes de introducir cambios. Modifica después **sólo la copia** de `b.txt`, repite y explica por qué cambia el resultado. La prueba no simula un defecto físico: representa una alteración detectable en el contenido. Conserva el origen intacto para demostrar restauración sin depender de memoria o de una captura.

En PowerShell, `Get-FileHash -Algorithm SHA256` calcula el hash de un archivo. Compara también nombre, tamaño y alcance del conjunto: tener un hash correcto de dos archivos no demuestra que se copiaron otros tres que faltaban en la lista. Una estrategia de comprobación debe detectar tanto modificación como ausencia de objetos esperados.

## 7. Priorizar la recuperación y evitar acciones irreversibles

Clasifica la incidencia antes de actuar. Si sólo falta una ruta de montaje, puede bastar reparar configuración después de identificar el volumen. Si hay pérdida de contenido por borrado y no existe copia, continuar escribiendo puede reutilizar espacio o activar mecanismos que dificulten recuperación. Si hay errores físicos, las lecturas repetidas pueden ser costosas y conviene escalar.

La clonación sectorial y la recuperación especializada requieren distinguir con absoluta certeza origen y destino. Intercambiar ambos puede destruir la información buscada. Por eso no se ofrece un comando genérico de clonación destructiva listo para copiar: se exige un procedimiento supervisado, inventario de dispositivos por identidad/capacidad, destino suficiente y validación del plan. Una VM desechable con discos virtuales sintéticos permite aprender esa identificación sin usar datos reales.

Tampoco se ejecuta una reparación del sistema de archivos mientras está montado si la herramienta y el procedimiento no lo admiten. Que una utilidad permita una opción no significa que sea adecuada para el estado actual. Antes de reparar, documenta qué modifica, qué copia existe, cómo accederás a la recuperación y qué resultado indicará éxito o necesidad de escalado.

## 8. Plan de seguimiento y sustitución

Define periodicidad según criticidad, carga y entorno. Conserva una línea base de inventario y telemetría, una revisión de cambios y alertas relacionadas con tendencias. La monitorización no reemplaza el backup; permite detectar señales y coordinar una sustitución antes de una parada cuando las señales existen.

Una propuesta de sustitución relaciona evidencia, impacto y disponibilidad de copia. «Disco con ocho años» es un dato de antigüedad, no una causa técnica suficiente por sí sola; «errores nuevos, lectura intermitente y puesto crítico sin tolerancia de parada» explica mejor la urgencia. Considera también soporte, capacidad y costes de migración. La unidad retirada se custodia según confidencialidad y gestión RAEE, con tratamiento de datos antes de abandonar el control de la organización.

## 9. Caso resuelto: escritura rápida que cae después

Un SSD copia un archivo sintético grande inicialmente a una tasa alta y después baja. Hipótesis: se agota una caché de escritura, aparece limitación térmica, cambia el origen o existe otro proceso que compite. La prueba discriminante registra tasa, temperatura y actividad de ambos extremos a lo largo del tiempo, manteniendo el mismo conjunto y con capacidad suficiente.

Si la temperatura sube y la reducción coincide con el mecanismo documentado del modelo, gana fuerza la hipótesis térmica. Si la caída aparece con cierta cantidad escrita sin esa correlación, investiga caché y comportamiento sostenido. Una única captura al final no separa las causas. La solución puede ser mejorar condiciones térmicas dentro del diseño o elegir un dispositivo adecuado a escritura sostenida; no se afirma que todas las caídas sean avería.

## 10. Práctica ampliada de conservación y decisión

Recibe tres informes sintéticos: un HDD con tendencia de errores de lectura, un SSD con mucho uso estimado pero sin errores nuevos y un disco virtual sin SMART. Construye para cada uno una decisión, las pruebas adicionales que aceptarías y las que evitarías. No asignes una probabilidad inventada de fallo a partir de una sola cifra.

Entrega una tabla de campos interpretados, una política de copia/restauración y un parte de intervención. Aceptación: distinguir hardware físico de virtual, conservar datos, justificar incertidumbre y comprobar un conjunto sintético restaurado. Rúbrica propia: interpretación 30 %, preservación 25 %, prueba de integridad 25 % y decisión/comunicación 20 %.

## Fuentes primarias

- [smartctl en Debian 13](https://manpages.debian.org/trixie/smartmontools/smartctl.8.en.html): consulta, transporte y códigos de salida.
- [NVM Express: especificaciones](https://nvmexpress.org/specifications/): definición de interfaces y registros; la interpretación de resistencia requiere también el fabricante.
- [Microsoft: Get-PhysicalDisk](https://learn.microsoft.com/powershell/module/storage/get-physicaldisk): alcance de los objetos presentados por Storage Management.
- [GNU Coreutils: sumas de comprobación](https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html): funcionamiento y verificación de SHA-2.
- [Microsoft: Get-FileHash](https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash): cálculo de hashes de archivos.
