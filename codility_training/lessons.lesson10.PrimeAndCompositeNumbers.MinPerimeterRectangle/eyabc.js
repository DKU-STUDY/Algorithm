// 최소 공약수의 쌍중 갭이 가장 작은 것의 둘레를 구한다
function solution (N) {
  for (let a = ~~Math.sqrt(N); a > 0; a--) {
    if (!(N % a)) { 
      const b = N / a;
      return 2 * (a + b);
    }
  }
}

console.log(solution(982451653))
console.log(solution(10000000000))
console.log(solution(1))
