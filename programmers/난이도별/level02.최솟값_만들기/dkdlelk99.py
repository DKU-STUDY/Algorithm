# 출처 https://programmers.co.kr/learn/courses/30/lessons/12941
# input A, B 길이가 같은 자연수 배열 (배열 크기, 원소 크기는 둘 다 1,000 이하)
# output A, B에서 각 원소를 곱한 값의 합이 최소가 되는 값

# 예를 들어 A = [1, 4, 2] , B = [5, 4, 4] 라면
# A에서 첫번째 숫자인 1, B에서 두번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)
# A에서 두번째 숫자인 4, B에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)
# A에서 세번째 숫자인 2, B에서 첫번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)
# 즉, 이 경우가 최소가 되므로 29를 return 합니다.

def solution(A,B):
    answer = 0
    A.sort(), B.sort(reverse=True)
    for a, b in zip(A, B):
        answer += a*b
    return answer

print(solution([1,4,2], [5,4,4]) == 29, solution([1,4,2], [5,4,4]))
print(solution([1,2], [3,4]) == 10, solution([1,2], [3,4]))
