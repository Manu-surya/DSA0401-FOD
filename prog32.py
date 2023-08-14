import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
data = np.array([[1400, 3, 300000],
                    [1600, 3, 330000],
                    [1700, 3, 350000],
                    [1875, 2, 270000],
                    [1100, 2, 220000],
                    [1550, 4, 350000]])

X = data[:, :-1]
y = data[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

new_area = float(input("Enter the area of the new house: "))
new_bedrooms = int(input("Enter the number of bedrooms in the new house: "))

new_house_features = np.array([[new_area, new_bedrooms]])
predicted_price = model.predict(new_house_features)
location = input(f"Enter location : ")
print(location)
print(f"Predicted price for the new house: ${predicted_price[0]:.2f}")

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)  
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'Root Mean Squared Error (RMSE): {rmse:.2f}')
print(f'Mean Absolute Error (MAE): {mae:.2f}')
print(f'R-squared (R2): {r2:.2f}')


plt.scatter(data[ :,0], data[:,2])
plt.xlabel('House Size')
plt.ylabel('House Price')
plt.title('Bivariate Analysis - House Size vs. House Price')
plt.show()
