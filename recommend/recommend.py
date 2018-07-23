import logging
import time
import tqdm

import numpy as np
import pandas as pd
import codecs
from implicit.als import AlternatingLeastSquares
from implicit.approximate_als import (AnnoyAlternatingLeastSquares, FaissAlternatingLeastSquares,
                                      NMSLibAlternatingLeastSquares)
from implicit.bpr import BayesianPersonalizedRanking
from implicit.nearest_neighbours import (BM25Recommender, CosineRecommender, TFIDFRecommender, bm25_weight)
from scipy.sparse import coo_matrix


from recommend import models

MODELS = {"als":  AlternatingLeastSquares,
          "nmslib_als": NMSLibAlternatingLeastSquares,
          "annoy_als": AnnoyAlternatingLeastSquares,
          "faiss_als": FaissAlternatingLeastSquares,
          "tfidf": TFIDFRecommender,
          "cosine": CosineRecommender,
          "bpr": BayesianPersonalizedRanking,
          "bm25": BM25Recommender}


def get_model(model_name):
    model_class = MODELS.get(model_name)
    if not model_class:
        raise ValueError("Unknown Model '%s'" % model_name)
    # some default params
    if issubclass(model_class, AlternatingLeastSquares):
        params = {'factors': 64, 'dtype': np.float32}
    elif model_name == "bm25":
        params = {'K1': 100, 'B': 0.5}
    elif model_name == "bpr":
        params = {'factors': 63}
    else:
        params = {}

    return model_class(**params)


def generate_csrmatrix():

    score = []
    fund = []
    user = []
    data = models.FundFlow.selectAll()
    for item in data:
        score.append(1)
        user.append(item[0])
        fund.append(item[1])

    score = pd.Series(score)
    score = score.astype(np.float32)
    fund = pd.Series(fund)
    fund = fund.astype("category")
    user = pd.Series(user)
    user = user.astype("category")

    result = coo_matrix((score,(fund.cat.codes,user.cat.codes))).tocsr()
    user = np.array(list(user.cat.categories))
    fund = np.array(list(fund.cat.categories))

    return fund, user, result


def calculate(model_name):

    funds, users, scores = generate_csrmatrix()

    model = get_model(model_name)
    if issubclass(model.__class__, AlternatingLeastSquares):
        logging.debug("weighting matrix by bm25_weight")
        scores = bm25_weight(scores, K1=100, B=0.8)
        model.approximate_recommend = False

    scores = scores.tocsr()

    logging.debug("training model %s", model_name)
    start = time.time()
    model.fit(scores)
    logging.debug("trained model '%s' in %0.2fs", model_name, time.time() - start)

    user_scores = scores.T.tocsr()
    print(users)
    print(funds)
    print(user_scores)
    with tqdm.tqdm(total=len(users)) as progress:
        with codecs.open("D:\Github\FundRecommendSystem\outputFile.tsv", "w", "utf8") as o:
            for userid, usernames in enumerate(users):
                for fundid, ascore in model.recommend(userid, user_scores):
                    o.write("%s\t%s\t%s\n" % (usernames, funds[fundid], ascore))
                progress.update(1)
                # print(userid, funds[fundid], score)

def calculate_similar_fund(model_name):
    funds, users, scores = generate_csrmatrix()

    model = get_model(model_name)
    if issubclass(model.__class__, AlternatingLeastSquares):
        logging.debug("weighting matrix by bm25_weight")
        scores = bm25_weight(scores, K1=100, B=0.8)
        model.approximate_recommend = False

    scores = scores.tocsr()
    logging.debug("training model %s", model_name)
    start = time.time()
    model.fit(scores)
    logging.debug("trained model '%s' in %0.2fs", model_name, time.time() - start)


