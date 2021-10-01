from collections import Counter

s = input()
res = ''
even_alpha = ''
for alpha, cnt in sorted(Counter(s).items()):
    res += alpha * (cnt // 2)
    if cnt % 2 != 0:
        if even_alpha == '':
            even_alpha = alpha
        else:
            print("I'm Sorry Hansoo")
            break
else:
    print(res+even_alpha+res[::-1])