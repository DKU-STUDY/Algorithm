// https://programmers.co.kr/learn/courses/30/lessons/42840
function solution(answers) {
  const arr = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  ]
  const len = arr.map(v => v.length)
  const result = arr.map((v, k) => answers.map((v2, k2) => v[k2 % len[k]] === v2).filter(v2 => v2).length)
  const max = Math.max(...result)
  const answer = []
  result.forEach((v, k) => { if (v == max) answer.push(k + 1) })
  return answer
}

console.log(solution([1,2,3,4,5]),[1])
console.log(solution([1,3,2,4,2]),[1, 2, 3])