def solution(arr, divisor):
    answer = sorted([number for number in arr if number % divisor == 0])
    return answer if answer else [-1]