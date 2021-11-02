from itertools import product


def solution(word):
    dict_words = []
    candidate = ['A', 'E', 'I', 'O', 'U']
    for pick_n in range(1, 5 + 1):
        for dict_word in product(candidate, repeat=pick_n):
            dict_words.append(''.join(dict_word))

    dict_words.sort()
    return dict_words.index(word) + 1