'''
https://programmers.co.kr/learn/courses/30/lessons/12933
정수 내림차순으로 배치하기 : 주어진 int의 자릿수별로 내림차순 정렬하여 int로 출력
double map
'''

def solution(n):
    return int(''.join(map(str, sorted(list(map(int, str(n))),reverse=True))))

''' sorted는 string으로 이루어진 int도 정렬한다. 따로 map(int, )할 필요 없음
def solution(n):
    return int("".join(sorted(str(n), reverse=True)));

'''