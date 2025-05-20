"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
  ruta_archivo = "files/input/data.csv"

  valores_por_clave = {}

  with open(ruta_archivo, "r") as archivo:
    for linea in archivo:
        columnas = linea.split("\t")

        dicc = columnas[4].split(",")  #columna 5

        for dic in dicc: #cada diccionario en esa columna
            clave, valor = dic.split(":") 
            valor = int(valor)

            if clave in valores_por_clave:
                valores_por_clave[clave].append(valor)
            else:
                valores_por_clave[clave] = [valor]

  #lista de tuplas (letra, max, min)
  resultado = []
  for clave in valores_por_clave:
    minimo = min(valores_por_clave[clave])
    maximo = max(valores_por_clave[clave])
    resultado.append((clave, minimo, maximo))

  # Ordenar alfabéticamente por clave
  resultado.sort()

  return resultado
