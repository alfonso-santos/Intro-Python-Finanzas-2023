import numpy as np
import pandas as pd
import datetime

def generar_fecha_random(n):
    random_dates = []
    start_date = np.datetime64("2000-01-01")
    end_date = np.datetime64("2023-12-31")
    random_days = np.random.randint((end_date - start_date).astype(int), size=n)
    days = np.repeat(start_date, n) + random_days
    return days

N = 100000
n_productos = 20
n_ventas_max = 5
precio_producto = {}
for i in range(n_productos):
    precio_producto[i] = np.around(np.random.rand(1)[0] * 30, decimals=2)

fechas = generar_fecha_random(N)
productos = np.random.randint(n_productos, size=N)
ventas = np.random.randint(1, n_ventas_max, size=N)
precio_productos = np.array([precio_producto[i] for i in productos])

print(fechas.shape, productos.shape, ventas.shape, precio_productos.shape)

d = {"fecha": fechas, "producto": productos, "productos_vendidos": ventas, "precio_producto": precio_productos}
data = pd.DataFrame(data=d)
data.to_csv("datos/ventas_generadas.csv")
