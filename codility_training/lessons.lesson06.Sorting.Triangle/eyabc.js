function solution(A) {
  A.sort((a, b) => a - b);
  const aLen = A.length - 2;
  for (let i = 0 ; i < aLen; i++) {
    const a = A[i], b = A[i + 1], c = A[i+2];
    if (a + b > c && b + c > a && a + c > b) return 1;
  }
  return 0;
}

console.log(solution([10, 2, 5, 1, 8, 20]) === 1);
console.log(solution([10, 50, 5, 1]) === 0);
