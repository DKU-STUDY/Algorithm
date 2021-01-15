function solution(n) {
  return Number((n + "").split('').sort((a, b) => b-a).join(''));
}

// 문제풀이: 
// 스트링으로 변환 후 => (n + "") 
// 한 글자씩 배열로 변환 => split('')
// 큰 숫자순으로 정렬 => sort((a,b) => b-a)
// 배열을 스트링으로 변환 -> join('')
// 스트링으로 숫자로 변환 -> Number(num)
