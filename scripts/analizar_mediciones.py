#!/usr/bin/env python3
"""Analiza un CSV de transferencias sintéticas sin generar tráfico de red.

CSV UTF-8 delimitado por ';': prueba;tamano_mib;duracion_ms;contexto.
p95 se calcula por rango más próximo, sin interpolación.
"""

import argparse
import csv
from decimal import Decimal, DecimalException, InvalidOperation, ROUND_CEILING
import json
from pathlib import Path
from statistics import median


def analizar(ruta: Path) -> dict:
    tiempos = []
    tamanos = []
    identificadores = set()
    with ruta.open(encoding='utf-8-sig', newline='') as entrada:
        lector = csv.DictReader(entrada, delimiter=';')
        necesarias = {'prueba', 'tamano_mib', 'duracion_ms', 'contexto'}
        if (lector.fieldnames is None or len(lector.fieldnames) != len(necesarias)
                or set(lector.fieldnames) != necesarias):
            raise ValueError('Cabeceras esperadas: prueba;tamano_mib;duracion_ms;contexto')
        for numero, fila in enumerate(lector, 2):
            if None in fila or any(valor is None for valor in fila.values()):
                raise ValueError(f'Fila {numero}: número de campos incorrecto')
            identificador = fila['prueba'].strip()
            if not identificador or identificador in identificadores:
                raise ValueError(f'Fila {numero}: identificador vacío o duplicado')
            try:
                tamano = Decimal(fila['tamano_mib'])
                tiempo = Decimal(fila['duracion_ms'])
            except InvalidOperation as exc:
                raise ValueError(f'Fila {numero}: número decimal inválido') from exc
            if not tamano.is_finite() or not tiempo.is_finite() or tamano <= 0 or tiempo <= 0:
                raise ValueError(f'Fila {numero}: tamaño y duración deben ser finitos y positivos')
            if not fila['contexto'].strip():
                raise ValueError(f'Fila {numero}: falta contexto de la medición')
            identificadores.add(identificador)
            tamanos.append(tamano)
            tiempos.append(tiempo)
    if not tiempos:
        raise ValueError('El archivo no contiene mediciones')
    ordenados = sorted(tiempos)
    rango = int((Decimal('0.95') * len(tiempos)).to_integral_value(rounding=ROUND_CEILING))
    tiempo_total = sum(tiempos, Decimal(0))
    volumen_total = sum(tamanos, Decimal(0))
    tasas = [tamano * 1000 / tiempo for tamano, tiempo in zip(tamanos, tiempos)]
    return {
        'muestras': len(tiempos),
        'media_ms': str(tiempo_total / len(tiempos)),
        'mediana_ms': str(median(tiempos)),
        'p95_rango_mas_proximo_ms': str(ordenados[rango - 1]),
        'rango_p95_contando_desde_uno': rango,
        'volumen_total_mib': str(volumen_total),
        'duracion_total_ms': str(tiempo_total),
        'caudal_agregado_mib_s': str(volumen_total * 1000 / tiempo_total),
        'media_de_tasas_individuales_mib_s': str(sum(tasas, Decimal(0)) / len(tasas)),
        'nota': 'Estadísticas de los datos de entrada; no se ha ejecutado una prueba de red.',
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv', type=Path)
    argumentos = parser.parse_args()
    try:
        resultado = analizar(argumentos.csv)
    except DecimalException:
        parser.exit(2, 'Error: valores fuera del rango numérico admitido para los cálculos.\n')
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        parser.exit(2, f'Error: {exc}\n')
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
