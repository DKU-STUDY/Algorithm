function solution (numbers, k) {
  const len = numbers.length
  if (len === 1) return -1
  const check = arr => {
    let prev = arr.shift()
    for (const v of arr) {
      if (Math.abs(prev - v) > k) return false
      prev = v
    }
    return true
  }
  const sorted = [ ...numbers ].sort((a, b) => a - b)
  if (check(sorted) === false) return -1

  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      if (i === j) continue
      if (Math.abs(numbers[i] - numbers[j]) <= k) {
        console.log(numbers[i], numbers[j])
      }
    }
  }
}

console.log(solution([10, 40, 30, 20], 20) === 1)
// console.log(solution([3, 7, 2, 8, 6, 4, 5, 1], 3) ===	2)
// console.log(solution([0, 100, 200, 300, 400], 40) ===	-1)
// console.log(solution([0, 11, 20, 30, 40], 10) ===	-1)
// console.log(solution([0, 1, 2, 3, 10],  6) ===	-1)