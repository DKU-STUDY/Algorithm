function solution (A, K) {
  if (!A || A.length === 0) return []
  const len = A.length, arr = A.splice(len - K % len)
  return [ ...arr, ...A ]
}

console.log(solution([3, 8, 9, 7, 6], 3).toString() === [9, 7, 6, 3, 8].toString())
