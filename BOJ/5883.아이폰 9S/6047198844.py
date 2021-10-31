import sys

N = int(sys.stdin.readline())

people = list()
for _ in range(N):
    people.append(sys.stdin.readline().rstrip())

res = 0
for removed_person in set(people):
    #person을 제거하자. -> 무시해보자.
    prev = None
    count = 0
    for person in people:
        #그냥 무시
        if person == removed_person:
            continue
        #이전과 같으면 count 올린다.
        if not prev or prev == person:
            count += 1
        else:
            res = max(res, count)
            count = 1
        prev = person
    res = max(res, count)

print(res)