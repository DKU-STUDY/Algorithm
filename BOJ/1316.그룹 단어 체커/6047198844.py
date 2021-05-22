n = int(input())
res = n
for _ in range(n):
    check = [False]*26
    s = [ord(i)-ord('a') for i in input()]

    for idx in range(len(s)):
        cur, lst = s[idx] , s[idx-1]
        if idx == 0 or (cur!=lst and not check[cur]) or (cur==lst and check[cur]):
            check[cur] = True
            continue
        else:
            res+=-1
            break
print(res)

# 그룹 단어 2가지 경우
# 현재 알파벳이 이전꺼와 같지 않으면서 방문이 안된경우.
# 현재 알파벳이 이전꺼와 같으면서 방문이 된경우.