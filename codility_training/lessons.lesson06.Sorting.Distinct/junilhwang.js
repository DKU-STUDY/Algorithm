function solution (A) {
  return Object.keys(A.reduce((obj, v) => (obj[v] = true, obj), {})).length
}

const assert = require('assert')
require('./test.json').forEach(([ input ,output ]) => {
  assert.deepEqual(solution(...input), output)
})