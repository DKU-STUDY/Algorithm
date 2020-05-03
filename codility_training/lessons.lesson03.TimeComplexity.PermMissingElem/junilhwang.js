function solution(A) {
  let sum1 = 0, sum2 = 0
  const last = A.length + 1;
  for (let i = 1; i < last; i++) {
    sum1 += i
    sum2 += A[i - 1]
  }
  return sum1 - sum2 + last
}

function solution2(A) {
  return A.findIndex((v, k) => v !== k+1) + 1
}

console.log(
  solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]) === 11,
  solution2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]) === 11,
);
