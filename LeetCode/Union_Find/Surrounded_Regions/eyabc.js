/**
 * @param board
 * 핵심
 * O 로 이어진 인덱스들의 동서남북 중 하나가 범위를 벗어나면 X 에 갇혀있지 않다.
 */

  //  동  북  서  남
const dx = [0, -1, 0, 1];
const dy = [1, 0, -1, 0];

const makeTable = (H, W) => {
  const table = new Array(H);
  for (let i = 0 ; i < H ; i++) {
    table[i] = new Array(W).fill(-0);
  }
  return table;
};

const solve = function(board) {
  // 배열의 열, 1차원 행렬일 때에는 board 를 그대로 리턴한다.
  if (!board[0]) return board;

  // 배열의 높이와 너비을 저장한다.
  const [H, W] = [board.length, board[0].length];

  // 이미 방문한 인덱스를 저장하기 위한 테이블을 만든다. -0 (방문전) 1 (방문함)
  const table = makeTable(H, W);

  // 현재 인덱스의 동서남북을 검사하는 함수
  const ENSW = (x, y, ref) => {
    // X 이거나 이미 방문한 인덱스는 동서남북을 검사하지 않는다.
    if (board[x][y] === 'X' || table[x][y] === 1) return;

    // 방문처리 한다.
    table[x][y] = 1;

    // 현재 인덱스의 동서남북이 모두 존재하는지 검사.
    let direction = 0;

    for (let i = 0 ; i < 4 ; i++) {
      const [nx, ny] = [x + dx[i], y + dy[i]];
      // 인덱스의 범위가 존재할 때
      if (board[nx] && board[nx][ny]) {
        const near = board[nx][ny];
        direction += 1;

        // 동/서/남/북 인덱스가 O 일때, O 인덱스의 동서남북을 순회한다.
        if (near === 'O') ENSW(nx, ny, ref);
      }
    }

    // 동서남북이 모두 있을때, ref 에 해당 O 의 인덱스를 추가한다.
    direction === 4 ?
      ref.push([x, y])
      // 동서남북이 모두 존재하지 않는다면, X 에 둘러쌓이지 않을 확률은 100% 이다.
      : (ref[0] = false);
  };

  // board 의 모든 인덱스를 검사한다.
  for (let x = 0 ; x < H ; x++) {
    for (let y = 0 ; y < W ; y++) {
      const thisPos = board[x][y];

      // 현재 인덱스가 X 이거나 이미 방문한 인덱스 이면 동서남북을 검사하지 않는다.
      if (thisPos === 'X' || table[x][y] === 1) continue;

      // ref: 이어진 O의 좌표를 담는 배열
      const ref = [];
      // x, y 좌표를 시작으로 이어지는 O 를 찾아 ref 배열에 담는 함수
      ENSW(x, y, ref);

      // 사방이 X 로 막힌 O 는 X 로 만들어 준다. ref 에는 O 의 인덱스들이 들어 있다.
      if (ref[0]) ref.forEach(([x, y]) => board[x][y] = 'X');
    }
  }
  return board;
};

console.log(
  solve([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]).toString()
  === [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']].toString(),
);

console.log(
  solve([
          ['X', 'O', 'X', 'O', 'X', 'O'],
          ['O', 'X', 'O', 'X', 'O', 'X'],
          ['X', 'O', 'X', 'O', 'X', 'O'],
          ['O', 'X', 'O', 'X', 'O', 'X'],
        ]).toString()
  ===
  [
    ['X', 'O', 'X', 'O', 'X', 'O'],
    ['O', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'O'],
    ['O', 'X', 'O', 'X', 'O', 'X'],
  ].toString(),
);

console.log(solve(['0'].toString() === ['0'].toString()));

console.log(
  solve([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']].toString()) ===
  [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']].toString(),
);