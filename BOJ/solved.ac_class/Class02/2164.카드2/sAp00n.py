from sys import stdin


def solution():
    N = int(stdin.readline().strip('\n'))
    deck = [card for card in range(1, N + 1)] + [None for _ in range(N + 1)]

    fst_card = 0
    end_card = N
    temp = deck[fst_card]
    while deck[fst_card + 1] is not None:
        deck[fst_card] = None
        temp = deck[fst_card + 1]
        deck[fst_card + 1] = None
        deck[end_card] = temp
        fst_card += 2
        end_card += 1
    print(temp)


solution()
