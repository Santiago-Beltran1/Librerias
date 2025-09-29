import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

n = 100
df = pd.DataFrame({
    'tenure': np.random.randint(1,60,n),
    'llamadas_soporte': np.random.randint(0,5,n),
    'premium': np.random.randint(0,2,n),
})
df['churn'] = (df['tenure']<20) | (df['llamadas_soporte']>3)

X, y = df[['tenure','llamadas_soporte','premium']], df['churn']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)
clf = RandomForestClassifier().fit(X_train,y_train)

print(classification_report(y_test, clf.predict(X_test)))
