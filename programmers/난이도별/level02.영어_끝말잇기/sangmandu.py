'''
https://programmers.co.kr/learn/courses/30/lessons/12981
영어 끝말잇기
중복 판별 및 끝-첫 글자 매칭
'''

def solution(n, words):
    prior = []
    end = words[0][0]
    for idx, word in enumerate(words):
        if word in prior or end != word[0]:
            return [(idx)%n+1,(idx)//n+1]
        prior.append(word)
        end = word[-1]
    return [0,0]


'''
prior로 메모리를 추가하는 것보다
words[:idx] 로 이전까지의 리스트를 참조하는 것이 좋았을 듯
def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    else:
        return [0, 0]
            
'''