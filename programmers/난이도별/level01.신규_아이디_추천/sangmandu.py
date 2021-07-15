'''
https://programmers.co.kr/learn/courses/30/lessons/72410
신규 아이디 추천
[풀이]
0. 정규식 사용 문제. 정규식을 모른다면 끔찍하다.
'''
import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = ''.join(re.findall('[a-z]|[0-9]|[.]|[_]|[-]', new_id))
    new_id = re.sub('[.]{2,}', '.', new_id)
    if len(new_id) and new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id) and new_id[-1] == ".":
        new_id = new_id[:-1]
    size = len(new_id)
    if not size: new_id += "a"
    if size >= 16:
        new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    while len(new_id) < 3:
        new_id = new_id + new_id[-1]
    return new_id
'''
정규식이랑 if를 너무 혼재해서 사용한 듯 하다
나보다 더 정규식을 잘 쓴 사람 코드를 배워야겠다
심지어 코드 구성도 멋지다

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    # [^] 는 특정 문자를 제외하라는 의미
    
    st = re.sub('\.+', '.', st)
    # 이 부분은 re.sub('[.]{2,}', '.', new_id)와 차이는 없다.
    
    st = re.sub('^[.]|[.]$', '', st)
    # ^는 ~로 시작하는, $는 ~로 끝나는. 이 정규식 문법을 생각을 못했다. 문제 의도는 이거였던것 같다
    
    st = 'a' if len(st) == 0 else st[:15]
    # 5~6단계를 합친 조건. 멋있다
    
    st = re.sub('^[.]|[.]$', '', st)
    # 이 때는 첫 시작은 고려하지 않아도 된다. 그냥 복붙한 것으로 추정.
    
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
'''