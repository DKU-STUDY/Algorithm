function solution(A) {
  if (A.length < 2) return 0
  const FO = { [A[0]]: 1 }, BO = {}
  let FLMax = 1, BLMax = 0,
      FC = 1, BC = A.length - 1,
      FL = A[0], BL
  for (let i = 1; A[i] !== undefined; i++) {
    const v = A[i]
    BO[v] = (BO[v] || 0) + 1
    BLMax = Math.max(BLMax, BO[v])
    if (BO[v] > BC / 2) BL = v
  }

  let cnt = (~~FL === ~~BL) * 1
  for (let i = 1; A[i] !== undefined; i++) {
    const v = A[i]
    FO[v] = (FO[v] || 0) + 1;
    BO[v] -= 1
    FC += 1
    BC -= 1

    BLMax = BO[BL]
    if (FO[v] > FLMax) ([FL, FLMax] = [v, FO[v]]);

    cnt += (FLMax > FC / 2 && BLMax > BC / 2 && ~~FL === ~~BL)
  }
  return cnt
}

const assert = require('assert').strict
require("./test.json").forEach(({ input, output }) => {
  assert.deepEqual(solution(...input), output)
})