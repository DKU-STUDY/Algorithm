// 최소 공약수의 쌍중 갭이 가장 작은 것의 둘레를 구한다
function solution (N) {
  const getPerimeter = (a, b) => 2 * (a + b);
  let a = ~~Math.sqrt(N);
  let b;

  for (;a > 0; a--) {
    if (Number.isInteger(N / a)) {
      b = N / a;
      break;
    }
  }
  return getPerimeter(a, b);
}

console.log(solution(982451653))
console.log(solution(10000000000))
console.log(solution(1))

