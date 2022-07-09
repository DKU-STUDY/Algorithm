# N x M 격자판
# 각 칸에 적 하나.
# N+1 행의 모든 칸에는 성이 있다.
# 궁수
#   성이 있는칸에 3명 배치. 하나의 칸에는 최대 1명의 궁수.
#   궁수는 적하나를 공격한다.
#   모든 궁수는 동시에 공격한다.
#   거리가 D 이하인 적중에서 가장 가까운적을 공격한다. 그러한 적이 여러명이면 가장 왼쪽에 있는 적을 공격한다. 같은 적이 여러 궁수에게 공격당할수있다.
# 적
#   공격 받으면 게임에서 제외된다.
#   공격이 끝나면 아래로 한칸 이동한다. 성이 있는 칸으로 이동한 경우 게임에서 제외된다.
import sys
from itertools import combinations


def kill_enemy(arrow_x_positions, arrow_y_position, range, enemy_set):
    res = 0
    while enemy_set:
        i, j, k = arrow_x_positions
        arrows = [Arrow(i, arrow_y_position, range), Arrow(j, arrow_y_position, range), Arrow(k, arrow_y_position, range)]
        for arrow in arrows:
            arrow.set_enemy(enemy_set)

        remove_enemy_list = list()
        for arrow in arrows:
            kill = arrow.kill()
            if kill is not None:
                remove_enemy_list.append(kill)

        for distance, remove_enemy in remove_enemy_list:
            if remove_enemy is not None and remove_enemy in enemy_set:
                enemy_set.remove(remove_enemy)
                res += 1

        tmp_set = set()
        for x, y in enemy_set:
            if y + 1 < arrow_y_position:
                tmp_set.add((x, y+1))
        enemy_set = tmp_set
    return res

class Arrow:
    def __init__(self, x, y, range):
        self.x = x
        self.y = y
        self.range = range
        self.enemy_list = list()

    def calculate(self, enemy_position):
        ex, ey = enemy_position
        return abs(ex - self.x) + abs(ey - self.y)

    def set_enemy(self, enemys):
        self.reset()
        for enemy in enemys:
            distance = self.calculate(enemy)
            if distance <= self.range:
                self.enemy_list.append((distance, enemy))

    def kill(self):
        if len(self.enemy_list) == 0:
            return None
        self.enemy_list.sort()
        return self.enemy_list[0]

    def reset(self):
        self.enemy_list = list()

N, M, D = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
enemy = set()
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            enemy.add((x, y))

res = 0
for arrow_x_positions in combinations(range(M), 3):
    res = max(res, kill_enemy(arrow_x_positions, N, D, enemy.copy()))
print(res)
