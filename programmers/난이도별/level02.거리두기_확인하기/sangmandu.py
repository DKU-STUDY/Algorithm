'''
https://programmers.co.kr/learn/courses/30/lessons/81302
거리두기 확인하기
[풀이]
1. 각 places 마다 답을 내야함
=> y,x = (4, 4)가 되기 이전에 반복문을 탈출하면 문제가 있는 것으로 판단
=> 여기서는 break를 위해 y와 x에 대한 이중 포문보다 while을 사용했다
=> for문을 사용하면 x에 대한 포문, y에 대한 포문을 계속 탈출해야함
=> while문으로 하나의 반복문만 탈출하도록 함
=> 함수를 선언하는 것이 좀 더 깔끔하다고 생각이 됨 (반복문은 break를 함수는 return이 가능하므로)
2. 각 좌표를 기준으로, 오른쪽과 아래 그리고 오른쪽 위와 오른쪽 아래를 살피도록 함
2-1. 오른쪽과 아래의 경우
=> 바로 옆에 P가 존재
=> 바로 옆에 O가 존재하고 그 옆에 P가 존재
=> 위 두 경우에 대해서만 항상 거리두기에 실패한다
2-2. 오른쪽 위와 오른쪽 아래의 경우
=> 대각선으로 P가 존재하는데 가로와 세로로 파티션이 존재하지 않음
=> 이 한 경우에 대해서만 항상 거리두기에 실패한다
'''
def solution(places):
    result = []
    for p in places:
        y = x = -1
        while True:
            x = (x + 1) % 5
            y = y + 1 if x == 0 else y
            if y * x >= 16:
                break

            if p[y][x] != "P":
                continue

            if x + 1 < 5:
                if p[y][x + 1] == "P":
                    break
                elif p[y][x + 1] == "O" and x + 2 < 5 and p[y][x + 2] == "P":
                    break

            if y + 1 < 5:
                if p[y + 1][x] == "P":
                    break
                elif p[y + 1][x] == "O" and y + 2 < 5 and p[y + 2][x] == "P":
                    break

            if x + 1 < 5 and y - 1 >= 0:
                if p[y - 1][x + 1] == "P":
                    if p[y][x + 1] == "O" or p[y - 1][x] == "O":
                        break

            if x + 1 < 5 and y + 1 < 5:
                if p[y + 1][x + 1] == "P":
                    if p[y][x + 1] == "O" or p[y + 1][x] == "O":
                        break

        result.append(1 if y * x >= 16 else 0)
    return result
'''
'''