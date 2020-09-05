/**
 * Board 내부에 단어들로 word 를 만들 수 있는지 판단
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
const exist = function (board, word) {
    const [row, col] = [board.length, board[0].length];
    const visited = {};
    const target = word.length;
    const checkOutOfBound = (i, j) => {
        return i >= row || i < 0 || j >= col || j < 0;
    };

    const search = (i, j, idx) => {
        const key = `${i},${j}`;

        if (idx === target)
            return true;

        if (checkOutOfBound(i, j) || board[i][j] !== word[idx] || visited[key] === true)
            return false;

        visited[key] = true;
        if (search(i - 1, j, idx + 1) || search(i + 1, j, idx + 1)
            || search(i, j - 1, idx + 1) || search(i, j + 1, idx + 1))
            return true;

        visited[key] = false;
        return false;
    };

    for (let i = 0; i < row; i++)
        for (let j = 0; j < col; j++)
            if ((board[i][j] === word[0]) && search(i, j, 0))
                return true;

    return false;
};