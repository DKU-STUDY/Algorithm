def solution(w,h):
# w와 h의 최대공약수만큼 사각형을 지날때마다 꼭짓점을 중간에 만나게 되는 규칙
    if w > h: # w <= h 상태를 이용
        tmp = h
        h = w
        w = tmp

    for d in range(w,1,-1):
        if w%d == 0 and h%d == 0: # 최대공약수
            # 최대공약수가 1이 아닌 경우
            # 꼭짓점을 만날 때마다 반복되었던 위치가 1칸씩 뒤로 밀려서 만나는 사각형이 감소(d)
            # w + h - d
            return w*h - (w+h-d)
    # 최대공약수가 1인 경우 : 대각선이 사각형의 꼭짓점을 양끝을 제외하고는 지나지 않음
    # 가로 방향에 보면 h개를 지남 + 세로 방향으로 보면 w개를 지남 - 가로와 세로로 갈 때 시작하는 사각형이 같음(1)
    # w + h -1
    return w*h - (w+h-1)

'''
import math
def solution(w,h):
    return w*h -(w+h-math.gcd(w,h)
'''

