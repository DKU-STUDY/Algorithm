function solution(A) {
  let pop = A.pop()
  const FO = {}
  const BO = { [pop]: 1 }
  let BLMax = 1, FLMax = 0,
      BC = 1, FC = A.length - 1,
      BL = pop, FL
  for (let i = 0; A[i] !== undefined; i++) {
    const v = A[i]
    FO[v] = (FO[v] || 0) + 1
    FLMax = Math.max(FLMax, FO[v])
    if (FLMax > FC / 2) FL = v
  }

  let cnt = (FL === BL) * 1

  while (A[1] !== undefined) {
    pop = A.pop()

    BO[pop] = (BO[pop] || 0) + 1;
    if (BO[pop] > BLMax) ([BL, BLMax] = [pop, BO[pop]]);
    BC += 1

    FO[pop] -= 1
    if (FO[pop] === 0) delete FO[pop]
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