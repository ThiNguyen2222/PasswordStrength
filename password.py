import pandas as pd
import re
import math
import string
import wordninja
import numpy as np
from collections import Counter

with open("word_list.txt") as f:
    word_list = set(word.strip().lower() for word in f.readlines())

df = pd.read_csv("data.csv", on_bad_lines='skip')

def count_chars(password):
    password = str(password)
    uppercase = sum(password.count(p) for p in string.ascii_uppercase)
    lowercase = sum(password.count(p) for p in string.ascii_lowercase)
    digits = sum(password.count(p) for p in string.digits)
    symbols = len(password) - (uppercase + lowercase + digits)
    return uppercase, lowercase, digits, symbols

def contains_dict_word(password):
    password = str(password).lower()
    reg_words = re.findall(r'[a-zA-Z]+', password)

    ninja_words = []
    for word in reg_words:
        if len(word) > 3:
            ninja_words.extend(wordninja.split(word))  

    all_words = set(reg_words + ninja_words)
    valid_words = [word for word in all_words if word in word_list and len(word) >= 3]
    return len(valid_words)


def entropy(password):
    password = str(password)
    values, counts = np.unique(list(password), return_counts = True)
    prob = counts / len(password)
    return -np.sum(prob * np.log2(prob))

df['uppercase'], df['lowercase'], df['digits'], df['symbols'] = zip(*df['password'].map(count_chars))
df['has_dict_word'] = df['password'].map(contains_dict_word)
df['entropy'] = df['password'].map(entropy)
df['entropy'] = df['entropy'].apply(lambda x: round(x, 3))
df['length'] = df['password'].apply(lambda x: len(str(x)) if pd.notna(x) else 0)

df.to_csv("processed_data.csv", index=False)
print("Processed CSV saved as 'processed_data.csv'")
