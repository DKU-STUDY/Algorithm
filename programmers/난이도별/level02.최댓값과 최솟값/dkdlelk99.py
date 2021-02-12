# 출처 https://programmers.co.kr/learn/courses/30/lessons/12939
# input s 공백으로 구분된 둘이상의 정수들
# output '(최소값) (최대값)'

def solution(s):
    nums = list(map(int, s.split(" ")))
    return str(min(nums)) + " " + str(max(nums))

print(solution("1 2 3 4"), solution("1 2 3 4") == '1 4')
print(solution("-1 -2 -3 -4"), solution("-1 -2 -3 -4") == '-4 -1')
print(solution("-1 -1"), solution("-1 -1") == '-1 -1')
