
import pandas as pd
import sqlite3


def test():
    print('Inside init_db file')
    #df = pd.read_csv('../../Data/cannabis_new.csv')
    df = pd.read_csv('cannabis_new.csv')
    print(df.shape)
    df = df.rename(columns={'Index': 'Strain_ID'})
    #conn = sqlite3.connect('../../Data/cannabis.sqlite3')
    conn = sqlite3.connect('cannabis.sqlite3')
    curs = conn.cursor()
    curs.execute("DROP TABLE IF EXISTS Cannabis")
    df.to_sql('Cannabis', con=conn)
    curs.close()
    conn.close()
    print('Database Created!')

if __name__ == '__main__':
    test()
