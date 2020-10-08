# 아래의 코드는 왜 실패 되나요?
'''
def solution(strings, n):
    answer = []
    while 1:
        if len(strings) == 1:
            answer += strings
            break
        c = strings[0]
        for s in strings[1:]:
            if c[n:] > s[n:]:
                c = s
        answer += [c]
        strings.remove(c)
    return answer
'''

def solution(strings, n):
    return sorted(sorted(strings) , key=lambda s: s[n]) # 내부 sorted는 인덱스 n의 값이 같은 것은 사전 순 배열이 필요

print(
    solution(["sun", "bed", "car"],1) == ['car', 'bed', 'sun'],
    solution(["abce", "abcd", "cdx"], 2) == ["abcd", "abce", "cdx"]
)

