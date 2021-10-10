N = int(input())
sanggen_cards = set(map(int, input().split()))
M = int(input())
for card in map(int, input().split()):
    if card in sanggen_cards:
        print(1, end=' ')
    else:
        print(0, end=' ')