function solution(X, A) {
  const arr = [...new Array(X).keys()].map(v => false) // O(n)
  const len = A.length
  for (let i = 0; i < len; i++) { // O(n)
    const v = A[i]
    arr[v - 1] = true
    if (arr.indexOf(false) === -1) return i // O(n)
  }

  // 최종 : O(n^2)
  return -1
}

// console.log(solution(1, [1]) === 0)
// console.log(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) === 6)
// console.log(solution(5, [1, 2, 3, 4, 4]) === -1)
// console.log(solution(4, [1, 2, 3, 4, 4]) === 3)
// console.log(solution(4, [1, 2, 3, 4, 5, 6, 7, 8]) === 3)
console.log(solution(3, [1, 3, 1, 3, 2, 1, 3]) === 4)
