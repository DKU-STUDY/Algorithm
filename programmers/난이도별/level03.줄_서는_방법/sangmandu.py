'''
https://programmers.co.kr/learn/courses/30/lessons/12936
줄 서는 방법
[풀이]
1. 각 경우의 수는 FACTORIAL 만큼 존재
=> 미리 factorial을 구해놓는다
=> math.factorial을 써도 가능하다
2. 사전 순으로 나열할 때 가장 처음 등장하는 수는
range(1, n+1)에서 (k-1) // (n-1)! 에 해당하는 순서의 수이다.
=> 반복문으로 이를 구한다
=> 매번 구해지는 순서는 결과 리스트에 추가
'''
def solution(n, k):
    dp = [1] + [0] * n
    for i in range(1, n + 1):
        dp[i] = i * dp[i - 1]

    lst = list(range(1, n + 1))
    ret = []
    for i in range(n - 1, -1, -1):
        idx = (k - 1) // dp[i]
        ret.append(lst.pop(idx))
        k = k % dp[i]
    return ret
'''
첫번째 제출한 코드.
효율성 뿐만 아니라 정확성 테스트에서도 시간초과가 난다.
왜냐하면 product는 O(n!) 의 시간복잡도를 가지기 때문.
여기서 O(N) 으로 돌려야 겠다고 직감 => 순서문제구나!

from itertools import product
def solution(n, k):
    lst = list(map(str, list(range(1, n+1))))
    pdt = list(product(*([lst] * n)))
    idx = 0
    for p in pdt:
        if len(set(p)) == n:
            if idx == k-1:
                return list(map(int, p))
            else:
                idx += 1
'''