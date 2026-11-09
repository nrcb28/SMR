# 7. Criptografía aplicada, copias y continuidad comprobable

[Índice del módulo](README.md) · [Guía inicial de copias](02-guia-tecnica.md) · [Riesgos y BIA](05-riesgos-bia-y-diseno-de-controles.md)

## 7.1 Elegir la propiedad que se necesita

Hash, cifrado, firma y certificado responden a preguntas distintas. Un hash permite comparar una representación de datos con una referencia. El cifrado protege confidencialidad bajo un modelo y unas claves. Una firma vincula una operación criptográfica con una clave y permite comprobar integridad y origen de esa firma dentro de una relación de confianza. Un certificado relaciona una clave pública con información y una autoridad, según extensiones y políticas. No intercambies esas funciones por el hecho de que todas produzcan cadenas difíciles de leer.

Si un documento y su archivo de hashes se almacenan con los mismos permisos y un atacante puede cambiar ambos, una comparación correcta no demuestra que el documento sea el original autorizado. Si el disco está cifrado y una sesión legítima lo tiene abierto, el cifrado no impide que esa sesión modifique archivos a los que está autorizada. Si una web tiene HTTPS, el canal se protege según la validación, pero el servidor todavía puede ejecutar una aplicación defectuosa o conceder acceso excesivo.

Empieza por el adversario o fallo que se quiere considerar. Para un portátil apagado perdido, cifrado de almacenamiento y custodia de claves son relevantes. Para borrado accidental desde una cuenta editora, una copia recuperable protege una propiedad distinta. Para verificar software descargado, una firma comprobada con una clave confiable aporta información que un hash publicado por un canal controlado por el mismo atacante podría no aportar.

## 7.2 Hashes y referencias de confianza

Crea tres archivos sintéticos pequeños en una carpeta de laboratorio nueva y conserva un listado de hashes antes de modificarlos. `sha256sum` calcula un resumen; `sha256sum -c` comprueba entradas de un archivo de referencias. Ambos leen datos y no convierten por sí mismos el listado en una evidencia autenticada.

```bash
mkdir -p "$HOME/lab-integridad-smr"
printf 'Documento de pruebas A\n' > "$HOME/lab-integridad-smr/a.txt"
printf 'Documento de pruebas B\n' > "$HOME/lab-integridad-smr/b.txt"
cd "$HOME/lab-integridad-smr"
sha256sum a.txt b.txt > referencias.sha256
sha256sum -c referencias.sha256
```

Utiliza una carpeta nueva; si ya existe, inspecciona antes los archivos para no sobrescribir trabajo previo. Copia la referencia a un lugar protegido que no se modifique durante el ensayo. Cambia después una sola línea de `a.txt` y repite la comprobación. Se espera que cambie el resultado de A, mientras B conserva coincidencia. Registra salida y código de retorno como evidencia real cuando ejecutes el laboratorio.

Un hash de una carpeta no se obtiene concatenando nombres sin un criterio. El listado debe establecer qué archivos se incluyen, rutas, codificación y tratamiento de cambios concurrentes. Para una copia, la herramienta puede utilizar su propio catálogo e integridad por bloques; eso no elimina la prueba de restauración del archivo que necesita el usuario.

## 7.3 Contraseñas, derivación y gestión de claves

Una contraseña humana suele tener menos entropía que una clave aleatoria del mismo tamaño expresado. Un esquema de almacenamiento de contraseñas emplea una función de derivación apropiada, sal y parámetros de coste; un hash rápido genérico no ofrece la misma resistencia ante prueba masiva fuera de línea. No desarrolles tu propio sistema de contraseñas para una aplicación real a partir de este ejercicio.

La sal impide que contraseñas iguales compartan necesariamente la misma representación y dificulta reutilizar cálculos entre muchas entradas. No es un secreto que deba guardarse como una contraseña. El coste temporal y de memoria dificulta cada intento, pero debe ajustarse a la plataforma y revisarse con el software de autenticación elegido. Copiar parámetros sin medir puede saturar un servidor pequeño o dejar un coste insuficiente.

La gestión de claves incluye generación, almacenamiento, acceso, copia, rotación, revocación y destrucción cuando corresponda. Si se pierde la única clave de un backup cifrado, los datos pueden volverse irrecuperables aun cuando todos los archivos del repositorio estén presentes. Si se guarda la contraseña del backup junto a una copia accesible por cualquiera, la confidencialidad queda limitada por ese acceso.

