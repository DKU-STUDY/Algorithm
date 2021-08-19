'''
https://www.acmicpc.net/problem/9081
단어 맞추기
[풀이]
1. 각 단어가 구성할 수 있는 경우의 수를 구하기 위해 permutations import
2. 이 때 단어의 알파벳이 중복될수도 있으므로 set을 적용해준다
3. 입력받은 단어 뒤의 단어를 알기위해 정렬을 한다
=> 문자열의 순서는 문자열을 숫자로 바꾸더라도 동일하다
4. idx를 찾는다. 마지막 원소라면 그대로 유지. 이후 반환
'''
n = int(input())
for _ in range(n):
    word = list(input())
    for idx in range(len(word)-1, 0, -1):
        if word[idx] > word[idx-1]:
            a, b = min([(w, jdx) for jdx, w in enumerate(word[idx:]) if w > word[idx - 1]])
            print(''.join(word[:idx-1]+[a]+sorted(word[idx:idx+b]+word[idx+b+1:]+[word[idx-1]])))
            break
    else:
        print(''.join(word))