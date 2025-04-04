import joblib
import pandas as pd
import numpy as np
import tkinter as tk
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

def suggest_improvements(password):
    suggestions = []
    
    if len(password) < 8:
        suggestions.append("Make your password at least 8 characters long.")
    if not any(char.isupper() for char in password):
        suggestions.append("Add at least one uppercase letter.")
    if not any(char.islower() for char in password):
        suggestions.append("Add at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        suggestions.append("Include at least one number.")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
        suggestions.append("Add at least one special character.")

    return "\n".join(suggestions)

def check_password():
    password_input = entry.get()
    strength = predict_strength(password_input)
    result_label.config(text=f"Predicted Strength: {strength}")
    if strength != "Strong":
        suggestions = suggest_improvements(password_input)
        suggestion_label.config(text=f"Suggestions:\n{suggestions}")
    else:
        suggestion_label.config(text="✅ Your password is strong. No further changes needed.")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")

entry = tk.Entry(root)
entry.pack(pady=20)

tk.Button(root, text="Check Strength", command=check_password).pack(pady=10)

result_label = tk.Label(root, text="Predicted Strength:")
result_label.pack(pady=10)

suggestion_label = tk.Label(root, text="Suggestions:")
suggestion_label.pack(pady=10)

root.mainloop()
