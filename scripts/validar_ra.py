#!/usr/bin/env python3
"""Valida la trazabilidad documental RA/CE contra referentes normativos locales.

No evalúa a estudiantes ni determina calificaciones. No necesita red.
"""

from datetime import date
import json
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit

from validar_documentacion import anclas, sin_bloques


RAIZ = Path(__file__).resolve().parents[1]


def normalizar(texto: str) -> str:
    return ' '.join(texto.split())


def clave(criterio: dict) -> str:
    return criterio.get('clave', criterio.get('letra', ''))


def leer_json(ruta: Path, errores: list):
    try:
        return json.loads(ruta.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, ValueError) as exc:
        errores.append(f'{ruta.relative_to(RAIZ)}: {exc}')
        return None


def ruta_local(valor, contexto: str, errores: list) -> None:
    if not isinstance(valor, str) or not valor.strip():
        errores.append(contexto + ': falta una ruta local')
        return
    partes = urlsplit(valor)
    if partes.scheme or partes.netloc or partes.path.startswith('/'):
        errores.append(contexto + ': se requiere ruta relativa a la raíz: ' + valor)
        return
    ruta = (RAIZ / unquote(partes.path)).resolve()
    if not ruta.is_relative_to(RAIZ) or not ruta.is_file():
        errores.append(contexto + ': archivo inexistente o fuera del repositorio: ' + valor)
        return
    if partes.fragment and ruta.suffix.lower() == '.md':
        texto = sin_bloques(ruta.read_text(encoding='utf-8'), errores, str(ruta.relative_to(RAIZ)))
        if unquote(partes.fragment) not in anclas(texto):
            errores.append(contexto + ': ancla inexistente: ' + valor)


def texto_obligatorio(objeto: dict, campo: str, contexto: str, errores: list) -> None:
    if not isinstance(objeto.get(campo), str) or not objeto[campo].strip():
        errores.append(contexto + ': falta texto en ' + campo)


def lista_textos(objeto: dict, campo: str, contexto: str, errores: list) -> list:
    valores = objeto.get(campo)
    if (not isinstance(valores, list) or not valores
            or any(not isinstance(v, str) or not v.strip() for v in valores)):
        errores.append(contexto + ': se requiere una lista no vacía en ' + campo)
        return []
    return valores


