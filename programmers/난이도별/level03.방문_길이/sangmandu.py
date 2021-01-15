'''
https://programmers.co.kr/learn/courses/30/lessons/49994
방문 길이
dictionary, set 사용
'''

def solution(dirs):
    move = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
    x = y = 0
    answer = set()
    for i in dirs:
        dx = x + move[i][0]
        dy = y + move[i][1]
        if dx < -5 or dx > 5 or dy < -5 or dy > 5:
            continue
        answer.add((x, y, dx, dy))
        answer.add((dx, dy, x, y))
        x = dx
        y = dy

    return len(answer) // 2

'''
'''