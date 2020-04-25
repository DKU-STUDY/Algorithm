function solution (A) {

  const checker = arr => {
    const len = arr.length
    if (len === 1) return true
    if (arr[0] === arr[1]) return false

    let before = arr[0] < arr[1]
    for (let i = 1; i < len - 1; i++) {
      const now = arr[i] < arr[i+1]
      if (arr[i] === arr[i+1] || now === before) return false
      before = now
    }
    return true
  }

  if (checker(A) === true) return 0

  const len = A.length
  let cnt = 0

  for (let i = 0; i < len; i++) {
    const arr1 = A.slice(0, i)
    const arr2 = A.slice(i + 1)
    cnt += checker([...arr1, ...arr2]) ? 1 : 0
    arr1.push(arr2.shift())
  }

  return cnt === 0 ? -1 : cnt
}

console.log(solution([3, 4, 5, 3, 7]) === 3)
console.log(solution([1, 2, 3, 4]) === -1)
console.log(solution([1, 3, 1, 2]) === 0)
console.log(solution([1, 3, 3, 3]) === -1)
console.log(solution([1]) === 0)
console.log(solution([1, 1]) === 2)
console.log(solution([1, 2]) === 0)
console.log(solution([2, 2]) === 2)
console.log(solution([2, 2, 2]) === -1)
console.log(solution([2, 3, 2]) === 0)
console.log(solution([10, 20, 30, 20]) === 2)
console.log(solution([10, 20, 30, 19]) === 3)
console.log(solution([10, 20, 30, 19, 10, 20, 30, 19]) === -1)