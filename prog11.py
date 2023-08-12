import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\ghant\\Downloads\\sal.csv")
print(df)
df.plot(kind='line',x='month',y='sales',title='sales of this month',color='r',grid='True')
plt.show()
df.plot(kind='scatter',x='month',y='sales',title='sales of this month',color='b',grid='True')
plt.show()
df.plot(kind='bar',x='month',y='sales',title='sales of this month',color='g',grid='True')
plt.show()
