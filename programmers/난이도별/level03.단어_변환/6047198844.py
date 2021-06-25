import collections

def is_valid(step_word, word):
    cnt = 0
    for s_char, char in zip(step_word, word):
        if s_char != char:
            cnt += 1
            if cnt > 1:
                return False
    return True
    

def solution(begin, target, words):
    answer = 0
    
    visited = set()
    Q = collections.deque([begin])
    
    while Q:
        answer += 1
        for _ in range(len(Q)):
            step_word = Q.popleft()
            for word in words:
                if word not in visited and is_valid(step_word, word):
                    if word == target:
                        return answer                    
                    Q.append(word)
                    visited.add(word)

    return 0