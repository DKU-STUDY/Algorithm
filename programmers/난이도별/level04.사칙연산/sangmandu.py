'''
https://programmers.co.kr/learn/courses/30/lessons/1843
사칙연산
1. 해당 식을 거꾸로 접근한다
2. -를 만날 때 마다, gain과 loss를 계산한다.
이 때, gain과 loss가 의미하는 바가 중요한데,
gain은 모든 음수들을 양수로 만들었을 때의 이득을 의미하고
loss는 음수와 음수 사이에 있는 양수들을 모두 음수로 만들었을 떄의 손해를 의미한다.
gain은 모든 음수들을 대상으로 하는데에 비해 loss가 음수와 음수 사이에 있는 양수들이 범위인 이유는
일단, 모든 양수들을 대상으로 하는 것은 최대값을 구하는 방향이 아니며,
음수와 음수 사이에 있지 않은 양수들은 굳이 음수화 될 필요가 없기 때문
3. 이 때 gain - loss 가 가장 큰 경우를 구한다.
이 때가 부호를 바꿨을 때 가장 큰 기댓값
이 때 기본 + 2 * 기댓값
'''

def solution(arr):
    signs = [1]
    values = []
    for x in arr:
        if x == "+":
            signs.append(1)
        elif x == "-":
            signs.append(-1)
        else:
            values.append(int(x))
    base = int(eval(''.join(arr)))
    n = len(values)
    loss = [0] * n
    gain = [0] * n
    l, g = 0, 0
    for i in range(n - 1, -1, -1):
        if signs[i] == 1:
            l += values[i]
        else:
            loss[i] = l
            l = 0
            gain[i] = g
            g += values[i]
    benefit = max([g - l for (g, l) in zip(gain, loss)])
    return base + 2 * benefit

'''
정확성은 문제가 없었지만 효율성을 통과하기가 굉장히 어려웠던 문제
level4부터는 확실히 다른 것 같다. 근 한달간 쩔쩔 맸음.
지금까지 본 문제중에 제일 어려웠다.
'''