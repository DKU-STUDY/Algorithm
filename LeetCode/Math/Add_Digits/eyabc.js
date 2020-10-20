/**
 * https://leetcode.com/problems/add-digits/
 * @param {number} num, 음이 아닌 정수
 * @return {number} num 의 모든 자리수를 더한다. 더한 수가 한자리수가 될 때 까지 반복한다. 그리고 한자리수의 결과를 리턴한다.
 * 방법 1 2 모두 92 ~ 100 ms 사이에서 동작함	40.1 MB
 */

// 문자열로 자리수를 끊어서 더하는 방법
const addDigits = function(num) {
  let sum = num;
  while (true) {
    if (sum < 10) return sum;
    sum = [...String(sum)].reduce((sum, v) => Number(v) + sum, 0);
    //    sum = [...String(sum)].map(Number)
    //                           .reduce((sum, v) => v + sum, 0); 하고도 시간이 거의 같다.
  }
};

// 숫자를 10으로 나머지를 계속 더하는 방법
const addDigits2 = function(num) {
  let result = num;

  while (true) {
    if (result < 10) return result;
    result = (result % 10) + ~~(result / 10);
  }
};

console.log(addDigits(38) === 2);