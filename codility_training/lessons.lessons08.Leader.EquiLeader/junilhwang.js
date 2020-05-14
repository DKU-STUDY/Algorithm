function solution(A) {
  if (A.length < 2) return 0
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

  const sorted = Object.keys(BO).sort((a, b) => BO[b] - BO[a])

  let cnt = (~~FL === ~~BL) * 1

  while (A[1] !== undefined) {

    shift = A.shift()
    front.push(shift)

    FO[shift] = (FO[shift] || 0) + 1;
    if (FO[shift] > FLMax) ([FL, FLMax] = [shift, FO[shift]]);
    FC += 1

    BO[shift] -= 1
    BC -= 1
    if (BO[shift] === 0) delete BO[shift]

    if (FLMax <= FC / 2) continue;

    BL = sorted.sort((a, b) => BO[b] - BO[a])[0]
    BLMax = BO[BL]

    cnt += (BLMax > BC / 2 && ~~FL === ~~BL)
  }
  return cnt
}

const assert = require('assert').strict
require("./test.json").forEach(({ input, output }) => {
  assert.deepEqual(solution(...input), output)
})