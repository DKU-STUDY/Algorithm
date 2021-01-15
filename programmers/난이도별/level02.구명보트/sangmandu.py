'''
https://programmers.co.kr/learn/courses/30/lessons/42885#
구명보트
case가 50000 이라 반복문 중첩은 어지간 하면 시간초과.
따라서 반복문 내에 remove, del, pop은 거의 사용 불가
indexing 비교만으로 count
핵심은 가장 무게가 많은 사람을 가장 무게가 적은 사람이 커버하지 못하면 어떤 사람도 커버하지 못한다는 것.
따라서 가장 무게가 많은 사람 + 가장 무게가 적은 사람이 limit을 초과하면 무게가 많은 사람만 보트에 태운다.
'''

def solution(people, limit):
    people.sort(reverse=True)
    cnt = 0
    i, j = 0, len(people)-1
    while i <= j:
        if people[i] + people[j] <= limit:
            j -= 1
        i += 1
        cnt += 1
    return cnt

'''
'''