function solution(A) {
  A.sort((a, b) => a - b)
  for (let i = 0, len = A.length - 2; i < len; i++) {
    if (A[i + 1] > A[i + 2] - A[i]) return 1;
  }
  return 0
}

const assert = require('assert').strict
require("./test.json").forEach(({ input, output }) =>
  assert.deepEqual(solution(...input), output)
)