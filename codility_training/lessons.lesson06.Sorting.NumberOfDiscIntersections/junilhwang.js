function solution (A) {
  const len = A.length
  let sum = 0
  for (let i = 0; i < len; i++) {
    const v = A[i]
    for (let j = i + 1; j < len; j++) {
      const v2 = A[j]
      if (!(i-v > j+v2 || i+v < j-v2)) {
        sum += 1
        if (sum > 10000000) return -1
      }
    }
  }
  return sum
}

const testCase = require("./test.json")
testCase.forEach(({ input, output }) =>
  console.log(input.toString(), '\n', solution(...input), output)
)