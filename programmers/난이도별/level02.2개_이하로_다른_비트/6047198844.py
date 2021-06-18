def solution(numbers):
    answer = []
    
    for number in numbers:
        #0이 위치하는 자리수.
        zero_digit = 0
        #0을 발견할때까지.
        while number & (1 << zero_digit) != 0:
            zero_digit += 1
        res = number
        #0의 자리수를 1로 변경한다.
        res |= 1 << zero_digit
        #1의 자리수를 0으로 변경한다.
        if zero_digit != 0:
            res ^= 1 << (zero_digit - 1)
        
        answer.append(res)
        
        
    return answer