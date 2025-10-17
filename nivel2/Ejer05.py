import matplotlib.pyplot as plt

sports=["Futbol","Basquet","Volei"]
boys=[12,10,5]
girls=[6,8,12]


plt.figure(figsize=(15,10), dpi=80)
plt.bar(sports, boys,label="chicos", color="black")
plt.bar(sports,girls,label="chicas",color="pink")
plt.title("Deportes")
plt.xlabel("Deportes")
plt.ylabel("Número de participantes")
plt.show()


