import re

def solution(dartResult):
    result = []
    numbers = re.findall('[0-9]+',dartResult)
    commands = re.findall('[SDT][*#]?',dartResult)
    powers = ' SDT'
    
    for number, command in zip(numbers,commands):
        result.append(pow(int(number),powers.index(command[0])))
        #옵션이 존재하는 경우
        if len(command) == 2:
            if command[1] == '#':
                result[-1] = -result[-1]
            else:
                result[-1] = result[-1]*2
                if len(result) > 1:
                    result[-2] = result[-2]*2
    return sum(result)