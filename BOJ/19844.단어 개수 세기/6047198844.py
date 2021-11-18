# qu'est-ce qu'il mange aujourd'hui
# 먼저 띄어쓰기와 하이픈을 기준으로 “단어”로 분리해 준다: qu'est / ce / qu'il / mange / aujourd'hui.
# 첫 번째 “단어”인 qu'est는 qu'로 시작하고 모음인 e로 이어지기 때문에 que와 est가 만나서 줄어든 것이다. 따라서 이 단어를 분리해 준다: que / est / ce / qu'il / mange / aujourd'hui.
# 세 번째 “단어” 역시 마찬가지로 분리해 준다: que / est / ce / que / il / mange / aujourd'hui.
# 마지막 “단어”는 어포스트로피가 있고 모음으로 취급되는 h로 이어지지만 앞 단어가 줄어들어 생긴 어포스트로피가 아니므로, 분리하지 않고 한 단어로 둔다.
# 기본적으로는 띄어쓰기나 -(하이픈) 단위로 단어를 구분한다.
# 앞 단어가 ce, je, ne, me, te, se, le, la, de, que 혹은 si이고 뒤 단어가 모음(a, e, i, o, u, h)으로 시작하는 경우, 앞 단어의 마지막 모음이 사라지고, 대신 '(어포스트로피)가 붙으면서 이어진다.
# 프랑스어에서 h는 언제나 묵음이므로, 이 문제에서는 일반적으로 알려진 모음 a, e, i, o, u는 물론이고 h도 모음으로 취급함에 유의하라.
# c', j', n', m', t', s', l', l', d', qu'

# step1
import re

sentence = ' '.join(' '.join(input().split()).split('-'))

# step2

cnt = 0
for word in sentence.split():
    cnt += 1

    front_words = ["c'", "j'", "n'", "m'", "t'", "s'", "l'", "d'", "qu'"]
    back_word = "[aeiouh]+"

    for front_word in front_words:
        p = re.compile(front_word + back_word)
        if p.match(word):
            cnt += 1
print(cnt)