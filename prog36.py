import csv
import numpy as np
import matplotlib.pyplot as plt

def calculate_stock_variability(closing_prices):
    volatility = np.std(closing_prices)

    return volatility

def analyze_price_movements(volatility):
    if volatility < 10:
        return "Low variability: The stock price has been relatively stable."
    elif volatility >= 10 and volatility < 30:
        return "Moderate variability: The stock price has experienced some fluctuations."
    else:
        return "High variability: The stock price has been highly volatile."


file_path = "C:\\Users\\ghant\\Downloads\\house1.csv"
date = []
closing_prices = []

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        date.append(row['date'])
        closing_prices.append(float(row['close']))

volatility = calculate_stock_variability(closing_prices)

price_movement_insights = analyze_price_movements(volatility)
print("Stock Price Variability Analysis")
print(f"Volatility: {volatility:.4f}")
print()
print("Price Movement Insights:")
print(price_movement_insights)
plt.figure(figsize=(10, 6))
plt.plot(date, closing_prices, marker='o')
plt.title("Stock Closing Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
