from sklearn.neighbors import KNeighborsClassifier
import numpy as np
data = np.array([
    [1, 2,3, 0],
    [2, 3, 4,0],
    [3, 1, 5,1],
    [5, 8,6, 1],
])
X = data[:, :-1]
y = data[:, -1]
new_patient_features = [float(input(f"Enter feature {i+1}: "))
                        for i in range(X.shape[1])]
k = int(input("Enter the value of k (number of neighbors): "))
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(X, y)
predicted_class = knn_classifier.predict([new_patient_features])

if predicted_class == 0:
    print("Predicted class: No condition")
else:
    print("Predicted class: Condition")
