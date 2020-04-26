function solution(N, A) {
  const stack = new Array(N).fill(0)
  let start = 0
  let max = start

  for (const v of A) {
    console.log(stack)
    if (N < v) {
      start = max
      continue
    }
    stack[v - 1] = Math.max(stack[v - 1], start) + 1
    max = Math.max(stack[v - 1], max)
  }
  const result = stack.map( v => v < start ? start : v )
  console.log(result)
  return result
}

console.log(
  solution(5, [3,4,4,6,1,4,4]).toString() === [3,2,2,4,2].toString()
)