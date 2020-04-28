function solution(A) {
  const aLen = A.length;
  A.sort((a,b) => a-b);
  for(let i = 0; i < aLen ;) {
    if (A[i] !== ++i) return 0;
  }
  return 1;
}
console.log(
  solution( [4, 1, 3, 2]) === 1,
  solution([4, 1, 3]) === 0
);