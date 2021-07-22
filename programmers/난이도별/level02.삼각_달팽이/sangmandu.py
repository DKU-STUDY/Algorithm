'''
https://programmers.co.kr/learn/courses/30/lessons/68645
삼각 달팽이
[풀이]
1. 삼각형의 테두리부터 반시계방향으로 1을 채워넣기
2. 머리, 몸통, 꼬리로 나누어서 합치기, 이 때 인덱스를 점화식으로 생각했음.
'''
def snail(n, s):
    if n == 1:
        return [[s - 1]]
    elif n == 2:
        return [[s - 1], [s, s + 1]]
    elif n == 3:
        return [[s - 1], [s, s + 4], [s + 1, s + 2, s + 3]]

    head = [[s - 1], [s, s + 3 * n - 5]]
    body = [[a, 2 * s + 3 * n - 5 - a] for a in range(s + 1, s + n -2)]
    tail = [[i for i in range(s + n - 2, s + 2 * n - 2)]]

    entity = []
    for i, j in zip(body, snail(n - 3, s + 3 * n - 3)):
        entity += [[i[0]] + j + [i[1]]]
    return head + entity + tail

def solution(n):
    return sum(snail(n, 2), [])
'''
수학처럼이 아니라, 컴퓨터 처럼 풀었어야 했던 것 같다.
삼각형의 각 진행방향에 따라 dx와 dy를 나눠서 구현한 풀이를 보고
본인의 s와 n으로 구성된 점화식으로 구현한 풀이를 보니
너무나도 어렵게 풀었구나 생각이 들음.

def solution(n):
    dx=[0,1,-1];dy=[1,0,-1]
    b=[[0]*i for i in range(1,n+1)]
    x,y=0,0;num=1;d=0
    while num<=(n+1)*n//2:
        b[y][x]=num
        ny=y+dy[d];nx=x+dx[d];num+=1
        if 0<=ny<n and 0<=nx<=ny and b[ny][nx]==0:y,x=ny,nx
        else:d=(d+1)%3;y+=dy[d];x+=dx[d]
    return sum(b,[])
'''