'''
https://programmers.co.kr/learn/courses/30/lessons/12906
연속된 수 제거하기
앞자리 수와 비교해서 제거해감
'''

def solution(arr):
    answer = []
    temp = arr[0]
    for i in arr[1:]:
        if temp != i:
            answer.append(temp)
        temp = i
    answer.append(temp)
    return answer

'''
배울점이 있는 코드 다른사람 코드
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
'''