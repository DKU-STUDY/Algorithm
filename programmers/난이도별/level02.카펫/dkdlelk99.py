# 출처 https://programmers.co.kr/learn/courses/30/lessons/42842
# input brown : 갈색 타일 수, yellow : 노란색 타일 수
# output 격자의 크기 [전체 타일의 가로 길이, 세로 길이]

def solution(brown, yellow):
    answer = []
    for i in range(yellow, 0, -1):
        if yellow % i == 0 and yellow // i <= i:
            answer.append([i, yellow // i])
    for i in range(len(answer)):
        if (answer[i][0] + answer[i][1]) * 2 + 4 == brown:
            return [answer[i][0] + 2, answer[i][1] + 2]

print(solution(12,4) == [4, 4], solution(12,4))
print(solution(14,4) == [6, 3], solution(14,4))
print(solution(18,6) == [8, 3], solution(18,6))
print(solution(14,6) == [5, 4], solution(14,6))
