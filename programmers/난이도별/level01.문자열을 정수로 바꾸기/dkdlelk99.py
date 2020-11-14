def solution(s):
    if s.find('.') != -1:
        return int(s)
    else:
        return float(s)


print(solution('12345') == 12345)
print(solution('-321') == -321)
