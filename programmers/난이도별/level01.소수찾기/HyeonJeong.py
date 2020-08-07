#방법1
def solution(n):
    answer = []
    if n >= 2:
            answer.append(2)
    for x in range(2, n + 1):
        for y in range(2, x):
            if x % y == 0:
                break
            elif y == x - 1:
                answer.append(x)
    return len(answer)

#방법2 : 짝수는 2만 소수에 속해서 2를 제외한 나머지 수는 확인을 생략함.
def solution(n):
    answer = [2]
    for x in range(3, n + 1, 2):
        if x == 3:
            answer.append(3)
        else:
            for y in range(3, x, 2):
                if x % y == 0:
                    break
                elif y == x - 2:
                    answer.append(x)
    return len(answer)

#방법3 : 방법2 + 바로 결과가 나올 수 있는 것은 먼저 return 처리
def solution(n):
    if n <= 4:
        if n == 2:
            return 1
        else:
            return 2
    answer = [2, 3]
    for x in range(5, n + 1, 2):
        for y in range(3, x, 2):
            if x % y == 0:
                break
            elif y == x - 2:
                answer.append(x)
    return len(answer)

print(
    solution(10) == 4,
    solution(5) == 3
      )