function solution (N) {
  const b = N.toString(2)
  const len = b.length
  let i = 0, max = 0;
  while (i < len) {
    const idx = b.indexOf('1', i + 1)
    if (idx === -1) break
    max = Math.max(idx - i - 1, max)
    i = idx
  }
  return max
}

console.log(solution(32) === 0)
console.log(solution(1041) === 5)
console.log(solution(9) === 2)
console.log(solution(529) === 4)
console.log(solution(20) === 1)
console.log(solution(15) === 0)