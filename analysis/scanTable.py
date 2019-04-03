import pandas
import sqlite3
import os

conn = sqlite3.connect('earnings.db')

csvFiles = ['MERGED2009_10_PP.csv',
            'MERGED2011_12_PP.csv',
            'MERGED2012_13_PP.csv',
            'MERGED2013_14_PP.csv',
            'MERGED2014_15_PP.csv',]

cur = conn.cursor()

conn.execute("")

drop_table = """
DROP TABLE IF EXISTS earnings;
"""
cur.execute(drop_table)

earnings_table = """
CREATE TABLE earnings (
id integer,
name VARCHAR(256),
year integer,
six_year_mean float,
six_year_mean_males float,
six_year_mean_females float,
seven_year_mean float,
eight_year_mean float,
nine_year_mean float,
ten_year_mean float,
ten_year_mean_males float,
ten_year_mean_females float,
cost_estimate_pub float,
cost_estimate_pri float);
"""
cur.execute(earnings_table)
conn.commit()

for fileName in csvFiles:
    print('Scanning: {0}'.format(fileName))
    df = pandas.read_csv('../data/{0}'.format(fileName),
                         header=0,
                         low_memory=False)
    df = df[['UNITID',
            'INSTNM',
            'MN_EARN_WNE_P6',
            'MN_EARN_WNE_MALE1_P6',
            'MN_EARN_WNE_MALE0_P6',
            'MN_EARN_WNE_P7',
            'MN_EARN_WNE_P8',
            'MN_EARN_WNE_P9',
            'MN_EARN_WNE_P10',
            'MN_EARN_WNE_MALE1_P10',
            'MN_EARN_WNE_MALE0_P10',
            'NPT4_PUB',
            'NPT4_PRIV']]

    cur.executemany("INSERT INTO earnings VALUES (?,?,{0},?,?,?,?,?,?,?,?,?,?,?)".format(fileName[8:10]), df.itertuples(index=False))
    conn.commit()
