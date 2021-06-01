import collections

N, M = map(int, input().split())
#모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다.
skip = dict()
for _ in range(N+M):
    key, value = map(int, input().split())
    skip[key] = value

Q = collections.deque()
Q.append(1)
path = set()
path.add(1)
dice_cnt = 0
while Q:
    dice_cnt += 1
    for _ in range(len(Q)):
        position = Q.popleft()
        for dice in range(1,6+1):
            new_position = position + dice
            #만약 주사위를 굴려서 이동한 결과가 100번 칸을 넘어간다면 이동할 수 없다.
            if new_position > 100:
                continue

            # 1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다.
            # 정답에 도달한 경우 주사위를 굴린 횟수를 반환하고 종료한다.
            if new_position == 100:
                print(dice_cnt)
                exit()

            #사다리나 뱀에 존재할경우. 해당 좌표로 이동한다.
            if new_position in skip:
                new_position = skip[new_position]

            #해당 경로가 발견되지 않았다면
            if new_position not in path:
                path.add(new_position)
                Q.append(new_position)

            #발견되었다면 Q에 넣지 않는다.

#항상 100번 칸에 도착할 수 있는 입력만 주어진다. -> Q가 empty인 경우는 없다.

#skip = {key: value for key, value in map(int, input().split()) for _ in range(N+M)} #뱀 / 사다리 정보 저장.
#https://bio-info.tistory.com/40