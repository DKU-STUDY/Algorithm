'''
https://www.acmicpc.net/problem/1141
접두사
[풀이]
1. A단어가 B단어의 접두사가 되려면 두 단어는 사전순으로 가까이에 위치해있다.
2. 사전순으로 정렬된(오름차순) 세 단어 A, B, C가 있다고 하자
=> A가 B의 접두사가 아니고 B는 C의 접두사가 아닐 때 A는 C의 접두사가 될 수 없다.
=> 사전순으로 정렬된다는 가정에 위배되기 때문
=> 따라서 사전 순으로 전에 위치한 단어가 후에 위치한 단어의 접두사가 아니라면 이후에 어떠한 단어의 접두사도 아니다.
3. startswith를 사용하여 조사한다.
=> 또는 find == 0 으로도 조사할 수 있다.
'''
n = int(input())
words = sorted([input() for _ in range(n)])
print(n-[words[i+1].startswith(words[i]) for i in range(n-1)].count(True))