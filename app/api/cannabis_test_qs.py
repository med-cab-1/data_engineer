import sqlite3

conn = sqlite3.connect('cannabis.sqlite3')

curs = conn.cursor()
num = 45
curs.execute(f"SELECT * FROM Cannabis WHERE Strain_ID == {num}")

print(curs.fetchall())