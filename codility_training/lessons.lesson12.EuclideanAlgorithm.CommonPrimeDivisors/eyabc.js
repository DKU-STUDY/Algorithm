function solution (A, B) {
  const getGCD = (a, b) => a % b === 0 ? b : getGCD(b, a % b);
  return A.reduce((cnt, a, k) => {
    let b = B[k];
    let gcd = getGCD(a, b);
    let gcdA = 0, gcdB = 0;

    while (gcdA !== 1) {
      gcdA = getGCD(a, gcd);
      a = a / gcdA;
    }

    while (gcdB !== 1) {
      gcdB = getGCD(b, gcd);
      b = b / gcdB;
    }

    return cnt + (a + b === 2);
  }, 0);
}

console.log(
  solution([15, 10, 9], [75, 30, 5]) === 1,
  solution([1], [1]) === 1,
  solution([3, 9, 20, 11], [9, 81, 5, 13]) === 2,
)
;