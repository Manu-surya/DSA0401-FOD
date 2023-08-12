import pandas as pd 
data = { 

    'property ID': [1, 2, 3, 4, 5, 6], 
    'loc': ['City A', 'City B', 'City A', 'City C', 'City B', 'City C'],
    'no of bedrooms': [3, 4, 3, 5, 2, 4], 
    'area in sqft': [1500, 1800, 1600, 2400, 1200, 2000], 
    'listing price': [250000, 320000, 280000, 420000, 180000, 380000]
} 
df = pd.DataFrame(data)
avg=df.groupby('loc')['listing price'].mean()
print("The Average :",avg)

largestarea = df[df['area in sqft'] == df['area in sqft'].max()]
print("Largest Area :",largestarea)

morethanfourbedrooms = df[df['no of bedrooms'] > 4]
number = len(morethanfourbedrooms)
print('more than four bedrooms:',number)
