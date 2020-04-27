function solution(A) {
  A.sort();
  const len = A.length;
  for (let i = 0; i < len; i += 2) {
    if (A[i] != A[i + 1]) return A[i];
  }
}
