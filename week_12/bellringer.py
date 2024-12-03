while True:
    password = input('Enter your password: ')

    # Check if the password is at least 8 characters long
    if len(password) < 8:
        print('Password should be at least 8 characters long.')
        continue

    # Check if the password contains at least one number
    if not any(char.isdigit() for char in password):
        print("Password should contain at least one number.")
        continue

    # Check if the password contains at least one special character
    if not any(char in '!@#$%^&*()-_=+[]{}|;:",.<>?/' for char in password):
        print("Password should contain at least one special character.")
        continue

    # If all criteria are met, print success message
    print("Your password is strong.")
    break