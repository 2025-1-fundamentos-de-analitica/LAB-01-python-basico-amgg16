"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
  ruta_archivo = "files/input/data.csv"

  conteo_por_registro = {}

  with open(ruta_archivo, "r") as archivo:
    for linea in archivo:
        columnas = linea.split("\t")
        clave=columnas[0]
        conteo = columnas[4].split(",")  #columna 5

        suma=0
        for num in conteo: #cada diccionario en columna 5
            valor = num.split(":") 
            suma += int(valor[1])

        if clave in conteo_por_registro:
            conteo_por_registro[clave]+=suma
        else:
            conteo_por_registro[clave] = suma
        
  return conteo_por_registro