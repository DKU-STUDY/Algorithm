def solution(num):
    if num % 2 == 1:
        return "Odd"
    else:
        return "Even"

print(solution(66) == "Even")
print(solution(11) == "Odd")
