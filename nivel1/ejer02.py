import matplotlib.pyplot as plt
people=["Bryan","Martin","Ruth","Emilio","Jordi","Oscar","Julián"]
fruits=["Banana","Coco","Papaya","Naranja","Melón","Manzana","Dragon Fruit"]
plt.figure(figsize=(10,7), dpi=80)
plt.bar(people,fruits,color="purple")
plt.title("Consumo de fruta")
plt.xlabel("Tipo de fruta")
plt.ylabel("Cantidad")
plt.show()
