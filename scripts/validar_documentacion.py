#!/usr/bin/env python3
"""Comprueba la documentación sin ejecutar comandos de las prácticas ni usar red.

Alcance: inventario curricular, rutas, UTF-8, bloques cercados Markdown,
enlaces locales de sintaxis inline/referencia e índices de módulos.
No es un parser completo de CommonMark ni un verificador de enlaces externos.
"""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


RAIZ = Path(__file__).resolve().parents[1]
ENLACE = re.compile(r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[\'"].*?[\'"])?\s*\)')
REFERENCIA = re.compile(r'^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)', re.MULTILINE)
CABECERA = re.compile(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$')


def sin_bloques(texto: str, errores: list, ruta: str) -> str:
    lineas = []
    cerca = None
    for numero, linea in enumerate(texto.splitlines(), 1):
        coincidencia = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', linea)
        if cerca is None and coincidencia:
            cerca = (coincidencia[1][0], len(coincidencia[1]), numero)
            lineas.append("")
        elif cerca is not None:
            if (coincidencia and coincidencia[1][0] == cerca[0]
                    and len(coincidencia[1]) >= cerca[1]
                    and not coincidencia[2].strip()):
                cerca = None
            lineas.append("")
        else:
            lineas.append(linea)
    if cerca:
        errores.append(f"{ruta}:{cerca[2]}: bloque de código sin cerrar")
    return "\n".join(lineas)


def anclas(texto: str) -> set:
    resultado = set()
    for linea in texto.splitlines():
        coincidencia = CABECERA.match(linea)
        if not coincidencia:
            continue
        titulo = coincidencia[1]
        titulo = re.sub(r'<[^>]*>', '', titulo)
        titulo = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', titulo)
        slug = re.sub(r'[^\w\- ]', '', titulo.lower()).replace(' ', '-')
        candidato = slug
        sufijo = 1
        while candidato in resultado:
            candidato = f"{slug}-{sufijo}"
            sufijo += 1
        resultado.add(candidato)
    resultado.update(re.findall(r'<a\s+(?:id|name)=[\'"]([^\'"]+)', texto))
    return resultado


def main() -> int:
    errores = []
    archivos = sorted(p for p in RAIZ.rglob('*.md') if '.git' not in p.parts)
    documentos = {}
    originales = {}
    for archivo in archivos:
        relativo = archivo.relative_to(RAIZ).as_posix()
        try:
            texto = archivo.read_text(encoding='utf-8')
        except UnicodeError as exc:
            errores.append(f"{relativo}: no es UTF-8: {exc}")
            continue
        if not texto.strip() or '\x00' in texto:
            errores.append(f"{relativo}: documento vacío o con carácter nulo")
        originales[archivo] = texto
        documentos[archivo] = sin_bloques(texto, errores, relativo)

    enlaces_locales = 0
    grafo = {p: set() for p in documentos}
    for archivo, texto in documentos.items():
        relativo = archivo.relative_to(RAIZ).as_posix()
        destinos = [m[1] for m in ENLACE.finditer(texto)]
        destinos += [m[1] for m in REFERENCIA.finditer(texto)]
        for destino in destinos:
            destino = destino.strip('<>')
            componentes = urlsplit(destino)
            if componentes.scheme or componentes.netloc:
                continue
            enlaces_locales += 1
            nombre = unquote(componentes.path)
            objetivo = ((RAIZ / nombre.lstrip('/')) if nombre.startswith('/')
                        else (archivo.parent / nombre)).resolve() if nombre else archivo
            if not objetivo.is_relative_to(RAIZ):
                errores.append(f"{relativo}: enlace fuera del repositorio: {destino}")
                continue
            if not objetivo.exists():
                errores.append(f"{relativo}: destino inexistente: {destino}")
                continue
            if objetivo.is_dir():
                objetivo = objetivo / 'README.md'
            if objetivo in documentos:
                grafo[archivo].add(objetivo)
                if componentes.fragment and unquote(componentes.fragment) not in anclas(documentos[objetivo]):
                    errores.append(f"{relativo}: ancla local no encontrada: {destino}")

    inventario = RAIZ / 'recursos/plan-estudios-madrid.json'
    plan = {}
    try:
        plan = json.loads(inventario.read_text(encoding='utf-8'))
        modulos = plan['modulos']
        if sum(m['horas'] for m in modulos) != plan['horas_totales']:
            errores.append('El total de horas del inventario no coincide con horas_totales')
        if len({m['id'] for m in modulos}) != len(modulos):
            errores.append('Hay identificadores de módulo duplicados')
        for curso in (1, 2):
            suma = sum(m['horas_semanales'] for m in modulos if m['curso_tabla'] == curso)
            if suma != 30:
                errores.append(f'El curso {curso} no suma 30 horas semanales')
        for modulo in modulos + plan['historicos']:
            carpeta = RAIZ / modulo['carpeta']
            if not (carpeta / 'README.md').is_file():
                errores.append(f"Falta índice de módulo: {modulo['carpeta']}/README.md")
        carpetas_reales = {p.parent.relative_to(RAIZ).as_posix()
                          for curso in ('primero', 'segundo')
                          for p in (RAIZ / curso).glob('*/README.md')}
        carpetas_plan = {m['carpeta'] for m in modulos}
        if carpetas_reales != carpetas_plan:
            errores.append('Las carpetas de primero/segundo y el inventario no coinciden')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errores.append(f'Inventario curricular inválido: {exc}')

    visitados = set()
    pendientes = [RAIZ / 'README.md']
    while pendientes:
        archivo = pendientes.pop()
        if archivo in visitados:
            continue
        visitados.add(archivo)
        pendientes.extend(grafo.get(archivo, set()) - visitados)
    huerfanos = [p.relative_to(RAIZ).as_posix() for p in documentos if p not in visitados]
    if huerfanos:
        errores.append('Markdown sin ruta de navegación desde README: ' + ', '.join(huerfanos))

    resumen = {
        'markdown': len(archivos),
        'palabras_aproximadas_markdown': sum(len(t.split()) for t in originales.values()),
        'enlaces_locales_comprobados': enlaces_locales,
        'modulos_plan_actual': len(plan.get('modulos', [])),
        'modulos_historicos': len(plan.get('historicos', [])),
        'errores': len(errores),
    }
    print(json.dumps(resumen, ensure_ascii=False, indent=2))
    for error in errores:
        print('ERROR: ' + error, file=sys.stderr)
    return 1 if errores else 0


if __name__ == '__main__':
    raise SystemExit(main())
