# Módulo profesional optativo · primero

En la distribución madrileña de SMR, primero incluye un módulo optativo de 50 horas de currículo y dos horas semanales de referencia. **Su denominación concreta, código, currículo y oferta dependen de la selección y autorización aplicables al centro.** No se asigna aquí un nombre oficial sin conocer esa información.

El catálogo autonómico se regula mediante la [Orden 3536/2025](https://www.bocm.es/boletin/CM_Orden_BOCM/2025/08/27/BOCM-20250827-5.PDF), con la modificación publicada en la [Orden 3822/2026](https://www.bocm.es/boletin/CM_Orden_BOCM/2026/09/25/BOCM-20260925-20.PDF). Consulta el [marco curricular](../../docs/curriculo-madrid.md) y la programación del centro antes de identificar una optativa o sus criterios de evaluación.

## Propuesta de ampliación propia: documentar prácticas con Git

La siguiente actividad es material complementario, no una equivalencia ni un currículo oficial de optativa. Permite aprender a conservar versiones de apuntes y configuraciones saneadas. Se puede realizar en Linux o Git Bash; los comandos de shell indicados no se deben copiar directamente en PowerShell si su sintaxis es diferente.

**Objetivo:** entregar un pequeño repositorio local con una guía, dos cambios justificados y un registro de revisión. No se requiere publicar en GitHub ni configurar claves.

### Conceptos

El directorio de trabajo contiene archivos editables. El índice o staging area selecciona el contenido del siguiente commit. Un commit registra una instantánea identificada por un objeto y metadatos; no guarda sólo una explicación verbal del cambio. Una rama identifica una línea de desarrollo; cambiar de rama puede modificar archivos del directorio de trabajo.

Un repositorio local no es automáticamente una copia externa. Si se pierde el disco que lo contiene, puede perderse también el historial. El control de versiones tampoco elimina la necesidad de copias de seguridad ni ofrece un lugar apropiado para contraseñas, claves privadas o datos de empresa.

### Procedimiento

Utiliza una carpeta nueva y vacía dentro de tu espacio de prácticas. Comprueba que estás en ella antes de iniciar el repositorio. Con Git 2.28 o posterior:

```bash
mkdir practica-documentacion
cd practica-documentacion
git init -b main
git config user.name "Alumno SMR"
git config user.email "alumno@example.invalid"
```

La identidad anterior es un ejemplo sintético para un ejercicio local. No modifica la configuración global porque no incluye `--global`. Para trabajo real, elige una identidad adecuada y revisa la privacidad del correo asociado.

Crea `README.md` con objetivo, equipo de laboratorio y pasos de una comprobación. Antes del primer commit, crea `.gitignore` para excluir archivos temporales y cualquier ruta de trabajo que no deba versionarse. Un patrón de exclusión no convierte en seguro un archivo ni retira del historial lo ya registrado.

```bash
git status --short
git add README.md .gitignore
git diff --cached
git commit -m "Documentar comprobacion inicial del laboratorio"
git log --oneline -5
```

`git diff --cached` permite revisar exactamente lo que se va a registrar. Si aparecen credenciales o información no autorizada, detén el commit y retira ese contenido del índice siguiendo la documentación de Git. No utilices `git add .` sin inspeccionar qué archivos incluye.

Haz dos cambios separados: corregir una instrucción y añadir una prueba con resultado esperado. Revisa el diff y crea un commit para cada propósito. Los mensajes deben describir el cambio; “cosas”, “final” o “último definitivo” no ayudan a investigar un problema.

### Práctica y evaluación propuesta

Otra persona debe leer el historial y explicar qué cambió entre la primera y la última versión. Después introduce una corrección mediante una rama de práctica y compara su diferencia con `main`. No necesitas publicar ni abrir solicitudes externas.

**Entregables:** carpeta local, guía Markdown, historial de tres commits útiles y una nota sobre qué información quedó fuera. **Aceptación:** instrucciones comprensibles, cambios delimitados, ausencia de secretos y explicación de la diferencia entre directorio, índice y commit.

**Preguntas:** ¿un commit copia archivos a GitHub? No, es local hasta que una operación de publicación lo envía a un remoto. ¿`.gitignore` borra un secreto ya registrado? No; hay que revocarlo si se expuso y sanear historial según proceda. ¿Un historial largo demuestra calidad? No; importa que permita entender decisiones y recuperar versiones útiles.

## Fuentes

- [Documentación oficial de Git](https://git-scm.com/doc).
- [Libro Pro Git: fundamentos](https://git-scm.com/book/es/v2).
- [GitHub Docs: seguridad de credenciales](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure).

[Índice de primero](../README.md) · [Índice general](../../README.md)
