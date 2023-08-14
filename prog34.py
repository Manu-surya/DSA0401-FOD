import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
data = {
    "age": [30, 45, 25, 40, 55, 35],
    "gender": ["Male", "Female", "Male", "Female", "Male", "Female"],
    "blood_pressure": [120, 140, 110, 130, 150, 125],
    "cholesterol": [200, 240, 180, 220, 260, 210],
    "treatment_outcome": ["Good", "Bad", "Good", "Good", "Bad", "Good"]
}

df = pd.DataFrame(data)
print(df)
df_encoded = pd.get_dummies(df, columns=["gender"], drop_first=True)


X = df_encoded.drop("treatment_outcome", axis=1)
y = df_encoded["treatment_outcome"]

X_train, X_test, y_train, y_test = train_test_split(X.values, y.values, test_size=0.2, random_state=42)


knn_classifier = KNeighborsClassifier(n_neighbors=3)  
knn_classifier.fit(X_train, y_train)
print("the knn classifer\n",knn_classifier.predict(X_test))


y_pred = knn_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label="Good")
recall = recall_score(y_test, y_pred, pos_label="Good")
f1 = f1_score(y_test, y_pred, pos_label="Good")


print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
