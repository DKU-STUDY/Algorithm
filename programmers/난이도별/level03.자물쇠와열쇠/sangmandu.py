'''
https://programmers.co.kr/learn/courses/30/lessons/60059
자물쇠와 열쇠 : 카카오 블라인드 채용 2020 문제
1) 키가 락이 완전히 겹치지 않아도 되는 부분까지 락으로 생각하고 락 확장. 이 떄 값은 -2
2) 키와 락이 겹칠 때는 1 + 0 이나 0 + 1로 1 그리고 -2 + 1 이나 -2 + 0까지 고려
3) 모든 락 홈에 맞아야 하므로 락 홈의 개수를 미리 구하고 이후에 모양이 맞더라도 모든 홈을 맞추었는지 조사
'''

def solution(key, lock):
    numLocks = sum([i.count(0) for i in lock])
    keysize = len(key)
    exlock = [[-2] * (keysize - 1) + i + [-2] * (keysize - 1) for i in lock]
    pad = [[-2] * len(exlock[0]) for i in range(keysize - 1)]
    exlock = pad + exlock + pad
    locksize = len(exlock)

    for rotate in range(4):
        key = [list(e) for e in zip(*key[::-1])]
        for i in range(locksize - keysize + 1):
            for j in range(locksize - keysize + 1):
                answer = num = 0
                for k in range(keysize):
                    for l in range(keysize):
                        if key[k][l] + exlock[i + k][j + l] == 1 or key[k][l] + exlock[i + k][j + l] < 0:
                            answer += 1
                            if exlock[i + k][j + l] == 0:
                                num += 1
                if answer == keysize ** 2 and num == numLocks:
                    return True
    return False

'''
아 굳이 -2 아니고 0으로 해도 되는구나..
'''