def cargar_y_validar():
    errores = []
    plan = leer_json(RAIZ / 'recursos/plan-estudios-madrid.json', errores)
    referentes = leer_json(RAIZ / 'recursos/ra/referentes-oficiales.json', errores)
    optativas = leer_json(RAIZ / 'optativas/catalogo.json', errores)
    if not all(isinstance(v, dict) for v in (plan, referentes, optativas)):
        return [], {}, errores
    esperados = []
    for modulo in plan.get('modulos', []):
        if modulo.get('codigo') != 'CMO':
            esperados.append((modulo['codigo'], modulo['carpeta'], 'comun', modulo))
    for modulo in optativas.get('modulos', []):
        esperados.append((modulo['codigo'], modulo['carpeta'], 'optativa', modulo))
    codigos = [v[0] for v in esperados]
    if len(codigos) != len(set(codigos)):
        errores.append('Hay códigos duplicados en el inventario común/optativo')
    refs = referentes.get('modulos', {})
    if set(refs) != set(codigos):
        errores.append('Los códigos de referentes oficiales no coinciden con el inventario de módulos')
    archivos_previstos = {(RAIZ / carpeta / 'alineacion-ra.json').resolve()
                         for _, carpeta, _, _ in esperados}
    archivos_reales = {p.resolve() for p in RAIZ.rglob('alineacion-ra.json') if '.git' not in p.parts}
    if archivos_reales != archivos_previstos:
        faltan = sorted(str(p.relative_to(RAIZ)) for p in archivos_previstos - archivos_reales)
        sobran = sorted(str(p.relative_to(RAIZ)) for p in archivos_reales - archivos_previstos)
        if faltan:
            errores.append('Faltan datos RA: ' + ', '.join(faltan))
        if sobran:
            errores.append('Datos RA fuera del inventario: ' + ', '.join(sobran))
    registros = []
    actividades_globales = set()
    for codigo, carpeta, tipo, metadata in esperados:
        ruta = RAIZ / carpeta / 'alineacion-ra.json'
        datos = leer_json(ruta, errores)
        if not isinstance(datos, dict):
            continue
        if datos.get('modulo') != codigo or datos.get('carpeta') != carpeta:
            errores.append(codigo + ': módulo o carpeta no coincide con el inventario')
        texto_obligatorio(datos, 'nombre', codigo, errores)
        for campo in ('guia_ra', 'guia_retos'):
            ruta_local(datos.get(campo), codigo + '.' + campo, errores)
        fuentes = datos.get('fuentes', [])
        if not isinstance(fuentes, list) or not fuentes:
            errores.append(codigo + ': faltan fuentes normativas')
            fuentes = []
        for fuente in fuentes:
            if not isinstance(fuente, dict):
                errores.append(codigo + ': formato de fuente inválido')
                continue
            for campo in ('norma', 'url', 'localizador', 'fecha_consulta'):
                texto_obligatorio(fuente, campo, codigo + '.fuente', errores)
            host = urlsplit(fuente.get('url', '')).hostname
            if host not in {'www.boe.es', 'www.bocm.es', 'www.comunidad.madrid', 'comunidad.madrid'}:
                errores.append(codigo + ': fuente normativa sin dominio oficial reconocido')
            try:
                date.fromisoformat(fuente.get('fecha_consulta', ''))
            except (TypeError, ValueError):
                errores.append(codigo + ': fecha de consulta no válida, usa AAAA-MM-DD')
        resultados = datos.get('resultados', [])
        oficiales = refs.get(codigo, {}).get('resultados', [])
        if not isinstance(resultados, list):
            errores.append(codigo + ': resultados debe ser una lista')
            continue
        numeros = [r.get('numero') for r in resultados if isinstance(r, dict)]
        numeros_oficiales = [r['numero'] for r in oficiales]
        if numeros != numeros_oficiales or any(type(n) is not int for n in numeros):
            errores.append(codigo + ': secuencia de RA distinta del referente oficial')
        oficiales_por_numero = {r['numero']: r for r in oficiales}
        for ra in resultados:
            if not isinstance(ra, dict):
                errores.append(codigo + ': resultado no es un objeto')
                continue
            numero = ra.get('numero')
            contexto = f'{codigo}.RA{numero}'
            oficial = oficiales_por_numero.get(numero)
            if not oficial:
                continue
            enunciado = ra.get('enunciado_oficial')
            if (not isinstance(enunciado, str)
                    or normalizar(enunciado) != normalizar(oficial['enunciado_oficial'])):
                errores.append(contexto + ': enunciado distinto de la transcripción normativa de referencia')
            for material in lista_textos(ra, 'materiales', contexto, errores):
                ruta_local(material, contexto + '.material', errores)
            criterios = ra.get('criterios', [])
            actividades = ra.get('actividades', [])
            if not isinstance(criterios, list) or not criterios:
                errores.append(contexto + ': criterios debe ser una lista no vacía')
                continue
            if not all(isinstance(c, dict) for c in criterios):
                errores.append(contexto + ': criterio no es un objeto')
                continue
            esperados_ce = [(clave(c), c['letra']) for c in oficial['criterios']]
            actuales_ce = [(clave(c), c.get('letra')) for c in criterios]
            if actuales_ce != esperados_ce:
                errores.append(contexto + ': claves/letras/orden de CE distintos del referente oficial')
            claves = [clave(c) for c in criterios]
            if len(claves) != len(set(claves)):
                errores.append(contexto + ': claves de CE duplicadas')
            if not isinstance(actividades, list) or not actividades:
                errores.append(contexto + ': faltan actividades')
                actividades = []
            por_id = {}
            cobertura = set()
            for actividad in actividades:
                if not isinstance(actividad, dict):
                    errores.append(contexto + ': actividad no es un objeto')
                    continue
                for campo in ('id', 'titulo', 'guia'):
                    texto_obligatorio(actividad, campo, contexto + '.actividad', errores)
                identificador = actividad.get('id', '')
                if identificador in por_id or identificador in actividades_globales:
                    errores.append(contexto + ': actividad duplicada: ' + identificador)
                por_id[identificador] = actividad
                actividades_globales.add(identificador)
                ruta_local(actividad.get('guia'), contexto + '.actividad', errores)
                for campo in ('entregables', 'comprobaciones'):
                    lista_textos(actividad, campo, contexto + '.actividad', errores)
                referencias = lista_textos(actividad, 'criterios', contexto + '.actividad', errores)
                if not set(referencias).issubset(set(claves)):
                    errores.append(contexto + ': actividad refiere CE inexistentes')
                cobertura.update(referencias)
            if cobertura != set(claves):
                errores.append(contexto + ': existen CE sin actividad que los desarrolle')
            for ce in criterios:
                for campo in ('letra', 'resumen', 'actividad', 'evidencia', 'aceptacion'):
                    texto_obligatorio(ce, campo, contexto + '.CE', errores)
                actividad = por_id.get(ce.get('actividad'))
                if not actividad or clave(ce) not in actividad.get('criterios', []):
                    errores.append(contexto + ': CE sin actividad coherente: ' + str(clave(ce)))
        registros.append({'codigo': codigo, 'carpeta': carpeta, 'tipo': tipo,
                          'metadata': metadata, 'datos': datos})
    resumen = {'modulos_comunes': 0, 'variantes_optativas': 0,
               'ra_comunes': 0, 'ce_comunes': 0, 'ra_optativas': 0, 'ce_optativas': 0}
    for registro in registros:
        tipo = registro['tipo']
        resumen['modulos_comunes' if tipo == 'comun' else 'variantes_optativas'] += 1
        sufijo = 'comunes' if tipo == 'comun' else 'optativas'
        ras = registro['datos']['resultados']
        resumen['ra_' + sufijo] += len(ras)
        resumen['ce_' + sufijo] += sum(len(r['criterios']) for r in ras)
    resumen['actividades_documentadas'] = len(actividades_globales)
    resumen['errores'] = len(errores)
    return registros, resumen, errores


def main() -> int:
    try:
        _, resumen, errores = cargar_y_validar()
    except (KeyError, TypeError, ValueError) as exc:
        print('Datos RA inválidos: ' + str(exc), file=sys.stderr)
        return 1
    print(json.dumps(resumen, ensure_ascii=False, indent=2))
    for error in errores:
        print('ERROR: ' + error, file=sys.stderr)
    return 1 if errores else 0


if __name__ == '__main__':
    raise SystemExit(main())
