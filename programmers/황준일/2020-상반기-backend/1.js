function solution (P, S) {
  return [ ...P ].reduce((sum, p, k) => {
    const s = S.charAt(k)
    const [big, small] = [ Math.max(p, s), Math.min(p, s) ]
    return sum + Math.min(big - small, (small + 10) - big)
  }, 0)
}

console.log(solution("82195", "64723") === 13)
console.log(solution("00000000000000000000", "91919191919191919191") === 20)