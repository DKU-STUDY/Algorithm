N = int(input())
sanggen_cards = set(map(int, input().split()))
M = int(input())
for card in map(int, input().split()):
    print(int(card in sanggen_cards), end=' ')