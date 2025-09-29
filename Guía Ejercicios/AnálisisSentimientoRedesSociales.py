import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Datos pequeños
textos = ["Me encanta este producto", "Odio el servicio", "Está bien", "Malo y lento", "Muy bueno"]
y = ["pos","neg","neu","neg","pos"]

# Modelo
X = CountVectorizer().fit_transform(textos)
clf = LogisticRegression().fit(X,y)

# Prueba
nuevos = ["excelente", "muy malo"]
Xn = CountVectorizer(vocabulary=clf.classes_).fit_transform(nuevos)  # para ejemplo simple
print(clf.predict(Xn))
