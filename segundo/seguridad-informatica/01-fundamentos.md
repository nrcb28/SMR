# 1. Fundamentos de seguridad informática

## 1.1 Propiedades que se deben proteger

La **confidencialidad** limita quién accede a la información. La **integridad** permite confiar en que no ha sido alterada de forma indebida. La **disponibilidad** asegura que el servicio puede utilizarse cuando se necesita. En un sistema administrado también importan autenticidad y trazabilidad. No todos los activos requieren el mismo equilibrio: un tablón público prioriza integridad y disponibilidad; las credenciales requieren una protección especialmente alta de confidencialidad.

Un control puede mejorar una propiedad y perjudicar otra. Cerrar todos los puertos reduce exposición, pero también puede inutilizar el servicio autorizado. Cifrar sin custodiar las claves protege datos ante pérdida del disco, pero puede impedir su recuperación. Una política correcta expresa primero qué operaciones deben ser posibles y después cómo se limita el resto.

La seguridad física sostiene a la lógica. Acceso a un equipo encendido, consola del hipervisor, discos extraíbles, cableado, alimentación y temperatura pueden afectar al sistema aunque las contraseñas sean robustas. La cuenta que administra el hipervisor controla los discos y consolas de las VM: su protección importa tanto como la del invitado.

## 1.2 Activo, amenaza, vulnerabilidad y riesgo

Un **activo** tiene valor para la organización: información, equipo, servicio, identidad o capacidad de trabajar. Una **amenaza** es una causa potencial de daño. Una **vulnerabilidad** es una debilidad que permite que una amenaza produzca un efecto. Un **incidente** es un suceso que afecta o puede afectar a la seguridad y debe gestionarse según el procedimiento.

El **riesgo** relaciona escenarios, probabilidad e impacto. No existe una cifra universal que convierta todos los riesgos en euros. En una matriz cualitativa, `probabilidad × impacto` permite priorizar dentro de una escala definida, pero multiplicar etiquetas ordinales no produce una predicción estadística. Debes explicar la escala, la evidencia y la incertidumbre.

Ejemplo didáctico: el servidor de archivos contiene manuales ficticios y sufre riesgo de borrado accidental. Se valora probabilidad 3 e impacto 4 en una escala propia de 1 a 5; el indicador es 12. Una copia versionada y una restauración ensayada pueden reducir el impacto previsto a 2, manteniendo probabilidad 3: residual 6. El control no impide necesariamente el borrado; reduce las consecuencias y el tiempo de recuperación.

Si dispones de datos cuantitativos, un escenario distinto puede estimar una pérdida media de 4.000 € y una frecuencia de 0,2 incidentes al año: pérdida anual esperada de 800 €. Es un cálculo educativo con supuestos, no un presupuesto ni una garantía. Costes reputacionales, legales, acumulación de fallos y eventos extremos pueden quedar fuera del modelo.

Los tratamientos habituales son reducir, evitar, transferir o aceptar el riesgo de forma autorizada. Contratar una póliza no elimina una vulnerabilidad. Aceptar requiere responsable, justificación, plazo y revisión; no equivale a olvidar el problema. Tras un cambio revisa riesgos nuevos: una copia en nube introduce dependencia de identidad, proveedor, conectividad y claves.

## 1.3 Superficie y defensa en profundidad

La superficie de ataque incluye servicios, interfaces, cuentas, aplicaciones, dependencias, personas y procedimientos accesibles. Una VM con sólo dos puertos puede seguir expuesta por una cuenta privilegiada reutilizada o una consola web del hipervisor. Reducir superficie significa retirar lo innecesario y limitar lo necesario por origen, función y contexto.

La defensa en profundidad combina controles que no fallen todos por el mismo motivo: privilegios limitados, actualizaciones, segmentación, autenticación, filtrado, registros, copias y recuperación. Dos productos que dependen de la misma cuenta administradora y del mismo disco pueden parecer independientes y no serlo ante un incidente.

