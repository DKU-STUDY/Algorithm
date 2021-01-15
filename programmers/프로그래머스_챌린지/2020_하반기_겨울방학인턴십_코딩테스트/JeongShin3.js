function solution(v) {
    const [row, col] = [v.length, v[0].length];
    const visited = new Map();
    const area = [];
    let val;

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (!visited.has(`${i},${j}`)) {
                val = v[i][j];
                dfs(v, i, j, val, visited);
                area[val] = (area[val] || 0) + 1;
            }
        }
    }
    return area;
}

function dfs(v, i, j, val, visited) {
    const stack = [[i, j]];
    visited.set(`${i},${j}`, true);

    while (stack[0]) {
        let [i, j] = stack.shift();
        const p = [[i - 1, j], [i + 1, j], [i, j + 1], [i, j - 1]];

        for (let [i, j] of p) {
            if (v[i] === undefined || v[i][j] === undefined || visited.has(`${i},${j}`) || v[i][j] !== val)
                continue;
            stack.push([i, j]);
            visited.set(`${i},${j}`, true);
        }
    }
}

// solution([[0, 0, 1, 1], [1, 1, 1, 1], [2, 2, 2, 1], [0, 0, 0, 2]]);