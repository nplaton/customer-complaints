from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import numpy as np


def text_to_cluster(nmf_weights):
    cluster = []
    number_clusters = len(nmf_weights[0])
    for array in nmf_weights:
        i = np.argmax(array)
        for c in xrange(number_clusters):
            if i == c:
                cluster.append(c)
    return cluster

def nmf_generator(series, n=3):

    vectorizer = TfidfVectorizer()
    vectorizer = vectorizer.fit(series)
    texts_vectorized = vectorizer.transform(series).todense()

    feature_words = vectorizer.get_feature_names()

    nmf = NMF(n_components=n,init='random')
    nmf_weights = nmf.fit_transform(texts_vectorized)
    nmf_features = nmf.components_
    return nmf_weights

def clustering(df, n=3):
	weights = nmf_generator(df["tweets"], n)
	df["cluster"] = text_to_cluster(weights)
	return df