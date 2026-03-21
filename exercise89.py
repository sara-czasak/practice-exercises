import sqlite3


data = sqlite3.connect('database.db')
print(data.cursor().execute("SELECT country FROM countries WHERE area >= 2000000").fetchall())