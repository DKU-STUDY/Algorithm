/**
 * https://programmers.co.kr/learn/courses/30/lessons/12948
 *
 * @param phone_number, 전화번호 문자열 , 길이 4 ~ 20
 * @return 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열
 */
function solution(phone_number) {
  const len = phone_number.length;
  if (len === 4) return phone_number;

  const standard = len - 4;
  return ''.padEnd(standard, '*')
    + phone_number.slice(standard, len);
}

// 프로그래머스 정규식
function hide_numbers(s) {
  return s.replace(/\d(?=\d{4})/g, "*");
}

// 프로그래머스 repeat
function hide_numbers(s){
  return "*".repeat(s.length - 4) + s.slice(-4);
}

console.log(solution('01033334444') === '*******4444');
console.log(solution('027778888') === '*****8888');
console.log(solution('2777') === '2777');

// 옛날에 푼 것
function solution2(phone_number) {
  let len = phone_number.length;
  return Array(len - 3).join('*') + phone_number.slice(len - 4, len);
}
