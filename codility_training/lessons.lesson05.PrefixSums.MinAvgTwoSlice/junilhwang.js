/**
 * 평균이 최소인 Slice의 시작 위치
 * @param A
 */
function solution(A) {
  const len = A.length
  const sum = (a, b) => a + b
  let min = Infinity, i = 0, resolve = -1
  do {
    const arr1 = A.slice(i, i + 2), len1 = arr1.length
    const arr2 = A.slice(i, i + 3), len2 = arr2.length
    let tmp = Math.min(arr1.reduce(sum) / len1, arr2.reduce(sum) / len2, min)
    if (tmp !== min) {
      resolve = i
      min = tmp
    }
    i += 1
  } while (i < len - 1)
  return resolve
}

const testCase = require("./test.json")
testCase.forEach(({ input, output }) => console.log(input.toString(), '\n', solution(...input), output))
