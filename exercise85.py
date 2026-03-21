with open('countries_raw.txt', 'r') as file:
    countries = file.read().splitlines()

clean_data = []

for country in countries:
    if country != '\n' and country != '' and len(country) > 1 and country != 'Top of Page':
        clean_data.append(country)

with open('countries_cleaned.txt', 'w') as file:
    for country in clean_data:
        file.write(f"{country}\n")
