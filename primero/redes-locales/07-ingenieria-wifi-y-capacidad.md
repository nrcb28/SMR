# Ingeniería Wi-Fi: cobertura, capacidad y pruebas

[Índice de Redes locales](README.md) · [Conmutación y VLAN](06-conmutacion-y-diseno-segmentado.md)

## 1. La pregunta de diseño cambia el resultado

Instalar Wi-Fi para treinta personas que leen documentos no plantea el mismo problema que treinta dispositivos transmitiendo vídeo simultáneamente. Tampoco es equivalente proporcionar cobertura a una esquina de almacén y sostener llamadas mientras una persona camina entre aulas. Define aplicaciones, número de dispositivos activos, movilidad, latencia, autenticación y restricciones del edificio antes de proponer puntos de acceso.

Una persona puede llevar portátil y teléfono; un equipo asociado puede permanecer casi inactivo. Por ello hay que distinguir aforo, dispositivos asociados y dispositivos que compiten por tiempo de transmisión. Dimensionar únicamente por «máximo de clientes soportado por AP» ignora la carga y el tiempo que ocupa cada cliente. Esa cifra del fabricante describe un límite de producto, no una garantía de experiencia.

El diseño físico incluye ubicación y orientación de antenas, altura, alimentación PoE, camino del cable, materiales y entorno. Un AP oculto dentro de un armario metálico puede tener conexión Ethernet perfecta y radio deficiente. La validación debe realizarse con clientes representativos y en condiciones comparables a la utilización prevista, no sólo con el teléfono del técnico debajo del AP.

## 2. Magnitudes que deben mantenerse separadas

**Potencia recibida** suele expresarse en dBm, una escala logarítmica referida a 1 mW. **Diferencia de potencia** se expresa en dB. **SNR** compara señal y ruido en dB. **Tasa física** describe un modo de modulación/transmisión; **throughput** es la tasa útil observada por una aplicación. Ninguna de esas cifras sustituye a las demás.

Para convertir una potencia P en mW: `dBm=10×log10(P)`. De forma inversa, `mW=10^(dBm/10)`. Un aumento de 3 dB aproximadamente duplica potencia;10 dB la multiplica por diez. Eso no implica duplicar o multiplicar por diez la velocidad: la modulación, el ancho de canal y la contención introducen otros límites.

Ejemplo didáctico: una señal de −62 dBm y un ruido de −92 dBm producen un SNR de 30 dB. Otra posición presenta −72 dBm y ruido −80 dBm: SNR de 8 dB. La segunda señal no es simplemente «diez unidades peor»; tanto la potencia recibida como la relación con el ruido han cambiado. Para decidir si sirve a una aplicación necesitas requisitos, tasas usadas, retransmisiones y pruebas reales.

RSSI es un indicador reportado por hardware/software que puede presentarse con escala propia o traducirse a dBm según producto. No compares un porcentaje de «calidad» de un cliente con dBm de otro como si fueran la misma medida. Registra modelo, driver, banda y herramienta, y conserva el valor original además de cualquier transformación.

## 3. Bandas, canales y dominio regulatorio

Las bandas de 2,4 GHz, 5 GHz y 6 GHz ofrecen posibilidades distintas de propagación, canales y compatibilidad. Frecuencias más altas suelen experimentar mayor pérdida de espacio libre a igual distancia y condiciones comparables; los materiales y antenas pueden modificar radicalmente la cobertura interior. No conviertas una regla general en una predicción exacta de metros por pared.

Un canal de 20 MHz y uno de 80 MHz ocupan porciones diferentes del espectro. Agregar canales puede aumentar la tasa posible de un cliente compatible y reducir el número de canales independientes disponibles para reutilización. En un edificio denso, elegir siempre el ancho máximo puede aumentar la competencia con otras celdas y empeorar la experiencia total.

