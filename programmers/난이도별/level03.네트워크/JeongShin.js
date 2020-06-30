function solution(n, computers) {
    let ans = 0;
    const visited = new Array(n).fill(false);
    const check_visited_all = () => {
        return !visited.find(el => !el);
    };
    const dfs = start => {
        const queue = [];
        queue.push(start);
        while (queue.length) {
            const index = queue.pop();
            const curr = computers[index];
            visited[index] = true;
            for (let i = 0; i < n; i++) {
                const next = curr[i];
                if (next && !visited[i])
                    queue.push(i);
            }
        }
    };
    while (!check_visited_all()) {
        const start = visited.indexOf(false);
        dfs(start);
        ans++;
    }
    return ans;
}

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]);
// solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]);
