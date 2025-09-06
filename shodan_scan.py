#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de consulta a Shodan filtrando resultados en Guatemala.
Muestra información en consola y genera un resumen con:
- Total de direcciones IP encontradas
- Total de IPs por puerto abierto

Datos del estudiante:
Carnet: 202012345
Nombre: Juan Pérez
Curso: Seguridad Informática
Sección: B
"""

import shodan
from collections import defaultdict

# Reemplazar con tu API Key personal de Shodan
SHODAN_API_KEY = "TU_API_KEY"

def main():
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        # Consulta dirigida a Guatemala (sin usar org:)
        query = 'country:"GT"'
        results = api.search(query)

        print("=" * 60)
        print(f"Consulta ejecutada: {query}")
        print(f"Total de resultados: {results['total']}")
        print("=" * 60)

        ips = set()
        puertos = defaultdict(set)

        # Mostrar todos los resultados obtenidos
        for result in results['matches']:
            ip = result['ip_str']
            port = result['port']

            print(f"IP: {ip} | Puerto: {port} | Hostname: {result.get('hostnames')}")
            ips.add(ip)
            puertos[port].add(ip)

        # Resumen
        print("\n" + "=" * 60)
        print("📊 RESUMEN")
        print(f"Total de direcciones IP identificadas: {len(ips)}")
        print("Total de IPs por puerto abierto:")
        for puerto, ipset in puertos.items():
            print(f" - Puerto {puerto}: {len(ipset)} IPs")

        print("=" * 60)
        print("Carnet: 202012345")
        print("Nombre: Juan Pérez")
        print("Curso: Seguridad Informática")
        print("Sección: B")
        print("=" * 60)

    except shodan.APIError as e:
        print(f"Error en la consulta: {e}")

if __name__ == "__main__":
    main()
