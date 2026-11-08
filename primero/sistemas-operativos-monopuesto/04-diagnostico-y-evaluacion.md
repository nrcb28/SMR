# 04 · Diagnóstico, casos y evaluación

[Volver al módulo](README.md)

## 1. Diagnosticar por capas

Antes de reparar, identifica si el fallo afecta a arranque, sesión, recurso o aplicación. Registra hora, mensaje exacto, alcance y último cambio conocido. Si únicamente falla una cuenta, compara identidad y configuración antes de reinstalar el SO. Si todas las aplicaciones fallan al escribir, revisa capacidad, montaje y permisos del recurso.

| Incidencia | Consultas iniciales | Interpretación y siguiente decisión |
| --- | --- | --- |
| No arranca tras cambiar firmware | Modo UEFI, orden y dispositivo detectado | Recuperar configuración documentada antes de tocar particiones |
| Linux informa de disco lleno | `df -hT`, `df -i`, montaje y uso por directorios | Distinguir bloques, inodos y archivos abiertos; preservar registros útiles |
| Acceso denegado a un archivo | Identidad, grupos, permisos de cada directorio y ACL | Corregir la regla concreta y probar con cuenta ordinaria |
| Servicio detenido | Estado, unidad y registros del intervalo | Separar configuración inválida, dependencia y fallo del programa |
| Actualización no resuelve | Repositorios, versiones y simulación de operación | No mezclar fuentes incompatibles ni desactivar firmas |
| Lentitud al abrir aplicaciones | CPU, memoria disponible, paginación e I/O | Medir durante el síntoma y comparar con línea base |
| Tarea programada sin copia | Identidad, rutas, entorno, código de salida y destino | Reproducir con el mismo contexto y verificar restauración |

En Linux, `journalctl -b` consulta el arranque actual y `journalctl -u nombre.service` acota una unidad real. En Windows utiliza Visor de eventos y el historial de la tarea o componente. Filtra por tiempo y relación con el síntoma; el primer aviso visible puede ser secundario.

## 2. Recuperación proporcional

Si un sistema de archivos presenta errores, evita escribir y prepara una copia o imagen por el procedimiento del centro. Las herramientas de comprobación pueden modificar metadatos y no se ejecutan indiscriminadamente sobre un sistema montado. Si el disco muestra fallos físicos, una reparación lógica no arregla la causa y puede aumentar daño o pérdida.

Ante un equipo que no arranca, comprueba primero que el firmware detecta la unidad y que el modo de arranque coincide con la instalación. Un medio de recuperación permite observar particiones y copiar datos, pero los volúmenes cifrados necesitan su recuperación legítima. No recrees particiones porque una unidad no tenga letra o no esté montada.

Si una actualización causa una regresión, registra paquetes o compilación, conserva evidencia y utiliza los mecanismos de reversión admitidos. Restaurar todo el equipo tiene un alcance mayor que revertir una configuración. Elige la operación más acotada que resuelva el problema y comprueba aplicaciones y datos después.

## 3. Preguntas resueltas

**1. `free` muestra poca memoria libre. ¿Falta RAM?**

No necesariamente. La caché puede recuperarse. Examina memoria disponible, paginación y comportamiento durante la tarea. Si el sistema responde bien y no existe presión sostenida, la memoria está siendo aprovechada.

**2. ¿Un servicio habilitado está ejecutándose?**

No tiene por qué. Habilitar define relaciones de activación; el estado actual se consulta por separado. Puede estar detenido, haber fallado o no haberse activado todavía. También puede ejecutarse un servicio no habilitado por inicio manual u otro mecanismo.

**3. Un archivo tiene modo `644`. ¿Quién puede modificarlo?**

En el modelo POSIX básico, el propietario tiene lectura y escritura; grupo y resto solo lectura. Deben considerarse ACL y privilegios. Eliminar su nombre depende del directorio contenedor y no se deduce únicamente de `644`.

**4. ¿Actualizar los índices de APT actualiza programas?**

No. Descarga metadatos de paquetes disponibles. La instalación de versiones nuevas es otra operación. Se revisan cambios, dependencias, capacidad y posibles reinicios antes de aplicarla.

**5. ¿Por qué una tarea funciona en terminal y falla programada?**

Puede usar otra identidad, entorno, directorio actual o acceso al destino. Deben usarse rutas claras y registros. Elevar todos los privilegios sin diagnóstico puede ocultar la causa y ampliar el riesgo.

**6. ¿Una suma SHA-256 igual demuestra una copia completa?**

Demuestra igualdad del contenido comparado con una probabilidad de colisión despreciable para este uso, si el cálculo y las referencias son fiables. No demuestra conservación de ACL, propietario, disponibilidad futura ni recuperación de todo el conjunto. Hay que comprobar esos requisitos aparte.

**7. ¿Por qué no usar siempre la terminación forzada?**

Impide que el proceso cierre archivos, confirme operaciones o guarde estado. Primero se intenta cierre normal y se identifica exactamente la tarea. Una finalización forzada solo se usa cuando está justificada y se asumen sus efectos.

**8. ¿Un snapshot guardado junto al disco virtual protege del fallo del anfitrión?**

No aporta independencia frente a ese fallo. Puede depender además de archivos base. La recuperación necesita copias en destinos adecuados y pruebas. Un snapshot sí puede ser útil para deshacer una configuración de laboratorio, dentro de sus limitaciones.

**9. ¿Por qué una pertenencia nueva a un grupo no aparece en una sesión antigua?**

La sesión puede conservar el contexto de seguridad creado al iniciarse. Inicia una sesión nueva y consulta identidad y grupos efectivos. No concluyas que la regla de permisos es incorrecta sin comprobar el contexto.

**10. ¿Formatear es una solución inicial a un problema de arranque?**

No. Destruye estructura o datos y evita un diagnóstico proporcional. Primero se observa firmware, unidad, particiones, cifrado, cargador y cambios recientes, preservando el contenido necesario.

## 4. Caso integrador

Un puesto Debian de laboratorio tarda más al iniciar sesión, no permite guardar ciertos archivos y una tarea de copia ha dejado de producir versiones nuevas. Debes determinar si hay una única causa o varias.

Una resolución razonada comienza por espacio e inodos, identidad y permisos del destino. Después revisa la tarea y sus registros con el mismo contexto. Si el volumen está lleno por retención ilimitada, no basta con borrar algo: hay que identificar datos prescindibles autorizados, aplicar una política de retención y comprobar copia y restauración. Si además una ACL cambió, se documentan dos causas en lugar de forzar una explicación única.

Entrega hipótesis descartadas, cambios mínimos, prueba de guardado, ejecución automática y restauración. Las evidencias deben permitir a otro alumno repetir la verificación sin conocer credenciales.

## 5. Autoevaluación final

- Explico la diferencia entre programa, proceso, hilo y servicio.
- Identifico el modo de arranque y las capas del almacenamiento sin modificarlas.
- Distingo RAM libre, disponible y presión por paginación.
- Pruebo permisos con identidades adecuadas y operaciones permitidas y denegadas.
- Separo actualizar índices, instalar paquetes y activar servicios.
- Puedo recuperar datos ficticios desde una copia independiente.
- Registro límites, errores y acciones de reversión con precisión.

La evaluación valora fundamento técnico, administración con alcance controlado y verificación reproducible. La apariencia del escritorio o la cantidad de comandos utilizados no sustituyen esos resultados.
