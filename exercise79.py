# TODO Flow: user input -> check string -> give feedback -> repeat until good ( .isdigit(), isupper() )
import string

approved = False

while not approved:

    password = input("Enter your password: ")

    min_length = 5
    uppercase_list = list(string.ascii_uppercase)
    numbers_list = list(string.digits)

    if len(password) >= min_length:

        for char in password:
            if char in uppercase_list:

                for char2 in numbers_list:
                    if char2 in password:

                        approved = True

print("Approved")
