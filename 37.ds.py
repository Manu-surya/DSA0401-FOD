import numpy as np
import matplotlib.pyplot as plt


study_time = [2, 3, 5, 1, 4, 6, 2, 7, 8, 5]
exam_scores = [65, 70, 85, 50, 75, 90, 60, 95, 100, 80]

correlation = np.corrcoef(study_time, exam_scores)[0, 1]
print("the correlation between study time and exam scores is :",correlation)


plt.figure(figsize=(8, 6))
plt.scatter(study_time, exam_scores, color='blue', label='Data Points')
plt.title("Study Time vs. Exam Scores")
plt.xlabel("Study Time (hours)")
plt.ylabel("Exam Scores")
plt.legend()
plt.grid(True)


plt.text(1, 105, f"Correlation: {correlation:.2f}", fontsize=12, color='red')


plt.tight_layout()
plt.show()
