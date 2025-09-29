import pandas as p2
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

datos = {
    "nombre": ["Santiago", "Andrés", "Martha", "Xiomara", "Marlon", "Camilo", "Luz", "Nicol", "Kevin", "Brayan", "Ximena", "Johana","David", "Alejandro", "Valery"],
    "edad": [10, 20, 30, 40, 50, 15, 25, 35, 45, 55, 12, 17, 34, 22, 5],
    "ciudad": ["Mosquera", "Funza", "Madrid", "Facatativa", "Fontibón", "Bogotá", "Medellín", "Tunja", "Villao", "Bucaramanga", "Barranquilla", "Cali", "Manizales", "Envigado", "Pereira"],
    "salario": [1450000, 2000000, 3000000, 4000000, 5000000, 2500000, 3500000, 4500000, 1500000, 5500000, 6000000, 1900000, 2700000, 3300000, 10000000]
}

df = p2.DataFrame(datos)
plt.style.use("default")
sns.set_palette("husl")
plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
plt.scatter(df["edad"], df["salario"], s=100, alpha=0.7, c="red")
plt.title("EDAD VS SALARIO")
plt.xlabel("Edad")
plt.ylabel("salario")
plt.tight_layout()
plt.show()