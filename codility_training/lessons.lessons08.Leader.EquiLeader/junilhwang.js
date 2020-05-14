function solution(A) {
  let shift = A.shift()
  const front = [ shift ]
  const FO = { [shift]: 1 }
  const BO = {}
  const capture = []
  let FLMax = 1, BLMax = 0,
      FC = 1, BC = A.length,
      FL = shift, BL
  for (let i = 0; A[i] !== undefined; i++) {
    const v = A[i]
    BO[v] = (BO[v] || 0) + 1
    BLMax = Math.max(BLMax, BO[v])
    if (BO[v] > BC / 2) BL = v
  }


  let cnt = (~~FL === ~~BL) * 1

  while (A[1] !== undefined) {

    shift = A.shift()
    front.push(shift)

    FO[shift] = (FO[shift] || 0) + 1;
    if (FO[shift] > FLMax) ([FL, FLMax] = [shift, FO[shift]]);
    FC += 1

    BO[shift] -= 1
    if (BO[shift] === 0) delete BO[shift]
    BL = Object.keys(BO).sort((a, b) => BO[b] - BO[a])[0];
    BLMax = BO[BL]
    BC -= 1

    if (BLMax > BC / 2 && FLMax > FC / 2 && ~~FL === ~~BL) {
      cnt += 1
    }
  }
  return cnt
}

const assert = require('assert').strict
require("./test.json").forEach(({ input, output }) => {
  assert.deepEqual(solution(...input), output)
})