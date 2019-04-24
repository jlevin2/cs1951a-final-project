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
              # Median debt for completed students
              "GRAD_DEBT_MDN",
              # Avg anual cost per academic year
              "COSTT4_A",
              # Net tuition revenue (tuition revenue minus discounts and allowances) divided by the number of FTE students (undergraduates and graduate students) (http://nces.ed.gov/ipeds/glossary/index.asp?id=854). Net tuition revenue is included in the IPEDS Finance component and FTE enrollment is included in the IPEDS 12-Month Enrollment component. This metric includes graduate students.
              "TUITFTE",
              # Retention Rate
              "RET_FT4",
              # Share low-income  0-30k
              "INC_PCT_LO",
              # Share first generation
              "PAR_ED_PCT_1STGEN",
              # Median Pell grant debt
              "PELL_DEBT_MDN",
              # Median debt for non-pell students
              "NOPELL_DEBT_MDN",
              # Number of students in median debt cohort
              "DEBT_N",
              # Average family income 2015
              "FAMINC"]

df = raw_df[attributes]
#print(df[df["UNITID"].isin(ivies)])
df = df.convert_objects(convert_numeric=True).round(2).dropna()
p = attributes.copy()
p.remove("INSTNM")
p.remove("UNITID")
data = df[p]
labelled = df[["INSTNM", "UNITID"]]

def colors(num):
    col = []
    for i in range(0, num):
        if labelled.values[i][1] in ivies:
            col.append('orange')
        else:
            col.append('black')
    return col

# pca = PCA(n_components=3)
#
# X = pca.fit_transform(data)
#
# fig = plt.figure(figsize=(6,6))
# ax = plt.axes(projection='3d')
# ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=colors(X.shape[0]), alpha=0.3) # Plot the documents

pca = PCA(n_components=2)

X = pca.fit_transform(data)

fig = plt.figure(figsize=(6,6))
ax = plt.axes()
#ax.scatter(X[:, 0], X[:, 1], ) # Plot the documents
for i in range(X.shape[0]):
    x, y = X[i, :]
    plt.scatter(x, y, c=colors(X.shape[0])[i], alpha=0.3)
    plt.annotate(
        labelled.values[i][0],
        xy=(x, y),
        xytext=(5, 2),
        textcoords='offset points',
        ha='right',
        va='bottom',
        fontsize=6)

plt.show()

