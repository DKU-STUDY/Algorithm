function solution (N, P, Q) {
  const semiCnt = new Array(N + 1).fill(0),
    maxNum = N + 1;
  // 참고함
  const isSemi = (num) => {
    let cnt = 0;
    for (let i = 2 ; cnt < 2 && i * i <= num ; ++i)
      while (num % i === 0) num /= i, ++cnt;
    if (num > 1) ++cnt;
    return cnt === 2;
  };

  for (let i = 1 ; i < maxNum ; i++)
    semiCnt[i] = semiCnt[i - 1] + (isSemi(i) ? 1 : 0);

  return P.map((start, k) => semiCnt[Q[k]] - semiCnt[start - 1]);
}


console.log(
  solution(26, [1, 4, 16], [26, 10, 20]).toString() === [10, 4, 0].toString(),
  solution(50, [1, 2, 3, 4, 10], [50, 49, 48, 40, 30]).toString() === [17, 17, 16, 15, 7].toString(),
);