function solution(A) {
  const back = [ A.pop() ]
  const FO = {}
  const BO = { [back[0]]: 1 }
  let BLMax = 1, FLMax = 0,
      BC = 1, FC = A.length - 1,
      BL = back[0], FL
  for (let i = 0; A[i] !== undefined; i++) {
    const v = A[i]
    FO[v] = (FO[v] || 0) + 1
    FLMax = Math.max(FLMax, FO[v])
    if (FLMax > FC / 2) FL = v
  }

  let cnt = (FL === BL) * 1

  while (A[0] !== undefined) {
    const v = A.pop()

    BO[v] = (BO[v] || 0) + 1;
    if (BO[v] > BLMax) ([BL, BLMax] = [v, BO[v]]);
    BC += 1

    FO[v] -= 1
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
  assert.deepEqual(solution(...input), 2)
})