#코드1
'''
def solution(n, words):
    answer = []
    list = []
    for m in range(len(words)):
        if len(words[m]) == 1:
            answer += [m % n + 1 if m % n + 1 <= n else 1, (m+1) // n if (m+1) % n == 0 else (m+1) // n + 1]
            return answer
    for j in range(1, len(words)):
        list = words[0:j]
        if words[j] in list:
            answer += [j % n + 1 if j % n + 1 <= n else 1, (j+1) // n if (j+1) % n == 0 else (j+1) // n + 1]
            return answer
    for i in range(len(words) - 1):
        if words[i][-1] != words [i+1][0]:
            answer += [(i+1) % n + 1 if (i+1) % n + 1 <= n else 1, (i+2) // n if (i+2) % n == 0 else (i+2) // n + 1]
            return answer
    return [0, 0]
'''

#코드2(간단한)
def solution(n, words):
    for i in range(len(words)):
        if len(words[i]) == 1:
            break
        list = words[0:i]
        if i != 0 and words[i] in list:
            break
        if i != len(words) - 1 and words[i][-1] != words [i+1][0]:
            i += 1
            break
        if i == len(words) - 1:
            return [0, 0]
    return [i % n + 1 if i % n + 1 <= n else 1, (i+1) // n if (i+1) % n == 0 else (i+1) // n + 1]

print(
    solution(3,['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'])==[3,3],
    solution(5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive'])==[0,0],
    solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw'])==[1,3]
)
