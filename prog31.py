import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = pd.DataFrame({
    'age': [5,6,7,8,9],
    'income':[10000,20000,30000,40000,50000] ,
    'purchase_frequency':[3,4,5,6,7],
    'loyalty_points': [10,15,30,6,50]
})

selected_features = ['age', 'income', 'purchase_frequency', 'loyalty_points']
X = data[selected_features]

num_clusters = 3
n_init=10
random_state = 42
kmeans = KMeans(n_clusters=num_clusters, n_init=n_init,random_state=random_state)
clusters = kmeans.fit_predict(X) + 1

data['cluster'] = clusters
plt.scatter(data['age'], data['income'], c=data['cluster'], cmap='rainbow')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Customer Segmentation')
plt.colorbar(label='Cluster')
plt.show()

cluster_means = data.groupby('cluster')[selected_features].mean()
print(cluster_means)
