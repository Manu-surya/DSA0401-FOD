import numpy as np
import pandas as pd
import scipy.stats as stats
data = pd.read_csv("C:\\Users\\ghant\\Downloads\\rare_elements.csv")
m = data["concentration"].values

sample_size = int(input("Enter the sample size: "))
confidence_level = float(input("Enter the confidence level (between 0 and 1): "))
precision = float(input("Enter the desired level of precision: "))

sample_mean = np.mean(m[:sample_size])
sample_std = np.std(m[:sample_size], ddof=1)
std_error = sample_std / np.sqrt(sample_size)

z_score = np.abs(stats.norm.ppf((1 - confidence_level) / 2))

moe= z_score * std_error
CI_lower = sample_mean - moe
CI_upper = sample_mean + moe

sample_size = ((z_score * sample_std) / precision) ** 2

print("Sample Mean:", sample_mean)
print("Sample Standard Deviation:", sample_std)
print("Standard Error of the Mean:", std_error)
print("Z-score:", z_score)
print("Margin of Error:", moe)
print(f"Confidence Interval: ({CI_lower:.4f}, {CI_upper:.4f})")
print("Required Sample Size for Desired Precision:", int(np.ceil(sample_size)))
