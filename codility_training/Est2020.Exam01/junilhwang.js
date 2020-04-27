function solution (A) {
  A.sort((a, b) => b - a)
  const len = A.length
  let i = 0
  while (i < len) {
    const n = A[i]
    const idx = A.lastIndexOf(n)
    if (idx - i + 1 === n) return n
    i = idx + 1
  }
  return 0
}

console.log(solution([3, 8, 2, 3, 3, 2]) === 3)
console.log(solution([7, 1, 2, 8, 2]) === 2)
console.log(solution([3, 1, 4, 1, 5]) === 0)
console.log(solution([5, 5, 5, 5, 5]) === 5)
console.log(solution([5, 5, 5, 5, 5, 5]) === 0)
console.log(solution([5, 5, 5, 5]) === 0)