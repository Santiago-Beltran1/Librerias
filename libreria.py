import pandas as pd

datos = {
    "nombre": ["Santiago", "Andrés", "Martha", "Xiomara", "Marlon", "Camilo", "Luz", "Nicol", "Kevin", "Brayan", "Ximena", "Johana","David", "Alejandro","Valery"],
    "edad": [10, 20, 30, 40, 50, 15, 25, 35, 45, 55, 12, 17, 34, 22, 5],
    "ciudad": ["Mosquera", "Funza", "Madrid", "Facatativa", "Fontibón", "Bogotá", "Medellín", "Tunja", "Villao", "Bucaramanga", "Barranquilla", "Cali", "Manizales", "Envigado", "Pereira"],
    "salario": [1450000, 2000000, 3000000, 4000000, 5000000, 2500000, 3500000, 4500000, 1500000, 5500000, 6000000, 1900000, 2700000, 3300000, 10000000]
}

df = pd.DataFrame(datos)
print(df)
print(df.shape)
print(df.columns.tolist())
print(df.head(3))
print(df.tail(2))
print(df.describe())
print(df["nombre"])
print(df["edad"])
print(df["ciudad"])
print(df["salario"])

edad = df[df["edad"] > 20]
print(edad)

df.to_csv("Empleado.csv", index=False)