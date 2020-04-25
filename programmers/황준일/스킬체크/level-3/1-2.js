function solution(N, road, K) {
    var answer = 1;
    const path = []
    path.length = N
    for (let i = 0; i < N; i++) {
        const p = []
        for (let j = 0; j < N; j++) {
            p[j] = 0
        }
        path[i] = p
    }
    road.forEach( v => {
        path[v[0] - 1][v[1] - 1] = path[v[1] - 1][v[0] - 1] = v[2]
    })

    path.forEach( v => {
        
    })
}

console.log(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
console.log(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))