from pandas import Series, DataFrame
import pandas as pd
import re


def dataStructure():
    a = pd.read_csv('test.csv',
                    names=['value', 'category1', 'category2', 'category3', 'category4', 'category5', 'cluster1',
                           'cluster2'])
    a = a.fillna(0)

    name = []
    cate1 = []
    name1 = []

    cate2 = []
    name2 = []

    cate3 = []
    name3 = []

    cate4 = []
    cate5 = []

    for i in range(len(a)):
        # print( a.iloc[i]['value'])
        p1 = '제[0-9]편';
        if (re.match(p1, str(a.iloc[i]['value']))):
            name1.append(str(a.iloc[i]['value']))

            if (len(cate5) != 0):
                cate4.append(cate5)
                cate5 = []

            if (len(cate4) != 0):
                cate3.append(cate4)
                cate4 = []
                cate2.append(cate3)
                cate3 = []
                cate1.append(cate2)
                cate2 = []

            continue

        p2 = '제[0-9]+장';
        if (re.match(p2, str(a.iloc[i]['value']))):
            name2.append(str(a.iloc[i]['value']))

            if (len(cate5) != 0):
                cate4.append(cate5)
                cate5 = []

            if (len(cate4) != 0):
                #print(cate2)
                cate3.append(cate4)
                cate4 = []

                cate2.append(cate3)
                cate3 = []

            name3.append('제1절.')
            continue

        p3 = '제[0-9]+절';
        if (re.match(p3, str(a.iloc[i]['value']))):
            if (name3[-1] == '제1절.'):
                name3.pop()
            name3.append(str(a.iloc[i]['value']))
            if (len(cate5) != 0):
                cate4.append(cate5)
                cate5 = []

            if (len(cate4) != 0):
                cate3.append(cate4)
                cate4 = []

            continue

        if (i != 0):
            if(str(a.iloc[i]['value'] )== '0' ):
                continue;
            if (int(a.iloc[i]['category5']) == 0):
                if (len(cate5) != 0):
                    cate4.append(cate5)
                    cate5 = []
                cate4.append([str(a.iloc[i]['value'])])

            else:
                cate5.append(str(a.iloc[i]['value']))

    if (len(cate4) != 0):
        if (len(cate5) != 0):
            cate4.append(cate5)
            cate5 = []

        cate3.append(cate4)
        cate4 = []
        cate2.append(cate3)
        cate3 = []
        cate1.append(cate2)
        cate2 = []




    return cate1, name1, name2, name3;
