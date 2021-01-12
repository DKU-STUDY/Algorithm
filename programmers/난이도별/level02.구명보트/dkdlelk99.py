# 출처 https://programmers.co.kr/learn/courses/30/lessons/42885
# input people : 사람들의 몸무게가 담긴 배열, limit : 구명보트의 무게 제한
# output 구명보트의 최소 갯수
# 보트의 최대 수용 인원은 2명
# 구명보트 무게 제한은 언제나 사람 무게와 같거나 크다. (구출할 수 없는 경우는 없음)

def solution(people, limit):
    answer, start, end = 0, 0, len(people)
    people = sorted(people)
    while start < end:
        end -= 1
        answer += 1
        if people[end] + people[start] <= limit:
            start += 1
    return answer

print(solution([70, 50, 80], 100) == 3, solution([70, 50, 80], 100))
print(solution([70, 50, 50, 80], 100) == 3, solution([70, 50, 50, 80], 100))
print(solution([70, 50, 80, 20, 90], 100) == 4, solution([70, 50, 80, 20, 90], 100))
print(solution([70, 10, 20, 20, 90, 50, 90, 80], 100) == 5, solution([70, 10, 20, 20, 90, 50, 90, 80], 100))
