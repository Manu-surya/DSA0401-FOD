item_prices = [2.3,1.5,3.5,4.8]
quantities = [1,2,3,4]
discount_rate = 15 
tax_rate = 10  
a= sum(price * quantity for price, quantity in zip(item_prices, quantities))
dis_amt= (discount_rate / 100) * a
b = a- dis_amt
tax_amt = (tax_rate / 100) * b
final = b+ tax_amt
print("Total Cost Before Discounts: $",a)
print("Discount Amount: $", dis_amt)
print("Total Cost After Discounts: $", b)
print("Tax Amount: $", tax_amt)
print("Final Total Cost: $", final)
