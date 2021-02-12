// https://programmers.co.kr/learn/courses/30/lessons/42842
function solution (b, r) {
  let s = b+r, n = ~~Math.sqrt(s), w = n, h = n
  const f = (w, h, bChk = w * 2 + h * 2 - 4, rChk = w * h - bChk) => bChk === b && rChk === r
  while (w >= h && !f(w, h)) w*h < s ? w++ : h--
  return [w, h]
}

//console.log(solution(10,2), [4, 3])
//console.log(solution(8,1), [3, 3])
//console.log(solution(24,24), [8, 6])
const arr = [
  [6, 4], [5, 5], [4, 4], [361, 360]
]
arr.forEach(([w, h]) => {
  const b = w * 2 + h * 2 - 4
  const r = w * h - b
  console.log(solution(b, r), [w, h])
})