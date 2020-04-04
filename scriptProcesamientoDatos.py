import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


##
## Praparación de los precios
##
preciosDias = []
max =0
with open("datos/IPCs_Anuales.csv", "rb") as file:
    ipcs = pd.read_csv(file)
    ipcs = ipcs.to_numpy()[:, 1:]
    file.close()

ipcs[:, 1] = ipcs[:, 1] / 100
n = ipcs.shape[0] -1
precios = [100]

while( n >= 0):
    precios.append(round(precios[-1] * (ipcs[n, 1] + 1), 5))
    n -= 1
print(len(precios), ipcs.shape[0])
for year in range(1995, 2016):
# year = 1995
    with open("datos/precios/Precio_Bolsa_Nacional_($kwh)_"+ str(year) +".xlsx", "rb") as file:

        datos = pd.read_excel(file)
        datosNumpy = datos.to_numpy()
        datosNumpy = np.nan_to_num(datosNumpy)
        file.close()
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
        # Deflectamos los precios
        preciosDias.append(promedio)
    
for year in range(2016, 2019):
    with open("datos/precios/Precio_Bolsa_Nacional_($kwh)_" + str(year) + ".xls", "rb") as file:
        datos = pd.read_excel(file)
        datosNumpy = datos.to_numpy()
        datosNumpy = np.nan_to_num(datosNumpy)
        file.close()
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