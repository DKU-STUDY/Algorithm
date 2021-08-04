'''
https://www.acmicpc.net/problem/1110
더하기 사이클
[풀이]
1. n이 한자리수면 앞에 '0' 을 추가한다.
2. 계속 변해가는 숫자 tmp, 사이클 횟수 cnt 선언
3. 제시된 방법대로 사이클 구성
'''
n = input()
if len(n) == 1:
    n = '0' + n
tmp, cnt = n, 0
while True:
    a, b = tmp
    c = str(int(a) + int(b))
    d = c[-1]
    tmp = b + d
    cnt += 1
    if tmp == n:
        break
print(cnt)