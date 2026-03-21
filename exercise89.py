import sqlite3


data = sqlite3.connect('database.db')
countries = data.cursor().execute("SELECT country FROM countries WHERE area >= 2000000").fetchall()
for i in countries:
    print(i[0])