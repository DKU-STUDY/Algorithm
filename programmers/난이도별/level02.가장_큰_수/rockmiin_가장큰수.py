
def solution(num):
    num= list(map(str, num))
    for i in range(len(num)): #숫자가 하나인 수를 범위 1000이상인 수로 만들어 주기 위해 4를 곱함
        if len(num[i])==1:
            num[i]*=4

    num = sorted(num, reverse=True)
    for i in range(len(num)): #다시 원래의 크기로 변환해 줌
        if len(num[i]) == 4:
            num[i] =num[i][0]
    return ''.join(num)

print(
    solution([3, 30, 34, 5, 9]),
)
