import numpy as np
import matplotlib.pyplot as plt

redes = ["WhatsApp", "Instagram", "TikTok", "Twitter", "Facebook"]
usuarios = np.random.randint(50, 500, size=5)


plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.pie(usuarios, labels=redes, autopct="%1.1f%%", colors=["yellow","orange","pink","green","purple"])
plt.title("Uso de redes sociales (circular)")


plt.subplot(1,2,2)
plt.bar(redes, usuarios, color=["yellow","orange","pink","green","purple"])
plt.title("Uso de redes sociales")
plt.ylabel("Número de usuarios")

# He tenido que buscar el layout se descuadraba
plt.tight_layout()
plt.show()
