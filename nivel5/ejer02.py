import matplotlib.pyplot as plt
import seaborn as sns
people = ["Bryan","Martin","Ruth","Emilio","Jordi","Oscar","Julián"]
num_cars = [1, 2, 1, 3, 2, 1, 2]

fig, axes = plt.subplots(1, 4, figsize=(30,5))

axes[0].bar(people, num_cars, color="skyblue")
axes[0].set_title("Personas y coches")
axes[0].set_xlabel("Propietario")
axes[0].set_ylabel("Número de coches")

axes[1].pie(num_cars, labels=people, autopct='%1.1f%%')
axes[1].set_title("Distribución de coches")

axes[2].plot(people, num_cars, marker='o', color="green")
axes[2].set_title("Número de coches por persona")
axes[2].set_xlabel("Propietario")
axes[2].set_ylabel("Número de coches")

axes[3].scatter( people, num_cars, color='purple')
axes[3].set_title("Coches")
axes[3].set_xlabel("Dueños")
axes[3].set_ylabel("cantidad coches")

plt.suptitle("Comparación de gráficos de coches")
plt.tight_layout()
plt.show()