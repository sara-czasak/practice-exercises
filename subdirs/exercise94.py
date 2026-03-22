with open('urls.txt', 'r') as f:
    data = f.read()

data = data.split('\n')
clean_data = []
for line in data:
    line = line.replace('s', '')
    line = line[:5] + '/' + line[5:]
    clean_data.append(line)

# clean_data.pop(4)
print(data)

# with open('urls.txt', 'w') as f:
#     for line in clean_data:
#         f.write(f"{line}\n")

print(clean_data)

