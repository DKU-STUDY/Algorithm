/**
 * https://programmers.co.kr/learn/courses/30/lessons/12947
 * 하샤드 수: x의 자릿수의 합으로 x가 나누어져야 합니다.
 * @param x, 1 ~ 10000 정수
 * @return 자연수 x를 입력받아 x가 하샤드 수인지 boolean
 */

  // 자리수의 합을 구하는 함수
const positionSum = (num) => [...String(num)].reduce((sum, num) => sum + Number(num), 0);

function solution(x) {
  return x % positionSum(x) === 0;
}

console.log(solution(10) === true);
console.log(solution(12) === true);
console.log(solution(11) === false);
console.log(solution(13) === false);


// 옛날에 푼 것
function solution2(x) {
  return x % ((x + '').split('').reduce((a, b) => +a + +b)) === 0;
}