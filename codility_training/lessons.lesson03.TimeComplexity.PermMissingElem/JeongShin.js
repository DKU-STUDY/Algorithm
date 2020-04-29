function solution(A) {
  if (!A) return;
  const len = A.length + 1;
  //원래 예상 합
  let x = ((1 + len) / 2) * len;
  //현재 배열 합
  const y = A.reduce((sum, curr) => sum + curr, 0);
    return sum + curr;
  }, 0);
  //missing num = 예상 합 - 현재 합
  return x - y;
}
