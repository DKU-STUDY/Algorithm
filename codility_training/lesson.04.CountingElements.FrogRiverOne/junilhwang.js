function solution(X, A) {
  const arr = [...new Array(X).keys()].map(v => false)
  const len = A.length
  for (let i = 0; i < len; i++) {
    const v = A[i]
    if (arr[v - 1] === undefined) continue
    arr[v - 1] = true
    if (X === v) {
      if (arr.indexOf(false) === -1) return i
    }
  }
  return -1
}

console.log(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) === 6)
