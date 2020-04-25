// https://programmers.co.kr/learn/courses/30/lessons/42583?language=javascript
function solution(bridge_length, w, ws) {
    let num = 0, sum = 0
    const queue = []
    while (ws.length) {
      num += 1
      if (queue.length && queue[0].t === num) {
        sum -= queue.shift().w
      }
      if (sum + ws[0] <= w) {
        const w = ws.shift()
        queue.push({w, t: num + bridge_length})
        sum += w
      }
    }
    return queue.pop().t;
}

console.log(solution(2, 10, [7,4,5,6]))
console.log(solution(100, 100, [10]))
console.log(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))