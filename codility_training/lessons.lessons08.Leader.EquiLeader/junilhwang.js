function solution(A) {
  let shift = A.shift()
  const front = [ shift ]
  const FO = {}
  const BO = { [shift]: 1 }
  let BLMax = 1, FLMax = 0,
      BC = 1, FC = A.length - 1,
      BL = shift, FL
  for (let i = 0; A[i] !== undefined; i++) {
    const v = A[i]
    FO[v] = (FO[v] || 0) + 1
    FLMax = Math.max(FLMax, FO[v])
    if (FLMax > FC / 2) FL = v
  }

  let cnt = (~~FL === ~~BL) * 1


  console.log(front, A)
  while (A[1] !== undefined) {

    shift = A.shift()
    front.push(shift)

    console.log(front, A)

    BO[shift] = (BO[shift] || 0) + 1;
    if (BO[shift] > BLMax) ([BL, BLMax] = [shift, BO[shift]]);
    BC += 1

    FO[shift] -= 1
    if (FO[shift] === 0) delete FO[shift]
    FL = Object.keys(FO).sort((a, b) => FO[b] - FO[a])[0];
    FLMax = FO[FL]
    FC -= 1

    if (BLMax < BC / 2 || FLMax < FC / 2) continue
    cnt += (~~FL === ~~BL) * 1
  }
  return cnt
}

const assert = require('assert').strict
require("./test.json").forEach(({ input, output }) => {
  assert.deepEqual(solution(...input), output)
})