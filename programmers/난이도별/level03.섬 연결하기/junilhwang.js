// 탐욕법 > 섬 연결하기 : https://programmers.co.kr/learn/courses/30/lessons/42861?language=javascript
function solution(n, costs) {
  costs.sort((a, b) => a[2] - b[2])
  let min = 0, cnt = 0
  const node = [...Array(n).keys()]
  const chk = ([x, y]) => {
    if (node[x] === node[y]) return false
    const [small, big]  = node[x] < node[y] ? [node[x], node[y]] : [node[y], node[x]]
    node.forEach((v, k) => { if ( v === big ) node[k] = small })
    return true
  }
  for (const [x, y, t] of costs) {
    if (!chk([x, y])) continue
    min += t, cnt += 1
    if (cnt === n) break
  }
  return min
}

// console.log(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]), 4)
// console.log(solution(5, [[0, 1, 1], [0, 2, 2], [1, 3, 2], [3, 4, 1]]), 6)
// console.log(solution(6, [[0, 1, 1], [0, 2, 2], [1, 3, 2], [3, 4, 1], [3, 5, 1], [4, 5, 2]]), 7)
// console.log(solution(5, [[0,1,1],[0,2,2],[0,3,1],[1,4,1],[1,2,2],[3,4,1]]), 5)
// console.log(solution(6, [[0, 1, 1], [0, 5, 2], [1, 2, 1], [1, 3, 1], [1, 4, 1], [2, 5, 1]]), 5)
// console.log(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]), 11)
console.log(solution(7, [[0, 1, 29], [1, 2, 16], [2, 3, 12], [3, 4, 22], [4, 5, 27], [5, 0, 10], [6, 1, 15], [6, 3, 18], [6, 4, 25]]), 10 + 27 + 22 + 15 + 12 + 16)