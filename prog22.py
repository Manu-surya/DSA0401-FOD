import pandas as pd
import numpy as np
from scipy import stats
data = pd.read_csv("C:\\Users\\ghant\\Downloads\\customer_reviews.csv")
ratings = data["rating"].values

c = float(input("Enter confidence level (b/w 0 and 1): "))

mean = np.mean(ratings)
std = np.std(ratings, ddof=1)  

std_error = std / np.sqrt(len(ratings))

d = len(ratings) - 1
t_score = np.abs(stats.t.ppf((1 - c) / 2, df=d))

moe = t_score * std_error

CI_lower = mean - moe
CI_upper = mean + moe

print("Sample Mean Rating:", mean)
print("Sample Standard Deviation:", std)
print("Standard Error of the Mean:", std_error)
print("Degrees of Freedom:", d)
print("t-score:", t_score)
print("Margin of Error:", moe)
print(f"Confidence Interval for Mean Rating: ({CI_lower:.2f}, {CI_upper:.2f})")
