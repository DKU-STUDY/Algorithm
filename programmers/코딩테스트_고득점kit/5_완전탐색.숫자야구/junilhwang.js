// https://programmers.co.kr/learn/courses/30/lessons/42841

function solution(baseball) {
  let answer = 0
  let nums = [1,2,3,4,5,6,7,8,9]
  const ball = baseball.filter(v => {
    const x = Array.from(`${v[0]}`).map(v => v*1)
    if (x.indexOf(0) !== -1 || x.length !== 3) return false
    if (v[1] + v[2] === 0) {
      nums = nums.filter(n => x.indexOf(n) === -1)
      return false
    }
    return true
  })
  const chk = nArr => {
    for (const [x, y, z] of ball) {
      let yChk = 0, zChk = 0
      const xArr = Array.from(x+'').map(v => v*1)
      if (xArr[0] === nArr[0]) yChk++;
      if (xArr[1] === nArr[1]) yChk++;
      if (xArr[2] === nArr[2]) yChk++;
      if (yChk !== y) return
      if (nArr[0] === xArr[1] || nArr[0] === xArr[2]) zChk++
      if (nArr[1] === xArr[0] || nArr[1] === xArr[2]) zChk++
      if (nArr[2] === xArr[1] || nArr[2] === xArr[0]) zChk++
      if (zChk !== z) return
      //console.log(nArr, x, y, yChk, z, zChk)
    }
    answer++
  }
  const f = p => {
    if (p.length === 3) {
      chk(p)
      return
    }
    nums.forEach(v => { if (p.indexOf(v) === -1) f([...p, v]) })
  }
  f([])
  return answer
}

console.log(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]), 2)
//console.log(solution([[123, 0, 0], [456, 3, 0]]), 1)
