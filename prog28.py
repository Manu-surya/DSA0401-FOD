from sklearn.cluster import KMeans
import numpy as np
data = np.array([
    [2, 3],  
    [1, 2],  
    [6, 8],   
    [5, 7],   
])
n= [float(input(f"Enter feature {i+1} for the new customer: "))
for i in range(data.shape[1])]
c = int(input("Enter the number of clusters (segments): "))
predicted_segment = KMeans(n_clusters=c, n_init=20).fit(data).predict([n])
print(f"The new customer belongs to segment {predicted_segment[0]}")
