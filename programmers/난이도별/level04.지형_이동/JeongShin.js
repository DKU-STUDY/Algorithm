/*
* 현재 좌표 start 에서 탐색 가능한 모든 좌표를 방문
* @param {object} visited : 좌표 방문 정보
* @param {object} set : Set
* @param {number} height : 넘을 수 있는 최대 높이 (문제에서 주어진 값)
* @param {number} bound : N * N 좌표에서 N 의 값 (문제에서 주어진 값)
* @param {Array.<number>} land : 2차원 배열 높이 정보 (문제에서 주어진 값)
* @param {Array.<number>} start : 탐색 시작 좌표 ex) [x, y]
* @param {Array.<Object>} edges : edge 정보를 포함한 배열
* */

function bfs(visited, set, height, bound, land, start, edges) {
    const checkOutOfBound = (x, y) => {
        return (x < 0 || y < 0 || x >= bound || y >= bound);
    };

    const isVisited = (x, y) => {
        return visited[x + ',' + y];
    };

    const visit = (x, y) => {
        visited[x + ',' + y] = set.number;
    };

    const pushVisitable = (stack, x, y) => {
        const possibleCoords = [[x, y + 1], [x, y - 1], [x - 1, y], [x + 1, y]];
        for (const coords of possibleCoords) {
            if (checkOutOfBound(...coords) || isVisited(...coords))
                continue;
            const difference = Math.abs((land[x][y] - land[coords[0]][coords[1]]));
            if (difference <= height) {
                visit(...coords);
                stack.push(coords);
                continue;
            }
            edges.push({weight: difference, from: [x, y], to: coords});
        }
    };

    const stack = [start];
    visit(...start);

    while (stack[0]) {
        const coords = stack.pop();
        pushVisitable(stack, ...coords);
    }
}

/*
* 자식의 최상위 부모를 찾음
* @param {Object} set : Set
* @param {number} child : 자식 그룹 번호
* @returns {number} parent : 최상위 부모 그룹 번호
* */

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
            set[num] = {number: num, parent: -1};
            bfs(visited, set[num], height, n, land, [i, j], edges);
            num++;
        }
    }

    edges.sort((a, b) => a.weight - b.weight);

    /* Union-find */
    let answer = 0;
    for (const e of edges) {
        const children = [visited[e.from], visited[e.to]];

        if (children[0] === children[1])
            continue;

        if (union(set, ...children.map(v => find(set, v))))
            answer += e.weight;
    }

    return answer;
}

// solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 3);