from sys import stdin

N = int(stdin.readline())

age_list = []
member_dict = {}

for _ in range(N):
    member_age, member_name = list(stdin.readline().split())
    member_age = int(member_age)
    if member_age not in age_list:
        age_list.append(member_age)
        member_dict[member_age] = []
    member_dict[member_age] += [str(member_age)+' '+member_name]

age_list.sort()
for age in age_list:
    for member in member_dict[age]:
        print(member)
