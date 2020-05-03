function solution(A) {
  if (!A) return;
  const len = A.length + 1;
  //원래 예상 합
  const x = (1 + len) / 2 * len;
  //missing num = 예상 합 - 현재 합
  return x - A.reduce((a, b) => a + b);
}
