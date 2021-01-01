'''
https://programmers.co.kr/learn/courses/30/lessons/12904
가장 긴 팰린드롬
매 단어마다 앞뒤 비교
'''

def solution(s):
    ret = 1
    for idx in range(len(s)):
        i = j = 1
        while idx-i >= 0 and idx+i < len(s) and s[idx-i] == s[idx+i]:
            i += 1
        if idx + 1 < len(s) and s[idx] == s[idx+1]:
            while idx-j >= 0 and idx+1+j < len(s) and s[idx-j] == s[idx+1+j]:
                j += 1
        if i > 1: i = i*2 - 1
        if j > 1: j = j*2
        ret = max(ret, i, j)
    return ret

'''
시간 복잡도는 N^2 정도인 것 같다.
물론 best case는 N
나름 괜찮다 하고 풀었는데 다른 사람들과 비슷해서 아쉽.
시간 효율이 떨어지지만 key point는 s에서 대칭이 아니면 s[1:]과 s[:-1]에서 대칭을 찾아야 한다는 점.
이렇게 짠 코드를 보고 놀랐다.
'''