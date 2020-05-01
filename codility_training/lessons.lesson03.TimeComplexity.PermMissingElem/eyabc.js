function solution(A) {
  if (!A) return 1;
  const len = A.length + 1;
  let i = 0;
  A.sort((a, b) => a - b);

  for(; i < len; i++) {
    if(A[i] > (i+1)) return A[i]-1;
    if(A[i] < (i+1)) return A[i]+1;
  }
  return i;
}

/* from JeongShin */
function solution2(A) {
  if (!A) return;
  const len = A.length + 1;
  //원래 예상 합
  const x = (1 + len) / 2 * len;
  //현재 배열 합
  const y = A.reduce((sum, curr) => sum + curr);
  //missing num = 예상 합 - 현재 합
  return x - y;
}
console.log(
  solution2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]) === 11,
  solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]) === 11
);
