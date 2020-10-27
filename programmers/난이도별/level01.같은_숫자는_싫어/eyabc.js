/**
 * https://programmers.co.kr/learn/courses/30/lessons/12906
 * @param arr
  : 배열 arr의 크기 : 1,000,000 이하의 자연수
 : 배열 arr의 원소의 크기 : 0~ 9 정수
 * @return rr 에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하고 남은 수들을 return
 */
function solution(arr) {
  return arr.filter((num, i) => num !== arr[i + 1]);
}

console.log(solution([1, 1, 3, 3, 0, 1, 1])); //	[1,3,0,1]
console.log(solution([4, 4, 4, 3, 3])); //[4,3]

// 옛날에 푼것
function solution2(arr) {
  return arr.filter((i, k) => {
    return i !== arr[k + 1];
  });
}