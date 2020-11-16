function s (prices) {
  const a = []
  const stack = [prices.pop()]
  const plen = prices.length
  let i = 1
  while (i <= plen) {
    const p = prices.pop()
    let j = 1, cnt = 0
    while (j <= i && stack[i - j] >= p) cnt++, j++
    if (j <= i && stack[i - j] < p) cnt += 1
    stack.push(p)
    a[plen - i] = cnt
    i++
  }
  a[plen] = 0
  return a
}

console.log(s([100, 200, 300, 400, 500, 100, 200, 50]))