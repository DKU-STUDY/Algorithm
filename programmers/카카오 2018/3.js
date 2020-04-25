/**
 * N 진수 게임
 * @param  n : 진수
 * @param  t : 총 구할 갯수
 * @param  m : 참여자
 * @param  p : 내가 몇번째인지
 * @return answer : string
 */
function solution (n, t, m, p) {
  const stack = [], answer = []
  const p2 = m === p ? 0 : p
  let cnt = 0, i = 0, tCnt = 0;

  while (true) {
    if (stack.length === 0) {
      stack.push(...`${i.toString(n).toUpperCase()}`)
      i++
    }
    const number = stack.shift()
    cnt += 1;

    if ((cnt % m) === p2) {
      answer.push(number)
      tCnt += 1;
    }

    if (tCnt == t) return answer.join('')
  }
}

console.log(solution(2, 4, 2, 1) === '0111')
console.log(solution(16, 16, 2, 1) === '02468ACE11111111')
console.log(solution(16, 16, 2, 2) === '13579BDF01234567')