function solution(A) {
  const arr = [], len = A.length;
  for (let i = 0; i < len; i++) {
    if (!arr[A[i]]) arr[A[i]] = 1;
    else arr[A[i]]++;
    if (arr[A[i]] > len / 2) return i;
  }
  return -1;
}
console.log(
  solution([3, 4, 3, 2, 3, -1, 3, 3]),
  solution([2, 1, 1, 3, 4] ),
  solution([1, 2, 1]),
  solution([3, 2, 1]),
  solution([2147483647] )
);