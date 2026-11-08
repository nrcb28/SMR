# 4. Diagnóstico, casos resueltos y evaluación

## 4.1 No confundas el control con la causa

El diagnóstico empieza por una operación concreta y un intervalo temporal. Un «timeout» puede deberse a filtrado, ruta incorrecta, host apagado o una aplicación que no responde. «Connection refused» suele indicar que se ha recibido un rechazo, pero hay que comprobar quién lo genera. Un mensaje HTTP 403 significa algo distinto de un fallo de certificado TLS.

La secuencia útil es: comprobar identidad del destino y ruta; comprobar servicio y escucha; comprobar control de red; comprobar autenticación; comprobar autorización; comprobar aplicación y datos. No desactives todos los controles para localizar un fallo: selecciona una prueba de cada capa y utiliza consola cuando el acceso remoto sea parte del problema.

## 4.2 Tabla de incidencias

| Síntoma | Comprobaciones | Acción que conserva el diagnóstico |
| --- | --- | --- |
| SSH deja de aceptar acceso tras un cambio | Consola, `sshd -t`, valores efectivos, `authorized_keys`, permisos y registros | Revertir sólo el archivo cambiado y validar; no habilitar root sin necesidad. |
| La clave funciona en una sesión pero no en otra | Clave ofrecida, agente, usuario, origen y `Match` | Forzar la identidad de prueba con `-i` y comparar el contexto. |
| Firewall parece no bloquear | Conexión previa, reglas efectivas, interfaz y cadena | Probar conexión nueva y revisar contadores y camino `input`/`forward`. |
| Tras filtrar falla IPv6 | ICMPv6, descubrimiento de vecinos y PMTU | Restaurar los mensajes de control necesarios; no negar toda la familia sin diseño. |
| HTTPS cifra pero navegador alerta | Nombre SAN, cadena, fechas, reloj y CA | Corregir certificado o confianza controlada; no aceptar todo globalmente. |
| Copia termina pero no restaura permisos | Metadatos del origen, privilegios y capacidad del destino | Restaurar en ruta alternativa y comparar ACL/propietario explícitamente. |
| Copia ocupa el disco del servidor | Montaje ausente y ruta real de destino | Detener nuevas copias y corregir comprobación previa; preservar los datos existentes. |
| Alerta sin registros suficientes | Política, conservación, hora y fuente | Declarar incertidumbre, conservar lo disponible y mejorar observación. |

## 4.3 Cómo validar sin falsear resultados

Una prueba necesita estado inicial conocido, acción y resultado observable. Para afirmar que un firewall bloquea TCP 8080, demuestra primero que el servicio escucha y responde sin ese control y después que una conexión nueva falla con él. Si el servidor no estaba arrancado, el intento fallido no prueba el firewall.

Para afirmar que la restauración mantiene confidencialidad, prueba con un usuario autorizado y otro no autorizado. Un hash idéntico prueba contenido respecto a una referencia fiable, pero no que los permisos sean correctos. Un programa de copia que termina con código correcto aporta evidencia de ejecución, no de recuperación de toda una aplicación.

Una medida de tiempo debe explicar inicio y fin. «Transferencia completada en cuatro minutos» no demuestra RTO de cuatro minutos si faltaron veinte de preparar VM, DNS y permisos. Separa tiempo técnico y tiempo hasta recuperar la operación de usuario definida.

## 4.4 Preguntas y respuestas razonadas

**1. Un alumno propone `chmod -R 777` para resolver acceso denegado. ¿Qué problema introduce?** Concede lectura, escritura y ejecución sin un diseño de identidades y puede afectar todo el árbol. Puede permitir que cualquiera modifique contenido y marca archivos ejecutables. Debe localizarse la entrada concreta que impide el acceso previsto y mantener la prueba de denegación a quien no corresponda.

**2. ¿Por qué una frase de paso no basta si roban el cliente mientras está desbloqueado?** La clave puede estar disponible mediante un agente o una sesión ya autenticada. Importan bloqueo, protección del equipo, duración y control de sesiones. Hay que revocar o retirar la clave autorizada y revisar accesos, no confiar sólo en el cifrado del archivo privado.

**3. ¿MFA equivale a dos contraseñas?** No. Debe combinar categorías de factores distintas. Dos secretos memorizados siguen siendo conocimiento. La resistencia al phishing y el proceso de recuperación también cambian la seguridad real.

