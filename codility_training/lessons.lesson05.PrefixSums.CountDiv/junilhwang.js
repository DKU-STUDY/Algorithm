/**
 * 정수 인수 A, B ,K 가 주어지고, A <= B 입니다.
 * 이 범위 사이의 수 중 (A <= i <= B) 가 K로 나누었을 때 나머지가 0이 되는 수의 갯수를 return 하는 문제입니다.
 */
function solution (A, B, K) {
  let cnt = 0
  const mod = A % K
  const start = A + (mod === 0 ? 0 : K - mod)
  for (let i = start; i < B + 1; i += K) cnt += 1
  return cnt
}

const testCase = require("./test.json")

testCase.forEach(({ input, output }) => console.log(solution(...input), output))
