function solution(tickets) {
    // dfs 종료조건 : 모든 티켓을 사용할 때, 즉, 현재 여행 경로의 길이가 티켓 개수 + 1
    const target = tickets.length + 1;
    let answer = false;

    // 1) 모든 티켓을 알파벳 순으로 정렬
    tickets.sort();

    const ticketCount = tickets.reduce((obj, t) => {
        const [from, to] = t;
        obj[from + to] = (obj[from + to] || 0) + 1;
        return obj;
    }, {});

    const dfs = routes => {
        const len = routes.length;

        if (answer)
            return;

        if (len === target) {
            return answer = routes;
        }

        const visited = routes.reduce((obj, to, idx) => {
            const from = routes[idx - 1];
            if (from)
                obj[from + to] = (obj[from + to] || 0) + 1;
            return obj;
        }, {});

        const end = routes[len - 1];

        tickets.forEach((v) => {
            const [from, to] = v;
            if (from === end && ((visited[from + to] || 0) < ticketCount[from + to]))
                dfs([...routes, to]);
        })
    }

    dfs(["ICN"]);
    return answer
}

