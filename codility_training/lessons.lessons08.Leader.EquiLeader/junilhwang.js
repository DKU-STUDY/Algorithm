function solution(A) {
  if (A.length < 2) return 0
  let shift = A.shift()
  const FO = { [shift]: 1 }, BO = {}
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

    FO[shift] = (FO[shift] || 0) + 1;
    BO[shift] -= 1
    FC += 1
    BC -= 1

    BLMax = BO[BL]
    if (FO[shift] > FLMax) ([FL, FLMax] = [shift, FO[shift]]);

    cnt += (FLMax > FC / 2 && BLMax > BC / 2 && ~~FL === ~~BL)
  }
  return cnt
}

const assert = require('assert').strict
require("./test.json").forEach(({ input, output }) => {
  assert.deepEqual(solution(...input), output)
})