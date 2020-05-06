/**
 * 평균이 최소인 Slice의 시작 위치
 * @param A
 */
function solution(A) {
  const len = A.length
  const sum = (a, b) => a + b
  let min = Infinity, i = 0, resolve = -1
  do {
    const arr1 = A.slice(i, i + 2), avg1 = arr1.reduce(sum) / arr1.length
    const arr2 = A.slice(i, i + 3), avg2 = arr2.reduce(sum) / arr2.length
    let tmp = Math.min(avg1, avg2, min)
    if (tmp !== min) ([ resolve, min ] = [ i, tmp ])
    i += 1
  } while (i < len - 1)
  return resolve
}

const testCase = require("./test.json")
testCase.forEach(({ input, output }) => console.log(input.toString(), '\n', solution(...input), output))
