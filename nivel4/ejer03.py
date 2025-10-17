import pandas as pd
df = pd.read_csv('projecte_dades/nivel4/notas.csv')
import matplotlib.pyplot as plt
import seaborn as sns


# Barras
plt.bar(df['Alumno'], df['Matematicas'], color='skyblue')
plt.title("Notas de Matemáticas")
plt.xlabel("Alumno")
plt.ylabel("Nota")
plt.show()

# Gráfico de lineas
plt.plot(df['Alumno'], df['Matematicas'], marker='o', color='green')
plt.title("Evolución de notas de Matemáticas")
plt.xlabel("Alumno")
plt.ylabel("Nota")
plt.show()

# Histograma
sns.histplot(df['Matematicas'], kde=True, color='purple')
plt.title("Distribución de notas de Matemáticas")
plt.xlabel("Nota")
plt.ylabel("Frecuencia")
plt.show()

