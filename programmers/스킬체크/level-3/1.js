function solution(N, road, K) {
    var answer = 1;
    const path = []
    const shortest = (end, p, t) => {
        if (path[end] && path[end].t < t) return
        const last = p.slice(-1)[0]
        if (last === end) path[end] = {p, t}
        for (let i = 0, len = road.length; i < len; i++) {
            const v = road[i]
            if (v[0] === last && p.indexOf(v[1]) === -1) {
                shortest(end, [...p, v[1]], t + v[2])
            } else if (v[1] === last && p.indexOf(v[0]) === -1) {
                shortest(end, [...p, v[0]], t + v[2])
            }
        }
    }
    for (let i = 2; i <= N; i++) {
        shortest(i, [1], 0)
    }
    console.log(path)
    return path.filter(v => v.t <= K).length + 1;
}

console.log(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
console.log(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))