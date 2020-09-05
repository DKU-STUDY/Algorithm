def solution(n):
    def bin(n):
        answer = []
        while True:
            answer.append(n%2)
            n=n//2
            if n==1: answer.append(1); break;
        return sum(answer)

    count= bin(n)
    for i in range(n+1, 1000001):
        if bin(i)==count: return i

print(solution(78))
