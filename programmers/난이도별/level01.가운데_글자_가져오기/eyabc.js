/**
 * https://programmers.co.kr/learn/courses/30/lessons/12903
 * @param s 길이가 1 이상, 100이하인 스트링
 * @return s 의 가운데 글자를 반환하는 함수, 짝수라면 가운데 두 글자를 반환
 */
function solution(s) {
  const middle = s.length / 2;
  const floor = ~~middle;
  return (Number.isInteger(middle) ? s[floor - 1] : '') + s[floor];
}

console.log(solution('abcde') === 'c');
console.log(solution('qwer') === 'we');

// 옛날에 푼 것
function solution2(s) {
  let a = Math.floor(s.length / 2);
  if (s.length % 2 === 1) {
    return s.slice(a, a + 1);
  } else {
    return s.slice(a - 1, a + 1);
  } // '홀' : '짝'
}