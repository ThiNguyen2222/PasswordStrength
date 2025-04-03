# Will be imported into predict.py

# Function needed to establish password improvements
def suggest_improvements(password):
    suggestions = []
    
    if not any(char.isupper() for char in password):
        suggestions.append("Add at least one uppercase letter.")
    if not any(char.islower() for char in password):
        suggestions.append("Add at least one lowercase letter.")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
        suggestions.append("Add at least one special character.")

    # Make suggestions to improve password strength
    if suggestions: 
        return "Suggestions: " + " ".join(suggestions)
    else:
        return "Your password meets the character requirements."
    

