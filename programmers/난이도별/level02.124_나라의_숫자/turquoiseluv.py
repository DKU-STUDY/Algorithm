'''
https://programmers.co.kr/learn/courses/30/lessons/12899

124로만 구성된 나라이므로, 1->1 2->2 3->4(예시에 나옴)으로 대체 가능하기 때문에,
123으로 변환을 한 뒤 규칙을 찾는 방법을 선택했다.

여기서 해당 규칙이 0이 없는 3진법이라는 것을 발견하여,
1) 3개의 숫자로 구성하기 위해 3진법으로 숫자를 변환
2) 첫자리를 제외하고 0이 없을 때까지 자리 내림으로 while 루프
3) 해당 수를 [1, 2, 3]에서 [1, 2, 4]로 대체
4) join한 값 반환

수학적으로 접근하여 나머지+몫을 이용한 수식화로 바로 푸는 방법도 있다.

def change124(n):
    num = ['1','2','4']
    answer = ""
    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3
    return answer
'''

n = 4

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n):
    x = convert(n, 3)
    x = list(map(int, x))

    while 0 in x[1:]:
        for i in range(1, len(x)):
            if x[i] == 0:
                x[i-1] -= 1
                x[i] += 3

    if x[0] == 0:
        x = x[1:]

    for i in range(len(x)):
        if x[i] == 3:
            x[i] = '4'

    return ''.join(x)

print(solution(n))
