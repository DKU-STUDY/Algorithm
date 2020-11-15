'''
https://programmers.co.kr/learn/courses/30/lessons/12915

처음에 sorted와 lambda로 string[n:]을 기준으로 정렬하는 코드를 썼다가
질문하기에서 25점 맞은 분 팁을 읽고 n 인덱스가 같은 문자열끼리는 전체 문자의 순서로 정렬하는 것을 깨달음

1) 소문자 알파벳(범위 제시됨) 크기의 alphabet 배열 생성
1) n 인덱스가 같은 문자들끼리 append
3) alphabet 안의 각 배열 정렬
4) 모든 배열 합친 ans 반환

string[n:] => (string[n], string) 이런식으로 했으면 바로 정렬 가능
튜플 정렬: "첫번쨰 원소 같으면 두번째 원소로 정렬 된다."

def solution(strings, n):
    return sorted(strings, key=lambda str: (str[n], str))
'''

strings = ["abce", "abcd", "cdx"]
n = 2

def solution(strings, n):
    ans = []
    alphabet = [[] for _ in range(26)]
    for string in strings:
        alphabet[ord(string[n])-ord("a")].append(string)
    x = list(map(lambda x : x.sort(), alphabet))
    for x in alphabet:
        ans += x
    return ans

print(solution(strings, n))
