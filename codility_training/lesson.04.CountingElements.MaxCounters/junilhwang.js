function solution(N, A) {
  const stack = new Array(N).fill(0)
  let max = 0
  for (const v of A) {
    if (N < v) {
      stack.forEach((v, k) => stack[k] = max)
      continue
    }
    stack[v-1] += 1
    max = Math.max(stack[v-1], max)
  }
  return stack
}

console.log(
  solution(5, [3,4,4,6,1,4,4]).toString() === [3,2,2,4,2].toString()
)