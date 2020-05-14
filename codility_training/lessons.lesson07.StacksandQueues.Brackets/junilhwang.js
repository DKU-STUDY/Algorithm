function solution(A) {
  const obj = { ']': '[', ')': '(', '}': '{' }
  const stack = []
  return (![ ...A ].some(v => {
    if ('[({'.indexOf(v) !== -1) stack.push(v)
    else if(stack.pop() !== obj[v]) return true
  }) && !stack.length) * 1
}

const assert = require('assert').strict
require("./test.json").forEach(({ input, output }) =>
  assert.deepEqual(solution(...input), output)
)