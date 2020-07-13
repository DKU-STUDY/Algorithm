/* 1번 케이스 불합격 ㅠ ㅠ
* 이 문제는 실력 더 키우고 다시 풀이 도전 해보겠습니다. 아직까진 다른 사람 solution 참고해도 잘 이해가 안가네요 ㅠ
* */

function solution(tickets) {
    const visitable = {};
    const graph = {};
    const ticketsInfo = {};

    const dfs = start => {
        const route = [];
        const visited = {};
        const ticketUsed = {};
        route.push(start);

        (function dfs(from) {
            graph[from].forEach((to) => {
                if ((visited[to] || 0) < visitable[to] && (ticketUsed[from + to] || 0) < ticketsInfo[from + to]) {
                    ticketUsed[from + to] = (ticketUsed[from + to] || 0) + 1;
                    visited[to] = (visited[to] || 0) + 1;
                    route.push(to);
                    dfs(to);
                }
            });
        })(start);

        for (const [ticket, count] of Object.entries(ticketsInfo)){
            if (ticketUsed[ticket] !== count)
                route.push(ticket.slice(3))
        }

        return route;
    }


    for (const t of tickets) {
        const [from, to] = t;
        graph[from] = (graph[from] || [])
        graph[from].push(to);
        ticketsInfo[from + to] = (ticketsInfo[from + to] || 0) + 1;
        visitable[from] = (visitable[from] || 0) + 1;
    }

    for (const dest of Object.values(graph))
        dest.sort();

    return dfs("ICN");
}

/* 다른 사람의 풀이 */

function solution(tickets) {
    let answer = [];
    const target_len = tickets.length - 1;
    tickets.sort();
    let finished = false;
    const dfs = (start, remain, route) => {
        if (finished)
            return;
        const possibleTickets = remain.filter(v => v[0] === start)
        possibleTickets.forEach(possibleTkt => {
            let temp_remain = Array.from(remain);
            let temp_route = Array.from(route);
            const idx = temp_remain.findIndex(i => i === possibleTkt)
            temp_remain.splice(idx, 1);
            if (temp_route.length === target_len) {
                temp_route = temp_route.concat(possibleTkt)
                finished = true;
                answer = temp_route;
            } else {
                temp_route.push(possibleTkt[0])
                dfs(possibleTkt[1], temp_remain, temp_route)
            }
        })
    };
    dfs('ICN', tickets, [])
    return answer
}


