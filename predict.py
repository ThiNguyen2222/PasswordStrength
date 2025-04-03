import joblib
import pandas as pd
import numpy as np
import string
import re
import wordninja


# Load trained model
nb_model = joblib.load("nb_model.pkl")

# Define feature extraction functions
def count_chars(password):
    password = str(password)
    uppercase = sum(password.count(p) for p in string.ascii_uppercase)
    lowercase = sum(password.count(p) for p in string.ascii_lowercase)
    digits = sum(password.count(p) for p in string.digits)
    symbols = len(password) - (uppercase + lowercase + digits)
    return [uppercase, lowercase, digits, symbols]

def contains_dict_word(password):
    with open("word_list.txt") as f:
        word_list = set(word.strip().lower() for word in f.readlines())

    password = str(password).lower()
    reg_words = re.findall(r'[a-zA-Z]+', password)
    ninja_words = [wordninja.split(word) for word in reg_words if len(word) > 3]
    all_words = set(reg_words + [w for sublist in ninja_words for w in sublist])
    return len([word for word in all_words if word in word_list and len(word) >= 3])

def entropy(password):
    password = str(password)
    values, counts = np.unique(list(password), return_counts=True)
    prob = counts / len(password)
    return -np.sum(prob * np.log2(prob))

# Function to predict password strength
def predict_strength(password):
    # Extract features
    features = count_chars(password) + [
        contains_dict_word(password),
        round(entropy(password), 3),
        len(password),
    ]
    
    # Convert to DataFrame for prediction
    feature_df = pd.DataFrame([features], columns=['uppercase', 'lowercase', 'digits', 'symbols', 'has_dict_word', 'entropy', 'length'])

    # Predict strength
    prediction = nb_model.predict(feature_df)
    
    # Strength labels
    strength_labels = {0: "Weak", 1: "Moderate", 2: "Strong"}
    return strength_labels[prediction[0]]

# Run a test prediction
from suggestion import suggest_improvements # Imported from suggestion.py

if __name__ == "__main__":
    password_input = input("Enter a password: ")
    print("Predicted Strength:", predict_strength(password_input))
    print(suggest_improvements(password_input)) # Function from suggestion.py
