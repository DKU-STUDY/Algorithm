function solution(n, weak, dist) {
  weak.sort((a, b) => a - b)
  dist.sort((a, b) => b - a)
  const len = dist.length
  const chk = a => {
    
  }
  const f = (a, last) => {
    chk(a)
    for (let i = last + 1; i < len; i++) {
      f([...a, i], i)
    }
  }
  for (let i = 0; i < len; i++) f([i], i)
  return -1;
}

console.log(solution(12,	[1, 5, 6, 10], [1, 2, 3, 4]),2)
//console.log(solution(12,	[1, 3, 4, 9, 10],	[3, 5, 7]),1)