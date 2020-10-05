/**
 * @param {string[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
const solve = function (board) {
    if (!board[0])
        return;
    const [row, col] = [board.length, board[0].length];
    const visited = new Map();
    const parent = new Map();
    let num = 1;

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            const key = i + ',' + j;
            if (board[i][j] === 'O' && !visited.has(key)) {
                parent.set(num, true);
                union(board, [i, j], visited, parent, num);
            }
            if (parent.get(visited.get(key)))
                board[i][j] = 'X';
            num++;
        }
    }
};


const union = function (board, start, visited, map, num, coords) {
    const stack = [start];

    while (stack[0]) {
        const [i, j] = stack.pop();
        const key = i + ',' + j;
        visited.set(key, num);

        [[i - 1, j], [i + 1, j], [i, j + 1], [i, j - 1]].forEach(([i, j]) => {
            const key = i + ',' + j;

            // 만약 undefined 를 마주할 경우 ('X'로 둘러 쌓이지 않은 경우) 해당 전체 set 은 false 로 바꿔준다.
            if (!board[i] || !board[i][j])
                map.set(num, false);

            // 아직 방문하지 않은 'O' 구역의 coords 는 스택에 푸쉬
            if (board[i] && board[i][j] === 'O' && !visited.get(key)) {
                stack.push([i, j]);
            }
        })
    }
};