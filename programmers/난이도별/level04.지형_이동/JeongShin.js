// 2020. 08. 26 코드 복습 및 수정

const key = (i, j) => i + ',' + j;

// params {number []} start : 시작 좌표 ex) [1,2]
function bfs(land, visited, start, height, edges, idx) {
    const stack = [start];
    while (stack[0]) {
        const [i, j] = stack.pop(), currHeight = land[i][j], k = key(i, j);
        visited.set(k, idx);

        [[i - 1, j], [i + 1, j], [i, j + 1], [i, j - 1]].forEach(([ni, nj]) => {
            const nk = key(ni, nj);
            // case 1 . land 배열을 벗어난 경우 skip
            if (!land[ni] || !land[ni][nj] || visited.has(nk))
                return;
            // case 2. 방문 가능한 지역일 경우 visited 체크 후 stack 에 푸쉬
            const heightDiff = Math.abs(currHeight - land[ni][nj]);
            if (heightDiff <= height) {
                visited.set(nk, idx);
                stack.push([ni, nj]);
                return;
            }
            // case 3. 방문 불가능한 지역일 경우 edges 에 푸쉬
            edges.push({from: k, to: nk, weight: heightDiff});
        })
    }
}

function find(areas, child) {
    let parent = child;
    while (areas[parent].parent > 0) {
        parent = areas[parent].parent;
    }
    return parent;
}

function union(areas, p1, p2) {
    if (p1 === p2)
        return false;
    areas[p1].parent = p2;
    return true;
}

function solution(land, height) {
    const [row, col] = [land.length, land[0].length];
    const visited = new Map(), areas = {}, edges = [];
    let answer = 0, idx = 0;

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (!visited.has(key(i, j))) {
                areas[++idx] = {idx: idx, parent: -1};
                bfs(land, visited, [i, j], height, edges, idx);
            }
        }
    }

    edges.sort((a, b) => a.weight - b.weight);

    for (const edge of edges) {
        const [from, to] = [visited.get(edge.from), visited.get(edge.to)];
        if (from === to)
            continue;
        answer += (union(areas, find(areas, from), find(areas, to)) * edge.weight);
    }

    return answer;
}

solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3);