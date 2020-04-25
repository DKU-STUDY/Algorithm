// https://programmers.co.kr/learn/courses/30/lessons/42862
function solution(n, lost, reserve) {
  const arr = [-1]
  for (let i = 1; i <= n; i++) arr[i] = 1
  lost.forEach(v => arr[v] -= 1)
  reserve.forEach(v => arr[v] += 1)
  for (let i = 1; i <= n; i++) {
    if (arr[i] === 2 && arr[i - 1] === 0) arr[i - 1] = arr[i] = 1
    if (arr[i] === 2 && arr[i + 1] === 0) arr[i + 1] = arr[i] = 1
  }
  return arr.filter(v => v >= 1).length;
}

console.log(solution(5, [2, 4], [1, 3, 5]), 5)
console.log(solution(5, [2, 4], [3]), 4)
console.log(solution(3, [3], [1]), 2)
console.log(solution(2, [1], [2]), 2)