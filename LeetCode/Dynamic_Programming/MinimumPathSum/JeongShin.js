const minPathSum = function (grid) {
    const col = grid.length, row = grid[0].length;
    const dp = grid.map((v, i) => i === 0 ? v : v.map((v, i) => i === 0 ? v : 0));
    let [i, j] = [0, 0];

    for (i = 0; i < col; i++) {
        for (j = 0; j < row; j++) {
            if (i === 0 && j === 0)
                continue;

            let up;
            if ( (up = (dp[i - 1] || [])[j]) === undefined)
                up = Infinity;

            let left;
            if ((left = dp[i][j - 1]) === undefined)
                left = Infinity;

            dp [i][j] = Math.min(left, up) + grid[i][j];
        }
    }

    return dp[col - 1][row - 1];
};

minPathSum([[0,0],[0,0]]);

/* 다른 사람 코드를 참고한 풀이 */
const minPathSum2 = function (grid) {
    const col = grid.length;
    const row = grid[0].length;

    for (let i = 1; i < col; i++) {
        grid[i][0] += grid[i - 1][0];
    }

    for (let j = 1; j < row; j++) {
        grid[0][j] += grid[0][j - 1];
    }

    for (let i = 1; i < col; i++) {
        for (let j = 1; j <row; j++) {
            grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
        }
    }
    return grid[col - 1][row - 1];
};