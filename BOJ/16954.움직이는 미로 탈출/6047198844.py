from collections import deque

maze = deque([input() for _ in range(8)])
visited = [[0 for _ in range(8)] for _ in range(8)]
EMPTY, BLOCK = ('.', '#')
dyx = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
EMPTYLINE = '.'*8

def answer():
  global EMPTY, BLOCK
  candidates = [(7, 0)]
  visited[7][0] = 1 
  while(True):
    candidates = 후보구하기(candidates)
    if visited[0][7] == 1: return 1
    if len(candidates) == 0: return 0
    nextMaze()
