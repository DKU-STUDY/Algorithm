'''
https://www.acmicpc.net/problem/1027
고층 건물
[풀이]
1. 빌딩은 기본적으로 양 옆 건물을 반드시 볼 수 있다
=> 따라서 기본적으로 2의 카운트를 가지고 시작
=> 양쪽 끝 건물은 1의 카운트를 가지고 시작
=> 만약 n=1 이라면 0을 출력
2. 탐색은 왼쪽과 오른쪽 방향으로 2만큼부터 시작
=> 양옆 건물은 반드시 볼 수 있기때문
3. 탐색 시작시 기준이 되는 기울기는 이웃한 빌딩과의 기울기로 설정
4. 오른쪽 기준, 기울기가 이전에 나온 최대기울기보다 커야 볼 수있음
5. 왼쪽 기준, 기울기가 이전에 나온 최소기울기보다 작아야 볼 수 있음
=> 4번과 5번을 통일해주기 위해 왼쪽일 때는 -1을 곱해준다
=> 따라서 똑같이 최대로 비교해줄 수 있음
'''
n = int(input())
lst = list(map(int, input().split()))
cnt = [1] + [2] * (n-2) + [1]
for src in range(n):
    for i, drt in enumerate([range(src-2, -1, -1), range(src+2, n, 1)]):
        sign = 2*i-1
        if not drt:
            continue
        max_grad = -(lst[src]-lst[src+sign])
        for dst in drt:
            if max_grad < sign * (lst[src]-lst[dst])/(src-dst):
                max_grad = sign * (lst[src]-lst[dst])/(src-dst)
                cnt[src] += 1
print(max(cnt) if n > 1 else 0)
