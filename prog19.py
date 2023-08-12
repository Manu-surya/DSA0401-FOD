import numpy as np
import scipy.stats as stats
new_data = [2.5, 3.1, 2.9, 2.8, 3.2, 2.7, 2.8, 3.0, 2.6, 3.3,
                 2.4, 2.9, 3.1, 2.7, 3.0, 3.2, 2.8, 3.1, 3.0, 2.6,
                 3.2, 2.9, 2.8, 3.1, 2.7, 2.6, 2.9, 2.8, 3.0, 3.2,
                 3.1, 2.8, 2.7, 2.9, 3.0, 2.8, 3.3, 2.5, 3.1, 2.7,
                 2.9, 2.8, 3.2, 2.6, 3.1, 2.9, 2.7, 3.0]
placebo_data = [1.6, 1.8, 1.5, 1.9, 1.7, 1.4, 1.9, 1.6, 1.8, 1.7,
                 1.5, 1.6, 1.7, 1.8, 1.9, 1.5, 1.6, 1.8, 1.7, 1.9,
                 1.6, 1.5, 1.7, 1.9, 1.8, 1.6, 1.5, 1.9, 1.8, 1.6,
                 1.7, 1.6, 1.8, 1.9, 1.5, 1.7, 1.6, 1.8, 1.9, 1.7,
                 1.5, 1.7, 1.8, 1.6, 1.9, 1.7, 1.5, 1.8]
alpha = 0.05
a = np.mean(new_data)
a1= np.std(new_data, ddof=1) 
b = np.mean(placebo_data)
b1 = np.std(placebo_data, ddof=1)
t_score = stats.t.ppf(1 - alpha/2, df=49)
moe1 = t_score * (a1/ np.sqrt(50))
moe2 = t_score * (b1 / np.sqrt(50))
new_drug = (a-moe1, a+moe2)
placebo = (b-moe2, b+ moe2)
print("New Drug Group:", new_drug)
print("Placebo Group :", placebo)
