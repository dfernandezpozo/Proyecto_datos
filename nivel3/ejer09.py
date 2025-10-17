import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Hacemos un dataFrame de pandas e indicamos
# la media , desviación y el total de números aleatorios
# que se van a generar

notes = pd.DataFrame({
    "Matemáticas": np.random.normal(7, 1.5, 50),
    "Historia": np.random.normal(6.5, 1, 50),
    "Inglés": np.random.normal(7.5, 0.8, 50)
})

sns.boxplot(data=notes, palette="pastel")
plt.title("Distribución de notas por asignatura")
plt.show()
