// https://programmers.co.kr/learn/courses/30/lessons/42839
function solution(numbers) {
  const arr = Array.from(numbers)
  const answer = new Set();
  const f = n => {
    if (n < 2) return false
    for (let i = 2; i <= ~~(n / 2); i++) if (n % i === 0) return false
    return true
  }
  const len = arr.length
  const f2 = p => {
    const n = p.map(k => arr[k]).join('')*1
    if (f(n))  answer.add(n)
    if (p.length === len) return
    arr.forEach((v, k) => {if (p.indexOf(k) === -1) f2([...p, k])})
  }
  arr.forEach((v, k) => f2([k]))
  return answer.size;
}

console.log(solution("17"), 3)
console.log(solution("011"), 2)