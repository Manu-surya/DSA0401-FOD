import pandas as pd
data = {
    'customer_id': [11,12,12,14,12,13,11],
    'order_date': ['08-12-2023', '2-08-2023', '2023-07-03', '2023-07-03', '2023-07-04', '2023-07-05', '2023-07-06'],
    'product_name': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'order_quantity': [3, 5, 2, 1, 2, 4, 3]
}
order_data = pd.DataFrame(data)
a= order_data['customer_id'].value_counts()
print('The total number of orders made by each customer:',a)
avg = order_data[['product_name','order_quantity']].groupby('product_name').mean()
print('Average order quantity for each product:',avg)
early= order_data['order_date'].min()
print('The earliest order:',early)
latest = order_data['order_date'].max()
print('The latest order :',latest)
