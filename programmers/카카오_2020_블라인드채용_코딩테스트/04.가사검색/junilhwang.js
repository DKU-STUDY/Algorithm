function solution(words, queries) {
  const n = queries.map(v => 0)
  const len = words.length 
  for (let i = 0; i < len; i++) {
    const v = words[i]
    queries.forEach((reg, k) => {
      const len = v.length
      if (len !== queries[k].length) return
      const a = v, b = queries[k]
      let chk = true
      for (let i = 0; i < len; i++) {
        if (b[i] === '?' || b[i] === a[i]) continue
        chk = false
        break
      }
      if (chk) n[k] += 1
    })
  }
  return n;
}

console.log(
  solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["fro??", "????o", "fr???", "fro???", "pro?"]
  ), [3, 2, 4, 1, 0]
)