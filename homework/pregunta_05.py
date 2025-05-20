"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
  ruta_archivo = "files/input/data.csv"

  valores_por_letra = {}

  with open(ruta_archivo, "r") as archivo:
    for linea in archivo:
        columnas = linea.split("\t")
        letra = columnas[0]
        valor = int(columnas[1])

        if letra in valores_por_letra:
            valores_por_letra[letra].append(valor)
        else:
            valores_por_letra[letra] = [valor]

  #lista de tuplas (letra, max, min)
  resultado = []
  for letra in valores_por_letra:
    max_val = max(valores_por_letra[letra])
    min_val = min(valores_por_letra[letra])
    resultado.append((letra, max_val, min_val))

  # Ordenar alfabéticamente por letra
  resultado.sort()

  return resultado