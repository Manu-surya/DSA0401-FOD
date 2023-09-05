import pandas as pd
import numpy as np
import random

def calculate_most_consistent_city(std_deviations):
    return std_deviations.idxmin()
np.random.seed(42)  
cities = ['chennai', 'pondy', 'trichy', 'goa', 'kanya']
temperature_values = [random.uniform(5, 35) for _ in range(len(cities) * 365)]  # Simulate daily temperatures

data = {'City': [city for city in cities for _ in range(365)],
        'Temperature': temperature_values}

temperature_df = pd.DataFrame(data)

city_stats = temperature_df.groupby('City')['Temperature'].agg([np.mean, np.std, np.ptp])

highest_range_city = city_stats['ptp'].idxmax()

most_consistent_city = calculate_most_consistent_city(city_stats['std'])

# Display results
print("Temperature Analysis for Cities")
print("--------------------------------")
print(city_stats)
print()
print(f"City with the Highest Temperature Range: {highest_range_city}")
print(f"City with the Most Consistent Temperature: {most_consistent_city}")
