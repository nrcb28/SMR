#!/usr/bin/env bash
# Consultas locales; sin instalar paquetes, elevar permisos ni modificar el sistema.
set -u

section() { printf '\n%s\n' "$1"; }

section 'Sistema operativo'
if [[ -r /etc/os-release ]]; then
    # Sólo claves públicas seleccionadas; no se ejecuta el contenido del fichero.
    awk -F= '$1 == "PRETTY_NAME" || $1 == "VERSION_ID" { print }' /etc/os-release
fi
uname -srm

section 'CPU'
if command -v lscpu >/dev/null 2>&1; then
    LC_ALL=C lscpu | awk -F: '$1 ~ /^(Architecture|CPU\(s\)|Model name|Thread\(s\) per core|Core\(s\) per socket|Socket\(s\))$/ { print }'
else
    printf '%s\n' 'lscpu no disponible; no se ha instalado ningún paquete.'
fi

section 'Memoria'
if command -v free >/dev/null 2>&1; then
    free -h
fi

section 'Discos y particiones: sin números de serie ni etiquetas'
if command -v lsblk >/dev/null 2>&1; then
    lsblk -o NAME,TYPE,SIZE,FSTYPE
fi

section 'Uso de los sistemas de archivos'
df -h --output=fstype,size,used,avail,pcent

printf '\n%s\n' 'Revisa la salida antes de compartirla. Los datos son observaciones, no una prueba de salud del hardware.'
