function solution(A) {
  const len = A.length
  const back = [ A.pop() ]
  let cnt = 0

  const getLeader = arr => {
    const obj = {}
    const half = arr.length / 2
    let max = 0;
    for (let i = 0, len = arr.length; i < len; i++) {
      const v = A[i]
      obj[v] = (obj[v] || 0) + 1
      if (obj[v] > half) return v;
    }
  }

  for (let i = 1; i < len - 1; i++) {
    const FL = getLeader(A)
    const BL = getLeader(back)
    cnt += FL !== undefined && BL !== undefined && FL === BL
    back.push(A.pop())
  }
  return cnt
}

const assert = require('assert').strict
require("./test.json").forEach(({ input, output }) => {
  assert.deepEqual(solution(...input), 2)
})