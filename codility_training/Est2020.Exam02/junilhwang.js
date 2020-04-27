function solution (A) {
  const obj = {}
  return A.reduce((max, v, k) => {
    const n = [...`${v}`].reduce((a, b) => a*1 + b*1)
    const arr = obj[n] || []
    if (arr) {
      const sum = Math.max(...arr.map(v2 => v + A[v2]))
      if (sum > max) max = sum
    }
    obj[n] = (arr.push(k), arr)
    return max
  }, -1)
}

console.log(solution([51, 71, 17, 42]) === 93)
console.log(solution([42, 33, 60]) === 102)
console.log(solution([51, 32, 43]) === -1)
console.log(solution([11, 2, 3, 21]) === 24)
console.log(solution([11, 2, 20]) === 31)
console.log(solution([1]) === -1)
console.log(solution([199999, 199989, 199998]) === 199989 + 199998)