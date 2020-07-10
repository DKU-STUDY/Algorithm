function solution(tickets) {
    const visitable = {};
    const graph = {};

    const dfs = start => {
        const route = [];
        const visited = {};
        // route.push(start);

        (function dfs(from) {
            if (!graph[from])
                return;
            graph[from].forEach((to) => {
                if ((visited[from + to] || 0) < visitable[from + to]) {
                    visited[from + to] = (visited[from + to] || 0) + 1;
                    route.push(to);
                    dfs(to);
                }
            });
        })(start);

        return route;
    }


    for (const t of tickets) {
        const [from, to] = t;
        graph[from] = (graph[from] || [])
        graph[from].push(to);
        visitable[from + to] = (visitable[from + to] || 0) + 1;
    }

    for (const dest of Object.values(graph))
        dest.sort();


    return dfs("ICN");
}

const r = solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]])
console.log(r);