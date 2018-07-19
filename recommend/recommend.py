# import h5py
# import argparse
# import codecs
# import logging
# import time
# import tqdm
# import pandas
# import numpy as np
# from scipy.sparse import coo_matrix, csr_matrix,hstack
# from implicit.als import AlternatingLeastSquares
# from implicit.approximate_als import (AnnoyAlternatingLeastSquares, FaissAlternatingLeastSquares,NMSLibAlternatingLeastSquares)
# from implicit.bpr import BayesianPersonalizedRanking
# from implicit.nearest_neighbours import (BM25Recommender, CosineRecommender,TFIDFRecommender, bm25_weight)
# from recommend import models
#
# MODELS = {"als":  AlternatingLeastSquares,
#           "nmslib_als": NMSLibAlternatingLeastSquares,
#           "annoy_als": AnnoyAlternatingLeastSquares,
#           "faiss_als": FaissAlternatingLeastSquares,
#           "tfidf": TFIDFRecommender,
#           "cosine": CosineRecommender,
#           "bpr": BayesianPersonalizedRanking,
#           "bm25": BM25Recommender}
#
#
# def get_model(model_name):
#     model_class = MODELS.get(model_name)
#     if not model_class:
#         raise ValueError("Unknown Model '%s'" % model_name)
#     # some default params
#     if issubclass(model_class, AlternatingLeastSquares):
#         params = {'factors': 64, 'dtype': np.float32}
#     elif model_name == "bm25":
#         params = {'K1': 100, 'B': 0.5}
#     elif model_name == "bpr":
#         params = {'factors': 63}
#     else:
#         params = {}
#
#     return model_class(**params)
#
#
# def generate_data():
#
#
#     result = coo_matrix((data['score'].astype(np.float32),
#                         (data['fund'].cat.codes.copy(),
#                          data['user'].cat.codes.copy()))).tocsr()
#     return result
#
#
# def calculate(model_name):
#
#     artists, users, plays = generate_data()
#     model = get_model(model_name)
#     if issubclass(model.__class__, AlternatingLeastSquares):
#         logging.debug("weighting matrix by bm25_weight")
#         plays = bm25_weight(plays, K1=100, B=0.8)
#         model.approximate_recommend = False
#
#     plays = plays.tocsr()
#
#     logging.debug("training model %s", model_name)
#     start = time.time()
#     model.fit(plays)
#     logging.debug("trained model '%s' in %0.2fs", model_name, time.time() - start)
#
#     user_count = np.ediff1d(plays.indptr)
#     to_generate = sorted(np.arange(len(artists)), key=lambda x: -user_count[x])
#     with tqdm.tqdm(total=len(to_generate)) as progress:
#
#             progress.update(1)
#
#
#
#     pandas.read_table()[].cat
#
#
