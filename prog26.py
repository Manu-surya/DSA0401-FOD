import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataset = [
    [1500, 3, 300000],
    [2000, 4, 400000],
    [1800, 3, 250000],
]

X = [[row[0], row[1]] for row in dataset]
y = [row[2] for row in dataset]

model = LinearRegression()

model.fit(X, y)

area = float(input("Enter the area: "))
bedrooms = int(input("Enter the number of bedrooms: "))

predicted_price = model.predict([[area, bedrooms]])

print("Predicted price of the new house:", predicted_price[0])

plt.scatter([row[0] for row in dataset], y, color='blue', label='Actual Prices')
plt.plot([row[0] for row in dataset], model.predict(X), color='red', label='Regression Line')
plt.scatter(area, predicted_price, color='green', marker='x', label='Predicted Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Housing Price Prediction')
plt.legend()
plt.show()
