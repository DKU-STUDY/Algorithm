def solution(s):
    small = []
    capital = []
    for x in s:
        capital.append(x) if 65 <= ord(x) <= 90 else small.append(x)
    return "".join(sorted(small + capital, reverse = True))

print(solution("Zbcdefg") == "gfedcbZ")