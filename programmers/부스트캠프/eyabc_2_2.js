const graph =
    [
        [0, 1, 2, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ];

const dic = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
};

let end;
const ans = [];

const action = (nowIdx, cnt) => {
    if (nowIdx === end) {
        ans.push(cnt + 1);
        return;
    }
    graph[nowIdx].forEach((v, k) => {
        if (v !== 0 && k <= end) {
            cnt++;
            action(k, cnt);
        };
    });
    return;
};

function solution (origin, dest) {
    if (origin === dest) return [0];

    const nowIdx = dic[origin];
    end = dic[dest];

    action(nowIdx, 0);

    return ans.length ? ans : [-1];
}