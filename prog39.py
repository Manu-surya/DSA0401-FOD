import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data={
    'customer_id':[1,2,3,4,5],
    'spending':[1000,2000,3000,4000,5000],
    'purchase_frequency':[5,6,7,11,2]}
data=pd.DataFrame(data)
print(data)
selected_features = ['customer_id', 'spending', 'purchase_frequency']
X = data[selected_features]

num_clusters = 3
n_init=10
random_state = 42
kmeans = KMeans(n_clusters=num_clusters, n_init=n_init,random_state=random_state)
clusters = kmeans.fit_predict(X) + 1

data['cluster'] = clusters
cluster_means = data.groupby('cluster')[selected_features].mean()
print(cluster_means)
plt.scatter(data['customer_id'], data['spending'], c=data['cluster'], cmap='rainbow')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Customer Segmentation')
plt.colorbar(label='Cluster')
plt.show()

