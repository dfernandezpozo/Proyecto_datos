import matplotlib.pyplot as plt
months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
temperatures = [12.3,12.4,14.2,16.4,19.6,26.1,28.5,26.5,23.2,17.8,13.4,11.6]
plt.figure(figsize=(15,10), dpi=80)
plt.plot(months,temperatures,marker="o",color="green")
plt.title("Temperatura media")
plt.xlabel("Meses")
plt.ylabel("Media")
plt.show()