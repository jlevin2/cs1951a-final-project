import sqlite3
import pandas

conn = sqlite3.connect('testing.db')

cur = conn.cursor()

conn.execute("")

sample_table = """
CREATE TABLE basics (
id integer,
name VARCHAR(256),
city VARCHAR(256),
state VARCHAR(256),
school_url VARCHAR(256),
ownership integer,
admission_rate float);
"""

df = pandas.read_csv('../data/MERGED2016_17_PP.csv',
                     header=0,
                     low_memory=False)

df = df[['UNITID','INSTNM', 'CITY', 'STABBR','INSTURL','CONTROL','ADM_RATE']]

print(df.columns)
#df.to_sql('testing_table', conn, if_exists='replace', index=False)
cur.execute(sample_table)
conn.commit()

cur.executemany("INSERT INTO basics VALUES (?,?,?,?,?,?,?)", df.itertuples(index=False))
conn.commit()
