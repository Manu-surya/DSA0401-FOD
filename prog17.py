import pandas as pd
import matplotlib.pyplot as plt
import string
from collections import Counter
import re
data = pd.read_csv("C:\\Users\\ghant\\Downloads\\house.csv")
print(data['feedback'])
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    stop_words = set(["the","and","is"])
    words = text.split()
    filtered_words = []
    for word in words:
        if word not in stop_words:
            filtered_words.append(word) 
    cleaned_text = ' '.join(filtered_words)  
    return cleaned_text
data['cleaned_feedback'] = data['feedback'].apply(preprocess_text)
print(data[['feedback', 'cleaned_feedback']])
combined_text = ' '.join(data['cleaned_feedback'])
words = re.findall(r'\b\w+\b',combined_text) 
word_frequencies = Counter(words)

for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")

N = int(input("Enter the number of most frequent words to display: "))
print(f"Top {N} most frequent words:")
for word, frequency in word_frequencies.most_common(N):
    print(f"{word}: {frequency}")

    top_words = [word for word, _ in word_frequencies.most_common(N)]
top_frequencies = [frequency for _, frequency in word_frequencies.most_common(N)]

plt.figure(figsize=(10, 6))
plt.bar(top_words, top_frequencies)
plt.xlabel('Words')
plt.ylabel('Frequencies')
plt.title(f'Top {N} Most Frequent Words')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()
