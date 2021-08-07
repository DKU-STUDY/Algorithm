import re
import collections

def solution(word, pages):
    answer = 0
    #전처리
    word = word.lower()
    pages = [page.lower() for page in pages]
    
    page_urls = []
    page_basic_score = collections.defaultdict(int)
    page_linked = collections.defaultdict(list)
    page_linking_num = collections.defaultdict(int)
    page_matching_score = []
    
    for idx, page in enumerate(pages):
        #해당 페이지 url
        p = re.compile("<head>.*</head>", re.I|re.S)
        m = p.search(page)
        p = re.compile("<meta.*/>", re.I|re.S)
        m = p.search(m.group())
        p = re.compile("\"https://.*\"", re.I)
        m = p.search(m.group())
        cur_page_url = m.group()[1:-1]
        page_urls.append(cur_page_url)
        
        #해당 페이지 기본 점수
        p = re.compile('[^a-z^A-Z]'+word+'[^a-z^A-Z]', re.I|re.S)
        m = p.findall(page)
        page_basic_score[cur_page_url] = len(m)
        
        #해당 페이지 참조 링크
        p = re.compile("\"https://.*\"", re.I)
        m = p.findall(page)
        page_linking_num[cur_page_url] = len(m)-1
        for link in m:
            if link[1:-1] != cur_page_url:
                page_linked[link[1:-1]].append(cur_page_url)
    
    for page_url in page_urls:
        matching_score = page_basic_score[page_url]
        for page_linking in page_linked[page_url]:
            matching_score += page_basic_score[page_linking] / page_linking_num[page_linking]
        
        page_matching_score.append(matching_score)
    
    print(page_matching_score.index(max(page_matching_score)))
    
    
    
    return page_matching_score.index(max(page_matching_score))

'''
 검색어에 가장 잘 맞는 웹페이지를 보여주기 위해 아래와 같은 규칙으로 검색어에 대한 웹페이지의 매칭점수를 계산
 - 한 웹페이지에 대해서 기본점수, 외부 링크 수, 링크점수, 그리고 매칭점수를 구할 수 있다.
    - 한 웹페이지의 기본점수는 해당 웹페이지의 텍스트 중, 검색어가 등장하는 횟수이다. (대소문자 무시)
    - 한 웹페이지의 링크점수는 (해당 웹페이지로 링크가 걸린 다른 웹페이지의 기본점수 ÷ 외부 링크 수)의 총합이다.
        - 한 웹페이지의 외부 링크 수는 해당 웹페이지에서 다른 외부 페이지로 연결된 링크의 개수이다.
    - 한 웹페이지의 매칭점수는 기본점수와 링크점수의 합으로 계산한다.
http://zeany.net/46
'''