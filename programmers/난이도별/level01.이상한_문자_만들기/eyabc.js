/**
 * https://programmers.co.kr/learn/courses/30/lessons/12930
 제한 사항
 - 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
 - 첫번째글자인 0번째 인덱스는 짝수번째 알파벳으로 처리
 * @param s 한개 이상의 단어로 구성된 문자열. 단어는 공백 문자로 구분 됨
 * @return 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수
 */
function solution1(s) {
  return s.split(' ')
          .map((string) => {
            let even = false;
            return Array.from(string, (char) => {
              even = !even;
              return even ? char.toUpperCase() : char.toLowerCase();
            }).join('');
          }).join(' ');
}


/*
 solution2 와 다른점은 짝수인지 홀수인지 나머지 계산을 하지 않고 짝수홀수 플래그를 두었다는 것임. 큰 차이는 없음
 테스트 1 〉	통과 (0.13ms, 30MB)
 테스트 2 〉	통과 (0.12ms, 30.2MB)
 테스트 3 〉	통과 (0.13ms, 30.3MB)
 테스트 4 〉	통과 (0.21ms, 30.1MB)
 테스트 5 〉	통과 (0.15ms, 30.2MB)
 테스트 6 〉	통과 (0.11ms, 30.1MB)
 테스트 7 〉	통과 (0.12ms, 30.2MB)
 테스트 8 〉	통과 (0.21ms, 30MB)
 테스트 9 〉	통과 (0.17ms, 30MB)
 테스트 10 〉	통과 (0.22ms, 30.2MB)
 테스트 11 〉	통과 (0.20ms, 30MB)
 테스트 12 〉	통과 (0.20ms, 30.1MB)
 테스트 13 〉	통과 (0.18ms, 30.2MB)
 테스트 14 〉	통과 (0.08ms, 30.1MB)
 테스트 15 〉	통과 (0.17ms, 30MB)
 테스트 16 〉	통과 (0.17ms, 29.9MB)
 */
console.log(solution('try hello world') === 'TrY HeLlO WoRlD');

function solution2(s) {
  return s.split(' ').map(v => Array.from(v.toUpperCase()).map((c, k) => k % 2 ? c.toLowerCase() : c).join('')).join(' ');
}

/*
 테스트 1 〉	통과 (0.12ms, 30.3MB)
 테스트 2 〉	통과 (0.09ms, 30.2MB)
 테스트 3 〉	통과 (0.10ms, 30.2MB)
 테스트 4 〉	통과 (0.17ms, 29.8MB)
 테스트 5 〉	통과 (0.14ms, 30.2MB)
 테스트 6 〉	통과 (0.10ms, 30MB)
 테스트 7 〉	통과 (0.10ms, 29.9MB)
 테스트 8 〉	통과 (0.17ms, 29.7MB)
 테스트 9 〉	통과 (0.14ms, 29.9MB)
 테스트 10 〉	통과 (0.20ms, 30MB)
 테스트 11 〉	통과 (0.18ms, 30.4MB)
 테스트 12 〉	통과 (0.16ms, 30.1MB)
 테스트 13 〉	통과 (0.11ms, 30.1MB)
 테스트 14 〉	통과 (0.10ms, 30.3MB)
 테스트 15 〉	통과 (0.11ms, 30MB)
 테스트 16 〉	통과 (0.14ms, 30MB)
 */

function solution3(s) {
  let even = false;
  return Array.from(s, (char) => {
    if (char === ' ') {
      even = false;
      return char;
    }
    even = !even;
    return even ? char.toUpperCase() : char.toLowerCase();
  }).join('');
}

/*
 세번째 방법은 split 나 join 을 한단계 줄였다. 큰 차이는 없음
 테스트 1 〉	통과 (0.11ms, 30.2MB)
 테스트 2 〉	통과 (0.08ms, 30.2MB)
 테스트 3 〉	통과 (0.09ms, 30.1MB)
 테스트 4 〉	통과 (0.15ms, 30.1MB)
 테스트 5 〉	통과 (0.13ms, 30.3MB)
 테스트 6 〉	통과 (0.08ms, 30.2MB)
 테스트 7 〉	통과 (0.09ms, 30MB)
 테스트 8 〉	통과 (0.15ms, 30.1MB)
 테스트 9 〉	통과 (0.12ms, 30.1MB)
 테스트 10 〉	통과 (0.17ms, 30.2MB)
 테스트 11 〉	통과 (0.15ms, 30.2MB)
 테스트 12 〉	통과 (0.14ms, 30.1MB)
 테스트 13 〉	통과 (0.14ms, 30.1MB)
 테스트 14 〉	통과 (0.10ms, 30.3MB)
 테스트 15 〉	통과 (0.11ms, 30.1MB)
 테스트 16 〉	통과 (0.14ms, 30MB)
 */

function solution5(s) {
  let even = false;
  let newStr = '';
  Array.prototype.forEach.call(s, (char) => {
    if (char === ' ') {
      even = false;
      newStr += ' ';
      return char;
    }
    even = !even;
    newStr += even ? char.toUpperCase() : char.toLowerCase();
  });
  return newStr;
}

function solution4(s) {
  let even = false;
  let newStr = '';
  Array.prototype.forEach.call(s, (char) => {
    if (char === ' ') {
      even = false;
      newStr += ' ';
      return char;
    }
    newStr += (even = !even) ? char.toUpperCase() : char.toLowerCase();
  });
  return newStr;
}
/*
 새 문자열을 만드는 방법
 테스트 1 〉	통과 (0.11ms, 30.1MB)
 테스트 2 〉	통과 (0.09ms, 30.2MB)
 테스트 3 〉	통과 (0.09ms, 30.1MB)
 테스트 4 〉	통과 (0.15ms, 30MB)
 테스트 5 〉	통과 (0.10ms, 30.1MB)
 테스트 6 〉	통과 (0.09ms, 30.4MB)
 테스트 7 〉	통과 (0.10ms, 30.1MB)
 테스트 8 〉	통과 (0.15ms, 30.2MB)
 테스트 9 〉	통과 (0.11ms, 30.2MB)
 테스트 10 〉	통과 (0.15ms, 30.1MB)
 테스트 11 〉	통과 (0.14ms, 30.2MB)
 테스트 12 〉	통과 (0.10ms, 29.9MB)
 테스트 13 〉	통과 (0.13ms, 30.3MB)
 테스트 14 〉	통과 (0.11ms, 29.9MB)
 테스트 15 〉	통과 (0.12ms, 30.1MB)
 테스트 16 〉	통과 (0.14ms, 30.1MB)
 */