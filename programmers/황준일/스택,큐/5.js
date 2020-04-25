// https://programmers.co.kr/learn/courses/30/lessons/42586?language=javascript
function solution(progresses, speeds) {
  var answer = [];
  while (progresses.length) {
    if (progresses.length === 1) {
      answer.push(1)
      break
    }
    for (let i = 0, len = progresses.length; i < len; i++) {
      if (progresses[i] < 100) progresses[i] += speeds[i]
    }
    let num = 0
    while (progresses[0] >= 100) {
      num += 1, progresses.shift(), speeds.shift()
    }
    if (num > 0) answer.push(num)
  }
  return answer;
}
console.log(solution([1, 93, 30, 99], [99, 1, 29, 5]))