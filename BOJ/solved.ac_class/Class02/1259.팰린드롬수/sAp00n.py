from sys import stdin


def word_input():
    temp = stdin.readline().rstrip('\n')
    word_list = []
    if temp != '0':
        word_list.append(temp)
        temp = stdin.readline().rstrip('\n')
        while temp != '0':
            word_list.append(temp)
            temp = stdin.readline().rstrip('\n')
    return word_list


def is_palindrome(input_str):
    idx = 0
    while idx < len(input_str) / 2:
        left_str = input_str[idx]
        right_str = input_str[-(idx + 1)]
        if left_str == right_str:
            idx += 1
        else:
            return False
    return True


word_list = word_input()
for word in word_list:
    if is_palindrome(word):
        print('yes')
    else:
        print('no')
