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

const testCase = require("./test.json")
testCase.forEach(({ input, output }) => (console.log(input), console.log(solution(...input), output)))