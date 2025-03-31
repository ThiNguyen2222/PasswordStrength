import pandas as pd
import re
import math
import string
import wordninja
import numpy as np
from collections import Counter
import nltk
from nltk.corpus import words

nltk.download('words')

word_list = set(words.words())

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
    segment = wordninja.split(password)
    return int(any(len(word) > 3 and word in word_list for word in segment))

def entropy(password):
    password = str(password)
    values, counts = np.unique(list(password), return_counts = True)
    prob = counts / len(password)
    return -np.sum(prob * np.log2(prob))

df['uppercase'], df['lowercase'], df['digits'], df['symbols'] = zip(*df['password'].map(count_chars))
df['has_dict_word'] = df['password'].map(contains_dict_word)
df['entropy'] = df['password'].map(entropy)
df['entropy'] = df['entropy'].apply(lambda x: round(x, 2))
df['length'] = df['password'].apply(lambda x: len(str(x)) if pd.notna(x) else 0)

df.to_csv("processed_data.csv", index=False)
print("Processed CSV saved as 'processed_data.csv'")
