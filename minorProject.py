## Loading the data
import pandas as pd

data=pd.read_csv("C:\\Users\\agarw\\Downloads\\archive (4)\\Titanic-Dataset.csv")
#print(data)

## Preprocessing the data
data.fillna(0,inplace=True)
data=pd.get_dummies(data)
#print(data.head())
data=data.drop(data.columns[7:],axis=1)

## Split the data
from sklearn.model_selection import train_test_split

X=data.drop("Survived",axis=1)
y=data['Survived']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=40)

## Model Training

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()
model.fit(X_train,y_train)

## Scaling

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Only fit-transform X_train

## Preparing ML model

import joblib
joblib.dump(model,'model.pkl')
joblib.dump(scaler,"scaler.pkl")