function solution (s) {
  const arr = eval(s.replace(/{/g, '[').replace(/}/g, ']'))
  arr.sort((a, b) => a.length - b.length)
  const resolve = [arr.shift()[0]]
  arr.forEach(v => {
    while (v.length > 1) {
      const index = v.findIndex(v2 => resolve.includes(v2))
      v.splice(index, 1)
    }
    resolve.push(v.pop())
  })
  return resolve
}

console.log(
  solution("{{2},{2,1},{2,1,3},{2,1,3,4}}").toString() === [2, 1, 3, 4].toString()
)
console.log(
  solution("{{1,2,3},{2,1},{1,2,4,3},{2}}").toString() === [2, 1, 3, 4].toString()
)
console.log(
  solution("{{20,111},{111}}").toString() === [111, 20].toString()
)
console.log(
  solution("{{123}}").toString() === [123].toString()
)
console.log(
  solution("{{4,2,3},{3},{2,3,4,1},{2,3}}").toString() === [3, 2, 4, 1].toString()
)
console.log(
  solution("{{2},{2,1},{2,1,3},{2,1,3,4},{2,1,3,4,2}}").toString() === [2, 1, 3, 4, 2].toString()
)
console.log(
  solution("{{2},{22},}").toString() === [2, 1, 3, 4, 2].toString()
)