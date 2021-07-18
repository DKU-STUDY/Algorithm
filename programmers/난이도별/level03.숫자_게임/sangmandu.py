'''
https://programmers.co.kr/learn/courses/30/lessons/12987
숫자 게임
[풀이]
1. 두 리스트 A, B를 내림차순으로 정렬
2. A에 원소보다 큰 B의 원소를 찾는다.
=> 못찾으면 B의 포인터를 +1씩 증가
=> 찾으면 A와 B의 포인터를 +1씩 증가
=> 이 방법이 왜 적용되는가?
=> B의 입장에서는 현재 포인터에서 a보다 b가 크면 이를 만족하는 b중에 가장 최소
=> 이 말은 B에서 나올 수 있는 경우의 수중 가장 효율적인 경우
=> A의 입장에서는 현재 포인터에서 a보다 큰 b를 못찾으면 이후에 있는 a보다 큰 b를 찾을 수 없음
=> 따라서 일단 현재 제일 작은 a부터 넘고 다음 문제를 해결해야함
3. 시간복잡도는 O(N+M)
'''
def solution(A, B):
    A.sort()
    B.sort()
    idx = result = 0

    for a in A:
        while idx < len(B):
            if a < B[idx]:
                result += 1
                idx += 1
                break
            idx += 1

    return result


'''
첫번째 제출한 코드.
정확성 테스트는 만점.
효율성 테스트는 O(n^2) 이 되버려서 시간초과.

def solution(A, B):
    B.sort()
    result = 0
    for a in A:
        idx = 0
        while idx < len(B) and a >= B[idx]:
            idx += 1
        if idx == len(B):
            B = B[1:]
        else:
            B = B[:idx]+B[idx+1:]
            result += 1

    return result
    
두번째 제출한 코드는 이진탐색 코드.
그러나 시간초과. O(N*logN) 도 안되나보다.

다음은 좀 더 효율성이 좋은 O(N) 코드
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            answer = answer + 1
            j = j+1

    return answer

이 코드 역시 A를 고정시키고 B를 증가시켰는데,
반복문의 대상을 B로 설정(나는 A로 설정)
'''