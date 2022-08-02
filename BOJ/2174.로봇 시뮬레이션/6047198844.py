import sys

# 5, 4
X, Y = map(lambda i: int(i) - 1, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())

robots = []
for _ in range(N):
    x, y, d = sys.stdin.readline().split()
    robots.append((Y - int(y) + 1, int(x) - 1, d))

for _ in range(M):
    robot_idx, command, repeat = sys.stdin.readline().split()
    robot = robots[int(robot_idx) - 1]
    for _ in range(int(repeat)):
        if command == 'F':
            if robot[2] == 'N':
                robot = (robot[0] - 1, robot[1], 'N')
            elif robot[2] == 'W':
                robot = (robot[0], robot[1] - 1, 'W')
            elif robot[2] == 'E':
                robot = (robot[0], robot[1] + 1, 'E')
            elif robot[2] == 'S':
                robot = (robot[0] + 1, robot[1], 'S')
        elif command == 'L':
            if robot[2] == 'N':
                robot = (robot[0], robot[1], 'W')
            elif robot[2] == 'W':
                robot = (robot[0], robot[1], 'S')
            elif robot[2] == 'E':
                robot = (robot[0], robot[1], 'N')
            elif robot[2] == 'S':
                robot = (robot[0], robot[1], 'E')
        elif command == 'R':
            if robot[2] == 'N':
                robot = (robot[0], robot[1], 'E')
            elif robot[2] == 'W':
                robot = (robot[0], robot[1], 'N')
            elif robot[2] == 'E':
                robot = (robot[0], robot[1], 'S')
            elif robot[2] == 'S':
                robot = (robot[0], robot[1], 'W')

        y, x, pos = robot
        # 벽 위치
        if y < 0 or y > Y or x < 0 or x > X:
            print(f"Robot {robot_idx} crashes into the wall")
            exit()

        for i in range(len(robots)):
            if i != int(robot_idx) - 1:
                y, x, pos = robot
                if y == robots[i][0] and x == robots[i][1]:
                    print(f"Robot {robot_idx} crashes into robot {i+1}")
                    exit()

        robots[int(robot_idx) - 1] = robot
print('OK')