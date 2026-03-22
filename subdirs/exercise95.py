comma_sep_input = input("Enter comma separated values: ")

comma_sep_input = comma_sep_input.split(',')

with open(f"comma_input_{comma_sep_input[0]}.txt", "w") as f:
    for i in comma_sep_input:
        f.write(f"{i}\n")
