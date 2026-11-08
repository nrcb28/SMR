# Implantación, aceptación y defensa

## Fase 1. Preparar un entorno repetible

1. Comprueba recursos del host y versiones de las máquinas virtuales. Guarda inventario de CPU virtual, RAM, discos, adaptadores y redes.
2. Identifica la NIC LAB en cada sistema. Documenta la NIC NAT separada y confirma que no recibe el ámbito DHCP de prácticas.
3. Establece direcciones estáticas de servidores y reserva un ámbito libre para clientes. Desactiva otro DHCP del hipervisor únicamente en la red LAB utilizada.
4. Verifica comunicación en la misma subred, hora y nombres de equipos. No consideres `ping` una prueba completa de los servicios.
5. Crea un punto de recuperación del laboratorio y una copia de la configuración antes de cada cambio relevante.

**Evidencia:** inventario, diagrama y resultados reales de conectividad. El documento debe poder distinguir un fallo de interfaz, de DNS y de servicio. Si no hay suficiente memoria para todas las VM simultáneas, reduce el alcance operativo y anota qué se simula; no presentes componentes apagados como servicios disponibles.

## Fase 2. Desplegar servicios de forma incremental

Aplica las guías de [Servicios en red](../servicios-en-red/README.md), [Sistemas operativos en red](../sistemas-operativos-en-red/README.md) y [Seguridad informática](../seguridad-informatica/README.md). Cada servicio necesita configuración validada, reinicio o recarga cuando corresponda, consulta del estado y prueba desde un cliente.

Orden sugerido: red estable, DNS, hora, identidades, archivos, web y copias. AD exige especial atención a DNS y sincronización horaria. No combines instrucciones de Samba independiente y de controlador de dominio como si fueran intercambiables. Para HTTPS, distribuye únicamente el certificado raíz necesario para la confianza del laboratorio, protegiendo la clave privada.

Registra los comandos realmente usados y sanea la información antes de incorporarla al repositorio. Los archivos con contraseñas de base de datos, claves privadas, tokens y copias de usuarios quedan fuera. Sustituir un secreto en el último commit no lo elimina del historial; ante una exposición hay que revocarlo y seguir el procedimiento de saneamiento apropiado.

## Fase 3. Ejecutar aceptación

Usa una tabla con ID, equipo origen, cuenta, fecha, acción, esperado, observado, evidencia y estado. “OK” sin resultado observable impide revisar la conclusión.

| Prueba | Acción y aceptación |
| --- | --- |
| T01 DHCP | Renovar un cliente de LAB; debe recibir IP del ámbito, prefijo y DNS previstos sin afectar a otras redes. |
| T02 DNS | Consultar `intranet.aula.test` al servidor previsto y registrar la respuesta; un nombre inexistente debe fallar como se haya diseñado. |
| T03 Archivos | Cuenta autorizada crea y modifica un archivo; cuenta sin permiso recibe denegación. |
| T04 HTTPS | Acceder por nombre y comprobar certificado sin omitir advertencias. |
| T05 Copia | Ejecutar copia de datos sintéticos y verificar el registro, tamaño y estado. |
| T06 Restauración | Restaurar a una ubicación separada y comparar hash y permisos de una muestra. |
| T07 Reinicio | Reiniciar las VM de pruebas de forma ordenada y comprobar arranque automático de servicios requeridos. |
| T08 Segmentación | En la extensión VLAN, probar un flujo permitido y otro denegado entre redes desde los orígenes adecuados. |
| T09 Operación | Otra persona sigue el manual para localizar un fallo simulado y explicar la reversión. |

Las pruebas negativas deben estar autorizadas y acotadas: usar una cuenta sin permiso o detener un servicio de laboratorio no exige atacar sistemas ajenos. No simules un incidente borrando datos reales ni desactivando protecciones en equipos de producción.

## Fase 4. Demostrar recuperación

Prepara una carpeta de prueba con documentos sintéticos y permisos distintos para dos grupos. Calcula un hash de referencia, realiza copia y verifica que existe una versión recuperable. Simula pérdida únicamente de una copia de trabajo de esa carpeta. Restaura a otro destino para comparar sin sobrescribir una fuente aún válida.

Cronometra desde el inicio del incidente simulado hasta la verificación desde el cliente, no sólo la transferencia. Compara hashes, número de archivos y permisos efectivos. Registra qué punto temporal se recupera para evaluar el RPO. Si necesitas claves para descifrar el backup, comprueba su disponibilidad por el procedimiento seguro definido; una copia cifrada sin clave recuperable no cumple el objetivo.

**Resultado esperado del ejercicio:** un informe con tiempo observado, datos recuperados, comprobaciones fallidas y mejoras. Si no se alcanza el objetivo de cuatro horas o veinticuatro horas de RPO, explica por qué y cómo lo corregirías. No modifiques el objetivo después para aparentar cumplimiento.

## Fase 5. Manuales y defensa

El manual de administración describe comprobación de servicios, altas y bajas, copias, actualizaciones y recuperación. El manual de usuario explica acceso, guardado, límites, canales de incidencia y buenas prácticas en lenguaje comprensible. Ambos deben indicar versión y fecha; una captura de interfaz puede quedar obsoleta y necesita texto que explique su función.

Para la defensa, dedica primero tiempo a la necesidad y a la arquitectura. Después muestra una prueba positiva, otra negativa y una restauración acotada. Cierra con coste, sostenibilidad, límites y mejoras pendientes. Prepara una demostración de reserva mediante evidencias saneadas por si el entorno no arranca, dejando claro que es evidencia previa y no una ejecución en directo.

Cada miembro debe explicar decisiones y pruebas aunque haya trabajado en un área distinta. Mantén un registro breve de contribuciones, revisiones y problemas resueltos. La cantidad de commits no mide por sí sola el aprendizaje ni la calidad: puede premiar fragmentación artificial.

## Rúbrica propia

| Área | Peso | Evidencia de calidad |
| --- | --- | --- |
| Requisitos y diseño | 20 % | Trazabilidad necesidad–decisión–prueba. |
| Despliegue y servicios | 25 % | Configuración coherente y operación estable en el alcance declarado. |
| Seguridad y recuperación | 25 % | Permisos efectivos, límites y restauración verificados. |
| Documentación y sostenibilidad | 20 % | Mantenimiento repetible, costes y decisiones justificadas. |
| Trabajo y defensa | 10 % | Aportaciones claras y explicación de límites. |

No sustituye los criterios de calificación del centro. Una incidencia encontrada y documentada con corrección razonada aporta más evidencia técnica que ocultarla y presentar sólo capturas favorables.

## Preguntas de defensa con respuesta razonada

1. **¿Por qué no basta una copia diaria para garantizar RPO de 24 h?** Puede fallar o no incluir todos los datos; hacen falta supervisión y prueba de recuperación.
2. **¿Qué habilita DHCP entre VLAN?** Un relay o una arquitectura equivalente configurada, además de rutas y reglas; una difusión no cruza el router por sí sola.
3. **¿Es un trunk cualquier cable entre switches?** No: depende de configuración y etiquetado compatibles en ambos extremos.
4. **¿Por qué probar con una cuenta sin privilegios?** Para evaluar permisos efectivos reales; una cuenta administradora oculta restricciones mal diseñadas.
5. **¿Qué harías con una clave publicada por error?** Revocarla o rotarla, revisar uso, sanear el historial cuando proceda y documentar el incidente. Borrar la línea en el último archivo no elimina copias previas.

[Guía de diseño](01-guia.md) · [Índice](README.md)
