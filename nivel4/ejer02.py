import numpy as np
import matplotlib.pyplot as plt

jornadas = np.arange(1, 21)
puntos = np.random.randint(0, 4, size=20)

plt.plot(jornadas, puntos, marker='o', linestyle='-', color='blue')
max_index = np.argmax(puntos)
plt.plot(jornadas[max_index], puntos[max_index], 'ro', markersize=10)
plt.title("Puntos ganados por jornada")
plt.xlabel("Jornada")
plt.ylabel("Puntos")
plt.show()
