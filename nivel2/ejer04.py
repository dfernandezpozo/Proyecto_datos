import matplotlib.pyplot as plt
coches=[10,20,4,5,7,14]
motos=[2,5,7,8,1,6]
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio"]
plt.plot(meses,coches,color="blue" , label="coches")
plt.plot(meses, motos, color="red" , label="motos")

plt.title("Venta de productos")
plt.xlabel("Meses")
plt.ylabel("Unidades Vendidas")
plt.legend()
plt.show()