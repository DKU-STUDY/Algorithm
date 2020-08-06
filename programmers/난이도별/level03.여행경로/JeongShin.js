function solution(tickets) {
    let answer = [];
    let finished = false;

    // dfs 종료조건 : 모든 티켓을 사용할 때, 즉, 현재 여행 경로의 길이가 티켓 개수 + 1
    const len = tickets.length + 1;
    const visitable = {};

    // 1) 모든 티켓을 알파벳 순으로 정렬
    tickets.sort();

    // 2) 티켓 개수를 오브젝트에 저장
    for (const t of tickets) {
        const [from, to] = t;
        visitable[from + to] = (visitable[from + to] || 0) + 1;
    }

    // 3) 깊이 우선 탐색 : (route) 를 재귀 호출
    const dfs = route => {
        const currLen = route.length;

        // 이후에 오는 알파벳 순이 아닌 여행 경로가 answer 를 바꾸는걸 방지하기 위함
        if (finished)
            return;

        // dfs 종료 조건을 만족하면 finished 를 참으로 변경
        if (currLen === len) {
            // console.log(route, visited, visitable);
            finished = true;
            answer = route;
            return;
        }

        // 현재 route 를 기준으로 visited 정보를 구함
        const visited = route.reduce((obj, to, idx) => {
            const from = route[idx - 1];
            if (from) {
                obj[from + to] = (obj[from + to] || 0) + 1;
            }
            return obj
        }, {});

        // 마지막 여행지 기준으로 가능한 다음 여행지를 구함
        const end = route[currLen - 1];

        // 마지막 여행지 기준으로 visited 티켓 개수가 visitable 보다 작은 여행지를 다음 여행지로 선정
        tickets.forEach(v => {
            const [from, to] = v;
            if (from === end && (visited[from + to] || 0) < visitable[from + to]) {
                dfs([...route, to]);
            }
        })
    };

    dfs(["ICN"], {});
    return answer
}

