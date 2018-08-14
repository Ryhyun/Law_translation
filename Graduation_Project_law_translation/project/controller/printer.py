from project import app

from project.models.preprocessing import analyzeText
from project.models.clustering import analizeCluster
from flask import render_template, request


@app.route('/', methods=['GET'])
def start():
    return render_template('index.html')


@app.route('/civil', methods=['POST'])
def civil():
    if request.method == "POST":
        input = request.form['civil_input']

    else:
        input= None


    output = analyzeText(input)
    cluster = analizeCluster(output)
    #print( output)
    #print( cluster)

    result = []
    detail = ['법인, 비법인', '소송 관련', '가족관계', '부동산 계약', '부동산 계약',
              '소송 관련', '땅 거래, 계약 등', '분쟁 해결', '법 용어 관련', '상속',
              '소송 관련', '상속', '변호사와의 상담 내용', '고소 사기 등', '소송 관련 문의',
              '계약 관련', '기타 사람 이름', '손해배상', '소송 관련 문의', '소송 관련 문의']
    for i in range( len(output)):
        tempDict = {}
        tempDict['output'] = output[i]
        tempDict['cluster'] = cluster[i]
        if( cluster[i] != '학습 중 입니다'):
            tempDict['detail'] = detail[cluster[i]]
        result.append(tempDict)



    return render_template('index.html',input = input, result= result)

