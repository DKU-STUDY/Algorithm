'''
https://www.acmicpc.net/problem/1138
한 줄로 서기
[풀이]
1. 키가 큰 순으로 자리를 배치시킨다.
=> 키가 큰 사람들을 고려하기 때문에 앞사람 만을 고려하면 된다.
=> 뒷 사람은 다 작으므로 고려할 필요 없음
2. 각 사람은 배치중인 자리를 기준으로 자신의 값만큼의 인덱스에 추가한다
=> 만약 현재 3명이 줄을 서있고 (이 사람들은 모두 자신보다 키가 큼)
=> 자신 왼쪽으로 1명이 있다면 1 ... (여기) ... 2 로 배치하면 된다
3. 문자열 꼴로 출력
'''
n = int(input())
lst = map(int, input()[::-1].split())
ret = []
for idx, val in enumerate(lst):
    ret = ret[:val]+[str(n-idx)]+ret[val:]
print(' '.join(ret))