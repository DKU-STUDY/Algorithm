'''
https://www.acmicpc.net/problem/2961
도영이가 만든 맛있는 음식
[풀이]
1. 조합될 수 있는 모든 경우를 구한다
2. 조합마다 신맛과 쓴맛의 차를 구한다
'''
import sys
input = sys.stdin.readline
N = int(input().strip())

cook = [tuple(map(int, input().strip().split())) for _ in range(N)]
foods = []
for sour, bitter in cook:
    temp = []
    for food in foods:
        temp.append(food + [[sour, bitter]])
    temp.append([[sour, bitter]])
    foods.extend(temp)

min_diff = abs(cook[0][0]-cook[0][1])
for food in foods:
    sour, bitter = 1, 0
    for s, b in food:
        sour *= s
        bitter += b
    min_diff = min(min_diff, abs(sour-bitter))
print(min_diff)