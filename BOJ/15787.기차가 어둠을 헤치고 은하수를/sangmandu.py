'''
https://www.acmicpc.net/problem/15787
기차가 어둠을 헤치고 은하수를
[풀이]
1. 20칸인 기차 생성
2. 각 액션들을 인덱스 번호로 실행할 수 있도록 선언
=> exec 사용 => lambda 에서는 할당이 안되므로
3. 열차칸을 문자열로 만들고 set()으로 중복 조사.
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
train = [['0'] * 20 for _ in range(n)]

action = [
    lambda x, y : exec('train[x][y] = "1"'),
    lambda x, y : exec('train[x][y] = "0"'),
    lambda x, y : exec('train[x] = ["0"] + train[x][:-1]'),
    lambda x, y : exec('train[x] = train[x][1:] + ["0"]')
]
for _ in range(m):
    ipt = list(map(int, input().strip().split()))
    if len(ipt) == 3: a, b, c = ipt
    else: a, b = ipt; c = 0
    action[a-1](b-1, c-1)
print(len(set([''.join(t) for t in train])))
