import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('soccer_players.csv')
top_goals_players = df.nlargest(5, 'Goals_Scored')
top_salary_players = df.nlargest(5, 'Weekly_Salary')
average_age = df['Age'].mean()
above_average_age_players = df[df['Age'] > average_age]
print("Top 5 Players with the Highest Goals Scored:")
print(top_goals_players)
print("\nTop 5 Players with the Highest Salaries:")
print(top_salary_players)
print(f"\nAverage Age of Players: {average_age:.2f}")
print("\nPlayers Above Average Age:")
print(above_average_age_players[['Name', 'Age']])

position_counts = df['Position'].value_counts()
position_counts.plot(kind='bar', xlabel='Position', ylabel='Count', title='Distribution of Players by Position')
plt.xticks(rotation=45)
plt.show()
