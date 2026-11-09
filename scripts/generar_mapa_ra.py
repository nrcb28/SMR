#!/usr/bin/env python3
"""Genera el mapa y la plantilla RA/CE; --check comprueba sin escribir.

La plantilla no contiene evaluaciones de alumnos. Copia el CSV antes de usarlo:
la generación actualiza la plantilla base, no un registro personal de progreso.
"""

import argparse
import csv
import io
import json
from pathlib import Path
import posixpath
import sys
from urllib.parse import urlsplit

from validar_ra import RAIZ, cargar_y_validar, clave


def escapar(texto: str) -> str:
    return texto.replace('|', '\\|').replace('\n', ' ')


def desde_docs(valor: str) -> str:
    partes = urlsplit(valor)
    ruta = posixpath.relpath(partes.path, 'docs')
    return ruta + ('#' + partes.fragment if partes.fragment else '')


def generar(registros: list, resumen: dict) -> dict:
    referencia = json.loads((RAIZ / 'recursos/ra/referentes-oficiales.json').read_text(encoding='utf-8'))
    fecha = referencia['fecha_revision']
    lineas = [
        '# Mapa de resultados de aprendizaje y criterios de evaluación', '',
        '[Índice general](../README.md) · [Cómo trabajar y evaluar por RA](evaluacion-por-ra.md) · [Catálogo de optativas](../optativas/README.md)', '',
        f'Revisión normativa: {fecha}. Este mapa relaciona los RA y CE oficiales con materiales y actividades didácticas del repositorio. La existencia de una ruta de estudio y una actividad no acredita que un estudiante haya adquirido el resultado.', '',
        '| Ámbito | Módulos o variantes | RA | CE |',
        '| --- | ---: | ---: | ---: |',
        f"| Parte común | {resumen['modulos_comunes']} | {resumen['ra_comunes']} | {resumen['ce_comunes']} |",
        f"| Catálogo optativo aplicable | {resumen['variantes_optativas']} | {resumen['ra_optativas']} | {resumen['ce_optativas']} |", '',
        'Las variantes de francés, inglés y alemán conservan códigos distintos y comparten su currículo de referencia. Los recuentos optativos cuentan cada código; no representan asignaturas que una persona deba cursar simultáneamente. Las condiciones de curso, duración y oferta se explican en el catálogo.', '',
        'Cada guía de alineación desarrolla la relación por criterio; la guía de retos explica procedimiento, entregables, comprobaciones y revisión. Los CE de esas guías se presentan mediante resúmenes didácticos. El referente normativo conserva sus enunciados y letras para cotejar la transcripción.', '',
        '- [Referentes normativos en JSON](../recursos/ra/referentes-oficiales.json).',
        '- [Inventario de módulos y cifras en JSON](../recursos/ra/mapa-ra.json).',
        '- [Plantilla de seguimiento de todos los CE](../recursos/ra/plantilla-seguimiento-ce.csv).',
        '- [Fuentes originales y huellas de los documentos consultados](../recursos/ra/fuentes-verificadas.json).', '',
        'En Proyecto, el RA5 del anexo II del RD 499/2024 imprime dos criterios con letra a). Se conservan ambas letras y se distinguen mediante claves editoriales a.1 y a.2. La clave no modifica la numeración oficial. Otras incidencias de transcripción se explican en la guía del módulo.', '',
    ]
    inventario = []
    csv_salida = io.StringIO(newline='')
    campos = ['modulo', 'ra', 'clave_ce', 'letra_oficial', 'criterio_resumido',
              'actividad', 'guia', 'evidencia_esperada', 'aceptacion', 'estado',
              'evidencia_obtenida', 'fecha', 'observaciones']
    escritor = csv.DictWriter(csv_salida, fieldnames=campos, delimiter=';', lineterminator='\n')
    escritor.writeheader()
    for registro in registros:
        datos = registro['datos']
        codigo = registro['codigo']
        tipo = registro['tipo']
        resultados = datos['resultados']
        nce = sum(len(ra['criterios']) for ra in resultados)
        inventario.append({
            'codigo': codigo, 'nombre': datos['nombre'], 'tipo': tipo,
            'carpeta': registro['carpeta'],
            'datos': registro['carpeta'] + '/alineacion-ra.json',
            'guia_ra': datos['guia_ra'], 'guia_retos': datos['guia_retos'],
            'resultados': len(resultados), 'criterios': nce,
        })
        lineas += [f"## {codigo} · {escapar(datos['nombre'])}", '',
                   f"Ámbito: {'parte común' if tipo == 'comun' else 'optativa/variante'}. {len(resultados)} RA y {nce} CE.", '',
                   f"[Alineación por criterio]({desde_docs(datos['guia_ra'])}) · [Retos desarrollados]({desde_docs(datos['guia_retos'])}) · [Datos]({desde_docs(registro['carpeta'] + '/alineacion-ra.json')})", '']
        for fuente in datos['fuentes']:
            lineas.append(f"Fuente: [{escapar(fuente['norma'])}]({fuente['url']}), {escapar(fuente['localizador'])}.")
        lineas += ['', '| RA | Enunciado oficial | CE | Material de estudio | Retos |',
                   '| --- | --- | ---: | --- | --- |']
        for ra in resultados:
            materiales = ', '.join(f'[{i}]({desde_docs(valor)})'
                                   for i, valor in enumerate(ra['materiales'], 1))
            retos = ', '.join(f"[{i}]({desde_docs(a['guia'])})"
                              for i, a in enumerate(ra['actividades'], 1))
            lineas.append(f"| RA{ra['numero']} | {escapar(ra['enunciado_oficial'])} | {len(ra['criterios'])} | {materiales} | {retos} |")
            actividades = {a['id']: a for a in ra['actividades']}
            for ce in ra['criterios']:
                actividad = actividades[ce['actividad']]
                escritor.writerow({
                    'modulo': codigo, 'ra': 'RA' + str(ra['numero']),
                    'clave_ce': clave(ce), 'letra_oficial': ce['letra'],
                    'criterio_resumido': ce['resumen'], 'actividad': ce['actividad'],
                    'guia': actividad['guia'], 'evidencia_esperada': ce['evidencia'],
                    'aceptacion': ce['aceptacion'], 'estado': 'sin_realizar',
                    'evidencia_obtenida': '', 'fecha': '', 'observaciones': '',
                })
        lineas.append('')
    lineas += ['## Uso de la plantilla', '',
               'Copia el CSV antes de registrar resultados. Todas sus filas empiezan en sin_realizar y las evidencias reales están vacías. Registra lo observado y la revisión correspondiente; no copies el resultado esperado a la evidencia obtenida. Las calificaciones y ponderaciones pertenecen a la programación del centro.', '',
               'Regeneración: `python3 scripts/generar_mapa_ra.py`. Comprobación sin escribir: `python3 scripts/generar_mapa_ra.py --check`. El proceso contrasta primero las alineaciones con el referente local y falla si faltan RA, CE, actividades o enlaces.', '']
    resumen_publicable = {k: v for k, v in resumen.items() if k != 'errores'}
    mapa = {'version': 1, 'fecha_revision': fecha,
            'alcance': 'Trazabilidad documental; no es evaluación ni acreditación del alumnado',
            'resumen': resumen_publicable, 'modulos': inventario}
    return {
        RAIZ / 'docs/mapa-ra.md': '\n'.join(lineas),
        RAIZ / 'recursos/ra/mapa-ra.json': json.dumps(mapa, ensure_ascii=False, indent=2) + '\n',
        RAIZ / 'recursos/ra/plantilla-seguimiento-ce.csv': csv_salida.getvalue(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        registros, resumen, errores = cargar_y_validar()
        if errores:
            for error in errores:
                print('ERROR: ' + error, file=sys.stderr)
            return 1
        productos = generar(registros, resumen)
        desactualizados = []
        for ruta, contenido in productos.items():
            if args.check:
                if not ruta.exists() or ruta.read_text(encoding='utf-8') != contenido:
                    desactualizados.append(str(ruta.relative_to(RAIZ)))
            else:
                ruta.parent.mkdir(parents=True, exist_ok=True)
                ruta.write_text(contenido, encoding='utf-8')
        if desactualizados:
            print('Archivos RA pendientes de regenerar: ' + ', '.join(desactualizados), file=sys.stderr)
            return 1
        print('Mapa RA y plantilla actualizados.' if args.check else 'Mapa RA y plantilla generados.')
        return 0
    except (OSError, UnicodeError, KeyError, TypeError, ValueError) as exc:
        print('No se pudo construir el mapa RA: ' + str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
