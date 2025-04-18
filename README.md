# PasswordStrength
This project implements a password strength evaluator using a Gaussian Naive Bayes classifier. The system classifies passwords into three categories: Weak, Moderate, and Strong, based on their structure and complexity. It utilizes machine learning techniques to analyze password strength based on features suchs as character, varierty, length, and entropy.

## Installation
Python packages that are required

`pip install pandas numpy wordninja nltk joblib scikit-learn tkinter`

`pip install matplotlib`


## Files Purposes
`Password.py`: Processes the raw dataset into extracted features

`train_model.py`: Trains a Naive Bayes model using `processed_data.py` and saves it as `nb_model.pkl`

`predict.py`: Loads `nb_model.pkl`and predicts password strength based on user input

`data.csv`: Orginal password dataset

`processed_data.csv`: The feature-extracted dataset which is used to train the model

`word_list.txt`: List of common words used to detect dictionary words in passwords

`confusion_matrix.py` : Generates a confusion matrix and classification report to evaluate the model's performance

## How to Run
1. Preprocess the data (This may take a minute):

`python password.py`

3. Train the Naive Bayes classifer: `nb_model.pkl`:

`python train_model.py`

3. Predict Password Strenth through command line :

`python predict.py`

Enter a password in the input field to evaluate its strength

4. Confusion Matrix:

`python confusion_matrix.py`

## Model Features
The Naive Bayes model is trained using these features:

* Uppercase letters
* Lowercase letters
* Numbers
* Special symbols
* Presence of dictionary words
* Entropy
* Password length

## Evaluation
We evaluated the performance of our Naive Bayes classifier using accuracy and a confusion matrix, which measures how well the model classifies passwords into the correct strength category (Weak, Moderate, Strong).

## Results
* Accuracy: 77% (varies depending on random training/test split)
* The model performs best at identifying weak and strong passwords but had issues classifying weak passwords as moderate e.g. Summer2025 was classified as moderate although it is weak
* The confusion matrix shows how many passwords were correctly or incorrectly classified using precision, recall, and F1-score per class

## Contributors
* Lillian Thacker: Model Implementation & Training

* Thi Nguyen: Data Collection & Processing

* Ngoc Pham: UI Development

* Caitlin San Pedro: Frontend Development & Visual Design

## References
* Password Dataset: https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset
* Code Reference: https://github.com/kishan0725/Checking-the-Password-Strength-using-ML
* Word List Generator: http://app.aspell.net/create
