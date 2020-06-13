function solution(N, facility) {
    if (facility.length === 1) return 0;
    let min = Infinity;
    for (let i = 0; i < N; i++ ) {
        for (let j = 0; j < N; j++) {
            const max = facility.reduce((max, v) => Math.max(
              (Math.abs(i - v[0]) + Math.abs(j - v[1])) * v[2], max
            ), 0)
            min = Math.min(min, max)
        }
    }
    return min;
}

console.log(
  solution(3, [[1,3,1],[3,1,1]]) === 2,
  solution(3, [[1,3,2],[3,1,1]]) === 3,
  solution(3, [[1,1,1]]) === 0,
)