def solution(n):
    answer = 0

    three_digit = ""

    while n > 0:
        # n은 10개씩 묶인 상태이다.
        three_digit = str(n % 3) + three_digit
        n //= 3

    for idx, i in enumerate(three_digit):
        answer += int(i) * pow(3, idx)

    return answer