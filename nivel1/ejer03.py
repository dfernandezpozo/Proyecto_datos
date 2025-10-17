import matplotlib.pyplot as plt
labels='Chrome','Firefox','Safari','Otros'
porcentaje=[65,20,10,5]
fig,ax=plt.subplots()
ax.pie(porcentaje,labels=labels, autopct='%1.1f%%')
plt.show()
