/*
  일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다.
  그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다.
  이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다.
  이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

  1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
  2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
  3. 그렇지 않으면 J를 인쇄합니다.
*/

function solution(priorities, location) {
    const queue = priorities.map((v, k) => ({v, k}))
    let i = 1;
    while (queue.length) {
      const target = queue.shift()
      const chk = queue.find(q => q.v > target.v)
      if (chk) {
        queue.push(target)
      } else {
        if (~~location === ~~target.k) return i
        i++
      }
    }
    return 0;
}

console.log(solution([2, 1, 3, 2],2))
console.log(solution([1, 1, 9, 1, 1, 1],0))