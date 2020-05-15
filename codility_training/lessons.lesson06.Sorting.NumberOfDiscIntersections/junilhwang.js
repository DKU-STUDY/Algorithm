function solution (A) {
  const [ upper, lower ] = A.reduce( ( [ u, l ], v ,i ) => (u.push(i + v), l.push(i - v), [ u, l ]), [ [], [] ])
  upper.sort((a, b) => a - b)
  lower.sort((a, b) => a - b)
  let sum = 0
  for (let i = 0, j = 0, len = A.length; i < len; i++) {
    while(upper[i] >= lower[j]){
      sum += j++ - i;
      if (lower[j] === undefined) return sum;
      if (sum > 10000000) return -1;
    }
  }
  return sum
}

const testCase = require("./test.json")
const assert = require('assert').strict
testCase.forEach(({ input, output }) =>
  assert.deepEqual(solution(...input), output)
)