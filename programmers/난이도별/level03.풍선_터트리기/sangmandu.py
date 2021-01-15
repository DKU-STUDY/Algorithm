'''
https://programmers.co.kr/learn/courses/30/lessons/68646
풍선 터트리기
a의 개수가 최대 2백만개라 O(n)으로 끝내야함
1) 선택한 숫자를 기준으로 양 옆의 수들에 대해 양쪽의 최소값보다 작으면 된다.
2) 양쪽 중 한쪽이라도 만족하면 가능(작은 것을 터트릴 수 있는 기회가 있기 떄문)
3) 왼쪽 오른쪽 두번에 거쳐서 1,2)를 만족하는지 기록 ; 동시에 비교하기는 어려움.
'''

def solution(a):
    answer = [0] * len(a)
    left = a[0] + 1
    for idx, val in enumerate(a):
        if val < left: answer[idx] += 1
        left = min(left, val)

    right = a[-1] + 1
    for idx, val in enumerate(a[::-1]):
        if val < right: answer[len(a) - 1 - idx] += 1
        right = min(right, val)

    return [i > 0 for i in answer].count(True)

'''
'''