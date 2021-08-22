"""
Prac 03 Password checker
"""
MINIMUM_LENGTH = 5


def main():
    password = get_password(MINIMUM_LENGTH)
    string_to_asterisk(password)


def string_to_asterisk(password):
    print("*" * len(password))


def get_password(MINIMUM_LENGTH):
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"The password must be at least {str(MINIMUM_LENGTH)} characters long.")
        password = input("Enter password: ")
    return password


main()
