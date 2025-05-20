"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
  ruta_archivo = "files/input/data.csv"

  conteo_por_registro = {}

  with open(ruta_archivo, "r") as archivo:
    for linea in archivo:
        columnas = linea.split("\t")
        dicc = columnas[4].split(",")  #columna 5


        for dic in dicc: #cada diccionario en esa columna
            clave, valor = dic.split(":") 
            valor = int(valor)

            if clave in conteo_por_registro:
                conteo_por_registro[clave]+=1
            else:
                conteo_por_registro[clave] = 1
        
  return conteo_por_registro
    