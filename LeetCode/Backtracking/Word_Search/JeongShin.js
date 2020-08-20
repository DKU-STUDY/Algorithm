/**
 * Board 내부에 단어들로 word 를 만들 수 있는지 판단
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */


const exist = function (board, word) {
    const [row, col] = [board.length, board[0].length];

    const getNeighbors = (char, x, y) =>
        [[x - 1, y], [x, y + 1], [x + 1, y], [x, y - 1]]
            .filter(([x, y]) => board[x] && (board[x][y]) === char);

    const search = (word, start) => {
        const visited = {};
        const target = word.length;

        visited[start[0] + ',' + start[1]] = true;
        let result = false;

        (function dfs(word, pos, idx = 1) {
            if (idx === target)
                return result = true;
            getNeighbors(word[idx], ...pos).forEach(([x, y]) => {
                if (!visited[x + ',' + y]) {
                    visited[x + ',' + y] = true;
                    return dfs(word, [x, y], idx + 1);
                }
            });
        })(word, start);

        return result;
    };

    for (let i = 0; i < row; i++)
        for (let j = 0; j < col; j++)
            if (board[i][j] === word[0] && search(word, [i, j]))
                return true;

    return false;
};