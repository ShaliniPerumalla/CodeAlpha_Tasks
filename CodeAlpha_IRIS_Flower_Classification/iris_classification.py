from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#Load data
iris=load_iris()
x=iris.data
y=iris.target

#split the data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

#create the model
model=KNeighborsClassifier(n_neighbors=3)

#train the model
model.fit(x_train,y_train)

sepal_length=float(input("sepal length(cm): "))
sepal_width=float(input("sepal width(cm): "))
petal_length=float(input("petal length(cm): "))
petal_width=float(input("petal width(cm): "))

input=[
    [sepal_length,
    sepal_width,
    petal_length,
    petal_width]
]

#predict the flower
y_pred=model.predict(input)


predicted_flower=iris.target_names[y_pred[0]]
print(f"\n predicted Flower: {predicted_flower}")
#accuracy caluclation
probability=model.predict_proba(input)
accuracy=max(probability[0])*100

print(f"Accuracy: {accuracy}")