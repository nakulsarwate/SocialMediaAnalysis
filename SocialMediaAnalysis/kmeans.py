import xlrd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

book = xlrd.open_workbook("DATA.xls")
sheet = book.sheet_by_name("Sheet1")

X = np.array()

#iterating over the entire excel sheet
if not sheet.cell(i, j).value == xlrd.empty_cell.value:
    X.append([sheet.cell(i, j).value])

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

colors = ['r','b','y','g','c','m']

for i in range(len(X)):
    print("coordinate:",X[i], "label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

plt.scatter(x,y)
plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()
