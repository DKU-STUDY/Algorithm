/**
 * https://programmers.co.kr/learn/courses/30/lessons/12943
 * 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다.
 *
 1-1. 입력된 수가 짝수라면 2로 나눕니다.
 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
 * @param num , 1 이상 8000000 미만인 정수
 * @return num 을 위 작업을 몇 번 반복해야 1로 만들 수 있는지 횟수를 반환함.
 *   작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환
 */
const isEven = (num) => num % 2 === 0;

// 1-1. 입력된 수가 짝수라면 2로 나눕니다.
// 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
const process = (num) => isEven(num) ? num / 2 : num * 3 + 1;

function solution(num) {
  let [cnt, number] = [0, num];

  // 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
  while (number !== 1) {
    number = process(number);

    // 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환
    if (cnt++ === 500) return -1;
  }
  return cnt;
}


console.log(solution(6) === 8);
console.log(solution(16) === 4);
console.log(solution(626331) === -1);

// 옛날에 푼것
function solution2(num) {
  let times = 0;
  while (num !== 1) {
    num = num % 2 ? num * 3 + 1 : num / 2;
    times++;
    if (times === 500) return -1;
  }
  return times;
}