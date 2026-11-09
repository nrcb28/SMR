#!/usr/bin/env python3
"""Funciones puras y ejemplos de paso de argumentos; no lee ni escribe archivos."""

import json


def resumir(registros: list) -> dict:
    """Devuelve totales por código; rechaza duplicados y cantidades inválidas."""
    resultado = {}
    for registro in registros:
        if not isinstance(registro, dict):
            raise ValueError('Cada registro debe ser un diccionario')
        codigo = registro.get('codigo')
        cantidad = registro.get('cantidad')
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError('Código vacío o inválido')
        codigo = codigo.strip()
        if type(cantidad) is not int or cantidad < 0:
            raise ValueError('Cantidad debe ser un entero no negativo')
        if codigo in resultado:
            raise ValueError('Código duplicado: ' + codigo)
        resultado[codigo] = cantidad
    return resultado


def reasignar(datos: list) -> None:
    datos = []  # Reasigna el nombre local, sin modificar la lista recibida.


def agregar(datos: list, valor) -> None:
    datos.append(valor)  # Modifica el objeto mutable compartido con quien llama.


def demostrar() -> dict:
    inventario = resumir([{'codigo': '0012', 'cantidad': 2}, {'codigo': '0040', 'cantidad': 0}])
    datos = ['A']
    reasignar(datos)
    tras_reasignacion = list(datos)
    agregar(datos, 'B')
    return {'inventario': inventario, 'tras_reasignar': tras_reasignacion,
            'tras_mutar': datos, 'lista_vacia': resumir([])}


if __name__ == '__main__':
    print(json.dumps(demostrar(), ensure_ascii=False, indent=2))
