/**
 * https://programmers.co.kr/learn/courses/30/lessons/12940
 * @param n
 * @param m
 * @return 두 수를 입력받아 두수의 [최대 공약수, 최소 공배수]
 * 두 수는 1이상 1000000이하의 자연수입니다.

 * 유클리드 호제법  https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95
 * 2개의 자연수의 최대공약수를 구하는 알고리즘의 하나이다.
 * 호제법이란 말은 두 수가 서로(互) 상대방 수를 나누어(除)서 결국 원하는 수를 얻는 알고리즘을 나타낸다.
 * 2개의 자연수 a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a > b),
 * a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 이 성질에 따라,
 * b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.
 */
const getGCD = (n, m) => {
  let [q, r] = [n, m].sort((a, b) => b - a);

  while (true) {
    const [newQ, newR] = [r, (q % r)];
    if (newR === 0)
      return r;
    [r, q] = [newR, newQ];
  }
};

const getLCD = (n, m, gcd) => n * m / gcd;

function solution(n, m) {
  if (n === m) return [n, m];

  const gcd = getGCD(n, m);
  const lcd = getLCD(n, m, gcd);

  return [gcd, lcd];
};

console.log(solution(3, 12), [3, 12]);
console.log(solution(2, 5), [1, 10]);
console.log(solution(104, 1000000), [1, 2]);
console.log(solution(78696, 19332), [36, 2]);

// 옛날에 푼 것
function solution2(n, m) {
  let i = 2, max = 1;
  if (n === m) {
    return [n, n];
  }
  while (i < n + m) {
    (n % i === 0) && (m % i === 0) ? max = i : '';
    i++;
  }
  let min = n * m / max;
  return [max, min];
}