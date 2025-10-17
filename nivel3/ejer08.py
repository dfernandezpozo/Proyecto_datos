import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generamos un array de 50 valores entre 0 y 10
horas_estudio = np.random.uniform(0, 10, 50)
# Calculamos las notas y hacemos que la snotas no sean exactas
notas = 4 + 0.5 * horas_estudio + np.random.normal(0, 1, 50)
# Limitamos que las notas estén entre 0 y 10
notas = np.clip(notas, 0, 10)

sns.scatterplot(x=horas_estudio, y=notas, color='orange')
plt.title("Relación entre horas de estudio y notas")
plt.xlabel("Horas de estudio")
plt.ylabel("Notas")
plt.show()
