"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
  ruta_archivo = "files/input/data.csv"

  conteo_por_letra = {}

  with open(ruta_archivo, "r") as archivo:
    for linea in archivo:
        columnas = linea.split("\t")
        letra = columnas[0]
        
        # Contar la letra
        if letra in conteo_por_letra:
            conteo_por_letra[letra] += 1
        else:
            conteo_por_letra[letra] = 1

  # Convertir a lista de tuplas y ordenar alfabéticamente
  lista = list(conteo_por_letra.items()) #.items() = (clave, valor).
  lista.sort()
  return lista