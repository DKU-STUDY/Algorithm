const find = function (child, map) {
    let parent = child;
    while (map.has(parent)) {
        parent = map.get(parent);
    }
    return parent;
};

// from 이 속한 집합에 to 를 포함 시킵니다. 만약 싸이클이 발생하는 경우에는 true 를 반환 합니다.
const union = function (from, to, map) {
    map.set(to, from);
};

/**
 * @param {number[][]} edges
 * @return {number[]}
 */

const findRedundantConnection = function (edges) {
    const map = new Map();
    const answer = [];

    for (let edge of edges) {
        let [from, to] = edge;
        to = map.has(to) ? find(to, map) : to;
        from = map.has(from) ? find(from, map) : from;
        from === to ? answer.push(edge) : union(from ,to, map);
    }

    return answer.pop();
};


findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]); // [1, 4]
