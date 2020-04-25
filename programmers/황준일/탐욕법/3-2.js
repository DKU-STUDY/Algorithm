function solution(number, k) {
  const stack = [number[0]], last = number.length, len = last - k
  let i = 1, j = 0, n = k
  do {
    if (n && stack[j] < number[i]) {
      stack.pop(), j--, n--
      continue
    }
    stack.push(number[i++]), j++
  } while (j < len || i < last)
  return stack.slice(0, len).join('')
}

//console.log(solution("1924", 2), "94")
//console.log(solution("1231234", 3), "3234")
//console.log(solution("4177252841", 4), "775841")
console.log(solution("12345654654321", 10), "6654")