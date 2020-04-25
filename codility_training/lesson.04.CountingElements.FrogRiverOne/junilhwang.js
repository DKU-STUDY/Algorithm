function solution(X, A) {
  const set = new Set()
  const len = A.length
  for (let i = 0; i < len; i++) { // O(n)
    set.add(A[i])
    if (set.size === X) return i
  }
  return -1
}

// console.log(solution(1, [1]) === 0)
// console.log(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) === 6)
// console.log(solution(5, [1, 2, 3, 4, 4]) === -1)
// console.log(solution(4, [1, 2, 3, 4, 4]) === 3)
// console.log(solution(4, [1, 2, 3, 4, 5, 6, 7, 8]) === 3)
console.log(solution(3, [1, 3, 1, 3, 2, 1, 3]) === 4)
