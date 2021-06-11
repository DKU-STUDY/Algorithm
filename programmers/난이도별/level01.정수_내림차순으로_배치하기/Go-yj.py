'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12933
문제 : 정수 내림차순으로 배치하기
입력받은 정수를 쪼갠 후 정렬하여 다시 합쳤습니다.
'''

def solution(n):
    n_list = list(str(n))
    n_list.sort()
    n_list.reverse()
    n_list = ''.join(n_list)
    return int(n_list)
