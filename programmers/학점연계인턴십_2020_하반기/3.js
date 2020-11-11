/*
* 서로 아는 사이일 경우 1을 가지는 이차원 배열 정보를 주어졌을때
* 서로 건너건너 아는 사이일 경우 하나의 그룹으로 지정하여 그룹의 개수를 반환하는 문제
* 지금 다시보면 Union-find 문제 같지만 그냥 dfs로 풀이 했습니다.
* */

function countGroups(related) {
    const graph = {};
    const visited = {};
    const len = related.length;
    let groups = 0;

    const dfs = (start) => {
        graph[start].forEach((n)=>{
            if (!visited[n]) {
                visited[n] = true;
                dfs(n)
            }
        })
    };

    related.forEach((el, i) => {
        for (let j = 0; j < len; j++) {
            graph[i] = (graph[i] || []);
            if (el[j] === '1' && i !== j) {
                graph[i].push(j)
            }
        }
    });

    for (const v of Object.keys(graph)) {
        if (!visited[v]) {
            visited[v] = true;
            dfs(v);
            groups++;
        }
    }

    return groups;
}

