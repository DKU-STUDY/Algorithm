tag = ''
word = ''
res = ''

S = input()
for char in S:
    if char == ' ':
        res += word[::-1]
        word = ''
        res += char
    #flag가 false면 word. True면 tag라는 뜻이다.
    if char == '<':
        #쌓여있던 word를 뒤집어서 결과에 붙인다.
        res += word[::-1]
        word = ''
        tag += char
    elif char == '>':
        tag += char
        res += tag
        tag = ''
    elif tag == '':
        word += char
    else:
        tag += char
res += word[::-1]
print(res)