function solution(n, results) {
    const players = {};

    const dfs = start => {
        let result = 0;
        Object.keys(players[start]).forEach((el) => {
            let count = 0;
            let visited = {};
            const stack = [];
            stack.push(start);
            while (stack[0]) {
                const curr = stack.pop();
                players[curr][el].forEach((v) => {
                    if (!visited[v]) {
                        visited[v] = true;
                        stack.push(v);
                        count++;
                    }
                })
            }
            result += count;
        })
        return result;
    }

    for (let i = 1; i <= n; i++) {
        players[i] = ({win: [], lose: []})
    }

    for (const r of results) {
        const [w, l] = r;
        players[w].win.push(l);
        players[l].lose.push(w);
    }

    let answer = 0;

    for (let i = 1; i <= n; i++) {
        const result = dfs(i);
        answer += (result === (n - 1))
    }

    return answer;
}

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])