const find = function (child, map) {
    let parent = child;
    while (map.has(parent)) {
        parent = map.get(parent);
    }
    return parent;
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
        from === to ? answer.push(edge) : map.set(to, from);
    }

    return answer.pop();
};


findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]); // [1, 4]
