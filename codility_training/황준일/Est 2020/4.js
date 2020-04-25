function solution (S, C) {
  const obj = {}
  const company = C.toLowerCase()
  return S.split(';').map(v => {
    const name = v.trim()
    const vArr = name.toLowerCase().replace(/\-/g, '').split(' ')
    let id = `${vArr.pop()}_${vArr[0]}`
    obj[id] = (obj[id] || 0) + 1
    if (obj[id] > 1) id += obj[id]
    return `${name} <${id}@${company}.com>`
  }).join('; ')
}


const C = "Example"

const S = "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker"
const resolve = `John Doe <doe_john@example.com>; Peter Benjamin Parker <parker_peter@example.com>; Mary Jane Watson-Parker <watsonparker_mary@example.com>; John Elvis Doe <doe_john2@example.com>; John Evan Doe <doe_john3@example.com>; Jane Doe <doe_jane@example.com>; Peter Brian Parker <parker_peter2@example.com>`
// console.log(solution(S, C) === resolve)

const S2 = "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker-a-b-c; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker"
const resolve2 = `John Doe <doe_john@example.com>; Peter Benjamin Parker <parker_peter@example.com>; Mary Jane Watson-Parker-a-b-c <watsonparkerabc_mary@example.com>; John Elvis Doe <doe_john2@example.com>; John Evan Doe <doe_john3@example.com>; Jane Doe <doe_jane@example.com>; Peter Brian Parker <parker_peter2@example.com>`
// console.log(solution(S2, C) === resolve2)

const S3 = "John Doe; Peter Benjamin Parker P2 P3 P4; Mary Jane Watson-Parker-a-b-c; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker"
const resolve3 = `John Doe <doe_john@example.com>; Peter Benjamin Parker P2 P3 P4 <p4_peter@example.com>; Mary Jane Watson-Parker-a-b-c <watsonparkerabc_mary@example.com>; John Elvis Doe <doe_john2@example.com>; John Evan Doe <doe_john3@example.com>; Jane Doe <doe_jane@example.com>; Peter Brian Parker <parker_peter@example.com>`
console.log(solution(S3, C) === resolve3)