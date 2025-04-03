import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Load processed dataset
df = pd.read_csv("processed_data.csv")

# Define feature columns
feature_cols = ['uppercase', 'lowercase', 'digits', 'symbols', 'has_dict_word', 'entropy', 'length']
X = df[feature_cols]  # Features
y = df['strength']     # Labels

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Naive Bayes model
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

# Save the trained model
joblib.dump(nb_model, "nb_model.pkl")
print("Model saved as nb_model.pkl")

# Evaluate the model
y_pred = nb_model.predict(X_test)
print("\nModel Performance:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
