/**
 * https://programmers.co.kr/learn/courses/30/lessons/12944
 *
 * @param arr, 정수를 담고 있는 배열
 * @return 배열 arr의 평균값
 *
 arr은 길이 1 이상, 100 이하인 배열입니다.
 arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
 */
console.log(solution([1, 2, 3, 4]) === 2.5);
console.log(solution([5, 5]) === 5);

function solution(arr) {
  return arr.reduce((sum, num) => sum + num) / arr.length;
}

// 옛날에 푼 것
function solution2(arr) {
  var answer = 0;
  arr.forEach(e => {
    answer += e;
  });
  return answer / arr.length;
}