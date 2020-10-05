from sys import stdin

N, M = map(int, stdin.readline().split())

non_heard_list = [stdin.readline().strip('\n') for _ in range(N)]
non_seen_dict = {}
return_list = []
for i in range(M):
    name = stdin.readline().strip('\n')
    non_seen_dict[name] = True

#print(f'non_seen: {non_seen_dict}   non_heard: {non_heard_list}')
for name in non_heard_list:
    temp = non_seen_dict.get(name)
    if temp:
        return_list.append(name)
return_list.sort()
print(len(return_list))
for name in return_list:
    print(name)
