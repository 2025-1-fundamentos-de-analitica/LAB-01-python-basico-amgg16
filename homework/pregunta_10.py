"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
  ruta_archivo = "files/input/data.csv"

  tupla_cantidades = []

  with open(ruta_archivo, "r") as archivo:
    for linea in archivo:
        columnas = linea.split("\t")
        columna1=columnas[0]
        columna4=columnas[3].split(",")
        columna5=columnas[4].split(",")
        tupla_cantidades.append((columna1,len(columna4),len(columna5)))
    
    return tupla_cantidades
