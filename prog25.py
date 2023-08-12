from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X = iris.data
y = iris.target
clf = DecisionTreeClassifier()

clf.fit(X, y)

sepal_length = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_length = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

predicted_species = clf.predict([[sepal_length, sepal_width, petal_length, petal_width]])


species_names = iris.target_names
predicted_species_name = species_names[predicted_species[0]]

print("Predicted species of the new flower:", predicted_species_name)
