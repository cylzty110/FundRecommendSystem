import sklearn.cluster as cls
import pandas as pd
import numpy as np


def AgglomerativeClustering(data):
    cluster = cls.AgglomerativeClustering(n_clusters=3, linkage='average', affinity='cosine')
    cluster.fit_predict(data)
    labels = cluster.labels_
    return labels


def KMeans(data):
    cluster = cls.KMeans(n_clusters=3, random_state=0)
    cluster.fit_predict(data)
    labels = cluster.labels_
    return labels


def MiniBatchKMeans(data):
    cluster = cls.MiniBatchKMeans(n_clusters=3, init='k-means++')
    cluster.fit_predict(data)
    labels = cluster.labels_
    return labels


def MeanShift(data):
    bandwidth = cls.estimate_bandwidth(data, quantile=0.2)
    ms = cls.MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(data)
    labels = ms.labels_
    labels_unique = np.unique(labels)
    cluster_centers = ms.cluster_centers_
    n_clusters_ = len(labels_unique)
    return labels, n_clusters_