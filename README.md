# Law_translation


http://52.79.208.206:5000/



프로젝트 목표는 위의 사진과 같이 우리가 일상에서 사용하는 용어로도 법 조문 검색이 가능하도록 하는 검색기를 만들려고 한다.



프로젝트를 진행하기 위해서는 몇가지 과정이 선행돼야했다.

첫째로 일상용어를 이해하기 위한 머신러닝 모델이다. 

이는 먼저 NAVER 지식인의 법관련 데이터를 수집하여 Word2Vec을 이용하여 학습을 시키고자 한다.



![image](https://user-images.githubusercontent.com/28247914/42813786-103b35b8-89fd-11e8-9f3b-90ea87233d09.png)


그리고 나서 필요한 모델은  Word2Vec으로 사상된 용어들을 Clustering하는 모델이다 .

K-means Custering알고리즘을 이용하여 개발하였고,

결과로 나온 Cluster를 분석하여 카테고리를 태깅하려 한다. 


![image](https://user-images.githubusercontent.com/28247914/42813800-2068fc5e-89fd-11e8-92f0-3cd71755119e.png)


프로토 타입으로 만든 웹이다

"집주인이 원룸 보증금을 안줘요"라는 텍스트가 입력됐을 때 

시스템은 Input을 형태소분석을 하여 각 형태소 별 카테고리를 출력한다.


![image](https://user-images.githubusercontent.com/28247914/42813812-282f0f50-89fd-11e8-8864-fad8bf642cf4.png)


