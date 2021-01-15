/**
 * @param {number[][]} M
 * @return {number}
 */
const findCircleNum = function (M) {
    const N = M.length;
    const group = new Map();
    let groupNum = 0;

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            if (M[i][j] === 1 && !group.has(i)) {
                group.set(i, ++groupNum);
                dfs(i, group, groupNum, N, M);
            }
        }
    }
    return groupNum;
};

function dfs(student, group, groupNum, N, M) {
    for (let friend = 0; friend < N; friend++) {
        if (M[student][friend] === 1 && !group.has(friend)) {
            group.set(friend, groupNum);
            dfs(friend, group, groupNum, N, M);
        }
    }
}