Separa credenciales de administración ordinaria y acceso a copias cuando el diseño lo permita. Una cuenta con capacidad de modificar origen y borrar todas las copias representa una causa común de pérdida. La separación técnica requiere verificar permisos efectivos: llamar «usuario backup» a una cuenta que sigue siendo administradora de todo no crea aislamiento.

## 7.4 PKI y TLS durante el ciclo de vida

La validación TLS no consiste únicamente en comprobar que un certificado no ha caducado. El cliente debe establecer confianza con la cadena apropiada, relacionar el nombre solicitado con las identidades del certificado, comprobar fechas y aplicar su política. Las aplicaciones pueden utilizar almacenes distintos: navegador, sistema operativo, biblioteca o paquete de CA propio. Por ello un navegador confiado no demuestra que una tarea automatizada o la HTTP API de un CMS confíen igual.

En el laboratorio se usan nombres `.test` y una CA interna exclusiva. Su clave privada queda fuera del árbol web y del repositorio. Los clientes reciben sólo el certificado público de la CA por un canal de prácticas controlado. La operación se retira al finalizar si esa confianza ya no es necesaria. Un certificado público de CA no es una contraseña, pero confiar en una CA sí cambia qué identidades acepta el cliente y debe ser una decisión consciente.

Para examinar el certificado que presenta un servicio de laboratorio:

```bash
openssl s_client -connect 192.168.56.10:443 \
  -servername srv01.aula.test -showcerts </dev/null
```

Este comando permite observar cadena e información de negociación; sus opciones y la salida deben interpretarse. La presencia de certificados en la salida no demuestra que el cliente haya validado nombre y confianza según el requisito. Para una petición real usa un cliente con CA explícita y nombre correcto, como en la guía de servicios. No conviertas `-k` o desactivar verificación en la solución final de una alerta.

Planifica renovación antes del vencimiento con responsable, archivo, recarga y prueba. Cambiar el archivo sin recargar el servicio puede dejar en uso el certificado anterior; recargar sin verificar permisos de la clave puede impedir que arranque. Registra huella, emisor, SAN y fechas antes/después. La rotación de certificado no exige necesariamente reutilizar indefinidamente la misma clave; el diseño de claves debe contemplar cuándo regenerarla.

## 7.5 Backup: conjuntos, consistencia y separación

La copia se diseña por conjuntos de recuperación. Una aplicación web puede necesitar código, contenido subido, configuración, base de datos y secretos coherentes. Copiar cada parte en momentos incompatibles puede producir un estado que nunca existió como conjunto. La herramienta de base de datos o un procedimiento de quiescencia apropiado proporciona mecanismos de consistencia que una copia de archivos abiertos no garantiza universalmente.

El principio didáctico 3-2-1 recuerda mantener varias copias, diversidad de soportes o medios y una ubicación separada. No es una certificación ni una fórmula suficiente para todas las amenazas. Evalúa también aislamiento, inmutabilidad cuando sea real y verificada, credenciales, retención, claves y restauración. Una copia «en nube» accesible con las mismas credenciales comprometidas puede compartir la causa del incidente.

La retención determina qué puntos históricos se mantienen. Una copia diaria que se reemplaza cada día no permite recuperar un documento cuyo error se descubre una semana después. Una retención larga sin control puede aumentar coste y datos conservados indebidamente. Relaciona periodos con detección, obligaciones, necesidades y capacidad, y documenta cómo se aplican las eliminaciones autorizadas sin afectar las copias requeridas.

## 7.6 Restauración con restic: leer, comprobar y recuperar

La guía inicial explica cómo crear el repositorio cifrado de laboratorio. Aquí se parte de ese repositorio ya existente, un conjunto pequeño sintético y acceso a su contraseña mediante un mecanismo privado. No se inicializa encima de un repositorio desconocido ni se publican secretos. `restic snapshots` enumera puntos; `restic check` comprueba estructuras y `--read-data` añade lectura de los datos del repositorio, con coste que debe planificarse.

```bash
restic -r /ruta/verificada/repositorio-lab snapshots
restic -r /ruta/verificada/repositorio-lab check --read-data
```

`/ruta/verificada/repositorio-lab` es un marcador que debe sustituirse por el destino realmente montado y comprobado. La comprobación no restaura la aplicación ni demuestra que la contraseña seguirá disponible en un incidente. Con un repositorio grande, leer todos los datos puede consumir tiempo y transferencia; en esta práctica se utilizan pocos archivos para poder completar y entender el ensayo.

Selecciona un ID concreto de snapshot, no «el más reciente» sin revisar sus fechas y contenido. Prepara un destino nuevo y separado, verifica espacio y ejecuta la restauración con la sintaxis de tu versión:

