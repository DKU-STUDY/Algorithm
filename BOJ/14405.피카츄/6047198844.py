# 문제
# 피카츄는 "pi", "ka", "chu"를 발음할 수 있다. 따라서, 피카츄는 이 세 음절을 합친 단어만 발음할 수 있다. 예를 들면, "pikapi"와 "pikachu"가 있다.
#
# 문자열 S가 주어졌을 때, 피카츄가 발음할 수 있는 문자열인지 아닌지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 문자열 S가 주어진다. 문자열은 알파벳 소문자로 이루어진 문자열이며, 길이는 5000을 넘지 않는다.
#
# 출력
# 문자열 S가 "pi", "ka", "chu"를 이어 붙여서 만들 수 있으면 "YES"를 아니면 "NO"를 출력한다.

S = input()
idx = 0
while idx < len(S):
    if S[idx] == 'p' and idx + 1 < len(S) and S[idx+1] == 'i':
        idx += 2
    elif S[idx] == 'k' and idx + 1 < len(S) and S[idx+1] == 'a':
        idx += 2
    elif S[idx] == 'c' and idx + 2 < len(S) and S[idx+1] == 'h' and S[idx+2] == 'u':
        idx += 3
    else:
        print('NO')
        exit()
else:
    print('YES')