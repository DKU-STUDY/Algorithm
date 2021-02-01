# 토스 체


def solution(n: int):
    # check -1 이면 검사 안한것
    check = [-1 for i in range(0, n + 1)]
    pc = 0  # prime count
    pn = []  # prime array

    # 2,3,....n
    for i in range(2, n + 1):
        if check[i] == -1:
            pc += 1
            pn.append(i)
            # 5*5 =25 , 30, 35 ,... n
            for j in range(i * i, n + 1, i):
                check[j] = 1
    # print(f"Primse is {pn}")
    return pc