/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
const updateMatrix = function (matrix) {
    const [row, col] = [matrix.length, matrix[0].length];
    const answer = [];
    for (let i = 0; i < row; i++) {
        answer[i] = answer[i] || [];
        for (let j = 0; j < col; j++) {
            if (matrix[i][j] === 0) {
                answer[i][j] = 0;
                continue;
            }
            answer[i][j] = bfs([i, j], matrix);
        }
    }
    return answer;
};

const key = ([x, y]) => `${x},${y}`;

const bfs = function (coordinates, matrix) {
    const stack = [[coordinates[0], coordinates[1], 0]];
    const visited = new Map();
    visited.set(key(coordinates), true);

    while (stack[0]) {
        let [i, j, distance] = stack.shift();
        if (matrix[i][j] === 0)
            return distance;
        [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
            .forEach(([x, y]) => {
                const k = key([x, y]);
                if (matrix[x] !== undefined && matrix[x][y] !== undefined && !visited.get(k)) {
                    visited.set(k, true);
                    stack.push([x, y, distance + 1]);
                }
            })
    }
};
