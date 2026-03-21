import pandas as pd
import sqlite3

cur = sqlite3.connect('database.db')
with open("ten_more_countries.txt", 'r') as file:
    data = [i.strip('\n') for i in file.readlines()]

data.pop(0)
# print(data)
for i in data:
    i = i.split(',')
    # print(i)
    params = (i[0] , i[1], i[2], 0)
    cur.execute(f'INSERT INTO countries VALUES (?, ?, ?, ?)', params)
    cur.commit()


