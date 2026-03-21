checklist = ["Portugal", "Germany", "Spain"]

with open('countries_missing.txt', 'r') as file:
    countries = [country.strip() for country in file.readlines()]
countries += checklist

print(sorted(countries))

with open('countries_added.txt', 'w') as file:
    for country in sorted(countries):
        file.write(f"{country}\n")