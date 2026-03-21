# TODO Flow: user input -> check string -> give feedback -> repeat until good ( .isdigit(), isupper() )
import string

approved = False

while not approved:

    password = input("Enter your password: ")

    min_length = 5
    uppercase_list = list(string.ascii_uppercase)
    numbers_list = list(string.digits)
    long_enough = False
    has_upper = False
    has_num = False

    if len(password) >= min_length:
        long_enough = True
        for char in password:
            if char in uppercase_list:
                has_upper = True
                for char2 in numbers_list:
                    if char2 in password:
                        has_num = True
                        approved = True

    if not long_enough:
        print("*X* Password too short")
    else:
        print("*✔* Password passed length check")
    if not has_num:
        print("*X* Must contain at least one number")
    else:
        print("*✔* Password passed digit test")
    if not has_upper:
        print("*X* Must contain at least one uppercase letter")
    else:
        print("*✔* Password passed uppercase test")

print("*** ALL TESTS PASSED, PASSWORD APPROVED ***")
