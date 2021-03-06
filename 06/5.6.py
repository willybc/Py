# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:14:38 2020

@author: WILLY
"""

import csv
'''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
'''

def parse_csv(nombre_archivo, select=False, types=[str,float], has_headers=True, silence_errors=False):
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        
        if select and not has_headers:
            raise RuntimeError("Para seleccionar, necesito encabezados")
        
        if has_headers and select:
            # Lee los encabezados del archivo
            encabezados = next(filas)
    
            # Si se indicó un selector de columnas,
            # buscar los índices de las columnas especificadas.
            # Y achicar el conjunto de encabezados para diccionarios
            
            if select:
                indices = [encabezados.index(ncolumna) for ncolumna in select]
                encabezados = select
            else:
                indices = []
    
            registros = []
            for fila in filas:
                try:
                    if not fila:    # Saltear filas vacías
                        continue
                    #Conversion de tipo
                    if types:
                        fila = [func(val) for func, val in zip(types, fila) ] 
                    # Filtrar la fila si se especificaron columnas
                    if indices:
                        fila = [fila[index] for index in indices]
        
                    # Armar el diccionario
                    registro = dict(zip(encabezados, fila))
                    registros.append(registro)
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {fila}: No pude convertir {filas}. Motivo {e}')
            
        if has_headers == False:
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                #Conversion de tipo
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ] 
                # Armar el diccionario
                registros.append((fila[0],fila[1]))
    return registros

camion = parse_csv('../Data/missing.csv',select=['nombre', 'cajones'],types=[str, int], silence_errors=True)
print(camion)

