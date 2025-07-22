import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

# Charge le fichier XML
tree = ET.parse("results/resultat_fonction.xml")
root = tree.getroot()

# Récupère les données
x_values = [float(x.text) for x in root.find("xdata").findall("x")]
y_values = [float(y.text) for y in root.find("ydata").findall("y")]

# Trace le graphique
plt.plot(x_values, y_values, label="f(x)")
plt.title("Ma fonction")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.savefig("mon_graphique.png")
plt.show()