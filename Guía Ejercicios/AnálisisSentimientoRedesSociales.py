# archivo: sentiment_demo.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# 1) ejemplo pequeño de textos (puedes reemplazar por tweets reales)
data = [
    ("Me encanta este producto, excelente calidad", "pos"),
    ("Muy mala atención, no vuelvo a comprar", "neg"),
    ("Servicio correcto, nada espectacular", "neu"),
    ("Adoro la nueva versión, superó mis expectativas", "pos"),
    ("No funciona, fallo tras fallo", "neg"),
    ("Entrega rápida, buen servicio", "pos"),
    ("Precio demasiado alto para lo que ofrece", "neg"),
    ("Ok, cumple su función", "neu"),
    ("Decepcionado, esperaba más", "neg"),
    ("Excelente, 100% recomendado", "pos")
]
df = pd.DataFrame(data, columns=['text','sentiment'])

# 2) vectorizar
vec = TfidfVectorizer(ngram_range=(1,2), min_df=1)
X = vec.fit_transform(df['text'])
y = df['sentiment']

# 3) train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=0)

# 4) entrenar clasificador
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

# 5) evaluar
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
print("Ejemplos predichos:")
for t, p in zip([df['text'].iloc[i] for i in X_test.indices[:5]], y_pred[:5]):
    print(t, "->", p)
