function solution (A) {
  const last = A.length - 1
  A.sort((a, b) => b - a)
  return Math.max(A[0] * A[1] * A[2], A[last] * A[last - 1] * Math.max(A[0], A[last - 2]))
}

const assert = require('assert')
require('./test.json').forEach(([ input ,output ]) => {
  assert.deepEqual(solution(...input), output)
})