function solution(expression) {
  const numberStack = []
  const operStack = []
  const opers = ['+', '-', '*']
  const len = expression.length
  let n = 0
  let token = ''
  while (n < len) {
    const c = expression.charAt(n)
    if (opers.indexOf(c) !== -1) {
      if (token.length) {
        numberStack.push(token)
        token = ''
      }
      operStack.push(c)
    } else {
      token += c
    }
    n++
  }
  if (token.length) numberStack.push(token)

  const sums = ['+*-','+-*','-*+','-+*','*-+','*+-'].map(v => {
    const opers = [ ...v ]
    const oStack = [ ...operStack ]
    const nStack = [ ...numberStack ]
    while (opers.length !== 0) {
      const oper = opers.shift()
      let idx = oStack.indexOf(oper)
      while (idx !== -1) {
        const exp = `${nStack[idx]} ${oper} ${nStack[idx + 1]}`
        nStack[idx] = eval(exp)
        nStack.splice(idx + 1, 1)
        oStack.splice(idx, 1)
        idx = oStack.indexOf(oper)
      }
    }
    return Math.abs(nStack.pop())
  })
  return Math.max(...sums)
}

console.log(
  solution("100-200*300-500+20") ===60420,
  solution("50*6-3*2") === 300,
)