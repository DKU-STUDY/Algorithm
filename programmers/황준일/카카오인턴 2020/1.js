function solution (board, moves) {
  const b = []
  const arr = board.map((v, x) => {
    return v.reduce((arr, v2, y) => {
      const n = board[y][x]
      if (n !== 0) arr.push(n)
      return arr
    }, [])
  })
  let resolve = 0;
  moves.forEach(v => {
    const n = arr[v - 1].shift()
    if (n !== undefined) {
      const before = b.pop()  
      if (before === undefined) {
        b.push(n)
      } else if (before !== n) {
        b.push(before, n)
      } else if (before === n) {
        resolve += 2
      }
    }
  })
  return resolve
}


console.log(
  solution(
    [
      [0,0,0,0,0],
      [0,0,1,0,3],
      [0,2,5,0,1],
      [4,2,4,4,2],
      [3,5,1,3,1]
    ],
    [1,5,3,5,1,2,1,4]
  ) === 4
)