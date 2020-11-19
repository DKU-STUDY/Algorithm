'''
https://programmers.co.kr/learn/courses/30/lessons/12935
제일 작은 수 제거하기
remove, sorted
'''
def solution(arr):
    arr and arr.remove(sorted(arr)[0])
    return arr or [-1]
'''
sorted = NlonN
min = N
이니 최소값(최대값)을 이용할 것
'''