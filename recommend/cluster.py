from sklearn import preprocessing
from recommend import models, custom
from sklearn.cluster import AgglomerativeClustering

enc = preprocessing.OneHotEncoder()
enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
print(enc.n_values_)
print(enc.transform([[0, 1, 3]]).toarray())
print(enc.transform([[0, 1, 1]]).toarray())


#层次聚类
def hierarchicalClustering():
    data = []
    cluster = AgglomerativeClustering(n_clusters=2, linkage='average').fit(data)
    label = cluster.labels_
    return label

