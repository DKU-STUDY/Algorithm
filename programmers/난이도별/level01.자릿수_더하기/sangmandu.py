'''
https://programmers.co.kr/learn/courses/30/lessons/12931
자릿수 더하기
list(str) = str을 한글자씩 끊어서 리스트화
'''

def solution(n):
    return sum(list(map(int, list(str(n)))))

'''
string은 list로 간주되기 때문에 굳이 list화 할 필요 없음
return sum(list(map(int, str(n))))
'''