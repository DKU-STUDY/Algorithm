function solution(A) {
  const obj = { ']': '[', ')': '(', '}': '{' }
  const stack = []
  for (const v of [...A]) {
    if ('[({'.indexOf(v) !== -1) stack.push(v)
    else if(stack.pop() !== obj[v]) return 0
  }
  return 1
}

const assert = require('assert').strict
require("./test.json").forEach(({ input, output }) =>
  assert.deepEqual(solution(...input), output)
)