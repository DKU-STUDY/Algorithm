/**
 * https://programmers.co.kr/learn/courses/30/lessons/12928
 * 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수
 * 제한 사항 | n은 0 이상 3000이하인 정수입니다.
 * @param n
 */
function solution(n) {
  if (n < 2) return n;

  let ans = 0;

  const max = Math.sqrt(n);

  // n 의 최대  Math.sqrt(n); 으로 나눈다.
  for (let i = 2 ; i <= max ; i++) {

    // 약수가 아닌 경우
    if ((n % i) !== 0) continue;

    // q 는 몫
    const q = n / i;

    // 나누는 수와 몫이 같을 때 ? 9 의 3 * 3 일 때
    if (i === q) {
      ans += i;
      break;
    }
    ans = ans + i + q;
  }
  return 1 + n + ans;
}

/*
 테스트 1 〉	통과 (0.06ms, 30MB)
 테스트 2 〉	통과 (0.07ms, 30.3MB)
 테스트 3 〉	통과 (0.07ms, 30.3MB)
 테스트 4 〉	통과 (0.07ms, 30.2MB)
 테스트 5 〉	통과 (0.07ms, 30.1MB)
 테스트 6 〉	통과 (0.07ms, 29.9MB)
 테스트 7 〉	통과 (0.08ms, 29.8MB)
 테스트 8 〉	통과 (0.07ms, 30.1MB)
 테스트 9 〉	통과 (0.07ms, 30.2MB)
 테스트 10 〉	통과 (0.07ms, 30.1MB)
 테스트 11 〉	통과 (0.08ms, 30.2MB)
 테스트 12 〉	통과 (0.05ms, 30MB)
 테스트 13 〉	통과 (0.07ms, 30.3MB)
 테스트 14 〉	통과 (0.07ms, 30.3MB)
 테스트 15 〉	통과 (0.07ms, 30.1MB)
 테스트 16 〉	통과 (0.06ms, 30MB)
 테스트 17 〉	통과 (0.07ms, 30.2MB)
 */

console.log(
  solution(0) === 0,
  solution(1) === 1,
  solution(2) === 3,
  solution(12) === 28,
  solution(5) === 6,
  solution(9) === 13,
);


// 옛날에 푼 것
function solution2(n) {
  var answer = n;
  let i = 2;
  if (n > 1) {
    answer += 1;
    for (; i < n ; i++) {
      n % i === 0 ? answer += i : '';
    }
  }
  return answer;
}

/*
 통과 (1.67ms, 37.3MB)
 테스트 2 〉	통과 (1.68ms, 37.2MB)
 테스트 3 〉	통과 (1.66ms, 37.4MB)
 테스트 4 〉	통과 (1.70ms, 37.3MB)
 테스트 5 〉	통과 (1.70ms, 37.6MB)
 테스트 6 〉	통과 (1.66ms, 37.2MB)
 테스트 7 〉	통과 (1.71ms, 37.2MB)
 테스트 8 〉	통과 (1.68ms, 37.3MB)
 테스트 9 〉	통과 (1.69ms, 37.3MB)
 테스트 10 〉	통과 (1.72ms, 37.4MB)
 테스트 11 〉	통과 (1.69ms, 37.5MB)
 테스트 12 〉	통과 (1.73ms, 37.3MB)
 테스트 13 〉	통과 (1.63ms, 37.2MB)
 테스트 14 〉	통과 (1.66ms, 37.4MB)
 테스트 15 〉	통과 (1.70ms, 37.6MB)
 테스트 16 〉	통과 (1.63ms, 37.2MB)
 테스트 17 〉	통과 (1.74ms, 37.3MB)
 */