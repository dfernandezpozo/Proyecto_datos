import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


notes = np.random.uniform(4, 10, 50)

sns.histplot(notes, kde=True, bins=10, color='green')


plt.title("Distribución de notas (entre 4 y 10)")
plt.xlabel("Nota")
plt.ylabel("Freqüencia")


plt.show()

    

