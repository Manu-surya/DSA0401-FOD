import pandas as pd
data = {
    'product_name': ['A', 'B', 'A', 'C', 'B', 'A', 'C','D','E','F'],
    'quantity_sold': [60,50,30,10,40,15,70,65,35,55]
}
sales_data = pd.DataFrame(data)
product_sales = sales_data.groupby('product_name')['quantity_sold'].sum()
sorted_product_sales = product_sales.sort_values(ascending=False)
top_5_products = sorted_product_sales.head(5)
print("Top 5 products sold the most in the past month:")
print(top_5_products)
