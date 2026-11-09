#!/usr/bin/env python3
"""Compara lectura secuencial y acceso directo con seek en un archivo temporal.

Los registros sintéticos ocupan 16 bytes: entero little-endian de 4 bytes y
código ASCII de 12 bytes, completado con ceros. El directorio se elimina al salir.
"""

import json
from pathlib import Path
import struct
import tempfile


REGISTRO = struct.Struct('<I12s')
DATOS = [(1, 'PC-001'), (2, 'PC-002'), (3, 'PC-003')]


def empaquetar(identificador: int, codigo: str) -> bytes:
    texto = codigo.encode('ascii')
    if len(texto) > 12:
        raise ValueError('El código supera los 12 bytes del registro')
    return REGISTRO.pack(identificador, texto)


def desempaquetar(datos: bytes) -> tuple:
    if len(datos) != REGISTRO.size:
        raise ValueError('Registro incompleto')
    identificador, codigo = REGISTRO.unpack(datos)
    return identificador, codigo.rstrip(b'\0').decode('ascii')


def leer_secuencial(ruta: Path) -> list:
    resultado = []
    with ruta.open('rb') as entrada:
        while True:
            bloque = entrada.read(REGISTRO.size)
            if not bloque:
                return resultado
            resultado.append(desempaquetar(bloque))


def leer_directo(ruta: Path, indice: int) -> tuple:
    if type(indice) is not int or indice < 0:
        raise IndexError('El índice debe ser un entero no negativo')
    with ruta.open('rb') as entrada:
        entrada.seek(0, 2)
        tamano = entrada.tell()
        if tamano % REGISTRO.size:
            raise ValueError('El archivo contiene un registro incompleto')
        if indice >= tamano // REGISTRO.size:
            raise IndexError('Índice fuera del número de registros')
        entrada.seek(indice * REGISTRO.size)
        return desempaquetar(entrada.read(REGISTRO.size))


def demostrar() -> dict:
    with tempfile.TemporaryDirectory(prefix='smr-registros-') as directorio:
        ruta = Path(directorio) / 'equipos.bin'
        with ruta.open('wb') as salida:
            for identificador, codigo in DATOS:
                salida.write(empaquetar(identificador, codigo))
        secuencial = leer_secuencial(ruta)
        directo = leer_directo(ruta, 1)
        if secuencial != DATOS or directo != DATOS[1]:
            raise RuntimeError('Lecturas incompatibles con el contrato')
        try:
            leer_directo(ruta, 3)
        except IndexError:
            fuera_de_rango = 'rechazado'
        else:
            raise RuntimeError('Se esperaba rechazo del índice 3')
        return {'bytes_por_registro': REGISTRO.size, 'bytes_del_archivo': ruta.stat().st_size,
                'lectura_secuencial': secuencial, 'indice_directo': 1,
                'desplazamiento_directo_bytes': REGISTRO.size,
                'lectura_directa': directo, 'indice_3': fuera_de_rango,
                'nota': 'Archivo de ensayo creado y leído en un directorio temporal, retirado al terminar.'}


if __name__ == '__main__':
    print(json.dumps(demostrar(), ensure_ascii=False, indent=2))
