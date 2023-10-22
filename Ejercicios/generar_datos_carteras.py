import numpy as np

N = 1000
n_activos = 10
medias = np.random.randn(n_activos) * 0.1 / 252
stds = np.abs(np.random.randn(n_activos)) * 0.1 / np.sqrt(252)

retornos = np.random.randn(N, n_activos) * stds[None, :] + medias[None, :]
np.save("datos/retornos_generados.npy", retornos)
