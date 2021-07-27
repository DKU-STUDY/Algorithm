'''
https://programmers.co.kr/learn/courses/30/lessons/42747#
H-Index
1. 문제 설명대로 비교. 1000편 이하이므로 2중 반복문 사용 가능.
2. all을 사용해서 i <=j 와 j >= i를 모두 만족하면 return
'''
def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations), 0, -1):
        if all([j >= i for j in citations[:i]]) and all([j <= i for j in citations[i:]]): return i
    return 0
'''
세상에 고수는 많다..
1) 이중 반복문을 안써도 되는 비교
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
    
2) ㄹㅇ 고인물. 응용력이 말도 안됨
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
'''