```bash
restic -r /ruta/verificada/repositorio-lab restore ID_REVISADO \
  --target /ruta/verificada/restauracion-nueva
```

Después localiza el árbol restaurado y compara archivos y metadatos con la referencia. No asumas la ruta final sin examinar cómo la herramienta conserva la estructura original. Publica un recurso temporal únicamente si es necesario para probar autorización y documenta su retirada. No ejecutes políticas `forget` o `prune` durante la práctica de restauración: eliminan puntos o datos según su función y requieren un procedimiento distinto, con catálogo y retención revisados.

## 7.7 Ejercicios de RPO y RTO

**Ejercicio A.** Hay copias completas utilizables a las 00:00, 06:00, 12:00 y 18:00. El origen se pierde a las 17:20 y no existe otro mecanismo de recuperación de cambios. El último punto disponible es 12:00; se pierden hasta 5 horas y 20 minutos. Un objetivo RPO de cuatro horas no se cumple. Haber programado una copia a las 18:00 no ayuda a un incidente anterior a esa copia.

**Ejercicio B.** Se cambia a puntos válidos cada tres horas y el incidente ocurre otra vez a las 17:20. El punto de 15:00 limita la pérdida a 2 horas y 20 minutos, siempre que esa copia haya terminado correctamente y sea recuperable. El calendario teórico no equivale a evidencia de ejecución; una tarea fallida puede devolver el último punto real a una hora anterior.

**Ejercicio C.** Se restauran 160 GiB a un ritmo efectivo medido de 75 MiB/s. La transferencia requiere `160 × 1024 / 75 = 2184,53 s`, unos 36,41 minutos. Si preparación e identificación consumen 15 minutos y verificación/habilitación otros 20, el tiempo total es aproximadamente 71,41 minutos. Cumple un objetivo de 90 en ese ensayo, pero no demuestra rendimiento idéntico con otra carga o destino.

**Ejercicio D.** Se pretende reducir el total anterior a 45 minutos aumentando sólo el caudal al doble. La transferencia bajaría aproximadamente a 18,20 minutos, pero las otras fases siguen sumando 35. El total sería 53,20 y el objetivo no se cumple. La mejora debe abordar también preparación y validación sin eliminarlas. Presentar sólo el tiempo de transferencia como RTO ocultaría ese problema.

## 7.8 Laboratorio de continuidad completa

### Diseño

Selecciona diez documentos sintéticos y una configuración de servicio sin secretos. Asigna RPO de 24 horas y RTO de 60 minutos como hipótesis del ejercicio. Diseña dos puntos de recuperación y un destino independiente. Si el hardware sólo permite simular separación, declara esa limitación y no afirmes protección frente a pérdida física del anfitrión.

### Ejecución y aceptación

1. Inventaría conjunto, identidades, permisos, rutas y herramienta.
2. Crea la copia inicial y comprueba su catálogo.
3. Modifica dos documentos, realiza una segunda copia y anota ambas fechas.
4. Decide un escenario de pérdida o alteración ficticia sin borrar el original.
5. Elige el punto apropiado justificando integridad y pérdida temporal.
6. Restaura a un destino nuevo; comprueba hashes, contenido legible y metadatos.
7. Prueba una operación autorizada desde cliente y otra que deba denegarse.
8. Mide las fases y compara objetivos con resultados reales.
9. Describe cómo se recuperaría la clave si el equipo de administración no estuviera disponible.

**Solución razonada:** no siempre se elige el snapshot más reciente. Si la alteración aparece antes de ese punto y no debe recuperarse, se necesita uno anterior y se acepta una pérdida mayor, documentada y autorizada. Si se recuperan documentos pero no permisos, la operación no cumple el requisito de servicio completo.

**Entregables:** política, catálogo, procedimiento, matriz, mediciones y limitaciones. **Rúbrica propia:** coherencia del diseño 20 %, integridad y permisos 30 %, recuperación funcional 30 % y análisis temporal/custodia 20 %.

## Referencias primarias

- [GNU Coreutils: sha2 utilities](https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html).
- [OpenSSL: documentación](https://docs.openssl.org/).
- [OpenSSH: manuales](https://www.openssh.com/manual.html).
- [restic: documentación](https://restic.readthedocs.io/en/stable/).
- [restic: restauración](https://restic.readthedocs.io/en/stable/050_restore.html).
- [restic: comprobación del repositorio](https://restic.readthedocs.io/en/stable/045_working_with_repos.html).
