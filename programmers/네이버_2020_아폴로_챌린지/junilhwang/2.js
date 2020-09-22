function solution(h, w, n, board) {
  const boardOf = board.map(str => [ ...str ].map(Number));

  let cnt = 0;

  for (let j = 0; j < h; j++) {
    let next = 0;
    for (let i = 0; i < w; i++) {
      if (boardOf[j][i] === 0) {
        if (next === n) cnt += 1;
        next = 0;
        continue;
      }
      next += 1;
    }
    if (next === n) cnt += 1;
  }

  for (let i = 0; i < w; i++) {
    let next = 0;
    for (let j = 0; j < h; j++) {
      if (boardOf[j][i] === 0) {
        if (next === n) cnt += 1;
        next = 0;
        continue;
      }
      next += 1;
    }
    if (next === n) cnt += 1;
  }

  const memo1 = {}
  const memo2 = {}

  const fn1 = (x, y) => {
    if (memo1[`${x},${y}`]) return;
    let next = 0;
    for (let i = x, j = y; i < w && j < h; i++, j++) {
      memo1[`${i},${j}`] = true;
      if (boardOf[j][i] === 0) {
        if (next === n) cnt += 1;
        next = 0;
        break;
      }
      next += 1;
    }
    if (next === n) cnt += 1;
  }

  const fn2 = (x, y) => {
    if (memo2[`${x},${y}`]) return;
    let next = 0;
    for (let i = x, j = y; i > -1 && j < h; i--, j++) {
      memo2[`${i},${j}`] = true;
      if (boardOf[j][i] === 0) {
        if (next === n) cnt += 1;
        next = 0;
        break;
      }
      next += 1;
    }
    if (next === n) cnt += 1;
  }

  // 대각선 검사
  for (let i = 0; i < h; i++) {
    let before = 0;
    let next = 0;
    for (let j = 0; j < w; j++) {
      if (boardOf[i][j] === 0) continue;
      fn1(j, i);
      fn2(j, i);
    }
  }
  return cnt;
}

console.log(
  solution(7, 9, 4, ["111100000","000010011","111100011","111110011","111100011","111100010","111100000"]), 10,
  solution(5, 5, 5, ["11111","11111","11111","11111","11111"]), 12,
)
// 1 1 1 1 1
// 1 1 1 1 1
// 1 1 1 1 1
// 1 1 1 1 1
// 1 1 1 1 1