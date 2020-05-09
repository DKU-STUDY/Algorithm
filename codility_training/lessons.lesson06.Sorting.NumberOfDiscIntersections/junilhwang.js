function solution (A) {
  const arr = []
  const len = A.length
  let sum = 0
  for (let i = 0; i < len; i++) {
    const start = i - A[i]
    const end = i + A[i]
    for (let j = 0; j < len; j++) {
      if (i === j) continue;
      const start2 = j - A[j]
      const end2 = j + A[j]
      if (!(start > end2 || end < start2)) {
        arr[i] = arr[i] || new Set()
        arr[j] = arr[j] || new Set()
        if (!arr[i].has(j)) {
          arr[i].add(j)
          arr[j].add(i)
          sum += 1
        }
      }
    }
  }
  return sum
}

const testCase = require("./test.json")
testCase.forEach(({ input, output }) =>
  console.log(input.toString(), '\n', solution(...input), output)
)