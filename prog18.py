import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 
data={'age':[23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61],
      '%fat':[9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]}
df=pd.DataFrame(data)
print(df)
a=df[['age','%fat']].mean()
print("mean",a)
b=df[['age','%fat']].median()
print("medain",b)
c=df[['age','%fat']].std()
print("standard",c)
df.plot(kind='box',x='age',y='%fat',title="ageVSfat",color='r',grid='True')
df.plot(kind='scatter',x='age',y='%fat',title="ageVSfat",color='r',grid='True') 
plt.show()
stats.probplot(data['age'], plot=plt) 
plt.title("Q-Q Plot of Age") 
plt.xlabel("Theoretical Quantiles") 
plt.ylabel("Sample Quantiles") 
plt.show() 
plt.figure(figsize=(8, 6)) 
stats.probplot(data['%fat'], plot=plt) 
plt.title("Q-Q Plot of %Fat") 
plt.xlabel("Theoretical Quantiles") 
plt.ylabel("Sample Quantiles") 
plt.show()
