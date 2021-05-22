def is_range_valid(y, x, ny, nx):
    return 0 <= y < ny and 0 <= x < nx

def is_word_valid(board, y, x, word, check):
    if not word:
        return True

    if not self.is_range_valid(y, x, len(board), len(board[0])):
        return False

    if word[0] != board[y][x]:
        return False

    tmp = word[y][x]
    word[y][x] = '#'

    for dy, dx in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
        if self.is_word_valid(board, y + dy, x + dx, word[1:]):
            return True

    word[y][x] = tmp

    return False

def exist(board, word: str) -> bool:
    check = [[False for i in range(len(board[0]))] for j in range(len(board))]

    for y in range(len(board)):
        for x in range(len(board[0])):
            if is_word_valid(board, y, x, word, check):
                return True
    return False

exist([["a"]],"a")