from collections import deque

N = int(input())
cards = deque(range(1, N+1))
while len(cards) > 1:
    cards.popleft()
    cards.rotate(-1)
print(cards.pop())