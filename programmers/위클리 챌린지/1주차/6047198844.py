def solution(price, money, count):
    need = count * (count + 1) // 2 * price - money
    return need if need > 0 else 0