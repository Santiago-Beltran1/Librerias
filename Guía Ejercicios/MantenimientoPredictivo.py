import numpy as np, pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

n=200
df=pd.DataFrame({
    's1': np.random.randn(n).cumsum(),
    's2': np.random.randn(n),
})
df['falla'] = (df['s1']>10).astype(int)

X,y=df[['s1','s2']],df['falla']
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.3,random_state=0)
clf=RandomForestClassifier().fit(Xtr,ytr)

print("Predicciones:", clf.predict(Xte[:10]))
