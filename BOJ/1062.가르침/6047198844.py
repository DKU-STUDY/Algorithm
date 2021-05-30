import re

def count_bit(n):
    return n % 2 + count_bit(n // 2) if n >= 2 else n

N, K = map(int, input().split())
words = [set(re.findall(r'[^acnit]',input())) for _ in range(N)]
union_words = set()
for word in words:
    union_words |= word

if K < 5:
    print(0)
    exit()

K = K - 5
word_n = len(union_words)
union_words = list(union_words)

#K는 최대로 배울수있는 단어수이다. 만약에 배워야하는 단어의수가 K보다 같거나 작으면 모든 단어를 배울수있다는뜻이다.
if K >= word_n:
    print(len(words))
    exit()

#최대로 배울수있는 단어의 수만큼 배운다.
res = 0
for i in range(1 << word_n):
    if count_bit(i) == K:
        choosen_alpha = set()
        for j in range(word_n):
            if i & 1 << j:
                choosen_alpha.add(union_words[j])
        cnt = 0
        for word in words:
            if word == word & choosen_alpha:
                cnt += 1
        res = max(res, cnt)

print(res)