/**
 * https://programmers.co.kr/learn/courses/30/lessons/12910
 * @param arr : 자연수를 담은 배열
 *     arr[i] ≠ arr[j]
 *     길이 1 이상인 배열
 * @param divisor : 자연수
 * @return divisors 로 나누어 떨어지는 원소를 오름차순으로 정렬한 배열
 *  divisor로 나누어 떨어지는 element가 하나도 없다면 [-1]
 */
function solution(arr, divisor) {
  const result = arr.filter((num) => num % divisor === 0);
  return result.length > 0 ? result.sort((a, b) => a - b) : [-1];
}

console.log(solution([5, 9, 7, 10], 5)); //[5, 10]
console.log(solution([2, 36, 1, 3], 1)); //[1, 2, 3, 36]
console.log(solution([3, 2, 6], 10)); //[-1]

// 옛날에 푼 것
function solution2(arr, divisor) {
  var answer = [];
  answer = arr.filter(i => i % divisor === 0).sort((a, b) => a - b);
  if (answer.length === 0) {
    return [-1];
  }
  return answer;
}