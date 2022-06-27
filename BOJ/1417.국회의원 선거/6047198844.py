import sys

N = int(sys.stdin.readline())

people = [int(sys.stdin.readline()) for _ in range(N)]

res = 0

while people[0] <= max(people[1:len(people)]):
    max_person = max(people[1:len(people)])
    idx = people[1:len(people)].index(max_person) + 1
    people[idx] -= 1
    people[0] += 1
    res += 1

print(res)