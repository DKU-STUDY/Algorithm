function solution (A) {
  let sum = 0, inc = 0
  for (const v of A) {
    [() => inc += 1, () => sum += inc][v]();
    if (sum > 1000000000) return -1
  }
  return sum
}

const assert = require('assert')
require('./test.json').forEach(([ input ,output ]) => {
  assert.deepEqual(solution(...input), output)
})