def solution(phone_number):
    N = len(phone_number)
    return '*' * (N-4) + phone_number[-4:]