def password_strength(password):
    strength = 0
    # length minimum 8 characters
    if len(password) >= 8:
        strength += 1
    # uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    # lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    # digits
    if any(char.isdigit() for char in password):
        strength += 1
    # special characters
    special_chars = "!@#$%^&*()_+[]{}|;:,.<>?~"
    if any(char in special_chars for char in password):
        strength += 1

    return strength
    
def rate_password_strength(score):
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

user_password = input("Enter your password: ")
score = password_strength(user_password)
rating = rate_password_strength(score)
print(f"Password strength score: {score}/5 - {rating}")