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

  console.log(numberStack, operStack)

  const sums = ['+*-','+-*','-*+','-+*','*-+','*+-'].map(v => {
    const stack1 = []
    const stack2 = []
    const opers = [ ...v ]
    while (operStack.length) {
      let start = operStack.indexOf(opers[0])
      console.log(start, opers[0])
      while (start !== -1) {
        numberStack[start] = `${numberStack[start]}${opers[0]}${numberStack[start + 1]}`
        numberStack.splice(start + 1, 1)
        operStack.splice(start, 1)
      }
      console.log(numberStack, operStack)
      return false
    }
  })
  console.log(sums)
}

console.log(
  solution("100-200*300-500+20") ===60420,
  //solution("50*6-3*2") === 300,
)