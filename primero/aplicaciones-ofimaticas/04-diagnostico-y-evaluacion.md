# Diagnóstico, evaluación y soluciones razonadas

## 1. Método de soporte

Conserva una copia y reproduce el problema con el menor archivo posible. Registra aplicación, versión, formato, configuración regional y pasos. Determina si el fallo pertenece a los datos, al documento, al perfil de usuario o al entorno. Cambiar simultáneamente formato, versión y plantilla impide saber qué resolvió el problema.

Cuando pruebes un perfil limpio, utiliza el procedimiento de modo seguro de LibreOffice y conserva los datos originales. Un perfil nuevo puede ayudar a aislar extensiones o ajustes, pero no convierte automáticamente un archivo corrupto en uno válido. Si el problema sólo ocurre en un documento, prueba a copiar una parte pequeña en un archivo nuevo para localizar el elemento afectado.

| Síntoma | Hipótesis | Comprobación útil | Corrección coherente |
| --- | --- | --- | --- |
| Un título no aparece en el índice | Estilo o nivel de esquema incorrecto | Navegador y propiedades del párrafo | Aplicar estilo/nivel y actualizar índice |
| Página en blanco inesperada | Salto, estilo o página par/impar | Mostrar marcas y revisar salto | Ajustar la regla de paginación |
| La suma ignora precios | Números almacenados como texto | `ESNUMERO` y origen CSV | Reimportar/converter con región correcta |
| La fórmula cambia el IVA al copiar | Referencia relativa en el parámetro | Inspeccionar fórmulas de filas contiguas | Fijar `$L$2` |
| `#N/D` en búsqueda | Clave ausente o diferencia de tipo/espacios | Comparar longitud, texto y criterio exacto | Normalizar claves y tratar ausencia |
| Función desconocida | Versión o nombre no soportado | Asistente y versión receptora | Usar alternativa o entorno compatible |
| Tabla dinámica muestra recuento | Campo numérico importado como texto | Tipo en origen y función de agregado | Corregir origen y actualizar |
| Base rechaza una incidencia | Clave o restricción incumplida | Mensaje y registro referenciado | Corregir el dato, no quitar integridad |
| Formulario muestra equipo equivocado | Enlace principal/subformulario erróneo | Campos maestros y subordinados | Enlazar por la clave correcta |
| Vídeo no funciona en otro equipo | Vínculo externo o códec ausente | Ubicación del recurso y pistas | Incrustar/distribuir y elegir formato compatible |
| PDF pierde estructura | Exportación sin etiquetas o fuente mal construida | Marcadores, lectura y selección | Corregir origen y volver a exportar |

## 2. Recuperación de archivos

No trabajes directamente sobre la única copia dañada. Guarda copia byte a byte antes de probar recuperación automática. Si la suite propone recuperar una versión, compara contenido y fecha con el original; un archivo que abre puede haber perdido objetos o últimas modificaciones.

En formatos basados en ZIP, una inspección del contenedor puede ayudar a determinar si faltan componentes, pero editar XML manualmente es una operación especializada y debe hacerse sobre copia. No publiques el contenedor como incidencia si incluye datos privados. Para una base incrustada, una copia realizada con la aplicación abierta puede ser inconsistente; repite la copia con el archivo cerrado y comprueba tablas y relaciones.

Una política de recuperación necesita objetivos: cuánto trabajo se puede perder y cuánto tiempo puede tardarse en reanudar. El autoguardado y la recuperación de sesión no sustituyen copias externas ni un historial. Ensaya la restauración de una versión conocida antes de depender de ella.

## 3. Preguntas con respuesta

**1. ¿Por qué no basta con poner un párrafo en negrita y tamaño grande para convertirlo en título?** Porque el aspecto no establece su función estructural. Un índice, un navegador o un lector de pantalla necesitan conocer la jerarquía. Debe aplicarse el estilo o nivel apropiado.

**2. Copio `=D2*E2*$L$2` de F2 a F3. ¿Qué cambia?** Las referencias relativas pasan a D3 y E3; L2 permanece fija. Si la referencia fuera `$L2`, cambiaría su fila a L3. La sintaxis expresa la regla de desplazamiento, no una protección del dato.

**3. Una hoja muestra dos decimales. ¿Todos los cálculos usan dos decimales?** No. El formato afecta a la visualización; la precisión almacenada puede ser mayor. Utiliza una regla explícita de redondeo cuando el procedimiento lo exija y comprueba la diferencia entre sumar importes redondeados y redondear la suma.

**4. ¿Por qué una búsqueda puede fallar si ambos códigos se ven iguales?** Pueden diferir en tipo, espacios invisibles, ceros iniciales o caracteres parecidos. Compara el contenido real y define un contrato de claves. No elimines caracteres automáticamente sin comprobar si forman parte del identificador.

**5. ¿Qué significa que una incidencia tenga `FECHA_CIERRE IS NULL`?** Que no tiene fecha de cierre registrada. No significa 0 ni una fecha vacía convertida a texto. En el modelo de ejemplo la restricción exige que una incidencia Cerrada sí tenga fecha, evitando contradicciones entre estado y cierre.

**6. ¿Por qué usamos `COUNT(I.ID_INCIDENCIA)` después de un `LEFT JOIN`?** Una unión izquierda conserva una fila del equipo aunque no exista incidencia. `COUNT(*)` contaría esa fila; contar una columna no nula de la incidencia omite la ausencia y produce cero.

**7. ¿Basta con guardar en DOCX para garantizar compatibilidad con Word?** No. Se deben revisar fuentes, tablas, campos, saltos y objetos en la aplicación receptora. Conservar el original permite corregir pérdidas de conversión sin acumular transformaciones sucesivas.

**8. ¿Un PDF es siempre accesible?** No. Puede ser una imagen escaneada, carecer de etiquetas o presentar un orden de lectura incorrecto. Deben revisarse tanto el archivo fuente como la exportación y el uso con ayudas técnicas.

**9. ¿Por qué no se debe enviar a cada destinatario el PDF que reúne todas las cartas?** Porque contiene información del resto de destinatarios. La combinación correcta no garantiza una distribución correcta: generación y permisos de entrega son dos controles distintos.

**10. ¿Cómo decido entre hoja y base de datos?** Evalúa relaciones, restricciones, concurrencia y operaciones. Una hoja sirve para analizar un inventario pequeño; una base con claves y permisos resulta más adecuada cuando varios procesos necesitan mantener historial e integridad. No elijas por la apariencia de la tabla.

## 4. Criterio de dominio

Se considera que puedes trabajar con autonomía cuando consigues regenerar una entrega a partir de sus fuentes, explicar una fórmula y una relación, corregir un problema sin ocultarlo y demostrar qué verificaste. Conserva un registro de incidencias con síntoma, hipótesis, prueba, cambio y resultado. Si algo no se probó en una segunda aplicación, indícalo de forma explícita.

La evaluación de este repositorio premia el razonamiento y la reproducibilidad. Un archivo decorativo con cálculos fijados a mano aporta menos evidencia que una solución sencilla cuyos datos, reglas y límites están documentados.
