import pandas as pd
import scipy
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


from sklearn import linear_model
import statsmodels.formula.api as sm
import numpy as np
import math

from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA


raw_df = pd.read_csv('../data/CollegeScorecard_Raw_Data/MERGED2016_17_PP.csv',
                     header=0,
                     low_memory=False)

ivies = [217156, 166027, 130794, 190415, 186131, 182670, 190150, 186131]
attributes = ["UNITID", "INSTNM",
              "ADM_RATE",
              "SAT_AVG",
              "UGDS",
              # Diversity
              "UGDS_WHITE", "UGDS_BLACK", "UGDS_HISP", "UGDS_ASIAN",
              # Economics
              "COSTT4_A", "PCTPELL",
              # Fac Salary
              "AVGFACSAL",
              #Completion rate
             "C150_4",
              # Share of independent students
              "DEP_STAT_PCT_IND",
              # Median debt for completed students
              "GRAD_DEBT_MDN" #,
              # Median salary 10 years after grad
              #"MD_EARN_WNE_P10"
             ]

df = raw_df[attributes]

df = df.convert_objects(convert_numeric=True).round(2).dropna()


data = df[["ADM_RATE",
              "SAT_AVG",
              "UGDS",
              # Diversity
              "UGDS_WHITE", "UGDS_BLACK", "UGDS_HISP", "UGDS_ASIAN",
              # Economics
              "COSTT4_A", "PCTPELL",
              # Fac Salary
              "AVGFACSAL",
              #Completion rate
             "C150_4",
              # Share of independent students
              "DEP_STAT_PCT_IND",
              # Median debt for completed students
              "GRAD_DEBT_MDN" #,
              # Median salary 10 years after grad
              #"MD_EARN_WNE_P10"
             ]]
labelled = df[["INSTNM", "UNITID"]]
print(len(data))

pca = PCA(n_components=3)

X = pca.fit_transform(data)

num_clusters = 30
kmeans = KMeans(n_clusters=num_clusters, random_state=0)

kmeans.fit(X)

clusters = [[] for i in range(0, num_clusters)]
for i, k in enumerate(kmeans.labels_):
    clusters[k].append(labelled.values[i][0])

for r in clusters:
    print(str(r) + '\n')

for i, k in enumerate(kmeans.labels_):
    if labelled.values[i][1] in ivies:
        print(labelled.values[i][0], k)

centers = kmeans.cluster_centers_


fig = plt.figure(figsize=(4,4))
ax = plt.axes(projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2],  c=kmeans.labels_, alpha=0.3) # Plot the documents
ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], c='black', alpha=1) # Plot the centers

plt.show()









