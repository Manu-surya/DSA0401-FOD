import numpy as np
sales_data = np.array([20000,30000,45000,50000])

tot_sales = np.sum(sales_data)
per_incr = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total sales for the year:", tot_sales)
print("Percentage increase from Q1 to Q4:", per_incr, "%")
