function solution (A) {
  return Object.keys(A.reduce((obj, v) => (obj[v] = true, obj), {})).length
}

function solution2 (A) {
  return new Set(A).size
}

const assert = require('assert')
require('./test.json').forEach(([ input ,output ]) => {
  assert.deepEqual(solution(...input), output)
  assert.deepEqual(solution2(...input), output)
})