import psycopg2
import pandas as pd
from psycopg2.extras import execute_values

df = pd.read_csv('cannabis_new.csv')

# cleaning

dbname = 'zgexitff'
user = 'zgexitff'
password = 'N-rZTbhw5RUyDylzQH6Cmai2wSD4SGtr'
host = 'isilo.db.elephantsql.com'

# connect to DB
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# cursor
pg_curs = pg_conn.cursor()

create_cannabis_table = """
DROP TABLE IF EXISTS Cannabis;
CREATE TABLE Cannabis (
    index INT, 
    Strain TEXT,
    Type TEXT, 
    Rating REAL, 
    Effects TEXT, 
    Description TEXT,
    Flavors TEXT, 
    Nearest TEXT
);    
"""

# creating table in postgres
pg_curs.execute(create_cannabis_table)
pg_conn.commit()

# execute values function
execute_values(pg_curs, """
INSERT INTO Cannabis
(index, Strain, Type, Rating, Effects, Description, Flavors, Nearest)
VALUES %s; 
""", [tuple(row) for row in df.values])

# commit
pg_conn.commit()
