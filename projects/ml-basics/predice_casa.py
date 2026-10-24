import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#datos de enetrenamiento -> metros cuadrados vs precio.

x = np.array([50, 100, 150]).reshape(-1,1)
y = np.array([50000, 100000, 150000])

#Entrenamos el modelo
modelo = LinearRegression()
modelo.fit(x,y)

#mostrar el patron aprendido
pendiente = modelo.coef_[0]
interseccion = modelo.intercept_

print("patron aprendido por el modelo:")
print(f"precio = ({pendiente:.0f} * Metros cuadrados) + {interseccion:.0f}\n")

# realizamos una prediccion para una casa de 120 m2
casa_nueva = np.array([[120]])
precio_predicho = modelo.predict(casa_nueva)

print(f'Prediccion para 120 m2: ${precio_predicho[0]:,.2f}')
