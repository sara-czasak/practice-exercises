checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open('countries_cleaned.txt', 'r') as file:
    countries = [country.strip() for country in file.readlines()]

# print(countries)

corrected_checklist = [item for item in checklist if item in countries]
print(corrected_checklist)