Separar redes no constituye por sí solo autorización. Una VLAN organiza un dominio de capa 2; los flujos entre VLAN requieren enrutamiento y controles. Un firewall de host regula tráfico del propio equipo; uno de red puede aplicar una política entre segmentos. En un host Linux que enruta o publica contenedores importa la cadena `forward`, no sólo `input`.

## 1.4 Contraseñas, claves y MFA

Una contraseña se comparte como secreto entre usuario y verificador; debe ser única, suficientemente larga y almacenarse mediante un gestor adecuado. Reutilizarla entre correo, GitHub y el laboratorio crea una vía de propagación. No se guardan en texto en scripts, capturas ni incidencias. La custodia de recuperación y la baja de cuentas son parte del sistema de identidad.

La autenticación multifactor combina factores de categorías distintas: conocimiento, posesión e inherencia. Dos contraseñas no forman dos factores. MFA tampoco elimina sesiones robadas, autorización excesiva o procedimientos de recuperación inseguros. Métodos resistentes al phishing, como credenciales FIDO2 con comprobación del servicio, ofrecen propiedades diferentes de un código que una persona puede entregar a una página falsa.

Una clave SSH privada se conserva en el cliente y la pública se autoriza en el servidor. Proteger la privada con una frase de paso limita algunos riesgos de robo del archivo, pero no sustituye la seguridad del cliente ni el control del agente de claves. La clave del host autentica al servidor; la del usuario autentica al usuario. Aceptar una clave de host sin verificar su huella debilita esa distinción.

## 1.5 Hash, cifrado y firma

Un **hash criptográfico** transforma datos en un resumen de longitud fija. Sirve para comparar integridad si el valor de referencia es fiable. Si un atacante cambia el archivo y el hash publicado en el mismo lugar, la comparación no prueba autenticidad. SHA-256 no cifra el archivo y no permite recuperar su contenido.

Las contraseñas necesitan funciones de derivación diseñadas para aumentar el coste de prueba y una sal única; no basta guardar `SHA256(contraseña)`. La sal no es una contraseña secreta: evita reutilizar el mismo resultado y dificulta tablas precalculadas entre usuarios. La elección de algoritmo y parámetros corresponde a la aplicación y sus recomendaciones actuales, no a un script improvisado.

El **cifrado simétrico** usa una clave compartida para proteger contenido. El **asimétrico** utiliza un par de claves relacionadas para operaciones que dependen del algoritmo y protocolo. Los protocolos modernos combinan mecanismos: acuerdo de claves, cifrado autenticado y autenticación del extremo. No se eligen algoritmos sólo por tener más bits ni se diseña un protocolo propio para una práctica de administración.

Una **firma digital** vincula datos a una clave privada y permite verificar su integridad y procedencia respecto a la clave pública correspondiente. No garantiza por sí sola que la persona real sea quien dice ser ni que una firma tenga un efecto jurídico concreto. La confianza depende del vínculo entre identidad y clave y del contexto del sistema.

Un **certificado** vincula datos de identidad o nombres con una clave pública mediante una firma y una política de confianza. En HTTPS hay que validar cadena, periodo de validez, nombre SAN y propósito apropiado. Un certificado autofirmado puede servir en laboratorio con una ancla de confianza controlada; no autoriza a desactivar la validación TLS en todos los clientes.

## 1.6 Copia, RPO y RTO

El **RPO** expresa la pérdida de datos tolerable medida en tiempo respecto al punto recuperable. El **RTO** expresa el tiempo objetivo para recuperar la actividad definida. Si se realiza una copia correcta cada noche y el incidente ocurre justo antes de la siguiente, la pérdida potencial se aproxima a un día. Restaurar en diez minutos no mejora ese RPO.

Una copia completa captura el conjunto definido. Las incrementales y diferenciales reducen algunas transferencias a cambio de depender de cadenas o puntos de referencia. El efecto concreto depende del producto, su deduplicación y su método de restauración. Debes probar la versión que vas a utilizar, no asumir que todas restauran igual.

