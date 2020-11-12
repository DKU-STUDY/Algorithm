// https://programmers.co.kr/learn/courses/30/lessons/42627?language=javascript

function solution(jobs) {
  jobs.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0])
  let total = jobs.length, job = jobs.shift(), t = job[0], sum = 0
  const q = []
  while (true) {
    while (jobs.length && t >= jobs[0][0]) {
      q.push(jobs.shift())
      if (q.length > 1) q.sort((a, b) => a[1] - b[1])
    }
    if (q[0] && !job && q[0][0] <= t) job = q.shift()
    if (job) {
      sum += (t += job[1]) - job[0]
      job = null
      if (jobs.length + q.length === 0) break
    } else t += 1
  }
  return ~~(sum / total)
}
console.log(solution([[0, 3], [10, 10]]), 6)
console.log(solution([[0, 3], [1, 9], [2, 6], [4, 3]]), 9)
console.log(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]), 74)
console.log(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]), 13)
console.log(solution([[15,34], [15,2]]), 19)
console.log(solution([[0, 5], [1, 2], [5, 5]]), 6)
console.log(solution([[0, 3], [1, 9], [2, 6]]), 9)
console.log(solution([[10, 6], [12, 6], [14, 4]]), 8)