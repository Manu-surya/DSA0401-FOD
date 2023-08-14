import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
def get_user_input(feature_names):
    features = []
    for feature_name in feature_names:
        feature_value = float(input(f"Enter the {feature_name}: "))
        features.append(feature_value)
    return np.array([features])
def main():
    X = np.array([[1000, 118, 18], [2000,92, 21], [3000, 234, 35]]) 
    y = np.array([25000, 30000, 20000])  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()

    model.fit(X_train, y_train)
    feature_names = ["engine_size", "horse power", "fuel efficiency"]

    new_car_features = get_user_input(feature_names)
    predicted_price =  model.predict(new_car_features)

    print(f"The predicted price of the new car is: {predicted_price[0]:.2f}")
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)  
    mae = mean_absolute_error(y_test, y_pred)

    print(f'Mean Squared Error (MSE): {mse:.2f}')
    print(f'Root Mean Squared Error (RMSE): {rmse:.2f}')
    print(f'Mean Absolute Error (MAE): {mae:.2f}')

if __name__ == "__main__":
    main()
