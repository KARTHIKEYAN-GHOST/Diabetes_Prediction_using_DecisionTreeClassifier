from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
import graphviz
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:\Users\karth\OneDrive\Documents\PLACEMENT_TRAINING_jan_feb\DecisionTree_Implementation\diabetes.csv")
print(df.info())

gp=df.groupby('Age')['Pregnancies'].sum()
gp.plot(kind="bar")
plt.show()

x=df.drop('Outcome', axis=1)
y=df['Outcome']
x_tr,x_te,y_tr,y_te=train_test_split(x,y,random_state=24)
model=DecisionTreeClassifier()
model.fit(x_tr,y_tr)
y_te=model.predict(x_te)

graphviz.Source(export_graphviz(model,feature_names=x.columns,filled=True))