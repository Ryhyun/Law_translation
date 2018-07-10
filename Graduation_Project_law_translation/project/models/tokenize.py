import sys
import re
from konlpy.tag import Mecab

# for 형태소 분석
pattern = "SSO|SSC|SC|SE|SW|SH|SY|SF|SN"
pos_tagger =Mecab()
nnpattern = "NNG|NNP"
def tokenize_basic(doc):
    a= []
    for t in pos_tagger.pos(doc):
        if( re.search(pattern, t[1]) != None):
            continue
        else:
            a.append('/'.join(t))
    return a

def tokenize_n(doc):
    pos_tagger =Mecab()

    a= []
    for t in pos_tagger.pos(doc):
        if( re.search(nnpattern, t[1]) != None):
            a.append('/'.join(t))
        else:
            continue;
    return a



class SentenceReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.count = 0;

    def __iter__(self):
        for line in codecs.open(self.filepath, encoding='utf-8'):
            self.count += 1
            if (self.count % 10000 == 0):
                print(self.count)
            yield tokenize_basic(line)


class SentenceReader_n:
    def __init__(self, filepath):
        self.filepath = filepath
        self.count = 0;

    def __iter__(self):
        for line in codecs.open(self.filepath, encoding='utf-8'):
            self.count += 1
            if (self.count % 10000 == 0):
                print(self.count)
            yield tokenize_n(line)