class Coords {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    toString() {
        return this.x + ',' + this.y;
    }
}

/*
* 현재 좌표 start 에서 탐색 가능한 모든 좌표를 방문
* @param {object} visited : 좌표 방문 정보
* @param {object} set : Set
* @param {number} height : 넘을 수 있는 최대 높이 (문제에서 주어진 값)
* @param {number} bound : N * N 좌표에서 N 의 값 (문제에서 주어진 값)
* @param {Array.<number>} land : 2차원 배열 높이 정보 (문제에서 주어진 값)
* @param {Coords} start : 탐색 시작 좌표 ex) [x, y]
* @param {Array.<Object>} edges : edge 정보를 포함한 배열
* */
function bfs(visited, set, height, bound, land, start, edges) {
    const checkOutOfBound = (x, y) => (x < 0 || y < 0 || x >= bound || y >= bound);

    const pushVisitable = (stack, curr, x = curr.x, y = curr.y) => {
        const possibleCoords = [[x, y + 1], [x, y - 1], [x - 1, y], [x + 1, y]].map((v) => new Coords(v[0], v[1]));

        for (const next of possibleCoords) {
            if (checkOutOfBound(next.x, next.y) || visited[next.toString()])
                continue;

            const difference = Math.abs((land[x][y] - land[next.x][next.y]));

            if (difference <= height) {
                visited[next.toString()] = set.area;
                stack.push(next);
                continue;
            }
            edges.push({weight: difference, from: curr, to: next});
        }
    };

    const stack = [start];
    visited[start.toString()] = set.area;

    while (stack[0]) {
        pushVisitable(stack, stack.pop());
    }
}

function find(set, child) {
    let parent = child;
    while (set[parent].parent > 0) {
        parent = set[parent].parent;
    }
    return parent;
}

function union(set, p1, p2) {
    if (p1 === p2)
        return;
    set[p1].parent = p2;
    return true;
}

function solution(land, height) {
    const n = land.length;
    const visited = {}, set = {}, edges = [];
    let num = 1;

    /* bfs */
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (visited[i + ',' + j])
                continue;
            set[num] = {area: num, parent: -1};
            bfs(visited, set[num], height, n, land, new Coords(i, j), edges);
            num++;
        }
    }

    let answer = 0;
    edges.sort((a, b) => a.weight - b.weight);

    /* Union-find */
    for (const e of edges) {
        const [c1, c2] = [visited[e.from.toString()], visited[e.to.toString()]];

        if (c1 === c2)
            continue;

        if (union(set, find(set, c1), find(set, c2)))
            answer += e.weight;
    }

    return answer;
}