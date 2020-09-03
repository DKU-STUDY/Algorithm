/*
* 노드의 개수 n 과 edge 정보 edges 가 주어졌을 때
* 서로 연결된 노드 끼리를 하나의 집합이라 가정할때 집합의 노드 개수의 sqrt 를 구하여
* 모든 집합들의 sqrt 값들의 총합을 구하는 문제
* */

function connectedSum(n, edges) {
    const graph = {}, visited = {};

    const dfs = (start) => {
        const stack = [];
        stack.push(start);
        visited[start] = true;
        let weight = 0;
        while (stack.length) {
            const v = stack.pop();
            weight++;
            graph[v].forEach((n) => {
                if (!visited[n]) {
                    visited[n] = true;
                    stack.push(n)
                }
            })
        }
        return weight
    };

    for (const e of edges) {
        const [from, to] = e.split(' ');
        graph[from] = (graph[from] || []);
        graph[to] = (graph[to] || []);
        graph[to].push(from);
        graph[from].push(to);
    }

    let sum = 0;

    for (const v of Object.keys(graph)) {
        if (!visited[v])
            sum += Math.ceil(Math.sqrt(dfs(v)))
    }

    for (let i = 1; i <= n; i++) {
        if (!visited[i])
            sum++;
    }

    return sum;
}

