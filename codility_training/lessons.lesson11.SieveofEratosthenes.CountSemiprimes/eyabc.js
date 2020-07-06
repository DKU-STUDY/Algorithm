function solution (N, P, Q) {
  const 소수배열 = (() => {
    const arr = [];
    for (let i = 1 ; i <= N ; i++) {
      let isPrime = true;
      for (let j = 2; j * j <= i ; j++) {
        if (i % j === 0) {
          isPrime = false;
          break;
        }
      }
      if (isPrime) arr.push(i)
    }
    return arr;
  })();

  const 세미프라임_판별 = (num) => 소수배열.indexOf(num) !== -1;

  console.log({ 소수배열 });

  const 약수배열 = (v) => {
    let divisor = [];
    for (let j = 2 ; j * j <= v ; j++) {
      if (v % j === 0 && 세미프라임_판별(j) && 세미프라임_판별(v / j)) {
        divisor.push(j);
        divisor.push(v / j);
      }
    }
    return divisor;
  };

  const res = P.map((start, k) => {
    const end = Q[k];
    let cnt = 0;

    for (let i = start ; i <= end ; i++) {
      if (!소수배열.includes(i) && 약수배열(i).length) {
        cnt++;
      }
    }
    return cnt;
  });
  console.log({ res });
  return res;
}


console.log(
  solution(26, [1, 4, 16], [26, 10, 20]).toString() === [10, 4, 0].toString(),
  solution(50, [1, 2, 3, 4, 10], [50, 49, 48, 40, 30]).toString() === [17, 17, 16, 15, 7].toString(),
);