**4. ¿Un hash que coincide prueba que un archivo procede del fabricante?** Sólo si la referencia está vinculada de forma fiable al fabricante. Si el atacante puede cambiar ambos, la coincidencia no autentica el origen. Una firma y una clave pública verificada aportan otra relación de confianza.

**5. ¿Cambiar SSH a un puerto alto elimina el riesgo de credenciales robadas?** Puede reducir ruido de algunos intentos automáticos, pero la autenticación, autorización y exposición siguen existiendo. El control principal no debe depender de que el puerto se desconozca.

**6. ¿RPO de dos horas significa restaurar en menos de dos horas?** No. Se refiere al punto de los datos recuperables y la pérdida temporal tolerada. El tiempo de restauración y recuperación del servicio se evalúa con RTO.

**7. ¿Una sincronización entre carpetas ya es copia independiente?** Puede conservar disponibilidad frente a ciertos fallos, pero también propagar borrado o corrupción. Versionado, retención, credenciales, ubicación y pruebas de restauración determinan si cubre el escenario.

**8. ¿Por qué no hay que borrar todas las reglas para probar un servicio?** Puede retirar controles de otras aplicaciones, NAT y segmentación, además de ocultar qué regla causaba el fallo. Usa una política conocida en una VM dedicada, contadores y cambios puntuales con reversión.

**9. ¿Notificamos todos los incidentes a la AEPD?** No todos son brechas de datos personales ni todos tienen la misma obligación de notificación. El responsable evalúa las condiciones y el riesgo conforme al RGPD y orientaciones oficiales; el técnico informa por el canal establecido y no espera a tener certeza absoluta para escalar una sospecha relevante.

**10. ¿Un firewall y antivirus instalados demuestran cumplimiento ENS?** No. El marco exige organización, gestión y medidas conforme al ámbito y categorización aplicables. Una herramienta aislada no reemplaza el análisis, los procedimientos ni la verificación exigible.

**11. La tabla de riesgos baja de 12 a 6, ¿ha bajado exactamente a la mitad la pérdida esperada?** No en la matriz cualitativa del capítulo. Es una prioridad ordinal construida con una escala didáctica. Para estimar pérdidas harían falta datos y un modelo cuantitativo distinto, con incertidumbre explícita.

**12. ¿Por qué conservar eventos de inicio de sesión exitoso?** Un éxito después de varios fallos puede ser relevante para una investigación y las acciones legítimas también necesitan trazabilidad. La recopilación debe ser proporcionada y protegida; más registro sin finalidad no equivale a mejor seguridad.

## 4.5 Rúbrica didáctica

La programación del centro prevalece sobre esta propuesta.

| Criterio | Peso propuesto | Evidencia |
| --- | --- | --- |
| Riesgos y requisitos | 20 % | Escenario definido, supuestos y medidas relacionadas con el riesgo. |
| Implementación controlada | 25 % | Estado previo, mínimo privilegio, validadores y reversión. |
| Pruebas de seguridad | 20 % | Casos positivos y negativos con causas bien diferenciadas. |
| Recuperación y respuesta | 25 % | Restauración útil, tiempos, cronología y decisiones justificadas. |
| Documentación y custodia | 10 % | Informe claro, datos mínimos y ausencia de secretos. |

Una configuración que expone datos o deja sin acceso de recuperación necesita corrección antes de cerrar la práctica. Si se descubre una clave privada o contraseña publicada, retirarla del archivo actual no basta: se revoca o cambia el secreto y se evalúa el historial y los accesos según el procedimiento.

## 4.6 Cierre del módulo

- El inventario y los servicios necesarios coinciden con la política final.
- Cada control importante tiene prueba positiva y negativa pertinente.
- Existe una consola o ruta de recuperación distinta del acceso que se modifica.
- Los servicios cifrados validan identidad, nombre y confianza.
- La copia está en el destino esperado y se ha restaurado en una ruta alternativa.
- RPO y RTO se expresan con supuestos y mediciones, sin confundirlos.
- La respuesta a incidentes distingue hechos, hipótesis, responsables y decisiones.
- El repositorio conserva sólo material didáctico y evidencias sin secretos ni datos personales reales.

[Volver al índice del módulo](README.md)
