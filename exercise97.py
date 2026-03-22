close = False
data = []

while not close:
    input_value = input("Enter value: ")
    if input_value != 'CLOSE' and input_value != 'SAVE':
        data.append(input_value)
    elif input_value == 'CLOSE':
        close = True
    else:
        with open("notes1.txt", "a+") as file:
            for i in data:
                file.write(f"{i}\n")

with open("notes1.txt", "a+") as file:
    for i in data:
        file.write(f"{i}\n")
