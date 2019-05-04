import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

df = pd.read_csv('./CollegeScorecard_Raw_Data/MERGED2015_16_PP.csv')
column_names = list(df)

# df_degrees2
pcip_headers = [x for x in column_names if x[:4] == "PCIP"]
pcip_state = ['STABBR'] + pcip_headers
df_degrees = df[pcip_state]
dfd2 = df_degrees.groupby(['STABBR']).mean()
dfd2_sort_cs = dfd2.sort_values(by=['PCIP11'], ascending=False)
print(dfd2_sort_cs.head())
# df.loc[df['STABBR'] == 'FM']

# avg admission rate
df3 = df[['INSTNM', 'STABBR', 'ADM_RATE', 'ADM_RATE_ALL']]
#df3.head(20)
df4 = df3[['STABBR', 'ADM_RATE']]
df4 = df4.groupby(['STABBR']).agg(['mean', 'count'])
df4.columns = df4.columns.droplevel(0)
df4.rename(columns={'mean':'mean_adm_rate', 'count':'num_univ'}, inplace=True)
df4.sort_values(by=['mean_adm_rate'])
print(df4.head())