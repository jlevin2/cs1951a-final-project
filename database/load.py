import sqlite3
import pandas
import psycopg2

# conn = sqlite3.connect('testing.db')
#
# cur = conn.cursor()

conn = psycopg2.connect(
    dbname='postgres',
    user='JoshLevin',
    password='',
    host='localhost',
    port=5432)


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

