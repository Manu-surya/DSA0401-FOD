import numpy as np
import matplotlib as mat
fuel_efficiency = np.array([28,32,48,26,50,40])
avg_efficiency = np.mean(fuel_efficiency)

model_index_1 = 2 
model_index_2 = 4  

initial_effi = fuel_efficiency[model_index_1]
impr_effi= fuel_efficiency[model_index_2]
per_impr = ((impr_effi - initial_effi) / initial_effi) * 100

print("Average fuel efficiency:", avg_efficiency, "mpg")
print("Percentage improvement between models", model_index_1, "and", model_index_2, ":", per_impr, "%")
