"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():

    with open('clusters_report.txt') as report:
        linea = report.readlines()
 
    linea = linea[4:]

    lista = [0, 0, 0, ""]
    lista2= []
    

    for elem in linea:
        if re.match("^ +[0-9]+ +", elem):
            num, cant, porc, *pal = elem.split()
    
            lista[0] = int(num)
            lista[1] = int(cant)
            lista[2] = float(porc.replace(",",".")) 

            pal.pop(0) 
            pal = " ".join(pal)
            lista[3] += " " + pal

        if re.match("^ +[a-z]", elem):
            pal = elem.split()
            pal = " ".join(pal)
            lista[3] += " " + pal

        if re.match("^\n", elem) or re.match("^ +$", elem):
            lista[3] = lista[3].replace(",",".") 
            lista2.append(lista)
            lista = [0, 0, 0, ""]

    salida = pd.DataFrame(lista2, columns = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"])
    
    return salida


    