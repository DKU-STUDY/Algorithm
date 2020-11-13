/**
 * https://programmers.co.kr/learn/courses/30/lessons/12932
 * n이 12345이면 [5,4,3,2,1]을 리턴
 제한 조건
 n은 10,000,000,000이하인 자연수입니다.
 * @param n | 자연수
 * @return n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴
 */
function solution(n) {
  const N = n.toString();
  return [...N].reduceRight((arr, num) => {
    arr.push(Number(num));
    return arr;
  }, []);
}

/*
 테스트 1 〉	통과 (0.07ms, 30.2MB)
 테스트 2 〉	통과 (0.09ms, 29.8MB)
 테스트 3 〉	통과 (0.07ms, 30.1MB)
 테스트 4 〉	통과 (0.08ms, 30.1MB)
 테스트 5 〉	통과 (0.09ms, 30.1MB)
 테스트 6 〉	통과 (0.07ms, 30MB)
 테스트 7 〉	통과 (0.07ms, 30MB)
 테스트 8 〉	통과 (0.07ms, 30.4MB)
 테스트 9 〉	통과 (0.07ms, 29.7MB)
 테스트 10 〉	통과 (0.07ms, 29.9MB)
 테스트 11 〉	통과 (0.07ms, 30.3MB)
 테스트 12 〉	통과 (0.08ms, 30.2MB)
 테스트 13 〉	통과 (0.07ms, 30.2MB)

 */

console.log(
  solution(12345) === [5, 4, 3, 2, 1],
);

function solution2(n) {
  return n.toString()
          .split('')
          .reverse()
          .map((Number));
}

/*
 테스트 1 〉	통과 (0.07ms, 30.2MB)
 테스트 2 〉	통과 (0.06ms, 29.6MB)
 테스트 3 〉	통과 (0.06ms, 29.9MB)
 테스트 4 〉	통과 (0.05ms, 30.1MB)
 테스트 5 〉	통과 (0.06ms, 30MB)
 테스트 6 〉	통과 (0.07ms, 30.1MB)
 테스트 7 〉	통과 (0.06ms, 30MB)
 테스트 8 〉	통과 (0.06ms, 30.1MB)
 테스트 9 〉	통과 (0.08ms, 30.3MB)
 테스트 10 〉	통과 (0.07ms, 30.1MB)
 테스트 11 〉	통과 (0.05ms, 30.3MB)
 테스트 12 〉	통과 (0.06ms, 29.9MB)
 테스트 13 〉	통과 (0.06ms, 29.9MB)
 */