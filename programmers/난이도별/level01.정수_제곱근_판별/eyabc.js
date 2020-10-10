/**
 * https://programmers.co.kr/learn/courses/30/lessons/12934
 제한 사항
 n은 1이상, 50000000000000 이하인 양의 정수입니다.
 * @param n , 양의 정수
 * @return n이 어떤 양의 정수 x의 제곱인지 아닌지 판단
 x+1의 제곱을 리턴 : n이 양의 정수 x의 제곱이라면
 -1을 리턴 : n이 양의 정수 x의 제곱이 아니라면
 */

function solution(n) {
  const sqrt = n ** 0.5;
  return (sqrt - ~~sqrt) === 0 ? (sqrt + 1) ** 2 : -1;
}

function solution2(n) {
  const sqrt = Math.sqrt(n);
  return (sqrt - ~~sqrt) === 0 ? (sqrt + 1) ** 2 : -1;
}
/**
 * 테스트 1 〉	통과 (0.04ms, 30MB)
 테스트 2 〉	통과 (0.04ms, 30.1MB)
 테스트 3 〉	통과 (0.04ms, 30.1MB)
 테스트 4 〉	통과 (0.04ms, 30.4MB)
 테스트 5 〉	통과 (0.04ms, 30.2MB)
 테스트 6 〉	통과 (0.04ms, 30.1MB)
 테스트 7 〉	통과 (0.06ms, 30.1MB)
 테스트 8 〉	통과 (0.05ms, 29.9MB)
 테스트 9 〉	통과 (0.04ms, 30MB)
 테스트 10 〉	통과 (0.03ms, 30.1MB)
 테스트 11 〉	통과 (0.05ms, 30.1MB)
 테스트 12 〉	통과 (0.04ms, 30.3MB)
 테스트 13 〉	통과 (0.03ms, 30MB)
 테스트 14 〉	통과 (0.04ms, 29.9MB)
 테스트 15 〉	통과 (0.06ms, 30MB)
 테스트 16 〉	통과 (0.05ms, 30.1MB)
 테스트 17 〉	통과 (0.05ms, 29.8MB)
 테스트 18 〉	통과 (0.05ms, 29.9MB)
 */
console.log(
  solution(121) === 144,
  solution(3) === -1,
);

function solution2(n) {
  let a = Math.sqrt(n);
  return Math.floor(a) - a < 0 ? -1 : (a + 1) * (a + 1);
}