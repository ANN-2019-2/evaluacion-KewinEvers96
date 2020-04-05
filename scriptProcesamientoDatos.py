import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


##
## Praparación de los precios
##
preciosDias = []
preciosDeflectados = []
max =0
##
## RECOGE LOS INDICES DE CADA AÑO DESDE 1995 - 2018, para la DEFLACTACIÓN
##
with open("datos/IPCs_Anuales.csv", "rb") as file:
    ipcs = pd.read_csv(file)
    ipcs = ipcs.to_numpy()[:, 1:]
    file.close()

ipcs[:, 1] = ipcs[:, 1] / 100
n = 0

## ==================================================
##          LISTADO DE LOS DATOS
##          Y DEFLACTACIÓN
## ==================================================
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
        preciosDias.append(promedio)
        # Deflectamos los precios
        promedio = promedio * (ipcs[-1, 1] / ipcs[n, 1])
        preciosDeflectados.append(promedio)
    n += 1
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
        # Precios deflectados
        promedio = promedio * (ipcs[-1, 1] / ipcs[n, 1])
        preciosDeflectados.append(promedio)
    n+=1
preciosDeflectados = np.nan_to_num(np.array(preciosDeflectados))
# preciosDeflectados = np.log(preciosDeflectados)
# preciosDeflectados = preciosDeflectados ** (1/4)

## ========================================
##         GRÁFICA PRECIOS DEFLECTADOS
## ========================================
# plt.title("Precios entre 1995 y 2018")
# plt.plot([dia for dia in range(len(preciosDias))], preciosDias, color= 'black', label = "valor")
# plt.plot([dia for dia in range(len(preciosDeflectados))], preciosDeflectados, color = 'red', label = "precios deflectados")
# plt.grid(True)
# plt.legend()
# plt.show()


class AdalineTS:
    
    def __init__ (self,
                    P = None,
                    learning_rate = 0.0001):
            self.P = P 
            self.learning_rate = learning_rate
            self.X = []
            self.coef_ = [0.0] * P
            self.intercept_ = 0.0
    
    def predict(self):
        if len(self.X) < self.P:
            return None
        
        X = np.array(self.X)
        u = np.dot(X, self.coef_) + self.intercept_
        return u

    def fit(self, d):
        y = self.predict()
        if y is not None:
            e = d - y
            self.coef_ += 2 *  self.learning_rate* e * np.array(self.X)
            self.intercept_ += 2 * self.learning_rate  * e
        self.X.append(d)

        if len(self.X) > self.P:
            self.X.pop(0)

adaline = AdalineTS(
    P = 5,
    learning_rate = 0.000000025)

forecast = []
for t, z in enumerate(preciosDeflectados):
    forecast.append(adaline.predict())
    adaline.fit(z)
plt.plot(forecast, color = "red", label ="predicciones")
plt.plot(preciosDeflectados, color = "black")
plt.show()