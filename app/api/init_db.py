#! usr/bin/python
"""
File containing functions for database creation and management
"""

# IMPORTS
import pandas as pd
import sqlite3



def create_db():
    print('Inside init_db file')
    #df = pd.read_csv('../../Data/cannabis_new.csv')
    df = pd.read_csv('Data/cannabis_new.csv')
    print(df.head())
    df = df.rename(columns={'Index': 'Strain_ID'})
    #conn = sqlite3.connect('../../Data/cannabis.sqlite3')
    conn = sqlite3.connect('Data/cannabis.sqlite3')
    curs = conn.cursor()
    curs.execute("DROP TABLE IF EXISTS Cannabis")
    df.to_sql('Cannabis', con=conn)
    # curs.close()
    # conn.close()
    print('Database Created!')

def say_hi():
    print("Hello!")


if __name__ == '__main__':
    create_db()
    say_hi()
