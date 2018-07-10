import sys
import re
import codecs

import pickle
from gensim.models import Word2Vec
from sklearn.cluster import KMeans
import gensim




def analizeCluster( input):

    kclusterer_20 = pickle.load(open('project/static/kclusterer_20', 'rb'))
    civil_model_n = gensim.models.Word2Vec.load('model/civil_law_n')

    output = []

    for text in input:
        try:
            output.append(kclusterer_20.classify(civil_model_n[text]))
        except:
            output.append('학습 중 입니다')



    return output


