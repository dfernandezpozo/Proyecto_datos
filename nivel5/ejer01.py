
# Voy a usar el gráfico del nivel 1 ejercicio 1

import matplotlib.pyplot as plt
months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
temperatures = [12.3,12.4,14.2,16.4,19.6,26.1,28.5,26.5,23.2,17.8,13.4,11.6]
plt.figure(figsize=(10,5), dpi=80)
plt.plot(months,temperatures,marker="o",color="orange", label="temperaturas")
plt.title("Temperatura media")
plt.title("Esto es una modificación")
plt.suptitle("Modificado el título y color de la figura")
plt.xlabel("Meses")
plt.ylabel("Media")
plt.legend()
plt.savefig("graf.png")
plt.show()

