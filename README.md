# Password Checker and Generator

## Description

This script checks the strength of a given password based on five criteria:
1. Length (minimum of 8 characters)
2. Presence of lowercase letters
3. Presence of uppercase letters
4. Presence of digits
5. Presence of special characters

If the password does not meet all criteria, the script generates and suggests five random passwords that include a user-provided word combined with random characters. The script provides a visual representation of the password's strengths and weaknesses using checkmarks and crosses for each criterion.

## Features

- Checks password strength against common security criteria.
- Provides visual feedback on password strength.
- Generates strong password suggestions if the provided password is weak.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the script.

2. Run the script in a Python environment:

    ```sh
    python password_checker.py
    ```

3. Follow the prompts:
    - Enter a word to include in the generated passwords.
    - Enter the password you want to check.

4. The script will display a visual representation of the password's strengths and weaknesses. If the password is not strong, it will suggest five random passwords that include the provided word.

## Example

```sh
Enter a word to include in the passwords: example
Enter the password to check: Passw0rd!
Password Strength Checker
--------------------------
Length (>= 8):    ✔
Lowercase:        ✔
Uppercase:        ✔
Digit:            ✔
Special Char:     ✔
--------------------------

The password is strong.
