function solution (board) {
  const len = board.length;
  const isDia = (depth, i, j) => {
    const startI = i - depth;
    const endI = i + depth;
    const startJ = j - depth;
    const endJ = j + depth;
    if (startI < 0 || endI >= len) return false;
    if (startJ < 0 || endJ >= len) return false;

    if (board[startI][j] !== 1 || board[endI][j] !== 1) return false;
    if (board[i][startJ] !== 1 || board[i][endJ] !== 1) return false;

    return true;

  }
  let cnt = 0;
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      const v = board[i][j];
      let depth = 1;
      if (v === 0) {
        cnt += isDia(1, i, j)
      }
    }
  }
  return cnt;
};

console.log(
  solution([[0,0,1,0,0],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[0,0,1,0,0]]) === 4,
  solution([[0,0,0,1,0,0,0],[0,0,1,0,1,1,0],[0,1,0,1,0,0,1],[1,0,0,0,1,1,0],[0,1,0,1,0,1,0],[1,0,1,0,0,0,1],[0,1,0,1,0,1,0]]) === 3,
)