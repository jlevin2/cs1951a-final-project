import pandas
import sqlite3
import os


conn = sqlite3.connect('demographics.db')

csvFiles = os.listdir("../data/")


def createTable(conn):
    cur = conn.cursor()

    conn.execute("")

    drop_table = """
    DROP TABLE IF EXISTS demographics;
    """

    cur.execute(drop_table)

    create_demographics_table = """
    CREATE TABLE demographics (
    id integer,
    name VARCHAR(256),
    year integer,
    percent_black float,
    percent_asian float,
    percent_hispanic float,
    percent_white float,
    mean_sat float,
    admissions_rate float);
    """

    cur.execute(create_demographics_table)
    conn.commit()


createTable(conn)

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
cur.executemany("INSERT INTO earnings VALUES (?,?,{0},?,?,?,?,?,?,?,?,?,?,?)".format(
    fileName[8:10]), df.itertuples(index=False))
conn.commit()
