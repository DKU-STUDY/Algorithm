function solution (user_id, banned_id) {
  const regs = banned_id.map(v => new RegExp('^' + v.replace(/\*/g, '.') + '$'))
  const set = new Set()
  const arr = regs.map(v => user_id.filter(v2 => v.test(v2)))
  const len = arr.length
  const resolve = []
  const f = (index, stack) => {
    if (stack.length === arr.length) {
      const res = stack.sort((a, b) => a > b ? 1 : -1).join(',')
      if (!resolve.includes(res)) {
        resolve.push(res)
      }
    }
    if (index === len) return
    arr[index].forEach(v => {
      if (!stack.includes(v)) {
        f(index + 1, [...stack, v])
      }
    })
  }
  f(0, [])
  return resolve.length
}

console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]) === 2)
console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]) === 2)
console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]) === 3)