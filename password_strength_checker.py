import re

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r"\d", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Evaluate strength
    strength = sum([length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, special_char_criteria])

    # Return strength level
    if strength == 5:
        return "Strong"
    elif 3 <= strength < 5:
        return "Moderate"
    else:
        return "Weak"

if __name__ == "__main__":
    test_passwords = ["password", "Password123!", "12345678", "P@ssw0rd"]
    for pwd in test_passwords:
        print(f"Password: {pwd}, Strength: {check_password_strength(pwd)}")

# Add password strength checker script
