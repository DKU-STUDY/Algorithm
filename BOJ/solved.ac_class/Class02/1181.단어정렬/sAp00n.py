from sys import stdin

N = int(stdin.readline())
words_list = []

for _ in range(N):
    words_list.append(stdin.readline().rstrip('\n'))

word_dict = {}
max_len = 0

for word in words_list:
    word_len = len(word)

    if word_len not in word_dict:
        word_dict[word_len] = []

    max_len = max(max_len, word_len)

    if word not in word_dict[word_len]:
        word_dict[word_len] += [word]

for len in range(1, max_len+1):

    if len in word_dict:
        temp = word_dict[len]
        temp.sort()

        for word in temp:
            print(word)
