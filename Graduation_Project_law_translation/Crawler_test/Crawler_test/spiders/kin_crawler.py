import scrapy


class exampleSpider(scrapy.Spider):
    name = 'kinspider' # scrapy의 spider를 실행하기 위해 필요한 매개변수
    dirId = '60201' # 크롤링하고자 하는 카테고리
    kin_urls = 'http://kin.naver.com/qna/expertAnswerList.nhn?dirId=' + dirId # 네이버 지식인 기본 URL
    start_urls = [kin_urls]

    # 최신 1000개의 질문 목록을 가져온다.
    def parse(self, response):
        # 현재 목록에 각 질문의 링크를 타고 들어간다. parse_doc에서 나머지를 처리함.
        for item in response.css('td.title a'):
            yield response.follow(item, self.parse_doc)

        # 다음 페이지를 자동으로 넘어간다. 중복된 페이지는 scrapy가 url을 체크해서 알아서 처리해줌.
        for next_page in response.css('div.paginate > a'):
            yield response.follow(next_page, self.parse)

    # 각 질문의 링크에 들어가서 질문의 본문을 각각 txt 파일로 저장한다.
    def parse_doc(self, response):
        docId = response.request.url.split("docId=")[-1]
        title = response.css('span.title_text ::text').extract_first().strip().encode('utf8')
        question_contents = response.css('div#contents_layer_0 div._endContentsText ::text').extract()
        answer_contents = response.css('div#contents_layer_1 div._endContentsText ::text').extract()
        
        question = "\n".encode('utf8')
        answer = "\n".encode('utf8')
        
        for q in question_contents:
            question += q.strip().encode('utf8')
            question += "\n".encode('utf8')
            
        for a in answer_contents:
            answer += a.strip().encode('utf8')
            answer += "\n".encode('utf8')
            
        filename = 'raw/traffic.txt' 
        with open(filename, 'ab') as f:
            f.write(title)
            f.write(question)
            f.write(answer)
