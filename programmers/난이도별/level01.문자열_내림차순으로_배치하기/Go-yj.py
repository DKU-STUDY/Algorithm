'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12917
문제 : 문자열 내림차순으로 배치하기
처음에는 ord(), chr()을 이용해서 아스키 코드로 바꾸고 정렬해서 문제를 해결했는데
매번 피드백 받은 것처럼 한 줄로 줄이고 더 간단하게 할 수 있는지 이것저것 시도해보다가
문자열 자체로도 정렬이 가능한 걸 알게 됐네요 ^^ 피드백 감사합니다!
'''

def solution(s):
    return "".join(sorted(s,reverse=True))
