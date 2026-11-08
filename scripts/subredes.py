#!/usr/bin/env python3
"""Calculadora didáctica de prefijos IPv4/IPv6, sin acceso a la red."""

import argparse
import ipaddress
import json


def calcular(cidr: str) -> dict:
    interfaz = ipaddress.ip_interface(cidr)
    red = interfaz.network
    resultado = {
        "entrada": str(interfaz),
        "version": red.version,
        "red": str(red.network_address),
        "prefijo": red.prefixlen,
        "numero_direcciones": red.num_addresses,
    }
    if red.version == 4:
        if red.prefixlen < 31:
            primero = red.network_address + 1
            ultimo = red.broadcast_address - 1
            hosts = red.num_addresses - 2
            nota = "Subred IPv4 ordinaria: red y broadcast excluidos."
        else:
            primero = red.network_address
            ultimo = red.broadcast_address
            hosts = red.num_addresses
            nota = (
                "/31: dos extremos de un enlace punto a punto (RFC 3021)."
                if red.prefixlen == 31 else
                "/32: una dirección individual; no es una LAN convencional."
            )
        resultado.update({
            "mascara": str(red.netmask),
            "limite_superior": str(red.broadcast_address),
            "broadcast": str(red.broadcast_address) if red.prefixlen < 31 else None,
            "primer_host": str(primero),
            "ultimo_host": str(ultimo),
            "hosts_segun_convencion": hosts,
            "nota": nota,
        })
    else:
        resultado.update({
            "limite_superior": str(red[-1]),
            "broadcast": None,
            "nota": (
                "IPv6 no tiene broadcast. Se muestra el intervalo matemático del "
                "prefijo, sin deducir hosts utilizables: existen direcciones y "
                "funciones especiales según el contexto."
            ),
        })
    return resultado


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cidr", help="Dirección/prefijo, por ejemplo 192.168.56.20/27")
    args = parser.parse_args()
    try:
        resultado = calcular(args.cidr)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
