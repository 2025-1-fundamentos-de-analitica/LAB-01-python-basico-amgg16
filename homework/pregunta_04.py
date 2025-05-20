"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
  ruta_archivo = "files/input/data.csv"

  conteo_por_mes = {}

  with open(ruta_archivo, "r") as archivo:
    for linea in archivo:
        columnas = linea.split("\t")
        fecha = columnas[2].split("-")
        mes=fecha[1]
        
        # Contar los meses
        if mes in conteo_por_mes:
            conteo_por_mes[mes] += 1
        else:
            conteo_por_mes[mes] = 1

  # Convertir a lista de tuplas y ordenar alfabéticamente
  lista = list(conteo_por_mes.items()) #.items() = (clave, valor).
  lista.sort()
  return lista