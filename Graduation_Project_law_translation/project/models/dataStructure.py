from pandas import Series, DataFrame
import pandas as pd
import re


def dataStructure( arr):
    a = pd.read_csv('test.csv',
                    names=['value', 'category1', 'category2', 'category3', 'category4', 'category5', 'cluster1',
                           'cluster2'])
    a = a.fillna(-1)


    cate1 = []
    name1 = []

    cate2 = []
    name2 = []

    cate3 = []
    name3 = []

    cate4 = []
    cate5 = []

    julC = []

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
            if( i > 2 ):
                julC.append( julC[-1]);
            else:
                julC.append(-1);
            continue

        p3 = '제[0-9]+절';
        if (re.match(p3, str(a.iloc[i]['value']))):
            if (name3[-1] == '제1절.'):
                name3.pop()
                julC.pop()
            name3.append(str(a.iloc[i]['value']))

            chkk = 0;

            for ind, jnd in enumerate(arr):

                if (int(a.iloc[i]['cluster1']) == 5 or int(a.iloc[i]['cluster1']) == 10 or int(a.iloc[i]['cluster1']) == 14 or
                            int(a.iloc[i]['cluster1']) == 15 or int(a.iloc[i]['cluster1']) == 18 or int(a.iloc[i]['cluster1']) == 19):
                    a.iloc[i]['cluster1'] = 1
                elif (int(a.iloc[i]['cluster1']) == 4 or int(a.iloc[i]['cluster2']) == 6):
                    a.iloc[i]['cluster1'] = 3
                elif (int(a.iloc[i]['cluster1']) == 11):
                    a.iloc[i]['cluster1'] = 9

                if (int(a.iloc[i]['cluster2']) == 5 or int(a.iloc[i]['cluster2']) == 10 or int(a.iloc[i]['cluster2']) == 14 or
                            int(a.iloc[i]['cluster2']) == 15 or int(a.iloc[i]['cluster2']) == 18 or int(a.iloc[i]['cluster2']) == 19):
                    a.iloc[i]['cluster2'] = 1
                elif (int(a.iloc[i]['cluster2']) == 4 or int(a.iloc[i]['cluster2']) == 6):
                    a.iloc[i]['cluster2'] = 3
                elif (int(a.iloc[i]['cluster2']) == 11):
                    a.iloc[i]['cluster2'] = 9

                if ( int(a.iloc[i]['cluster1'])   == jnd  or int(a.iloc[i]['cluster2'])   == jnd ):

                    julC.append(ind);

                    chkk = 1;
                    break;
            if (chkk == 0):
                julC.append(-1);

            if (len(cate5) != 0):
                cate4.append(cate5)
                cate5 = []

            if (len(cate4) != 0):
                cate3.append(cate4)
                cate4 = []

            continue

        if (i != 0):
            if(str(a.iloc[i]['value'] )== '-1' ):
                continue;
            if (int(a.iloc[i]['category5']) == -1):
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

    return cate1, name1, name2, name3, julC;
