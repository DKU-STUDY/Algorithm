function solution(S, P, Q) {
  return P.map((start, k) => {
    const end = Q[k]
    const A = S.indexOf('A', start)
    if ( A !== -1 && A <= end) return 1
    const C = S.indexOf('C', start)
    if ( C !== -1 && C <= end) return 2
    const G = S.indexOf('G', start)
    if ( G !== -1 && G <= end) return 3
    const T = S.indexOf('T', start)
    if ( T !== -1 && T <= end) return 4
  })
}

function solution2(S, P, Q) {
  return P.map((start, k) => {
    const str = S.substring(start, Q[k] + 1)
    if ( str.indexOf('A') !== -1 ) return 1
    if ( str.indexOf('C') !== -1 ) return 2
    if ( str.indexOf('G') !== -1 ) return 3
    if ( str.indexOf('T') !== -1 ) return 4
  })
}

require("./test.json")
  .forEach(({ input, output }) =>
    console.log(solution2(...input).toString() === output.toString())
  )