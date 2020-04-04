import pandas as pd 
import numpy as np

ipcsAnuales = []
years = []
dictio = {}
with open("1.1.INF_Serie histórica Meta de inflación IQY.xlsx", "rb") as file:
    datos = pd.read_excel(file)
    datos = datos[6:]
    datosN = datos.to_numpy()

    _, column = np.where(datosN == "Inflación total 1")

    row, _ = np.where(datosN == 201812)

    row0 = row[0]
    
    year = 2018
    suma = 0
    while(year >= 1995):
        suma += datosN[row[0], column[0]]
        row += 1
        
        if ((row[0] - row0) % 12) == 0:
            ipcsAnuales.append(round(suma / 12, 4))
            years.append(year)
            suma = 0
            year -= 1
    dictio['Year'] = years
    dictio['IPC'] = ipcsAnuales

newDoct = pd.DataFrame(dictio, columns = ['Year', 'IPC'])
newDoct.to_csv("IPCs_Anuales.csv")