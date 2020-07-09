function solution(s) {
  const stack = []
  const len = s.length
  let min = len
  loop: for (let i = 1; i < ~~(len/2) + 1; i++) {
    let word = s.substr(0, i), temp = '', cnt = 1, j = i
    while (true) {
      const next = s.substr(j, i)
      if (word === next) {
        cnt += 1
      } else {
        temp += `${cnt > 1 ? cnt : ''}${word}`
        word = next
        cnt = 1
      }
      if (temp.length > min) continue loop
      if (j > len) break
      j+=i
    }
    //console.log(i, min, temp)
    if (min > temp.length) min = temp.length
  }
  return min;
}

// console.log(solution("aabbaccc"), 7)
// console.log(solution("ababcdcdababcdcd"), 9)
// console.log(solution("abcabcdede"), 8)
// console.log(solution("abcabcabcabcdededededede"), 14)
// console.log(solution("xababcdcdababcdcd"), 17)