import numpy as np
import sklearn.cluster as cls


def AgglomerativeClustering(data, clusters_num):
    cluster = cls.AgglomerativeClustering(n_clusters=clusters_num, linkage='average', affinity='cosine')
    cluster.fit_predict(data)
    labels = cluster.labels_
    return labels


def KMeans(data, clusters_num):
    cluster = cls.KMeans(n_clusters=clusters_num, random_state=0)
    cluster.fit_predict(data)
    labels = cluster.labels_
    return labels


def MiniBatchKMeans(data, clusters_num):
    cluster = cls.MiniBatchKMeans(n_clusters=clusters_num, init='k-means++')
    cluster.fit_predict(data)
    labels = cluster.labels_
    return labels


def MeanShift(data, quantiles):
    bandwidth = cls.estimate_bandwidth(data, quantile=quantiles)
    ms = cls.MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(data)
    labels = ms.labels_
    labels_unique = np.unique(labels)
    cluster_centers = ms.cluster_centers_
    n_clusters_ = len(labels_unique)
    return labels, n_clusters_

def Bitch(data, clusters_num):
    cluster = cls.Birch(clusters_num)
    cluster.fit_predict(data)
    labels = cluster.labels_
    return labels