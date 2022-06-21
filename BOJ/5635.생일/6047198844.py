import datetime as dt
import heapq
from collections import defaultdict

N = int(input())
arr = list()
for _ in range(N):
    name, *date = input().split()
    strptime = dt.datetime.strptime(' '.join(date), "%d %m %Y")
    heapq.heappush(arr, (strptime, name))
print(heapq.nlargest(1, arr)[0][1])
print(heapq.nsmallest(1, arr)[0][1])

'''
5
Mickey 1 10 1991
Alice 30 12 1990
Tom 15 8 1993
Jerry 18 9 1990
Garfield 20 9 1990
'''