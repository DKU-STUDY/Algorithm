/**
 Input: grid = [
 ["1","1","1","1","0"],
 ["1","1","0","1","0"],
 ["1","1","0","0","0"],
 ["0","0","0","0","0"]
 ]
 위와 같이 1이 육지고 0이 물일 떄, 육지를 찾는 문제
 Output: 1
 */

const numIslands = function (grid) {
    const visited = {};

    if (!grid[0])
        return 0;

    const [row, col] = [grid.length, grid[0].length];
    let answer = 0;

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            const key = i + ',' + j;
            if (!visited[key]) {
                visited[key] = true;
                if (grid[i][j] === '1') {
                    dfs(grid, visited, i, j, row, col);
                    answer++;
                }
            }
        }
    }
    return answer;
};

const dfs = (grid, visited, i, j, row, col) => {
    const neighbors = [[i - 1, j], [i + 1, j], [i, j + 1], [i, j - 1]];
    for (const [i, j] of neighbors) {
        if (i < 0 || i >= row || j < 0 || j >= col)
            continue;
        const key = i + ',' + j;
        if (grid[i] && grid[i][j] && !visited[key]) {
            visited[key] = true;
            if (grid[i][j] === '1')
                dfs(grid, visited, i, j, row, col);
        }
    }
};