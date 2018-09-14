from project import app

from project.models.preprocessing import analyzeText
from project.models.clustering import analizeCluster
from project.models.dataStructure import dataStructure
from flask import render_template, request


@app.route('/', methods=['GET'])
def start():
    return render_template('index.html', chk = 0 )


@app.route('/civil', methods=['POST'])
def civil():
    if request.method == "POST":
        input = request.form['civil_input']

    else:
        input= None


    output = analyzeText(input)
    cluster = analizeCluster(output)

    result = []
    detail = ['법인, 비법인', '소송 관련', '가족 관계', '부동산 계약', '부동산 계약',
              '소송 관련', '땅 거래, 계약 등', '분쟁 해결', '법 용어 관련', '상속',
              '소송 관련', '상속', '변호사와의 상담 내용', '고소 사기 등', '소송 관련',
              '계약 관련', '기타', '손해 배상', '소송 관련', '소송 관련']

    for i in range( len(output)):
        tempDict = {}

        tempDict['output'] = output[i]
        tempDict['cluster'] = cluster[i]
        if( cluster[i] != '학습 중 입니다'):
            tempDict['detail'] = detail[cluster[i]]
        result.append(tempDict)

    totalC = len( cluster)
    tempArr = [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range( totalC):
        if (cluster[i] != '학습 중 입니다'):
            if( int( cluster[i]) == 5 or int( cluster[i]) == 10 or int( cluster[i]) == 14 or int( cluster[i]) == 18 or int( cluster[i]) == 19 ):
                tempArr[1] += 1
            elif(int( cluster[i]) == 4 or int( cluster[i]) == 6 ):
                tempArr[3] += 1
            elif( int( cluster[i]) == 11):
                tempArr[9] += 1
            else:
                tempArr[ int(cluster[i])] += 1
    strResult = '    "' + str(input) + '" 분석하면   '
    aResult = ""
    cnt = 0

    indArr = []
    for i in range(20):
        if( tempArr[i] != 0 ):
            cnt += tempArr[i]
            indArr.append(i)
            aResult = aResult + " " +  detail[i]+"일 확률:" + str(float("{:.2f}".format(tempArr[i] / totalC))* 100 ) + "% "


    if cnt == 0 :
        strResult = '    "' + str(input) + '" 학습 중 입니다~'

    cate, name1, name2, name3, julC = dataStructure( indArr);

    return render_template('index.html',chk = 1, input = input, result= result , cate = cate, name1= name1 , name2 = name2 , name3 = name3, julC = julC , strResult= strResult, aResult = aResult )



@app.route('/test', methods=['GET'])
def test():
    cate , name1 , name2 , name3 = dataStructure() ;


    return render_template('modal.html', cate = cate, name1= name1 , name2 = name2 , name3 = name3 )

