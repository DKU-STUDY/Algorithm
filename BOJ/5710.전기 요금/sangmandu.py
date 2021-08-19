'''
https://www.acmicpc.net/problem/5710
전기 요금
[풀이]
1. watt를 fee로 바꾸는 함수 생성
2. fee를 watt로 바꾸는 함수 생성
3. 총 사용량 A를 금액으로 변경
4. 이진 탐색으로 만족하는 값 찾기
'''
def watt_fee(watt):
    return sum([a*b for a, b in zip([watt-l for l in [0, 100, 10000, 1000000]], [2, 1, 2, 2]) if a > 0])

def fee_watt(fee):
    ret = ([(b, b*c) for a, (b, c) in zip([fee-l for l in [0, 200, 29900, 4979900]], [(2, 0), (1, 100), (2, 10000), (2, 1000000)]) if a > 0])
    a, b = list(zip(*ret))
    return (fee+sum(b)) // sum(a)

while True:
    A, B = map(int, input().split())
    if A == B == 0:
        break
    total = fee_watt(A)
    left, right = 0, total
    while True:
        mid = (left + right) // 2
        if watt_fee(total-mid) - watt_fee(mid) > B:
            left = mid + 1
        elif watt_fee(total-mid) - watt_fee(mid) < B:
            right = mid - 1
        else:
            break
    print(watt_fee(mid))
