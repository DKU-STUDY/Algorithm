/**
 * https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3
 *
 * @param phone_book 전화번호부에 적힌 전화번호를 담은 배열
 * @return 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return
 *
 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

 구조대 : 119
 박준영 : 97 674 223
 지영석 : 11 9552 4421

 phone_book의 길이는 1 이상 1,000,000 이하입니다.
 각 전화번호의 길이는 1 이상 20 이하입니다.
 */
function solution(phone_book) {
  const len = phone_book.length + 1;

  // sort 를 먼저 하면 유사한 phone 과 더 먼저 비교를 할 수 있습니다.
  phone_book.sort();

  // 접두사를 포함하는지 검사합니다. 접두사를 포함하면 반복문을 종료하고 true 를 리턴합니다.
  const hasPrefix = (phone, i) => {

    // phone 으로 시작하는 다른 phone 이 있는지 검사하는 정규식을 수행합니다.
    const regex = new RegExp(`^${phone}`);
    for (let j = i + 1 ; j < len ; j++)
      if (regex.test(phone_book[j])) return true;
  };

  return !phone_book.some(hasPrefix);
}


function solution2(phone_book) {
  const len = phone_book.length + 1;

  const hasPrefix = (phone, i) => {

    const regex = new RegExp(`^${phone}`);
    for (let j = i + 1 ; j < len ; j++)
      if (regex.test(phone_book[j])) return true;
  };

  return !phone_book.some(hasPrefix);
}


console.log(solution(['119', '97674223', '1195524421']) === false);
console.log(solution(['123', '456', '789']) === true);
console.log(solution(['12', '123', '1235', '567', '88']) === false);