La regla 3-2-1 propone diversificar tres ejemplares totales, dos tipos de soporte y uno fuera de la ubicación principal. Es un punto de partida, no una prueba automática de continuidad. Añade controles frente a borrado por credenciales comprometidas, inmutabilidad o desconexión, cifrado cuando corresponda y pruebas de restauración. Una carpeta sincronizada puede propagar borrados; RAID protege frente a algunos fallos de disco, no ante todos los incidentes.

Define quién puede leer, escribir y borrar las copias. Usar la misma cuenta de administrador del servidor para borrar todas las copias reduce su independencia. Separa el procedimiento de recuperar una clave del procedimiento de recuperar el repositorio cifrado; ambos deben seguir disponibles durante una crisis.

## 1.7 Registro, detección y evidencia

Un registro permite investigar sólo lo que se ha configurado para observar y conservar. Conviene registrar identidad, recurso, acción, resultado y hora coherente. Recogerlo todo puede saturar el sistema, dificultar búsquedas e introducir datos personales innecesarios. Establece finalidad, acceso, integridad y conservación.

Una alerta necesita contexto: cinco errores de acceso pueden ser una persona que olvidó la contraseña o un intento no autorizado. No se decide únicamente por el contador. Correlaciona origen, hora, cuenta, éxito posterior y comportamiento del equipo, respetando los límites de la investigación autorizada.

Guardar un hash de una evidencia ayuda a detectar modificaciones, pero no demuestra por sí solo su origen ni quién la obtuvo. La cadena de custodia documenta identificación, adquisición, responsables, fechas, traslados y controles. En una práctica basta trabajar con datos ficticios y registrar claramente los pasos; en un incidente real se aplica el procedimiento establecido y se evita alterar evidencias sin necesidad.

## 1.8 Protección de datos y ENS en el trabajo técnico

Los datos personales incluyen información que identifica o hace identificable a una persona; una dirección de usuario o un registro de actividad puede serlo según el contexto. El técnico debe aplicar el procedimiento del responsable: minimizar datos, limitar acceso y comunicar incidentes por el canal previsto. Seudonimizar no equivale automáticamente a anonimizar.

El RGPD contempla medidas de seguridad adecuadas al riesgo y reglas de notificación de brechas. La notificación a la autoridad competente se evalúa por el responsable del tratamiento, con la excepción relativa a que sea improbable el riesgo para derechos y libertades. El plazo de referencia es sin dilación indebida y, cuando sea posible, hasta 72 horas desde que tenga constancia. La comunicación a afectados responde a otros requisitos, incluido el alto riesgo; no se confunden ambos trámites. Consulta [las orientaciones de la AEPD](https://www.aepd.es/derechos-y-deberes/cumple-tus-deberes/medidas-de-cumplimiento/brechas-de-datos-personales-notificacion).

El ENS, regulado por el Real Decreto 311/2022, establece un marco de seguridad cuyo ámbito debe comprobarse para cada organización y servicio. Categorizar un sistema y seleccionar medidas requiere análisis y responsables definidos; instalar antivirus y firewall no equivale a certificarlo. La guía sólo introduce estas responsabilidades para la práctica técnica. La fuente normativa es el [texto consolidado del ENS en el BOE](https://www.boe.es/eli/es/rd/2022/05/03/311/con).

## Referencias para ampliar

- [INCIBE: guía de copias de seguridad](https://www.incibe.es/sites/default/files/contenidos/guias/guia-copias-de-seguridad.pdf).
- [OpenSSH: manuales oficiales](https://www.openssh.org/manual.html).
- [NIST: glosario de ciberseguridad](https://csrc.nist.gov/glossary).
- [AEPD: comunicación de brechas a interesados](https://www.aepd.es/derechos-y-deberes/cumple-tus-deberes/medidas-de-cumplimiento/comunicacion-de-brechas-de-datos).
- [RGPD publicado en el BOE](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807).

Los cálculos, ejemplos y matrices de este capítulo son didácticos. No sustituyen un análisis de riesgos de una organización ni una decisión del responsable del tratamiento.
