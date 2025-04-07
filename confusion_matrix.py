import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

df = pd.read_csv("processed_data.csv")

df.dropna(subset=['password'], inplace=True)


vectorizer = CountVectorizer(analyzer='char')
X = vectorizer.fit_transform(df['password']) 
y = df['strength']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots(figsize=(6, 4))
cax = ax.matshow(cm, cmap="Blues")
fig.colorbar(cax)
ax.set_xticklabels([""] + ["Weak", "Moderate", "Strong"])
ax.set_yticklabels([""] + ["Weak", "Moderate", "Strong"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Processed Data 2")

for (i, j), value in np.ndenumerate(cm):
    ax.text(j, i, str(value), ha='center', va='center', color='black')

plt.show()

# Print classification report
print(classification_report(y_test, y_pred))
