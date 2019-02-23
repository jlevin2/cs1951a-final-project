import pandas as pd

pd.set_option('display.max_columns', 10)

df = pd.read_excel('../data/CollegeScorecardDataDictionary.xlsx', sheet_name='data_dictionary')

#print(df.head(1))

# for i in range(0,5):
#     print(df.iloc[[i]])

df = df[['VARIABLE NAME', 'API data type']].drop_duplicates()

table = """
CREATE TABLE raw (
"""

for i,row in enumerate(df.iterrows()):
    if i > 0:
        if i < len(df.index) - 1:
            table += "{0} {1},\n".format(row[1].values[0], row[1].values[1])
        else:
            table += "{0} {1}\n".format(row[1].values[0],row[1].values[1])

table += ");"

file = open('create_table.sql', 'w')
file.write(table)
file.close()