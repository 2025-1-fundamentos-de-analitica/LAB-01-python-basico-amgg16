"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
  ruta_archivo = "files/input/data.csv"

  asociaciones = {}

  with open(ruta_archivo, "r") as archivo:
    for linea in archivo:
        columnas = linea.split("\t")

        letra = columnas[0]
        valor = int(columnas[1])  

        if valor in asociaciones:
            asociaciones[valor].append(letra)
        else:
            asociaciones[valor] = [letra]

  # Convertir a lista de tuplas y ordenar por valor de columna 2
  lista = list(asociaciones.items()) #.items() = (clave, valor).
  lista.sort()
  return lista
