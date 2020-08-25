import pandas as pd
import sqlite3

df = pd.read_csv('cannabis_new.csv')

df = df.rename(columns={'Index': 'Strain_ID'})

print(df)
conn = sqlite3.connect('cannabis.sqlite3')

curs = conn.cursor()
curs.execute("DROP TABLE IF EXISTS Cannabis")

df.to_sql('Cannabis', con=conn)
