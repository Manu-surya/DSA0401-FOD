import numpy as np

house_data = np.array([
    [3, 1200, 250000],
    [4, 1500, 300000],
    [5, 1800, 350000],
    [4, 1600, 280000],
    [5, 2000, 400000]
])
bedrooms_column = house_data[:, 0] 
houses_with_more_than_four_bedrooms = house_data[bedrooms_column > 4]
avg_sale_price = np.mean(houses_with_more_than_four_bedrooms[:, 2])  
print("Average sale price of houses with more than 4 bedrooms:", avg_sale_price)
