import json

def solution(s) :
    return ''.join(sorted(list(s), reverse=True))

with open('./test.json') as testFile:
    for v in json.load(testFile):
        print(solution(*v['input']) == v['output'])