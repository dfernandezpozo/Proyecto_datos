import random
import matplotlib.pyplot as plt

# Lista de alumnos
personas = ["Pepe","Juan","Pedro","Cata","Laura","Lucía","Jorge","Martín","Brayan","Manolo"]

# Generar una nota aleatoria para cada alumno
notas_alumnos = [round(random.uniform(0,10),2) for _ in personas]

# Crear la figura y un único eje
fig, ax = plt.subplots(figsize=(10,6))

# Gráfico de barras
ax.bar(personas, notas_alumnos, color="skyblue", edgecolor="black")
ax.set_title("Notas por alumno")
ax.set_ylabel("Nota")
ax.set_ylim(0, 10)  # límites de 0 a 10 en el eje Y
ax.tick_params(axis='x', rotation=45)

plt.show()
