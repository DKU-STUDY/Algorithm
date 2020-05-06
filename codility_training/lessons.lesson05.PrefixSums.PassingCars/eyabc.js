function solution(A) {
  let count = 0, res = 0;
  const aLen = A.length - 1;
  for(let i = aLen; i > -1; i--) {
    if (A[i] === 0) res += count;
    if (A[i] === 1) count++;
  }
  return res < 1000000001 ? res : -1;
}
console.log(
  solution([0, 1, 0, 1, 1]) === 5
);