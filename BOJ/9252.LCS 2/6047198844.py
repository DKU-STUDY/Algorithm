# 문제
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
#
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
#
# 입력
# 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
A = '.' + input()
B = '.' + input()

# memo[i][j]
# A[~i] / B[~j] 까지의 최장 공통 부분 수열의 길이.
memo = [[0 for _ in range(len(A))] for _ in range(len(B))]

for y in range(1, len(B)):
    for x in range(1, len(A)):
        if A[x] == B[y]:
            # 정의를 생각해보자. memo[y-1][x-1] 은 바로 직전의 최장 공통 부분 수열이다.
            # x, y 는 현재를 뜻한다. 현재값이 같다면, 최적화된 직전값에 1을 더했을때도 최적값이다.
            memo[y][x] = memo[y-1][x-1] + 1
        else:
            # 바로 직전의 두 값중 하나가 최적값이다.
            # 근거는 연속되지 않아도 되기때문에 직전값의 값을 계승해도 문제가 없다. 따라서 직전의 값을 계승한다.
            memo[y][x] = max(memo[y-1][x], memo[y][x-1])

# 맨끝에서 부터 찾아나간다.
# 영향을 어디서 부터 받았는지 생각해보자.
# 값이 같다면, 직전으로부터 영향을 받은것이고, 값이 틀리다면 큰값으로 부터 영향을 받은것이다. 영향 받는 곳으로 역추적하자. 어쩌피, 맨 마지막값이 답이다.
res = ''
M, N = len(B) - 1, len(A) - 1

print(memo[M][N])
while M > 0 and N > 0:
    if A[N] == B[M]:
        res += A[N]
        M -= 1
        N -= 1
    else:
        if memo[M][N-1] > memo[M-1][N]:
            N -= 1
        else:
            M -= 1
print(res[::-1])