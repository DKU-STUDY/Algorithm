/*
* 이 문제는 과감하게 포기하겠습니다.
* 구글링 해봐도 마땅한 solution 도 없고 제가 풀 수 있는 문제는 아니라고 판단 됩니다 😢
* */

function solution(A, B) {
    class Graph {
        constructor() {
            this.adjList = {};
        }

        addVertex(v) {
            if (!this.adjList[v])
                this.adjList[v] = [];
        }

        addEdge(from, to) {
            this.adjList[from].push(to);
            this.adjList[to].push(from);
        }

        dfs(start) {
            const path = [];
            const visited = {};
            const adjList = this.adjList;
            (function dfs(v) {
                if (!v) return null;
                visited[v] = true;
                path.push(v);
                adjList[v].forEach(neighbor => {
                    if (!visited[neighbor]) {
                        return dfs(neighbor);
                    }
                })
            })(start);

            const len = path.length;
            // 나누지 않았을때, 둘로 나누었을때, 셋으로 나누었을때
            const d2 = Math.floor(len / 2) * Math.ceil(len / 2);
            const d3 = Math.ceil(len / 3) * (Math.ceil(len / 3) - (len % 3 === 1)) * (Math.ceil(len / 3) - (len % 3 === 1 || len % 3 === 2));
            const result = Math.max(len, d2, d3);

            return result.toString();
        }
    }

    /* Build posts in Map */
    const len = A.length;
    const Map = new Graph();

    for (let i = 0; i <= len; i++) {
        Map.addVertex(i);
    }

    for (let idx = 0; idx < len; idx++) {
        const [from, to] = [A[idx], B[idx]];
        Map.addEdge(from, to);
    }
    return Map.dfs('0');
}