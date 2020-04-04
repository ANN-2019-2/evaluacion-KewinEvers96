import pandas as pd 
import numpy as np

ipcsAnuales = []
years = []
dictio = {}
#
# Coger los indices de cada año del mes de enero. Y tomarlos como los inidices para el IPC anual
#
with open("1.2.5.IPC_Serie_variaciones.xlsx", "rb") as file:
    datos = pd.read_excel(file)
    datos = datos[6:]
    datosN = datos.to_numpy()
    file.close()
_ , column = np.where(datosN == "Inflación total 1")

rowInit, _ = np.where(datosN == 201812)
finalRow, _ = np.where(datosN == 199501)
row0 = finalRow[0]

year = 1995
suma = 0
while(year <= 2018):
    years.append(year)
    ipcsAnuales.append(datosN[finalRow, 1][0])
    finalRow -= 12
    year += 1
dictio['Year'] = years
dictio['IPC'] = ipcsAnuales

newDoct = pd.DataFrame(dictio, columns = ['Year', 'IPC'])
newDoct.to_csv("IPCs_Anuales.csv")