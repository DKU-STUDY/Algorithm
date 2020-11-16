function solution(n, build_frame) {
  var answer = [], stack = [], nodeA = [], nodeB = [];
  // a {0 - 기둥, 1 - 보}, b {0 - 삭제, 1 - 설치}
  build_frame.forEach(([x, y, a, b]) => {
    if (b === 0) {
      const idx = answer.findIndex(([x2, y2, a2]) => {
        return (x2 === x && y2 === y && a2 === a) 
      })
      answer.splice(idx, 1)
    } else {
      if (y === 0 && a === 1) return
      if (a === 1) {
        if (nodeA[y] === undefined) {
          nodeA[y][x] = nodeA[y][x+1] = x
        } else {
          switch (true) {
            case nodeA[y][x] === undefined && nodeA[y][x + 1] === undefined:
              nodeA[y][x] = nodeA[y][x + 1] = x
            break
            case nodeA[y][x] !== undefined && nodeA[y][x + 1] === undefined:
              nodeA[y][x+1] = nodeA[y][x]
            break
            case nodeA[y][x] === undefined && nodeA[y][x + 1] !== undefined:
              nodeA[y][x] = nodeA[y][x+1]
            break
          }
        }
      }
      answer.push([x, y, a])
    }
  })
  answer.sort((a, b) => a[0] - b[0])
  return answer;
}

/* console.log(
  solution(
    5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
  ), [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]
) */
console.log(
  solution(
    5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
  ), [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]]
)