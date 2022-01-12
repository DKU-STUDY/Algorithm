# 문제
# 암호화하려는 문장 (평문)의 단어와 암호화 키를 숫자로 바꾼 다음, 평문의 단어에 암호화 키에 해당하는 숫자를 빼서 암호화하는 방식을 생각해 보자.
# 제시된 평문의 첫 번째 문자인 ‘n’은 해당 암호화 키 ‘l’의 알파벳 순서가 12 이므로 알파벳상의 순서에서 ‘n’보다 12앞의 문자인 ‘b’로 변형된다.
# 평문의 문자가 공백 문자인 경우는 그 공백 문자를 그대로 출력한다.
#
# 이와 같은 암호화를 행하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 평문이, 둘째 줄에 암호화 키가 주어진다.
#
# 평문은 알파벳 소문자와 공백문자(space)로만 구성되며, 암호화 키는 알파벳 소문자만으로 구성된다. 평문의 길이는 공백까지 포함해서 30000자 이하이다.
#
# 출력
# 첫 번째 줄에 암호문을 출력한다.

plaintext = input()
ciphertext = input()
for idx, plain in enumerate(plaintext):
    if plain.isalpha():
        order = ord(ciphertext[idx % len(ciphertext)]) - ord('a') + 1# 순서
        print(chr(ord('a') + (ord(plain) - ord('a') - order) % 26), end='')
    else:
        print(' ', end='')