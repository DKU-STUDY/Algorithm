// https://programmers.co.kr/learn/courses/30/lessons/42747?language=javascript
function solution(citations) {
  for (let h = Math.max(...citations); h > -1 ; h--)
    if (citations.filter(v => v >= h).length >= h) return h
  return 0
}

console.log(solution([3, 0, 6, 1, 5]), 3)
console.log(solution([22, 42]), 2)