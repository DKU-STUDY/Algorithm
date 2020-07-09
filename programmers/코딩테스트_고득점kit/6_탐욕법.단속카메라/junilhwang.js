// 단속카메라 - https://programmers.co.kr/learn/courses/30/lessons/42884?language=javascript

function solution(routes) {
  // 미해결. 포기
  routes.sort((a, b) => Math.abs(a[0] - a[1]) - Math.abs(b[0] - b[1]))
  const stack = [], last = routes.length
  let cnt = 0
  loop: for (let i = 0; i < last; i++) {
    const [start, end] = routes[i]
    stack.push(i)
    let chk = false
    for (let j = i + 1; j < last; j++) {
      if (stack.indexOf(j) !== -1) continue
      const chk1 = routes[j][0] <= start && start <= routes[j][1]
      const chk2 = routes[j][0] <= end && end <= routes[j][1]
      if (chk1 || chk2) {
        chk = true
        stack.push(j)
        if (stack.length === last) {
          cnt += 1
          break loop
        }
      }
    }
    if (chk) cnt += 1
  }
  return cnt
}

//console.log(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]), 2)
//console.log(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]), 2)
//console.log(solution([[-2, -1], [1, 2], [-3, 0]]), 2)
console.log(solution([[-20, 15], [-20, -15], [-20, -15], [-18, -13], [-5, -3]]), 2)