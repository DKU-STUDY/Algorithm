def solution(A,B):
# A와 B 배열에서 한 개씩 뽑아 두 수를 곱한 합이 최소가 되는 값을 구하는 문제
# A를 오름차순, B를 내림차순으로 정리하고 같은 인덱스끼리 곱한 합을 반환하게 구성함
    A.sort()
    B.sort(reverse = True)
    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer
