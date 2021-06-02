import collections

prime = set(range(2, 9999 + 1))
#에라스토테네스의 체
def sieve():
    #2부터 9999까지의 소수를 prime에 저장한다.
    for num in range(2, 9999 + 1):
        #num이 소수이면
        if num in prime:
            for not_prime_num in range(num*2, 9999 + 1, num):
                prime.discard(not_prime_num)

#4자리수인지 판단하는 함수
def is_four_digits(num):
    return int(num) // 1000

#소수인지 판단하는 함수
def is_prime(num):
    return int(num) in prime


def bfs(base, target):
    convert_cnt = 0
    if base == target:
        return convert_cnt

    Q = collections.deque()
    visited = set()
    Q.append(base)
    visited.add(base)

    while Q:
        convert_cnt += 1
        for _ in range(len(Q)):
            num = Q.popleft()
            for index in range(0,4):
                for nn in range(0,9+1):
                    nnum = num[:index] + str(nn) + num[index+1:]
                    if nnum == target:
                        return convert_cnt
                    if is_prime(nnum) and is_four_digits(nnum) and nnum not in visited:
                        Q.append(nnum)
                        visited.add(nnum)
    print('Impossible')


T = int(input())
sieve()
for _ in range(T):
    base, target = input().split()
    print(bfs(base, target))
