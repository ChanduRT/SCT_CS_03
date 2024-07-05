import random
import string
import re

def is_strong_password(password):
    criteria = {
        "length": len(password) >= 8,
        "lowercase": re.search(r"[a-z]", password) is not None,
        "uppercase": re.search(r"[A-Z]", password) is not None,
        "digit": re.search(r"[0-9]", password) is not None,
        "special": re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None
    }
    return all(criteria.values()), criteria

def print_password_strength(criteria):
    fig = """
    Password Strength Checker
    --------------------------
    Length (>= 8):    {}
    Lowercase:        {}
    Uppercase:        {}
    Digit:            {}
    Special Char:     {}
    --------------------------
    """
    return fig.format(
        "✔" if criteria["length"] else "✘",
        "✔" if criteria["lowercase"] else "✘",
        "✔" if criteria["uppercase"] else "✘",
        "✔" if criteria["digit"] else "✘",
        "✔" if criteria["special"] else "✘"
    )

def generate_passwords(word, length=12, num_passwords=5):
    passwords = []
    for _ in range(num_passwords):
        password = word
        while len(password) < length:
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        passwords.append(''.join(random.sample(password, len(password))))
    return passwords

# Get user input

user_password = input("Enter the password to check: ")

# Check if the user's password is strong
is_strong, criteria = is_strong_password(user_password)
print(print_password_strength(criteria))

if not is_strong:
    print("The password is not strong enough. Here are some suggestions:")
    # Generate passwords
    passwords = generate_passwords(user_password)
    # Print the passwords
    for i, password in enumerate(passwords, 1):
        print(f"{i}. {password}")
else:
    print("The password is strong.")
