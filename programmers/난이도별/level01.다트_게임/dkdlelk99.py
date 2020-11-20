def solution(dartResult):
    score = []
    for i in range(len(dartResult)):
        if dartResult[i] == "S":
            if dartResult[i-2:i] == '10':
                score.append(10)    
            score.append(int(dartResult[i-1]))
        elif dartResult[i] == "D":
            if dartResult[i-2:i] == '10':
                score.append(100)
            score.append(int(dartResult[i-1]) ** 2)
        elif dartResult[i] == "T":
            if dartResult[i-2:i] == '10':
                score.append(1000)
            score.append(int(dartResult[i-1]) ** 3)
        elif dartResult[i] == "*":
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2
        elif dartResult[i] == "#":
            score[-1] *= -1
    return sum(score)


print(solution("1S2D*3T") == 37)
print(solution("1D2S#10S") == 9)
print(solution("1D2S0T") == 3)
print(solution("1S*2T*3S") == 23)
print(solution("1D#2S*3S") == 5)
print(solution("1T2D3D#") == -4)
print(solution("1D2S3T*") == 59)
