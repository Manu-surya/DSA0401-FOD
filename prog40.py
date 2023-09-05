import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('soccer_players.csv')
# Top 5 players by goals scored
top_players_goals = df.nlargest(5, 'Goals_Scored')

# Top 5 players by salaries
top_players_salaries = df.nlargest(5, 'Weekly_Salary')
average_age = df['Age'].mean()
above_average_age_players = df[df['Age'] > average_age]['Name']
import matplotlib.pyplot as plt

position_counts = df['Position'].value_counts()
position_counts.plot(kind='bar')
plt.xlabel('Position')
plt.ylabel('Count')
plt.title('Distribution of Players by Position')
plt.show()
