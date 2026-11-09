#!/usr/bin/env python3
"""Genera INDICE.md desde los documentos existentes; --check sólo compara."""

import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote


RAIZ = Path(__file__).resolve().parents[1]
SALIDA = RAIZ / 'INDICE.md'


def titulo(ruta: Path) -> str:
    for linea in ruta.read_text(encoding='utf-8').splitlines():
        if linea.startswith('# '):
            texto = linea[2:].strip()
            return re.sub(r'[\[\]`*]', '', texto)
    return ruta.stem


def generar() -> str:
    plan = json.loads((RAIZ / 'recursos/plan-estudios-madrid.json').read_text(encoding='utf-8'))
    nombres = {m['carpeta']: m['nombre'] for m in plan['modulos'] + plan['historicos']}
    catalogo = RAIZ / 'optativas/catalogo.json'
    if catalogo.is_file():
        optativas = json.loads(catalogo.read_text(encoding='utf-8'))
        nombres.update({m['carpeta']: m['codigo'] + ' · ' + m['nombre']
                        for m in optativas['modulos']})
    grupos = defaultdict(list)
    for archivo in RAIZ.rglob('*.md'):
        relativo = archivo.relative_to(RAIZ)
        if archivo == SALIDA or any(p.startswith('.') for p in relativo.parts):
            continue
        grupos[relativo.parent.as_posix()].append(archivo)
    orden_area = {'.': 0, 'docs': 1, 'cuaderno-integrador': 2,
                  'primero': 3, 'segundo': 4, 'optativas': 5,
                  'plan-anterior': 6, 'recursos': 7}
    def ordenar_grupo(nombre: str) -> tuple:
        area = nombre.split('/')[0]
        return (orden_area.get(area, 99), nombre)
    lineas = [
        '# Índice completo de capítulos', '',
        '[Presentación y ruta de estudio](README.md) · [Cuaderno integrador](cuaderno-integrador/README.md)', '',
        'Navegación por todos los documentos del repositorio. Los índices de cada asignatura explican el orden de estudio y los requisitos de sus prácticas.', '',
        'Este archivo se genera con `python3 scripts/generar_indice.py`. Para comprobar que está actualizado, utiliza `python3 scripts/generar_indice.py --check`.', '',
    ]
    for grupo in sorted(grupos, key=ordenar_grupo):
        nombre = nombres.get(grupo, 'Presentación' if grupo == '.' else grupo.replace('/', ' · '))
        lineas += ['## ' + nombre, '', '| Documento | Archivo |', '| --- | --- |']
        archivos = sorted(grupos[grupo], key=lambda p: (p.name != 'README.md', p.name))
        for archivo in archivos:
            ruta = archivo.relative_to(RAIZ).as_posix()
            etiqueta = titulo(archivo).replace('|', '\\|')
            lineas.append(f'| [{etiqueta}]({quote(ruta, safe="/")}) | `{archivo.name}` |')
        lineas.append('')
    return '\n'.join(lineas)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='No escribe; devuelve 1 si falta actualizar')
    argumentos = parser.parse_args()
    try:
        contenido = generar()
        if argumentos.check:
            if not SALIDA.exists() or SALIDA.read_text(encoding='utf-8') != contenido:
                print('INDICE.md necesita regenerarse.', file=sys.stderr)
                return 1
            print('INDICE.md está actualizado.')
        else:
            SALIDA.write_text(contenido, encoding='utf-8')
            print('INDICE.md generado.')
    except (OSError, UnicodeError, ValueError, KeyError) as exc:
        print(f'No se pudo generar el índice: {exc}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
