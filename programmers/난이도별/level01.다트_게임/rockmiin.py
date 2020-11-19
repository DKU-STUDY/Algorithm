def solution(dartResult):
    result = []

    for i, j in enumerate(dartResult):
        if j == "S":
            if dartResult[i - 2: i] == "10":
                result.append(10)
            else:
                result.append(int(dartResult[i - 1]))
        elif j == "D":
            if dartResult[i - 2: i] == "10":
                result.append(10 ** 2)
            else:
                result.append(int(dartResult[i - 1]) ** 2)
        elif j == "T":
            if dartResult[i - 2: i] == "10":
                result.append(10 ** 3)
            else:
                result.append(int(dartResult[i - 1]) ** 3)
        elif j == "*":
            if len(result) < 2:
                result[-1] *= 2
            elif len(result) >= 2:
                result[-1] *= 2
                result[-2] *= 2
        elif j == "#":
            result[-1] *= -1
    return sum(result)

print(
    solution("1S*2D#3T"),
    solution("1S*2D#3T")==25
)

