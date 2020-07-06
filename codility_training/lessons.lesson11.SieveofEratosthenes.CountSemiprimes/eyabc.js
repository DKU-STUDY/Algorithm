function solution (N, P, Q) {
  const semiCnt = new Array(N + 1).fill(0),
    maxNum = N + 1;

  const isPrime = (i) => {
    for (let j = 2 ; j * j <= i ; j++)
      if (i % j === 0) return false;
    return true;
  };

  // 참고함
  const isSemi = (num) => {
    let cnt = 0;
    for (let i = 2 ; cnt < 2 && i * i <= num ; ++i)
      while (num % i === 0)
        num /= i, ++cnt; // Increment count of prime numbers

    // If number is greater than 1, add it to
    // the count variable as it indicates the
    // number remain is prime number
    if (num > 1)
      ++cnt;

    // 나누어 지는 수가 2개 초과면 semi 가 아니다.
    return cnt === 2;
  };

  for (let i = 1 ; i < maxNum ; i++)
    semiCnt[i] = semiCnt[i - 1] + (isPrime(i) ? 0 : isSemi(i) ? 1 : 0);

  return P.map((start, k) => semiCnt[Q[k]] - semiCnt[start - 1]);
}


console.log(
  solution(26, [1, 4, 16], [26, 10, 20]).toString() === [10, 4, 0].toString(),
  solution(50, [1, 2, 3, 4, 10], [50, 49, 48, 40, 30]).toString() === [17, 17, 16, 15, 7].toString(),
);