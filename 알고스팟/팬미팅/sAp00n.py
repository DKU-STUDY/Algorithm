from sys import stdin


def simple_mult(list_of_fan, list_of_members):
    computing_result = [0] * (len(list_of_fan) + len(list_of_members) - 1)
    for member_idx in range(len(list_of_members)):
        for fan_idx in range(len(list_of_fan)):
            computing_result[member_idx + fan_idx] += list_of_members[member_idx] * list_of_fan[fan_idx]
            # print(f'compute: {computing_result}')
    computing_result = computing_result[::-1]
    return computing_result


def adder(a, b):
    if len(b) > len(a):
        a, b = b, a

    result = [a[i] + b[i] if i < len(b) else a[i] for i in range(len(a))]
    return result


def kara(list_of_fan, list_of_members):
    len_of_list = len(list_of_fan)
    if len_of_list < 50:
        return simple_mult(list_of_fan, list_of_members)
    fan_list01, fan_list02 = list_of_fan[:len_of_list // 2], list_of_fan[len_of_list // 2:]
    mem_list01, mem_list02 = list_of_members[:len_of_list // 2], list_of_members[len_of_list // 2:]
    z2 = kara(fan_list02, mem_list02)
    z0 = kara(fan_list01, mem_list01)
    z1 = kara(adder(fan_list01, fan_list02), adder(mem_list01, mem_list02))
    result = adder(adder(z2 + [0] * (len_of_list // 2), z1 + [0] * (len_of_list // 4)), z0)
    return result


def sol():
    list_of_members = [1 if member == 'M' else 0 for member in stdin.readline().strip('\n')]
    list_of_members = list_of_members[::-1]
    len_of_mem = len(list_of_members)
    list_of_fan = [1 if fan == 'M' else 0 for fan in stdin.readline().strip('\n')]
    len_of_fan = len(list_of_fan)
    diff = len(list_of_fan) - len(list_of_members)
    list_of_members = [0] * diff + list_of_members
    result = kara(list_of_fan, list_of_members)
    result = result[len_of_mem - 1:len_of_fan]
    counter = 0
    for i in result:
        if i == 0:
            counter += 1
    return counter


C = int(stdin.readline())
for _ in range(C):
    print(sol())
