import json

def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')

with open('./test.json') as testFile:
    for v in json.load(testFile):
        print(solution(*v['input']) == v['output'])