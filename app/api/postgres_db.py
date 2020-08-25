import psycopg2
import pandas as pd
from psycopg2.extras import execute_values

df = pd.read_csv('cannabis.csv')

# cleaning

dbname = 'zgexitff'
user = 'zgexitff'
password = 'XXX'
host = 'isilo.db.elephantsql.com'

# connect to DB
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

#cursor
pg_curs = pg_conn.cursor()

create_cannabis_table ="""
DROP TABLE IF EXIST Cannabis;
CREATE TABLE Cannabis (
    index INT, 
    strain TEXT,
    rating, 
    type TEXT, 
    effects TEXT, 
    description TEXT,
"""

# creating table in postgres
pg_curs.excute(create_cannabis_table)
pg_conn.commit()

# execute values function
execute_values(pg_curs, """
INSERT INTO Cannabis
(strain, rating, type, effects, description)
VALUES %s; 
""", [tuple(row) for row in df.values])

# commit
pg_conn.commit()