En 2,4 GHz hay fuerte solapamiento entre numerosos canales. Un plan debe evitar combinaciones que interfieran de forma innecesaria y respetar el dominio regulatorio del equipo. En 5 y 6 GHz cambian disponibilidad y condiciones. Algunas frecuencias o clases de dispositivo pueden requerir mecanismos y restricciones específicas; un perfil de otro país no es una forma válida de obtener más canales o potencia.

En España la referencia es el [portal oficial del CNAF](https://digital.gob.es/telecomunicaciones-infraestructuras-digitales/areas-interes/espectro-radioelectrico/cuadro-nacional-atribucion-frecuencias) y la disposición vigente que allí se enlaza. En la consulta de esta ampliación se ha contrastado la [Orden TDF/732/2026 en BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2026-15661), publicada el 17 de julio de 2026. Deben contrastarse notas UN, ubicación, clase de equipo, potencia y mecanismos exigidos para el caso real. Este capítulo no fija una tabla legal de potencias reutilizable sin fecha.

La función DFS, cuando resulte exigida en una banda y clase aplicables, permite detectar ciertos usos prioritarios y cambiar de canal. Una pérdida breve coincidente con un cambio DFS no se diagnostica como avería de cableado sólo porque haya ocurrido durante una llamada. Correlaciona evento del AP, canal anterior/nuevo, cliente y momento. No desactives una obligación regulatoria para ocultar el síntoma.

## 4. Tiempo de aire y efecto de clientes lentos

Wi-Fi comparte el medio. Una radio no ofrece a cada estación una porción independiente del ancho de banda nominal. Debe contender, transmitir, recibir confirmaciones, gestionar tramas de control y, a veces, retransmitir. Un cliente con mala señal puede necesitar tasas más bajas y ocupar más tiempo para transportar los mismos datos.

Modelo simplificado: dos clientes deben enviar cada uno 10 Mbit útiles. Si el primero logra una tasa útil efectiva de 100 Mb/s durante su turno, necesita 0,1 s; si el segundo obtiene 10 Mb/s, necesita 1 s. Sin contar otras cargas, la segunda estación consume diez veces más tiempo para esa tarea. El ejemplo no modela todos los mecanismos 802.11, pero demuestra por qué sumar tasas nominales no dimensiona una celda.

Las retransmisiones consumen tiempo adicional y no siempre se reflejan como pérdida TCP. El enlace puede recuperar una trama antes de que la aplicación detecte un error. Observa tasa de reintentos, ocupación de canal y latencia, no sólo paquetes perdidos en un ping. Una red puede no perder ecos y aun tener tiempos de respuesta inaceptables bajo carga.

Cada SSID y sus mecanismos de anuncio/control producen carga. Crear un SSID distinto para cada pequeño grupo no es gratis. Agrupa requisitos de seguridad y operación de forma razonada y utiliza las funciones apropiadas de identidad y asignación de políticas. El número exacto de SSID recomendable depende del producto, bandas y escenario; evita un límite universal sin referencia al diseño.

## 5. Cobertura y capacidad se verifican por separado

Una medición de cobertura registra señal y calidad en posiciones. Una prueba de capacidad aplica demanda representativa y mide cómo responde la celda. Tener un mapa coloreado con señal suficiente no demuestra que cuarenta clientes puedan realizar la tarea al mismo tiempo. A la inversa, una buena transferencia cerca del AP no demuestra cobertura en todo el aula.

Divide la zona en posiciones reproducibles: centro, esquinas, pasillos y puestos detrás de obstáculos. Indica altura y orientación del cliente. Registra si puertas y mobiliario estaban en posición habitual. La comparación antes/después sólo es útil si se conserva el método. Cambiar cliente, distancia y servidor a la vez impide atribuir mejora al AP.

Prepara un servidor de medición cableado dentro del laboratorio autorizado. Así reduces la dependencia de Internet al medir radio y acceso local. Si el test utiliza un servidor externo, el enlace WAN, rutas y carga remota forman parte del resultado. No llames «velocidad Wi-Fi» a una prueba de Internet sin esa distinción.

Una propuesta didáctica puede requerir que la aplicación descargue un archivo sintético en menos de un umbral elegido y que una llamada de prueba mantenga cierta calidad al moverse. Esos umbrales deben identificarse como requisitos del ejercicio, no como valores oficiales de aprobación del ciclo. Registra valores observados, percentiles o dispersión cuando el tamaño de muestra lo permita.

## 6. Planificación de canales y potencia

Comienza con un plano y una previsión de celdas. Después observa redes propias y ajenas mediante herramientas autorizadas de exploración pasiva. Un escaneo de SSID no detecta por sí solo toda interferencia: otros sistemas y emisiones pueden ocupar el medio sin aparecer como una red 802.11. Un analizador de espectro aporta otra clase de evidencia.

En una zona de alta densidad, considera si anchos menores permiten más reutilización y menor competencia. Evalúa 20, 40 u 80 MHz según banda, clientes y espectro permitido; el resultado correcto no tiene por qué ser el más ancho. La planificación automática del controlador ayuda, pero requiere límites y revisión de resultados, especialmente después de cambiar la disposición del edificio.

Potencia máxima del AP tampoco significa mejor diseño. El cliente puede no transmitir con potencia comparable, de modo que escucha al AP y no consigue responder con calidad. Aumentar la potencia de todos los AP puede ampliar interferencias y favorecer asociaciones lejanas. Analiza simetría del enlace y cómo decide el cliente, además del mapa de cobertura descendente.

Un presupuesto simplificado de enlace combina potencia de transmisión, ganancias de antena y pérdidas. Sirve para explicar tendencias si se declaran hipótesis; en interiores, modelos simplificados no sustituyen medición. No añadas ganancias sin revisar la potencia radiada permitida y la configuración del equipo. Cambiar antena puede alterar tanto cobertura como cumplimiento.

## 7. Roaming, autenticación y experiencia de usuario

Varios AP pueden anunciar el mismo SSID y formar parte de una red extendida, pero el cliente participa de forma decisiva al elegir cuándo y a qué BSSID cambiar. El controlador no garantiza por sí solo que cualquier dispositivo cambie en el punto que dibujó el técnico. Registra capacidades del cliente y funciones de asistencia disponibles.

El cambio de radio puede requerir autenticación, derivación de claves y actualización del camino de datos. Las funciones 802.11k, 802.11v y 802.11r pueden ayudar cuando red y clientes son compatibles y están configurados adecuadamente. No se deben habilitar indiscriminadamente en una infraestructura heterogénea sin pruebas: determinados terminales o configuraciones empresariales pueden presentar problemas de compatibilidad.

Distingue caída de asociación, fallo de autenticación, falta de DHCP y fallo DNS. Un teléfono que muestra «conectado sin Internet» puede haber completado la radio y carecer de DNS, gateway o acceso a la página de comprobación del sistema. Recoge estado de asociación, IP, concesión, resolución y prueba de aplicación en orden.

En autenticación empresarial, el cliente debe validar la identidad del servidor de autenticación conforme a la configuración prevista. Aceptar cualquier certificado para conectar elimina una propiedad de seguridad importante. En redes personales utiliza protocolos y cifrados mantenidos compatibles con el parque; WEP/TKIP no se recuperan como atajo para equipos antiguos.

## 8. Capacidad: ejemplo de aula con hipótesis

Un aula tiene 30 portátiles, de los cuales se espera que 24 realicen una transferencia simultánea de 3 Mb/s útiles. La demanda útil prevista es 72 Mb/s. Añadir un 40% de margen de diseño da 100,8 Mb/s como objetivo interno del escenario. No se convierte esta cifra en una tasa física requerida por una regla fija de eficiencia: se debe contrastar el comportamiento real del hardware y del medio.

Supón dos mediciones sintéticas de planificación, aún no resultados ejecutados: una celda con canal 80 MHz entrega 115 Mb/s útiles en la prueba agregada y muestra latencia alta; dos celdas con canales 20 MHz bien reutilizados entregan 70 Mb/s cada una con reparto razonable. La segunda arquitectura puede servir mejor al conjunto, aunque cada enlace individual anuncie menos tasa física. Hay que añadir coste, cableado, PoE, roaming y capacidad del uplink.

El presupuesto PoE debe calcularse por potencia requerida y capacidad total del switch. Que todos los puertos sean PoE no garantiza suministrar simultáneamente la máxima potencia de cada AP. Registra clase/negociación y consumo esperado según fabricante; las funciones de una radio pueden limitarse si el AP recibe potencia insuficiente.

## 9. Práctica avanzada: estudio reproducible de un aula

**Preparación:** zona autorizada, AP propio, cliente representativo, servidor cableado, plano y permisos. Guarda la configuración y no cambies las redes de terceros. Identifica qué bandas y canales puedes utilizar legalmente con el equipo y su país configurado. Define una aplicación objetivo y un límite de carga que no afecte a otros usuarios.

**Procedimiento:** mide primero sin carga en seis posiciones; repite con una tarea de tráfico controlado. Conserva banda, canal, ancho, señal, ruido si está disponible, tasa usada, reintentos, latencia y transferencia. Cambia una variable: por ejemplo ancho de canal dentro de la banda autorizada. Repite las mismas posiciones y carga, y restaura después la configuración.

**Entregables:** plano, inventario, tabla cruda, hipótesis, comparación, limitaciones y propuesta. Si no se dispone de AP o herramientas, realiza la parte de diseño con datos sintéticos expresamente rotulados y deja pendiente la aceptación radio; no presentes una hoja inventada como estudio de cobertura real.

**Rúbrica propia:**20% requisitos/entorno,25% método reproducible,25% análisis cobertura/capacidad,20% decisiones justificadas y 10% recuperación/confidencialidad. Una tabla de números sin condiciones de medición no permite aprobar el método. La evaluación del centro puede utilizar otros instrumentos y ponderaciones.

## 10. Problemas resueltos y decisiones

**¿−50 dBm garantiza mejor experiencia que −65 dBm?** No. Faltan ruido, ocupación, reintentos, cliente y aplicación. Un canal muy ocupado con señal fuerte puede responder peor que otro menos ocupado.

**¿SNR se expresa en dBm?** No: la relación se expresa en dB. dBm representa potencia respecto a 1 mW. Restar dos niveles en dBm produce una diferencia en dB.

**¿Duplicar AP duplica capacidad?** Sólo puede mejorarla si se añade capacidad de radio reutilizable y recursos de red, sin introducir competencia equivalente o peor. AP contiguos en el mismo canal pueden compartir el mismo medio.

**¿Un cliente conectado a 6 GHz usa necesariamente 80 MHz?** No. Banda, ancho, estándar, capacidad de ambos extremos y política son dimensiones distintas. Deben observarse en el enlace real.

**¿Una prueba cableada elimina todos los límites?** Elimina el tramo radio de ese cliente, pero conserva servidor, disco, CPU, switch, rutas y protocolo. Sirve como referencia, no como velocidad infinita.

## Referencias primarias

- [Ministerio: CNAF y normativa vigente](https://digital.gob.es/telecomunicaciones-infraestructuras-digitales/areas-interes/espectro-radioelectrico/cuadro-nacional-atribucion-frecuencias).
- [Ministerio: uso común del espectro](https://digital.gob.es/telecomunicaciones-infraestructuras-digitales/areas-interes/espectro-radioelectrico/informacion-general/uso-espectro-radioelectrico/comun).
- [HPE Aruba: planificación de radiofrecuencia](https://arubanetworking.hpe.com/techdocs/aos/wifi-design-deploy/design-guides/lpv/rf-planning/).
- [Cisco Meraki: diagnóstico de conexiones y rendimiento](https://documentation.meraki.com/Wireless/Troubleshooting_and_Support/Troubleshooting/Troubleshoot_Wireless_Client_Connection_and_Performance_Issues).
- [IEEE 802.11: grupo de trabajo](https://www.ieee802.org/11/).
- [ESnet: iperf 3 y metodología de pruebas](https://software.es.net/iperf/).
