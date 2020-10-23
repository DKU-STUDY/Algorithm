/** https://programmers.co.kr/learn/courses/30/lessons/12921
 * 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수,
 * 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다. (1은 소수가 아닙니다.)
 * n은 2이상 1000000이하의 자연수입니다.
 * @param n
 * @return
 */

function solution(n) {
  const N = n + 1;

  // 해당 수가 소수인지 아닌지를 기록하는 표(배열을 만듭니다)
  // n 이 10 이라면 [false,.... 가 11개 존재합니다.] 0 은 사용하지 않는 인덱스 입니다.
  const primeTable = new Array(N).fill(false);

  const max = Math.sqrt(N);

  // 2부터 Math.sqrt(N) 까지 수가 소수인지 판별하는 로직 입니다.
  // 1 은 소수가 아니므로 2 부터 셉니다.
  for (let i = 2 ; i < max ; i++) {

    // 만약 셀려는 값의 인덱스가 true 이면, 해당 수는 이미 어떤 소수의 배수이므로, 해당 수의 배수가 되는 수를 찾을 필요가 없습니다.
    if (primeTable[i]) continue;

    // 해당 수가 소수일 경우, 해당 수의 배수가 되는 수는 모두 소수가 아니므로 true 로 바꾸어 줍니다.
    for (let j = i + i ; j < N ; j += i) {
      primeTable[j] = true;
    }
  }

  // primeTable 에서 false (소수인 수) 의 수를 셉니다. 2를 빼는 이유는 0 과 1 인덱스는 소수가 아니기 때문입니다.
  return primeTable.filter((n) => !n).length - 2;
}
/*
 테스트 1 〉	통과 (0.06ms, 30.1MB)
 테스트 2 〉	통과 (0.12ms, 30MB)
 테스트 3 〉	통과 (0.16ms, 30MB)
 테스트 4 〉	통과 (0.26ms, 30.3MB)
 테스트 5 〉	통과 (0.18ms, 30.1MB)
 테스트 6 〉	통과 (1.03ms, 29.9MB)
 테스트 7 〉	통과 (0.43ms, 30.3MB)
 테스트 8 〉	통과 (0.85ms, 29.9MB)
 테스트 9 〉	통과 (1.11ms, 30.2MB)
 테스트 10 〉	통과 (25.18ms, 35.2MB)
 테스트 11 〉	통과 (31.86ms, 40.5MB)
 테스트 12 〉	통과 (14.56ms, 35.7MB)
 효율성  테스트
 테스트 1 〉	통과 (33.26ms, 41.1MB)
 테스트 2 〉	통과 (32.92ms, 41.1MB)
 테스트 3 〉	통과 (33.98ms, 41.1MB)
 테스트 4 〉	통과 (32.76ms, 40.9MB)
 */
console.log(solution(10) === 4);
console.log(solution(5) === 3);

// 옛날에 푼 것
function solution2(n) {
  const arr = [];
  for (let i = 0 ; i < n ; i++) arr.push(i + 1);
  delete arr[0];
  const max = Math.sqrt(n);
  for (let i = 2 ; i <= max ; i++) {
    if (arr[i - 1]) for (let j = i + i ; j <= n ; j += i) delete arr[j - 1];
  }
  return arr.filter(v => v).length;
}

/*

 테스트 1 〉	통과 (1.69ms, 37.3MB)
 테스트 2 〉	통과 (1.71ms, 37.2MB)
 테스트 3 〉	통과 (1.79ms, 37.3MB)
 테스트 4 〉	통과 (1.84ms, 37.4MB)
 테스트 5 〉	통과 (1.81ms, 37.5MB)
 테스트 6 〉	통과 (3.10ms, 37.6MB)
 테스트 7 〉	통과 (2.09ms, 37.8MB)
 테스트 8 〉	통과 (2.69ms, 37.5MB)
 테스트 9 〉	통과 (3.27ms, 37.6MB)
 테스트 10 〉	통과 (42.28ms, 46.9MB)
 테스트 11 〉	통과 (128.40ms, 69.2MB)
 테스트 12 〉	통과 (45.19ms, 46.9MB)
 효율성  테스트
 테스트 1 〉	통과 (129.85ms, 69.1MB)
 테스트 2 〉	통과 (127.70ms, 68.9MB)
 테스트 3 〉	통과 (130.71ms, 69.2MB)
 테스트 4 〉	통과 (129.56ms, 69MB)
 */