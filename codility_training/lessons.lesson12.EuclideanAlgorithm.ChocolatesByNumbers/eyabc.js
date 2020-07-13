// 초콜릿을 먹는 index만 보면 0부터 시작해서 N과 M의 최대 공약수의 배수(< N) 라고 합니다.
function solution (N, M) {
  const gcd = (a, b) => a % b === 0 ? b : gcd(b, a % b);
  return ~~(N / gcd(N, M));
}
console.log(
  solution(10, 4),
  solution(30, 120)
);
