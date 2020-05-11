function solution (A) {
  const arr = A.map(() => new Set())
  const len = A.length
  return A.reduce((sum, v, i) => {
    for (let j = i + 1; j < len; j++) {
      const v2 = A[j]
      if (!(i-v > j+v2 || i+v < j-v2)) {
        if (!arr[i].has(j)) {
          arr[i].add(j)
          arr[j].add(i)
          sum += 1
        }
      }
    }
    return sum
  }, 0)
}

const testCase = require("./test.json")
testCase.forEach(({ input, output }) =>
  console.log(input.toString(), '\n', solution(...input), output)
)