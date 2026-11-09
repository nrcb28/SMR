#!/usr/bin/env bash
# Genera un manifiesto de archivos regulares. No copia ni elimina el origen.
set -euo pipefail
umask 077

if [[ $# -ne 2 ]]; then
    printf '%s\n' 'Uso: bash manifiesto.sh DIRECTORIO_ORIGEN DIRECTORIO_SALIDA' >&2
    exit 64
fi

for herramienta in realpath flock find sha256sum mktemp mv rm date wc; do
    if ! command -v "$herramienta" >/dev/null 2>&1; then
        printf 'Falta herramienta: %s\n' "$herramienta" >&2
        exit 69
    fi
done

origen=$(realpath -e -- "$1")
salida=$(realpath -e -- "$2")
if [[ ! -d "$origen" || ! -d "$salida" ]]; then
    printf '%s\n' 'Origen y salida deben ser directorios existentes.' >&2
    exit 66
fi

if [[ "$salida" == "$origen" || "$salida" == "${origen%/}/"* ]]; then
    printf '%s\n' 'La salida no puede ser el origen ni estar dentro de él.' >&2
    exit 64
fi

exec 9>"$salida/.manifiesto.lock"
if ! flock -n 9; then
    printf '%s\n' 'Ya hay una ejecución que utiliza esta salida.' >&2
    exit 75
fi

temporal=$(mktemp "$salida/.manifiesto.XXXXXX")
trap 'rm -f -- "$temporal"' EXIT

if ! (cd -- "$origen" && find . -type f -exec sha256sum -- {} +) >"$temporal"; then
    printf '%s\n' 'No se ha publicado el manifiesto: falló la lectura.' >&2
    exit 74
fi
if [[ ! -s "$temporal" ]]; then
    printf '%s\n' 'No hay archivos regulares; se conserva el manifiesto anterior.' >&2
    exit 66
fi

mv -f -- "$temporal" "$salida/manifiesto.sha256"
trap - EXIT
printf 'UTC=%s archivos=%s resultado=correcto\n' \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
    "$(wc -l < "$salida/manifiesto.sha256")"
