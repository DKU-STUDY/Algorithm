# N명의 사람과, 각각의 사람이 지불할 용의가 있는 최대 금액과 배송비가 주어졌을 때, 세준이의 이익을 최대로 하는 가격을 출력하는 프로그램을 작성하시오.
# 세준이가 안 팔수도 있다.
# 1000000 -> brute force

N = int(input())
pays = list()

for _ in range(N):
    pays.append(tuple(map(int, input().split())))
pays.sort()

res = 0
benefit = 0

for real_price, _ in pays:
    acc = 0
    for pay in pays:
        affordable_price, delivery_price = pay
        # 고객이 사는 경우 / 세준이가 파는 경우
        if affordable_price >= real_price and real_price - delivery_price > 0:
            acc += real_price - delivery_price
    if acc > benefit:
        benefit = acc
        res = real_price

print(res)
