function solution (office, r, c, move) {
  let direction = 0
  const len = office.length
  const go = () => {
    const tmp = [r, c]
    switch (direction) {
      case 0: r -= 1; break;
      case 1: c += 1; break;
      case 2: r += 1; break;
      case 3: c -= 1; break;
    }
    if (Math.max(r, c) >= len || Math.min(r, c) < 0 || office[r][c] < 0) {
      ([r, c] = tmp)
    }
  }
  const left = () => direction = direction === 0 ? 3 : direction - 1
  const right = () => direction = (direction + 1) % 4

  return move
    .reduce((stack, v) => {
      ({ go, left, right })[v]();
      const pos = `${r},${c}`
      if (stack.indexOf(pos) === -1) stack.push(pos)
      return stack
    }, [ `${r},${c}` ])
    .reduce((sum, v) => {
      const [r, c] = v.split(',')
      return sum + office[r][c]
    }, 0)
}

console.log(
  solution([[5,-1,4],[6,3,-1],[2,-1,1]], 1, 0, ['go','go','right','go','right','go','left','go']) === 14
)