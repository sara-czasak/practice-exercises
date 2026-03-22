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


# comma_sep_input = input("Enter comma separated values: ")
#
# comma_sep_input = comma_sep_input.split(',')
#
# with open(f"comma_input.txt", "a") as f:
#     for i in comma_sep_input:
#         f.write(f"{i}\n")