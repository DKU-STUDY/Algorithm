function solution(A) {
  const obj = {}
  const half = A.length / 2
  let max = 0;
  for (const i in A) {
    const v = A[i]
    obj[v] = (obj[v] || 0) + 1
    if (obj[v] > half) return i*1;
  }
  return -1
}

const assert = require('assert').strict
require("./test.json").forEach(({ input, output }) => {
  const expected = solution(...input)
  assert.notEqual(output.indexOf(expected), -1)
})