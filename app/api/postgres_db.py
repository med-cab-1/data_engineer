import psycopg2
import pandas as pd
from psycopg2.extras import execute_values
from os import getenv
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv('cannabis_new.csv')

# cleaning

dbname = getenv('POSTGRES_DB_NAME')

user = getenv('POST_GRES_DB_USER')

password = getenv('POSTGRES_PASS_KEY')

host = getenv('DATABASE_URL')


# connect to DB
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

# pg_conn = psycopg2.connect(dbname=dbname, user=dbname,
#                            password=password, host=host)

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
