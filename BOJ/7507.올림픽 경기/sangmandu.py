'''
https://www.acmicpc.net/problem/7507
올림픽 경기
[풀이]
1. 날짜 순으로 정렬 그리고 끝나는 시간으로 정렬한다.
2. 내가 보고 있는 프로그램이 다음에 위치하는 프로그램과 겹칠 때
=> 내가 보고 있는 프로그램이 먼저 끝난다(정렬을 그렇게 했으니까)
=> 이후에 프로그램을 하나 더 볼 가능성이 높다
=> 따라서 그대로 pass
3. 내가 보고 있는 프로그램이 다음에 위치하는 프로그램보다 먼저 끝난다
=> 볼 수 있는 프로그램 수를 하나 더 센다.
'''
import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    m = int(input())
    games = sorted([list(map(int, input().split())) for _ in range(m)], key = lambda x : (x[0], x[2]))
    max_games = 0
    cur_day = cur_ed = 0
    for day, st, ed in games:
        if cur_ed <= st or cur_day != day:
            max_games += 1
            cur_day, cur_ed = day, ed
    print(f"Scenario #{i+1}:\n{max_games}\n")