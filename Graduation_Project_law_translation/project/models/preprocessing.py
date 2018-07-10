import sys
import re
import codecs
from konlpy.tag import Mecab
from gensim.models import Word2Vec
from sklearn.cluster import KMeans

from project.models.tokenize import SentenceReader_n,SentenceReader,tokenize_basic,tokenize_n






def analyzeText( input):

    output =tokenize_n(input)
    return output

