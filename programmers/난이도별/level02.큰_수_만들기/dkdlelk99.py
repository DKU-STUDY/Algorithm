def solution(number, k):
    i = 0
    while k > 0:
        if number[i] < number[i + 1]:
            number = number[:i] + number[i + 1:]
            k -= 1
            if i ! = 0:
                i -= 1 # i=0을 하면 많이 틀림 왜?
        else:
            i += 1
            if i == len(number)-1:
                return number[:-k]
    return number

print(solution("1924", 2), solution("1924", 2) == "94")
print(solution("1231234", 3), solution("1231234", 3) == "3234")
print(solution("4177252841", 4), solution("4177252841", 4) == "775841")
print(solution("100000", 2) ,solution("100000", 2) == "1000")
