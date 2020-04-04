import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


##
## Praparación de los precios
##
preciosDias = []
max =0

for year in range(1995, 2016):
# year = 1995
    with open("datos/precios/Precio_Bolsa_Nacional_($kwh)_"+ str(year) +".xlsx", "rb") as file:

        datos = pd.read_excel(file)
        datosNumpy = datos.to_numpy()
        datosNumpy = np.nan_to_num(datosNumpy)
        # Encontrar el valor "Fecha"
        row, column = np.where(datosNumpy == "Fecha")
        row +=1
        column +=1
        datosNumpy = datosNumpy[row[0]:, column[0]:]
        if year >= 2010:
            datosNumpy = datosNumpy[:, :-2]
        if isinstance(datosNumpy[0, -1], str):
            datosNumpy = datosNumpy[:, :-1]
        for i in range(datosNumpy.shape[0]):
            promedio = sum(datosNumpy[i,:])/ datosNumpy.shape[1]
            preciosDias.append(promedio)
        file.close()
for year in range(2016, 2019):
    with open("datos/precios/Precio_Bolsa_Nacional_($kwh)_" + str(year) + ".xls", "rb") as file:
        datos = pd.read_excel(file)
        datosNumpy = datos.to_numpy()
        datosNumpy = np.nan_to_num(datosNumpy)

        row, column = np.where(datosNumpy == "Fecha")
        row += 1
        column += 1
        datosNumpy = datosNumpy[row[0]: , column[0]:]
        datosNumpy = datosNumpy[:, :-2]
        
        for i in range(datosNumpy.shape[0]):
            promedio = sum(datosNumpy[i, :]) / datosNumpy.shape[1]
            preciosDias.append(promedio)

        file.close()
plt.title("Precios entre 1995 - 2018")
plt.plot([dia for dia in range(len(preciosDias))], preciosDias, color= 'black', label = "valor")
plt.legend()
plt.show()