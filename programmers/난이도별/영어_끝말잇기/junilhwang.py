import math

def solution(n, words):
    length = len(words)
    i = 0
    while i < length :
        if length == 1: break
        temp = words[:i]
        if i != 0 and words[i] in temp:
            break
        if i != length - 1 and words[i][-1] != words[i+1][0]:
            i += 1
            break
        if i == length - 1:
            return [0, 0]
        i += 1

    return [i % n + 1, math.ceil((i+1) / n)]

print(
    solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']) == [3, 3],
    solution(5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']) == [0, 0],
    solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']) == [1, 3]
)