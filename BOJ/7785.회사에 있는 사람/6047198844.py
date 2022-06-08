n = int(input())
people = set()
for _ in range(n):
    name, log = input().split()
    if log == 'enter':
        people.add(name)
    elif name in people:
        people.remove(name)
for person in sorted(people)[::-1]:
    print(person)