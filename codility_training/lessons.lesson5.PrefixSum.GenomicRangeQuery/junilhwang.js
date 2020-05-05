function solution(S, P, Q) {
  const obj = { 'A': 1, 'C': 2, 'G': 3, 'T': 4 }
  const arr = [ ...S ].map(v => obj[v])
  return P.map((start, k) => Math.min(...arr.slice(start, Q[k] + 1)))
}

const testCase = require("./test.json")
testCase.forEach(({ input, output }) => (console.log(input), console.log(solution(...input), output)))