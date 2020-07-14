function solution(tickets) {
    let answer = [];
    let finished = false;
    const len = tickets.length + 1;
    const visitable = {};

    tickets.sort();

    for (const t of tickets) {
        const [from, to] = t;
        visitable[from + to] = (visitable[from + to] || 0) + 1;
    }

    const dfs = (route, visited) => {
        const currLen = route.length;

        if (finished)
            return;

        if (currLen === len) {
            // console.log(route, visited, visitable);
            finished = true;
            answer = route;
            return;
        }

        const currVisited = route.reduce((obj, to, idx) => {
            const from = route[idx - 1];
            if (from) {
                obj[from + to] = (obj[from + to] || 0) + 1;
            }
            return obj
        }, {});

        const end = route[currLen - 1];

        tickets.forEach(v => {
            const [from, to] = v;
            if (from === end && (visited[from + to] || 0) < visitable[from + to]) {
                visited[from + to] = (visited[from + to] || 0) + 1;
                dfs([...route, to], currVisited);
            }
        })
    };

    dfs(["ICN"], {});
    return answer
}

// solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]);
//["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
// solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]])