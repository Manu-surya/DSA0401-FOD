import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
new_treatment_data =[20, 12]
placebo_data = [5, 17]
t_statistic, p_value = stats.ttest_ind(new_treatment_data, placebo_data)
print("T-statistic:", t_statistic)
print("P-value:", p_value)
if p_value < 0.05:
    print("The new treatment has a statistically significant effect compared to placebo.")
else:
    print("There is no statistically significant difference between the groups.")
plt.boxplot([new_treatment_data,placebo_data ], labels=['Control Group', 'Treatment Group'])
plt.show()
plt.bar(['p-value'], [p_value], color=['blue'])
plt.title('p-value')
plt.ylabel('p-value')
plt.ylim(0,1)
plt.show()
