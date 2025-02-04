def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    # Initialize flags 
    has_upper = False
    has_lower = False
    has_digits = False
    has_special = False

    special_chars = "@!#$%^&*()_-+={}[]:;'?/>.<\",~`*"

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digits = True
        if char in special_chars:
            has_special = True

    # Increment score for character type checks
    if has_upper and has_lower:
        score += 1
    if has_digits:
        score += 1
    if has_special:
        score += 1

    # Determine the password strength based on the score
    if score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    else:
        return "Weak"

# Get user input and check password strength
password = input("Enter a password to check: ")  
res = check_password_strength(password)  
print(f"Password strength: {res}")  
