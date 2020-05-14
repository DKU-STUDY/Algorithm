function solution(board) {
  const set = [ ...new Set(board) ]
  const setSize = set.length
  const place = set.map(v => [board.indexOf(v), board.lastIndexOf(v)])
  const last = Math.min(...place.pop())
  let start = 0
  for (let i = 0; place[i] !== undefined; i++) {
    const [min, max] = place[i]
    if (new Set(board.slice(min, last + 1)).size !== setSize) break
    start = Math.max(min, start)
    if (max <= last && new Set(board.slice(max, last + 1)).size === setSize) {
      start = Math.max(max, start)
    }
  }
  return [ start + 1, last + 1]
}

console.log(
  solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]).toString() === [3, 7].toString(),
  solution(["AA", "AB", "AC", "AA", "AC"]).toString() === [1, 3].toString(),
  solution(["XYZ", "XYZ", "XYZ"]).toString() === [1, 1].toString(),
  solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]).toString() === [1, 5].toString(),
)