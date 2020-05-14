function solution(A) {
  if (!A.length) return -1
  const obj = {}
  const [ max, dominator ] = A.reduce(([ m, d ], v, k) => {
    obj[v] = (obj[v] || []).concat([k])
    const tmp = Math.max(obj[v].length, m)
    return tmp > m ? [ tmp, v ] : [ m, d ]
  }, [0, -1])
  return max > A.length / 2 ? obj[dominator][0] : -1
}

const assert = require('assert').strict
require("./test.json").forEach(({ input, output }) => {
  const expected = solution(...input)
  console.log(expected)
  assert.deepEqual(expected, output)
})