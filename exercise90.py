import sqlite3
import pandas as pd


data = sqlite3.connect('database.db')
countries = data.cursor().execute("SELECT * FROM countries WHERE area >= 2000000").fetchall()

with open("data_csv.csv", 'w') as file:
    for i in countries:
        file.write(f"{i[0]},{i[1]},{i[2]},{i[3]} \n")
