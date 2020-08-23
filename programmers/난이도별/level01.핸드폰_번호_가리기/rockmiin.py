def solution(phone_number):
    return ("*"*(len(phone_number)-4)+phone_number[len(phone_number)-4:])

solution("01033334444")