close = False
data = []

while not close:
    input_value = input("Enter value: ")
    if input_value.upper() != 'CLOSE' and input_value.upper() != 'SAVE':
        data.append(input_value)
    elif input_value.upper() == 'CLOSE':
        print("*** Closing and saving... ***")
        close = True
    else:
        with open("notes1.txt", "a+") as file:
            for i in data:
                file.write(f"{i}\n")
        print("*** Notes saved successfully! ***")

with open("notes1.txt", "a+") as file:
    for i in data:
        file.write(f"{i}\n")
