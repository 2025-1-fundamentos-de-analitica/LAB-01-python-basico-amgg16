"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
  ruta_archivo = "files/input/data.csv"

  suma_segunda_columna = 0

  # Abrir el archivo y procesar línea por línea
  with open(ruta_archivo, "r") as archivo:
    for columna in archivo:
        columnas = columna.split("\t")

        suma_segunda_columna += int(columnas[1])
  return suma_segunda_columna