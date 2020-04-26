function solution(N, A) {
  let start = 0, max = 0
  const arr = new Array(N).fill(0)
  for (const v of A) {
    if (N < v) {
      start = max
      continue
    }
    arr[v-1] = Math.max(arr[v-1], start) + 1
    max = Math.max(arr[v-1], max)
  }
  return arr.map(v => Math.max(v, start))
}

console.log(
  solution(5, [3,4,4,6,1,4,4]).toString() === [3,2,2,4,2].toString()
)