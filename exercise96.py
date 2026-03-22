close = False
data = []

while not close:
    input_value = input("Enter value: ")
    if input_value != 'CLOSE':
        data.append(input_value)
    else:
        close = True

with open("notes.txt", "a+") as myfile:
    for i in data:
        myfile.write(f"{i}\n")
