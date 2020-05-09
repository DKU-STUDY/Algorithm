function solution (A) {
  const arr = []
  const len = A.length
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      if (i === j) continue;
    }
  }
  return 0
}

const testCase = require("./test.json")
testCase.forEach(({ input, output }) =>
  console.log(input.toString(), '\n', solution(...input), output)
)