# 출처 https://programmers.co.kr/learn/courses/30/lessons/70129
# input 0과 1로 이루어진 문자열 s
# output 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수
# 여기서 x에 대한 이진 변환이란 아래와 같다
# 1. x의 모든 0을 제거합니다.
# 2. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.

def solution(s):
    cnt_change = 0
    cnt_zero = 0
    while s != '1':
        cnt_change += 1
        cnt = 0
        for i in s:
            if i =='0':
                cnt += 1
        cnt_zero += cnt
        s = format((len(s)-cnt),'b')
    return [cnt_change,cnt_zero]


print(solution('110010101001'), solution('110010101001') == [3,8])
print(solution('01110'), solution('01110') == [3,3])
print(solution('1111111'), solution('1111111') == [4,1])
