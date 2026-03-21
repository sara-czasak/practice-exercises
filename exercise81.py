import string

with open('users.txt', 'r') as file:
    data = file.readlines()
    users = [data.strip() for data in data]

new_user = False
name = ""
while not new_user:
    name = input("Enter username: ")
    if name.capitalize() not in users:
        print(f"Username {name} created successfully")
        new_user = True
    else:
        print(f"Username {name} already exists!")

approved = False

while not approved:

    password = input("\nEnter your password: ")

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
        print("\n*X* Password too short")
    else:
        print("\n*✔* Password passed length check")
    if not has_num:
        print("*X* Must contain at least one number")
    else:
        print("*✔* Password passed digit test")
    if not has_upper:
        print("*X* Must contain at least one uppercase letter")
    else:
        print("*✔* Password passed uppercase test")

print("*** ALL TESTS PASSED, PASSWORD APPROVED ***\n")

print(f"*** New User Created ***\n\tUsername: {name}\n\tPassword: {password}")