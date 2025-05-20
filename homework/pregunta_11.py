"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
  ruta_archivo = "files/input/data.csv"

  valores_por_clave = {}

  with open(ruta_archivo, "r") as archivo:
    for linea in archivo:
        columnas = linea.split("\t")

        letras = columnas[3].split(",")  #columna 4

        for letra in letras: #cada diccionario en esa columna
            if letra in valores_por_clave:
                valores_por_clave[letra]+=int(columnas[1])
            else:
                valores_por_clave[letra] = int(columnas[1])

  return valores_por_clave
