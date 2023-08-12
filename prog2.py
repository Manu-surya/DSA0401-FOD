import numpy as np
import matplotlib as mt
sales=np.array([
    [100,200,300],
    [150,250,350],
    [400,450,500]
    ])
avg=np.mean(sales)
print('average product of sales:',avg)
g=mt.barplot(sales)
